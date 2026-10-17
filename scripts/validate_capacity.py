#!/usr/bin/env python3
"""Check recorded prompts, real response continuity, times, hashes and capacity claims."""
import gzip
import hashlib
import json
import math
import pathlib

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'modelos/nvidia-qwen3.8-27b-nvfp4/capacidad-de-conversacion'
def read(p):return json.loads(p.read_text())
def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def quantile(values,p):
    values=sorted(v for v in values if v is not None)
    return values[max(0,math.ceil(p*len(values))-1)] if values else None


def main():
    inventory=read(OUT/'reproduccion/inventario.json')
    for item in inventory:
        assert hashlib.sha256((OUT/item['file']).read_bytes()).hexdigest()==item['sha256'],item['file']
    meta_path=OUT/'reproduccion/metadata.json'
    if not meta_path.exists():
        print('Plan and available source files verified; no recorded trials yet.');return
    meta=read(meta_path);cases={c['id']:c for c in meta.get('cases',[])}
    verified=0
    script_hashes={hashlib.sha256(p.read_bytes()).hexdigest() for p in (OUT/'reproduccion/scripts').rglob('*.py')}
    for path in OUT.glob('memoria-*/mediciones.json'):
        data=read(path);s=data['summary'];c=read(path.with_name('configuracion.json'))
        record=cases[c['id']]
        assert record['state']!='running','Partial data must not be published as a completed trial'
        if s.get('status') in ('running','measurement_error'):
            assert not record.get('acceptable_reference'),'An interrupted measuring process cannot establish capacity'
            assert 'Medidor interrumpido' in path.with_name('README.md').read_text()
            table=(OUT/'README.md').read_text()
            capacity_row=next(line for line in table.splitlines() if line.startswith(f"| {round(c['memory_fraction']*100)}% |"))
            assert 'frontera sin cerrar' in capacity_row,'A measuring error must leave the boundary explicitly pending'
        assert s['script_sha256'] in script_hashes,'Executed source script missing'
        assert s['concurrency']==c['users'] and s['memory_fraction']==c['memory_fraction']
        assert s['server_max_num_seqs']==c['server_limit'] and c['server_limit']>=c['users']
        rs=data['requests'];good=[r for r in rs if r['ok']]
        assert len(good)==s['completed']
        assert len({(r['user_id'],r['turn']) for r in rs})==len(rs)
        for r in good:
            assert r['usage']['prompt_tokens']==r['input_tokens']
            assert r['usage']['total_tokens']==r['input_tokens']+r['usage']['completion_tokens']<=262144
            assert 0<r['usage']['completion_tokens']<=r['effective_output_budget']
            assert r['started_at_s']<=r['first_token_at_s']<=r['finished_at_s']
            assert abs(r['finished_at_s']-r['started_at_s']-r['total_s'])<.00001
        follow=[r for r in good if r['turn']>1]
        expected=quantile([r.get('visible_ttft_s') for r in follow],.95)
        assert expected==s['followups_visible_ttft_p95_s']
        history_path=path.with_name('historiales.json.gz')
        if history_path.exists():
            histories=json.loads(gzip.decompress(history_path.read_bytes()))['histories']
            for user,h in histories.items():
                own=sorted([r for r in rs if str(r['user_id'])==user],key=lambda r:r['turn'])
                messages=list(h['initial_messages'])
                assert len(h['exchanges'])==len(own)
                for i,(r,exchange) in enumerate(zip(own,h['exchanges'])):
                    if i:
                        messages.append(exchange['user_message'])
                        assert r['input_tokens']>own[i-1]['input_tokens']
                        assert r['started_at_s']>=own[i-1]['finished_at_s']+s['think_seconds']-.01
                    else:assert messages[-1]==exchange['user_message']
                    assert digest(messages)==r['prompt_sha256'],'A previous message/reply was changed or omitted'
                    assert exchange['assistant_message']==r['assistant_message']
                    if r['ok']:messages.append(r['assistant_message'])
                assert messages==h['final_messages']
        elif record.get('exit_code')==0:
            raise AssertionError('Successful trial has no reproducible history')
        if s.get('kind')=='growing_chat':
            targets=s['growth_targets']
            for r in rs:
                assert targets[r['turn']-1]-32<=r['input_tokens']<=targets[r['turn']-1]
            for w in s['windows']:
                block=[r for r in rs if w['first_turn']<=r['turn']<=w['last_turn']]
                done=[r for r in block if r['ok']]
                waits=[r['visible_ttft_s'] for r in done if r['has_visible_answer']]
                speeds=[(r['usage']['completion_tokens']-1)/(r['total_s']-r['ttft_s']) for r in done if r.get('ttft_s') is not None and r['total_s']>r['ttft_s']]
                assert len(block)==w['measured']
                assert quantile(waits,.95)==w['visible_ttft_p95_s']
                assert quantile(speeds,.05)==w['decode_p05_tokens_s']
                assert quantile([r['total_s'] for r in done],.95)==w['total_p95_s']
                expected_ok=bool(len(done)==w['expected'] and all(r['has_visible_answer'] and r['naturally_finished'] for r in done)
                    and waits and quantile(waits,.95)<=5 and max(waits)<=10
                    and speeds and quantile(speeds,.05)>=5 and w['total_p95_s']<=120)
                assert expected_ok==w['acceptable_reference']
            if record.get('acceptable_reference'):
                assert s['reached_final_target'] and not s['growth_stop_reason']
                assert len(good)==c['users']*len(targets)
                assert all(w['acceptable_reference'] for w in s['windows'])
                assert all(r['has_visible_answer'] and r['naturally_finished'] for r in good)
                assert min(s['final_total_tokens_by_user'].values())>=262144-160
                assert s['acceptable_reference']
        verified+=1
    for b in meta.get('boundaries',[]):
        if b['state']!='complete':continue
        good=b['largest_confirmed_acceptable'];bad=b.get('first_not_confirmed_acceptable')
        observations=b['observations']
        if good:assert all(observations[str(good)])
        if bad is not None:
            assert not all(observations[str(bad)])
            if good:assert bad==good+1
        for name in b['attempts']:
            assert name in cases and cases[name]['state']!='running'
    if meta.get('state')=='stopped' and meta.get('measurements_complete'):
        plan=read(OUT/'plan.json')
        assert {b['memory_fraction'] for b in meta['boundaries']}==set(plan['memory_fractions'])
        assert all(b['state'] in ('complete','startup_failed') for b in meta['boundaries'])
        assert meta['restore_status']=='healthy'
        proof=read(OUT/'reproduccion/verificacion-final.json')
        assert proof['verified'] and proof['command']==meta['original_command']
        assert not any(proof['requests'].values())
    print(f'Validated {verified} finished trials, real message continuity, token growth, timestamps, source hashes and published capacity claims.')


if __name__=='__main__':main()
