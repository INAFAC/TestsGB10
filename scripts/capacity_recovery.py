#!/usr/bin/env python3
"""Repeat interrupted measurements after the original campaign has restored service."""
import argparse
import datetime
import fcntl
import hashlib
import json
import pathlib
import re
import signal
import subprocess
import sys
import time
import urllib.request

from recurrent_campaign import atomic, emit, run


def read(path):
    return json.loads(path.read_text())


def pending_cases(root, meta):
    pending=[]
    for case in meta.get('cases',[]):
        path=root/'pruebas'/case['id']/'mediciones.json'
        if case['state']=='running' or case.get('resolved_by') or not path.exists():
            continue
        if read(path)['summary']['status'] in ('running','measurement_error'):
            pending.append(case)
    return pending


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',required=True)
    parser.add_argument('--compose',default=str(pathlib.Path.home()/'ai/vllm/compose.yaml'))
    parser.add_argument('--check-only',action='store_true')
    args=parser.parse_args();root=pathlib.Path(args.root)
    meta=read(root/'metadata.json');plan=read(root/'plan.json')
    pending=pending_cases(root,meta)
    if args.check_only:
        print(json.dumps({'state':meta['state'],'pending':[c['id'] for c in pending]}));return
    lock=(root/'capacity.lock').open('a')
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    if meta['state']!='stopped' or meta.get('restore_status')!='healthy':
        raise RuntimeError('The original campaign must finish and restore service first')
    proof=read(root/'verificacion-final.json')
    if not proof['verified'] or proof['command']!=meta['original_command']:
        raise RuntimeError('Independent original-service verification is required')
    if not pending:
        print('No interrupted measurements require recovery');return
    if any(not read(root/'pruebas'/c['id']/'configuracion.json').get('grows_from_short_to_full') for c in pending):
        raise RuntimeError('An interrupted reasoning control needs a separately reviewed recovery')
    base=pathlib.Path(args.compose);source=base.read_bytes()
    inspect=lambda:json.loads(run(['docker','inspect','vllm-qwen38']))[0]
    before=inspect();original=meta['original_command']
    if before['Config']['Cmd']!=original or before['Image']!=meta['image_id'] or hashlib.sha256(source).hexdigest()!=meta['compose_sha256']:
        raise RuntimeError('Service changed after restoration; do not overwrite external changes')
    version=root/'revisiones'/datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    version.mkdir(parents=True)
    atomic(version/'metadata-antes-de-repetir.json',meta)
    atomic(version/'verificacion-anterior.json',proof)
    recovery={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'pending':[c['id'] for c in pending],'state':'running'}
    meta.setdefault('recoveries',[]).append(recovery)
    persist=lambda:atomic(root/'metadata.json',meta)
    compose=['docker','compose','-f',str(base)]
    active=None;current=None;active_limit=None

    def interrupt(signum,frame):
        raise KeyboardInterrupt('Signal '+str(signum))
    for sig in (signal.SIGTERM,signal.SIGINT,signal.SIGHUP):signal.signal(sig,interrupt)

    def idle():
        raw=urllib.request.urlopen('http://127.0.0.1:8000/metrics',timeout=10).read().decode()
        for key in ('num_requests_running','num_requests_waiting'):
            values=re.findall(r'^vllm:'+key+r'(?:\{[^\n]*\})? ([^\n]+)',raw,re.M)
            if not values or any(float(v) for v in values):return False
        return True

    def ready():
        start=time.monotonic()
        while time.monotonic()-start<1200:
            try:
                if urllib.request.urlopen('http://127.0.0.1:8000/health',timeout=5).status==200:return True,time.monotonic()-start
            except Exception:pass
            state=inspect()
            if state['RestartCount'] or state['State']['Status'] in ('exited','dead','restarting'):break
            time.sleep(5)
        return False,time.monotonic()-start

    def configure(fraction,limit):
        nonlocal active_limit
        if base.read_bytes()!=source:raise RuntimeError('Compose changed externally')
        command=[];i=0
        while i<len(original):
            if original[i] in ('--gpu-memory-utilization','--max-num-seqs','--max-model-len'):i+=2
            else:command.append(original[i]);i+=1
        command+=['--gpu-memory-utilization',str(fraction),'--max-num-seqs',str(limit),'--max-model-len','262144']
        override=root/'recovery-override.json';atomic(override,{'services':{'vllm':{'command':command}}})
        run(compose+['-f',str(override),'config','--quiet'])
        run(compose+['-f',str(override),'up','-d','--force-recreate','vllm'])
        ok,seconds=ready()
        meta['profiles'].append(dict(fraction=fraction,server_limit=limit,command=command,ready=ok,startup_seconds=seconds,recovery=True))
        (root/f'arranque-{len(meta["profiles"]):02d}.log').write_text(run(['docker','logs','vllm-qwen38']))
        persist();active_limit=limit
        if not ok:raise RuntimeError('Recovery configuration failed to start')

    def measure(fraction,users,reasoning='disabled'):
        nonlocal active,current
        context=512 if reasoning=='disabled' else 8192
        kind='recorrido-completo' if reasoning=='disabled' else 'control-con-razonamiento'
        prefix=f'memoria-{round(fraction*100)}-personas-{users}-{kind}-intento-'
        repetition=1+max((int(c['id'].split('-')[-1]) for c in meta['cases'] if c['id'].startswith(prefix)),default=0)
        name=prefix+str(repetition);folder=root/'pruebas'/name;folder.mkdir(parents=True)
        if active_limit!=max(4,users):configure(fraction,max(4,users))
        config=dict(id=name,memory_fraction=fraction,input_tokens=context,users=users,repetition=repetition,
                    purpose='boundary' if reasoning=='disabled' else 'control-razonamiento',reasoning=reasoning,
                    server_limit=max(4,users),turns=257 if reasoning=='disabled' else 5,
                    think_seconds=plan['think_seconds'],output_tokens=1024 if reasoning=='disabled' else 4096,
                    seed=plan['seed']+context+(1000000 if reasoning=='disabled' else 3000000)+users*10000,
                    schedule='simultaneous',grows_from_short_to_full=reasoning=='disabled',
                    growth_protocol_version=2,seed_reuses_original_attempt=True)
        atomic(folder/'configuracion.json',config)
        command=[sys.executable,'-u',str(root/'capacity_probe_v2.py'),'--concurrency',str(users),
                 '--server-max-seqs',str(config['server_limit']),'--memory-fraction',str(fraction),
                 '--input-tokens',str(context),'--output-tokens',str(config['output_tokens']),
                 '--turns',str(config['turns']),'--think-seconds',str(config['think_seconds']),
                 '--seed',str(config['seed']),'--case-id',name,'--reasoning',reasoning,
                 '--request-timeout','1800','--followup-timeout','120','--test-timeout',str(plan['trajectory_timeout_seconds']),
                 '--result',str(folder/'mediciones.json'),'--state-output',str(folder/'historiales.json.gz')]
        if reasoning=='disabled':command+=['--grow-to-context-limit','--growth-step',str(plan['growth_step_tokens'])]
        current=dict(id=name,state='running',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),recovery=True)
        meta['cases'].append(current);persist();emit('CASE',name,flush=True);start=time.monotonic()
        with (folder/'ejecucion.log').open('w') as log:
            active=subprocess.Popen(command,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT)
            try:code=active.wait(timeout=plan['trajectory_timeout_seconds'])
            except subprocess.TimeoutExpired:
                active.terminate()
                try:active.wait(timeout=15)
                except subprocess.TimeoutExpired:active.kill();active.wait()
                raise RuntimeError('Recovery trajectory exceeded its deadline')
        active=None
        current.update(state='finished',exit_code=code,timed_out=False,duration_seconds=time.monotonic()-start)
        data=read(folder/'mediciones.json');s=data['summary']
        passed=bool(code==0 and s['status']=='complete' and s['acceptable_reference'])
        current['acceptable_reference']=passed
        (folder/'servidor.log').write_text(run(['docker','logs','vllm-qwen38']))
        persist();emit('CASE_DONE',json.dumps(current),flush=True)
        if s['status'] not in ('complete','stopped_early'):raise RuntimeError('Recovery medidor did not produce a valid terminal measurement')
        for _ in range(30):
            if idle():break
            time.sleep(2)
        else:configure(fraction,max(4,users))
        return passed,name

    try:
        if not idle():raise RuntimeError('Service has active requests before recovery')
        meta.update(state='running',restore_status='pending',measurements_complete=False,error=None);persist()
        fractions=sorted({read(root/'pruebas'/c['id']/'configuracion.json')['memory_fraction'] for c in pending})
        for fraction in fractions:
            configure(fraction,4)
            old=[c for c in pending if read(root/'pruebas'/c['id']/'configuracion.json')['memory_fraction']==fraction]
            # Keep valid old observations; an interrupted process is not a failure observation.
            valid=[];counts={}
            for c in meta['cases']:
                config=read(root/'pruebas'/c['id']/'configuracion.json')
                path=root/'pruebas'/c['id']/'mediciones.json'
                if config['memory_fraction']!=fraction or not config.get('grows_from_short_to_full') or not path.exists():continue
                if read(path)['summary']['status'] not in ('complete','stopped_early'):continue
                counts[config['users']]=[bool(c.get('acceptable_reference'))];valid.append(c['id'])
            cell=dict(memory_fraction=fraction,input_tokens=512,state='running',attempts=valid,
                      largest_confirmed_acceptable=0,first_confirmed_unacceptable=None,recovery_of=[c['id'] for c in old])
            meta['boundaries'].append(cell);persist()
            def check(users):
                passed,name=measure(fraction,users);counts[users]=[passed];cell['attempts'].append(name)
                cell['observations']={str(k):v for k,v in sorted(counts.items())}
                for c in old:
                    if read(root/'pruebas'/c['id']/'configuracion.json')['users']==users:c['resolved_by']=name
                persist();return passed
            for users in sorted({read(root/'pruebas'/c['id']/'configuracion.json')['users'] for c in old}):check(users)
            low=max((n for n,v in counts.items() if all(v)),default=0)
            high=min((n for n,v in counts.items() if not all(v) and n>low),default=None)
            if low==0 and 2 not in counts:check(2);low=2 if all(counts[2]) else 0
            if low==0:high=min(counts)
            while low and high is None and low<plan['max_users']:
                users=min(plan['max_users'],low*2)
                if check(users):low=users
                else:high=users
            while high is not None and high-low>1:
                users=(low+high)//2
                if check(users):low=users
                else:high=users
            cell.update(state='complete',largest_confirmed_acceptable=low,first_not_confirmed_acceptable=high,
                        first_confirmed_unacceptable=high,reached_search_ceiling=high is None,
                        observations={str(k):v for k,v in sorted(counts.items())},
                        nonmonotonic=any(not all(v) and n<low for n,v in counts.items()))
            persist()
            for users in sorted({1,low}-{0}):
                controls=[c['id'] for c in meta['cases'] if c['state']=='finished' and c['id'].startswith(f'memoria-{round(fraction*100)}-personas-{users}-control-con-razonamiento-')]
                if controls:name=controls[-1]
                else:_,name=measure(fraction,users,'default')
                cell.setdefault('default_reasoning_controls',[]).append(name);persist()
        if pending_cases(root,meta):raise RuntimeError('Interrupted measurements still unresolved')
        meta['measurements_complete']=True;recovery['state']='complete';persist()
    except BaseException as exc:
        recovery.update(state='interrupted',error=repr(exc));meta['error']=repr(exc)
        if active is not None:
            active.terminate()
            try:active.wait(timeout=15)
            except subprocess.TimeoutExpired:active.kill();active.wait()
            if current is not None:current.update(state='interrupted',exit_code=active.returncode,reason=repr(exc))
        persist()
    finally:
        meta['state']='restoring';persist()
        if base.read_bytes()!=source:meta['restore_status']='source_changed';persist();raise RuntimeError('Compose changed externally')
        override=root/'restore-override.json';atomic(override,{'services':{'vllm':{'command':original}}})
        run(compose+['-f',str(override),'up','-d','vllm'])
        ok,seconds=ready();after=inspect()
        meta.update(state='stopped',restore_seconds=seconds,restore_status='healthy' if ok and after['Config']['Cmd']==original and after['Image']==meta['image_id'] else 'failed')
        recovery['ended_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();persist()
        result=subprocess.run([sys.executable,str(root/'verify_recurrent_restore.py'),'--root',str(root),'--compose',str(base)])
        if result.returncode:raise RuntimeError('Independent restoration verification failed')
    if recovery['state']!='complete':raise SystemExit(1)


if __name__=='__main__':main()
