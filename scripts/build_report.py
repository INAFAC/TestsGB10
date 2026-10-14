#!/usr/bin/env python3
"""One comparison table per model, plus per-conversation evidence."""
import collections
import json
import pathlib
import re
import statistics

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT/'results'
DETAILS = ROOT/'details'
DEFAULT_MODEL = 'nvidia/Qwen3.8-27B-NVFP4'


def num(x, digits=1):
    return 'N/M' if x is None else f'{x:.{digits}f}'.replace('.', ',')


def integer(x):
    return '—' if x is None else f'{int(x):,}'.replace(',', '.')


def mean(values):
    values = [x for x in values if x is not None]
    return statistics.mean(values) if values else None


def ident(path):
    return re.sub(r'[^a-zA-Z0-9-]+', '-', str(path.relative_to(DATA).with_suffix(''))).strip('-')


def memory(path):
    for part in path.parts:
        if part.startswith('memory-'):
            return int(part.split('-')[1])
    if any(part in ('short','context-40','detailed-short-40','reuse-40') for part in path.parts):
        return 40
    return None


def read_test(path):
    raw = json.loads(path.read_text())
    if not isinstance(raw, dict):
        return None
    if isinstance(raw, dict) and 'http_status' in raw and 'output_requested' in raw:
        t = dict.fromkeys(['engine_pct','system_pct','ttft','response','sum_response',
                          'throughput','mean_request_rate','cache','queue','preemptions','active'])
        t.update(id=ident(path), path=path, model=raw.get('model', DEFAULT_MODEL), memory=memory(path),
                 description='Superar el contexto máximo: rechazo esperado', input=raw['input_tokens'],
                 output=raw['output_requested'], concurrency=1, server_limit=4, count=1, completed=0,
                 duration=raw['elapsed_s'], requests=[], kind='rejection',
                 status='Rechazo esperado (HTTP '+str(raw['http_status'])+')')
        return t
    if 'model_id' in raw and 'mean_ttft_ms' in raw:
        count = raw['num_prompts']
        return {'id': ident(path), 'path': path, 'model': raw['model_id'], 'memory': memory(path),
                'description': 'Carga corta inicial (detalle individual no guardado)',
                'input': raw['total_input_tokens']//count, 'output': raw['total_output_tokens']//count,
                'concurrency': raw['max_concurrency'], 'server_limit': 4, 'active': None, 'count': count,
                'completed': raw['completed'], 'failed': raw['failed'],
                'ttft': raw['mean_ttft_ms']/1000, 'response': raw['mean_e2el_ms']/1000,
                'sum_response': raw['mean_e2el_ms']/1000*raw['completed'],
                'duration': raw['duration'], 'throughput': raw['output_throughput'],
                'mean_request_rate': None, 'cache': None, 'queue': None,
                'engine_pct': None, 'system_pct': None, 'preemptions': None,
                'requests': [], 'status': 'OK' if not raw['failed'] else 'Errores'}
    s = raw.get('summary', {})
    if 'input_tokens' not in s:
        return None
    requests = sorted(raw.get('requests', []), key=lambda r: r['index'])
    good = [r for r in requests if r.get('ok')]
    count = s.get('num_requests', s['concurrency'])
    total_output = sum(r.get('usage', {}).get('completion_tokens', 0) for r in good)
    status = ('OK' if s.get('completed') == count and not s.get('failed') else
              'No admitida en 90 s' if s.get('status') == 'not_admitted_within_90s' else
              'Interrumpida a los 1.500 s' if s.get('status') == 'timeout_1500s' else
              'En curso / incompleta')
    if s.get('failed'):
        status = 'Errores'
    elif status == 'OK' and s.get('preemptions', 0):
        status = 'Completa; recálculos'
    elif status == 'OK' and s.get('peak_running', s['concurrency']) < s['concurrency']:
        status = 'Completa; cola'
    description = ('Contexto casi máximo; prefijos independientes' if s['input_tokens'] >= 260000 else
                   'Respuesta larga; prefijos independientes' if s['output_tokens'] >= 2048 else
                   'Carga corta; prefijos independientes' if s['input_tokens'] <= 8192 else
                   'Historial largo; prefijos independientes')
    if 'reuse' in str(path):
        description = 'Reutilización de historial: '+path.stem
    elif 'detailed-short' in str(path):
        description = 'Carga corta con métricas individuales'
    if 'context-40' in path.parts:
        description += ' (serie inicial)'
    elif 'after30' in path.parts and memory(path) == 40 and s.get('server_max_num_seqs', 4) == 4:
        description += ' (repetición 40%)'
    return {'id': ident(path), 'path': path, 'model': s.get('model', DEFAULT_MODEL),
            'memory': round(s['memory_fraction']*100) if s.get('memory_fraction') is not None else memory(path), 'description': description, 'input': s['input_tokens'],
            'output': s['output_tokens'], 'concurrency': s['concurrency'], 'active': s.get('peak_running'),
            'server_limit': s.get('server_max_num_seqs', 4),
            'count': count, 'completed': s.get('completed', 0), 'failed': s.get('failed', 0),
            'ttft': mean([r.get('ttft_s') for r in good]),
            'response': mean([r.get('total_s') for r in good]),
            'sum_response': sum(r.get('total_s', 0) for r in good) if good else None,
            'duration': s.get('duration_s'),
            'throughput': total_output/s['duration_s'] if good and s.get('duration_s') else None,
            'mean_request_rate': mean([r['usage']['completion_tokens']/r['total_s'] for r in good if r.get('usage')]),
            'cache': 100*s['peak_kv_fraction'] if s.get('peak_kv_fraction') is not None else None,
            'queue': s.get('peak_waiting'), 'engine_pct': s.get('peak_gpu_engine_percent'),
            'system_pct': s.get('peak_system_used_percent'), 'preemptions': s.get('preemptions'),
            'requests': requests, 'status': status, 'summary': s}


def startup_tests():
    tests = []
    for path in sorted(DATA.rglob('metadata.json')):
        raw = json.loads(path.read_text())
        for profile in raw.get('profiles', []):
            fraction = round(profile['fraction']*100)
            seqs = profile.get('max_num_seqs', 4)
            label = 'memory-'+str(fraction)+(('-seqs-'+str(seqs)) if seqs != 4 else '')
            for attempt in profile.get('attempts', []):
                context = attempt['max_model_len']
                log = path.parent/label/('startup-'+str(context)+'.log')
                t = dict.fromkeys(['engine_pct','system_pct','ttft','response','sum_response',
                                  'throughput','mean_request_rate','cache','queue','preemptions','active'])
                t.update(id=ident(log), path=log if log.exists() else path,
                         model=raw.get('model', DEFAULT_MODEL), memory=fraction,
                         description=('Servidor ya preparado; contexto ' if attempt.get('reused_running_server') else 'Arranque con contexto máximo ')+integer(context),
                         input=0, output=0, concurrency=0, server_limit=seqs, count=0, completed=0,
                         duration=attempt['startup_seconds'], requests=[], kind='startup',
                         status='Arranque correcto' if attempt['ready'] else '**FALLO DE ARRANQUE**',
                         attempt=attempt)
                tests.append(t)
    return tests


def write_detail(t):
    path = DETAILS/(t['id']+'.md')
    source = '../'+t['path'].relative_to(ROOT).as_posix()
    if t.get('kind') == 'rejection':
        path.write_text('\n'.join(['# '+t['description'], '', '[Volver a la comparación](../README.md)', '',
                       f"Se enviaron {integer(t['input'])} tokens de entrada y se pidió {t['output']} de salida.", '',
                       'El rechazo demuestra que la API aplica el límite configurado; no mide falta de memoria.', '',
                       f"Resultado: **{t['status']}** en {num(t['duration'],3)} s.", '',
                       f'[Respuesta original]({source}).', '']))
        return
    if t.get('kind') == 'startup':
        raw = t['path'].read_text()
        errors = [line for line in raw.splitlines() if any(term in line for term in
                  ('ValueError:', 'RuntimeError:', 'OutOfMemoryError:', 'CUDA out of memory'))]
        lines = ['# '+t['description'], '', '[Volver a la comparación](../README.md)', '',
                 f"- Modelo: `{t['model']}`.", f"- Memoria asignada: {num(t['memory'],0)}%.",
                 f"- Límite del servidor: {t['server_limit']} solicitudes.",
                 f"- Resultado: {t['status']} en {num(t['duration'])} s.",
                 '- No se enviaron conversaciones en esta comprobación de arranque.',
                 ('- Se reutilizó el servidor ya preparado: la duración es la comprobación de salud, no el tiempo de cargar el modelo.' if t['attempt'].get('reused_running_server') else '- La duración mide la espera hasta disponibilidad o fallo tras recrear el servicio.'),
                 f'- [Registro original]({source}).', '', '```text',
                 *errors[:6], '```', '', 'Comando utilizado:', '', '```json',
                 json.dumps(t['attempt']['command'], ensure_ascii=False, indent=2), '```', '']
        path.write_text('\n'.join(lines))
        return
    lines = ['# '+t['id'], '', '[Volver a la comparación](../README.md)', '',
             t['description']+'.', '',
             f"- Modelo: `{t['model']}`.",
             f"- Presupuesto vLLM: {num(t['memory'],0)}% de la memoria del GB10.",
             f"- Entrada / salida por solicitud: {integer(t['input'])} / {integer(t['output'])} tokens.",
             f"- Solicitudes: {t['count']}; concurrencia del cliente: {t['concurrency']}; límite del servidor: {t['server_limit']}.",
             f"- Duración de la prueba: {num(t['duration'])} s.",
             f"- Resultado: **{t['status']}**, {t['completed']}/{t['count']} completadas.",
             f'- [Datos originales]({source}).', '',
             '## Conversaciones individuales', '',
             '| Conversación | Tokens entrada | Tokens salida | Inicio / TTFT (s) | Respuesta completa (s) | Generación (tokens/s) | Con espera incluida (tokens/s) | Enviada en (s) | Primer token en (s) | Final en (s) | Resultado |',
             '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|']
    for r in t['requests']:
        usage = r.get('usage') or {}
        output = usage.get('completion_tokens')
        elapsed = r.get('total_s')
        ttft = r.get('ttft_s')
        generation = ((output-1)/(elapsed-ttft)
                      if output and elapsed and ttft is not None and elapsed > ttft else None)
        e2e = output/elapsed if output and elapsed else None
        lines.append(f"| C{r['index']+1} | {integer(usage.get('prompt_tokens'))} | {integer(output)} "
                     f"| {num(ttft,2)} | {num(elapsed,2)} | {num(generation,2)} | {num(e2e,2)} "
                     f"| {num(r.get('started_at_s'),2)} | {num(r.get('first_token_at_s'),2)} | {num(r.get('finished_at_s'),2)} "
                     f"| {'OK' if r.get('ok') else 'Error'} |")
    if not t['requests']:
        lines += ['', '**No medido:** en esta primera serie se guardaron estadísticas agregadas, no los tiempos de cada solicitud. No se han reconstruido ni inventado valores individuales.']
    lines += ['', 'Generación = (tokens de salida − 1) / tiempo desde el primer token hasta el final. '
              'Con espera incluida = tokens de salida / tiempo completo de esa solicitud. '
              'Los tokens son los devueltos por la API, no el número de mensajes SSE.', '',
              '## Memoria y planificación', '',
              f"- Pico observado del motor GPU: {num(t['engine_pct'])}% del GB10 ({num(t.get('summary', {}).get('peak_gpu_engine_gib'),2)} GiB).",
              f"- Pico de memoria usada por el sistema: {num(t['system_pct'])}% del GB10.",
              f"- Pico de caché ocupada: {num(t['cache'])}% de la reserva KV.",
              f"- Máximo observado de solicitudes activas: {integer(t['active'])}.",
              f"- Máximo observado en cola: {integer(t['queue'])}.",
              f"- Preempciones por memoria: {integer(t['preemptions'])}."]
    if t.get('summary', {}).get('prefix_cache_queries') is not None:
        s = t['summary']
        lines += [f"- Tokens consultados en prefix cache: {integer(s.get('prefix_cache_queries'))}.",
                  f"- Tokens recuperados de prefix cache: {integer(s.get('prefix_cache_hits'))}."]
        lines += [f"- Temperatura GPU máxima observada: {num(s.get('peak_gpu_temperature_c'))} °C.",
                  f"- Utilización GPU máxima observada: {num(s.get('peak_gpu_utilization_percent'))}%."]
    if t.get('summary', {}).get('peak_overlapping_responses') is not None:
        s = t['summary']
        lines += [f"- Máximo de respuestas solapadas desde primer token hasta final (entre las solicitudes ya terminadas): {integer(s['peak_overlapping_responses'])}.",
                  f"- Tiempo observado con alguna solicitud en cola: {num(s.get('seconds_with_queue'))} s.",
                  f"- Tiempo observado con caché al 95% o más: {num(s.get('seconds_cache_above_95_percent'))} s.",
                  f"- Contexto máximo informado por la API: {integer(s.get('max_model_len'))} tokens.", '',
                  'Enviada, primer token y final usan el mismo reloj relativo al comienzo de la prueba. '
                  'El solapamiento indica respuestas abiertas simultáneamente, no garantiza que el motor genere un token para todas en cada paso.']
    lines += ['', 'N/M significa que esa métrica no se recogió durante esta prueba.', '']
    path.write_text('\n'.join(lines).replace('N/M%', 'N/M'))


def main():
    DETAILS.mkdir(exist_ok=True)
    tests = []
    for path in DATA.rglob('*.json'):
        if path.name in ('summary.json', 'metadata.json', 'override.json', 'session.json', 'index.json'):
            continue
        try:
            test = read_test(path)
        except (ValueError, KeyError, TypeError):
            continue
        if test:
            tests.append(test)
    tests.extend(startup_tests())
    models = collections.defaultdict(list)
    for t in tests:
        models[t['model']].append(t)
        write_detail(t)
    session_file = DATA/'2026-10-14/session.json'
    session = json.loads(session_file.read_text()) if session_file.exists() else {'status': 'running'}
    lines = ['# Tests GB10', '',
             'Comparación de modelos locales en NVIDIA GB10: cuánta memoria necesitan, cuántas solicitudes pueden atender y cuánto espera cada conversación.', '',
             '**Estado:** '+('pruebas terminadas y configuración original restaurada.' if session.get('status') == 'complete' else 'pruebas en curso; los resultados se van incorporando al terminar cada ensayo.'), '',
             'Una tabla por modelo y una fila por prueba. El ID de cada fila abre los tiempos y velocidades de **cada conversación**, junto con los datos originales.', '',
             '[Cómo se hicieron las pruebas y qué límites tienen](METODOLOGIA.md).', '',
             '## Cómo leer las tablas', '',
             '- **Asignado:** presupuesto configurado con `--gpu-memory-utilization`; se refiere a toda la memoria del GB10.',
             '- **Motor / GB10:** pico medido con `nvidia-smi` del proceso `VLLM::EngineCore`, dividido entre la memoria total. Incluye sus reservas GPU; no incluye toda la RAM de la API ni del sistema.',
             '- **Sistema / GB10:** pico de `(MemTotal − MemAvailable) / MemTotal`; incluye los demás procesos y el motor.',
             '- **Concurrencia enviada / límite / activa / respuestas:** máximo de peticiones en vuelo del cliente, límite configurado en el servidor y máximo observado dentro del motor. Activa incluye lectura del prompt y generación. Respuestas es el máximo de intervalos solapados desde primer token hasta final, calculado al terminar la prueba.',
             '- **Inicio:** tiempo medio hasta el primer token. **Respuesta:** tiempo medio completo, incluida la espera. **Acumulado:** suma de los tiempos individuales; puede superar la duración real por el solapamiento.',
             '- **Duración:** tiempo de pared de la prueba, sin el arranque del modelo; las filas de arranque muestran el tiempo hasta disponibilidad o fallo. **t/s por conversación:** media de tokens de salida / tiempo completo individual, incluyendo espera. **t/s total:** toda la salida / duración de la prueba.',
             '- **Cola:** máximo observado de solicitudes esperando; una cola transitoria durante el prefill no demuestra por sí sola falta de memoria.',
             '- **Caché:** pico de uso de la reserva KV, no porcentaje de RAM del equipo; puede incluir prefijos conservados de solicitudes anteriores. **Recálculos:** preempciones registradas por vLLM.',
             '- **N/M:** no medido. No se sustituye por una estimación ni por cero.', '',
             '## Entorno', '',
             'GB10 con 121,63 GiB de memoria unificada visible. Pruebas del 14 de octubre de 2026. '
             'Imagen `nvcr.io/nvidia/vllm:26.09-py3`, vLLM `0.29.0+5013de39.dev`. Un solo modelo activo. El límite del servidor se registra en cada fila.', '',
             'Los tiempos se miden contra la API de vLLM, sin Open WebUI. Las entradas son sintéticas y no contienen datos personales. '
             'Estas pruebas miden funcionamiento y rendimiento, no calidad de las respuestas.', '']
    for model in sorted(models):
        title = model.split('/')[-1]
        lines += ['## '+title, '', f'Modelo exacto: `{model}`.', '']
        if model == DEFAULT_MODEL:
            lines += ['Pesos cargados: **19,95 GiB**, aproximadamente **16,4% del GB10**. '
                      'Ese valor no incluye caché ni buffers. Configuración original: **40%**, cuatro solicitudes y contexto máximo de 262.144 tokens. '
                      'Prefix caching activado, caché KV automática BF16 y modo Mamba `align`.', '']
        conclusions = ROOT/'conclusions'/f'{title}.md'
        if conclusions.exists():
            lines += [conclusions.read_text().strip(), '']
        lines += ['| Prueba / detalle individual | Enunciado | Asignado | Motor / GB10 | Sistema / GB10 | Tokens entrada / salida | Concurrencia enviada / límite / activa / respuestas | OK / total | Inicio medio (s) | Respuesta media (s) | Acumulado (s) | Duración prueba (s) | t/s conversación | t/s total | Pico caché | Cola máx. | Recálculos | Resultado |',
                  '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|']
        ordered = sorted(models[model], key=lambda t: (t['memory'] if t['memory'] is not None else float('inf'), t['server_limit'], t['input'], t['concurrency'], t['output'], t['id']))
        for i,t in enumerate(ordered,1):
            lines.append(f"| [P{i:02d}](details/{t['id']}.md) | {t['description']} | {num(t['memory'],0)}% "
                         f"| {num(t['engine_pct'])}% | {num(t['system_pct'])}% | {integer(t['input'])} / {integer(t['output'])} "
                         f"| {t['concurrency']} / {t['server_limit']} / {integer(t['active'])} / {integer(t.get('summary', {}).get('peak_overlapping_responses') if t.get('summary', {}).get('status') == 'complete' else None)} | {t['completed']}/{t['count']} "
                         f"| {num(t['ttft'])} | {num(t['response'])} | {num(t['sum_response'])} "
                         f"| {num(t['duration'])} | {num(t['mean_request_rate'])} | {num(t['throughput'])} "
                         f"| {num(t['cache'])}% | {integer(t['queue'])} | {integer(t['preemptions'])} | {t['status']} |")
        lines += ['']
    for matrix_file in sorted(DATA.rglob('metadata.json')):
        m=json.loads(matrix_file.read_text())
        if 'restore_status' not in m:
            continue
        lines += ['## Estado de la batería: '+matrix_file.parent.name, '',
                  'Se registra también si el modelo consigue arrancar con el contexto máximo solicitado. '
                  'Cada intento figura también como fila en la tabla del modelo. Arrancar no garantiza que varias conversaciones largas puedan ejecutarse a la vez.', '']
        for profile in m.get('profiles',[]):
            for a in profile.get('attempts',[]):
                lines.append(f"- **{profile['fraction']*100:.0f}%**, contexto máximo {integer(a['max_model_len'])}: "
                             f"{'arranque correcto' if a['ready'] else 'no arrancó'} en {num(a['startup_seconds'])} s.")
        lines += ['', 'Restauración registrada: **'+m.get('restore_status','pendiente')+'**.', '']
        if m.get('coordination_incident'):
            lines += ['**Incidencia de coordinación:** al cambiar el orden de las pruebas después del 30%, '
                      'se interrumpió una recreación de Docker y el primer intento de restauración coincidió con ella. '
                      'Se recuperó ejecutando el Compose original y restituyendo el nombre del contenedor. '
                      'Las cuatro pruebas al 30% ya habían terminado; no se ejecutó ninguna inferencia al 50% antes de repetir el 40%. '
                      'No se clasifica como fallo de capacidad del modelo.', '']
    overflow=DATA/'2026-10-14/context-40/limit-rejection.json'
    if overflow.exists():
        d=json.loads(overflow.read_text())
        lines += ['## Validación del límite de contexto', '',
                  f"Una petición de {integer(d['input_tokens'])} tokens de entrada más {d['output_requested']} de salida "
                  f"recibió **HTTP {d['http_status']}** en {num(d['elapsed_s'],3)} s: rechazo esperado al superar 262.144 tokens. "
                  '[Respuesta original](results/2026-10-14/context-40/limit-rejection.json).', '']
    lines += ['## Reproducir y añadir modelos', '',
              '- [context_probe.py](scripts/context_probe.py): mide cada solicitud, memoria y caché. Acepta `--model` y `--base-url` para probar otro modelo ya desplegado.',
              '- [short_benchmark.sh](scripts/short_benchmark.sh): primera batería con la herramienta oficial de vLLM.',
              '- [memory_matrix.py](scripts/memory_matrix.py): pruebas temporales sobre el servicio Qwen de este GB10. Recrea el contenedor, usa overrides sin editar el Compose original y restaura el comando original al terminar.',
              '- [build_report.py](scripts/build_report.py): agrupa los JSON de `results/` por identificador de modelo y genera las tablas y los detalles individuales.', '',
              '```bash',
              'python3 scripts/context_probe.py --model nvidia/Qwen3.8-27B-NVFP4 \\',
              '  --concurrency 4 --requests 4 --input-tokens 32768 --output-tokens 512 \\',
              '  --memory-fraction 0.4 --server-max-seqs 4 \\',
              '  --result /tmp/contexto-32k.json',
              '```', '',
              'Ejecuta el medidor en el GB10: la telemetría de hardware corresponde a la máquina que ejecuta el script. '
              '`--memory-fraction` y `--server-max-seqs` registran la configuración existente; no la modifican. '
              'Para añadir otro modelo, usa su identificador y sus valores reales, guarda el JSON bajo `results/` y ejecuta `build_report.py`. '
              'Una memoria no registrada aparece como N/M, no se supone que sea el 40%.', '',
              'En las primeras pruebas se guardaron menos métricas; se conservan como historial y sus celdas ausentes están marcadas N/M. '
              'Las nuevas guardan tiempos individuales y muestrean la caché cada segundo y la memoria GPU aproximadamente cada cinco segundos. '
              'Las comparaciones de memoria deben mantener modelo, entrada, salida y concurrencia iguales.', '',
              'Los ensayos largos con prefijos nuevos miden la lectura completa del historial. '
              'Continuar un historial que siga en caché puede ser mucho más rápido. '
              'No se ha validado aquí la calidad con contextos largos ni estabilidad durante días.', '',
              'Todos los resultados y registros están en [results](results).', '']
    (ROOT/'README.md').write_text('\n'.join(lines).replace('N/M%', 'N/M'))


if __name__ == '__main__':
    main()
