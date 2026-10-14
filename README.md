# Tests GB10

Pruebas de memoria, contexto y concurrencia realizadas el 14 de octubre de 2026.

**Estado:** pruebas en curso; esta tabla contiene únicamente las mediciones ya guardadas.

## Equipo y configuración

- NVIDIA GB10, 121,63 GiB de memoria unificada visible para el sistema.
- Modelo: `nvidia/Qwen3.8-27B-NVFP4`.
- Imagen: `nvcr.io/nvidia/vllm:26.09-py3`; vLLM `0.29.0+5013de39.dev`.
- Configuración original: memoria `0.40`, `--max-num-seqs 4`, contexto máximo 262.144 tokens.
- Caché de contexto original: 23,6 GiB. Modelo cargado: 19,95 GiB.
- Prefix caching activado; caché KV automática (BF16), configuración híbrida Mamba `align`.
- No hay otros modelos activos durante estas pruebas.

El porcentaje es el presupuesto de vLLM sobre la memoria total; no es un límite estricto de toda la RAM del contenedor. El contexto incluye entrada y salida. Una conversación guardada que no está generando no equivale a una solicitud activa.

## Pruebas cortas al 40%

Herramienta oficial `vllm bench serve`. Cada respuesta genera 128 tokens. Hay una petición de comprobación y una de calentamiento adicionales por ensayo, excluidas de la tabla.

| Modelo | Memoria | Entrada | Concurrencia enviada | Completadas | Inicio medio (s) | Respuesta completa media (s) | Tokens/s totales |
|---|---:|---:|---:|---:|---:|---:|---:|
| Qwen3.8-27B NVFP4 | 40% | 1,024 | 1 | [20/20](results/2026-10-14/short/c1-in1024.json) | 0.65 | 10.6 | 12.0 |
| Qwen3.8-27B NVFP4 | 40% | 1,024 | 2 | [20/20](results/2026-10-14/short/c2-in1024.json) | 1.04 | 11.6 | 22.0 |
| Qwen3.8-27B NVFP4 | 40% | 1,024 | 4 | [20/20](results/2026-10-14/short/c4-in1024.json) | 1.40 | 12.7 | 40.2 |
| Qwen3.8-27B NVFP4 | 40% | 1,024 | 8 | [20/20](results/2026-10-14/short/c8-in1024.json) | 11.22 | 22.6 | 40.9 |
| Qwen3.8-27B NVFP4 | 40% | 8,192 | 4 | [12/12](results/2026-10-14/short/c4-in8192.json) | 5.21 | 23.5 | 21.6 |

Con ocho solicitudes enviadas se observaron cuatro en ejecución y cuatro en cola. La concurrencia enviada no cambia el límite del servidor.

## Contextos largos y distintos presupuestos

Solicitudes simultáneas con prefijos sintéticos distintos, sin reutilización intencionada de contexto. Se fuerza la longitud de respuesta para que todos los ensayos tengan trabajo definido. Métricas de caché y cola muestreadas cada segundo.

**Enviada / activa máxima** distingue clientes simultáneos del máximo de solicitudes que el motor llegó a mantener en ejecución. La espera inicial incluye lectura del contexto y cola. El tiempo completo incluye esa espera.

| Modelo | Memoria | Tokens entrada / salida | Concurrencia enviada / activa máxima | Completadas | Inicio medio (s) | Completa media (s) | Pico caché | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Qwen3.8-27B NVFP4 | 40% | 32,768 / 512 | 4 / 4 | 4/4 | 40.8 | 122.5 | 84.3% | [OK](results/2026-10-14/context-40/c4-in32768-out512.json) |
| Qwen3.8-27B NVFP4 | 40% | 65,536 / 512 | 4 / 2 | 4/4 | 123.1 | 207.2 | 85.6% | [OK; con cola](results/2026-10-14/context-40/c4-in65536-out512.json) |

## Cómo interpretar los resultados

- **OK** significa que terminó la carga sintética y devolvió los tokens pedidos; no evalúa la calidad de las respuestas.
- **Con cola** significa que las solicitudes terminaron, pero el motor no llegó a ejecutar todas simultáneamente.
- Los tokens/s de las pruebas cortas son el rendimiento total, no la velocidad de cada usuario.
- El pico de caché es uso de la reserva de vLLM, no porcentaje de la memoria física del equipo.
- La cifra de capacidad de tokens que imprime vLLM al arrancar es una estimación. En este modelo híbrido hay que verificar el comportamiento real del gestor de caché.
- Son ensayos puntuales, no una garantía de disponibilidad ni una prueba de estabilidad durante días. Prompts reales, herramientas, imágenes, más salida o un segundo modelo pueden cambiar los resultados.

## Repetir las pruebas

Las pruebas cortas usan `vllm bench serve` dentro del contenedor. Las largas usan [context_probe.py](scripts/context_probe.py), que solo envía peticiones y lee métricas.

```bash
python3 scripts/context_probe.py --concurrency 4 --input-tokens 32768 \
  --output-tokens 512 --result /tmp/contexto-32k.json
```

[memory_matrix.py](scripts/memory_matrix.py) cambia temporalmente el servicio mediante un archivo Compose adicional, sin editar el Compose original. Recrea el contenedor y restaura el comando original al terminar. **Este script interrumpe el servicio durante los cambios; no debe ejecutarse a la vez que otras pruebas.**

Resultados originales y registros: [results/2026-10-14](results/2026-10-14). Los datos de prueba son sintéticos; no contienen conversaciones personales ni claves.
