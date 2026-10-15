#!/usr/bin/env python3
"""Publish completed recurrent cases, preserving sources beside their explanations."""
import argparse
import hashlib
import json
import math
import os
import pathlib
import re
import shutil
import subprocess

ROOT=pathlib.Path(__file__).resolve().parents[1]
MODEL=ROOT/'modelos/nvidia-qwen3.8-27b-nvfp4'
OUT=MODEL/'conversaciones-recurrentes'
def read(p):return json.loads(p.read_text())
def n(v,d=1):return '—' if v is None else f'{v:,.{d}f}'.replace(',','@').replace('.',',').replace('@','.')
def quantile(values,p):
    values=sorted(v for v in values if v is not None)
    return values[max(0,math.ceil(p*len(values))-1)] if values else None
def rate(r):
    return (r['usage']['completion_tokens']-1)/(r['total_s']-r['ttft_s']) if r.get('ok') and r.get('ttft_s') is not None and r['total_s']>r['ttft_s'] else None


def main():
    p=argparse.ArgumentParser();p.add_argument('--cache',default=str(pathlib.Path.home()/'.cache/TestsGB10/conversaciones-recurrentes-2026-10-15'))
    p.add_argument('--host',default=os.environ.get('GB10_HOST'));p.add_argument('--sync',action='store_true');p.add_argument('--publish',action='store_true');p.add_argument('--message',default='Añade una prueba de conversaciones recurrentes')
    a=p.parse_args();cache=pathlib.Path(a.cache);cache.mkdir(parents=True,exist_ok=True)
    if a.sync:
        if not a.host:p.error('Set --host or GB10_HOST to the SSH host configured locally')
        subprocess.run(['rsync','-az','--exclude=*.tmp',a.host+':/tmp/gb10-recurrent-20261015/',str(cache)+'/'],check=True)
    meta=read(cache/'metadata.json');plan=read(OUT/'plan.json');rows=[];inventory=[]
    def copy(src,dest):
        dest.parent.mkdir(parents=True,exist_ok=True)
        original=src.read_bytes();public=original
        if src.suffix!='.gz':
            value=original.decode()
            value=re.sub(r'/home/[^/\s\"\']+', '/home/usuario', value)
            value=re.sub(r'\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b','PRIVATE_IP',value)
            value=re.sub(r'\b[\w-]+\.local\b','HOST.local',value)
            public=value.encode()
        dest.write_bytes(public)
        inventory.append({'file':str(dest.relative_to(ROOT)),'sha256':hashlib.sha256(public).hexdigest(),'original_sha256':hashlib.sha256(original).hexdigest(),'sanitized':original!=public})
    equipment=OUT/'configuracion-y-registros'
    equipment.mkdir(parents=True,exist_ok=True)
    (equipment/'README.md').write_text('# Registros y reproducción\n\nLas mediciones proceden de entradas sintéticas. Los registros publicados sustituyen rutas personales, direcciones privadas y nombres locales de equipo. Los originales completos se conservan fuera del repositorio. El inventario indica la huella del original, la del archivo publicado y si se ha aplicado esa sustitución. Las mediciones numéricas y los errores se conservan.\n')
    for file in ['metadata.json','queue.json','restore-override.json','restored-server.log']:
        if (cache/file).exists():copy(cache/file,equipment/file)
    for src in (cache/'scripts').rglob('*.py'):copy(src,equipment/'scripts'/src.relative_to(cache/'scripts'))
    for src in (cache/'pilot').glob('*'):
        if src.is_file():copy(src,equipment/'comprobacion-del-medidor'/src.name)
    for profile in meta['profiles']:
        src_profile=cache/'profiles'/profile['id']
        if (src_profile/'startup.log').exists():copy(src_profile/'startup.log',equipment/profile['id']/'arranque.log')
        for case_record in profile['cases']:
            source=src_profile/case_record['id'];c=read(source/'configuration.json')
            folder=OUT/(f"memoria-{round(profile['fraction']*100)}-"+case_record['id'])
            names={'configuration.json':'configuracion.json','measurements.json':'mediciones.json','execution.log':'registro-de-ejecucion.log','server.log':'registro-del-servidor.log','executed-command.json':'comando-ejecutado.json','histories.json.gz':'historiales-reproducibles.json.gz'}
            for old,new in names.items():
                if (source/old).exists():copy(source/old,folder/new)
            data=read(source/'measurements.json') if (source/'measurements.json').exists() else {'summary':{},'requests':[]}
            s=data['summary'];requests=sorted(data['requests'],key=lambda r:(r['user_id'],r['turn']));good=[r for r in requests if r['ok']];follow=[r for r in good if r['turn']>1]
            initial=[r for r in good if r['turn']==1];count=c['users']*c.get('turns',3)
            all_done=len(good)==count and case_record['exit_code']==0
            fluent=all_done and bool(s.get('followups_reference_fluent'))
            label='Cumple la referencia' if fluent else 'No cumple la referencia' if all_done else 'No completó todo'
            row={'folder':folder.name,'config':c,'summary':s,'record':case_record,'all_done':all_done,'fluent':fluent,'label':label,'count':count,'done':len(good),'cold95':quantile([r.get('ttft_s') for r in initial],.95),'follow95':quantile([r.get('ttft_s') for r in follow],.95),'decode05':quantile([rate(r) for r in follow],.05)};rows.append(row)
            lines=[f"# {c['users']} usuarios · {round(profile['fraction']*100)}% · historial inicial de {n(c['input_tokens'],0)} tokens",'', '[Volver a la comparación](../README.md)','',
                   f"**Continuaciones: {label.lower()}.** Respuestas completas: **{len(good)}/{count}**. Tiempo de la prueba: **{n(s.get('duration_s'))} s**.",'',
                   f"Límite impuesto al servidor: **{c['server_limit']} activas**. Cada usuario mantiene una sola petición pendiente y espera **{c.get('think_seconds',30)} s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.",'',
                   'Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.','',
                   '## Resultado por turno','',
                   '| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |','|---|---:|---:|---:|---:|---:|---:|---|']
            for t in s.get('per_turn',[]):
                lines.append(f"| {t['turn']} | {t['completed']}/{t['expected']} | {n(t['ttft_p50_s'])} s | {n(t['ttft_p95_s'])} s | {n(t['ttft_max_s'])} s | {n(t['total_p95_s'])} s | {n(t['decode_p05_tokens_s'],2)} tokens/s | {'Cumple' if t['reference_fluent'] else 'No cumple'} |")
            lines+=['','La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.','',
                    '## Memoria y comportamiento del grupo','', '| Medida | Resultado |','|---|---|',
                    f"| Presupuesto configurado | {round(profile['fraction']*100)}% |",
                    f"| Pico del motor / GB10 | {n(s.get('peak_gpu_engine_percent'))}% |",
                    f"| Pico del sistema / GB10 | {n(s.get('peak_system_used_percent'))}% |",
                    f"| Menor memoria disponible | {n(s.get('min_available_gib'),2)} GiB |",
                    f"| Pico de caché | {n(100*s['peak_kv_fraction'] if s.get('peak_kv_fraction') is not None else None)}% |",
                    f"| Máximo activo / respuestas solapadas | {n(s.get('peak_running'),0)} / {n(s.get('peak_overlapping_responses'),0)} |",
                    f"| Máximo en cola | {n(s.get('peak_waiting'),0)} |",
                    f"| Recálculos | {n(s.get('preemptions'),0)} |",
                    f"| Tokens recuperados de caché | {n(s.get('prefix_cache_hits'),0)} |",
                    f"| Tokens/s de todo el grupo, incluyendo pausas | {n(sum(r['usage']['completion_tokens'] for r in good)/s['duration_s'] if s.get('duration_s') else None,2)} |",
                    f"| Suma de tiempos individuales | {n(sum(r['total_s'] for r in good))} s |",
                    f"| Tiempo total de la prueba, incluyendo pausas | {n(s.get('duration_s'))} s |",'',
                    '## Cada persona y cada mensaje','',
                    '| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |',
                    '|---|---:|---:|---:|---:|---:|---|']
            for r in requests:
                u=r.get('usage') or {};result='Completa' if r['ok'] else 'Error: '+str(r.get('error','longitud inesperada')).replace('|','/')
                lines.append(f"| {r['user_id']+1} | {r['turn']} | {n(r['input_tokens'],0)} + {n(u.get('completion_tokens'),0)} | {n(r.get('ttft_s'))} s | {n(r.get('total_s'))} s | {n(rate(r),2)} | {result} |")
            if len(requests)<count:lines+=['',f"No se ejecutaron {count-len(requests)} turnos previstos. Se conserva el registro del fallo; no se cuentan como respuestas recibidas."]
            maximum=sum(r['usage']['total_tokens']==262144 for r in good)
            if maximum:lines+=['',f'**Llegaron exactamente al máximo de 262.144 tokens y completaron la respuesta: {maximum} conversaciones.**']
            lines+=['','## Datos y reproducción','', '[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)','']
            if (folder/'historiales-reproducibles.json.gz').exists():lines+=['[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.','']
            (folder/'README.md').write_text('\n'.join(lines))
    (equipment/'inventario-originales.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
    existing=(OUT/'README.md').read_text();existing=existing.split('<!-- resultados-inicio -->')[0].rstrip()
    notice='**Se están realizando nuevas pruebas de conversaciones recurrentes con 10, 20 y 30 usuarios.**'
    if plan['status']!='running':existing=existing.replace(notice+'\n','')
    lines=[existing,'','<!-- resultados-inicio -->','## Resultados publicados','',
           'Se publica una prueba cuando termina. Los percentiles del primer turno y de las continuaciones se muestran separados. Las medidas parciales no se publican como resultados definitivos.','',
           '| Prueba | Memoria | Usuarios / límite | Historial inicial | Respuestas | Espera p95 primer turno | Espera p95 continuaciones | Velocidad p05 continuaciones | Caché máxima | Recálculos | Tiempo total | Continuaciones |',
           '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|']
    for r in rows:
        c=r['config'];s=r['summary']
        lines.append(f"| [{c['id']}]({r['folder']}/README.md) | {round(c['memory_fraction']*100)}% | {c['users']} / {c['server_limit']} | {n(c['input_tokens'],0)} | {r['done']}/{r['count']} | {n(r['cold95'])} s | {n(r['follow95'])} s | {n(r['decode05'],2)} tokens/s | {n(100*s['peak_kv_fraction'] if s.get('peak_kv_fraction') is not None else None)}% | {n(s.get('preemptions'),0)} | {n(s.get('duration_s'))} s | {r['label']} |")
    lines+=['','[Configuración y registros de esta campaña](configuracion-y-registros/metadata.json).','']
    (OUT/'README.md').write_text('\n'.join(lines))
    (OUT/'resumen.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    subprocess.run([sys.executable,str(ROOT/'scripts/build_report.py')],check=True,cwd=ROOT)
    subprocess.run([sys.executable,str(ROOT/'scripts/validate_report.py')],check=True,cwd=ROOT)
    subprocess.run([sys.executable,str(ROOT/'scripts/validate_recurrent.py')],check=True,cwd=ROOT)
    subprocess.run(['git','diff','--check'],check=True,cwd=ROOT)
    if a.publish:
        subprocess.run([sys.executable,str(ROOT/'scripts/validate_new_public_files.py')],check=True,cwd=ROOT)
        subprocess.run(['git','add','-A'],check=True,cwd=ROOT)
        if subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT).returncode:
            subprocess.run(['git','commit','-m',a.message],check=True,cwd=ROOT)
        subprocess.run(['git','push'],check=True,cwd=ROOT)


if __name__=='__main__':
    import sys
    main()
