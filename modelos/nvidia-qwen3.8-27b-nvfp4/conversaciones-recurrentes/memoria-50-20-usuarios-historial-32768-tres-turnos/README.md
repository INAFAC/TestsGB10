# 20 usuarios · 50% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **2.805,0 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 316,9 s | 716,5 s | 745,3 s | 1.045,1 s | 1,45 tokens/s | No cumple |
| 2 | 20/20 | 553,6 s | 648,3 s | 650,9 s | 1.036,1 s | 1,29 tokens/s | No cumple |
| 3 | 20/20 | 585,8 s | 657,3 s | 687,0 s | 1.029,4 s | 1,22 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 505,9 s |
| Tiempo medio de respuesta completa | 836,8 s |
| Presupuesto configurado | 50% |
| Pico del motor / GB10 | 46,6% |
| Pico del sistema / GB10 | 55,4% |
| Menor memoria disponible | 54,19 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 9 / 9 |
| Máximo en cola | 19 |
| Recálculos | 85 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 10,95 |
| Suma de tiempos individuales | 50.206,6 s |
| Tiempo total de la prueba, incluyendo pausas | 2.805,0 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 391,6 s | 701,4 s | 2.164,2 s | 0,71 |
| 2 | 3/3 | 630,9 s | 909,7 s | 2.789,2 s | 0,55 |
| 3 | 3/3 | 586,6 s | 901,0 s | 2.762,9 s | 0,56 |
| 4 | 3/3 | 530,8 s | 894,1 s | 2.742,2 s | 0,56 |
| 5 | 3/3 | 432,7 s | 775,1 s | 2.385,3 s | 0,64 |
| 6 | 3/3 | 516,4 s | 873,8 s | 2.681,3 s | 0,57 |
| 7 | 3/3 | 607,4 s | 904,2 s | 2.772,6 s | 0,55 |
| 8 | 3/3 | 451,9 s | 825,6 s | 2.536,7 s | 0,61 |
| 9 | 3/3 | 538,7 s | 895,5 s | 2.746,6 s | 0,56 |
| 10 | 3/3 | 642,4 s | 914,1 s | 2.802,3 s | 0,55 |
| 11 | 3/3 | 449,7 s | 793,8 s | 2.441,5 s | 0,63 |
| 12 | 3/3 | 578,2 s | 897,5 s | 2.752,4 s | 0,56 |
| 13 | 3/3 | 528,9 s | 883,9 s | 2.711,7 s | 0,57 |
| 14 | 3/3 | 416,5 s | 743,8 s | 2.291,5 s | 0,67 |
| 15 | 3/3 | 422,8 s | 764,7 s | 2.354,1 s | 0,65 |
| 16 | 3/3 | 413,3 s | 754,3 s | 2.322,8 s | 0,66 |
| 17 | 3/3 | 402,7 s | 733,9 s | 2.261,6 s | 0,68 |
| 18 | 3/3 | 430,3 s | 804,6 s | 2.473,7 s | 0,62 |
| 19 | 3/3 | 654,9 s | 914,7 s | 2.804,3 s | 0,55 |
| 20 | 3/3 | 490,8 s | 850,0 s | 2.609,9 s | 0,59 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 512 | 23,6 s | 231,6 s | 2,46 | Completa |
| 1 | 2 | 33.536 + 512 | 512,5 s | 843,2 s | 1,55 | Completa |
| 1 | 3 | 34.304 + 512 | 638,9 s | 1.029,4 s | 1,31 | Completa |
| 2 | 1 | 32.768 + 512 | 687,5 s | 1.016,0 s | 1,56 | Completa |
| 2 | 2 | 33.536 + 512 | 518,1 s | 901,1 s | 1,33 | Completa |
| 2 | 3 | 34.304 + 512 | 687,0 s | 812,1 s | 4,09 | Completa |
| 3 | 1 | 32.768 + 512 | 629,6 s | 957,9 s | 1,56 | Completa |
| 3 | 2 | 33.536 + 512 | 515,2 s | 897,9 s | 1,34 | Completa |
| 3 | 3 | 34.304 + 512 | 615,1 s | 847,1 s | 2,20 | Completa |
| 4 | 1 | 32.768 + 512 | 400,6 s | 743,1 s | 1,49 | Completa |
| 4 | 2 | 33.536 + 512 | 635,5 s | 1.023,1 s | 1,32 | Completa |
| 4 | 3 | 34.304 + 512 | 556,3 s | 916,0 s | 1,42 | Completa |
| 5 | 1 | 32.768 + 512 | 146,4 s | 370,5 s | 2,28 | Completa |
| 5 | 2 | 33.536 + 512 | 648,3 s | 1.036,1 s | 1,32 | Completa |
| 5 | 3 | 34.304 + 512 | 503,3 s | 918,7 s | 1,23 | Completa |
| 6 | 1 | 32.768 + 512 | 344,8 s | 685,3 s | 1,50 | Completa |
| 6 | 2 | 33.536 + 512 | 547,2 s | 917,4 s | 1,38 | Completa |
| 6 | 3 | 34.304 + 512 | 657,2 s | 1.018,5 s | 1,41 | Completa |
| 7 | 1 | 32.768 + 512 | 658,6 s | 986,9 s | 1,56 | Completa |
| 7 | 2 | 33.536 + 512 | 516,9 s | 898,8 s | 1,34 | Completa |
| 7 | 3 | 34.304 + 512 | 646,6 s | 826,8 s | 2,84 | Completa |
| 8 | 1 | 32.768 + 512 | 288,9 s | 627,7 s | 1,51 | Completa |
| 8 | 2 | 33.536 + 512 | 481,0 s | 874,8 s | 1,30 | Completa |
| 8 | 3 | 34.304 + 512 | 585,8 s | 974,1 s | 1,32 | Completa |
| 9 | 1 | 32.768 + 512 | 427,6 s | 780,8 s | 1,45 | Completa |
| 9 | 2 | 33.536 + 512 | 629,8 s | 1.014,2 s | 1,33 | Completa |
| 9 | 3 | 34.304 + 512 | 558,9 s | 891,7 s | 1,54 | Completa |
| 10 | 1 | 32.768 + 512 | 716,5 s | 1.045,1 s | 1,55 | Completa |
| 10 | 2 | 33.536 + 512 | 553,6 s | 951,2 s | 1,29 | Completa |
| 10 | 3 | 34.304 + 512 | 657,3 s | 746,0 s | 5,76 | Completa |
| 11 | 1 | 32.768 + 512 | 172,8 s | 398,4 s | 2,26 | Completa |
| 11 | 2 | 33.536 + 512 | 650,9 s | 1.040,3 s | 1,31 | Completa |
| 11 | 3 | 34.304 + 512 | 525,4 s | 942,7 s | 1,22 | Completa |
| 12 | 1 | 32.768 + 512 | 561,8 s | 852,1 s | 1,76 | Completa |
| 12 | 2 | 33.536 + 512 | 589,1 s | 972,3 s | 1,33 | Completa |
| 12 | 3 | 34.304 + 512 | 583,8 s | 868,0 s | 1,80 | Completa |
| 13 | 1 | 32.768 + 512 | 372,7 s | 714,2 s | 1,50 | Completa |
| 13 | 2 | 33.536 + 512 | 603,1 s | 966,3 s | 1,41 | Completa |
| 13 | 3 | 34.304 + 512 | 610,8 s | 971,2 s | 1,42 | Completa |
| 14 | 1 | 32.768 + 512 | 69,7 s | 286,7 s | 2,35 | Completa |
| 14 | 2 | 33.536 + 512 | 609,8 s | 959,0 s | 1,46 | Completa |
| 14 | 3 | 34.304 + 512 | 570,1 s | 985,8 s | 1,23 | Completa |
| 15 | 1 | 32.768 + 512 | 119,6 s | 342,6 s | 2,29 | Completa |
| 15 | 2 | 33.536 + 512 | 647,0 s | 1.034,2 s | 1,32 | Completa |
| 15 | 3 | 34.304 + 512 | 501,7 s | 917,3 s | 1,23 | Completa |
| 16 | 1 | 32.768 + 512 | 94,1 s | 314,6 s | 2,32 | Completa |
| 16 | 2 | 33.536 + 512 | 644,4 s | 1.031,0 s | 1,32 | Completa |
| 16 | 3 | 34.304 + 512 | 501,5 s | 917,1 s | 1,23 | Completa |
| 17 | 1 | 32.768 + 512 | 46,3 s | 259,1 s | 2,40 | Completa |
| 17 | 2 | 33.536 + 512 | 547,6 s | 911,2 s | 1,41 | Completa |
| 17 | 3 | 34.304 + 512 | 614,0 s | 1.031,2 s | 1,22 | Completa |
| 18 | 1 | 32.768 + 512 | 260,9 s | 599,2 s | 1,51 | Completa |
| 18 | 2 | 33.536 + 512 | 479,2 s | 869,9 s | 1,31 | Completa |
| 18 | 3 | 34.304 + 512 | 550,6 s | 944,5 s | 1,30 | Completa |
| 19 | 1 | 32.768 + 512 | 745,3 s | 1.074,2 s | 1,55 | Completa |
| 19 | 2 | 33.536 + 512 | 591,2 s | 981,1 s | 1,31 | Completa |
| 19 | 3 | 34.304 + 512 | 628,2 s | 689,0 s | 8,41 | Completa |
| 20 | 1 | 32.768 + 512 | 316,9 s | 656,4 s | 1,51 | Completa |
| 20 | 2 | 33.536 + 512 | 510,5 s | 881,6 s | 1,38 | Completa |
| 20 | 3 | 34.304 + 512 | 645,1 s | 1.011,9 s | 1,39 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
