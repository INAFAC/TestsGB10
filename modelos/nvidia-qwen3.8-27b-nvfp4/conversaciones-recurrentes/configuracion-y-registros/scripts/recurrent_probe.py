#!/usr/bin/env python3
"""Recurrent synthetic conversations; preserves actual generated token IDs between turns.

Uses token IDs, not meaningful conversations. Never changes the server.
Writes incremental measurements so an externally timed-out test is reviewable.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import gzip
import math
import statistics
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
    p.add_argument('--server-max-seqs', type=int, default=4)
    p.add_argument('--memory-fraction', type=float)
    p.add_argument('--input-tokens', type=int, required=True)
    p.add_argument('--output-tokens', type=int, default=256)
    p.add_argument('--seed', type=int, default=19000)
    p.add_argument('--request-timeout', type=float, default=1200, help='Maximum seconds without network data per request')
    p.add_argument('--test-timeout', type=float, help='Group timeout enforced by the external runner, for the measurement record')
    p.add_argument('--history-step', type=int, help='Step in an explicitly ordered prefix-reuse comparison')
    p.add_argument('--turns', type=int, default=3)
    p.add_argument('--think-seconds', type=float, default=30)
    p.add_argument('--new-message-tokens', type=int, default=256)
    p.add_argument('--parent-state')
    p.add_argument('--state-output', required=True)
    p.add_argument('--case-id', required=True)
    p.add_argument('--result', required=True)
    a = p.parse_args()
    count = a.concurrency*a.turns
    histories = {}
    lock = threading.Lock()
    parent = json.loads(gzip.decompress(pathlib.Path(a.parent_state).read_bytes())) if a.parent_state else None
    started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    script_sha256 = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    dest = pathlib.Path(a.result)
    dest.parent.mkdir(parents=True, exist_ok=True)
    samples, results = [], []
    try:
        models = json.load(urllib.request.urlopen(a.base_url+'/v1/models', timeout=10))['data']
        model_info = next(m for m in models if m['id'] == a.model)
    except Exception:
        model_info = {}
    stop = threading.Event()
    start = time.monotonic()
    gpu_last = {'at': 0, 'gib': None, 'temperature_c': None, 'utilization_percent': None}

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
            try:
                values = subprocess.check_output(['nvidia-smi',
                    '--query-gpu=temperature.gpu,utilization.gpu',
                    '--format=csv,noheader,nounits'], text=True, timeout=5).strip().split(',')
                gpu_last['temperature_c'] = float(values[0])
                gpu_last['utilization_percent'] = float(values[1])
            except Exception:
                pass
            gpu_last['at'] = time.monotonic()
        d['gpu_engine_gib'] = gpu_last['gib']
        d['gpu_engine_percent'] = None if gpu_last['gib'] is None else 100*gpu_last['gib']/d['mem_total_gib']
        d['gpu_temperature_c'] = gpu_last['temperature_c']
        d['gpu_utilization_percent'] = gpu_last['utilization_percent']
        return d

    def monitor():
        while not stop.is_set():
            try:
                samples.append(metrics())
            except Exception as e:
                samples.append({'timestamp': time.time(), 'error': str(e)})
            stop.wait(1)

    def request_one(user, turn, prompt):
        index = user*a.turns+turn
        payload = {'model': a.model, 'prompt': prompt,
                   'max_tokens': a.output_tokens, 'ignore_eos': True,
                   'temperature': 0, 'seed': a.seed+user,
                   'return_token_ids': True, 'stream': True,
                   'stream_options': {'include_usage': True}}
        req = urllib.request.Request(a.base_url+'/v1/completions',
              data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
        started = time.monotonic()
        first, usage, finish, events = None, None, None, 0
        generated = []
        try:
            with urllib.request.urlopen(req, timeout=a.request_timeout) as response:
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
                        generated.extend(choice.get('token_ids') or [])
                        if choice.get('text'):
                            first = time.monotonic() if first is None else first
                            events += 1
                        if choice.get('finish_reason'):
                            finish = choice['finish_reason']
            correct = bool(usage and usage['prompt_tokens'] == len(prompt)
                           and usage['completion_tokens'] == a.output_tokens and len(generated) == a.output_tokens)
            return {'index': index, 'user_id': user, 'turn': turn+1, 'input_tokens': len(prompt), 'prompt_sha256': hashlib.sha256(json.dumps(prompt,separators=(',',':')).encode()).hexdigest(), 'generated_token_ids': generated, 'ok': correct,
                    'started_at_s': started-start, 'finished_at_s': time.monotonic()-start,
                    'first_token_at_s': None if first is None else first-start,
                    'ttft_s': None if first is None else first-started,
                    'total_s': time.monotonic()-started, 'usage': usage,
                    'finish_reason': finish, 'text_events': events}
        except Exception as e:
            return {'index': index, 'user_id': user, 'turn': turn+1, 'input_tokens': len(prompt), 'prompt_sha256': hashlib.sha256(json.dumps(prompt,separators=(',',':')).encode()).hexdigest(), 'generated_token_ids': generated, 'ok': False,
                    'started_at_s': started-start, 'finished_at_s': time.monotonic()-start,
                    'first_token_at_s': None if first is None else first-start,
                    'ttft_s': None if first is None else first-started,
                    'usage': usage, 'finish_reason': finish, 'text_events': events,
                    'total_s': time.monotonic()-started, 'error': str(e), 'error_type': type(e).__name__}

    barrier = threading.Barrier(a.concurrency)
    def user_session(user):
        rng = random.Random(a.seed+user)
        history = list(parent['histories'][str(user)]) if parent else []
        if len(history)>a.input_tokens:raise ValueError('Parent history exceeds target')
        history.extend(rng.randrange(1000,30000) for _ in range(a.input_tokens-len(history)))
        barrier.wait(timeout=120)
        for turn in range(a.turns):
            if turn:
                time.sleep(a.think_seconds)
                rng_turn=random.Random(a.seed+1000000+user*100+turn)
                history.extend(rng_turn.randrange(1000,30000) for _ in range(a.new_message_tokens))
            if len(history)+a.output_tokens>model_info['max_model_len']:
                raise ValueError('Planned conversation exceeds maximum context')
            result=request_one(user,turn,history)
            with lock:results.append(result)
            print('REQUEST '+json.dumps({k:v for k,v in result.items() if k!='generated_token_ids'}),flush=True)
            if not result['ok']:return
            history.extend(result['generated_token_ids'])
        with lock:histories[str(user)]=history

    def quantile(values,p):
        values=sorted(v for v in values if v is not None)
        if not values:return None
        # Nearest-rank percentiles: p95 of 20 users is their 19th ordered value.
        return values[max(0,math.ceil(p*len(values))-1)]

    def save(status):
        with lock:captured_results=list(results)
        valid = [s for s in samples if 'error' not in s]
        good = [r for r in captured_results if r['ok']]
        if status=='complete' and len(captured_results)<count:status='finished_with_errors'
        summary = {'kind': 'recurrent', 'case_id': a.case_id, 'turns': a.turns, 'think_seconds': a.think_seconds, 'new_message_tokens': a.new_message_tokens, 'parent_state': a.parent_state, 'status': status, 'started_utc': started_utc, 'script_sha256': script_sha256, 'model': a.model, 'concurrency': a.concurrency, 'num_requests': count,
                   'server_max_num_seqs': a.server_max_seqs, 'memory_fraction': a.memory_fraction,
                   'input_tokens': a.input_tokens, 'output_tokens': a.output_tokens,
                   'seed': a.seed, 'max_model_len': model_info.get('max_model_len'),
                   'request_timeout_s': a.request_timeout,
                   'test_timeout_s': a.test_timeout,
                   'history_step': a.history_step,
                   'completed': len(good),
                   'failed': len(captured_results)-len(good), 'not_attempted': count-len(captured_results), 'duration_s': time.monotonic()-start,
                   'mean_ttft_s': sum(r['ttft_s'] or 0 for r in good)/max(1, len(good)),
                   'mean_total_s': sum(r['total_s'] for r in good)/max(1, len(good)),
                   'peak_kv_fraction': max((s['kv_cache_usage_perc'] for s in valid), default=None),
                   'peak_running': max((s['num_requests_running'] for s in valid), default=None),
                   'peak_waiting': max((s['num_requests_waiting'] for s in valid), default=None),
                   'preemptions': valid[-1]['num_preemptions_total']-valid[0]['num_preemptions_total'] if valid else None,
                   'prefix_cache_queries': valid[-1]['prefix_cache_queries_total']-valid[0]['prefix_cache_queries_total'] if valid else None,
                   'prefix_cache_hits': valid[-1]['prefix_cache_hits_total']-valid[0]['prefix_cache_hits_total'] if valid else None,
                   'min_available_gib': min((s['mem_available_gib'] for s in valid), default=None)}
        for field in ['gpu_engine_gib', 'gpu_engine_percent', 'system_used_percent',
                      'gpu_temperature_c', 'gpu_utilization_percent']:
            summary['peak_'+field] = max((s[field] for s in valid if s.get(field) is not None), default=None)
        events = []
        for r in good:
            if r.get('first_token_at_s') is not None:
                events.extend([(r['first_token_at_s'], 1), (r['finished_at_s'], -1)])
        generating = peak_generating = 0
        for _, change in sorted(events):
            generating += change
            peak_generating = max(peak_generating, generating)
        summary['peak_overlapping_responses'] = peak_generating
        summary['seconds_with_queue'] = sum(
            max(0, b['timestamp']-v['timestamp']) for v,b in zip(valid,valid[1:])
            if v.get('num_requests_waiting', 0)>0)
        summary['seconds_cache_above_95_percent'] = sum(
            max(0, b['timestamp']-v['timestamp']) for v,b in zip(valid,valid[1:])
            if v.get('kv_cache_usage_perc', 0)>=.95)
        per_turn=[]
        for turn in range(1,a.turns+1):
            rs=[r for r in good if r['turn']==turn]
            rates=[(r['usage']['completion_tokens']-1)/(r['total_s']-r['ttft_s']) for r in rs if r.get('ttft_s') is not None and r['total_s']>r['ttft_s']]
            row={'turn':turn,'completed':len(rs),'expected':a.concurrency,
                 'ttft_p50_s':quantile([r.get('ttft_s') for r in rs],.5),
                 'ttft_p95_s':quantile([r.get('ttft_s') for r in rs],.95),
                 'ttft_max_s':max((r['ttft_s'] for r in rs if r.get('ttft_s') is not None),default=None),
                 'total_p95_s':quantile([r['total_s'] for r in rs],.95),
                 'decode_p05_tokens_s':quantile(rates,.05),
                 'decode_p50_tokens_s':quantile(rates,.5)}
            row['reference_fluent']=len(rs)==a.concurrency and row['ttft_p95_s'] is not None and row['ttft_p95_s']<=5 and row['decode_p05_tokens_s'] is not None and row['decode_p05_tokens_s']>=10
            per_turn.append(row)
        summary['per_turn']=per_turn
        summary['all_turns_completed']=len(good)==count
        summary['followups_reference_fluent']=all(r['reference_fluent'] for r in per_turn[1:])
        summary['followups_ttft_p95_s']=quantile([r.get('ttft_s') for r in good if r['turn']>1],.95)
        summary['followups_total_p95_s']=quantile([r['total_s'] for r in good if r['turn']>1],.95)
        temporary = dest.with_suffix('.json.tmp')
        temporary.write_text(json.dumps({'summary': summary, 'requests': list(captured_results),
                                        'metrics': list(samples)}, indent=2))
        temporary.replace(dest)
        return summary

    samples.append(metrics())
    watcher = threading.Thread(target=monitor, daemon=True)
    watcher.start()
    print('START '+str(dest), flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.concurrency) as pool:
        pending = {pool.submit(user_session, i) for i in range(a.concurrency)}
        last = 0
        while pending:
            done, pending = concurrent.futures.wait(pending, timeout=5,
                            return_when=concurrent.futures.FIRST_COMPLETED)
            for f in done:f.result()
            summary = save('running')
            elapsed = time.monotonic()-start
            if elapsed-last >= 30:
                last = elapsed
                print('PROGRESS '+json.dumps(summary), flush=True)
    if len(histories)==a.concurrency:
        state={'case_id':a.case_id,'histories':histories,'source_result':str(dest)}
        pathlib.Path(a.state_output).write_bytes(gzip.compress(json.dumps(state,separators=(',',':')).encode()))
    stop.set()
    watcher.join(timeout=12)
    samples.append(metrics())
    final_summary = save('complete')
    print('DONE '+json.dumps(final_summary), flush=True)
    if final_summary['failed'] or not final_summary['all_turns_completed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
