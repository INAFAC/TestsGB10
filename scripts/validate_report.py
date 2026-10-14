#!/usr/bin/env python3
"""Check source preservation, response lengths, timing consistency and report links."""
import hashlib
import json
import pathlib
import re
ROOT=pathlib.Path(__file__).resolve().parents[1]
errors=[];checked=0
for path in (ROOT/'modelos').rglob('*.json'):
    try:d=json.loads(path.read_text())
    except ValueError as e:
        errors.append(f'{path}: invalid JSON: {e}');continue
    if path.name=='inventario-de-archivos-originales.json':
        for entry in d:
            target=ROOT/entry['archivo']
            if not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest()!=entry['sha256']:
                errors.append(f'Original file changed or missing: {target}')
    if not isinstance(d,dict):continue
    s=d.get('summary',{})
    if 'input_tokens' not in s:continue
    checked+=1;requests=d.get('requests',[]);good=[r for r in requests if r.get('ok')]
    count=s.get('num_requests',s['concurrency'])
    if s['completed']!=len(good):errors.append(f'{path}: completion count mismatch')
    if len({r['index'] for r in requests})!=len(requests):errors.append(f'{path}: duplicate request')
    if s.get('status')=='complete' and len(requests)!=count:errors.append(f'{path}: complete with missing requests')
    for r in good:
        u=r['usage']
        if (u['prompt_tokens'],u['completion_tokens'])!=(s['input_tokens'],s['output_tokens']):errors.append(f'{path}: token count mismatch')
        if not 0<=r['ttft_s']<=r['total_s']<=s['duration_s']:errors.append(f'{path}: inconsistent times')
        if r.get('first_token_at_s') is not None:
            if not 0<=r['started_at_s']<=r['first_token_at_s']<=r['finished_at_s']<=s['duration_s']:errors.append(f'{path}: inconsistent timeline')
            if abs(r['first_token_at_s']-r['started_at_s']-r['ttft_s'])>.01:errors.append(f'{path}: TTFT mismatch')
    for key in ['preemptions','peak_running','peak_waiting']:
        if s.get(key) is not None and s[key]<0:errors.append(f'{path}: negative {key}')
for path in [ROOT/'README.md',ROOT/'GUIA-DE-LECTURA.md',*(ROOT/'modelos').rglob('*.md'),*(ROOT/'scripts').glob('*.md')]:
    if not path.exists():continue
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if '://' in target or target.startswith('#'):continue
        if not (path.parent/target.split('#')[0]).exists():errors.append(f'{path}: broken link {target}')
# Once the campaign is declared complete, every planned block must be resolved.
# A failed startup resolves its block; unexecuted cases after a test failure do not.
import build_report
for model_dir in (ROOT/'modelos').iterdir():
    if not model_dir.is_dir():continue
    plans=list((model_dir/'configuracion-del-equipo').rglob('plan-y-estado-general.json'))
    if not plans:continue
    plan=json.loads(plans[0].read_text())
    if plan.get('status')!='complete':continue
    verification=plan.get('final_verification',{})
    if not (verification.get('verified') is True
            and verification.get('health_http_status')==200
            and verification.get('container_status')=='running'
            and verification.get('runner_restore_status')=='healthy'
            and verification.get('requests')=={'num_requests_running':0,'num_requests_waiting':0}):
        errors.append(f'{model_dir.name}: campaign marked complete without verified restoration')
    equipment=json.loads((model_dir/'configuracion-del-equipo/equipo.json').read_text())
    tests=[build_report.load_test(p,equipment) for p in model_dir.glob('memoria-*/**/configuracion.json')]
    for group in plan.get('planned_groups',[]):
        def matches(t):
            c=t['c'];kind=group['kind']
            return (t['memory']==group['memory_percent'] and t['limit']==group['server_limit']
                    and not c.get('medicion_inicial')
                    and bool(c.get('repeticion_de_control'))==(kind=='control')
                    and bool(c.get('espera_ampliada'))==(kind=='extended'))
        subset=[t for t in tests if t['type']=='conversaciones' and matches(t)
                and bool(t['c'].get('historial_reutilizado'))==(group['kind']=='reuse')]
        starts=[t for t in tests if t['type']=='arranque' and matches(t)]
        if not subset and starts and all(not t['raw']['ready'] for t in starts):continue
        terminal=lambda t:t['finished'] or t.get('summary',{}).get('status')=='not_admitted_within_90s' or t.get('summary',{}).get('status','').startswith('timeout_')
        if len(subset)!=group['tests'] or not all(terminal(t) for t in subset):
            errors.append(f'{model_dir.name}: campaign marked complete with unresolved block {group}')

if errors:raise SystemExit('\n'.join(errors))
print(f'Validated {checked} measured tests, original-file hashes and report links.')
