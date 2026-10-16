#!/usr/bin/env python3
"""Find measured chat-capacity boundaries and restore the captured service."""
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True)
    parser.add_argument('--compose', default=str(pathlib.Path.home()/'ai/vllm/compose.yaml'))
    args = parser.parse_args()
    root = pathlib.Path(args.root)
    plan = json.loads((root/'plan.json').read_text())
    lock = (root/'capacity.lock').open('a')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    if (root/'metadata.json').exists():
        raise RuntimeError('Existing measurements: preserve them and explicitly plan a new attempt')
    base = pathlib.Path(args.compose)
    source = base.read_bytes()
    inspect = lambda: json.loads(run(['docker','inspect','vllm-qwen38']))[0]
    before = inspect()
    original = before['Config']['Cmd']
    meta = dict(started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        original_command=original, image=before['Config']['Image'], image_id=before['Image'],
        compose_sha256=hashlib.sha256(source).hexdigest(), state='running',
        restore_status='pending', profiles=[], boundaries=[],
        script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
    persist = lambda: atomic(root/'metadata.json', meta)
    persist()
    active = None
    active_limit = None
    current_case = None
    compose = ['docker','compose','-f',str(base)]

    def stopped(signum, frame):
        raise KeyboardInterrupt('Signal '+str(signum))
    for sig in (signal.SIGTERM,signal.SIGINT,signal.SIGHUP):
        signal.signal(sig,stopped)

    def ready():
        started = time.monotonic()
        while time.monotonic()-started < 1200:
            try:
                if urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=5).status == 200:
                    return True, time.monotonic()-started
            except Exception:
                pass
            status = inspect()
            if status['RestartCount'] or status['State']['Status'] in ('exited','dead','restarting'):
                return False, time.monotonic()-started
            time.sleep(5)
        return False, time.monotonic()-started

    def idle():
        raw = urllib.request.urlopen('http://127.0.0.1:8000/metrics',timeout=10).read().decode()
        for key in ('num_requests_running','num_requests_waiting'):
            vals = re.findall(r'^vllm:'+key+r'(?:\{[^\n]*\})? ([^\n]+)',raw,re.M)
            if not vals or any(float(v) for v in vals):
                return False
        return True

    def configure(fraction, limit):
        nonlocal active_limit
        if base.read_bytes()!=source:
            raise RuntimeError('Compose changed externally')
        command=[]; i=0
        while i<len(original):
            if original[i] in ('--gpu-memory-utilization','--max-num-seqs','--max-model-len'):
                i+=2
            else:
                command.append(original[i]); i+=1
        command += ['--gpu-memory-utilization',str(fraction),'--max-num-seqs',str(limit),'--max-model-len','262144']
        override=root/'override.json'
        atomic(override,{'services':{'vllm':{'command':command}}})
        run(compose+['-f',str(override),'config','--quiet'])
        run(compose+['-f',str(override),'up','-d','--force-recreate','vllm'])
        ok,seconds=ready()
        record=dict(fraction=fraction,server_limit=limit,command=command,ready=ok,startup_seconds=seconds)
        meta['profiles'].append(record)
        (root/f'arranque-{len(meta["profiles"]):02d}.log').write_text(run(['docker','logs','vllm-qwen38']))
        persist()
        active_limit=limit
        return ok

    def measure(fraction, context, users, repetition, purpose='boundary', reasoning='disabled'):
        nonlocal active,current_case
        kind='recorrido-completo' if purpose=='boundary' else 'control-con-razonamiento'
        name=f'memoria-{round(fraction*100)}-personas-{users}-{kind}-intento-{repetition}'
        folder=root/'pruebas'/name
        folder.mkdir(parents=True)
        config=dict(id=name,memory_fraction=fraction,input_tokens=context,users=users,
            repetition=repetition,purpose=purpose,reasoning=reasoning,
            server_limit=max(4,users),turns=plan['turns'],think_seconds=plan['think_seconds'],
            output_tokens=plan['output_tokens'] if reasoning=='disabled' else 4096,
            seed=plan['seed']+context+repetition*1000000+users*10000,
            schedule='simultaneous')
        if purpose=='boundary':
            config['turns']=len(range(context,262144-config['output_tokens'],plan['growth_step_tokens']))+2
        atomic(folder/'configuracion.json',config)
        if active_limit!=config['server_limit'] and not configure(fraction,config['server_limit']):
            meta.setdefault('cases',[]).append(dict(id=name,state='startup_failed',acceptable_reference=False))
            persist()
            return False,name
        command=[sys.executable,'-u',str(root/'capacity_probe.py'),
            '--concurrency',str(users),'--server-max-seqs',str(config['server_limit']),
            '--memory-fraction',str(fraction),'--input-tokens',str(context),
            '--output-tokens',str(config['output_tokens']),'--turns',str(config['turns']),
            '--think-seconds',str(config['think_seconds']),'--seed',str(config['seed']),
            '--case-id',name,'--reasoning',reasoning,'--request-timeout','1800',
            '--followup-timeout','120','--test-timeout',str(plan['trajectory_timeout_seconds']),
            '--result',str(folder/'mediciones.json'),'--state-output',str(folder/'historiales.json.gz')]
        if purpose=='boundary':
            command+=['--grow-to-context-limit','--growth-step',str(plan['growth_step_tokens'])]
            config['grows_from_short_to_full']=True
            atomic(folder/'configuracion.json',config)
        current_case=dict(id=name,state='running',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        meta.setdefault('cases',[]).append(current_case); persist()
        emit('CASE',name,flush=True)
        started=time.monotonic()
        with (folder/'ejecucion.log').open('w') as log:
            active=subprocess.Popen(command,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT)
            timed_out=False
            while active.poll() is None:
                if time.monotonic()-started>plan['trajectory_timeout_seconds']:
                    active.terminate()
                    try: active.wait(timeout=15)
                    except subprocess.TimeoutExpired: active.kill();active.wait()
                    timed_out=True;break
                time.sleep(5)
            code=active.returncode;active=None
        current_case.update(state='finished',exit_code=code,timed_out=timed_out,duration_seconds=time.monotonic()-started)
        result=json.loads((folder/'mediciones.json').read_text()) if (folder/'mediciones.json').exists() else None
        passed=bool(code==0 and result and result['summary']['status']=='complete' and result['summary']['acceptable_reference'])
        current_case['acceptable_reference']=passed
        (folder/'servidor.log').write_text(run(['docker','logs','vllm-qwen38']))
        persist();emit('CASE_DONE',json.dumps(current_case),flush=True)
        for _ in range(30):
            if idle():break
            time.sleep(2)
        else:
            if not configure(fraction,config['server_limit']):
                raise RuntimeError('Recovery failed')
        return passed,name

    try:
        if not idle():
            raise RuntimeError('Service has active requests before the campaign')
        index=0
        while True:
            plan=json.loads((root/'plan.json').read_text())
            if index>=len(plan['memory_fractions']):
                if plan.get('finished'):break
                meta['state']='awaiting_maximum_memory_profile';persist()
                time.sleep(5);continue
            fraction=plan['memory_fractions'][index]
            index+=1
            meta['state']='running';persist()
            if not configure(fraction,4):
                meta['boundaries'].append(dict(memory_fraction=fraction,state='startup_failed'))
                persist();continue
            for context in plan['contexts']:
                cell=dict(memory_fraction=fraction,input_tokens=context,state='running',attempts=[],
                    largest_confirmed_acceptable=0,first_confirmed_unacceptable=None)
                meta['boundaries'].append(cell);persist()
                counts={}
                def check(users):
                    # Full trajectories supply hundreds of real successive turns.
                    # Failed trajectories stop after sustained degradation, not
                    # after an isolated slow response.
                    outcomes=[]
                    for repetition in range(1,plan['repetitions_per_user_count']+1):
                        passed,name=measure(fraction,context,users,repetition)
                        outcomes.append(passed);cell['attempts'].append(name);persist()
                    counts[users]=outcomes
                    cell['observations']={str(k):v for k,v in sorted(counts.items())}
                    persist()
                    return all(outcomes)
                low=0;high=None;users=1
                while users<=plan['max_users']:
                    if check(users):
                        low=users
                        if users==plan['max_users']:break
                        users=min(plan['max_users'],users*2)
                    else:
                        high=users;break
                # If one user fails, also measure two: a failed single-user trial
                # must not be silently generalized to all concurrency values.
                if low==0 and high==1:
                    if check(2):
                        low=2;high=None
                        users=4
                        while users<=plan['max_users']:
                            if check(users):
                                low=users
                                if users==plan['max_users']:break
                                users=min(plan['max_users'],users*2)
                            else:high=users;break
                while high is not None and high-low>1:
                    mid=(low+high)//2
                    if check(mid):low=mid
                    else:high=mid
                cell.update(state='complete',largest_confirmed_acceptable=low,
                    first_not_confirmed_acceptable=high,
                    first_confirmed_unacceptable=high if high is not None and not any(counts[high]) else None,
                    reached_search_ceiling=high is None,
                    nonmonotonic=any(not all(v) and k<low for k,v in counts.items()))
                persist()
                # Near the full context, explicitly compare the server's default
                # reasoning mode. These controls do not establish its full boundary.
                if context==max(plan['contexts']):
                    for n in sorted({1,low} - {0}):
                        _,name=measure(fraction,8192,n,3,purpose='control-razonamiento',reasoning='default')
                        cell.setdefault('default_reasoning_controls',[]).append(name);persist()
        meta['measurements_complete']=True;persist()
    except BaseException as exc:
        meta['error']=repr(exc)
        if active is not None:
            if active.poll() is None:
                active.terminate()
                try:active.wait(timeout=15)
                except subprocess.TimeoutExpired:active.kill();active.wait()
            if current_case is not None:
                current_case.update(state='interrupted',exit_code=active.returncode,reason=repr(exc))
            active=None
        persist()
    finally:
        meta['state']='restoring';persist()
        if base.read_bytes()!=source:
            meta['restore_status']='source_changed';persist()
            raise RuntimeError('Compose changed externally; captured command not applied')
        override=root/'restore-override.json'
        atomic(override,{'services':{'vllm':{'command':original}}})
        run(compose+['-f',str(override),'up','-d','vllm'])
        ok,seconds=ready();after=inspect()
        meta.update(state='stopped',restore_seconds=seconds,
            restore_status='healthy' if ok and after['Config']['Cmd']==original and after['Image']==before['Image'] else 'failed')
        persist()
        proof=subprocess.run([sys.executable,str(root/'verify_recurrent_restore.py'),'--root',str(root),'--compose',str(base)])
        if proof.returncode:raise RuntimeError('Independent restoration verification failed')
    if meta.get('error'):raise SystemExit(1)


if __name__=='__main__':
    main()
