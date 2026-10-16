#!/usr/bin/env python3
"""Measure continued chat, separating historical loading from subsequent turns."""
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
import urllib.error


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
    p.add_argument('--schedule', choices=['simultaneous','independent'], default='simultaneous')
    p.add_argument('--reasoning', choices=['disabled','default'], default='disabled')
    p.add_argument('--followup-timeout', type=float, default=120)
    p.add_argument('--grow-to-context-limit', action='store_true')
    p.add_argument('--growth-step', type=int, default=1024)
    p.add_argument('--growth-stop-context', type=int, help='Only for validating the growth protocol on a small pilot')
    a = p.parse_args()
    thinking = a.reasoning == 'default'
    if a.parent_state:
        raise ValueError('This probe starts independent histories; parent-state is not supported')
    count = a.concurrency*a.turns
    histories = {}
    lock = threading.Lock()
    parent = json.loads(gzip.decompress(pathlib.Path(a.parent_state).read_bytes())) if a.parent_state else None
    started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    script_sha256 = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    dest = pathlib.Path(a.result)
    dest.parent.mkdir(parents=True, exist_ok=True)
    samples, results = [], []
    last_checkpoint_count=-1
    try:
        models = json.load(urllib.request.urlopen(a.base_url+'/v1/models', timeout=10))['data']
        model_info = next(m for m in models if m['id'] == a.model)
    except Exception:
        model_info = {}
    growth_targets=[]
    if a.grow_to_context_limit:
        last=a.growth_stop_context or model_info['max_model_len']-a.output_tokens
        growth_targets=list(range(a.input_tokens,last,a.growth_step))+[last]
        if not a.growth_stop_context:
            growth_targets.append(model_info['max_model_len']-128)
        a.turns=len(growth_targets)
        count=a.concurrency*a.turns
        if a.schedule!='simultaneous':
            raise ValueError('Growth trials require synchronized turns')
    growth_stop_reason=None
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
        output_budget=min(a.output_tokens,model_info['max_model_len']-input_tokens) if a.grow_to_context_limit else a.output_tokens
        if output_budget<=0 or input_tokens+output_budget>model_info['max_model_len']:
            raise ValueError('Insufficient room for the full requested answer')
        payload={'model':a.model,'messages':messages,'max_tokens':output_budget,
                 'temperature':0,'seed':a.seed+user,'stream':True,'stream_options':{'include_usage':True}}
        if not thinking:payload['chat_template_kwargs']={'enable_thinking':False}
        req=urllib.request.Request(a.base_url+'/v1/chat/completions',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
        # Tokenization and preparation precede the start barrier; every user has
        # finished loading their history before any measured continuation starts.
        if a.schedule=='simultaneous' or turn in (0,1):
            barrier.wait(timeout=7200)
        started=time.monotonic();first=visible=reasoning_first=None
        usage=finish=None;content='';reasoning='';events=0;error=None
        try:
            with urllib.request.urlopen(req,timeout=a.request_timeout if turn==0 else a.followup_timeout) as response:
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
        except urllib.error.HTTPError as exc:
            error=f'HTTP {exc.code}: '+exc.read().decode(errors='replace')[:4000]
        except Exception as exc:error=type(exc).__name__+': '+str(exc)
        ended=time.monotonic()
        ok=bool(not error and usage and usage['prompt_tokens']==input_tokens and 0<usage['completion_tokens']<=a.output_tokens and finish in ('stop','length'))
        if not ok and error is None:
            error=f'Unexpected response: expected prompt_tokens={input_tokens}, completion_tokens between 1 and {a.output_tokens}, and stop/length; received usage={usage}, finish_reason={finish}'
        assistant={'role':'assistant','content':content}
        if reasoning:assistant['reasoning']=reasoning
        return {'index':user*a.turns+turn,'user_id':user,'turn':turn+1,'input_tokens':input_tokens,
                'prompt_sha256':hashlib.sha256(json.dumps(messages,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),
                'assistant_message':assistant,'ok':ok,'started_at_s':started-start,'finished_at_s':ended-start,
                'network_idle_timeout_s':a.request_timeout if turn==0 else a.followup_timeout,
                'effective_output_budget':output_budget,
                'first_token_at_s':None if first is None else first-start,'ttft_s':None if first is None else first-started,
                'visible_ttft_s':None if visible is None else visible-started,
                'reasoning_ttft_s':None if reasoning_first is None else reasoning_first-started,
                'total_s':ended-started,'usage':usage,'finish_reason':finish,'text_events':events,
                'has_visible_answer':bool(content),'naturally_finished':finish=='stop','error':error}

    barrier=threading.Barrier(a.concurrency)
    def add_small_message(messages, question, target, rng, turn):
        # Preserve every old message and real reply. Only the NEW user message is
        # padded with fresh fictional notes to advance by about 1024 total tokens.
        intro=f'{question}\nEstas son las nuevas notas ficticias del paso {turn+1}:\n'
        base_count=tokenize(messages+[{'role':'user','content':intro}])
        allowance=target-base_count
        if allowance<0:
            raise ValueError('The real answer exceeded the reserved growth step')
        notes=''.join(f'Nota nueva {rng.randrange(100000,999999)}: hay {rng.randrange(3,40)} tareas, {rng.randrange(2,20)} personas y {rng.randrange(1,30)} días. Mantén las decisiones anteriores y ajusta solo lo necesario.\n' for _ in range(max(20,allowance//8)))
        low=0; high=len(notes); best=''
        while low<=high:
            mid=(low+high)//2
            size=post('/tokenize',{'model':a.model,'prompt':notes[:mid]})['count']
            if size<=max(0,allowance-4):best=notes[:mid];low=mid+1
            else:high=mid-1
        message={'role':'user','content':intro+best}
        actual=tokenize(messages+[message])
        while actual>target and best:
            best=best[:-max(1,actual-target)]
            message={'role':'user','content':intro+best}
            actual=tokenize(messages+[message])
        if actual>target or actual<target-32:
            raise ValueError(f'Unexpected small-message token sizing: {actual}, target {target}')
        messages.append(message)

    def round_acceptable(rs):
        if len(rs)!=a.concurrency or any(not r['ok'] or not r['has_visible_answer'] or not r['naturally_finished'] for r in rs):return False
        waits=sorted(r['visible_ttft_s'] for r in rs)
        rates=sorted((r['usage']['completion_tokens']-1)/(r['total_s']-r['ttft_s']) for r in rs)
        totals=sorted(r['total_s'] for r in rs)
        return waits[max(0,math.ceil(.95*len(rs))-1)]<=5 and max(waits)<=10 and rates[max(0,math.ceil(.05*len(rs))-1)]>=5 and totals[max(0,math.ceil(.95*len(rs))-1)]<=120

    def user_session(user):
        nonlocal growth_stop_reason
        rng=random.Random(a.seed+user)
        system={'role':'system','content':'Eres un asistente que ayuda a organizar proyectos ficticios. Responde en español, en un máximo de 100 palabras por respuesta. Todos los datos de este ejercicio son inventados.'}
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
        followups=['Añade un calendario sencillo para esas acciones y señala dos riesgos que debería vigilar.',
                   'Resume las decisiones que hemos tomado y dime cuál debería ser mi siguiente paso.',
                   'Ahora el plazo se reduce a la mitad. Ajusta nuestro plan conservando lo esencial.',
                   'Con los cambios anteriores, prepara una lista final de comprobaciones antes de empezar.']
        for turn in range(a.turns):
            if turn:
                time.sleep(a.think_seconds)
                question=followups[(turn-1)%len(followups)]
                if a.grow_to_context_limit:
                    if turn==a.turns-1 and not a.growth_stop_context:
                        question='Cierra el plan con una sola frase de un máximo de diez palabras.'
                    add_small_message(messages,question,growth_targets[turn],rng,turn)
                else:
                    messages.append({'role':'user','content':question})
            result=request_one(user,turn,messages)
            with lock:results.append(result)
            print('REQUEST '+json.dumps({k:v for k,v in result.items() if k!='assistant_message'}),flush=True)
            exchanges.append({'user_message':messages[-1],'assistant_message':result['assistant_message']})
            # Keep all users on the same round even after an API error, preserving
            # the failure. No empty or invented assistant response enters history.
            if result['ok']:messages.append(result['assistant_message'])
            with lock:
                histories[str(user)]=json.loads(json.dumps({'initial_messages':initial,'exchanges':exchanges,'final_messages':messages}))
            if a.grow_to_context_limit:
                barrier.wait(timeout=7200)
                with lock:
                    captured=list(results)
                if any(not r['ok'] for r in captured):
                    growth_stop_reason='api_or_network_error'
                elif any(r['finish_reason']=='length' or not r['has_visible_answer'] for r in captured):
                    growth_stop_reason='answer_cut_or_not_visible'
                elif turn>=7 and all(not round_acceptable([r for r in captured if r['turn']==t]) for t in range(turn-1,turn+2)):
                    growth_stop_reason='three_consecutive_rounds_outside_reference'
                barrier.wait(timeout=7200)
                if growth_stop_reason:break
        with lock:histories[str(user)]={'initial_messages':initial,'exchanges':exchanges,'final_messages':messages}

    def quantile(values,p):
        values=sorted(v for v in values if v is not None)
        if not values:return None
        # Nearest-rank percentiles: p95 of 20 users is their 19th ordered value.
        return values[max(0,math.ceil(p*len(values))-1)]

    def save(status):
        nonlocal last_checkpoint_count
        with lock:
            captured_results=list(results)
            captured_histories=dict(histories)
        exchange_count=sum(len(h['exchanges']) for h in captured_histories.values())
        if exchange_count!=last_checkpoint_count:
            checkpoint=pathlib.Path(a.state_output)
            temporary_checkpoint=checkpoint.with_suffix(checkpoint.suffix+'.tmp')
            state={'case_id':a.case_id,'histories':captured_histories,'source_result':str(dest)}
            temporary_checkpoint.write_bytes(gzip.compress(json.dumps(state,separators=(',',':')).encode()))
            temporary_checkpoint.replace(checkpoint)
            last_checkpoint_count=exchange_count
        valid = [s for s in samples if 'error' not in s]
        good = [r for r in captured_results if r['ok']]
        if status=='complete' and len(captured_results)<count:status='finished_with_errors'
        summary = {'kind': 'chat_recurrent', 'api': '/v1/chat/completions', 'reasoning_mode': 'server_default' if thinking else 'disabled', 'forced_output_length': False, 'case_id': a.case_id, 'turns': a.turns, 'think_seconds': a.think_seconds, 'new_message_tokens': None, 'parent_state': a.parent_state, 'status': status, 'started_utc': started_utc, 'script_sha256': script_sha256, 'model': a.model, 'concurrency': a.concurrency, 'num_requests': count,
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
        follow=[r for r in good if r['turn']>1]
        rates=[(r['usage']['completion_tokens']-1)/(r['total_s']-r['ttft_s']) for r in follow
               if r.get('ttft_s') is not None and r['total_s']>r['ttft_s']]
        summary.update(kind='capacity_chat', schedule=a.schedule,
            followup_network_idle_timeout_s=a.followup_timeout,
            followups_decode_p05_tokens_s=quantile(rates,.05),
            followups_visible_ttft_max_s=max((r['visible_ttft_s'] for r in follow if r['visible_ttft_s'] is not None),default=None),
            all_answers_visible_and_natural=len(good)==count and all(r['has_visible_answer'] and r['naturally_finished'] for r in good))
        summary['acceptable_reference']=bool(summary['all_answers_visible_and_natural']
            and summary['followups_visible_ttft_p95_s'] is not None and summary['followups_visible_ttft_p95_s']<=5
            and summary['followups_visible_ttft_max_s']<=10
            and summary['followups_decode_p05_tokens_s'] is not None and summary['followups_decode_p05_tokens_s']>=5
            and summary['followups_total_p95_s']<=120)
        summary['comfortable_reference']=bool(summary['acceptable_reference']
            and summary['followups_visible_ttft_p95_s']<=2
            and summary['followups_decode_p05_tokens_s']>=10
            and summary['followups_total_p95_s']<=60)
        if a.grow_to_context_limit:
            windows=[]
            for lower in range(2,a.turns+1,16):
                upper=min(a.turns,lower+15)
                rs=[r for r in captured_results if lower<=r['turn']<=upper]
                if not rs:continue
                complete=[r for r in rs if r['ok']]
                waits=[r['visible_ttft_s'] for r in complete if r['has_visible_answer']]
                speeds=[(r['usage']['completion_tokens']-1)/(r['total_s']-r['ttft_s']) for r in complete if r.get('ttft_s') is not None and r['total_s']>r['ttft_s']]
                row=dict(first_turn=lower,last_turn=upper,measured=len(rs),expected=(upper-lower+1)*a.concurrency,
                    min_input_tokens=min(r['input_tokens'] for r in rs),max_input_tokens=max(r['input_tokens'] for r in rs),
                    visible_ttft_p95_s=quantile(waits,.95),visible_ttft_max_s=max(waits,default=None),
                    decode_p05_tokens_s=quantile(speeds,.05),total_p95_s=quantile([r['total_s'] for r in complete],.95))
                row['acceptable_reference']=bool(len(complete)==row['expected'] and all(r['has_visible_answer'] and r['naturally_finished'] for r in complete)
                    and row['visible_ttft_p95_s'] is not None and row['visible_ttft_p95_s']<=5 and row['visible_ttft_max_s']<=10
                    and row['decode_p05_tokens_s'] is not None and row['decode_p05_tokens_s']>=5 and row['total_p95_s']<=120)
                windows.append(row)
            summary.update(kind='growing_chat',growth_step_tokens=a.growth_step,
                growth_targets=growth_targets,growth_stop_reason=growth_stop_reason,
                windows=windows,
                reached_final_target=len(good)==count,
                actual_rounds=max((r['turn'] for r in captured_results),default=0),
                final_total_tokens_by_user={str(user):max((r['usage']['total_tokens'] for r in good if r['user_id']==user),default=0) for user in range(a.concurrency)})
            if growth_stop_reason and status!='running':summary['status']='stopped_early'
            summary['acceptable_reference']=summary['acceptable_reference'] and all(w['acceptable_reference'] for w in windows)
        temporary = dest.with_suffix('.json.tmp')
        temporary.write_text(json.dumps({'summary': summary, 'requests': list(captured_results),
                                        'metrics': list(samples)}, indent=2))
        temporary.replace(dest)
        return summary

    samples.append(metrics())
    watcher = threading.Thread(target=monitor, daemon=True)
    watcher.start()
    print('START '+str(dest), flush=True)
    def guarded_session(user):
        try:return user_session(user)
        except BaseException:
            barrier.abort()
            raise
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.concurrency) as pool:
        pending = {pool.submit(guarded_session, i) for i in range(a.concurrency)}
        last = 0
        while pending:
            done, pending = concurrent.futures.wait(pending, timeout=5,
                            return_when=concurrent.futures.FIRST_COMPLETED)
            for f in done:f.result()
            summary = save('running')
            elapsed = time.monotonic()-start
            if elapsed-last >= 30:
                last = elapsed
                print('PROGRESS '+json.dumps({k:summary.get(k) for k in ('case_id','status','completed','num_requests','duration_s','actual_rounds','final_total_tokens_by_user','growth_stop_reason')}), flush=True)
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
