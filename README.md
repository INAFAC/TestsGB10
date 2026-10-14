# Tests GB10

Comparación de modelos locales en NVIDIA GB10: cuánta memoria necesitan, cuántas solicitudes pueden atender y cuánto espera cada conversación.

**Estado:** pruebas en curso; los resultados se van incorporando al terminar cada ensayo.

Una tabla por modelo y una fila por prueba. El ID de cada fila abre los tiempos y velocidades de **cada conversación**, junto con los datos originales.

## Cómo leer las tablas

- **Asignado:** presupuesto configurado con `--gpu-memory-utilization`; se refiere a toda la memoria del GB10.
- **Motor / GB10:** pico medido con `nvidia-smi` del proceso `VLLM::EngineCore`, dividido entre la memoria total. Incluye sus reservas GPU; no incluye toda la RAM de la API ni del sistema.
- **Sistema / GB10:** pico de `(MemTotal − MemAvailable) / MemTotal`; incluye los demás procesos y el motor.
- **Concurrencia enviada / activa:** máximo de peticiones en vuelo del cliente y máximo observado dentro del motor. Activa incluye lectura del prompt y generación.
- **Inicio:** tiempo medio hasta el primer token. **Respuesta:** tiempo medio completo, incluida la espera. **Acumulado:** suma de los tiempos individuales; puede superar la duración real por el solapamiento.
- **Duración:** tiempo de pared de la prueba, sin el arranque del modelo. **t/s por conversación:** media de tokens de salida / tiempo completo individual, incluyendo espera. **t/s total:** toda la salida / duración de la prueba.
- **Cola:** máximo observado de solicitudes esperando; una cola transitoria durante el prefill no demuestra por sí sola falta de memoria.
- **Caché:** pico de uso de la reserva KV, no porcentaje de RAM del equipo. **Recálculos:** preempciones registradas por vLLM.
- **N/M:** no medido. No se sustituye por una estimación ni por cero.

## Entorno

GB10 con 121,63 GiB de memoria unificada visible. Pruebas del 14 de octubre de 2026. Imagen `nvcr.io/nvidia/vllm:26.09-py3`, vLLM `0.29.0+5013de39.dev`. Un solo modelo activo, con límite del servidor de cuatro solicitudes.

Los tiempos se miden contra la API de vLLM, sin Open WebUI. Las entradas son sintéticas y no contienen datos personales. Estas pruebas miden funcionamiento y rendimiento, no calidad de las respuestas.

## Qwen3.8-27B-NVFP4

Modelo exacto: `nvidia/Qwen3.8-27B-NVFP4`.

Pesos cargados: **19,95 GiB**, aproximadamente **16,4% del GB10**. Ese valor no incluye caché ni buffers. Configuración original: **40%**, cuatro solicitudes y contexto máximo de 262.144 tokens. Prefix caching activado, caché KV automática BF16 y modo Mamba `align`.

| Prueba / detalle individual | Enunciado | Asignado | Motor / GB10 | Sistema / GB10 | Tokens entrada / salida | Concurrencia enviada / activa | OK / total | Inicio medio (s) | Respuesta media (s) | Acumulado (s) | Duración prueba (s) | t/s conversación | t/s total | Pico caché | Cola máx. | Recálculos | Resultado |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [P01](details/2026-10-14-short-c1-in1024.md) | Carga corta inicial (detalle individual no guardado) | 40% | N/M% | N/M% | 1.024 / 128 | 1 / — | 20/20 | 0,7 | 10,6 | 212,5 | 212,5 | N/M | 12,0 | N/M% | — | — | OK |
| [P02](details/2026-10-14-short-c2-in1024.md) | Carga corta inicial (detalle individual no guardado) | 40% | N/M% | N/M% | 1.024 / 128 | 2 / — | 20/20 | 1,0 | 11,6 | 232,8 | 116,5 | N/M | 22,0 | N/M% | — | — | OK |
| [P03](details/2026-10-14-short-c4-in1024.md) | Carga corta inicial (detalle individual no guardado) | 40% | N/M% | N/M% | 1.024 / 128 | 4 / — | 20/20 | 1,4 | 12,7 | 254,1 | 63,6 | N/M | 40,2 | N/M% | — | — | OK |
| [P04](details/2026-10-14-short-c8-in1024.md) | Carga corta inicial (detalle individual no guardado) | 40% | N/M% | N/M% | 1.024 / 128 | 8 / — | 20/20 | 11,2 | 22,6 | 451,3 | 62,6 | N/M | 40,9 | N/M% | — | — | OK |
| [P05](details/2026-10-14-short-c4-in8192.md) | Carga corta inicial (detalle individual no guardado) | 40% | N/M% | N/M% | 8.192 / 128 | 4 / — | 12/12 | 5,2 | 23,5 | 282,3 | 71,2 | N/M | 21,6 | N/M% | — | — | OK |
| [P06](details/2026-10-14-context-40-c4-in32768-out512.md) | Historial nuevo; prefijos independientes | 40% | N/M% | N/M% | 32.768 / 512 | 4 / 4 | 4/4 | 40,8 | 122,5 | 490,0 | 125,5 | 4,2 | 16,3 | 84,3% | 3 | 0 | OK |
| [P07](details/2026-10-14-context-40-c4-in65536-out512.md) | Historial nuevo; prefijos independientes | 40% | N/M% | N/M% | 65.536 / 512 | 4 / 2 | 4/4 | 123,1 | 207,2 | 828,7 | 267,3 | 2,7 | 7,7 | 85,6% | 3 | 0 | OK |
| [P08](details/2026-10-14-context-40-c4-in131072-out256.md) | Historial nuevo; prefijos independientes | 40% | N/M% | N/M% | 131.072 / 256 | 4 / 1 | 4/4 | 286,4 | 315,5 | 1261,8 | 504,5 | 1,1 | 2,0 | 86,0% | 3 | 0 | OK |

## Validación del límite de contexto

Una petición de 262.145 tokens de entrada más 1 de salida recibió **HTTP 400** en 0,046 s: rechazo esperado al superar 262.144 tokens. [Respuesta original](results/2026-10-14/context-40/limit-rejection.json).

## Reproducir y añadir modelos

- [context_probe.py](scripts/context_probe.py): mide cada solicitud, memoria y caché. Acepta `--model` y `--base-url` para probar otro modelo ya desplegado.
- [short_benchmark.sh](scripts/short_benchmark.sh): primera batería con la herramienta oficial de vLLM.
- [memory_matrix.py](scripts/memory_matrix.py): pruebas temporales sobre el servicio Qwen de este GB10. Recrea el contenedor, usa overrides sin editar el Compose original y restaura el comando original al terminar.
- [build_report.py](scripts/build_report.py): agrupa los JSON de `results/` por identificador de modelo y genera las tablas y los detalles individuales.

```bash
python3 scripts/context_probe.py --model nvidia/Qwen3.8-27B-NVFP4 \
  --concurrency 4 --requests 4 --input-tokens 32768 --output-tokens 512 \
  --result /tmp/contexto-32k.json
```

En las primeras pruebas se guardaron menos métricas; se conservan como historial y sus celdas ausentes están marcadas N/M. Las nuevas guardan tiempos individuales y muestrean la caché cada segundo y la memoria GPU aproximadamente cada cinco segundos. Las comparaciones de memoria deben mantener modelo, entrada, salida y concurrencia iguales.

Los ensayos largos con prefijos nuevos miden la lectura completa del historial. Continuar un historial que siga en caché puede ser mucho más rápido. No se ha validado aquí la calidad con contextos largos ni estabilidad durante días.

Todos los resultados y registros están en [results](results).
