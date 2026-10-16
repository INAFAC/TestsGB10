# 1 persona · 40% de memoria

[Volver a la capacidad por memoria](../README.md)

**No cumple la referencia de tiempos del control.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **predeterminado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 4.096 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **5/5 previstas**. Duración: **6,7 min**, incluidas las pausas. Este control no recorre todo el contexto.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado por turno

| Turno | Sin error | Visibles y naturales | Espera visible p95 | Respuesta completa p95 | Velocidad p05 |
|---:|---:|---:|---:|---:|---:|
| 1 | 1/1 | 1/1 | 52,3 s | 61,4 s | 11,96 tokens/s |
| 2 | 1/1 | 1/1 | 38,9 s | 48,2 s | 11,94 tokens/s |
| 3 | 1/1 | 1/1 | 34,2 s | 41,4 s | 11,92 tokens/s |
| 4 | 1/1 | 1/1 | 74,3 s | 83,3 s | 11,89 tokens/s |
| 5 | 1/1 | 1/1 | 36,8 s | 46,4 s | 11,86 tokens/s |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 5 | 11.587 | 4,420% | 250.557 |

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 40% |
| Pico de memoria del motor / GB10 | 36,7% |
| Pico de memoria total del sistema / GB10 | 45,1% |
| Pico de caché | 5,5% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 47,3 s |
| Espera media al primer token, incluido razonamiento | 1,1 s |
| Tiempo medio de petición completa | 56,1 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 8,18 tokens/s |
| Suma de tiempos individuales de petición | 280,7 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 5/5 | 47,3 s | 56,1 s | 400,8 s | 8,19 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 | 695 | 52,3 s | 61,4 s | 11,96 | Natural |
| 1 | 2 | 8.916 | 570 | 38,9 s | 48,2 s | 11,94 | Natural |
| 1 | 3 | 9.512 | 488 | 34,2 s | 41,4 s | 11,92 | Natural |
| 1 | 4 | 10.031 | 988 | 74,3 s | 83,3 s | 11,89 | Natural |
| 1 | 5 | 11.046 | 541 | 36,8 s | 46,4 s | 11,86 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
