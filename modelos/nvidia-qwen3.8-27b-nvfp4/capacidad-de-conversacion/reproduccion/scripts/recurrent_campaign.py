#!/usr/bin/env python3
"""Run a reviewable queue of recurrent tests, then restore the captured service."""
import argparse
import datetime
import hashlib
import fcntl
import os
import json
import pathlib
import signal
import subprocess
import sys
import time
import urllib.request


def emit(*args, **kwargs):
    """Losing an observer must not abort a benchmark or its restoration."""
    try:
        print(*args, **kwargs)
    except (BrokenPipeError, OSError):
        sys.stdout = open(os.devnull, 'w')


def run(args):
    return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)


def atomic(path, value):
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    tmp.replace(path)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',required=True)
    p.add_argument('--resume',action='store_true',help='Preserve the captured baseline and skip recorded profiles')
    p.add_argument('--check',action='store_true',help='Validate and show pending profiles without starting them')
    p.add_argument('--compose',default=str(pathlib.Path.home()/'ai/vllm/compose.yaml'))
    a=p.parse_args();root=pathlib.Path(a.root);root.mkdir(exist_ok=True,parents=True)
    lock=(root/'controller.lock').open('a')
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    base=pathlib.Path(a.compose);original=base.read_bytes()
    inspect=lambda:json.loads(run(['docker','inspect','vllm-qwen38']))[0]
    before=inspect();source_hash=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
    if a.resume:
        metadata=json.loads((root/'metadata.json').read_text())
        if hashlib.sha256(original).hexdigest()!=metadata['compose_sha256']:
            raise RuntimeError('Compose differs from the captured baseline')
        if before['Image']!=metadata['image_id']:
            raise RuntimeError('Container image differs from the captured baseline')
        original_cmd=metadata['original_command']
    else:
        if (root/'metadata.json').exists():
            raise RuntimeError('Existing campaign: use --resume; never overwrite its measurements')
        original_cmd=before['Config']['Cmd']
        metadata={'started_utc':stamp,'original_command':original_cmd,'image':before['Config']['Image'],
                  'image_id':before['Image'],'compose_sha256':hashlib.sha256(original).hexdigest(),
                  'runner_sha256':source_hash,'restore_status':'pending','state':'running','profiles':[]}
    queue=json.loads((root/'queue.json').read_text())
    recorded={r['id']:r for r in metadata['profiles']}
    for spec in queue['profiles']:
        previous=recorded.get(spec['id'])
        if previous and previous.get('state')!='startup_failed' and {c['id'] for c in previous['cases']}!={c['id'] for c in spec['cases']}:
            raise RuntimeError('Unrecorded attempt must be preserved before resuming: '+spec['id'])
    if a.check:
        emit(json.dumps({'resume':a.resume,'skip_profiles':list(recorded),
                         'pending_profiles':[r['id'] for r in queue['profiles'] if r['id'] not in recorded]}))
        return
    if a.resume:
        metadata.setdefault('runner_restarts',[]).append({'started_utc':stamp,'script_sha256':source_hash,
            'previous_state':metadata.get('state'),'previous_error':metadata.pop('error',None)})
        metadata['state']='running';metadata['restore_status']='pending'
    persist=lambda:atomic(root/'metadata.json',metadata)
    persist();active=None
    def stopped(signum,frame):raise KeyboardInterrupt('Signal '+str(signum))
    signal.signal(signal.SIGTERM,stopped);signal.signal(signal.SIGINT,stopped);signal.signal(signal.SIGHUP,stopped)
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
            if elapsed-last>=30:emit('STARTUP',label,round(elapsed),flush=True);last=elapsed
            time.sleep(5)
        return False,time.monotonic()-start
    force_recreate=a.resume
    def configure(fraction,limit):
        nonlocal force_recreate
        cmd=[];i=0
        while i<len(original_cmd):
            if original_cmd[i] in ('--gpu-memory-utilization','--max-num-seqs','--max-model-len'):i+=2
            else:cmd.append(original_cmd[i]);i+=1
        cmd+=['--gpu-memory-utilization',str(fraction),'--max-num-seqs',str(limit),'--max-model-len','262144']
        override=root/'override.json';atomic(override,{'services':{'vllm':{'command':cmd}}})
        run(compose+['-f',str(override),'config','--quiet'])
        flags=['--force-recreate'] if force_recreate else []
        emit(run(compose+['-f',str(override),'up','-d']+flags+['vllm']),flush=True)
        force_recreate=False
        return cmd
    def logs(path):path.write_text(run(['docker','logs','vllm-qwen38']))
    try:
        index=0;last_wait=0
        while True:
            queue=json.loads((root/'queue.json').read_text())
            if index>=len(queue['profiles']):
                if queue.get('finished'):break
                metadata['state']='awaiting_next_stage';persist()
                if time.monotonic()-last_wait>45:emit('AWAITING_NEXT_STAGE',index,flush=True);last_wait=time.monotonic()
                time.sleep(5);continue
            spec=queue['profiles'][index]
            if spec['id'] in recorded:
                index+=1;continue
            metadata['state']='running'
            folder=root/'profiles'/spec['id'];folder.mkdir(parents=True,exist_ok=True)
            record={'id':spec['id'],'fraction':spec['fraction'],'server_limit':spec.get('server_limit',32),'cases':[]}
            metadata['profiles'].append(record);persist()
            emit('PROFILE',spec['id'],flush=True)
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
                emit('CASE',spec['id'],case['id'],flush=True)
                start=time.monotonic();last=0;timed_out=False
                with (case_dir/'execution.log').open('w') as log:
                    active=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,text=True)
                    while active.poll() is None:
                        elapsed=time.monotonic()-start
                        if elapsed>case.get('timeout',7200):
                            active.terminate();active.wait(timeout=30);timed_out=True;break
                        if elapsed-last>=30:
                            emit('PROGRESS',case['id'],round(elapsed),flush=True);last=elapsed
                        time.sleep(5)
                    exit_code=active.returncode;active=None
                result={'id':case['id'],'exit_code':exit_code,'duration_seconds':time.monotonic()-start,'timed_out':timed_out}
                if timed_out and (case_dir/'measurements.json').exists():
                    d=json.loads((case_dir/'measurements.json').read_text());d['summary']['status']='group_timeout';atomic(case_dir/'measurements.json',d)
                logs(case_dir/'server.log');record['cases'].append(result);persist()
                emit('CASE_DONE',json.dumps(result),flush=True)
                if exit_code:
                    # Recreate after a failed client so stale requests cannot contaminate the next case.
                    run(compose+['-f',str(root/'override.json'),'up','-d','--force-recreate','vllm'])
                    result['recovery_ready'],result['recovery_seconds']=ready('recovery')
                    persist()
                    if not result['recovery_ready']:raise RuntimeError('Server recovery failed')
            record['state']='complete';persist();index+=1
    except BaseException as exc:
        metadata['error']=repr(exc)
        if active is not None:
            if active.poll() is None:
                active.terminate();active.wait(timeout=30)
            result={'id':case['id'],'exit_code':active.returncode,
                    'duration_seconds':time.monotonic()-start,'timed_out':False,
                    'interrupted':True,'interruption_reason':repr(exc)}
            record['cases'].append(result);record['state']='interrupted';active=None
            try:logs(case_dir/'server.log')
            except Exception as log_error:result['log_capture_error']=repr(log_error)
        persist();raise
    finally:
        if active is not None and active.poll() is None:active.terminate();active.wait(timeout=30)
        metadata['state']='restoring';persist();emit('RESTORING',flush=True)
        if base.read_bytes()!=original:
            metadata['restore_status']='source_changed';persist();raise RuntimeError('Compose changed externally')
        restore=root/'restore-override.json';atomic(restore,{'services':{'vllm':{'command':original_cmd}}})
        run(compose+['-f',str(restore),'up','-d','vllm'])
        ok,seconds=ready('original');after=inspect()
        metadata['restore_status']='healthy' if ok and after['Config']['Cmd']==original_cmd and after['Image']==before['Image'] else 'failed'
        metadata['restore_seconds']=seconds;metadata['restored_command']=after['Config']['Cmd']
        metadata['state']='stopped';logs(root/'restored-server.log');persist()
        emit('RESTORED',metadata['restore_status'],flush=True)


if __name__=='__main__':main()
