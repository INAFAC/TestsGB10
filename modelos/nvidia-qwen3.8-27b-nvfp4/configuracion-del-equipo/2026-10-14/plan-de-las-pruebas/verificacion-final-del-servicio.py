import datetime,hashlib,json,pathlib,re,subprocess,time,urllib.request
expected=['vllm','serve','nvidia/Qwen3.8-27B-NVFP4','--gpu-memory-utilization','0.40','--max-num-seqs','4','--enable-auto-tool-choice','--tool-call-parser','qwen3_coder','--reasoning-parser','qwen3']
expected_sha='1caf0951ec1175b71b97d53ffcc557e9d9ea2e506dd046b2647603c8551fd696'
expected_image='sha256:557747337846eecf34486866f3d992383c6f8af869fdb0e365b5093fcaee02c2'
base=pathlib.Path('/home/canadas/ai/vllm/compose.yaml')
c=json.loads(subprocess.check_output(['docker','inspect','vllm-qwen38'],text=True))[0]
with urllib.request.urlopen('http://127.0.0.1:8000/health',timeout=15) as r:health=r.status
with urllib.request.urlopen('http://127.0.0.1:8000/v1/models',timeout=15) as r:models=json.load(r)
payload={'model':expected[2],'prompt':[100]*16,'max_tokens':16,'temperature':0,'ignore_eos':True}
started=time.monotonic()
request=urllib.request.Request('http://127.0.0.1:8000/v1/completions',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
with urllib.request.urlopen(request,timeout=60) as r:smoke=json.load(r)
smoke_result={'duration_s':time.monotonic()-started,'usage':smoke['usage'],'finish_reason':smoke['choices'][0]['finish_reason']}
assert smoke['usage']['prompt_tokens']==16 and smoke['usage']['completion_tokens']==16,smoke_result
with urllib.request.urlopen('http://127.0.0.1:8000/metrics',timeout=15) as r:metrics=r.read().decode()
counts={name:sum(float(m.group(1)) for m in re.finditer(r'^vllm:'+name+r'(?:\{[^\n]*\})?\s+([\d.eE+-]+)$',metrics,re.M)) for name in ['num_requests_running','num_requests_waiting']}
metadata=json.loads(pathlib.Path('/tmp/gb10-additional-20261014/verificacion-final-30/metadata.json').read_text())
record={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'health_http_status':health,'container_status':c['State']['Status'],'container_started_at':c['State']['StartedAt'],'container_restart_count':c['RestartCount'],'command':c['Config']['Cmd'],'compose_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),'image_id':c['Image'],'models':models,'requests':counts,'runner_restore_status':metadata['restore_status']}
assert record['command']==expected,record['command']
assert record['compose_sha256']==expected_sha,record['compose_sha256']
assert record['image_id']==expected_image,record['image_id']
assert record['container_status']=='running'
assert health==200
assert metadata['restore_status']=='healthy'
assert models['data'][0]['id']==expected[2]
assert models['data'][0]['max_model_len']==262144,models
assert all(v==0 for v in counts.values()),counts
assert all(re.search(r'^vllm:'+name+r'(?:\{|\s)',metrics,re.M) for name in counts), 'Missing metrics'
record['smoke_generation']=smoke_result
record['verified']=True
print(json.dumps(record,ensure_ascii=False,indent=2))
