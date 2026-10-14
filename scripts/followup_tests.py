#!/usr/bin/env python3
"""Detailed short tests and prefix-reuse tests after the original server is restored."""
import argparse
import json
import pathlib
import subprocess
import sys
import time

p=argparse.ArgumentParser()
p.add_argument('--wait-metadata', required=True)
p.add_argument('--results', required=True)
a=p.parse_args()
root=pathlib.Path(a.results)
root.mkdir(parents=True, exist_ok=True)
print('WAIT_RESTORE '+a.wait_metadata, flush=True)
while True:
    try:
        state=json.loads(pathlib.Path(a.wait_metadata).read_text())
        if state.get('restore_status')=='healthy':break
    except (OSError,ValueError):pass
    time.sleep(5)
info=json.loads(subprocess.check_output(['docker','inspect','vllm-qwen38'],text=True))[0]
cmd=info['Config']['Cmd']
assert cmd[cmd.index('--gpu-memory-utilization')+1] in ('0.40','0.4')
assert cmd[cmd.index('--max-num-seqs')+1]=='4'
probe=pathlib.Path(__file__).with_name('context_probe.py')
cases = [
    ('reuse-40','01-cold-65536',1,1,65536,128,90000),
    ('reuse-40','02-repeat-65536',1,1,65536,128,90000),
    ('reuse-40','03-extend-131072',1,1,131072,128,90000),
    ('reuse-40','04-repeat-131072',1,1,131072,128,90000),
    ('reuse-40','05-extend-262016',1,1,262016,128,90000),
    ('reuse-40','06-repeat-262016',1,1,262016,128,90000),
]
metadata={'original_command':cmd,'status':'running','tests':[]}
for folder,name,c,n,inp,out,seed in cases:
    d=root/folder;d.mkdir(exist_ok=True)
    command=[sys.executable,'-u',str(probe),'--concurrency',str(c),'--requests',str(n),
             '--server-max-seqs','4','--memory-fraction','0.4','--input-tokens',str(inp),
             '--output-tokens',str(out),'--seed',str(seed),'--result',str(d/(name+'.json'))]
    print('TEST '+folder+' '+name,flush=True)
    start=time.monotonic()
    with (d/(name+'.log')).open('w') as log:
        try:
            result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,timeout=900)
            code=result.returncode
        except subprocess.TimeoutExpired:
            code=124
    metadata['tests'].append({'case':name,'exit_code':code,'seconds':time.monotonic()-start})
    (root/'metadata.json').write_text(json.dumps(metadata,indent=2))
    print('DONE '+name+' exit='+str(code),flush=True)
    if code:break
metadata['status']='complete'
(root/'metadata.json').write_text(json.dumps(metadata,indent=2))
print('FINISHED '+str(root),flush=True)
