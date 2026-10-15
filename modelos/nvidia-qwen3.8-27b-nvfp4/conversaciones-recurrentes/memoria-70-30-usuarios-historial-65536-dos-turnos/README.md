# 30 usuarios · 70% · historial inicial de 65.536 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **6.337,6 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 30/30 | 1.414,3 s | 2.861,7 s | 2.937,2 s | 3.569,3 s | 0,72 tokens/s | No cumple |
| 2 | 30/30 | 2.556,4 s | 2.767,3 s | 2.787,3 s | 3.423,3 s | 0,69 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 1.986,0 s |
| Tiempo medio de respuesta completa | 2.608,9 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 76,0% |
| Menor memoria disponible | 29,23 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 8 / 8 |
| Máximo en cola | 29 |
| Recálculos | 75 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 4,85 |
| Suma de tiempos individuales | 156.536,2 s |
| Tiempo total de la prueba, incluyendo pausas | 6.337,6 s |
| Espera máxima sin datos en una conexión | 7.200 s |
| Plazo máximo configurado para todo el grupo | 10.800 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Historial de origen

Esta prueba continúa los historiales de [la etapa anterior](../memoria-70-30-usuarios-historial-32768-tres-turnos/README.md), conservando sus respuestas reales. Antes del primer turno se añade entrada sintética hasta 65.536 tokens. No se simulan los turnos intermedios entre ambos tamaños ni se presupone que todo el historial siga en la caché de la GPU.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 2/2 | 1.553,1 s | 2.175,8 s | 4.381,5 s | 0,23 |
| 2 | 2/2 | 2.377,8 s | 3.050,7 s | 6.131,4 s | 0,17 |
| 3 | 2/2 | 2.209,1 s | 2.893,7 s | 5.817,3 s | 0,18 |
| 4 | 2/2 | 1.804,5 s | 2.445,9 s | 4.921,9 s | 0,21 |
| 5 | 2/2 | 1.513,2 s | 2.138,1 s | 4.306,2 s | 0,24 |
| 6 | 2/2 | 2.124,0 s | 2.789,7 s | 5.609,4 s | 0,18 |
| 7 | 2/2 | 1.244,9 s | 1.887,2 s | 3.804,5 s | 0,27 |
| 8 | 2/2 | 2.692,4 s | 3.147,4 s | 6.324,7 s | 0,16 |
| 9 | 2/2 | 2.653,5 s | 3.144,8 s | 6.319,6 s | 0,16 |
| 10 | 2/2 | 1.217,5 s | 1.848,1 s | 3.726,1 s | 0,27 |
| 11 | 2/2 | 1.941,7 s | 2.593,6 s | 5.217,3 s | 0,20 |
| 12 | 2/2 | 1.422,6 s | 2.071,1 s | 4.172,1 s | 0,25 |
| 13 | 2/2 | 1.343,1 s | 2.002,5 s | 4.035,0 s | 0,25 |
| 14 | 2/2 | 1.979,7 s | 2.631,5 s | 5.293,0 s | 0,19 |
| 15 | 2/2 | 2.054,2 s | 2.739,2 s | 5.508,4 s | 0,19 |
| 16 | 2/2 | 2.453,7 s | 3.113,8 s | 6.257,6 s | 0,16 |
| 17 | 2/2 | 2.757,4 s | 3.153,0 s | 6.336,1 s | 0,16 |
| 18 | 2/2 | 1.656,9 s | 2.295,0 s | 4.620,0 s | 0,22 |
| 19 | 2/2 | 1.934,8 s | 2.555,8 s | 5.141,6 s | 0,20 |
| 20 | 2/2 | 1.730,7 s | 2.364,2 s | 4.758,4 s | 0,22 |
| 21 | 2/2 | 2.305,4 s | 2.969,3 s | 5.968,6 s | 0,17 |
| 22 | 2/2 | 2.302,1 s | 3.007,3 s | 6.044,6 s | 0,17 |
| 23 | 2/2 | 2.553,2 s | 3.128,0 s | 6.285,9 s | 0,16 |
| 24 | 2/2 | 1.582,6 s | 2.251,8 s | 4.533,6 s | 0,23 |
| 25 | 2/2 | 2.600,2 s | 3.138,5 s | 6.307,0 s | 0,16 |
| 26 | 2/2 | 2.603,0 s | 3.141,9 s | 6.313,8 s | 0,16 |
| 27 | 2/2 | 1.542,8 s | 2.213,8 s | 4.457,6 s | 0,23 |
| 28 | 2/2 | 1.877,8 s | 2.517,8 s | 5.065,6 s | 0,20 |
| 29 | 2/2 | 2.273,8 s | 2.931,3 s | 5.892,6 s | 0,17 |
| 30 | 2/2 | 1.273,2 s | 1.927,4 s | 3.884,8 s | 0,26 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 65.536 + 512 | 561,6 s | 1.120,9 s | 0,91 | Completa |
| 1 | 2 | 66.304 + 512 | 2.544,6 s | 3.230,6 s | 0,74 | Completa |
| 2 | 1 | 65.536 + 512 | 2.189,6 s | 2.854,8 s | 0,77 | Completa |
| 2 | 2 | 66.304 + 512 | 2.566,1 s | 3.246,6 s | 0,75 | Completa |
| 3 | 1 | 65.536 + 512 | 1.711,7 s | 2.336,0 s | 0,82 | Completa |
| 3 | 2 | 66.304 + 512 | 2.706,5 s | 3.451,3 s | 0,69 | Completa |
| 4 | 1 | 65.536 + 512 | 975,6 s | 1.634,9 s | 0,78 | Completa |
| 4 | 2 | 66.304 + 512 | 2.633,3 s | 3.257,0 s | 0,82 | Completa |
| 5 | 1 | 65.536 + 512 | 423,3 s | 984,1 s | 0,91 | Completa |
| 5 | 2 | 66.304 + 512 | 2.603,1 s | 3.292,1 s | 0,74 | Completa |
| 6 | 1 | 65.536 + 512 | 1.638,1 s | 2.260,2 s | 0,82 | Completa |
| 6 | 2 | 66.304 + 512 | 2.610,0 s | 3.319,2 s | 0,72 | Completa |
| 7 | 1 | 65.536 + 512 | 104,5 s | 673,2 s | 0,90 | Completa |
| 7 | 2 | 66.304 + 512 | 2.385,3 s | 3.101,2 s | 0,71 | Completa |
| 8 | 1 | 65.536 + 512 | 2.861,7 s | 3.569,3 s | 0,72 | Completa |
| 8 | 2 | 66.304 + 512 | 2.523,1 s | 2.725,4 s | 2,53 | Completa |
| 9 | 1 | 65.536 + 512 | 2.787,8 s | 3.498,4 s | 0,72 | Completa |
| 9 | 2 | 66.304 + 512 | 2.519,3 s | 2.791,3 s | 1,88 | Completa |
| 10 | 1 | 65.536 + 512 | 52,4 s | 600,2 s | 0,93 | Completa |
| 10 | 2 | 66.304 + 512 | 2.382,6 s | 3.095,9 s | 0,72 | Completa |
| 11 | 1 | 65.536 + 512 | 1.414,3 s | 2.037,5 s | 0,82 | Completa |
| 11 | 2 | 66.304 + 512 | 2.469,1 s | 3.149,7 s | 0,75 | Completa |
| 12 | 1 | 65.536 + 512 | 285,9 s | 898,6 s | 0,83 | Completa |
| 12 | 2 | 66.304 + 512 | 2.559,3 s | 3.243,5 s | 0,75 | Completa |
| 13 | 1 | 65.536 + 512 | 220,4 s | 822,8 s | 0,85 | Completa |
| 13 | 2 | 66.304 + 512 | 2.465,8 s | 3.182,1 s | 0,71 | Completa |
| 14 | 1 | 65.536 + 512 | 1.488,4 s | 2.110,5 s | 0,82 | Completa |
| 14 | 2 | 66.304 + 512 | 2.471,0 s | 3.152,5 s | 0,75 | Completa |
| 15 | 1 | 65.536 + 512 | 1.565,6 s | 2.186,4 s | 0,82 | Completa |
| 15 | 2 | 66.304 + 512 | 2.542,9 s | 3.292,0 s | 0,68 | Completa |
| 16 | 1 | 65.536 + 512 | 2.265,1 s | 2.930,4 s | 0,77 | Completa |
| 16 | 2 | 66.304 + 512 | 2.642,2 s | 3.297,2 s | 0,78 | Completa |
| 17 | 1 | 65.536 + 512 | 2.937,2 s | 3.647,8 s | 0,72 | Completa |
| 17 | 2 | 66.304 + 512 | 2.577,5 s | 2.658,3 s | 6,32 | Completa |
| 18 | 1 | 65.536 + 512 | 827,8 s | 1.485,2 s | 0,78 | Completa |
| 18 | 2 | 66.304 + 512 | 2.486,0 s | 3.104,7 s | 0,83 | Completa |
| 19 | 1 | 65.536 + 512 | 1.313,3 s | 1.874,3 s | 0,91 | Completa |
| 19 | 2 | 66.304 + 512 | 2.556,4 s | 3.237,2 s | 0,75 | Completa |
| 20 | 1 | 65.536 + 512 | 901,8 s | 1.559,1 s | 0,78 | Completa |
| 20 | 2 | 66.304 + 512 | 2.559,6 s | 3.169,3 s | 0,84 | Completa |
| 21 | 1 | 65.536 + 512 | 2.024,9 s | 2.608,1 s | 0,88 | Completa |
| 21 | 2 | 66.304 + 512 | 2.586,0 s | 3.330,6 s | 0,69 | Completa |
| 22 | 1 | 65.536 + 512 | 2.115,4 s | 2.781,0 s | 0,77 | Completa |
| 22 | 2 | 66.304 + 512 | 2.488,8 s | 3.233,7 s | 0,69 | Completa |
| 23 | 1 | 65.536 + 512 | 2.339,2 s | 3.004,2 s | 0,77 | Completa |
| 23 | 2 | 66.304 + 512 | 2.767,3 s | 3.251,7 s | 1,05 | Completa |
| 24 | 1 | 65.536 + 512 | 752,2 s | 1.409,4 s | 0,78 | Completa |
| 24 | 2 | 66.304 + 512 | 2.412,9 s | 3.094,2 s | 0,75 | Completa |
| 25 | 1 | 65.536 + 512 | 2.413,0 s | 3.079,9 s | 0,77 | Completa |
| 25 | 2 | 66.304 + 512 | 2.787,3 s | 3.197,2 s | 1,25 | Completa |
| 26 | 1 | 65.536 + 512 | 2.603,6 s | 3.339,4 s | 0,69 | Completa |
| 26 | 2 | 66.304 + 512 | 2.602,4 s | 2.944,4 s | 1,49 | Completa |
| 27 | 1 | 65.536 + 512 | 678,1 s | 1.336,3 s | 0,78 | Completa |
| 27 | 2 | 66.304 + 512 | 2.407,5 s | 3.091,3 s | 0,75 | Completa |
| 28 | 1 | 65.536 + 512 | 1.130,7 s | 1.729,7 s | 0,85 | Completa |
| 28 | 2 | 66.304 + 512 | 2.624,9 s | 3.305,9 s | 0,75 | Completa |
| 29 | 1 | 65.536 + 512 | 1.868,5 s | 2.439,3 s | 0,90 | Completa |
| 29 | 2 | 66.304 + 512 | 2.679,0 s | 3.423,3 s | 0,69 | Completa |
| 30 | 1 | 65.536 + 512 | 161,0 s | 749,1 s | 0,87 | Completa |
| 30 | 2 | 66.304 + 512 | 2.385,4 s | 3.105,7 s | 0,71 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
