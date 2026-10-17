# 1 persona · 85% de memoria

[Volver a la capacidad por memoria](../README.md)

**No cumple la referencia de tiempos del control.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **predeterminado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 4.096 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **5/5 previstas**. Duración: **5,8 min**, incluidas las pausas. Este control no recorre todo el contexto.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado por turno

| Turno | Sin error | Visibles y naturales | Espera visible p95 | Respuesta completa p95 | Velocidad p05 |
|---:|---:|---:|---:|---:|---:|
| 1 | 1/1 | 1/1 | 42,2 s | 49,8 s | 11,94 tokens/s |
| 2 | 1/1 | 1/1 | 25,5 s | 32,4 s | 11,93 tokens/s |
| 3 | 1/1 | 1/1 | 50,7 s | 60,7 s | 11,91 tokens/s |
| 4 | 1/1 | 1/1 | 34,3 s | 43,9 s | 11,90 tokens/s |
| 5 | 1/1 | 1/1 | 32,3 s | 41,5 s | 11,86 tokens/s |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 5 | 10.942 | 4,174% | 251.202 |

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 85% |
| Pico de memoria del motor / GB10 | 81,8% |
| Pico de memoria total del sistema / GB10 | 89,7% |
| Pico de caché | 1,7% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 37,0 s |
| Espera media al primer token, incluido razonamiento | 1,4 s |
| Tiempo medio de petición completa | 45,6 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 7,56 tokens/s |
| Suma de tiempos individuales de petición | 228,2 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 5/5 | 37,0 s | 45,6 s | 348,3 s | 7,57 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 | 534 | 42,2 s | 49,8 s | 11,94 | Natural |
| 1 | 2 | 8.755 | 381 | 25,5 s | 32,4 s | 11,93 | Natural |
| 1 | 3 | 9.162 | 720 | 50,7 s | 60,7 s | 11,91 | Natural |
| 1 | 4 | 9.913 | 516 | 34,3 s | 43,9 s | 11,90 | Natural |
| 1 | 5 | 10.456 | 486 | 32,3 s | 41,5 s | 11,86 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
