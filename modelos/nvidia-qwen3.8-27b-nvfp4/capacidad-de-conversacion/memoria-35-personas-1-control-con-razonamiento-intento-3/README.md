# 1 persona · 35% de memoria

[Volver a la capacidad por memoria](../README.md)

**No cumple la referencia de tiempos del control.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **predeterminado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 4.096 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **5/5 previstas**. Duración: **5,7 min**, incluidas las pausas. Este control no recorre todo el contexto.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado por turno

| Turno | Sin error | Visibles y naturales | Espera visible p95 | Respuesta completa p95 | Velocidad p05 |
|---:|---:|---:|---:|---:|---:|
| 1 | 1/1 | 1/1 | 47,8 s | 55,6 s | 12,00 tokens/s |
| 2 | 1/1 | 1/1 | 45,3 s | 51,7 s | 11,99 tokens/s |
| 3 | 1/1 | 1/1 | 29,4 s | 36,8 s | 12,00 tokens/s |
| 4 | 1/1 | 1/1 | 34,8 s | 42,0 s | 11,98 tokens/s |
| 5 | 1/1 | 1/1 | 28,1 s | 35,6 s | 11,97 tokens/s |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 5 | 10.885 | 4,152% | 251.259 |

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 35% |
| Pico de memoria del motor / GB10 | 31,7% |
| Pico de memoria total del sistema / GB10 | 39,9% |
| Pico de caché | 7,5% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 37,1 s |
| Espera media al primer token, incluido razonamiento | 1,4 s |
| Tiempo medio de petición completa | 44,4 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 7,54 tokens/s |
| Suma de tiempos individuales de petición | 221,8 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 5/5 | 37,1 s | 44,4 s | 341,9 s | 7,55 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 | 607 | 47,8 s | 55,6 s | 12,00 | Natural |
| 1 | 2 | 8.828 | 615 | 45,3 s | 51,7 s | 11,99 | Natural |
| 1 | 3 | 9.469 | 437 | 29,4 s | 36,8 s | 12,00 | Natural |
| 1 | 4 | 9.937 | 501 | 34,8 s | 42,0 s | 11,98 | Natural |
| 1 | 5 | 10.465 | 420 | 28,1 s | 35,6 s | 11,97 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
