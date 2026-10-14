#!/usr/bin/env python3
"""Generate readable model reports with each test's explanation beside its data."""
import json
import pathlib
import re
import statistics

ROOT=pathlib.Path(__file__).resolve().parents[1]
MODELS=ROOT/'modelos'

def number(value,digits=1):
    return 'No medido' if value is None else f'{value:,.{digits}f}'.replace(',','@').replace('.',',').replace('@','.')
def integer(value):return '—' if value is None else number(value,0)
def average(values):
    values=[v for v in values if v is not None]
    return statistics.mean(values) if values else None
def link(path,base):
    import os
    return pathlib.Path(os.path.relpath(path,base)).as_posix()
def read(path):return json.loads(path.read_text())
def percent(value):return 'No medido' if value is None else number(value)+'%'

def load_test(path,equipment):
    c=read(path);raw=read(path.with_name('mediciones.json'))
    t={'path':path.parent,'c':c,'raw':raw,'type':c['tipo'],'memory':c['memoria_porcentaje'],
       'model_max':equipment.get('contexto_maximo_del_modelo'),'requests':[],
       'count':c.get('conversaciones_totales',0),'done':0,'failed':0,
       'input':c.get('tokens_entrada',0),'output':c.get('tokens_respuesta_pedidos',0),
       'concurrency':c.get('concurrencia_enviada',0),'limit':c['limite_servidor'],
       'context':c['limite_contexto_configurado']}
    for k in ['ttft','response','sum_response','duration','throughput','request_rate','cache','queue','active','overlap','engine','system','preemptions']:
        t[k]=None
    if t['type']=='arranque':
        t['title']=('Comprobar servidor ya preparado' if raw.get('reused_running_server') else 'Arrancar el modelo')+' con límite de '+integer(t['context'])+' tokens'
        t.update(duration=raw['startup_seconds'],state='Arrancó' if raw['ready'] else '**NO ARRANCÓ**',finished=raw['ready'])
        return t
    if t['type']=='rechazo':
        t.update(title='Enviar más tokens que el límite permitido',duration=raw['elapsed_s'],
                 state='Rechazo esperado: HTTP '+str(raw['http_status']),finished=True)
        return t
    s=raw.get('summary',{})
    t['summary']=s
    t['requests']=sorted(raw.get('requests',[]),key=lambda r:r['index'])
    good=[r for r in t['requests'] if r.get('ok')]
    t['good']=good
    if 'model_id' in raw:
        t.update(done=raw['completed'],failed=raw['failed'],duration=raw['duration'],
                 ttft=raw['mean_ttft_ms']/1000,response=raw['mean_e2el_ms']/1000,
                 sum_response=raw['mean_e2el_ms']/1000*raw['completed'],throughput=raw['output_throughput'],finished=True)
    else:
        t.update(done=s.get('completed',len(good)),failed=s.get('failed',0),duration=s.get('duration_s'),
                 ttft=average([r.get('ttft_s') for r in good]),response=average([r.get('total_s') for r in good]),
                 sum_response=sum(r['total_s'] for r in good) if good else None,
                 cache=100*s['peak_kv_fraction'] if s.get('peak_kv_fraction') is not None else None,
                 queue=s.get('peak_waiting'),active=s.get('peak_running'),engine=s.get('peak_gpu_engine_percent'),
                 system=s.get('peak_system_used_percent'),preemptions=s.get('preemptions'),
                 finished=s.get('status','complete')=='complete')
        if good and t['duration']:
            t['throughput']=sum(r['usage']['completion_tokens'] for r in good)/t['duration']
            t['request_rate']=average([r['usage']['completion_tokens']/r['total_s'] for r in good])
        if t['finished']:t['overlap']=s.get('peak_overlapping_responses')
    t['reached_model']=sum(r['usage']['prompt_tokens']+r['usage']['completion_tokens']==t['model_max'] for r in good)
    t['reached_configured']=sum(r['usage']['prompt_tokens']+r['usage']['completion_tokens']==t['context'] for r in good)
    t['all_done']=t['done']==t['count'] and not t['failed'] and t['finished']
    t['title']=f"{t['count']} {'conversación' if t['count']==1 else 'conversaciones'}, hasta {t['concurrency']} a la vez; {integer(t['input'])} de entrada + {integer(t['output'])} de respuesta"
    if c.get('historial_reutilizado'):
        phase=c['paso_historial']
        t['title']=('Historial nuevo' if phase==1 else 'Repetir historial' if phase%2==0 else 'Ampliar historial')+f": {integer(t['input'])} + {integer(t['output'])} tokens"
    if c.get('medicion_inicial'):t['title']+=' (primera medición)'
    if t['all_done']:
        t['state']=('Terminó con '+integer(t['preemptions'])+' recálculos' if t['preemptions'] else
                    'Terminó atendiendo por turnos' if t['active'] is not None and t['active']<t['concurrency'] else 'Terminó')
    elif t['failed']:t['state']='Hubo errores'
    elif s.get('status')=='not_admitted_within_90s':t['state']='Detenida: 90 s en cola sin iniciar'
    elif s.get('status')=='timeout_1500s':t['state']='No terminó dentro de 1.500 s'
    else:t['state']='En curso'
    return t

def completion(t):
    if t['type']=='arranque':return t['state']
    if t['type']=='rechazo':return 'Rechazada, como se esperaba'
    if t['all_done']:return f"**Sí: {t['done']}/{t['count']}**"
    return f"{t['done']}/{t['count']} ({t['state'].lower()})"

def maximum(t):
    if t['type']!='conversaciones':return 'No se enviaron conversaciones' if t['type']=='arranque' else 'Superarlo fue rechazado'
    if t['reached_model']:return f"**Sí: {t['reached_model']}/{t['count']}**"
    if t['reached_configured'] and t['context']!=t['model_max']:
        return 'Llegó a '+integer(t['context'])+'; límite reducido'
    if t['input']+t['output']==t['model_max']:return 'Todavía no' if not t['finished'] else 'No'
    return 'No se intentó'

def behavior(t):
    if t['type']!='conversaciones':return t['state']
    bits=[]
    if t['overlap'] is not None:bits.append('1 respuesta a la vez' if t['overlap']==1 else integer(t['overlap'])+' respuestas solapadas')
    elif t['active'] is not None:bits.append('1 activa en el motor' if t['active']==1 else integer(t['active'])+' activas en el motor')
    if t['queue'] is not None:bits.append('cola máxima '+integer(t['queue']))
    if t['preemptions']:bits.append(integer(t['preemptions'])+' recálculos')
    if t['failed']:bits.append(integer(t['failed'])+' errores')
    return '; '.join(bits) or 'No se guardó este detalle'

def evidence(t):
    lines=['','<details>','<summary>Mediciones originales y registros de esta prueba</summary>','',
           '- [Mediciones originales](mediciones.json).','- [Configuración de esta prueba](configuracion.json).']
    for path in sorted(t['path'].glob('*.log')):lines.append(f'- [{path.stem.replace("-"," ").capitalize()}]({path.name}).')
    return lines+['','</details>','']

def write_test(t,model_dir,equipment):
    lines=['# '+t['title'],'',f"[Volver al modelo]({link(model_dir/'README.md',t['path'])}) · [Ver las pruebas con esta memoria](../README.md)",'',
           f"**Modelo:** `{t['c']['modelo']}`. **Memoria asignada:** {t['memory']}% del GB10.",'']
    if t['type']=='arranque':
        lines += [f"**Resultado: {t['state']}.**",'',f"Se comprobó el arranque con un límite de **{integer(t['context'])} tokens por conversación** y hasta **{t['limit']} solicitudes activas**.",'',
                  f"Tiempo de comprobación: **{number(t['duration'])} segundos**.",'']
        if t['raw'].get('reused_running_server'):lines += ['El servidor ya estaba preparado. Este tiempo es la comprobación de disponibilidad, no la carga del modelo.','']
        if not t['raw']['ready']:
            lines += ['No se pudieron enviar conversaciones con esta configuración. Que otro contexto más pequeño arranque no convierte este intento en correcto.','']
            log=t['path']/'registro-del-servidor.log'
            if log.exists():
                errors=[line for line in log.read_text().splitlines() if any(x in line for x in ('ValueError:','RuntimeError:','OutOfMemoryError:'))]
                if errors:lines += ['<details>','<summary>Mensaje exacto del error</summary>','','```text',*errors[:5],'```','','</details>','']
        lines += ['Arrancar solo demuestra que el servicio está disponible. Las pruebas de conversaciones comprueban si las respuestas llegan a terminar.']
    elif t['type']=='rechazo':
        lines += ['**Resultado: rechazo esperado.**','',f"Se enviaron {integer(t['input'])} tokens de entrada y se pidió {integer(t['output'])} de respuesta: la suma supera el límite configurado.",'',
                  f"La API respondió HTTP {t['raw']['http_status']} en {number(t['duration'],3)} s. Esto comprueba el límite de tokens, no un fallo de memoria."]
    else:
        lines += ['## ¿Qué ocurrió?','',f"- **¿Terminaron todas las conversaciones?** {completion(t)}. Terminar significa recibir todos los tokens de respuesta solicitados.",
                  f"- **¿Llegaron al máximo del modelo ({integer(t['model_max'])} tokens)?** {maximum(t)}.",
                  f"- **Límite configurado en esta prueba:** {integer(t['context'])} tokens, sumando entrada y respuesta.",
                  f"- **¿Se atendieron al mismo tiempo?** {behavior(t)}.",
                  f"- **Tiempo para completar la prueba:** {number(t['duration'])} s.",'',
                  f"{'Se envió **1 conversación**' if t['count']==1 else 'Se enviaron **'+str(t['count'])+' conversaciones**'}, hasta **{t['concurrency']} a la vez**. Cada una pidió **{integer(t['input'])} tokens de entrada + {integer(t['output'])} de respuesta = {integer(t['input']+t['output'])} tokens**.",'']
        if t['reached_configured']:
            lines += [f"**{t['reached_configured']} conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**",'']
        if t['reached_model']:
            lines += ['Esta prueba llega al máximo sumando historial y respuesta. No es una generación de todo ese máximo como respuesta nueva.','']
        lines += ['## Cada conversación: tokens y finalización','',
                  '| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |',
                  '|---|---:|---:|---:|---:|---|---|']
        for r in t['requests']:
            u=r.get('usage') or {};inp=u.get('prompt_tokens');out=u.get('completion_tokens');total=inp+out if inp is not None and out is not None else None
            lines.append(f"| {r['index']+1} | {integer(inp)} | {integer(t['output'])} | {integer(out)} | {integer(total)} | {'Sí' if r.get('ok') else 'No'} | {'Sí' if t['model_max'] is not None and total==t['model_max'] else 'No'} |")
        if not t['requests']:lines += ['', 'Todavía no hay conversaciones terminadas.' if not t['finished'] else 'En esta primera medición solo se guardaron cifras del grupo; no se inventan datos individuales.']
        lines += ['', '## Cada conversación: tiempos y velocidad','',
                  '| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |',
                  '|---|---:|---:|---:|---:|']
        for r in t['requests']:
            u=r.get('usage') or {};out=u.get('completion_tokens');elapsed=r.get('total_s');first=r.get('ttft_s')
            rate=(out-1)/(elapsed-first) if out and elapsed and first is not None and elapsed>first else None
            lines.append(f"| {r['index']+1} | {number(first,2)} | {number(elapsed,2)} | {number(rate,2)} | {number(out/elapsed if out and elapsed else None,2)} |")
        rows=[('Memoria asignada al motor',str(t['memory'])+'%'),('Pico medido del motor / memoria del GB10',percent(t['engine'])),
              ('Pico usado por todo el sistema / memoria del GB10',percent(t['system'])),('Conversaciones totales',integer(t['count'])),
              ('Máximo de peticiones enviadas a la vez',integer(t['concurrency'])),('Límite de solicitudes del servidor',integer(t['limit'])),
              ('Máximo activo en el motor',integer(t['active'])),('Máximo de respuestas solapadas',integer(t['overlap'])),
              ('Espera media hasta primer texto',number(t['ttft'])+' s'),('Tiempo medio de respuesta completa',number(t['response'])+' s'),
              ('Suma de los tiempos individuales',number(t['sum_response'])+' s'),('Tiempo total de la prueba',number(t['duration'])+' s'),
              ('Tokens/s medios por conversación, incluyendo espera',number(t['request_rate'],2)),('Tokens/s totales del grupo',number(t['throughput'],2)),
              ('Pico de caché ocupada',percent(t['cache'])),('Máximo de solicitudes en cola',integer(t['queue'])),
              ('Recálculos por falta de espacio en caché',integer(t['preemptions']))]
        s=t.get('summary',{})
        rows += [('Tiempo observado con cola',number(s.get('seconds_with_queue'))+' s'),
                 ('Tiempo observado con caché al 95% o más',number(s.get('seconds_cache_above_95_percent'))+' s'),
                 ('Tokens recuperados de caché de prefijos',integer(s.get('prefix_cache_hits'))),('Temperatura GPU máxima',number(s.get('peak_gpu_temperature_c'))+' °C')]
        lines += ['', '## Todas las medidas del grupo','', '| Medida | Resultado |','|---|---|']+[f'| {name} | {value} |' for name,value in rows]
        lines += ['', 'La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.','',
                  'Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.']
        if any(r.get('started_at_s') is not None for r in t['requests']):
            lines += ['', '<details>','<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>','',
                      'Segundos desde el inicio de la prueba.','','| Conversación | Enviada | Primer texto | Final |','|---|---:|---:|---:|']
            lines += [f"| {r['index']+1} | {number(r.get('started_at_s'),2)} | {number(r.get('first_token_at_s'),2)} | {number(r.get('finished_at_s'),2)} |" for r in t['requests']]
            lines += ['','</details>']
    lines += evidence(t)
    (t['path']/'README.md').write_text('\n'.join(lines))

def table(tests,base,full=False):
    if full:
        lines=['| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |',
               '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|']
    else:
        lines=['| Prueba | Memoria asignada | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |',
               '|---|---:|---:|---|---|---:|---|']
    for t in tests:
        label=t['title']
        if t['type']=='conversaciones' and not t['c'].get('historial_reutilizado'):
            label=f"{t['count']} {'conversación' if t['count']==1 else 'conversaciones'}; hasta {t['concurrency']} a la vez"
            if t['c'].get('medicion_inicial'):label+=' · primera medición'
        title=f"[{label}]({link(t['path']/'README.md',base)})"
        tokens=integer(t['input'])+' + '+integer(t['output']) if t['type']!='arranque' else 'Sin conversaciones'
        if full:
            lines.append(f"| {title} | {t['memory']}% | {percent(t['engine'])} | {percent(t['system'])} | {tokens} | {t['concurrency']} / {t['limit']} / {integer(t['active'])} / {integer(t['overlap'])} | {completion(t)} | {number(t['ttft'])} | {number(t['response'])} | {number(t['sum_response'])} | {number(t['duration'])} | {number(t['request_rate'],2)} | {number(t['throughput'],2)} | {percent(t['cache'])} | {integer(t['queue'])} | {integer(t['preemptions'])} | {t['state']} |")
        else:
            lines.append(f"| {title} | {t['memory']}% | {tokens} | {completion(t)} | {maximum(t)} | {number(t['duration'])} s | {behavior(t)} |")
    return lines

def main():
    model_summaries=[]
    for model_dir in sorted(MODELS.iterdir()):
        if not model_dir.is_dir():continue
        eqfile=model_dir/'configuracion-del-equipo/equipo.json'
        equipment=read(eqfile) if eqfile.exists() else {}
        tests=[load_test(p,equipment) for p in model_dir.glob('memoria-*/**/configuracion.json')]
        if not tests:continue
        tests.sort(key=lambda t:(t['memory'],t['limit'],t['input'],t['concurrency'],t['output'],t['c'].get('medicion_inicial',False),t['path'].name))
        for t in tests:write_test(t,model_dir,equipment)
        model=tests[0]['c']['modelo'];maximum_model=equipment.get('contexto_maximo_del_modelo')
        statuses=list((model_dir/'configuracion-del-equipo').rglob('plan-y-estado-general.json'))
        complete=bool(statuses and read(statuses[0]).get('status')=='complete')
        lines=['# '+model.split('/')[-1],'','[Volver al inicio](../../README.md) · [Cómo leer las medidas](../../GUIA-DE-LECTURA.md)','',
               f'**Modelo exacto:** `{model}`.','',
               '**Estado:** '+('pruebas terminadas y configuración original restaurada.' if complete else 'pruebas en curso. Los resultados se actualizan a medida que terminan.'),'',
               f'**Máximo por conversación: {integer(maximum_model)} tokens, sumando historial y respuesta.** '
               'La memoria asignada puede obligar a configurar un límite menor.','',
               '“Terminó” significa que entregó todos los tokens de respuesta solicitados. '
               '“Llegó al máximo” exige además que la suma real de entrada y respuesta alcance ese máximo; arrancar el servidor no basta.','',
               '## ¿Puede llegar al máximo y terminar?','']
        for mem in sorted({t['memory'] for t in tests}):
            subset=[t for t in tests if t['memory']==mem and t['type']=='conversaciones']
            reaching=[t for t in subset if t['reached_model']]
            if reaching:
                best=sorted(reaching,key=lambda t:(t['c'].get('medicion_inicial',False),-t['done']))[0]
                statement=f"**Sí:** {best['reached_model']}/{best['count']} completadas con {integer(maximum_model)} tokens y toda la respuesta solicitada. {behavior(best)}."
            else:
                totals=[r['usage']['prompt_tokens']+r['usage']['completion_tokens'] for t in subset for r in t.get('good',[])]
                statement=('Hasta ahora se ha completado una conversación de **'+integer(max(totals))+' tokens**. Aún no demuestra alcanzar '+integer(maximum_model)+'.') if totals else 'Todavía no hay una conversación terminada registrada con este presupuesto.'
                failed=[t for t in tests if t['memory']==mem and t['type']=='arranque' and not t['raw']['ready'] and t['context']==maximum_model]
                if failed:statement+=' **El arranque con el máximo del modelo falló.**'
            lines.append(f'- **{mem}% de memoria:** '+statement)
        previous=(model_dir/'README.md').read_text() if (model_dir/'README.md').exists() else ''
        match=re.search(r'<!-- interpretacion-inicio -->\n(.*?)\n<!-- interpretacion-fin -->',previous,re.S)
        commentary=match.group(1) if match else 'Las recomendaciones se completarán al terminar las comparaciones de memoria, concurrencia e historiales reutilizados.'
        lines += ['', '## Qué configuración elegir','', '<!-- interpretacion-inicio -->',commentary,'<!-- interpretacion-fin -->','',
                  '## Todas las pruebas','', 'Abre el nombre de una prueba para ver cada conversación, sus tiempos, los tokens recibidos y sus registros. Las primeras mediciones se conservan y están identificadas.','']
        lines += table(tests,model_dir)
        lines += ['', '<details>', '<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>', '']+table(tests,model_dir,True)+['','</details>','',
                  '## Carpetas por memoria','']
        for mem in sorted({t['memory'] for t in tests}):
            folder=model_dir/f'memoria-{mem}-por-ciento';subset=[t for t in tests if t['memory']==mem]
            (folder/'README.md').write_text('\n'.join([f'# Pruebas con {mem}% de memoria','',f'[Volver a todas las pruebas del modelo](../README.md)','',
                f'En estas pruebas se reservó el **{mem}% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.','']+table(subset,folder)+['']))
            lines.append(f'- [{mem}% de memoria]({folder.name}/README.md).')
        lines += ['', '## Equipo y configuración','',f"GB10: {number(equipment.get('memoria_total_gib'),2)} GiB. Pesos del modelo: {number(equipment.get('pesos_del_modelo_gib'),2)} GiB.",
                  f"Imagen: `{equipment.get('imagen','No registrada')}`. vLLM: `{equipment.get('version_vllm','No registrada')}`.",'',
                  '[Configuración y registros del equipo](configuracion-del-equipo).','']
        (model_dir/'README.md').write_text('\n'.join(lines))
        successful=sum(t['all_done'] for t in tests if t['type']=='conversaciones')
        model_summaries.append((model,model_dir,maximum_model,successful,len(tests),complete))
    lines=['# Pruebas de modelos en el GB10','',
           'Resultados para decidir cuánta memoria reservar y cuántas conversaciones puede atender cada modelo, incluyendo historiales cercanos a su límite.','',
           '**Estado:** '+('pruebas terminadas y configuración original restaurada.' if model_summaries and all(m[-1] for m in model_summaries) else 'pruebas en curso; se publican tanto los éxitos como los fallos.'),'',
           '## Resultados por modelo','', '| Modelo | Máximo por conversación | Informe |','|---|---:|---|']
    for model,folder,limit,good,total,complete in model_summaries:
        lines.append(f'| {model.split("/")[-1]} | {integer(limit)} tokens | [Ver resultados y qué configuración elegir]({link(folder/"README.md",ROOT)}) |')
    lines += ['', '## Qué puedes comprobar','',
              '- **Si todas las conversaciones terminaron:** cuántas recibieron la respuesta completa solicitada.',
              '- **Si llegaron al máximo de tokens:** se comprueba la suma real de historial y respuesta. También se distingue un límite reducido por falta de memoria.',
              '- **Si respondieron a la vez o por turnos:** se muestran el solapamiento, las colas y los recálculos.',
              '- **Cuánto tardaron y cuánta memoria usaron:** cada prueba incluye los tiempos y velocidades de cada conversación.','',
              'Un ejemplo: **262.016 tokens de historial + 128 de respuesta = 262.144 tokens en la conversación**. Llegar a ese límite no significa generar 262.144 tokens de respuesta nueva.','',
              '## Dónde está cada cosa','',
              'Entra en **modelos → nombre del modelo → porcentaje de memoria → prueba**. Cada prueba tiene su explicación en `README.md`, las mediciones originales y sus registros en la misma carpeta.','',
              '- [Guía de lectura](GUIA-DE-LECTURA.md): significado de las medidas y cómo se hicieron las pruebas.',
              '- [Herramientas de prueba](scripts): scripts para medir y actualizar los informes.','']
    (ROOT/'README.md').write_text('\n'.join(lines))
    print(f'Generated readable reports for {len(model_summaries)} model(s).')

if __name__=='__main__':main()
