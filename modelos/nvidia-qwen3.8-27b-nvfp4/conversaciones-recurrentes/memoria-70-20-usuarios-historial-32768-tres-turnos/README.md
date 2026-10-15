# 20 usuarios · 70% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **2.102,8 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 194,4 s | 494,0 s | 520,9 s | 887,5 s | 1,30 tokens/s | No cumple |
| 2 | 20/20 | 300,1 s | 321,1 s | 322,7 s | 767,1 s | 1,10 tokens/s | No cumple |
| 3 | 20/20 | 293,6 s | 375,3 s | 376,3 s | 767,3 s | 1,04 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 275,2 s |
| Tiempo medio de respuesta completa | 643,5 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,8% |
| Pico del sistema / GB10 | 75,7% |
| Menor memoria disponible | 29,58 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 13 / 13 |
| Máximo en cola | 19 |
| Recálculos | 24 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 14,61 |
| Suma de tiempos individuales | 38.611,8 s |
| Tiempo total de la prueba, incluyendo pausas | 2.102,8 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 188,9 s | 571,1 s | 1.773,3 s | 0,87 |
| 2 | 3/3 | 194,5 s | 580,9 s | 1.802,8 s | 0,85 |
| 3 | 3/3 | 224,4 s | 627,0 s | 1.941,1 s | 0,79 |
| 4 | 3/3 | 365,6 s | 680,7 s | 2.102,1 s | 0,73 |
| 5 | 3/3 | 327,9 s | 677,1 s | 2.091,2 s | 0,73 |
| 6 | 3/3 | 295,5 s | 668,4 s | 2.065,1 s | 0,74 |
| 7 | 3/3 | 331,1 s | 675,5 s | 2.086,6 s | 0,74 |
| 8 | 3/3 | 206,3 s | 590,8 s | 1.832,3 s | 0,84 |
| 9 | 3/3 | 209,3 s | 606,9 s | 1.880,6 s | 0,82 |
| 10 | 3/3 | 260,2 s | 662,0 s | 2.046,0 s | 0,75 |
| 11 | 3/3 | 309,5 s | 672,3 s | 2.077,0 s | 0,74 |
| 12 | 3/3 | 216,6 s | 616,7 s | 1.910,2 s | 0,80 |
| 13 | 3/3 | 305,6 s | 669,8 s | 2.069,3 s | 0,74 |
| 14 | 3/3 | 319,5 s | 673,5 s | 2.080,4 s | 0,74 |
| 15 | 3/3 | 238,5 s | 634,5 s | 1.963,5 s | 0,78 |
| 16 | 3/3 | 315,0 s | 671,1 s | 2.073,3 s | 0,74 |
| 17 | 3/3 | 329,0 s | 674,5 s | 2.083,6 s | 0,74 |
| 18 | 3/3 | 337,5 s | 677,9 s | 2.093,7 s | 0,73 |
| 19 | 3/3 | 346,5 s | 678,7 s | 2.096,0 s | 0,73 |
| 20 | 3/3 | 183,3 s | 561,2 s | 1.743,8 s | 0,88 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 512 | 31,8 s | 330,3 s | 1,71 | Completa |
| 1 | 2 | 33.536 + 512 | 238,8 s | 618,1 s | 1,35 | Completa |
| 1 | 3 | 34.304 + 512 | 296,2 s | 764,9 s | 1,09 | Completa |
| 2 | 1 | 32.768 + 512 | 48,1 s | 357,1 s | 1,65 | Completa |
| 2 | 2 | 33.536 + 512 | 237,9 s | 618,5 s | 1,34 | Completa |
| 2 | 3 | 34.304 + 512 | 297,6 s | 767,3 s | 1,09 | Completa |
| 3 | 1 | 32.768 + 512 | 124,4 s | 464,7 s | 1,50 | Completa |
| 3 | 2 | 33.536 + 512 | 315,5 s | 693,6 s | 1,35 | Completa |
| 3 | 3 | 34.304 + 512 | 233,3 s | 722,8 s | 1,04 | Completa |
| 4 | 1 | 32.768 + 512 | 520,9 s | 914,6 s | 1,30 | Completa |
| 4 | 2 | 33.536 + 512 | 302,9 s | 769,6 s | 1,10 | Completa |
| 4 | 3 | 34.304 + 512 | 273,0 s | 358,0 s | 6,01 | Completa |
| 5 | 1 | 32.768 + 512 | 440,2 s | 833,4 s | 1,30 | Completa |
| 5 | 2 | 33.536 + 512 | 298,8 s | 762,5 s | 1,10 | Completa |
| 5 | 3 | 34.304 + 512 | 244,8 s | 435,3 s | 2,68 | Completa |
| 6 | 1 | 32.768 + 512 | 194,4 s | 544,7 s | 1,46 | Completa |
| 6 | 2 | 33.536 + 512 | 319,2 s | 697,7 s | 1,35 | Completa |
| 6 | 3 | 34.304 + 512 | 372,9 s | 762,7 s | 1,31 | Completa |
| 7 | 1 | 32.768 + 512 | 413,3 s | 806,4 s | 1,30 | Completa |
| 7 | 2 | 33.536 + 512 | 251,0 s | 657,1 s | 1,26 | Completa |
| 7 | 3 | 34.304 + 512 | 329,0 s | 563,2 s | 2,18 | Completa |
| 8 | 1 | 32.768 + 512 | 65,4 s | 384,0 s | 1,60 | Completa |
| 8 | 2 | 33.536 + 512 | 262,5 s | 625,7 s | 1,41 | Completa |
| 8 | 3 | 34.304 + 512 | 291,1 s | 762,6 s | 1,08 | Completa |
| 9 | 1 | 32.768 + 512 | 83,8 s | 410,9 s | 1,56 | Completa |
| 9 | 2 | 33.536 + 512 | 313,7 s | 692,4 s | 1,35 | Completa |
| 9 | 3 | 34.304 + 512 | 230,5 s | 717,4 s | 1,05 | Completa |
| 10 | 1 | 32.768 + 512 | 169,8 s | 518,5 s | 1,47 | Completa |
| 10 | 2 | 33.536 + 512 | 317,2 s | 695,3 s | 1,35 | Completa |
| 10 | 3 | 34.304 + 512 | 293,6 s | 772,2 s | 1,07 | Completa |
| 11 | 1 | 32.768 + 512 | 332,6 s | 725,5 s | 1,30 | Completa |
| 11 | 2 | 33.536 + 512 | 225,3 s | 607,9 s | 1,34 | Completa |
| 11 | 3 | 34.304 + 512 | 370,5 s | 683,6 s | 1,63 | Completa |
| 12 | 1 | 32.768 + 512 | 103,5 s | 437,8 s | 1,53 | Completa |
| 12 | 2 | 33.536 + 512 | 315,2 s | 693,4 s | 1,35 | Completa |
| 12 | 3 | 34.304 + 512 | 231,2 s | 718,9 s | 1,05 | Completa |
| 13 | 1 | 32.768 + 512 | 220,3 s | 569,9 s | 1,46 | Completa |
| 13 | 2 | 33.536 + 512 | 321,1 s | 699,7 s | 1,35 | Completa |
| 13 | 3 | 34.304 + 512 | 375,3 s | 739,8 s | 1,40 | Completa |
| 14 | 1 | 32.768 + 512 | 359,5 s | 752,2 s | 1,30 | Completa |
| 14 | 2 | 33.536 + 512 | 227,1 s | 609,4 s | 1,34 | Completa |
| 14 | 3 | 34.304 + 512 | 371,9 s | 658,9 s | 1,78 | Completa |
| 15 | 1 | 32.768 + 512 | 146,5 s | 491,5 s | 1,48 | Completa |
| 15 | 2 | 33.536 + 512 | 316,9 s | 695,2 s | 1,35 | Completa |
| 15 | 3 | 34.304 + 512 | 252,0 s | 716,8 s | 1,10 | Completa |
| 16 | 1 | 32.768 + 512 | 246,0 s | 595,7 s | 1,46 | Completa |
| 16 | 2 | 33.536 + 512 | 322,7 s | 702,4 s | 1,35 | Completa |
| 16 | 3 | 34.304 + 512 | 376,3 s | 715,2 s | 1,51 | Completa |
| 17 | 1 | 32.768 + 512 | 386,4 s | 779,3 s | 1,30 | Completa |
| 17 | 2 | 33.536 + 512 | 226,4 s | 609,4 s | 1,33 | Completa |
| 17 | 3 | 34.304 + 512 | 374,2 s | 634,9 s | 1,96 | Completa |
| 18 | 1 | 32.768 + 512 | 467,1 s | 860,5 s | 1,30 | Completa |
| 18 | 2 | 33.536 + 512 | 300,1 s | 764,5 s | 1,10 | Completa |
| 18 | 3 | 34.304 + 512 | 245,2 s | 408,7 s | 3,13 | Completa |
| 19 | 1 | 32.768 + 512 | 494,0 s | 887,5 s | 1,30 | Completa |
| 19 | 2 | 33.536 + 512 | 301,4 s | 767,1 s | 1,10 | Completa |
| 19 | 3 | 34.304 + 512 | 244,0 s | 381,4 s | 3,72 | Completa |
| 20 | 1 | 32.768 + 512 | 16,1 s | 304,0 s | 1,77 | Completa |
| 20 | 2 | 33.536 + 512 | 239,4 s | 617,7 s | 1,35 | Completa |
| 20 | 3 | 34.304 + 512 | 294,3 s | 762,0 s | 1,09 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
