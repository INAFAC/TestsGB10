#!/usr/bin/env python3
"""Validate report links and numerical consistency without contacting the server."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors = []
checked = 0
for path in (ROOT/'results').rglob('*.json'):
    try:
        d = json.loads(path.read_text())
    except ValueError as e:
        errors.append(f'{path}: invalid JSON: {e}')
        continue
    if not isinstance(d, dict):
        continue
    s = d.get('summary', {})
    if 'input_tokens' not in s:
        continue
    checked += 1
    requests = d.get('requests', [])
    good = [r for r in requests if r.get('ok')]
    count = s.get('num_requests', s['concurrency'])
    if s['completed'] != len(good):
        errors.append(f'{path}: completion count mismatch')
    if len({r['index'] for r in requests}) != len(requests):
        errors.append(f'{path}: duplicate request index')
    if s.get('status') == 'complete' and len(requests) != count:
        errors.append(f'{path}: complete but missing requests')
    for r in good:
        u = r['usage']
        if (u['prompt_tokens'], u['completion_tokens']) != (s['input_tokens'], s['output_tokens']):
            errors.append(f'{path}: token count mismatch')
        if not 0 <= r['ttft_s'] <= r['total_s'] <= s['duration_s']:
            errors.append(f'{path}: inconsistent request times')
        if r.get('first_token_at_s') is not None:
            if not 0 <= r['started_at_s'] <= r['first_token_at_s'] <= r['finished_at_s'] <= s['duration_s']:
                errors.append(f'{path}: inconsistent timeline')
            if abs((r['first_token_at_s']-r['started_at_s'])-r['ttft_s']) > .01:
                errors.append(f'{path}: TTFT does not match timeline')
    for key in ['preemptions', 'peak_running', 'peak_waiting']:
        if s.get(key) is not None and s[key] < 0:
            errors.append(f'{path}: negative {key}')
for path in [ROOT/'README.md', *(ROOT/'details').glob('*.md')]:
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        if not (path.parent/target.split('#')[0]).exists():
            errors.append(f'{path}: broken link {target}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Validated {checked} measured tests and all Markdown links.')
