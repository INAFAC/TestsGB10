#!/usr/bin/env python3
"""Queue the maximum-context test only after verifying a completed parent history."""
import argparse
import fcntl
import gzip
import json
import pathlib
import time

p=argparse.ArgumentParser()
p.add_argument('--root',required=True)
a=p.parse_args();root=pathlib.Path(a.root)
lock=(root/'advance-maximum.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
while True:
    meta=json.loads((root/'metadata.json').read_text())
    queue_path=root/'queue.json';queue=json.loads(queue_path.read_text())
    if queue.get('finished') or meta.get('restore_status')!='pending':
        raise RuntimeError('Campaign closed before the maximum stage was queued')
    completed={(profile['id'],case['id']):case for profile in meta['profiles'] for case in profile['cases']}
    successful=[];pending=False
    for profile in queue['profiles']:
        if profile['fraction']!=.7 or profile.get('server_limit')!=32:continue
        for case in profile['cases']:
            if (case['users'],case['input_tokens'],case.get('turns',3))!=(20,131072,2):continue
            record=completed.get((profile['id'],case['id']))
            if record is None:
                pending=True;continue
            if record.get('interrupted') or record.get('exit_code')!=0:continue
            folder=root/'profiles'/profile['id']/case['id']
            data=json.loads((folder/'measurements.json').read_text());s=data['summary']
            if s['status']=='complete' and s['all_turns_completed'] and s['completed']==40 and not s['failed']:
                successful.append((folder,data))
    if successful:
        folder,data=successful[-1];s=data['summary']
        state=json.loads(gzip.decompress((folder/'histories.json.gz').read_bytes()))
        assert set(state['histories'])=={str(i) for i in range(20)}
        for user in range(20):
            history=state['histories'][str(user)]
            records=sorted((r for r in data['requests'] if r['user_id']==user),key=lambda r:r['turn'])
            assert len(history)==132352 and len(records)==2 and all(r['ok'] for r in records)
            assert history[131072:131584]==records[0]['generated_token_ids']
            assert history[-512:]==records[1]['generated_token_ids']
        case={'id':'20-usuarios-historial-260864-dos-turnos','users':20,'input_tokens':260864,
              'turns':2,'seed':20260864,'output_tokens':512,'think_seconds':30,
              'timeout':28800,'request_timeout':21600,'parent_state':str(folder/'histories.json.gz')}
        profile={'id':'contexto-maximo-memoria-70','fraction':.7,'server_limit':32,'cases':[case]}
        existing=next((v for v in queue['profiles'] if v['id']==profile['id']),None)
        if existing is not None:assert existing==profile
        else:
            queue['profiles'].append(profile)
            temporary=queue_path.with_suffix('.maximum.tmp')
            temporary.write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n');temporary.replace(queue_path)
        print(json.dumps({'maximum_queued':True,'parent_case':folder.name,'queue_remains_open':True}),flush=True)
        break
    if not pending:raise RuntimeError('No successful or pending 131072-token parent; review the failed attempt')
    time.sleep(45)
