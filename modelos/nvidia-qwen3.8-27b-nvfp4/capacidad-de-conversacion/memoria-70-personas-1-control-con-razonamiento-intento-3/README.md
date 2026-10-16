# 1 persona · 70% de memoria

[Volver a la capacidad por memoria](../README.md)

**No cumple la referencia completa.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **predeterminado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 4.096 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **5/5 previstas**. Duración: **6,2 min**, incluidas las pausas. Este control no recorre todo el contexto.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado por turno

| Turno | Sin error | Visibles y naturales | Espera visible p95 | Respuesta completa p95 | Velocidad p05 |
|---:|---:|---:|---:|---:|---:|
| 1 | 1/1 | 1/1 | 45,4 s | 54,2 s | 12,00 tokens/s |
| 2 | 1/1 | 1/1 | 40,4 s | 49,8 s | 11,98 tokens/s |
| 3 | 1/1 | 1/1 | 38,9 s | 49,2 s | 11,96 tokens/s |
| 4 | 1/1 | 1/1 | 42,5 s | 51,6 s | 11,94 tokens/s |
| 5 | 1/1 | 1/1 | 37,6 s | 47,2 s | 11,92 tokens/s |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 5 | 11.239 | 4,287% | 250.905 |

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 70% |
| Pico de memoria del motor / GB10 | 66,8% |
| Pico de memoria total del sistema / GB10 | 75,6% |
| Pico de caché | 2,2% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto del modelo | 1,4 s |
| Tiempo medio de petición completa | 50,4 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 7,88 tokens/s |
| Suma de tiempos individuales de petición | 252,0 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 5/5 | 41,0 s | 50,4 s | 372,0 s | 7,89 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 | 591 | 45,4 s | 54,2 s | 12,00 | Natural |
| 1 | 2 | 8.812 | 591 | 40,4 s | 49,8 s | 11,98 | Natural |
| 1 | 3 | 9.429 | 583 | 38,9 s | 49,2 s | 11,96 | Natural |
| 1 | 4 | 10.043 | 613 | 42,5 s | 51,6 s | 11,94 | Natural |
| 1 | 5 | 10.683 | 556 | 37,6 s | 47,2 s | 11,92 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
