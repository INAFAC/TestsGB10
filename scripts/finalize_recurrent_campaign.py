#!/usr/bin/env python3
"""Close a fully recorded queue and independently verify restoration on the GB10."""
import argparse
import fcntl
import json
import pathlib
import subprocess
import sys
import time


def ready_to_close(root, queue, meta):
    maximum = next((p for p in queue['profiles'] if p['id'] == 'contexto-maximo-memoria-70'), None)
    if maximum is None:
        return False
    records = {p['id']: p for p in meta['profiles']}
    final = records.get(maximum['id'])
    if final is None or {c['id'] for c in final['cases']} != {c['id'] for c in maximum['cases']}:
        return False
    measured = set()
    for profile in queue['profiles']:
        record = records.get(profile['id'])
        if record is None or not record.get('ready'):
            raise RuntimeError('Unresolved profile: ' + profile['id'])
        cases = {c['id']: c for c in record['cases']}
        if set(cases) != {c['id'] for c in profile['cases']}:
            raise RuntimeError('Unrecorded cases: ' + profile['id'])
        for case in profile['cases']:
            if cases[case['id']].get('interrupted'):
                continue
            folder = root / 'profiles' / profile['id'] / case['id']
            summary = json.loads((folder / 'measurements.json').read_text())['summary']
            if summary['status'] not in ('complete', 'finished_with_errors', 'group_timeout'):
                raise RuntimeError('Unresolved measurement: ' + case['id'])
            measured.add((round(profile['fraction'] * 100), case['users'], case['input_tokens'],
                          case.get('turns', 3), case['id'].startswith('chat-'),
                          summary.get('reasoning_mode'), case.get('output_tokens', 512)))
    required = {(m, 20, n, 3, False, None, 512) for m in (40, 50, 60, 70, 85) for n in (8192, 32768)}
    required |= {(70, u, n, 3, False, None, 512) for u in (10, 30) for n in (8192, 32768)}
    required |= {(70, u, 65536, 2, False, None, 512) for u in (10, 20, 30)}
    required |= {(70, 20, n, 2, False, None, 512) for n in (131072, 260864)}
    required |= {(70, 20, n, 3, True, mode, out) for n, mode in
                 ((8192, 'disabled'), (32768, 'disabled'), (8192, 'server_default')) for out in (512, 2048)}
    if not required <= measured:
        raise RuntimeError('Required campaign coverage missing: ' + repr(required - measured))
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True)
    parser.add_argument('--check', action='store_true', help='Read-only readiness check')
    args = parser.parse_args()
    root = pathlib.Path(args.root)
    lock = (root / 'finalizer.lock').open('a')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    while True:
        queue_path = root / 'queue.json'
        queue = json.loads(queue_path.read_text())
        meta = json.loads((root / 'metadata.json').read_text())
        ready = ready_to_close(root, queue, meta)
        if args.check:
            print(json.dumps({'all_required_attempts_recorded': ready, 'queue_finished': queue.get('finished')}))
            return
        if ready:
            if not queue.get('finished'):
                queue['finished'] = True
                temporary = queue_path.with_suffix('.finalizer.tmp')
                temporary.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n')
                temporary.replace(queue_path)
                print('ALL_REQUIRED_ATTEMPTS_RECORDED_QUEUE_CLOSED', flush=True)
            if meta['state'] == 'stopped':
                if meta.get('restore_status') != 'healthy':
                    raise RuntimeError('Restoration needs review')
                subprocess.run([sys.executable, str(root / 'scripts/verify_recurrent_restore.py'),
                                '--root', str(root)], check=True)
                print('RESTORATION_VERIFIED_FINAL_REPORT_REVIEW_REQUIRED', flush=True)
                return
        time.sleep(45)


if __name__ == '__main__':
    main()
