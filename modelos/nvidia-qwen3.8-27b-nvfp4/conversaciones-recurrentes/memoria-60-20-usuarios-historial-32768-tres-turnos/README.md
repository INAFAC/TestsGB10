# 20 usuarios · 60% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **2.120,5 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 211,8 s | 500,2 s | 540,2 s | 851,2 s | 1,46 tokens/s | No cumple |
| 2 | 20/20 | 332,2 s | 354,3 s | 362,6 s | 679,3 s | 1,42 tokens/s | No cumple |
| 3 | 20/20 | 379,5 s | 406,5 s | 416,2 s | 734,1 s | 1,45 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 325,0 s |
| Tiempo medio de respuesta completa | 637,0 s |
| Presupuesto configurado | 60% |
| Pico del motor / GB10 | 56,6% |
| Pico del sistema / GB10 | 65,6% |
| Menor memoria disponible | 41,89 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 11 / 11 |
| Máximo en cola | 19 |
| Recálculos | 39 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 14,49 |
| Suma de tiempos individuales | 38.220,4 s |
| Tiempo total de la prueba, incluyendo pausas | 2.120,5 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 324,2 s | 643,3 s | 1.990,0 s | 0,77 |
| 2 | 3/3 | 387,9 s | 682,2 s | 2.106,7 s | 0,73 |
| 3 | 3/3 | 266,9 s | 590,8 s | 1.832,4 s | 0,84 |
| 4 | 3/3 | 253,0 s | 573,2 s | 1.779,6 s | 0,86 |
| 5 | 3/3 | 308,0 s | 627,9 s | 1.943,6 s | 0,79 |
| 6 | 3/3 | 246,4 s | 564,6 s | 1.753,7 s | 0,88 |
| 7 | 3/3 | 282,3 s | 608,4 s | 1.885,3 s | 0,81 |
| 8 | 3/3 | 328,2 s | 663,8 s | 2.051,4 s | 0,75 |
| 9 | 3/3 | 396,0 s | 683,0 s | 2.109,2 s | 0,73 |
| 10 | 3/3 | 362,8 s | 679,2 s | 2.097,7 s | 0,73 |
| 11 | 3/3 | 423,6 s | 686,6 s | 2.119,8 s | 0,72 |
| 12 | 3/3 | 411,7 s | 685,2 s | 2.115,6 s | 0,73 |
| 13 | 3/3 | 274,4 s | 599,6 s | 1.858,8 s | 0,83 |
| 14 | 3/3 | 259,8 s | 582,0 s | 1.806,0 s | 0,85 |
| 15 | 3/3 | 345,9 s | 676,9 s | 2.090,6 s | 0,73 |
| 16 | 3/3 | 354,4 s | 678,1 s | 2.094,3 s | 0,73 |
| 17 | 3/3 | 232,5 s | 536,4 s | 1.669,2 s | 0,92 |
| 18 | 3/3 | 379,6 s | 681,3 s | 2.103,9 s | 0,73 |
| 19 | 3/3 | 290,7 s | 617,3 s | 1.911,8 s | 0,80 |
| 20 | 3/3 | 371,2 s | 680,3 s | 2.100,9 s | 0,73 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 512 | 211,8 s | 525,4 s | 1,63 | Completa |
| 1 | 2 | 33.536 + 512 | 344,7 s | 656,9 s | 1,64 | Completa |
| 1 | 3 | 34.304 + 512 | 416,2 s | 747,6 s | 1,54 | Completa |
| 2 | 1 | 32.768 + 512 | 450,5 s | 798,0 s | 1,47 | Completa |
| 2 | 2 | 33.536 + 512 | 331,5 s | 674,3 s | 1,49 | Completa |
| 2 | 3 | 34.304 + 512 | 381,7 s | 574,4 s | 2,65 | Completa |
| 3 | 1 | 32.768 + 512 | 84,9 s | 374,4 s | 1,77 | Completa |
| 3 | 2 | 33.536 + 512 | 346,5 s | 675,7 s | 1,55 | Completa |
| 3 | 3 | 34.304 + 512 | 369,2 s | 722,2 s | 1,45 | Completa |
| 4 | 1 | 32.768 + 512 | 48,7 s | 325,0 s | 1,85 | Completa |
| 4 | 2 | 33.536 + 512 | 342,8 s | 674,3 s | 1,54 | Completa |
| 4 | 3 | 34.304 + 512 | 367,5 s | 720,3 s | 1,45 | Completa |
| 5 | 1 | 32.768 + 512 | 171,8 s | 473,0 s | 1,70 | Completa |
| 5 | 2 | 33.536 + 512 | 354,3 s | 679,3 s | 1,57 | Completa |
| 5 | 3 | 34.304 + 512 | 397,8 s | 731,3 s | 1,53 | Completa |
| 6 | 1 | 32.768 + 512 | 32,2 s | 300,4 s | 1,90 | Completa |
| 6 | 2 | 33.536 + 512 | 340,1 s | 673,2 s | 1,53 | Completa |
| 6 | 3 | 34.304 + 512 | 366,9 s | 720,0 s | 1,45 | Completa |
| 7 | 1 | 32.768 + 512 | 125,9 s | 423,8 s | 1,72 | Completa |
| 7 | 2 | 33.536 + 512 | 350,3 s | 677,4 s | 1,56 | Completa |
| 7 | 3 | 34.304 + 512 | 370,7 s | 724,2 s | 1,45 | Completa |
| 8 | 1 | 32.768 + 512 | 302,4 s | 642,8 s | 1,50 | Completa |
| 8 | 2 | 33.536 + 512 | 282,6 s | 614,5 s | 1,54 | Completa |
| 8 | 3 | 34.304 + 512 | 399,5 s | 734,1 s | 1,53 | Completa |
| 9 | 1 | 32.768 + 512 | 475,2 s | 823,9 s | 1,47 | Completa |
| 9 | 2 | 33.536 + 512 | 330,5 s | 673,3 s | 1,49 | Completa |
| 9 | 3 | 34.304 + 512 | 382,4 s | 551,9 s | 3,01 | Completa |
| 10 | 1 | 32.768 + 512 | 376,6 s | 720,2 s | 1,49 | Completa |
| 10 | 2 | 33.536 + 512 | 331,9 s | 674,5 s | 1,49 | Completa |
| 10 | 3 | 34.304 + 512 | 379,9 s | 643,1 s | 1,94 | Completa |
| 11 | 1 | 32.768 + 512 | 540,2 s | 889,8 s | 1,46 | Completa |
| 11 | 2 | 33.536 + 512 | 362,6 s | 723,6 s | 1,42 | Completa |
| 11 | 3 | 34.304 + 512 | 368,1 s | 446,4 s | 6,53 | Completa |
| 12 | 1 | 32.768 + 512 | 500,2 s | 851,2 s | 1,46 | Completa |
| 12 | 2 | 33.536 + 512 | 328,3 s | 672,3 s | 1,49 | Completa |
| 12 | 3 | 34.304 + 512 | 406,5 s | 532,1 s | 4,07 | Completa |
| 13 | 1 | 32.768 + 512 | 104,8 s | 399,1 s | 1,74 | Completa |
| 13 | 2 | 33.536 + 512 | 347,8 s | 675,9 s | 1,56 | Completa |
| 13 | 3 | 34.304 + 512 | 370,7 s | 723,9 s | 1,45 | Completa |
| 14 | 1 | 32.768 + 512 | 66,3 s | 349,7 s | 1,80 | Completa |
| 14 | 2 | 33.536 + 512 | 344,0 s | 674,4 s | 1,55 | Completa |
| 14 | 3 | 34.304 + 512 | 369,0 s | 721,9 s | 1,45 | Completa |
| 15 | 1 | 32.768 + 512 | 327,1 s | 668,3 s | 1,50 | Completa |
| 15 | 2 | 33.536 + 512 | 331,9 s | 674,6 s | 1,49 | Completa |
| 15 | 3 | 34.304 + 512 | 378,7 s | 687,7 s | 1,65 | Completa |
| 16 | 1 | 32.768 + 512 | 351,8 s | 694,3 s | 1,49 | Completa |
| 16 | 2 | 33.536 + 512 | 332,0 s | 674,4 s | 1,49 | Completa |
| 16 | 3 | 34.304 + 512 | 379,5 s | 665,6 s | 1,79 | Completa |
| 17 | 1 | 32.768 + 512 | 16,3 s | 276,3 s | 1,97 | Completa |
| 17 | 2 | 33.536 + 512 | 285,7 s | 601,1 s | 1,62 | Completa |
| 17 | 3 | 34.304 + 512 | 395,5 s | 731,8 s | 1,52 | Completa |
| 18 | 1 | 32.768 + 512 | 425,9 s | 772,1 s | 1,48 | Completa |
| 18 | 2 | 33.536 + 512 | 331,3 s | 673,9 s | 1,49 | Completa |
| 18 | 3 | 34.304 + 512 | 381,6 s | 598,0 s | 2,36 | Completa |
| 19 | 1 | 32.768 + 512 | 148,2 s | 448,4 s | 1,70 | Completa |
| 19 | 2 | 33.536 + 512 | 351,7 s | 677,7 s | 1,57 | Completa |
| 19 | 3 | 34.304 + 512 | 372,1 s | 725,7 s | 1,45 | Completa |
| 20 | 1 | 32.768 + 512 | 401,3 s | 746,1 s | 1,48 | Completa |
| 20 | 2 | 33.536 + 512 | 332,2 s | 674,8 s | 1,49 | Completa |
| 20 | 3 | 34.304 + 512 | 380,1 s | 620,0 s | 2,13 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
