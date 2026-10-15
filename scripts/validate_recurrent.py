#!/usr/bin/env python3
"""Validate actual multi-turn history continuity, timing, and source preservation."""
import gzip
import hashlib
import json
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
    if s.get('kind')!='recurrent':continue
    source=BASE/'configuracion-y-registros/scripts/versions'/(s['script_sha256']+'.py')
    if not source.exists() or hashlib.sha256(source.read_bytes()).hexdigest()!=s['script_sha256']:errors.append('Executed probe missing: '+str(path))
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
    if not read(BASE/'configuracion-y-registros/queue.json').get('finished'):errors.append('Queue still open')
if errors:raise SystemExit('\n'.join(errors))
print(f'Validated {checked} recurrent cases, actual output reuse, pause intervals, checkpoints and source hashes.')
