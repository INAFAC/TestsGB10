# 1 persona · 50% de memoria

[Volver a la capacidad por memoria](../README.md)

**No cumple la referencia de tiempos del control.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **predeterminado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 4.096 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **5/5 previstas**. Duración: **6,6 min**, incluidas las pausas. Este control no recorre todo el contexto.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado por turno

| Turno | Sin error | Visibles y naturales | Espera visible p95 | Respuesta completa p95 | Velocidad p05 |
|---:|---:|---:|---:|---:|---:|
| 1 | 1/1 | 1/1 | 54,0 s | 63,1 s | 11,99 tokens/s |
| 2 | 1/1 | 1/1 | 46,0 s | 55,0 s | 11,97 tokens/s |
| 3 | 1/1 | 1/1 | 45,2 s | 53,7 s | 11,95 tokens/s |
| 4 | 1/1 | 1/1 | 46,2 s | 55,8 s | 11,93 tokens/s |
| 5 | 1/1 | 1/1 | 40,7 s | 50,0 s | 11,90 tokens/s |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 5 | 11.538 | 4,401% | 250.606 |

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 50% |
| Pico de memoria del motor / GB10 | 46,6% |
| Pico de memoria total del sistema / GB10 | 55,3% |
| Pico de caché | 3,6% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 46,4 s |
| Espera media al primer token, incluido razonamiento | 1,5 s |
| Tiempo medio de petición completa | 55,5 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 8,13 tokens/s |
| Suma de tiempos individuales de petición | 277,5 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 5/5 | 46,4 s | 55,5 s | 397,6 s | 8,13 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 | 694 | 54,0 s | 63,1 s | 11,99 | Natural |
| 1 | 2 | 8.915 | 652 | 46,0 s | 55,0 s | 11,97 | Natural |
| 1 | 3 | 9.593 | 636 | 45,2 s | 53,7 s | 11,95 | Natural |
| 1 | 4 | 10.260 | 660 | 46,2 s | 55,8 s | 11,93 | Natural |
| 1 | 5 | 10.947 | 591 | 40,7 s | 50,0 s | 11,90 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
