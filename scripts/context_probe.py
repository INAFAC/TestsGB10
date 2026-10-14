#!/usr/bin/env python3
"""Synthetic cold-prefix context/concurrency test against an existing vLLM server.

Uses token IDs, not meaningful conversations. Never changes the server.
Writes incremental measurements so an externally timed-out test is reviewable.
"""
import argparse
import concurrent.futures
import json
import pathlib
import random
import re
import subprocess
import threading
import time
import urllib.request


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--base-url', default='http://127.0.0.1:8000')
    p.add_argument('--model', default='nvidia/Qwen3.8-27B-NVFP4')
    p.add_argument('--concurrency', type=int, required=True)
    p.add_argument('--requests', type=int, help='Total requests; defaults to concurrency')
    p.add_argument('--input-tokens', type=int, required=True)
    p.add_argument('--output-tokens', type=int, default=256)
    p.add_argument('--seed', type=int, default=19000)
    p.add_argument('--result', required=True)
    a = p.parse_args()
    count = a.requests or a.concurrency
    dest = pathlib.Path(a.result)
    dest.parent.mkdir(parents=True, exist_ok=True)
    samples, results = [], []
    stop = threading.Event()
    start = time.monotonic()
    gpu_last = {'at': 0, 'gib': None}

    def metrics():
        raw = urllib.request.urlopen(a.base_url+'/metrics', timeout=10).read().decode()
        d = {'timestamp': time.time()}
        for key in ['num_requests_running', 'num_requests_waiting',
                    'kv_cache_usage_perc', 'num_preemptions_total',
                    'prefix_cache_queries_total', 'prefix_cache_hits_total']:
            values = re.findall(r'^vllm:'+key+r'(?:\{[^\n]*\})? ([^\n]+)', raw, re.M)
            d[key] = sum(float(v) for v in values)
        mem = {line.split(':')[0]: int(line.split()[1])
               for line in pathlib.Path('/proc/meminfo').read_text().splitlines()
               if line.startswith(('MemAvailable:', 'MemTotal:'))}
        d['mem_available_gib'] = mem['MemAvailable']/1048576
        d['mem_total_gib'] = mem['MemTotal']/1048576
        d['system_used_percent'] = 100*(1-mem['MemAvailable']/mem['MemTotal'])
        if time.monotonic()-gpu_last['at'] >= 5:
            try:
                raw_gpu = subprocess.check_output(['nvidia-smi',
                    '--query-compute-apps=process_name,used_memory',
                    '--format=csv,noheader,nounits'], text=True, timeout=5)
                values = [float(line.rsplit(',', 1)[1].strip()) for line in raw_gpu.splitlines()
                          if 'VLLM::EngineCore' in line and 'N/A' not in line]
                gpu_last['gib'] = sum(values)/1024 if values else None
            except Exception:
                gpu_last['gib'] = None
            gpu_last['at'] = time.monotonic()
        d['gpu_engine_gib'] = gpu_last['gib']
        d['gpu_engine_percent'] = None if gpu_last['gib'] is None else 100*gpu_last['gib']/d['mem_total_gib']
        return d

    def monitor():
        while not stop.is_set():
            try:
                samples.append(metrics())
            except Exception as e:
                samples.append({'timestamp': time.time(), 'error': str(e)})
            stop.wait(1)

    def request_one(index):
        rng = random.Random(a.seed+index)
        payload = {'model': a.model,
                   'prompt': [rng.randrange(1000, 30000) for _ in range(a.input_tokens)],
                   'max_tokens': a.output_tokens, 'ignore_eos': True,
                   'temperature': 0, 'stream': True,
                   'stream_options': {'include_usage': True}}
        req = urllib.request.Request(a.base_url+'/v1/completions',
              data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
        started = time.monotonic()
        first, usage, finish, events = None, None, None, 0
        try:
            with urllib.request.urlopen(req, timeout=1200) as response:
                for line in response:
                    if not line.startswith(b'data: '):
                        continue
                    val = line[6:].strip()
                    if val == b'[DONE]':
                        break
                    data = json.loads(val)
                    if data.get('error'):
                        raise RuntimeError(str(data['error']))
                    if data.get('usage'):
                        usage = data['usage']
                    for choice in data.get('choices', []):
                        if choice.get('text'):
                            first = time.monotonic() if first is None else first
                            events += 1
                        if choice.get('finish_reason'):
                            finish = choice['finish_reason']
            correct = bool(usage and usage['prompt_tokens'] == a.input_tokens
                           and usage['completion_tokens'] == a.output_tokens)
            return {'index': index, 'ok': correct,
                    'ttft_s': None if first is None else first-started,
                    'total_s': time.monotonic()-started, 'usage': usage,
                    'finish_reason': finish, 'text_events': events}
        except Exception as e:
            return {'index': index, 'ok': False,
                    'total_s': time.monotonic()-started, 'error': str(e)}

    def save(status):
        valid = [s for s in samples if 'error' not in s]
        good = [r for r in results if r['ok']]
        summary = {'status': status, 'model': a.model, 'concurrency': a.concurrency, 'num_requests': count,
                   'input_tokens': a.input_tokens, 'output_tokens': a.output_tokens,
                   'seed': a.seed, 'completed': len(good),
                   'failed': len(results)-len(good), 'duration_s': time.monotonic()-start,
                   'mean_ttft_s': sum(r['ttft_s'] or 0 for r in good)/max(1, len(good)),
                   'mean_total_s': sum(r['total_s'] for r in good)/max(1, len(good)),
                   'peak_kv_fraction': max((s['kv_cache_usage_perc'] for s in valid), default=None),
                   'peak_running': max((s['num_requests_running'] for s in valid), default=None),
                   'peak_waiting': max((s['num_requests_waiting'] for s in valid), default=None),
                   'preemptions': valid[-1]['num_preemptions_total']-valid[0]['num_preemptions_total'] if valid else None,
                   'prefix_cache_queries': valid[-1]['prefix_cache_queries_total']-valid[0]['prefix_cache_queries_total'] if valid else None,
                   'prefix_cache_hits': valid[-1]['prefix_cache_hits_total']-valid[0]['prefix_cache_hits_total'] if valid else None,
                   'min_available_gib': min((s['mem_available_gib'] for s in valid), default=None)}
        for field in ['gpu_engine_gib', 'gpu_engine_percent', 'system_used_percent']:
            summary['peak_'+field] = max((s[field] for s in valid if s.get(field) is not None), default=None)
        dest.write_text(json.dumps({'summary': summary, 'requests': list(results),
                                   'metrics': list(samples)}, indent=2))
        return summary

    samples.append(metrics())
    watcher = threading.Thread(target=monitor, daemon=True)
    watcher.start()
    print('START '+str(dest), flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.concurrency) as pool:
        pending = {pool.submit(request_one, i) for i in range(count)}
        last = 0
        while pending:
            done, pending = concurrent.futures.wait(pending, timeout=5,
                            return_when=concurrent.futures.FIRST_COMPLETED)
            for f in done:
                result = f.result()
                results.append(result)
                print('REQUEST '+json.dumps(result), flush=True)
            summary = save('running')
            elapsed = time.monotonic()-start
            if elapsed-last >= 30:
                last = elapsed
                print('PROGRESS '+json.dumps(summary), flush=True)
    stop.set()
    watcher.join(timeout=12)
    samples.append(metrics())
    print('DONE '+json.dumps(save('complete')), flush=True)


if __name__ == '__main__':
    main()
