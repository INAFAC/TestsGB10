#!/usr/bin/env python3
"""Validate actual multi-turn history continuity, timing, and source preservation."""
import gzip
import hashlib
import json
import math
import pathlib
import random

ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/'modelos/nvidia-qwen3.8-27b-nvfp4/conversaciones-recurrentes'
read=lambda p:json.loads(p.read_text())
if not (BASE/'configuracion-y-registros/metadata.json').exists():
    print('Recurrent campaign has no published measurements yet.');raise SystemExit
meta=read(BASE/'configuracion-y-registros/metadata.json');errors=[];checked=0
for item in read(BASE/'configuracion-y-registros/inventario-originales.json'):
    p=ROOT/item['file']
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:errors.append('Original changed: '+str(p))
folders=list(BASE.glob('memoria-*/configuracion.json'))
state_paths={}
for config in folders:
    c=read(config)
    state_paths[f"/tmp/gb10-recurrent-20261015/profiles/{c['profile_id']}/{c['id']}/histories.json.gz"]=config.parent/'historiales-reproducibles.json.gz'
for config in folders:
    c=read(config);path=config.with_name('mediciones.json')
    if not path.exists():continue
    d=read(path);s=d['summary'];checked+=1
    source=BASE/'configuracion-y-registros/scripts/versions'/(s['script_sha256']+'.py')
    if not source.exists() or hashlib.sha256(source.read_bytes()).hexdigest()!=s['script_sha256']:errors.append('Executed probe missing: '+str(path))
    if s.get('kind')=='chat_recurrent':
        checkpoint=config.with_name('historiales-reproducibles.json.gz')
        state=json.loads(gzip.decompress(checkpoint.read_bytes())) if checkpoint.exists() else None
        if state is None:errors.append('Chat transcript missing: '+str(path));continue
        for user,conversation in state['histories'].items():
            messages=list(conversation['initial_messages']);previous=None
            rs=sorted([r for r in d['requests'] if r['user_id']==int(user)],key=lambda r:r['turn'])
            for r,exchange in zip(rs,conversation['exchanges']):
                if r['turn']>1:messages.append(exchange['user_message'])
                digest=hashlib.sha256(json.dumps(messages,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
                if digest!=r['prompt_sha256']:errors.append('Chat history mismatch: '+str(path))
                if exchange['assistant_message']!=r['assistant_message']:errors.append('Chat reply mismatch: '+str(path))
                if previous and r['started_at_s']<previous['finished_at_s']+s['think_seconds']-.02:errors.append('Chat pause mismatch: '+str(path))
                if r['ok']:messages.append(r['assistant_message'])
                if r.get('visible_ttft_s') is not None and not 0<=r['visible_ttft_s']<=r['total_s']:errors.append('Chat visible latency mismatch: '+str(path))
                previous=r
            if len(rs)!=len(conversation['exchanges']) or messages!=conversation['final_messages']:errors.append('Chat transcript incomplete: '+str(path))
        continue
    parent=None
    if s.get('parent_state'):
        target=state_paths.get(s['parent_state'])
        if target is None or not target.exists():errors.append('Missing parent history: '+str(path));continue
        parent=json.loads(gzip.decompress(target.read_bytes()))
    checkpoint=config.with_name('historiales-reproducibles.json.gz')
    final=json.loads(gzip.decompress(checkpoint.read_bytes())) if checkpoint.exists() else None
    for user in range(s['concurrency']):
        rng=random.Random(s['seed']+user)
        history=list(parent['histories'][str(user)]) if parent else []
        history.extend(rng.randrange(1000,30000) for _ in range(s['input_tokens']-len(history)))
        rows=sorted([r for r in d['requests'] if r['user_id']==user],key=lambda r:r['turn'])
        previous=None
        for r in rows:
            if r['turn']>1:
                rng=random.Random(s['seed']+1000000+user*100+r['turn']-1)
                history.extend(rng.randrange(1000,30000) for _ in range(s['new_message_tokens']))
                if previous is None or previous['turn']!=r['turn']-1:errors.append('Missing previous turn: '+str(path))
                elif r['started_at_s']<previous['finished_at_s']+s['think_seconds']-.02:errors.append('Think interval not respected: '+str(path))
            digest=hashlib.sha256(json.dumps(history,separators=(',',':')).encode()).hexdigest()
            if digest!=r['prompt_sha256'] or len(history)!=r['input_tokens']:errors.append('History mismatch: '+str(path))
            if r['ok']:
                if len(r['generated_token_ids'])!=s['output_tokens']:errors.append('Output token IDs missing: '+str(path))
                if r['usage']['total_tokens']!=len(history)+len(r['generated_token_ids']):errors.append('Total tokens mismatch: '+str(path))
                if r['usage']['total_tokens']>s['max_model_len']:errors.append('Exceeded context: '+str(path))
                history.extend(r['generated_token_ids'])
            previous=r
        if final is not None and final['histories'].get(str(user))!=history:errors.append('Checkpoint mismatch: '+str(path))
    if s['all_turns_completed'] and len(d['requests'])!=s['concurrency']*s['turns']:errors.append('Missing completed turns: '+str(path))
plan=read(BASE/'plan.json')
if plan['status']=='complete':
    if meta.get('restore_status')!='healthy' or meta.get('state')!='stopped':errors.append('Restoration not verified')
    queue=read(BASE/'configuracion-y-registros/queue.json')
    if not queue.get('finished'):errors.append('Queue still open')
    recorded={p['id']:p for p in meta['profiles']}
    for profile in queue['profiles']:
        rec=recorded.get(profile['id'])
        if rec is None:errors.append('Queued profile never attempted: '+profile['id']);continue
        if not rec.get('ready'):
            if rec.get('state')!='startup_failed':errors.append('Unresolved startup: '+profile['id'])
            continue
        if {c['id'] for c in profile['cases']}!={c['id'] for c in rec['cases']}:errors.append('Queued tests missing: '+profile['id'])
    entries=[]
    for config in folders:
        c=read(config);measurement=config.with_name('mediciones.json')
        entries.append((c,read(measurement)['summary'] if measurement.exists() else {}))
    def require(memory,users,tokens,turns,chat=False,mode=None):
        found=[(c,s) for c,s in entries if round(100*c['memory_fraction'])==memory and c['users']==users
               and c['input_tokens']==tokens and c.get('turns',3)==turns and c['id'].startswith('chat-')==chat
               and s.get('status') in ('complete','finished_with_errors','group_timeout')
               and (mode is None or s.get('reasoning_mode')==mode)]
        if not found:errors.append(f'Missing required test: {memory}% / {users} users / {tokens} input / {turns} turns / chat={chat} / {mode}')
        return found
    for memory in (40,70,85):
        for tokens in (8192,32768):require(memory,20,tokens,3)
    decisions=plan.get('decisions',{})
    selected=decisions.get('selected_memory_percent')
    if selected not in (40,50,60,70,85):errors.append('Selected memory not documented')
    if not decisions.get('selection_evidence'):errors.append('Selection evidence missing')
    for users in (10,30):
        for tokens in (8192,32768):require(selected,users,tokens,3)
    for users in (10,20,30):
        growth=require(selected,users,65536,2)
        if users==20 or any(s.get('followups_reference_fluent') for c,s in growth):require(selected,users,131072,2)
    require(selected,20,260864,2)
    for memory in (50,60):
        decision=decisions.get('refinement_'+str(memory),{})
        if decision.get('required') is True:
            for tokens in (8192,32768):require(memory,20,tokens,3)
        elif decision.get('required') is not False or not decision.get('reason'):
            errors.append('Memory refinement not resolved: '+str(memory))
    rule=plan.get('refinement_comparison')
    if rule and decisions.get('refinement_50',{}).get('required'):
        measurements={}
        for config in folders:
            c=read(config);path=config.with_name('mediciones.json')
            if c['users']==20 and c.get('turns',3)==3 and not c['id'].startswith('chat-') and path.exists():
                measurements[round(100*c['memory_fraction']),c['input_tokens']]=read(path)
        retained=[]
        def decode_p05(data):
            rates=sorted((r['usage']['completion_tokens']-1)/(r['total_s']-r['ttft_s'])
                         for r in data['requests'] if r['ok'] and r['turn']>1
                         and r.get('ttft_s') is not None and r['total_s']>r['ttft_s'])
            return rates[max(0,math.ceil(.05*len(rates))-1)] if rates else None
        for size in rule['loads_input_tokens']:
            reference=measurements.get((rule['reference_memory_percent'],size))
            candidate=measurements.get((50,size))
            if not reference or not reference['summary'].get('all_turns_completed'):
                errors.append('Refinement reference incomplete: '+str(size));continue
            if not candidate or not candidate['summary'].get('all_turns_completed'):
                retained.append(False);continue
            a=reference['summary'];b=candidate['summary'];base_rate=decode_p05(reference);candidate_rate=decode_p05(candidate)
            retained.append(b['followups_ttft_p95_s'] is not None and b['followups_total_p95_s'] is not None
                and candidate_rate is not None and base_rate is not None
                and b['followups_ttft_p95_s']<=max(a['followups_ttft_p95_s']*rule['followup_ttft_p95_max_ratio'],a['followups_ttft_p95_s']+rule['followup_ttft_p95_absolute_tolerance_seconds'])
                and b['followups_total_p95_s']<=a['followups_total_p95_s']*rule['followup_total_p95_max_ratio']
                and candidate_rate>=base_rate*rule['followup_decode_p05_min_ratio'])
        if len(retained)==len(rule['loads_input_tokens']) and decisions.get('refinement_60',{}).get('required')!=(not all(retained)):
            errors.append('Decision about 60% disagrees with the predeclared performance rule')
    for tokens in (8192,32768):require(selected,20,tokens,3,True,'disabled')
    require(selected,20,8192,3,True,'server_default')
    proof=BASE/'configuracion-y-registros/verificacion-final.json'
    if not proof.exists():errors.append('Independent final runtime verification missing')
    else:
        verification=read(proof)
        if not (verification.get('verified') is True and verification.get('container_status')=='running'
                and verification.get('health_http_status')==200 and verification.get('command')==meta['original_command']
                and verification.get('image_id')==meta['image_id'] and verification.get('compose_sha256')==meta['compose_sha256']
                and verification.get('max_model_len')==262144 and verification.get('generation_ok') is True
                and verification.get('requests')=={'num_requests_running':0,'num_requests_waiting':0}):
            errors.append('Independent final runtime verification failed')
        source=BASE/'configuracion-y-registros/scripts/versions'/(verification.get('verification_script_sha256','missing')+'.py')
        if not source.exists() or hashlib.sha256(source.read_bytes()).hexdigest()!=verification.get('verification_script_sha256'):
            errors.append('Final verification source missing')
    for p in [ROOT/'README.md',BASE.parent/'README.md',BASE/'README.md']:
        if 'Se están realizando nuevas pruebas' in p.read_text():errors.append('Temporary notice remains: '+str(p))
if errors:raise SystemExit('\n'.join(errors))
print(f'Validated {checked} recurrent cases, actual output reuse, pause intervals, checkpoints and source hashes.')
