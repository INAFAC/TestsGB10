# 20 usuarios · 85% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **3.312,5 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 281,6 s | 793,4 s | 844,4 s | 1.602,5 s | 0,60 tokens/s | No cumple |
| 2 | 20/20 | 241,2 s | 330,9 s | 331,5 s | 1.267,7 s | 0,54 tokens/s | No cumple |
| 3 | 20/20 | 280,0 s | 482,6 s | 487,5 s | 1.243,8 s | 0,53 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 316,7 s |
| Tiempo medio de respuesta completa | 1.058,2 s |
| Presupuesto configurado | 85% |
| Pico del motor / GB10 | 81,6% |
| Pico del sistema / GB10 | 88,7% |
| Menor memoria disponible | 13,70 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 16 / 16 |
| Máximo en cola | 19 |
| Recálculos | 9 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 9,27 |
| Suma de tiempos individuales | 63.492,2 s |
| Tiempo total de la prueba, incluyendo pausas | 3.312,5 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 204,7 s | 1.022,7 s | 3.128,1 s | 0,49 |
| 2 | 3/3 | 382,0 s | 1.080,8 s | 3.302,3 s | 0,47 |
| 3 | 3/3 | 322,7 s | 1.072,0 s | 3.276,0 s | 0,47 |
| 4 | 3/3 | 365,9 s | 1.079,7 s | 3.299,2 s | 0,47 |
| 5 | 3/3 | 358,5 s | 1.074,9 s | 3.284,7 s | 0,47 |
| 6 | 3/3 | 333,4 s | 1.077,5 s | 3.292,4 s | 0,47 |
| 7 | 3/3 | 336,7 s | 1.073,5 s | 3.280,4 s | 0,47 |
| 8 | 3/3 | 226,9 s | 1.056,5 s | 3.229,4 s | 0,48 |
| 9 | 3/3 | 349,3 s | 1.078,6 s | 3.295,9 s | 0,47 |
| 10 | 3/3 | 309,7 s | 1.070,4 s | 3.271,3 s | 0,47 |
| 11 | 3/3 | 186,8 s | 986,8 s | 3.020,3 s | 0,51 |
| 12 | 3/3 | 464,7 s | 1.084,0 s | 3.311,9 s | 0,46 |
| 13 | 3/3 | 215,1 s | 1.040,7 s | 3.182,2 s | 0,48 |
| 14 | 3/3 | 297,4 s | 1.068,7 s | 3.266,2 s | 0,47 |
| 15 | 3/3 | 318,5 s | 1.076,3 s | 3.288,8 s | 0,47 |
| 16 | 3/3 | 411,4 s | 1.081,7 s | 3.305,1 s | 0,46 |
| 17 | 3/3 | 429,5 s | 1.082,5 s | 3.307,6 s | 0,46 |
| 18 | 3/3 | 447,5 s | 1.083,3 s | 3.309,9 s | 0,46 |
| 19 | 3/3 | 178,0 s | 968,8 s | 2.966,5 s | 0,52 |
| 20 | 3/3 | 195,6 s | 1.004,7 s | 3.074,1 s | 0,50 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 512 | 96,0 s | 789,2 s | 0,74 | Completa |
| 1 | 2 | 33.536 + 512 | 234,1 s | 1.035,2 s | 0,64 | Completa |
| 1 | 3 | 34.304 + 512 | 283,9 s | 1.243,6 s | 0,53 | Completa |
| 2 | 1 | 32.768 + 512 | 593,4 s | 1.443,7 s | 0,60 | Completa |
| 2 | 2 | 33.536 + 512 | 286,1 s | 1.228,0 s | 0,54 | Completa |
| 2 | 3 | 34.304 + 512 | 266,5 s | 570,6 s | 1,68 | Completa |
| 3 | 1 | 32.768 + 512 | 244,7 s | 1.044,1 s | 0,64 | Completa |
| 3 | 2 | 33.536 + 512 | 240,9 s | 1.033,8 s | 0,64 | Completa |
| 3 | 3 | 34.304 + 512 | 482,6 s | 1.138,1 s | 0,78 | Completa |
| 4 | 1 | 32.768 + 512 | 502,6 s | 1.349,3 s | 0,60 | Completa |
| 4 | 2 | 33.536 + 512 | 330,9 s | 1.270,8 s | 0,54 | Completa |
| 4 | 3 | 34.304 + 512 | 264,2 s | 619,0 s | 1,44 | Completa |
| 5 | 1 | 32.768 + 512 | 320,9 s | 1.145,8 s | 0,62 | Completa |
| 5 | 2 | 33.536 + 512 | 282,4 s | 1.050,4 s | 0,67 | Completa |
| 5 | 3 | 34.304 + 512 | 472,3 s | 1.028,4 s | 0,92 | Completa |
| 6 | 1 | 32.768 + 512 | 406,6 s | 1.247,5 s | 0,61 | Completa |
| 6 | 2 | 33.536 + 512 | 331,5 s | 1.267,0 s | 0,55 | Completa |
| 6 | 3 | 34.304 + 512 | 262,0 s | 717,9 s | 1,12 | Completa |
| 7 | 1 | 32.768 + 512 | 281,6 s | 1.094,8 s | 0,63 | Completa |
| 7 | 2 | 33.536 + 512 | 241,2 s | 1.032,2 s | 0,65 | Completa |
| 7 | 3 | 34.304 + 512 | 487,5 s | 1.093,4 s | 0,84 | Completa |
| 8 | 1 | 32.768 + 512 | 149,6 s | 891,1 s | 0,69 | Completa |
| 8 | 2 | 33.536 + 512 | 236,4 s | 1.034,4 s | 0,64 | Completa |
| 8 | 3 | 34.304 + 512 | 294,6 s | 1.243,8 s | 0,54 | Completa |
| 9 | 1 | 32.768 + 512 | 453,5 s | 1.298,4 s | 0,60 | Completa |
| 9 | 2 | 33.536 + 512 | 330,1 s | 1.267,7 s | 0,54 | Completa |
| 9 | 3 | 34.304 + 512 | 264,4 s | 669,8 s | 1,26 | Completa |
| 10 | 1 | 32.768 + 512 | 210,4 s | 993,1 s | 0,65 | Completa |
| 10 | 2 | 33.536 + 512 | 238,6 s | 1.033,3 s | 0,64 | Completa |
| 10 | 3 | 34.304 + 512 | 480,1 s | 1.184,9 s | 0,72 | Completa |
| 11 | 1 | 32.768 + 512 | 47,1 s | 687,6 s | 0,80 | Completa |
| 11 | 2 | 33.536 + 512 | 231,4 s | 1.035,7 s | 0,64 | Completa |
| 11 | 3 | 34.304 + 512 | 282,0 s | 1.237,0 s | 0,54 | Completa |
| 12 | 1 | 32.768 + 512 | 844,4 s | 1.652,0 s | 0,63 | Completa |
| 12 | 2 | 33.536 + 512 | 280,0 s | 1.230,6 s | 0,54 | Completa |
| 12 | 3 | 34.304 + 512 | 269,6 s | 369,3 s | 5,12 | Completa |
| 13 | 1 | 32.768 + 512 | 122,1 s | 840,2 s | 0,71 | Completa |
| 13 | 2 | 33.536 + 512 | 236,3 s | 1.035,9 s | 0,64 | Completa |
| 13 | 3 | 34.304 + 512 | 287,0 s | 1.246,1 s | 0,53 | Completa |
| 14 | 1 | 32.768 + 512 | 178,9 s | 942,3 s | 0,67 | Completa |
| 14 | 2 | 33.536 + 512 | 238,4 s | 1.035,0 s | 0,64 | Completa |
| 14 | 3 | 34.304 + 512 | 475,0 s | 1.229,0 s | 0,68 | Completa |
| 15 | 1 | 32.768 + 512 | 362,4 s | 1.196,6 s | 0,61 | Completa |
| 15 | 2 | 33.536 + 512 | 330,8 s | 1.263,8 s | 0,55 | Completa |
| 15 | 3 | 34.304 + 512 | 262,2 s | 768,3 s | 1,01 | Completa |
| 16 | 1 | 32.768 + 512 | 691,5 s | 1.505,0 s | 0,63 | Completa |
| 16 | 2 | 33.536 + 512 | 276,5 s | 1.220,7 s | 0,54 | Completa |
| 16 | 3 | 34.304 + 512 | 266,3 s | 519,3 s | 2,02 | Completa |
| 17 | 1 | 32.768 + 512 | 742,4 s | 1.553,3 s | 0,63 | Completa |
| 17 | 2 | 33.536 + 512 | 277,6 s | 1.223,9 s | 0,54 | Completa |
| 17 | 3 | 34.304 + 512 | 268,6 s | 470,4 s | 2,53 | Completa |
| 18 | 1 | 32.768 + 512 | 793,4 s | 1.602,5 s | 0,63 | Completa |
| 18 | 2 | 33.536 + 512 | 280,1 s | 1.228,6 s | 0,54 | Completa |
| 18 | 3 | 34.304 + 512 | 268,9 s | 418,8 s | 3,41 | Completa |
| 19 | 1 | 32.768 + 512 | 24,0 s | 637,7 s | 0,83 | Completa |
| 19 | 2 | 33.536 + 512 | 230,0 s | 1.036,0 s | 0,63 | Completa |
| 19 | 3 | 34.304 + 512 | 280,0 s | 1.232,8 s | 0,54 | Completa |
| 20 | 1 | 32.768 + 512 | 71,0 s | 738,2 s | 0,77 | Completa |
| 20 | 2 | 33.536 + 512 | 234,1 s | 1.036,8 s | 0,64 | Completa |
| 20 | 3 | 34.304 + 512 | 281,7 s | 1.239,1 s | 0,53 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
