#!/usr/bin/env python3
"""Publish chat trajectories and their measured local capacity boundary."""
import argparse
import gzip
import hashlib
import json
import pathlib
import re
import subprocess

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'modelos/nvidia-qwen3.8-27b-nvfp4/capacidad-de-conversacion'

def read(p):return json.loads(p.read_text())
def number(value,places=1):
    return '—' if value is None else f'{value:,.{places}f}'.replace(',','@').replace('.',',').replace('@','.')
def rate(r):
    if not r.get('ok') or r.get('ttft_s') is None or r['total_s']<=r['ttft_s']:return None
    return (r['usage']['completion_tokens']-1)/(r['total_s']-r['ttft_s'])


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--cache',required=True)
    p.add_argument('--host')
    p.add_argument('--remote-root')
    p.add_argument('--sync',action='store_true')
    p.add_argument('--publish',action='store_true')
    a=p.parse_args();cache=pathlib.Path(a.cache);cache.mkdir(parents=True,exist_ok=True)
    if a.sync:
        if not a.host or not a.remote_root:p.error('--sync requires --host and --remote-root')
        subprocess.run(['rsync','-az','--exclude=*.tmp','--exclude=*.lock','--exclude=__pycache__',a.host+':'+a.remote_root+'/',str(cache)+'/'],check=True)
    meta=read(cache/'metadata.json') if (cache/'metadata.json').exists() else {'state':'preparing','boundaries':[],'cases':[]}
    plan=read(OUT/'plan.json');inventory=[]
    records=OUT/'reproduccion';records.mkdir(parents=True,exist_ok=True)
    def copy(source,dest):
        original=source.read_bytes();raw=gzip.decompress(original) if source.suffix=='.gz' else original
        text=raw.decode()
        text=re.sub(r'/home/[^/\s\"\']+','/home/usuario',text)
        text=re.sub(r'\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b','PRIVATE_IP',text)
        text=re.sub(r'\b[\w-]+\.local\b','HOST.local',text)
        public=original if text.encode()==raw else gzip.compress(text.encode(),mtime=0) if source.suffix=='.gz' else text.encode()
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(public)
        inventory.append(dict(file=str(dest.relative_to(OUT)),sha256=hashlib.sha256(public).hexdigest(),original_sha256=hashlib.sha256(original).hexdigest(),sanitized=public!=original))
    for src in cache.glob('*.py'):copy(src,records/'scripts'/src.name)
    for src in (cache/'versions').glob('*.py'):copy(src,records/'scripts/versions'/src.name)
    for src in cache.glob('arranque-*.log'):copy(src,records/src.name)
    for name in ['metadata.json','plan.json','verificacion-final.json']:
        if (cache/name).exists():copy(cache/name,records/name)
    for src in (cache/'piloto').glob('*'):
        if src.is_file():copy(src,records/'comprobacion-del-medidor'/src.name)
    rows=[]
    reasons={'three_consecutive_rounds_outside_reference':'Tres rondas seguidas con tiempos fuera de referencia',
        'answer_cut_or_not_visible':'Respuesta cortada o sin texto visible',
        'api_or_network_error':'Error de API o plazo de espera del cliente',
        'missing_measurements':'No se obtuvieron mediciones; revisar el registro'}
    for case in meta.get('cases',[]):
        folder=cache/'pruebas'/case['id'];out=OUT/case['id']
        if not (folder/'mediciones.json').exists():
            if case['state']=='running':continue
            c=read(folder/'configuracion.json')
            for src in folder.iterdir():
                if src.is_file() and not src.name.endswith('.tmp'):copy(src,out/src.name)
            reason='El servidor no pudo arrancar con esta configuración.' if case['state']=='startup_failed' else 'El intento terminó sin un archivo de mediciones. No se atribuye a falta de memoria sin evidencia del registro.'
            (out/'README.md').write_text(f"# Intento sin mediciones\n\n[Volver a la comparación](../README.md)\n\n{reason}\n\nPresupuesto: {round(c['memory_fraction']*100)}%. Personas: {c['users']}. Límite activo: {c['server_limit']}.\n\n[Configuración solicitada](configuracion.json) · [Registros del controlador](../reproduccion/metadata.json)\n")
            rows.append((case,c,{'growth_stop_reason':'missing_measurements','duration_s':case.get('duration_seconds')},out.name))
            continue
        d=read(folder/'mediciones.json');s=d['summary'];c=read(folder/'configuracion.json')
        if 'final_total_tokens_by_user' not in s:
            s=dict(s,final_total_tokens_by_user={str(user):max((r['usage']['total_tokens'] for r in d['requests'] if r['user_id']==user and r['ok']),default=0) for user in range(c['users'])})
        if case['state']=='running':
            rows.append((case,c,s,None));continue
        for src in folder.iterdir():
            if src.is_file() and not src.name.endswith('.tmp'):copy(src,out/src.name)
        rows.append((case,c,s,out.name))
        trajectory=c.get('grows_from_short_to_full',False)
        passed=case.get('acceptable_reference',False)
        reason=reasons.get(s.get('growth_stop_reason'),s.get('growth_stop_reason'))
        label='Cumplió durante todo el recorrido' if passed and trajectory else 'Cumplió el control' if passed else reason or ('No cumple la referencia del recorrido' if trajectory else 'No cumple la referencia de tiempos del control')
        lines=[f"# {c['users']} {'persona' if c['users']==1 else 'personas'} · {round(c['memory_fraction']*100)}% de memoria",'',
            '[Volver a la capacidad por memoria](../README.md)','',f'**{label}.**','',
            f"Modelo: `{s['model']}`. Razonamiento: **{'desactivado' if c['reasoning']=='disabled' else 'predeterminado'}**. Límite impuesto al servidor: **{c['server_limit']} solicitudes activas**. Presupuesto de salida: **hasta {number(c['output_tokens'],0)} tokens por respuesta**, con petición de hasta 100 palabras.",'',
            f"Respuestas recibidas sin error: **{s['completed']}/{s['num_requests']} previstas**. Duración: **{number(s['duration_s']/60)} min**, incluidas las pausas. {'Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.' if trajectory else 'Este control no recorre todo el contexto.'}",'',
            f"Peticiones con error: **{s['failed']}**. Peticiones previstas que no llegaron a enviarse: **{s['not_attempted']}**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.",'',
            'Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.','',
            '## Resultado durante el crecimiento','',
            '| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |',
            '|---|---:|---:|---:|---:|---:|---:|---|']
        for w in s.get('windows',[]):
            window_label='Cumple' if w['acceptable_reference'] else 'No cumple' if w['measured']==w['expected'] else 'Incompleto'
            lines.append(f"| {w['first_turn']}-{w['last_turn']} | {number(w['min_input_tokens'],0)}–{number(w['max_input_tokens'],0)} | {w['measured']}/{w['expected']} | {number(w['visible_ttft_p95_s'])} s | {number(w['visible_ttft_max_s'])} s | {number(w['decode_p05_tokens_s'],2)} tokens/s | {number(w['total_p95_s'])} s | {window_label} |")
        if not trajectory:
            lines=lines[:lines.index('## Resultado durante el crecimiento')]
            lines+=['## Resultado por turno','','| Turno | Sin error | Visibles y naturales | Espera visible p95 | Respuesta completa p95 | Velocidad p05 |','|---:|---:|---:|---:|---:|---:|']
            for t in s.get('per_turn',[]):
                natural=sum(r['ok'] and r['has_visible_answer'] and r['naturally_finished'] for r in d['requests'] if r['turn']==t['turn'])
                lines.append(f"| {t['turn']} | {t['completed']}/{t['expected']} | {natural}/{t['expected']} | {number(t['visible_ttft_p95_s'])} s | {number(t['total_p95_s'])} s | {number(t['decode_p05_tokens_s'],2)} tokens/s |")
        lines+=['','## Contexto alcanzado por persona','','| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |','|---:|---:|---:|---:|---:|']
        for user in range(c['users']):
            good=[r for r in d['requests'] if r['user_id']==user and r['ok']]
            total=max((r['usage']['total_tokens'] for r in good),default=0)
            lines.append(f"| {user+1} | {max((r['turn'] for r in good),default=0)} | {number(total,0)} | {number(total/262144*100,3)}% | {number(262144-total,0)} |")
        if trajectory:
            lines+=['','El cierre previsto reserva hasta 128 tokens y pide terminar en diez palabras. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. '+('Este intento llegó al cierre.' if s.get('reached_final_target') else 'Este intento no llegó a ese cierre.')]
        visible_waits=[r['visible_ttft_s'] for r in d['requests'] if r.get('ok') and r.get('visible_ttft_s') is not None]
        lines+=['',
            '## Memoria, colas y rendimiento del grupo','','| Medida | Resultado |','|---|---:|',
            f"| Presupuesto configurado | {number(c['memory_fraction']*100,0)}% |",
            f"| Pico de memoria del motor / GB10 | {number(s.get('peak_gpu_engine_percent'))}% |",
            f"| Pico de memoria total del sistema / GB10 | {number(s.get('peak_system_used_percent'))}% |",
            f"| Pico de caché | {number(100*s['peak_kv_fraction'] if s.get('peak_kv_fraction') is not None else None)}% |",
            f"| Solicitudes activas / respuestas solapadas, máximo | {number(s.get('peak_running'),0)} / {number(s.get('peak_overlapping_responses'),0)} |",
            f"| Cola máxima / segundos con cola | {number(s.get('peak_waiting'),0)} / {number(s.get('seconds_with_queue'))} s |",
            f"| Espera media al primer texto visible | {number(sum(visible_waits)/len(visible_waits) if visible_waits else None)} s |",
            f"| Espera media al primer token, incluido razonamiento | {number(s.get('mean_ttft_s'))} s |",
            f"| Tiempo medio de petición completa | {number(s.get('mean_total_s'))} s |",
            f"| Recálculos por falta de espacio de caché | {number(s.get('preemptions'),0)} |",
            f"| Velocidad global, incluidas pausas | {number(sum((r.get('usage') or {}).get('completion_tokens',0) for r in d['requests'])/s['duration_s'],2)} tokens/s |",
            f"| Suma de tiempos individuales de petición | {number(sum(r['total_s'] for r in d['requests']))} s |",'',
            '## Resumen por persona','','| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |',
            '|---:|---:|---:|---:|---:|---:|']
        for user in range(c['users']):
            own=[r for r in d['requests'] if r['user_id']==user]
            good=[r for r in own if r['ok']]
            waits=[r['visible_ttft_s'] for r in good if r.get('visible_ttft_s') is not None]
            session=max((r['finished_at_s'] for r in own),default=0)-min((r['started_at_s'] for r in own),default=0)
            lines.append(f"| {user+1} | {len(good)}/{len(own)} | {number(sum(waits)/len(waits) if waits else None)} s | {number(sum(r['total_s'] for r in good)/len(good) if good else None)} s | {number(session)} s | {number(sum(r['usage']['completion_tokens'] for r in good)/session if session>0 else None,2)} |")
        lines+=['','<details>','<summary>Cada persona y cada respuesta</summary>','',
            '| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |','|---:|---:|---:|---:|---:|---:|---:|---|']
        for r in sorted(d['requests'],key=lambda r:(r['turn'],r['user_id'])):
            usage=r.get('usage') or {}
            ending='Natural' if r['ok'] and r['finish_reason']=='stop' and r['has_visible_answer'] else 'Cortada' if r.get('finish_reason')=='length' else 'Sin respuesta visible / error'
            lines.append(f"| {r['user_id']+1} | {r['turn']} | {number(r['input_tokens'],0)} | {number(usage.get('completion_tokens'),0)} | {number(r.get('visible_ttft_s'))} s | {number(r['total_s'])} s | {number(rate(r),2)} | {ending} |")
        links='[Mediciones](mediciones.json) · [Configuración](configuracion.json)'
        if (out/'historiales.json.gz').exists():links+=' · [Historial reproducible](historiales.json.gz)'
        lines+=['','</details>','',links,'','La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.']
        (out/'README.md').write_text('\n'.join(lines)+'\n')
    lines=['# Cuántas personas pueden conversar hasta llenar el contexto','',
        '[Volver al modelo](../README.md)','',
        '**La pregunta medida es cuántas personas mantienen una conversación útil desde el principio hasta el límite de contexto, para cada presupuesto de memoria.** Cada persona conserva todos sus mensajes y las respuestas reales.','',
        '## Qué se considera útil','',
        'Las respuestas deben tener texto visible y terminar naturalmente. En cada bloque de hasta 16 rondas se exige primer texto en 5 s o menos para el 95% de las peticiones, ninguna espera superior a 10 s, al menos 5 tokens/s para el 95% y respuesta completa en 120 s o menos para el 95%. También se comprueba el conjunto del recorrido. Son criterios explícitos de comparación, no una definición universal de comodidad.','',
        '**La tabla principal usa razonamiento desactivado**, respuestas solicitadas de hasta 100 palabras y un límite de 1.024 tokens de salida. No se debe aplicar ese número de personas al modo de razonamiento predeterminado: sus controles se muestran aparte.','',
        '## Capacidad comprobada por memoria','',
        '| Presupuesto del modelo | Personas con recorrido completo y útil | Siguiente grupo ensayado | Estado de la comprobación |','|---:|---:|---:|---|']
    for fraction in plan['memory_fractions']:
        cells=[b for b in meta.get('boundaries',[]) if b['memory_fraction']==fraction]
        b=cells[-1] if cells else None
        if b and b['state']=='complete':
            good=b['largest_confirmed_acceptable'];bad=b.get('first_not_confirmed_acceptable')
            label=('Al menos '+str(good)) if b.get('reached_search_ceiling') else str(good) if good else 'Ninguno de los ensayados'
            status='Frontera local medida' if good and bad is not None else 'Techo de búsqueda alcanzado' if good else 'Revisar la causa; no implica que el modelo no funcione'
            if b.get('nonmonotonic'):status+='; resultados no monótonos'
            lines.append(f"| {round(fraction*100)}% | {label} | {bad if bad is not None else '—'} | {status} |")
        elif b and b['state']=='startup_failed':lines.append(f"| {round(fraction*100)}% | No medible con este arranque | — | Arranque fallido; ver registros |")
        else:
            trajectories=[(case,c,s) for case,c,s,_ in rows if c['memory_fraction']==fraction and c.get('grows_from_short_to_full')]
            confirmed=max((c['users'] for case,c,s in trajectories if case['state']=='finished' and case.get('acceptable_reference') and s.get('acceptable_reference')),default=0)
            running=[c['users'] for case,c,s in trajectories if case['state']=='running']
            label=f'Al menos {confirmed}' if confirmed else 'Pendiente de completar el recorrido'
            next_group=f'{running[-1]} (en curso)' if running else '—'
            state='Buscando el máximo; mínimo ya comprobado' if confirmed else 'En curso' if b else 'Pendiente'
            lines.append(f"| {round(fraction*100)}% | {label} | {next_group} | {state} |")
    lines+=['','El presupuesto de memoria no es un límite estricto de toda la RAM del GB10. El límite activo del servidor es el mayor entre cuatro y las personas de la prueba; nunca es inferior al grupo enviado. La búsqueda llega hasta 32 personas: si se alcanza ese techo se informa como un mínimo demostrado, nunca como el máximo del equipo. La búsqueda acota los grupos ensayados; no demuestra todas las configuraciones posibles.','',
        '## Recorridos y controles individuales','',
        '| Prueba | Memoria | Personas | Rondas medidas | Mayor contexto alcanzado | Espera visible p95 al continuar | Velocidad p05 | Tiempo del grupo | Resultado |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---|']
    for case,c,s,folder in rows:
        kind='Recorrido desde el principio' if c.get('grows_from_short_to_full') else 'Control con razonamiento'
        link=f'[{kind}]({folder}/README.md)' if folder else kind
        contexts=s.get('final_total_tokens_by_user',{})
        tokens=max(contexts.values(),default=None)
        state='En curso; no es un resultado final' if case['state']=='running' else 'Cumple' if case.get('acceptable_reference') else reasons.get(s.get('growth_stop_reason'),'No cumple')
        if case['state']=='running':
            failed_windows=[w for w in s.get('windows',[]) if w['measured']==w['expected'] and not w['acceptable_reference']]
            if failed_windows:
                state=f"En curso; {len(failed_windows)} {'bloque completo fuera' if len(failed_windows)==1 else 'bloques completos fuera'} de referencia"
        lines.append(f"| {link} | {round(c['memory_fraction']*100)}% | {c['users']} | {s.get('actual_rounds',len([t for t in s.get('per_turn',[]) if t['completed']]))} | {number(tokens,0)} | {number(s.get('followups_visible_ttft_p95_s'))} s | {number(s.get('followups_decode_p05_tokens_s'),2)} tokens/s | {number(s['duration_s']/60 if s.get('duration_s') is not None else None)} min | {state} |")
    for case,c,s,_ in rows:
        if case['state']!='running':continue
        failed_windows=[w for w in s.get('windows',[]) if w['measured']==w['expected'] and not w['acceptable_reference']]
        if failed_windows:
            w=failed_windows[-1]
            lines+=['',f"En la prueba en curso al **{round(c['memory_fraction']*100)}% con {c['users']} {'persona' if c['users']==1 else 'personas'}**, el último bloque completo fuera de referencia es **{w['first_turn']}–{w['last_turn']}**: espera p95 de **{number(w['visible_ttft_p95_s'],2)} s**, peor espera de **{number(w['visible_ttft_max_s'],2)} s**, velocidad p05 de **{number(w['decode_p05_tokens_s'],2)} tokens/s** y respuesta completa p95 de **{number(w['total_p95_s'])} s**. Los valores del conjunto del recorrido pueden ocultar esta ralentización; se exige cumplir también en cada bloque."]
    lines+=['','## Cómo avanza cada conversación','']
    lines += [f'{i}. {step}' for i,step in enumerate(plan['method'],1)]
    lines+=['','## Alcance de la respuesta','']+[f'- {line}' for line in plan['limitations']]
    lines+=['','La prueba mide tiempos y finalización. No garantiza que todas las respuestas sean correctas ni que el modelo recuerde perfectamente todos los detalles del historial.','',
        '[Plan exacto](plan.json) · [Datos de ejecución y scripts reproducibles](reproduccion/README.md)','']
    if meta.get('state')=='stopped':
        lines.append(f"Restauración del servicio: **{meta.get('restore_status','sin verificar')}**. "+('[Comprobación independiente](reproduccion/verificacion-final.json).' if (records/'verificacion-final.json').exists() else 'La comprobación independiente aún no está publicada.'))
        if meta.get('error'):lines.append('La ejecución del controlador se interrumpió; las pruebas pendientes no se consideran realizadas.')
    (OUT/'README.md').write_text('\n'.join(lines)+'\n')
    (records/'README.md').write_text('# Reproducción y registros\n\n[Volver a los resultados](../README.md)\n\nEl [plan](../plan.json) describe la carga y los criterios antes de medir. Aquí se conservan el estado del controlador, el piloto y los scripts efectivamente ejecutados. Los registros sustituyen rutas personales, direcciones privadas y nombres locales. Las mediciones y los historiales ficticios se mantienen junto a cada prueba. El [inventario](inventario.json) permite comprobar su procedencia.\n')
    (records/'inventario.json').write_text(json.dumps(inventory,indent=2,ensure_ascii=False)+'\n')
    subprocess.run(['python3',str(ROOT/'scripts/validate_capacity.py')],check=True)
    subprocess.run(['python3',str(ROOT/'scripts/validate_new_public_files.py')],check=True)
    if a.publish:
        subprocess.run(['git','add',str(OUT),str(ROOT/'scripts/capacity_probe.py'),str(ROOT/'scripts/capacity_campaign.py'),str(ROOT/'scripts/capacity_report.py'),str(ROOT/'scripts/validate_capacity.py')],cwd=ROOT,check=True)
        if subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT).returncode:
            subprocess.run(['git','commit','-m','Mide conversaciones completas y capacidad por memoria'],cwd=ROOT,check=True)
            subprocess.run(['git','push','origin','HEAD'],cwd=ROOT,check=True)


if __name__=='__main__':main()
