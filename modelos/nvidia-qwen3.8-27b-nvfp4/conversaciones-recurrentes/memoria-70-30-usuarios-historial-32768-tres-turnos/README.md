# 30 usuarios · 70% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **90/90**. Tiempo de la prueba: **4.289,5 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 30/30 | 494,2 s | 1.129,2 s | 1.164,3 s | 1.691,4 s | 0,90 tokens/s | No cumple |
| 2 | 30/30 | 792,5 s | 940,0 s | 944,2 s | 1.509,9 s | 0,81 tokens/s | No cumple |
| 3 | 30/30 | 898,4 s | 1.000,9 s | 1.031,3 s | 1.628,8 s | 0,73 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 747,3 s |
| Tiempo medio de respuesta completa | 1.293,6 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,8% |
| Menor memoria disponible | 29,46 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 14 / 14 |
| Máximo en cola | 29 |
| Recálculos | 70 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 10,74 |
| Suma de tiempos individuales | 116.425,9 s |
| Tiempo total de la prueba, incluyendo pausas | 4.289,5 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 656,4 s | 1.219,3 s | 3.717,8 s | 0,41 |
| 2 | 3/3 | 668,5 s | 1.206,3 s | 3.678,8 s | 0,42 |
| 3 | 3/3 | 910,4 s | 1.401,4 s | 4.264,3 s | 0,36 |
| 4 | 3/3 | 948,8 s | 1.406,2 s | 4.278,6 s | 0,36 |
| 5 | 3/3 | 569,5 s | 1.112,0 s | 3.396,0 s | 0,45 |
| 6 | 3/3 | 930,1 s | 1.402,8 s | 4.268,4 s | 0,36 |
| 7 | 3/3 | 599,9 s | 1.139,4 s | 3.478,3 s | 0,44 |
| 8 | 3/3 | 681,5 s | 1.245,8 s | 3.797,5 s | 0,40 |
| 9 | 3/3 | 897,7 s | 1.400,5 s | 4.261,5 s | 0,36 |
| 10 | 3/3 | 988,6 s | 1.409,5 s | 4.288,6 s | 0,36 |
| 11 | 3/3 | 841,2 s | 1.393,4 s | 4.240,3 s | 0,36 |
| 12 | 3/3 | 848,5 s | 1.396,0 s | 4.248,0 s | 0,36 |
| 13 | 3/3 | 785,3 s | 1.385,7 s | 4.217,2 s | 0,36 |
| 14 | 3/3 | 614,8 s | 1.167,5 s | 3.562,5 s | 0,43 |
| 15 | 3/3 | 669,9 s | 1.232,3 s | 3.756,9 s | 0,41 |
| 16 | 3/3 | 644,3 s | 1.193,2 s | 3.639,7 s | 0,42 |
| 17 | 3/3 | 546,4 s | 1.083,1 s | 3.309,4 s | 0,46 |
| 18 | 3/3 | 826,3 s | 1.392,0 s | 4.236,1 s | 0,36 |
| 19 | 3/3 | 669,5 s | 1.277,8 s | 3.893,4 s | 0,39 |
| 20 | 3/3 | 810,6 s | 1.390,5 s | 4.231,6 s | 0,36 |
| 21 | 3/3 | 860,7 s | 1.397,1 s | 4.251,4 s | 0,36 |
| 22 | 3/3 | 681,9 s | 1.290,5 s | 3.931,6 s | 0,39 |
| 23 | 3/3 | 885,1 s | 1.398,9 s | 4.256,6 s | 0,36 |
| 24 | 3/3 | 759,2 s | 1.348,9 s | 4.106,8 s | 0,37 |
| 25 | 3/3 | 525,0 s | 1.045,4 s | 3.196,1 s | 0,48 |
| 26 | 3/3 | 731,4 s | 1.324,0 s | 4.032,0 s | 0,38 |
| 27 | 3/3 | 694,2 s | 1.258,0 s | 3.834,0 s | 0,40 |
| 28 | 3/3 | 704,9 s | 1.315,8 s | 4.007,5 s | 0,38 |
| 29 | 3/3 | 836,1 s | 1.394,8 s | 4.244,3 s | 0,36 |
| 30 | 3/3 | 633,6 s | 1.180,3 s | 3.601,0 s | 0,43 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 512 | 235,0 s | 660,6 s | 1,20 | Completa |
| 1 | 2 | 33.536 + 512 | 932,9 s | 1.503,4 s | 0,90 | Completa |
| 1 | 3 | 34.304 + 512 | 801,2 s | 1.493,8 s | 0,74 | Completa |
| 2 | 1 | 32.768 + 512 | 204,4 s | 627,4 s | 1,21 | Completa |
| 2 | 2 | 33.536 + 512 | 892,8 s | 1.392,3 s | 1,02 | Completa |
| 2 | 3 | 34.304 + 512 | 908,2 s | 1.599,1 s | 0,74 | Completa |
| 3 | 1 | 32.768 + 512 | 1.058,1 s | 1.620,6 s | 0,91 | Completa |
| 3 | 2 | 33.536 + 512 | 764,3 s | 1.370,0 s | 0,84 | Completa |
| 3 | 3 | 34.304 + 512 | 908,7 s | 1.213,6 s | 1,68 | Completa |
| 4 | 1 | 32.768 + 512 | 1.129,2 s | 1.691,4 s | 0,91 | Completa |
| 4 | 2 | 33.536 + 512 | 769,0 s | 1.398,6 s | 0,81 | Completa |
| 4 | 3 | 34.304 + 512 | 948,1 s | 1.128,6 s | 2,83 | Completa |
| 5 | 1 | 32.768 + 512 | 70,0 s | 457,4 s | 1,32 | Completa |
| 5 | 2 | 33.536 + 512 | 789,5 s | 1.356,2 s | 0,90 | Completa |
| 5 | 3 | 34.304 + 512 | 848,9 s | 1.522,4 s | 0,76 | Completa |
| 6 | 1 | 32.768 + 512 | 1.093,7 s | 1.656,0 s | 0,91 | Completa |
| 6 | 2 | 33.536 + 512 | 763,4 s | 1.370,2 s | 0,84 | Completa |
| 6 | 3 | 34.304 + 512 | 933,3 s | 1.182,2 s | 2,05 | Completa |
| 7 | 1 | 32.768 + 512 | 94,5 s | 491,4 s | 1,29 | Completa |
| 7 | 2 | 33.536 + 512 | 792,5 s | 1.358,6 s | 0,90 | Completa |
| 7 | 3 | 34.304 + 512 | 912,7 s | 1.568,3 s | 0,78 | Completa |
| 8 | 1 | 32.768 + 512 | 299,8 s | 726,0 s | 1,20 | Completa |
| 8 | 2 | 33.536 + 512 | 940,0 s | 1.509,9 s | 0,90 | Completa |
| 8 | 3 | 34.304 + 512 | 804,6 s | 1.501,6 s | 0,73 | Completa |
| 9 | 1 | 32.768 + 512 | 1.022,9 s | 1.585,6 s | 0,91 | Completa |
| 9 | 2 | 33.536 + 512 | 762,2 s | 1.367,6 s | 0,84 | Completa |
| 9 | 3 | 34.304 + 512 | 907,9 s | 1.248,3 s | 1,50 | Completa |
| 10 | 1 | 32.768 + 512 | 1.164,3 s | 1.726,7 s | 0,91 | Completa |
| 10 | 2 | 33.536 + 512 | 770,3 s | 1.400,7 s | 0,81 | Completa |
| 10 | 3 | 34.304 + 512 | 1.031,3 s | 1.101,2 s | 7,31 | Completa |
| 11 | 1 | 32.768 + 512 | 728,7 s | 1.274,1 s | 0,94 | Completa |
| 11 | 2 | 33.536 + 512 | 867,1 s | 1.419,9 s | 0,92 | Completa |
| 11 | 3 | 34.304 + 512 | 927,9 s | 1.486,3 s | 0,92 | Completa |
| 12 | 1 | 32.768 + 512 | 794,5 s | 1.344,5 s | 0,93 | Completa |
| 12 | 2 | 33.536 + 512 | 894,3 s | 1.498,7 s | 0,85 | Completa |
| 12 | 3 | 34.304 + 512 | 856,8 s | 1.344,7 s | 1,05 | Completa |
| 13 | 1 | 32.768 + 512 | 596,2 s | 1.161,5 s | 0,90 | Completa |
| 13 | 2 | 33.536 + 512 | 762,2 s | 1.334,4 s | 0,89 | Completa |
| 13 | 3 | 34.304 + 512 | 997,5 s | 1.661,3 s | 0,77 | Completa |
| 14 | 1 | 32.768 + 512 | 120,2 s | 525,4 s | 1,26 | Completa |
| 14 | 2 | 33.536 + 512 | 793,6 s | 1.359,9 s | 0,90 | Completa |
| 14 | 3 | 34.304 + 512 | 930,5 s | 1.617,2 s | 0,74 | Completa |
| 15 | 1 | 32.768 + 512 | 266,8 s | 693,1 s | 1,20 | Completa |
| 15 | 2 | 33.536 + 512 | 939,1 s | 1.507,5 s | 0,90 | Completa |
| 15 | 3 | 34.304 + 512 | 803,7 s | 1.496,3 s | 0,74 | Completa |
| 16 | 1 | 32.768 + 512 | 175,1 s | 593,4 s | 1,22 | Completa |
| 16 | 2 | 33.536 + 512 | 859,5 s | 1.398,7 s | 0,95 | Completa |
| 16 | 3 | 34.304 + 512 | 898,4 s | 1.587,6 s | 0,74 | Completa |
| 17 | 1 | 32.768 + 512 | 46,5 s | 423,6 s | 1,36 | Completa |
| 17 | 2 | 33.536 + 512 | 781,7 s | 1.345,5 s | 0,91 | Completa |
| 17 | 3 | 34.304 + 512 | 810,9 s | 1.480,2 s | 0,76 | Completa |
| 18 | 1 | 32.768 + 512 | 695,8 s | 1.239,2 s | 0,94 | Completa |
| 18 | 2 | 33.536 + 512 | 817,7 s | 1.378,2 s | 0,91 | Completa |
| 18 | 3 | 34.304 + 512 | 965,4 s | 1.558,7 s | 0,86 | Completa |
| 19 | 1 | 32.768 + 512 | 426,1 s | 985,9 s | 0,91 | Completa |
| 19 | 2 | 33.536 + 512 | 752,5 s | 1.321,9 s | 0,90 | Completa |
| 19 | 3 | 34.304 + 512 | 829,8 s | 1.525,6 s | 0,73 | Completa |
| 20 | 1 | 32.768 + 512 | 630,2 s | 1.196,6 s | 0,90 | Completa |
| 20 | 2 | 33.536 + 512 | 800,8 s | 1.346,3 s | 0,94 | Completa |
| 20 | 3 | 34.304 + 512 | 1.000,9 s | 1.628,8 s | 0,81 | Completa |
| 21 | 1 | 32.768 + 512 | 861,7 s | 1.413,3 s | 0,93 | Completa |
| 21 | 2 | 33.536 + 512 | 862,0 s | 1.466,9 s | 0,84 | Completa |
| 21 | 3 | 34.304 + 512 | 858,5 s | 1.311,2 s | 1,13 | Completa |
| 22 | 1 | 32.768 + 512 | 460,2 s | 1.020,4 s | 0,91 | Completa |
| 22 | 2 | 33.536 + 512 | 755,2 s | 1.324,6 s | 0,90 | Completa |
| 22 | 3 | 34.304 + 512 | 830,4 s | 1.526,7 s | 0,73 | Completa |
| 23 | 1 | 32.768 + 512 | 947,0 s | 1.486,2 s | 0,95 | Completa |
| 23 | 2 | 33.536 + 512 | 826,2 s | 1.431,4 s | 0,84 | Completa |
| 23 | 3 | 34.304 + 512 | 882,3 s | 1.279,0 s | 1,29 | Completa |
| 24 | 1 | 32.768 + 512 | 562,1 s | 1.126,3 s | 0,91 | Completa |
| 24 | 2 | 33.536 + 512 | 761,8 s | 1.332,9 s | 0,89 | Completa |
| 24 | 3 | 34.304 + 512 | 953,7 s | 1.587,6 s | 0,81 | Completa |
| 25 | 1 | 32.768 + 512 | 23,7 s | 390,2 s | 1,39 | Completa |
| 25 | 2 | 33.536 + 512 | 780,9 s | 1.343,7 s | 0,91 | Completa |
| 25 | 3 | 34.304 + 512 | 770,4 s | 1.402,2 s | 0,81 | Completa |
| 26 | 1 | 32.768 + 512 | 528,2 s | 1.090,7 s | 0,91 | Completa |
| 26 | 2 | 33.536 + 512 | 760,4 s | 1.332,0 s | 0,89 | Completa |
| 26 | 3 | 34.304 + 512 | 905,5 s | 1.549,3 s | 0,79 | Completa |
| 27 | 1 | 32.768 + 512 | 332,2 s | 758,9 s | 1,20 | Completa |
| 27 | 2 | 33.536 + 512 | 944,2 s | 1.513,9 s | 0,90 | Completa |
| 27 | 3 | 34.304 + 512 | 806,2 s | 1.501,2 s | 0,74 | Completa |
| 28 | 1 | 32.768 + 512 | 494,2 s | 1.055,2 s | 0,91 | Completa |
| 28 | 2 | 33.536 + 512 | 754,9 s | 1.325,2 s | 0,90 | Completa |
| 28 | 3 | 34.304 + 512 | 865,6 s | 1.567,1 s | 0,73 | Completa |
| 29 | 1 | 32.768 + 512 | 761,5 s | 1.309,3 s | 0,93 | Completa |
| 29 | 2 | 33.536 + 512 | 892,4 s | 1.497,2 s | 0,84 | Completa |
| 29 | 3 | 34.304 + 512 | 854,4 s | 1.377,8 s | 0,98 | Completa |
| 30 | 1 | 32.768 + 512 | 147,1 s | 559,4 s | 1,24 | Completa |
| 30 | 2 | 33.536 + 512 | 828,4 s | 1.368,5 s | 0,95 | Completa |
| 30 | 3 | 34.304 + 512 | 925,2 s | 1.613,1 s | 0,74 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
