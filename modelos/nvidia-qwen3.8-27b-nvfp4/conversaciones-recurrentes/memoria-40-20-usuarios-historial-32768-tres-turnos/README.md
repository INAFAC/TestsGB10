# 20 usuarios · 40% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **2.116,4 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 264,7 s | 554,8 s | 600,2 s | 700,4 s | 3,51 tokens/s | No cumple |
| 2 | 20/20 | 487,0 s | 514,8 s | 525,7 s | 648,3 s | 2,74 tokens/s | No cumple |
| 3 | 20/20 | 545,2 s | 605,7 s | 629,7 s | 802,6 s | 2,37 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 446,0 s |
| Tiempo medio de respuesta completa | 602,9 s |
| Presupuesto configurado | 40% |
| Pico del motor / GB10 | 36,6% |
| Pico del sistema / GB10 | 45,1% |
| Menor memoria disponible | 66,79 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 6 / 6 |
| Máximo en cola | 19 |
| Recálculos | 88 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 14,52 |
| Suma de tiempos individuales | 36.176,7 s |
| Tiempo total de la prueba, incluyendo pausas | 2.116,4 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 377,6 s | 531,6 s | 1.654,7 s | 0,93 |
| 2 | 3/3 | 345,0 s | 509,3 s | 1.587,9 s | 0,97 |
| 3 | 3/3 | 447,2 s | 611,3 s | 1.894,0 s | 0,81 |
| 4 | 3/3 | 406,1 s | 574,6 s | 1.783,8 s | 0,86 |
| 5 | 3/3 | 559,3 s | 685,2 s | 2.115,7 s | 0,73 |
| 6 | 3/3 | 388,5 s | 552,0 s | 1.716,1 s | 0,90 |
| 7 | 3/3 | 419,7 s | 588,4 s | 1.825,3 s | 0,84 |
| 8 | 3/3 | 510,9 s | 670,0 s | 2.070,0 s | 0,74 |
| 9 | 3/3 | 468,6 s | 630,4 s | 1.951,1 s | 0,79 |
| 10 | 3/3 | 558,3 s | 684,6 s | 2.113,7 s | 0,73 |
| 11 | 3/3 | 357,1 s | 517,7 s | 1.613,1 s | 0,95 |
| 12 | 3/3 | 444,0 s | 598,1 s | 1.854,4 s | 0,83 |
| 13 | 3/3 | 524,2 s | 672,1 s | 2.076,2 s | 0,74 |
| 14 | 3/3 | 491,2 s | 658,5 s | 2.035,5 s | 0,75 |
| 15 | 3/3 | 507,7 s | 665,5 s | 2.056,4 s | 0,75 |
| 16 | 3/3 | 484,5 s | 651,6 s | 2.014,9 s | 0,76 |
| 17 | 3/3 | 544,3 s | 678,7 s | 2.096,1 s | 0,73 |
| 18 | 3/3 | 339,1 s | 502,4 s | 1.567,1 s | 0,98 |
| 19 | 3/3 | 413,3 s | 581,5 s | 1.804,4 s | 0,85 |
| 20 | 3/3 | 333,2 s | 495,5 s | 1.546,5 s | 0,99 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 512 | 96,9 s | 227,8 s | 3,91 | Completa |
| 1 | 2 | 33.536 + 512 | 509,8 s | 644,3 s | 3,80 | Completa |
| 1 | 3 | 34.304 + 512 | 526,2 s | 722,7 s | 2,60 | Completa |
| 2 | 1 | 32.768 + 512 | 48,8 s | 187,9 s | 3,67 | Completa |
| 2 | 2 | 33.536 + 512 | 485,1 s | 629,9 s | 3,53 | Completa |
| 2 | 3 | 34.304 + 512 | 501,2 s | 710,1 s | 2,45 | Completa |
| 3 | 1 | 32.768 + 512 | 335,6 s | 480,8 s | 3,52 | Completa |
| 3 | 2 | 33.536 + 512 | 485,2 s | 633,4 s | 3,45 | Completa |
| 3 | 3 | 34.304 + 512 | 520,6 s | 719,8 s | 2,57 | Completa |
| 4 | 1 | 32.768 + 512 | 189,5 s | 334,2 s | 3,53 | Completa |
| 4 | 2 | 33.536 + 512 | 485,4 s | 631,2 s | 3,50 | Completa |
| 4 | 3 | 34.304 + 512 | 543,3 s | 758,5 s | 2,37 | Completa |
| 5 | 1 | 32.768 + 512 | 600,2 s | 732,9 s | 3,85 | Completa |
| 5 | 2 | 33.536 + 512 | 525,7 s | 712,5 s | 2,74 | Completa |
| 5 | 3 | 34.304 + 512 | 552,0 s | 610,3 s | 8,76 | Completa |
| 6 | 1 | 32.768 + 512 | 171,1 s | 316,2 s | 3,52 | Completa |
| 6 | 2 | 33.536 + 512 | 483,5 s | 630,2 s | 3,48 | Completa |
| 6 | 3 | 34.304 + 512 | 510,9 s | 709,7 s | 2,57 | Completa |
| 7 | 1 | 32.768 + 512 | 225,8 s | 370,9 s | 3,52 | Completa |
| 7 | 2 | 33.536 + 512 | 487,0 s | 632,8 s | 3,50 | Completa |
| 7 | 3 | 34.304 + 512 | 546,5 s | 761,7 s | 2,37 | Completa |
| 8 | 1 | 32.768 + 512 | 500,1 s | 645,4 s | 3,52 | Completa |
| 8 | 2 | 33.536 + 512 | 488,4 s | 644,1 s | 3,28 | Completa |
| 8 | 3 | 34.304 + 512 | 544,1 s | 720,4 s | 2,90 | Completa |
| 9 | 1 | 32.768 + 512 | 354,1 s | 498,7 s | 3,53 | Completa |
| 9 | 2 | 33.536 + 512 | 486,4 s | 634,5 s | 3,45 | Completa |
| 9 | 3 | 34.304 + 512 | 565,4 s | 757,9 s | 2,65 | Completa |
| 10 | 1 | 32.768 + 512 | 554,8 s | 700,4 s | 3,51 | Completa |
| 10 | 2 | 33.536 + 512 | 490,4 s | 646,9 s | 3,26 | Completa |
| 10 | 3 | 34.304 + 512 | 629,7 s | 706,3 s | 6,67 | Completa |
| 11 | 1 | 32.768 + 512 | 66,4 s | 206,3 s | 3,65 | Completa |
| 11 | 2 | 33.536 + 512 | 485,2 s | 631,2 s | 3,50 | Completa |
| 11 | 3 | 34.304 + 512 | 519,7 s | 715,5 s | 2,61 | Completa |
| 12 | 1 | 32.768 + 512 | 264,7 s | 395,5 s | 3,91 | Completa |
| 12 | 2 | 33.536 + 512 | 511,2 s | 644,8 s | 3,82 | Completa |
| 12 | 3 | 34.304 + 512 | 556,0 s | 754,2 s | 2,58 | Completa |
| 13 | 1 | 32.768 + 512 | 518,6 s | 663,5 s | 3,53 | Completa |
| 13 | 2 | 33.536 + 512 | 489,4 s | 645,1 s | 3,28 | Completa |
| 13 | 3 | 34.304 + 512 | 564,5 s | 707,6 s | 3,57 | Completa |
| 14 | 1 | 32.768 + 512 | 390,3 s | 535,4 s | 3,52 | Completa |
| 14 | 2 | 33.536 + 512 | 487,6 s | 636,0 s | 3,44 | Completa |
| 14 | 3 | 34.304 + 512 | 595,6 s | 804,1 s | 2,45 | Completa |
| 15 | 1 | 32.768 + 512 | 432,4 s | 563,2 s | 3,91 | Completa |
| 15 | 2 | 33.536 + 512 | 514,8 s | 648,3 s | 3,83 | Completa |
| 15 | 3 | 34.304 + 512 | 575,9 s | 784,8 s | 2,45 | Completa |
| 16 | 1 | 32.768 + 512 | 372,5 s | 516,9 s | 3,54 | Completa |
| 16 | 2 | 33.536 + 512 | 487,3 s | 635,4 s | 3,45 | Completa |
| 16 | 3 | 34.304 + 512 | 593,6 s | 802,6 s | 2,45 | Completa |
| 17 | 1 | 32.768 + 512 | 537,1 s | 682,0 s | 3,53 | Completa |
| 17 | 2 | 33.536 + 512 | 490,1 s | 645,9 s | 3,28 | Completa |
| 17 | 3 | 34.304 + 512 | 605,7 s | 708,2 s | 4,99 | Completa |
| 18 | 1 | 32.768 + 512 | 32,2 s | 169,7 s | 3,72 | Completa |
| 18 | 2 | 33.536 + 512 | 484,8 s | 629,4 s | 3,53 | Completa |
| 18 | 3 | 34.304 + 512 | 500,5 s | 708,0 s | 2,46 | Completa |
| 19 | 1 | 32.768 + 512 | 207,9 s | 352,4 s | 3,54 | Completa |
| 19 | 2 | 33.536 + 512 | 486,6 s | 632,0 s | 3,51 | Completa |
| 19 | 3 | 34.304 + 512 | 545,2 s | 759,9 s | 2,38 | Completa |
| 20 | 1 | 32.768 + 512 | 16,3 s | 151,7 s | 3,77 | Completa |
| 20 | 2 | 33.536 + 512 | 483,5 s | 628,3 s | 3,53 | Completa |
| 20 | 3 | 34.304 + 512 | 500,0 s | 706,4 s | 2,47 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
