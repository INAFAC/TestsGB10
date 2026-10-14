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
    check = kw.pop('check', False)
    process = subprocess.Popen(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kw)
    try:
        output, _ = process.communicate()
    except BaseException:
        try:
            process.communicate(timeout=120)
        except subprocess.TimeoutExpired:
            process.terminate()
            process.communicate(timeout=30)
        raise
    if check and process.returncode:
        raise subprocess.CalledProcessError(process.returncode, args, output=output)
    return subprocess.CompletedProcess(args, process.returncode, stdout=output)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--compose', default='/home/canadas/ai/vllm/compose.yaml')
    p.add_argument('--results', required=True)
    p.add_argument('--profiles-file', help='JSON list of [memory_fraction, max_num_seqs, test_cases]')
    p.add_argument('--reuse-initial', action='store_true', help='Use the first profile if the restored running server already matches')
    p.add_argument('--wait-for', help='Baseline result file that must exist before changing settings')
    p.add_argument('--wait-metadata', help='Wait until another matrix metadata reports healthy restoration')
    p.add_argument('--mode', choices=['memory', 'concurrency', 'after30'], default='memory')
    a = p.parse_args()
    root = pathlib.Path(a.results)
    root.mkdir(parents=True, exist_ok=True)
    base = pathlib.Path(a.compose)
    original = base.read_bytes()
    inspect = json.loads(sh(['docker', 'inspect', 'vllm-qwen38'], check=True).stdout)[0]
    original_cmd = inspect['Config']['Cmd']
    metadata = {'date': datetime.datetime.now().isoformat(), 'original_command': original_cmd,
                'model': original_cmd[2],
                'runner_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
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

    def change(fraction, max_len, max_seqs=4):
        cmd = []
        i = 0
        while i < len(original_cmd):
            if original_cmd[i] in ('--gpu-memory-utilization', '--max-model-len', '--max-num-seqs'):
                i += 2
            else:
                cmd.append(original_cmd[i]); i += 1
        cmd += ['--gpu-memory-utilization', str(fraction), '--max-model-len', str(max_len),
                '--max-num-seqs', str(max_seqs)]
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
        (0.30, [(4,8192,128), (4,32768,512), (4,65536,512), (1,130816,256)]),
        (0.50, [(4,32768,512), (4,65536,512), (4,131072,256), (1,262016,128)]),
        (0.70, [(4,65536,512), (4,131072,256), (2,262016,128)]),
        (0.85, [(4,131072,256), (4,262016,128)]),
        (0.92, [(4,131072,256), (4,262016,128)]),
    ]
    profiles = [(fraction, 4, cases) for fraction, cases in profiles]
    if a.mode == 'concurrency':
        profiles = [
            (.40, 8, [(8,1024,128), (8,8192,128), (8,32768,256)]),
            (.40, 16, [(16,1024,128), (16,8192,128)]),
        ]
    if a.mode == 'after30':
        # Complete 40% repeat before changing to the larger budgets.
        full40 = [(1,1024,128,8), (2,1024,128,8), (4,1024,128,8), (8,1024,128,8),
                  (4,8192,128,8), (4,32768,512), (4,65536,512),
                  (4,131072,256), (1,262016,128), (4,8192,2048)]
        profiles = [(.40,4,full40),
                    (.25,4,[(4,1024,128),(4,8192,128),(4,32768,256),(1,65280,256)]),
                    (.20,4,[(1,1024,128)])] + profiles[1:] + [
            (.40,8,[(8,1024,128),(8,8192,128),(8,32768,256)]),
            (.40,16,[(16,1024,128),(16,8192,128)]),
            (.40,32,[(32,1024,128),(32,8192,128)]),
            (.40,64,[(64,1024,128),(64,8192,128)]),
            (.70,16,[(16,32768,256),(16,65536,128)]),
        ]
    if a.profiles_file:
        profiles = json.loads(pathlib.Path(a.profiles_file).read_text())
    probe = pathlib.Path(__file__).with_name('context_probe.py')
    try:
        if a.wait_metadata:
            print('WAIT_RESTORE '+a.wait_metadata, flush=True)
            while True:
                try:
                    state = json.loads(pathlib.Path(a.wait_metadata).read_text())
                    if state.get('restore_status') == 'healthy':
                        break
                except (OSError, ValueError):
                    pass
                time.sleep(5)
            # Capture the original configuration after the previous run restores it.
            inspect = json.loads(sh(['docker', 'inspect', 'vllm-qwen38'], check=True).stdout)[0]
            original_cmd = inspect['Config']['Cmd']
            metadata['original_command'] = original_cmd
            persist()
        if a.wait_for:
            print('WAIT_BASELINE '+a.wait_for, flush=True)
            while not pathlib.Path(a.wait_for).exists():
                time.sleep(5)
            # The baseline writes only after all requests have completed.
            time.sleep(3)
        for profile_index, profile in enumerate(profiles):
            fraction, max_seqs, cases = profile[:3]
            options = profile[3] if len(profile)>3 else {}
            request_timeout = options.get('request_timeout_s', 1200)
            test_timeout = options.get('test_timeout_s', 1500)
            label = 'memory-'+str(round(fraction*100))
            if max_seqs != 4:
                label += '-seqs-'+str(max_seqs)
            if request_timeout>1200:
                label += '-timeout-'+str(request_timeout)
            directory = root/label
            directory.mkdir(exist_ok=True)
            record = {'fraction': fraction, 'max_num_seqs': max_seqs, 'attempts': [], 'tests': [],
                      'request_timeout_s': request_timeout, 'test_timeout_s': test_timeout}
            metadata['profiles'].append(record)
            ready = False
            context_attempts = ([8192] if fraction == .20 else [65536,32768,8192] if fraction == .25
                                else [262144,131072,65536] if fraction == .30 else [262144])
            context_attempts = options.get('context_attempts', context_attempts)
            for max_len in context_attempts:
                print('PROFILE '+label+' max_context='+str(max_len), flush=True)
                reused = False
                if a.reuse_initial and profile_index == 0 and healthy():
                    current = json.loads(sh(['docker','inspect','vllm-qwen38'], check=True).stdout)[0]['Config']['Cmd']
                    models = json.load(urllib.request.urlopen('http://127.0.0.1:8000/v1/models', timeout=5))['data']
                    reused = (float(current[current.index('--gpu-memory-utilization')+1]) == fraction
                              and int(current[current.index('--max-num-seqs')+1]) == max_seqs
                              and models[0].get('max_model_len') == max_len)
                cmd = current if reused else change(fraction, max_len, max_seqs)
                ready, elapsed = wait_ready(label)
                raw = startup_log(directory/('startup-'+str(max_len)+'.log'))
                record['attempts'].append({'max_model_len': max_len, 'command': cmd,
                                           'ready': ready, 'startup_seconds': elapsed, 'reused_running_server': reused})
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
                record['status'] = 'startup_failed'
                persist()
                continue
            for case_index, case in enumerate(cases):
                concurrency, input_len, output_len = case[:3]
                requests = case[3] if len(case) > 3 else concurrency
                name = f'c{concurrency}-in{input_len}-out{output_len}'
                if input_len+output_len > record['max_model_len']:
                    record['tests'].append({'case': name, 'status': 'skipped_context_limit'})
                    persist(); continue
                print('TEST '+label+' '+name, flush=True)
                command = [sys.executable, '-u', str(probe), '--concurrency', str(concurrency),
                           '--requests', str(requests), '--server-max-seqs', str(max_seqs), '--memory-fraction', str(fraction),
                           '--input-tokens', str(input_len), '--output-tokens', str(output_len),
                           '--request-timeout', str(request_timeout),
                           '--test-timeout', str(test_timeout),
                           '--seed', str(50000+profile_index*1000+case_index*100),
                           '--result', str(directory/(name+'.json'))]
                started = time.monotonic()
                with (directory/(name+'.log')).open('w') as log:
                    active = subprocess.Popen(command, text=True, stdout=log, stderr=subprocess.STDOUT)
                    last = 0
                    while active.poll() is None:
                        elapsed = time.monotonic()-started
                        # A request that never enters execution is not a useful
                        # 25-minute load test. Preserve evidence and move on.
                        partial = directory/(name+'.json')
                        if elapsed > 90 and partial.exists():
                            try:
                                report = json.loads(partial.read_text())
                                s = report['summary']
                                if s.get('peak_running') == 0 and s.get('peak_waiting', 0) > 0:
                                    active.terminate()
                                    active.wait(timeout=20)
                                    s['status'] = 'not_admitted_within_90s'
                                    s['stop_reason'] = 'Waiting without any request entering execution for 90 seconds'
                                    partial.write_text(json.dumps(report, indent=2))
                                    break
                            except (ValueError, KeyError):
                                pass
                        if elapsed > test_timeout:
                            active.terminate()
                            active.wait(timeout=20)
                            if partial.exists():
                                report = json.loads(partial.read_text())
                                report['summary']['status'] = 'timeout_'+str(test_timeout)+'s'
                                report['summary']['test_timeout_s'] = test_timeout
                                partial.write_text(json.dumps(report, indent=2))
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
