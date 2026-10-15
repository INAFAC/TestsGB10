# 20 usuarios · 70% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Peticiones sin error: **60/60**. Respuestas con contenido visible: **60/60**. Peticiones terminadas por el modelo: **54/60**. Tiempo de la prueba: **2.213,4 s**.

Límite impuesto al servidor: **32 activas**. Cada persona espera 30 s tras su respuesta y conserva los mensajes reales anteriores. El historial inicial se aproxima al objetivo; la tabla muestra los tokens realmente enviados en cada turno.

Control mediante `/v1/chat/completions`, con conversaciones ficticias en español. Modo de razonamiento: **desactivado**. Cada respuesta puede terminar antes del límite de 512 tokens. Se distinguen primer texto del modelo, respuesta visible y finalización natural. No es una evaluación de calidad semántica.

## Resultado por turno

| Turno | Peticiones sin error | Espera mediana | Espera del 95% | Peor espera | Fin de petición del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 268,3 s | 598,8 s | 631,2 s | 1.043,1 s | 0,73 tokens/s | No cumple |
| 2 | 20/20 | 315,1 s | 362,2 s | 367,2 s | 927,3 s | 0,70 tokens/s | No cumple |
| 3 | 20/20 | 302,9 s | 353,9 s | 389,9 s | 672,7 s | 0,64 tokens/s | No cumple |

### Respuesta visible y finalización natural

| Turno | Respuestas con contenido visible | Terminaron sin alcanzar el límite de salida | Espera p95 al contenido visible |
|---|---:|---:|---:|
| 1 | 20/20 | 19/20 | 598,8 s |
| 2 | 20/20 | 15/20 | 362,2 s |
| 3 | 20/20 | 20/20 | 353,9 s |

En este control, cumplir la referencia requiere además que todas las respuestas tengan contenido visible antes de 5 s (p95) y terminen naturalmente. Alcanzar el límite de salida conserva la medición, pero no se presenta como una respuesta terminada naturalmente.

Que el modelo termine la petición por sí mismo (`stop`) no garantiza que haya entregado una respuesta visible: puede haber generado solo razonamiento. Por eso se muestran ambos recuentos. La velocidad incluye todos los tokens de salida, también los de razonamiento; no equivale necesariamente a la velocidad del texto que lee la persona.

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 305,1 s |
| Tiempo medio hasta fin de petición | 666,8 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,8% |
| Menor memoria disponible | 29,46 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 13 / 13 |
| Máximo en cola | 19 |
| Recálculos | 8 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 8,70 |
| Suma de tiempos individuales | 40.008,9 s |
| Tiempo total de la prueba, incluyendo pausas | 2.213,4 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 274,2 s | 710,9 s | 2.192,9 s | 0,59 |
| 2 | 3/3 | 318,0 s | 710,1 s | 2.190,3 s | 0,52 |
| 3 | 3/3 | 309,2 s | 714,5 s | 2.203,6 s | 0,54 |
| 4 | 3/3 | 230,3 s | 669,5 s | 2.068,8 s | 0,52 |
| 5 | 3/3 | 377,4 s | 707,5 s | 2.182,7 s | 0,39 |
| 6 | 3/3 | 355,2 s | 687,4 s | 2.122,3 s | 0,39 |
| 7 | 3/3 | 274,2 s | 615,5 s | 1.906,5 s | 0,48 |
| 8 | 3/3 | 250,8 s | 698,0 s | 2.154,1 s | 0,52 |
| 9 | 3/3 | 238,0 s | 535,9 s | 1.667,7 s | 0,47 |
| 10 | 3/3 | 352,3 s | 709,6 s | 2.189,0 s | 0,48 |
| 11 | 3/3 | 246,6 s | 608,1 s | 1.884,4 s | 0,47 |
| 12 | 3/3 | 356,3 s | 703,4 s | 2.170,4 s | 0,38 |
| 13 | 3/3 | 331,7 s | 703,0 s | 2.169,0 s | 0,45 |
| 14 | 3/3 | 329,0 s | 627,4 s | 1.942,2 s | 0,40 |
| 15 | 3/3 | 234,7 s | 590,8 s | 1.832,5 s | 0,47 |
| 16 | 3/3 | 405,8 s | 709,7 s | 2.189,2 s | 0,39 |
| 17 | 3/3 | 286,5 s | 560,1 s | 1.740,3 s | 0,41 |
| 18 | 3/3 | 309,2 s | 705,5 s | 2.176,6 s | 0,50 |
| 19 | 3/3 | 331,4 s | 713,1 s | 2.199,5 s | 0,49 |
| 20 | 3/3 | 291,9 s | 656,4 s | 2.029,3 s | 0,46 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Espera a respuesta visible | Fin de petición | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 512 | 236,5 s | 236,5 s | 842,3 s | 0,84 | Alcanzó el límite de salida |
| 1 | 2 | 33.312 + 512 | 312,2 s | 312,2 s | 824,2 s | 1,00 | Alcanzó el límite de salida |
| 1 | 3 | 33.853 + 271 | 273,8 s | 273,8 s | 466,3 s | 1,40 | Terminó naturalmente |
| 2 | 1 | 32.768 + 349 | 381,7 s | 381,7 s | 820,7 s | 0,79 | Terminó naturalmente |
| 2 | 2 | 33.148 + 512 | 299,2 s | 299,2 s | 812,7 s | 0,99 | Alcanzó el límite de salida |
| 2 | 3 | 33.688 + 271 | 273,1 s | 273,1 s | 496,7 s | 1,21 | Terminó naturalmente |
| 3 | 1 | 32.768 + 420 | 457,4 s | 457,4 s | 993,9 s | 0,78 | Terminó naturalmente |
| 3 | 2 | 33.219 + 483 | 314,9 s | 314,9 s | 927,3 s | 0,79 | Terminó naturalmente |
| 3 | 3 | 33.730 + 296 | 155,3 s | 155,3 s | 222,3 s | 4,40 | Terminó naturalmente |
| 4 | 1 | 32.768 + 350 | 47,3 s | 47,3 s | 422,9 s | 0,93 | Terminó naturalmente |
| 4 | 2 | 33.149 + 512 | 289,8 s | 289,8 s | 897,4 s | 0,84 | Alcanzó el límite de salida |
| 4 | 3 | 33.690 + 216 | 353,9 s | 353,9 s | 688,4 s | 0,64 | Terminó naturalmente |
| 5 | 1 | 32.768 + 346 | 565,4 s | 565,4 s | 1.027,8 s | 0,75 | Terminó naturalmente |
| 5 | 2 | 33.145 + 356 | 315,1 s | 315,1 s | 728,8 s | 0,86 | Terminó naturalmente |
| 5 | 3 | 33.529 + 153 | 251,6 s | 251,6 s | 365,9 s | 1,33 | Terminó naturalmente |
| 6 | 1 | 32.768 + 355 | 499,2 s | 499,2 s | 972,4 s | 0,75 | Terminó naturalmente |
| 6 | 2 | 33.154 + 293 | 277,3 s | 277,3 s | 511,6 s | 1,25 | Terminó naturalmente |
| 6 | 3 | 33.475 + 186 | 289,2 s | 289,2 s | 578,1 s | 0,64 | Terminó naturalmente |
| 7 | 1 | 32.768 + 335 | 148,5 s | 148,5 s | 490,3 s | 0,98 | Terminó naturalmente |
| 7 | 2 | 33.134 + 404 | 346,8 s | 346,8 s | 781,9 s | 0,93 | Terminó naturalmente |
| 7 | 3 | 33.566 + 176 | 327,4 s | 327,4 s | 574,1 s | 0,71 | Terminó naturalmente |
| 8 | 1 | 32.768 + 469 | 96,0 s | 96,0 s | 632,0 s | 0,87 | Terminó naturalmente |
| 8 | 2 | 33.268 + 493 | 349,4 s | 349,4 s | 902,6 s | 0,89 | Terminó naturalmente |
| 8 | 3 | 33.789 + 162 | 307,2 s | 307,2 s | 559,4 s | 0,64 | Terminó naturalmente |
| 9 | 1 | 32.768 + 292 | 71,3 s | 71,3 s | 385,1 s | 0,93 | Terminó naturalmente |
| 9 | 2 | 33.091 + 280 | 288,9 s | 288,9 s | 667,9 s | 0,74 | Terminó naturalmente |
| 9 | 3 | 33.399 + 220 | 353,9 s | 353,9 s | 554,7 s | 1,09 | Terminó naturalmente |
| 10 | 1 | 32.768 + 313 | 532,3 s | 532,3 s | 937,5 s | 0,77 | Terminó naturalmente |
| 10 | 2 | 33.112 + 512 | 250,7 s | 250,7 s | 761,7 s | 1,00 | Alcanzó el límite de salida |
| 10 | 3 | 33.653 + 219 | 274,1 s | 274,1 s | 429,7 s | 1,40 | Terminó naturalmente |
| 11 | 1 | 32.768 + 339 | 121,6 s | 121,6 s | 463,7 s | 0,99 | Terminó naturalmente |
| 11 | 2 | 33.138 + 336 | 283,5 s | 283,5 s | 759,8 s | 0,70 | Terminó naturalmente |
| 11 | 3 | 33.502 + 212 | 334,8 s | 334,8 s | 600,9 s | 0,79 | Terminó naturalmente |
| 12 | 1 | 32.768 + 259 | 419,7 s | 419,7 s | 739,1 s | 0,81 | Terminó naturalmente |
| 12 | 2 | 33.058 + 322 | 346,4 s | 346,4 s | 698,6 s | 0,91 | Terminó naturalmente |
| 12 | 3 | 33.408 + 248 | 302,9 s | 302,9 s | 672,7 s | 0,67 | Terminó naturalmente |
| 13 | 1 | 32.768 + 333 | 333,7 s | 333,7 s | 668,7 s | 0,99 | Terminó naturalmente |
| 13 | 2 | 33.132 + 446 | 347,5 s | 347,5 s | 824,2 s | 0,93 | Terminó naturalmente |
| 13 | 3 | 33.606 + 197 | 314,0 s | 314,0 s | 616,0 s | 0,65 | Terminó naturalmente |
| 14 | 1 | 32.767 + 307 | 268,3 s | 268,3 s | 578,3 s | 0,99 | Terminó naturalmente |
| 14 | 2 | 33.105 + 307 | 367,2 s | 367,2 s | 709,1 s | 0,89 | Terminó naturalmente |
| 14 | 3 | 33.440 + 157 | 351,5 s | 351,5 s | 594,6 s | 0,64 | Terminó naturalmente |
| 15 | 1 | 32.768 + 296 | 24,2 s | 24,2 s | 347,2 s | 0,91 | Terminó naturalmente |
| 15 | 2 | 33.095 + 341 | 289,9 s | 289,9 s | 753,1 s | 0,73 | Terminó naturalmente |
| 15 | 3 | 33.464 + 221 | 389,9 s | 389,9 s | 672,1 s | 0,78 | Terminó naturalmente |
| 16 | 1 | 32.768 + 313 | 631,2 s | 631,2 s | 1.043,1 s | 0,76 | Terminó naturalmente |
| 16 | 2 | 33.112 + 356 | 334,0 s | 334,0 s | 746,1 s | 0,86 | Terminó naturalmente |
| 16 | 3 | 33.496 + 178 | 252,3 s | 252,3 s | 339,8 s | 2,02 | Terminó naturalmente |
| 17 | 1 | 32.768 + 290 | 205,9 s | 205,9 s | 485,3 s | 1,03 | Terminó naturalmente |
| 17 | 2 | 33.089 + 279 | 317,0 s | 317,0 s | 703,8 s | 0,72 | Terminó naturalmente |
| 17 | 3 | 33.396 + 140 | 336,5 s | 336,5 s | 491,1 s | 0,90 | Terminó naturalmente |
| 18 | 1 | 32.768 + 384 | 301,3 s | 301,3 s | 705,3 s | 0,95 | Terminó naturalmente |
| 18 | 2 | 33.183 + 512 | 345,8 s | 345,8 s | 888,5 s | 0,94 | Alcanzó el límite de salida |
| 18 | 3 | 33.724 + 199 | 280,5 s | 280,5 s | 522,7 s | 0,82 | Terminó naturalmente |
| 19 | 1 | 32.768 + 376 | 598,8 s | 598,8 s | 1.112,5 s | 0,73 | Terminó naturalmente |
| 19 | 2 | 33.175 + 471 | 360,3 s | 360,3 s | 960,6 s | 0,78 | Terminó naturalmente |
| 19 | 3 | 33.674 + 231 | 35,0 s | 35,0 s | 66,2 s | 7,37 | Terminó naturalmente |
| 20 | 1 | 32.767 + 343 | 176,6 s | 176,6 s | 535,7 s | 0,95 | Terminó naturalmente |
| 20 | 2 | 33.141 + 425 | 362,2 s | 362,2 s | 833,8 s | 0,90 | Terminó naturalmente |
| 20 | 3 | 33.594 + 170 | 337,0 s | 337,0 s | 599,7 s | 0,64 | Terminó naturalmente |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
