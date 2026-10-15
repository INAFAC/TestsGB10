#!/usr/bin/env python3
"""Run a reviewable queue of recurrent tests, then restore the captured service."""
import argparse
import datetime
import hashlib
import json
import pathlib
import signal
import subprocess
import sys
import time
import urllib.request


def run(args):
    return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)


def atomic(path, value):
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    tmp.replace(path)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',required=True)
    p.add_argument('--compose',default=str(pathlib.Path.home()/'ai/vllm/compose.yaml'))
    a=p.parse_args();root=pathlib.Path(a.root);root.mkdir(exist_ok=True,parents=True)
    base=pathlib.Path(a.compose);original=base.read_bytes()
    inspect=lambda:json.loads(run(['docker','inspect','vllm-qwen38']))[0]
    before=inspect();original_cmd=before['Config']['Cmd']
    metadata={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'original_command':original_cmd,'image':before['Config']['Image'],
              'image_id':before['Image'],'compose_sha256':hashlib.sha256(original).hexdigest(),
              'runner_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'restore_status':'pending','state':'running','profiles':[]}
    persist=lambda:atomic(root/'metadata.json',metadata)
    persist();active=None
    def stopped(signum,frame):raise KeyboardInterrupt('Signal '+str(signum))
    signal.signal(signal.SIGTERM,stopped);signal.signal(signal.SIGINT,stopped)
    compose=['docker','compose','-f',str(base)]
    def health():
        try:return urllib.request.urlopen('http://127.0.0.1:8000/health',timeout=5).status==200
        except Exception:return False
    def ready(label):
        start=time.monotonic();last=0
        while time.monotonic()-start<900:
            if health():return True,time.monotonic()-start
            c=inspect()
            if c['RestartCount'] or c['State']['Status'] in ('exited','dead','restarting'):return False,time.monotonic()-start
            elapsed=time.monotonic()-start
            if elapsed-last>=30:print('STARTUP',label,round(elapsed),flush=True);last=elapsed
            time.sleep(5)
        return False,time.monotonic()-start
    def configure(fraction,limit):
        cmd=[];i=0
        while i<len(original_cmd):
            if original_cmd[i] in ('--gpu-memory-utilization','--max-num-seqs','--max-model-len'):i+=2
            else:cmd.append(original_cmd[i]);i+=1
        cmd+=['--gpu-memory-utilization',str(fraction),'--max-num-seqs',str(limit),'--max-model-len','262144']
        override=root/'override.json';atomic(override,{'services':{'vllm':{'command':cmd}}})
        run(compose+['-f',str(override),'config','--quiet'])
        print(run(compose+['-f',str(override),'up','-d','vllm']),flush=True)
        return cmd
    def logs(path):path.write_text(run(['docker','logs','vllm-qwen38']))
    try:
        index=0;last_wait=0
        while True:
            queue=json.loads((root/'queue.json').read_text())
            if index>=len(queue['profiles']):
                if queue.get('finished'):break
                metadata['state']='awaiting_next_stage';persist()
                if time.monotonic()-last_wait>45:print('AWAITING_NEXT_STAGE',index,flush=True);last_wait=time.monotonic()
                time.sleep(5);continue
            spec=queue['profiles'][index];metadata['state']='running'
            folder=root/'profiles'/spec['id'];folder.mkdir(parents=True,exist_ok=True)
            record={'id':spec['id'],'fraction':spec['fraction'],'server_limit':spec.get('server_limit',32),'cases':[]}
            metadata['profiles'].append(record);persist()
            print('PROFILE',spec['id'],flush=True)
            record['command']=configure(spec['fraction'],record['server_limit'])
            record['ready'],record['startup_seconds']=ready(spec['id'])
            logs(folder/'startup.log');persist()
            if not record['ready']:
                record['state']='startup_failed';persist();index+=1;continue
            for case in spec['cases']:
                case_dir=folder/case['id'];case_dir.mkdir(exist_ok=True)
                config=dict(case,memory_fraction=spec['fraction'],server_limit=record['server_limit'],profile_id=spec['id'])
                atomic(case_dir/'configuration.json',config)
                command=[sys.executable,'-u',str(pathlib.Path(__file__).with_name('recurrent_probe.py')),
                         '--concurrency',str(case['users']),'--server-max-seqs',str(record['server_limit']),
                         '--memory-fraction',str(spec['fraction']),'--input-tokens',str(case['input_tokens']),
                         '--output-tokens',str(case.get('output_tokens',512)),'--turns',str(case.get('turns',3)),
                         '--think-seconds',str(case.get('think_seconds',30)),'--new-message-tokens','256',
                         '--request-timeout',str(case.get('request_timeout',3600)),
                         '--test-timeout',str(case.get('timeout',7200)),
                         '--seed',str(case['seed']),'--case-id',case['id'],
                         '--result',str(case_dir/'measurements.json'),'--state-output',str(case_dir/'histories.json.gz')]
                if case.get('parent_state'):command+=['--parent-state',case['parent_state']]
                atomic(case_dir/'executed-command.json',command)
                print('CASE',spec['id'],case['id'],flush=True)
                start=time.monotonic();last=0;timed_out=False
                with (case_dir/'execution.log').open('w') as log:
                    active=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,text=True)
                    while active.poll() is None:
                        elapsed=time.monotonic()-start
                        if elapsed>case.get('timeout',7200):
                            active.terminate();active.wait(timeout=30);timed_out=True;break
                        if elapsed-last>=30:
                            print('PROGRESS',case['id'],round(elapsed),flush=True);last=elapsed
                        time.sleep(5)
                    exit_code=active.returncode;active=None
                result={'id':case['id'],'exit_code':exit_code,'duration_seconds':time.monotonic()-start,'timed_out':timed_out}
                if timed_out and (case_dir/'measurements.json').exists():
                    d=json.loads((case_dir/'measurements.json').read_text());d['summary']['status']='group_timeout';atomic(case_dir/'measurements.json',d)
                logs(case_dir/'server.log');record['cases'].append(result);persist()
                print('CASE_DONE',json.dumps(result),flush=True)
                if exit_code:
                    # Recreate after a failed client so stale requests cannot contaminate the next case.
                    run(compose+['-f',str(root/'override.json'),'up','-d','--force-recreate','vllm'])
                    result['recovery_ready'],result['recovery_seconds']=ready('recovery')
                    persist()
                    if not result['recovery_ready']:raise RuntimeError('Server recovery failed')
            record['state']='complete';persist();index+=1
    except BaseException as exc:
        metadata['error']=repr(exc);persist();raise
    finally:
        if active is not None and active.poll() is None:active.terminate();active.wait(timeout=30)
        metadata['state']='restoring';persist();print('RESTORING',flush=True)
        if base.read_bytes()!=original:
            metadata['restore_status']='source_changed';persist();raise RuntimeError('Compose changed externally')
        restore=root/'restore-override.json';atomic(restore,{'services':{'vllm':{'command':original_cmd}}})
        run(compose+['-f',str(restore),'up','-d','vllm'])
        ok,seconds=ready('original');after=inspect()
        metadata['restore_status']='healthy' if ok and after['Config']['Cmd']==original_cmd and after['Image']==before['Image'] else 'failed'
        metadata['restore_seconds']=seconds;metadata['restored_command']=after['Config']['Cmd']
        metadata['state']='stopped';logs(root/'restored-server.log');persist()
        print('RESTORED',metadata['restore_status'],flush=True)


if __name__=='__main__':main()
