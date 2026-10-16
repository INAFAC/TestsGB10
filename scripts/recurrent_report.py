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

def case_title(c):
    if c['id'].startswith('chat-comprobacion-medidor-'):
        return 'Medidor: '+('sin razonamiento' if c['id'].endswith('-sin-razonamiento') else 'modo predeterminado')
    if c['id'].startswith('chat-'):
        return 'Chat: '+('sin razonamiento' if c['id'].endswith('-sin-razonamiento') else 'modo predeterminado')+f" · hasta {n(c.get('output_tokens',512),0)} tokens de salida"
    if c['input_tokens']==260864:return 'Continuar hasta el máximo de contexto'
    if c.get('parent_state'):return 'Continuar con un historial ampliado'+(' · repetición tras interrupción' if c['id'].endswith('-repeticion-por-interrupcion') else '')
    return f"Conversación de {c.get('turns',3)} turnos por persona"

def comparison_overview(rows,plan):
    selected=plan.get('decisions',{}).get('selected_memory_percent')
    chosen=[r for r in rows if r['measurement_available'] and round(100*r['config']['memory_fraction'])==selected]
    synthetic=[r for r in chosen if not r['config']['id'].startswith('chat-')
               and r['config']['users'] in (10,20,30) and r['config']['input_tokens'] in (8192,32768)
               and r['config'].get('turns',3)==3]
    lines=[]
    if synthetic:
        lines=['## Cómo cambia la conversación con más personas','',
               f'Comparación directa de las pruebas terminadas al **{selected}% de memoria**. Cada persona envía tres mensajes, pide 512 tokens de respuesta por turno y espera 30 segundos antes de continuar. El {selected}% es el presupuesto de referencia elegido para estas pruebas, no un mínimo demostrado para cada número de personas.','',
               '| Historial inicial | Personas | Respuestas sin error | Espera p95 inicial | Espera p95 al continuar | Respuesta completa p95 al continuar | Velocidad p05 al continuar |',
               '|---:|---:|---:|---:|---:|---:|---:|']
        for r in sorted(synthetic,key=lambda r:(r['config']['input_tokens'],r['config']['users'])):
            c=r['config'];s=r['summary']
            lines.append(f"| {n(c['input_tokens'],0)} | [{c['users']}]({r['folder']}/README.md) | {r['done']}/{r['count']} | {n(r['cold95'])} s | {n(r['follow95'])} s | {n(s.get('followups_total_p95_s'))} s | {n(r['decode05'],2)} tokens/s |")
        lines+=['','Una prueba puede cumplir la referencia de espera y quedar por debajo de la referencia de velocidad. Las cifras de ambas columnas permiten valorar ese equilibrio; la etiqueta general de referencia no sustituye esos tiempos.','']
    growth=[r for r in chosen if not r['config']['id'].startswith('chat-') and r['config'].get('parent_state')]
    if growth:
        lines+=['## Qué ocurre al ampliar el historial','',
                f'Pruebas al **{selected}%**, conservando el historial y las respuestas de la etapa anterior. Cada persona realiza dos turnos nuevos. El primer turno incluye el coste de ampliar el historial; el segundo mide volver a continuar.','',
                '| Historial del primer turno | Personas | Completaron ambos turnos | Llegaron a 262.144 tokens | Espera p95 al ampliar | Espera p95 al continuar | Respuesta completa p95 al continuar | Tiempo del grupo |',
                '|---:|---:|---:|---|---:|---:|---:|---:|']
        for r in sorted(growth,key=lambda r:(r['config']['input_tokens'],r['config']['users'])):
            c=r['config'];s=r['summary'];maximum=f"{r['users_at_maximum_context']}/{c['users']}" if c['input_tokens']==260864 else 'No se intentó'
            workload=n(c['input_tokens'],0)+(' · interrumpida' if r['record'].get('interrupted') else ' · repetición' if c['id'].endswith('-repeticion-por-interrupcion') else '')
            lines.append(f"| [{workload}]({r['folder']}/README.md) | {c['users']} | {r['users_completed_all_turns']}/{c['users']} | {maximum} | {n(r['cold95'])} s | {n(r['follow95'])} s | {n(s.get('followups_total_p95_s'))} s | {n(s.get('duration_s'))} s |")
        lines+=['','Llegar al máximo exige una respuesta recibida cuya suma real de entrada y salida sea 262.144 tokens. El número de personas que completó ambos turnos se muestra aparte: alcanzar el máximo no demuestra rapidez ni calidad de conversación.','']
        decisions=plan.get('decisions',{}).get('growth_131072',{})
        for users,decision in sorted(decisions.items(),key=lambda item:int(item[0])):
            lines.append(f"**Etapa de 131.072 tokens, {users} personas:** {decision['reason']} [Medición anterior]({decision['evidence']}/README.md).")
            lines.append('')
    chat=[r for r in chosen if r['config']['id'].startswith('chat-') and not r['config']['id'].startswith('chat-comprobacion-medidor-')]
    if chat:
        lines+=['## Controles con conversaciones de chat','',
                f'Controles al **{selected}% de memoria**, con mensajes ficticios legibles, respuestas reales conservadas y permiso para terminar antes del límite de salida. Una respuesta visible terminada debe contener texto para la persona y acabar por decisión del modelo, sin alcanzar el límite de tokens.','',
                '| Historial inicial | Personas | Razonamiento | Límite de salida | Peticiones sin error | Con texto visible | Respuesta visible terminada | Cortadas por límite | Espera visible p95 al continuar |',
                '|---:|---:|---|---:|---:|---:|---:|---:|---:|']
        for r in chat:
            c=r['config'];s=r['summary'];mode='Desactivado' if s.get('reasoning_mode')=='disabled' else 'Predeterminado'
            lines.append(f"| [{n(c['input_tokens'],0)}]({r['folder']}/README.md) | {c['users']} | {mode} | {c.get('output_tokens',512)} | {r['done']}/{r['count']} | {s.get('visible_answers',0)}/{r['count']} | {r['chat_visible_natural_answers']}/{r['count']} | {r['chat_output_limit_reached']}/{r['count']} | {n(s.get('followups_visible_ttft_p95_s'))} s |")
        lines+=['','La espera visible empieza al enviar la petición y acaba cuando llega el primer texto de respuesta. Si el modelo solo produce razonamiento, no se cuenta como una respuesta visible. Los percentiles se calculan sobre las respuestas recibidas; el recuento permite ver si faltan otras.','']
    return lines


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
    for file in ['metadata.json','queue.json','restore-override.json','restored-server.log','verificacion-final.json']:
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
            names={'configuration.json':'configuracion.json','measurements.json':'mediciones.json','execution.log':'registro-de-ejecucion.log','server.log':'registro-del-servidor.log','executed-command.json':'comando-ejecutado.json','histories.json.gz':'historiales-reproducibles.json.gz','interruption.json':'interrupcion.json','controller-metadata-at-interruption.json':'controlador-al-interrumpirse.json','queue-at-interruption.json':'cola-al-interrumpirse.json'}
            for old,new in names.items():
                if (source/old).exists():copy(source/old,folder/new)
            measurement_available=(source/'measurements.json').exists()
            data=read(source/'measurements.json') if measurement_available else {'summary':{},'requests':[]}
            s=data['summary'];requests=sorted(data['requests'],key=lambda r:(r['user_id'],r['turn']));good=[r for r in requests if r['ok']];follow=[r for r in good if r['turn']>1]
            initial=[r for r in good if r['turn']==1];count=c['users']*c.get('turns',3)
            all_done=len(good)==count and case_record['exit_code']==0 and not case_record.get('interrupted')
            fluent=all_done and bool(s.get('followups_reference_fluent'))
            label='Interrumpida por el controlador' if case_record.get('interrupted') else 'Sin mediciones; revisar registro' if not measurement_available else 'Cumple la referencia' if fluent else 'No cumple la referencia' if all_done else 'No completó todo'
            row={'folder':folder.name,'measurement_available':measurement_available,'config':c,'summary':s,'record':case_record,'all_done':all_done,'fluent':fluent,'label':label,'count':count,'done':len(good),'cold95':quantile([r.get('ttft_s') for r in initial],.95),'follow95':quantile([r.get('ttft_s') for r in follow],.95),'decode05':quantile([rate(r) for r in follow],.05)};rows.append(row)
            row['users_completed_all_turns']=sum(sum(r['user_id']==user for r in good)==c.get('turns',3) for user in range(c['users']))
            row['users_at_maximum_context']=len({r['user_id'] for r in good if (r.get('usage') or {}).get('total_tokens')==s.get('max_model_len',262144)})
            row['chat_visible_natural_answers']=sum(bool(r.get('has_visible_answer') and r.get('naturally_finished')) for r in good) if s.get('kind')=='chat_recurrent' else None
            row['chat_output_limit_reached']=sum(r.get('finish_reason')=='length' for r in good) if s.get('kind')=='chat_recurrent' else None
            lines=[f"# {c['users']} usuarios · {round(profile['fraction']*100)}% · historial inicial de {n(c['input_tokens'],0)} tokens",'', '[Volver a la comparación](../README.md)','',
                   f"**Continuaciones: {label.lower()}.** Respuestas completas: **{len(good)}/{count}**. Tiempo de la prueba: **{n(s.get('duration_s'))} s**.",'',
                   f"Límite impuesto al servidor: **{c['server_limit']} activas**. Cada usuario mantiene una sola petición pendiente y espera **{c.get('think_seconds',30)} s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.",'',
                   'Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.','',
                   '## Resultado por turno','',
                   '| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |','|---|---:|---:|---:|---:|---:|---:|---|']
            for t in s.get('per_turn',[]):
                lines.append(f"| {t['turn']} | {t['completed']}/{t['expected']} | {n(t['ttft_p50_s'])} s | {n(t['ttft_p95_s'])} s | {n(t['ttft_max_s'])} s | {n(t['total_p95_s'])} s | {n(t['decode_p05_tokens_s'],2)} tokens/s | {'Cumple' if t['reference_fluent'] else 'No cumple'} |")
            if s.get('kind')=='chat_recurrent':
                lines[4]=f"**Continuaciones: {label.lower()}.** Peticiones sin error: **{len(good)}/{count}**. Respuestas con contenido visible: **{s.get('visible_answers',0)}/{count}**. Peticiones terminadas por el modelo: **{s.get('natural_completions',0)}/{count}**. Tiempo de la prueba: **{n(s.get('duration_s'))} s**."
                lines[12]=lines[12].replace('Respuesta completa del 95%','Fin de petición del 95%').replace('Completadas','Peticiones sin error')
                lines[6]=f"Límite impuesto al servidor: **{c['server_limit']} activas**. Cada persona espera {c.get('think_seconds',30)} s tras su respuesta y conserva los mensajes reales anteriores. El historial inicial se aproxima al objetivo; la tabla muestra los tokens realmente enviados en cada turno."
                reasoning_label='desactivado' if s['reasoning_mode']=='disabled' else 'predeterminado del servidor'
                lines[8]=f"Control mediante `/v1/chat/completions`, con conversaciones ficticias en español. Modo de razonamiento: **{reasoning_label}**. Cada respuesta puede terminar antes del límite de {c.get('output_tokens',512)} tokens. Se distinguen primer texto del modelo, respuesta visible y finalización natural. No es una evaluación de calidad semántica."
                lines+=['','### Respuesta visible y finalización natural','','| Turno | Respuestas con contenido visible | Terminaron sin alcanzar el límite de salida | Espera p95 al contenido visible |','|---|---:|---:|---:|']
                for t in s.get('per_turn',[]):lines.append(f"| {t['turn']} | {t['visible_answers']}/{t['expected']} | {t['natural_completions']}/{t['expected']} | {n(t['visible_ttft_p95_s'])} s |")
                lines+=['','En este control, cumplir la referencia requiere además que todas las respuestas tengan contenido visible antes de 5 s (p95) y terminen naturalmente. Alcanzar el límite de salida conserva la medición, pero no se presenta como una respuesta terminada naturalmente.']
                lines+=['','Que el modelo termine la petición por sí mismo (`stop`) no garantiza que haya entregado una respuesta visible: puede haber generado solo razonamiento. Por eso se muestran ambos recuentos. La velocidad incluye todos los tokens de salida, también los de razonamiento; no equivale necesariamente a la velocidad del texto que lee la persona.']
            lines+=['','La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.','',
                    '## Memoria y comportamiento del grupo','', '| Medida | Resultado |','|---|---|',
                    f"| Espera media al primer texto | {n(s.get('mean_ttft_s'))} s |",
                    f"| Tiempo medio de respuesta completa | {n(s.get('mean_total_s'))} s |",
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
                    f"| Tiempo total de la prueba, incluyendo pausas | {n(s.get('duration_s'))} s |",
                    f"| Espera máxima sin datos en una conexión | {n(s.get('request_timeout_s'),0)} s |",
                    f"| Plazo máximo configurado para todo el grupo | {n(s.get('test_timeout_s'),0)} s |",'',
                    'Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.','',
                    '## Cada persona y cada mensaje','',
                    '| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |',
                    '|---|---:|---:|---:|---:|---:|---|']
            if c.get('parent_state'):
                parts=pathlib.PurePosixPath(c['parent_state']).parts
                at=parts.index('profiles');parent_profile=parts[at+1];parent_case=parts[at+2]
                parent_fraction=next(p['fraction'] for p in meta['profiles'] if p['id']==parent_profile)
                parent_folder=f"memoria-{round(parent_fraction*100)}-{parent_case}"
                origin_position=lines.index('## Cada persona y cada mensaje')
                lines[origin_position:origin_position]=['## Historial de origen','',
                        f"Esta prueba continúa los historiales de [la etapa anterior](../{parent_folder}/README.md), conservando sus respuestas reales. Antes del primer turno se añade entrada sintética hasta {n(c['input_tokens'],0)} tokens. No se simulan los turnos intermedios entre ambos tamaños ni se presupone que todo el historial siga en la caché de la GPU.",'']
            position=lines.index('## Cada persona y cada mensaje')
            person_lines=['## Resumen por persona','',
                          '| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |',
                          '|---|---:|---:|---:|---:|---:|']
            for user in range(c['users']):
                individual=[r for r in requests if r['user_id']==user]
                completed=[r for r in individual if r['ok']]
                latencies=[r['ttft_s'] for r in completed if r.get('ttft_s') is not None]
                elapsed=max(r['finished_at_s'] for r in individual)-min(r['started_at_s'] for r in individual) if individual else None
                mean_latency=sum(latencies)/len(latencies) if latencies else None
                mean_total=sum(r['total_s'] for r in completed)/len(completed) if completed else None
                throughput=sum(r['usage']['completion_tokens'] for r in completed)/elapsed if elapsed else None
                person_lines.append(f"| {user+1} | {len(completed)}/{c.get('turns',3)} | {n(mean_latency)} s | {n(mean_total)} s | {n(elapsed)} s | {n(throughput,2)} |")
            person_lines+=['','Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.','']
            lines[position:position]=person_lines
            if s.get('kind')=='chat_recurrent':
                heading=next(i for i,line in enumerate(lines) if line.startswith('| Persona | Turno |'))
                lines[heading]=lines[heading].replace('| Respuesta completa |','| Espera a respuesta visible | Fin de petición |')
                lines[heading+1]='|---|---:|---:|---:|---:|---:|---:|---|'
            for r in requests:
                u=r.get('usage') or {};result=('Terminó naturalmente' if r.get('naturally_finished') else 'Alcanzó el límite de salida') if r['ok'] and s.get('kind')=='chat_recurrent' else 'Completa' if r['ok'] else 'Error: '+str(r.get('error','longitud inesperada')).replace('|','/')
                if r['ok'] and s.get('kind')=='chat_recurrent' and not r.get('has_visible_answer'):result+='; sin respuesta visible'
                visible_cell=f"{n(r.get('visible_ttft_s'))} s | " if s.get('kind')=='chat_recurrent' else ''
                lines.append(f"| {r['user_id']+1} | {r['turn']} | {n(r['input_tokens'],0)} + {n(u.get('completion_tokens'),0)} | {n(r.get('ttft_s'))} s | {visible_cell}{n(r.get('total_s'))} s | {n(rate(r),2)} | {result} |")
            if measurement_available and len(requests)<count:lines+=['',f"No hay un resultado final registrado para {count-len(requests)} turnos previstos. Pueden incluir peticiones pendientes al interrumpirse la prueba y turnos posteriores que no llegaron a enviarse. No se cuentan como respuestas recibidas."]
            maximum=sum(r['usage']['total_tokens']==262144 for r in good)
            if maximum:lines+=['',f'**Llegaron exactamente al máximo de 262.144 tokens y completaron la respuesta: {maximum} conversaciones.**']
            sources=[('Mediciones originales','mediciones.json'),('Configuración','configuracion.json'),('Registro de ejecución','registro-de-ejecucion.log'),('Comando ejecutado','comando-ejecutado.json')]
            links=' · '.join(f'[{label}]({name})' for label,name in sources if (folder/name).exists())
            lines+=['','## Datos y reproducción','',links,'']
            if not measurement_available:
                lines[4]=f"**No se generó un archivo de mediciones.** El cliente terminó con código {case_record['exit_code']}. Se conservan la configuración, el estado del controlador y los registros disponibles. Este fallo no permite determinar cuántas respuestas recibió el cliente ni atribuir el problema a la memoria del modelo."

            if (folder/'historiales-reproducibles.json.gz').exists():lines+=['[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.','']
            if s.get('kind')=='chat_recurrent':
                lines=[line.replace('Tiempo medio de respuesta completa','Tiempo medio hasta fin de petición').replace('| Respuesta completa |','| Fin de petición |') for line in lines]
            if measurement_available and c['id'].startswith('chat-comprobacion-medidor-'):
                lines[4]=f"**Comprobación del medidor de chat.** Peticiones sin error: **{len(good)}/{count}**. Esta prueba pequeña verifica la recogida de tiempos y la continuidad de los mensajes; no se utiliza para elegir la memoria ni para calificar la fluidez del uso normal."
                lines=[line.replace('| No cumple |','| No se evalúa |').replace('| Cumple |','| No se evalúa |') for line in lines]
            if case_record.get('interrupted'):
                lines[4]=f"**Prueba interrumpida por el controlador.** Se conservan **{len(good)}/{count}** respuestas recibidas y la última medición, tomada a los **{n(s.get('duration_s'))} s**. No se completó el grupo."
                lines[5:5]=['','El lanzador perdió su canal de salida (`BrokenPipeError`) y detuvo el cliente. Este es un fallo de ejecución de la prueba; no demuestra falta de memoria del modelo. Las mediciones originales se conservan sin cambios y su estado interno puede seguir indicando «running», porque son el último registro anterior a la interrupción. El tiempo mostrado corresponde a ese registro, no a una finalización normal. Se repite el ensayo completo como una prueba separada. [Evidencia de la interrupción](interrupcion.json).','']
            elif c['id'].endswith('-repeticion-por-interrupcion'):
                original_folder=folder.name.removesuffix('-repeticion-por-interrupcion')
                lines[0]+=' · repetición tras interrupción'
                lines[5:5]=['',f'Se repite la carga del [intento interrumpido](../{original_folder}/README.md), después de recrear el contenedor. Ambos intentos se conservan por separado. Las cifras de este informe corresponden exclusivamente a esta repetición; no se suman respuestas del intento anterior.','']
            (folder/'README.md').write_text('\n'.join(lines))
    (equipment/'inventario-originales.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
    existing=(OUT/'README.md').read_text();existing=existing.split('<!-- resultados-inicio -->')[0].rstrip()
    notice='**Se están realizando nuevas pruebas de conversaciones recurrentes con 10, 20 y 30 usuarios.**'
    if plan['status']!='running':existing=existing.replace(notice+'\n','')
    lines=[existing,'','<!-- resultados-inicio -->','## Configuraciones utilizadas','',
           '| Configuración | Presupuesto | Límite activo | Servicio listo | Espera hasta estar listo | Reserva de caché registrada |',
           '|---|---:|---:|---|---:|---:|']
    for profile in meta['profiles']:
        log=cache/'profiles'/profile['id']/'startup.log'
        match=re.search(r'Available KV cache memory: ([0-9.]+) GiB',log.read_text()) if log.exists() else None
        reserve=float(match.group(1)) if match else None
        status='Sí' if profile.get('ready') else 'No' if profile.get('state')=='startup_failed' else 'En curso'
        profile_labels={'seleccion-memoria-':'Comparación inicial de memoria',
                        'ajuste-memoria-':'Ajuste del presupuesto',
                        'comparacion-usuarios-y-chat-':'Comparación de usuarios y controles de chat',
                        'crecimiento-memoria-':'Ampliación del historial',
                        'chat-salida-2048-':'Chat con hasta 2.048 tokens de salida',
                        'historial-muy-largo-repeticion-':'Historiales muy largos: repetición tras interrupción',
                        'historial-muy-largo-':'Historiales muy largos',
                        'contexto-maximo-':'Comprobación del contexto máximo'}
        profile_title=next((label for prefix,label in profile_labels.items() if profile['id'].startswith(prefix)),profile['id'].replace('-', ' ').capitalize())
        title=f"[{profile_title}](configuracion-y-registros/{profile['id']}/arranque.log)" if log.exists() else profile_title
        lines.append(f"| {title} | {round(profile['fraction']*100)}% | {profile['server_limit']} | {status} | {n(profile.get('startup_seconds'))} s | {n(reserve,2)} GiB |")
    lines+=['','La reserva de caché procede del registro de arranque. No equivale a memoria ocupada por conversaciones ni permite deducir por sí sola cuántas personas tendrán una respuesta fluida. El pico de ocupación de esa reserva se mide durante cada prueba.',
           '', 'La espera hasta estar listo se mide después de aplicar la configuración. Si la siguiente etapa conserva los mismos parámetros, Docker puede reutilizar el contenedor y esa espera será casi cero; no significa que el modelo se haya cargado desde cero en ese tiempo. La espera al primer texto de cada conversación se mide por separado.','',
           '## Resultados publicados','',
           'Cada fila corresponde a un intento cerrado, incluidos los interrumpidos, que se identifican expresamente. En una interrupción se conserva la última medición disponible; su duración y percentiles son parciales. Los percentiles del primer turno y de las continuaciones se muestran separados.','',
           '| Prueba | Memoria | Usuarios / límite | Historial inicial | Peticiones sin error | Espera p95 primer turno | Espera p95 continuaciones | Velocidad p05 continuaciones | Caché máxima | Recálculos | Tiempo total | Continuaciones |',
           '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|']
    for r in rows:
        c=r['config'];s=r['summary']
        if c['id'].startswith('chat-comprobacion-medidor-'):continue
        count_text=f"{r['done']}/{r['count']}" if r['measurement_available'] else 'Sin mediciones'
        lines.append(f"| [{case_title(c)}]({r['folder']}/README.md) | {round(c['memory_fraction']*100)}% | {c['users']} / {c['server_limit']} | {n(c['input_tokens'],0)} | {count_text} | {n(r['cold95'])} s | {n(r['follow95'])} s | {n(r['decode05'],2)} tokens/s | {n(100*s['peak_kv_fraction'] if s.get('peak_kv_fraction') is not None else None)}% | {n(s.get('preemptions'),0)} | {n(s.get('duration_s'))} s | {r['label']} |")
    checks=[r for r in rows if r['config']['id'].startswith('chat-comprobacion-medidor-')]
    if checks:
        lines+=['','## Comprobaciones del medidor de chat','',
                'Estas pruebas pequeñas comprueban la captura de tiempos y la conservación de los mensajes. Sus respuestas tienen un límite de salida reducido; no se utilizan para decidir la memoria necesaria ni la fluidez del uso normal. Se conservan también sus errores y los casos que agotan ese límite.','',
                '| Comprobación | Memoria | Usuarios | Turnos | Límite de salida | Peticiones sin error | Con texto visible | Terminadas por el modelo | Tiempo |',
                '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
        for r in checks:
            c=r['config'];s=r['summary']
            lines.append(f"| [{case_title(c)}]({r['folder']}/README.md) | {round(c['memory_fraction']*100)}% | {c['users']} | {c['turns']} | {c.get('output_tokens',512)} | {r['done']}/{r['count']} | {s.get('visible_answers',0)}/{r['count']} | {s.get('natural_completions',0)}/{r['count']} | {n(s.get('duration_s'))} s |")
    lines+=['','[Configuración y registros de esta campaña](configuracion-y-registros/metadata.json).','']
    lines[3:3]=comparison_overview(rows,plan)
    (OUT/'README.md').write_text('\n'.join(lines))
    (OUT/'resumen.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    subprocess.run([sys.executable,str(ROOT/'scripts/build_report.py')],check=True,cwd=ROOT)
    subprocess.run([sys.executable,str(ROOT/'scripts/validate_report.py')],check=True,cwd=ROOT)
    subprocess.run([sys.executable,str(ROOT/'scripts/validate_recurrent.py')],check=True,cwd=ROOT)
    subprocess.run(['git','diff','--check'],check=True,cwd=ROOT)
    if a.publish:
        subprocess.run([sys.executable,str(ROOT/'scripts/validate_new_public_files.py')],check=True,cwd=ROOT)
        subprocess.run(['git','add','--','README.md','GUIA-DE-LECTURA.md',str(MODEL/'README.md'),str(OUT),'scripts/README.md','scripts/build_report.py','scripts/recurrent_campaign.py','scripts/advance_recurrent_maximum.py','scripts/finalize_recurrent_campaign.py','scripts/recurrent_probe.py','scripts/chat_probe.py','scripts/recurrent_report.py','scripts/validate_report.py','scripts/validate_recurrent.py','scripts/validate_new_public_files.py','scripts/verify_recurrent_restore.py'],check=True,cwd=ROOT)
        if subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT).returncode:
            subprocess.run(['git','commit','-m',a.message],check=True,cwd=ROOT)
        subprocess.run(['git','push'],check=True,cwd=ROOT)


if __name__=='__main__':
    import sys
    main()
