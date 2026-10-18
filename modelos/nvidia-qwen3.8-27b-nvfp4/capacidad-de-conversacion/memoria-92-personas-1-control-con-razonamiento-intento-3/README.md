# 1 persona · 92% de memoria

[Volver a la capacidad por memoria](../README.md)

**No cumple la referencia de tiempos del control.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **predeterminado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 4.096 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **5/5 previstas**. Duración: **6,4 min**, incluidas las pausas. Este control no recorre todo el contexto.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado por turno

| Turno | Sin error | Visibles y naturales | Espera visible p95 | Respuesta completa p95 | Velocidad p05 |
|---:|---:|---:|---:|---:|---:|
| 1 | 1/1 | 1/1 | 73,6 s | 80,7 s | 11,94 tokens/s |
| 2 | 1/1 | 1/1 | 33,5 s | 40,8 s | 11,91 tokens/s |
| 3 | 1/1 | 1/1 | 37,1 s | 45,9 s | 11,90 tokens/s |
| 4 | 1/1 | 1/1 | 41,2 s | 49,2 s | 11,88 tokens/s |
| 5 | 1/1 | 1/1 | 35,6 s | 44,9 s | 11,86 tokens/s |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 5 | 11.336 | 4,324% | 250.808 |

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 92% |
| Pico de memoria del motor / GB10 | 88,8% |
| Pico de memoria total del sistema / GB10 | 96,0% |
| Pico de caché | 1,5% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 44,2 s |
| Espera media al primer token, incluido razonamiento | 1,4 s |
| Tiempo medio de petición completa | 52,3 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 7,94 tokens/s |
| Suma de tiempos individuales de petición | 261,4 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 5/5 | 44,2 s | 52,3 s | 381,5 s | 7,94 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 | 904 | 73,6 s | 80,7 s | 11,94 | Natural |
| 1 | 2 | 9.125 | 479 | 33,5 s | 40,8 s | 11,91 | Natural |
| 1 | 3 | 9.630 | 540 | 37,1 s | 45,9 s | 11,90 | Natural |
| 1 | 4 | 10.201 | 579 | 41,2 s | 49,2 s | 11,88 | Natural |
| 1 | 5 | 10.807 | 529 | 35,6 s | 44,9 s | 11,86 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
