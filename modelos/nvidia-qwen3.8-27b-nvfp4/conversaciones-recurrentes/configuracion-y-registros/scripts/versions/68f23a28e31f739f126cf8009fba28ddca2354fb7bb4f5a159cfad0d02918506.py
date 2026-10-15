#!/usr/bin/env python3
"""Chat API control using fabricated Spanish conversations and real assistant replies."""
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
    thinking = not a.case_id.endswith('-sin-razonamiento')
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

    def post(endpoint,payload):
        req=urllib.request.Request(a.base_url+endpoint,data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
        return json.load(urllib.request.urlopen(req,timeout=60))

    def tokenize(messages):
        extra={} if thinking else {'chat_template_kwargs':{'enable_thinking':False}}
        return post('/tokenize',dict(model=a.model,messages=messages,add_generation_prompt=True,**extra))['count']

    def request_one(user,turn,messages):
        input_tokens=tokenize(messages)
        payload={'model':a.model,'messages':messages,'max_tokens':a.output_tokens,
                 'temperature':0,'seed':a.seed+user,'stream':True,'stream_options':{'include_usage':True}}
        if not thinking:payload['chat_template_kwargs']={'enable_thinking':False}
        req=urllib.request.Request(a.base_url+'/v1/chat/completions',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
        started=time.monotonic();first=visible=reasoning_first=None
        usage=finish=None;content='';reasoning='';events=0;error=None
        try:
            with urllib.request.urlopen(req,timeout=a.request_timeout) as response:
                for line in response:
                    if not line.startswith(b'data: '):continue
                    val=line[6:].strip()
                    if val==b'[DONE]':break
                    data=json.loads(val)
                    if data.get('error'):raise RuntimeError(str(data['error']))
                    if data.get('usage'):usage=data['usage']
                    for choice in data.get('choices',[]):
                        delta=choice.get('delta') or {}
                        text=delta.get('content') or ''
                        thought=delta.get('reasoning') or delta.get('reasoning_content') or ''
                        now=time.monotonic()
                        if text or thought:
                            if first is None:first=now
                            events+=1
                        if text:
                            if visible is None:visible=now
                            content+=text
                        if thought:
                            if reasoning_first is None:reasoning_first=now
                            reasoning+=thought
                        if choice.get('finish_reason'):finish=choice['finish_reason']
        except Exception as exc:error=type(exc).__name__+': '+str(exc)
        ended=time.monotonic()
        ok=bool(not error and usage and usage['prompt_tokens']==input_tokens and 0<usage['completion_tokens']<=a.output_tokens and finish in ('stop','length'))
        assistant={'role':'assistant','content':content}
        if reasoning:assistant['reasoning']=reasoning
        return {'index':user*a.turns+turn,'user_id':user,'turn':turn+1,'input_tokens':input_tokens,
                'prompt_sha256':hashlib.sha256(json.dumps(messages,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),
                'assistant_message':assistant,'ok':ok,'started_at_s':started-start,'finished_at_s':ended-start,
                'first_token_at_s':None if first is None else first-start,'ttft_s':None if first is None else first-started,
                'visible_ttft_s':None if visible is None else visible-started,
                'reasoning_ttft_s':None if reasoning_first is None else reasoning_first-started,
                'total_s':ended-started,'usage':usage,'finish_reason':finish,'text_events':events,
                'has_visible_answer':bool(content),'naturally_finished':finish=='stop','error':error}

    barrier=threading.Barrier(a.concurrency)
    def user_session(user):
        rng=random.Random(a.seed+user)
        system={'role':'system','content':'Eres un asistente que ayuda a organizar proyectos ficticios. Responde en español de forma clara y breve. Todos los datos de este ejercicio son inventados.'}
        intro=f'Conversación de prueba {a.seed}-{user}. Estoy organizando un proyecto ficticio. Estas son mis notas de trabajo.\n'
        notes=''.join(f'Nota {i}: el taller {rng.randrange(10000,99999)} dispone de {rng.randrange(2,90)} piezas; la tarea {rng.randrange(1000,9999)} durará {rng.randrange(1,30)} días. Revisar materiales, distribución y plazos antes de comenzar.\n' for i in range(max(100,a.input_tokens//15)))
        question='\nCon estas notas, propón tres acciones concretas para organizar el trabajo y explica brevemente por qué. No reproduzcas todas las notas.'
        low=0;high=len(notes);best=None
        while low<=high:
            mid=(low+high)//2
            candidate=[system,{'role':'user','content':intro+notes[:mid]+question}]
            size=tokenize(candidate)
            if size<=a.input_tokens:best=candidate;low=mid+1
            else:high=mid-1
        if best is None:raise ValueError('Target input shorter than chat instructions')
        messages=best;initial=json.loads(json.dumps(messages));exchanges=[]
        barrier.wait(timeout=180)
        followups=['Añade un calendario sencillo para esas acciones y señala dos riesgos que debería vigilar.',
                   'Resume las decisiones que hemos tomado y dime cuál debería ser mi siguiente paso.']
        for turn in range(a.turns):
            if turn:
                time.sleep(a.think_seconds)
                messages.append({'role':'user','content':followups[(turn-1)%len(followups)]})
            result=request_one(user,turn,messages)
            with lock:results.append(result)
            print('REQUEST '+json.dumps({k:v for k,v in result.items() if k!='assistant_message'}),flush=True)
            exchanges.append({'user_message':messages[-1],'assistant_message':result['assistant_message']})
            if not result['ok']:break
            messages.append(result['assistant_message'])
        with lock:histories[str(user)]={'initial_messages':initial,'exchanges':exchanges,'final_messages':messages}

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
        summary = {'kind': 'chat_recurrent', 'api': '/v1/chat/completions', 'reasoning_mode': 'server_default' if thinking else 'disabled', 'forced_output_length': False, 'case_id': a.case_id, 'turns': a.turns, 'think_seconds': a.think_seconds, 'new_message_tokens': a.new_message_tokens, 'parent_state': a.parent_state, 'status': status, 'started_utc': started_utc, 'script_sha256': script_sha256, 'model': a.model, 'concurrency': a.concurrency, 'num_requests': count,
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
            row['visible_ttft_p95_s']=quantile([r.get('visible_ttft_s') for r in rs],.95)
            row['visible_answers']=sum(r['has_visible_answer'] for r in rs)
            row['natural_completions']=sum(r['naturally_finished'] for r in rs)
            row['reference_fluent']=len(rs)==a.concurrency and row['visible_answers']==a.concurrency and row['natural_completions']==a.concurrency and row['visible_ttft_p95_s'] is not None and row['visible_ttft_p95_s']<=5 and row['ttft_p95_s'] is not None and row['ttft_p95_s']<=5 and row['decode_p05_tokens_s'] is not None and row['decode_p05_tokens_s']>=10
            per_turn.append(row)
        summary['visible_answers']=sum(r.get('has_visible_answer',False) for r in good)
        summary['natural_completions']=sum(r.get('naturally_finished',False) for r in good)
        summary['followups_visible_ttft_p95_s']=quantile([r.get('visible_ttft_s') for r in good if r['turn']>1],.95)
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
