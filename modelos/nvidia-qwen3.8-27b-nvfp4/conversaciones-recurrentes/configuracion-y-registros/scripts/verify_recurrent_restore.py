#!/usr/bin/env python3
"""Run on the GB10 after the campaign stops; verify the captured service and a small generation."""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import time
import urllib.request

p=argparse.ArgumentParser()
p.add_argument('--root',required=True)
p.add_argument('--compose',default=str(pathlib.Path.home()/'ai/vllm/compose.yaml'))
p.add_argument('--container',default='vllm-qwen38')
p.add_argument('--base-url',default='http://127.0.0.1:8000')
a=p.parse_args()
root=pathlib.Path(a.root)
meta=json.loads((root/'metadata.json').read_text())
proof={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'verified':False,
       'verification_script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}

def get(endpoint):
    return urllib.request.urlopen(a.base_url+endpoint,timeout=10)

def requests():
    raw=get('/metrics').read().decode()
    result={}
    for key in ('num_requests_running','num_requests_waiting'):
        values=re.findall(r'^vllm:'+key+r'(?:\{[^\n]*\})? ([^\n]+)',raw,re.M)
        if not values:raise RuntimeError('Required metric missing: '+key)
        result[key]=sum(float(v) for v in values)
    return result

try:
    if meta['state']!='stopped' or meta['restore_status']!='healthy':
        raise RuntimeError('Controller has not confirmed a healthy restoration')
    container=json.loads(subprocess.check_output(['docker','inspect',a.container],text=True))[0]
    proof.update(container_status=container['State']['Status'],command=container['Config']['Cmd'],
                 image_id=container['Image'],compose_sha256=hashlib.sha256(pathlib.Path(a.compose).read_bytes()).hexdigest())
    for field,expected in [('command',meta['original_command']),('image_id',meta['image_id']),('compose_sha256',meta['compose_sha256'])]:
        if proof[field]!=expected:raise RuntimeError('Restored configuration mismatch: '+field)
    if proof['container_status']!='running':raise RuntimeError('Container is not running')
    proof['health_http_status']=get('/health').status
    if proof['health_http_status']!=200:raise RuntimeError('Health check failed')
    models=json.load(get('/v1/models'))['data']
    model=next(v for v in models if v['id']==meta['original_command'][2])
    proof['max_model_len']=model['max_model_len']
    if proof['max_model_len']!=262144:raise RuntimeError('Unexpected model context limit')
    proof['requests_before_generation']=requests()
    if any(proof['requests_before_generation'].values()):raise RuntimeError('Other requests are still active; defer final verification')
    payload={'model':model['id'],'prompt':'Continúa esta secuencia de números: uno, dos, tres,',
             'max_tokens':16,'ignore_eos':True,'temperature':0}
    started=time.monotonic()
    req=urllib.request.Request(a.base_url+'/v1/completions',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
    result=json.load(urllib.request.urlopen(req,timeout=120))
    proof['generation_seconds']=time.monotonic()-started
    proof['generation_usage']=result.get('usage')
    proof['generation_ok']=bool(result.get('choices') and result['choices'][0].get('text')
                                and (result.get('usage') or {}).get('completion_tokens')==16)
    if not proof['generation_ok']:raise RuntimeError('Generation check failed')
    for _ in range(10):
        proof['requests']=requests()
        if not any(proof['requests'].values()):break
        time.sleep(1)
    if any(proof['requests'].values()):raise RuntimeError('Requests remain active after verification')
    proof['verified']=True
except Exception as exc:
    proof['error']=type(exc).__name__+': '+str(exc)
finally:
    out=root/'verificacion-final.json';temp=out.with_suffix('.json.tmp')
    temp.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n');temp.replace(out)
    print(json.dumps(proof,ensure_ascii=False,indent=2))
if not proof['verified']:raise SystemExit(1)
