#!/usr/bin/env python3
"""Generate the human-readable report from recorded measurements."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT/'results/2026-10-14'


def fmt(value, digits=1):
    return '—' if value is None else f'{value:.{digits}f}'


def context_row(file, memory):
    data = json.loads(file.read_text())
    s = data['summary']
    completed = s.get('completed', 0)
    target = s['concurrency']
    state = 'OK' if completed == target and not s.get('failed') else 'Incompleta / revisar'
    if s.get('preemptions', 0):
        state += f"; {int(s['preemptions'])} recálculos"
    if completed == target and s.get('peak_running', target) < target:
        state += '; con cola'
    link = file.relative_to(ROOT).as_posix()
    return (f"| Qwen3.8-27B NVFP4 | {memory}% | {s['input_tokens']:,} / {s['output_tokens']} "
            f"| {target} / {fmt(s.get('peak_running'), 0)} | {completed}/{target} "
            f"| {fmt(s.get('mean_ttft_s'))} | {fmt(s.get('mean_total_s'))} "
            f"| {fmt(s['peak_kv_fraction']*100 if s.get('peak_kv_fraction') is not None else None)}% "
            f"| [{state}]({link}) |")


def main():
    matrix_path = DATA/'memory/metadata.json'
    matrix = json.loads(matrix_path.read_text()) if matrix_path.exists() else {}
    restored = matrix.get('restore_status') == 'healthy'
    lines = [
        '# Tests GB10', '',
        'Pruebas de memoria, contexto y concurrencia realizadas el 14 de octubre de 2026.', '',
        '**Estado:** '+('pruebas terminadas; configuración original del 40% restaurada y servidor sano.'
                       if restored else 'pruebas en curso; esta tabla contiene únicamente las mediciones ya guardadas.'), '',
        '## Equipo y configuración', '',
        '- NVIDIA GB10, 121,63 GiB de memoria unificada visible para el sistema.',
        '- Modelo: `nvidia/Qwen3.8-27B-NVFP4`.',
        '- Imagen: `nvcr.io/nvidia/vllm:26.09-py3`; vLLM `0.29.0+5013de39.dev`.',
        '- Configuración original: memoria `0.40`, `--max-num-seqs 4`, contexto máximo 262.144 tokens.',
        '- Caché de contexto original: 23,6 GiB. Modelo cargado: 19,95 GiB.',
        '- Prefix caching activado; caché KV automática (BF16), configuración híbrida Mamba `align`.',
        '- No hay otros modelos activos durante estas pruebas.', '',
        'El porcentaje es el presupuesto de vLLM sobre la memoria total; no es un límite estricto de toda la RAM del contenedor. '
        'El contexto incluye entrada y salida. Una conversación guardada que no está generando no equivale a una solicitud activa.', '',
        '## Pruebas cortas al 40%', '',
        'Herramienta oficial `vllm bench serve`. Cada respuesta genera 128 tokens. '
        'Hay una petición de comprobación y una de calentamiento adicionales por ensayo, excluidas de la tabla.', '',
        '| Modelo | Memoria | Entrada | Concurrencia enviada | Completadas | Inicio medio (s) | Respuesta completa media (s) | Tokens/s totales |',
        '|---|---:|---:|---:|---:|---:|---:|---:|',
    ]
    files = sorted((DATA/'short').glob('*.json'),
                   key=lambda f: (json.loads(f.read_text()).get('total_input_tokens', 0)//max(1,json.loads(f.read_text()).get('num_prompts',1)),
                                  json.loads(f.read_text()).get('max_concurrency',0)))
    for file in files:
        s = json.loads(file.read_text())
        n = s['num_prompts']
        link = file.relative_to(ROOT).as_posix()
        lines.append(f"| Qwen3.8-27B NVFP4 | 40% | {s['total_input_tokens']//n:,} | {s['max_concurrency']} "
                     f"| [{s['completed']}/{n}]({link}) | {s['mean_ttft_ms']/1000:.2f} "
                     f"| {s['mean_e2el_ms']/1000:.1f} | {s['output_throughput']:.1f} |")
    lines += ['', 'Con ocho solicitudes enviadas se observaron cuatro en ejecución y cuatro en cola. '
              'La concurrencia enviada no cambia el límite del servidor.', '',
              '## Contextos largos y distintos presupuestos', '',
              'Solicitudes simultáneas con prefijos sintéticos distintos, sin reutilización intencionada de contexto. '
              'Se fuerza la longitud de respuesta para que todos los ensayos tengan trabajo definido. '
              'Métricas de caché y cola muestreadas cada segundo.', '',
              '**Enviada / activa máxima** distingue clientes simultáneos del máximo de solicitudes que el motor llegó a mantener en ejecución. '
              'La espera inicial incluye lectura del contexto y cola. El tiempo completo incluye esa espera.', '',
              '| Modelo | Memoria | Tokens entrada / salida | Concurrencia enviada / activa máxima | Completadas | Inicio medio (s) | Completa media (s) | Pico caché | Resultado |',
              '|---|---:|---:|---:|---:|---:|---:|---:|---|']
    for file in sorted((DATA/'context-40').glob('c*.json'),
                       key=lambda f: json.loads(f.read_text())['summary']['input_tokens']):
        lines.append(context_row(file, 40))
    for directory in sorted((DATA/'memory').glob('memory-*')):
        memory = int(directory.name.split('-')[1])
        for file in sorted(directory.glob('c*.json'),
                           key=lambda f: json.loads(f.read_text())['summary']['input_tokens']):
            lines.append(context_row(file, memory))
    if matrix.get('profiles'):
        lines += ['', '### Arranques y capacidad reservada', '',
                  '| Memoria | Contexto máximo intentado | Arranque | Caché KV del perfil operativo |',
                  '|---:|---:|---|---:|']
        for p in matrix['profiles']:
            for attempt in p['attempts']:
                ok = attempt['ready']
                lines.append(f"| {p['fraction']*100:.0f}% | {attempt['max_model_len']:,} "
                             f"| {'OK' if ok else 'No arrancó'} | {fmt(p.get('kv_gib'))+' GiB' if ok else '—'} |")
    lines += ['', '## Cómo interpretar los resultados', '',
              '- **OK** significa que terminó la carga sintética y devolvió los tokens pedidos; no evalúa la calidad de las respuestas.',
              '- **Con cola** significa que las solicitudes terminaron, pero el motor no llegó a ejecutar todas simultáneamente.',
              '- Los tokens/s de las pruebas cortas son el rendimiento total, no la velocidad de cada usuario.',
              '- El pico de caché es uso de la reserva de vLLM, no porcentaje de la memoria física del equipo.',
              '- La cifra de capacidad de tokens que imprime vLLM al arrancar es una estimación. '
              'En este modelo híbrido hay que verificar el comportamiento real del gestor de caché.',
              '- Son ensayos puntuales, no una garantía de disponibilidad ni una prueba de estabilidad durante días. '
              'Prompts reales, herramientas, imágenes, más salida o un segundo modelo pueden cambiar los resultados.', '',
              '## Repetir las pruebas', '',
              'Las pruebas cortas usan `vllm bench serve` dentro del contenedor. '
              'Las largas usan [context_probe.py](scripts/context_probe.py), que solo envía peticiones y lee métricas.', '',
              '```bash',
              'python3 scripts/context_probe.py --concurrency 4 --input-tokens 32768 \\',
              '  --output-tokens 512 --result /tmp/contexto-32k.json',
              '```', '',
              '[memory_matrix.py](scripts/memory_matrix.py) cambia temporalmente el servicio mediante un archivo Compose adicional, '
              'sin editar el Compose original. Recrea el contenedor y restaura el comando original al terminar. '
              '**Este script interrumpe el servicio durante los cambios; no debe ejecutarse a la vez que otras pruebas.**', '',
              'Resultados originales y registros: [results/2026-10-14](results/2026-10-14). '
              'Los datos de prueba son sintéticos; no contienen conversaciones personales ni claves.', '']
    (ROOT/'README.md').write_text('\n'.join(lines))


if __name__ == '__main__':
    main()
