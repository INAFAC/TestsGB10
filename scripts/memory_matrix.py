#!/usr/bin/env python3
"""Run authorized temporary Compose overrides; restore original command in finally.

Run on the GB10, next to context_probe.py. Source compose.yaml is never edited.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import signal
import subprocess
import sys
import time
import urllib.request


def sh(args, **kw):
    return subprocess.run(args, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, **kw)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--compose', default='/home/canadas/ai/vllm/compose.yaml')
    p.add_argument('--results', required=True)
    p.add_argument('--wait-for', help='Baseline result file that must exist before changing settings')
    a = p.parse_args()
    root = pathlib.Path(a.results)
    root.mkdir(parents=True, exist_ok=True)
    base = pathlib.Path(a.compose)
    original = base.read_bytes()
    inspect = json.loads(sh(['docker', 'inspect', 'vllm-qwen38'], check=True).stdout)[0]
    original_cmd = inspect['Config']['Cmd']
    metadata = {'date': datetime.datetime.now().isoformat(), 'original_command': original_cmd,
                'image': inspect['Config']['Image'], 'image_id': inspect['Image'],
                'compose_sha256': hashlib.sha256(original).hexdigest(),
                'restore_status': 'pending', 'profiles': []}
    def persist():
        (root/'metadata.json').write_text(json.dumps(metadata, indent=2))
    persist()
    override = root/'override.json'
    compose = ['docker', 'compose', '-f', str(base)]
    active = None

    def stopped(signum, frame):
        raise KeyboardInterrupt('Received signal '+str(signum))
    signal.signal(signal.SIGTERM, stopped)
    signal.signal(signal.SIGINT, stopped)

    def healthy():
        try:
            with urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=5) as response:
                return response.status == 200
        except Exception:
            return False

    def wait_ready(label):
        started = time.monotonic()
        last = 0
        while time.monotonic()-started < 660:
            if healthy():
                return True, time.monotonic()-started
            state = json.loads(sh(['docker', 'inspect', 'vllm-qwen38'], check=True).stdout)[0]
            if state['RestartCount'] or state['State']['Status'] in ('exited', 'dead', 'restarting'):
                return False, time.monotonic()-started
            elapsed = time.monotonic()-started
            if elapsed-last >= 30:
                print('STARTUP '+label+' '+str(round(elapsed))+'s', flush=True)
                last = elapsed
            time.sleep(5)
        return False, time.monotonic()-started

    def change(fraction, max_len):
        cmd = []
        i = 0
        while i < len(original_cmd):
            if original_cmd[i] in ('--gpu-memory-utilization', '--max-model-len'):
                i += 2
            else:
                cmd.append(original_cmd[i]); i += 1
        cmd += ['--gpu-memory-utilization', str(fraction), '--max-model-len', str(max_len)]
        override.write_text(json.dumps({'services': {'vllm': {'command': cmd}}}, indent=2))
        sh(compose+['-f', str(override), 'config', '--quiet'], check=True)
        result = sh(compose+['-f', str(override), 'up', '-d', 'vllm'], check=True)
        print(result.stdout.strip(), flush=True)
        return cmd

    def startup_log(path):
        raw = sh(['docker', 'logs', 'vllm-qwen38']).stdout
        path.write_text(raw)
        return raw

    profiles = [
        (0.30, [(4,8192,128), (4,32768,512), (4,65536,512)]),
        (0.50, [(4,32768,512), (4,65536,512), (4,131072,256)]),
        (0.70, [(4,65536,512), (4,131072,256), (2,262016,128)]),
        (0.85, [(4,131072,256), (4,262016,128)]),
    ]
    probe = pathlib.Path(__file__).with_name('context_probe.py')
    try:
        if a.wait_for:
            print('WAIT_BASELINE '+a.wait_for, flush=True)
            while not pathlib.Path(a.wait_for).exists():
                time.sleep(5)
            # The baseline writes only after all requests have completed.
            time.sleep(3)
        for profile_index, (fraction, cases) in enumerate(profiles):
            label = 'memory-'+str(round(fraction*100))
            directory = root/label
            directory.mkdir(exist_ok=True)
            record = {'fraction': fraction, 'attempts': [], 'tests': []}
            metadata['profiles'].append(record)
            ready = False
            for max_len in ([262144, 131072, 65536] if fraction == .30 else [262144]):
                print('PROFILE '+label+' max_context='+str(max_len), flush=True)
                cmd = change(fraction, max_len)
                ready, elapsed = wait_ready(label)
                raw = startup_log(directory/('startup-'+str(max_len)+'.log'))
                record['attempts'].append({'max_model_len': max_len, 'command': cmd,
                                           'ready': ready, 'startup_seconds': elapsed})
                persist()
                if ready:
                    record['max_model_len'] = max_len
                    for pattern, key in [(r'Available KV cache memory: ([\d.]+) GiB', 'kv_gib'),
                                         (r'GPU KV cache size: ([\d,]+) tokens', 'estimated_cache_tokens')]:
                        match = re.search(pattern, raw)
                        if match:
                            record[key] = float(match.group(1).replace(',', ''))
                    persist()
                    break
                sh(compose+['-f', str(override), 'stop', 'vllm'], check=True)
            if not ready:
                raise RuntimeError('Profile failed to start: '+label)
            for case_index, (concurrency, input_len, output_len) in enumerate(cases):
                name = f'c{concurrency}-in{input_len}-out{output_len}'
                if input_len+output_len > record['max_model_len']:
                    record['tests'].append({'case': name, 'status': 'skipped_context_limit'})
                    persist(); continue
                print('TEST '+label+' '+name, flush=True)
                command = [sys.executable, '-u', str(probe), '--concurrency', str(concurrency),
                           '--input-tokens', str(input_len), '--output-tokens', str(output_len),
                           '--seed', str(30000+profile_index*1000+case_index*100),
                           '--result', str(directory/(name+'.json'))]
                started = time.monotonic()
                with (directory/(name+'.log')).open('w') as log:
                    active = subprocess.Popen(command, text=True, stdout=log, stderr=subprocess.STDOUT)
                    last = 0
                    while active.poll() is None:
                        elapsed = time.monotonic()-started
                        if elapsed > 1500:
                            active.terminate()
                            active.wait(timeout=20)
                            break
                        if elapsed-last >= 30:
                            last = elapsed
                            print('TEST_PROGRESS '+label+' '+name+' '+str(round(elapsed))+'s', flush=True)
                        time.sleep(5)
                    exit_code = active.returncode
                    active = None
                record['tests'].append({'case': name, 'exit_code': exit_code,
                                        'elapsed_s': time.monotonic()-started})
                persist()
                if exit_code:
                    print('TEST_INCOMPLETE '+label+' '+name+' exit='+str(exit_code), flush=True)
                    # Do not add more load after a failed/aborted test on this profile.
                    break
                print('TEST_DONE '+label+' '+name, flush=True)
                # Capture server diagnostics without recording prompts or credentials.
                startup_log(directory/'server.log')
    finally:
        if active is not None and active.poll() is None:
            active.terminate()
            active.wait(timeout=20)
        print('RESTORE_ORIGINAL', flush=True)
        if base.read_bytes() != original:
            metadata['restore_status'] = 'blocked_source_changed'
            persist()
            raise RuntimeError('Base Compose changed externally; refusing to overwrite it')
        sh(compose+['up', '-d', 'vllm'], check=True)
        ready, elapsed = wait_ready('original-40')
        final = json.loads(sh(['docker', 'inspect', 'vllm-qwen38'], check=True).stdout)[0]
        metadata['restore_status'] = 'healthy' if ready and final['Config']['Cmd'] == original_cmd else 'failed'
        metadata['restore_seconds'] = elapsed
        metadata['restored_command'] = final['Config']['Cmd']
        startup_log(root/'restored-server.log')
        persist()
        print('RESTORED '+metadata['restore_status'], flush=True)


if __name__ == '__main__':
    main()
