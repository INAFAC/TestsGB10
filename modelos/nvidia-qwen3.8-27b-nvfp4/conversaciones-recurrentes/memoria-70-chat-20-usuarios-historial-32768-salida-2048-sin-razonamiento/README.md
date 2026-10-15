# 20 usuarios · 70% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Peticiones sin error: **60/60**. Respuestas con contenido visible: **60/60**. Peticiones terminadas por el modelo: **60/60**. Tiempo de la prueba: **2.328,1 s**.

Límite impuesto al servidor: **32 activas**. Cada persona espera 30 s tras su respuesta y conserva los mensajes reales anteriores. El historial inicial se aproxima al objetivo; la tabla muestra los tokens realmente enviados en cada turno.

Control mediante `/v1/chat/completions`, con conversaciones ficticias en español. Modo de razonamiento: **desactivado**. Cada respuesta puede terminar antes del límite de 2048 tokens. Se distinguen primer texto del modelo, respuesta visible y finalización natural. No es una evaluación de calidad semántica.

## Resultado por turno

| Turno | Peticiones sin error | Espera mediana | Espera del 95% | Peor espera | Fin de petición del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 267,1 s | 591,4 s | 621,9 s | 1.124,1 s | 0,66 tokens/s | No cumple |
| 2 | 20/20 | 335,7 s | 470,5 s | 503,8 s | 1.088,7 s | 0,65 tokens/s | No cumple |
| 3 | 20/20 | 266,5 s | 330,8 s | 352,1 s | 569,5 s | 0,64 tokens/s | No cumple |

### Respuesta visible y finalización natural

| Turno | Respuestas con contenido visible | Terminaron sin alcanzar el límite de salida | Espera p95 al contenido visible |
|---|---:|---:|---:|
| 1 | 20/20 | 20/20 | 591,4 s |
| 2 | 20/20 | 20/20 | 470,5 s |
| 3 | 20/20 | 20/20 | 330,8 s |

En este control, cumplir la referencia requiere además que todas las respuestas tengan contenido visible antes de 5 s (p95) y terminen naturalmente. Alcanzar el límite de salida conserva la medición, pero no se presenta como una respuesta terminada naturalmente.

Que el modelo termine la petición por sí mismo (`stop`) no garantiza que haya entregado una respuesta visible: puede haber generado solo razonamiento. Por eso se muestran ambos recuentos. La velocidad incluye todos los tokens de salida, también los de razonamiento; no equivale necesariamente a la velocidad del texto que lee la persona.

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 295,7 s |
| Tiempo medio hasta fin de petición | 672,7 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,9% |
| Menor memoria disponible | 29,27 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 14 / 14 |
| Máximo en cola | 19 |
| Recálculos | 18 |
| Tokens recuperados de caché | 18.032 |
| Tokens/s de todo el grupo, incluyendo pausas | 8,67 |
| Suma de tiempos individuales | 40.361,3 s |
| Tiempo total de la prueba, incluyendo pausas | 2.328,1 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 235,0 s | 624,8 s | 1.934,5 s | 0,52 |
| 2 | 3/3 | 259,1 s | 605,2 s | 1.875,7 s | 0,47 |
| 3 | 3/3 | 222,0 s | 704,6 s | 2.173,8 s | 0,55 |
| 4 | 3/3 | 329,7 s | 626,3 s | 1.939,0 s | 0,44 |
| 5 | 3/3 | 337,5 s | 724,8 s | 2.234,5 s | 0,48 |
| 6 | 3/3 | 214,9 s | 584,1 s | 1.812,4 s | 0,53 |
| 7 | 3/3 | 319,4 s | 752,4 s | 2.317,3 s | 0,59 |
| 8 | 3/3 | 377,9 s | 705,2 s | 2.175,7 s | 0,41 |
| 9 | 3/3 | 219,6 s | 493,2 s | 1.539,7 s | 0,47 |
| 10 | 3/3 | 306,2 s | 671,4 s | 2.074,4 s | 0,45 |
| 11 | 3/3 | 288,4 s | 646,5 s | 1.999,5 s | 0,49 |
| 12 | 3/3 | 374,3 s | 706,2 s | 2.178,7 s | 0,41 |
| 13 | 3/3 | 342,2 s | 718,4 s | 2.215,2 s | 0,44 |
| 14 | 3/3 | 387,0 s | 710,6 s | 2.192,0 s | 0,38 |
| 15 | 3/3 | 345,9 s | 695,3 s | 2.146,0 s | 0,37 |
| 16 | 3/3 | 346,0 s | 725,3 s | 2.236,1 s | 0,50 |
| 17 | 3/3 | 205,6 s | 570,2 s | 1.770,6 s | 0,51 |
| 18 | 3/3 | 174,8 s | 726,2 s | 2.238,7 s | 0,69 |
| 19 | 3/3 | 301,9 s | 732,4 s | 2.257,4 s | 0,52 |
| 20 | 3/3 | 326,4 s | 730,9 s | 2.253,0 s | 0,48 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Espera a respuesta visible | Fin de petición | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 320 | 147,3 s | 147,3 s | 442,9 s | 1,08 | Terminó naturalmente |
| 1 | 2 | 33.119 + 427 | 280,4 s | 280,4 s | 905,5 s | 0,68 | Terminó naturalmente |
| 1 | 3 | 33.574 + 250 | 277,3 s | 277,3 s | 526,0 s | 1,00 | Terminó naturalmente |
| 2 | 1 | 32.768 + 328 | 175,3 s | 175,3 s | 488,1 s | 1,05 | Terminó naturalmente |
| 2 | 2 | 33.128 + 327 | 343,0 s | 343,0 s | 843,6 s | 0,65 | Terminó naturalmente |
| 2 | 3 | 33.483 + 235 | 259,0 s | 259,0 s | 483,8 s | 1,04 | Terminó naturalmente |
| 3 | 1 | 32.768 + 431 | 24,2 s | 24,2 s | 452,5 s | 1,00 | Terminó naturalmente |
| 3 | 2 | 33.230 + 574 | 335,7 s | 335,7 s | 1.088,7 s | 0,76 | Terminó naturalmente |
| 3 | 3 | 33.832 + 201 | 306,1 s | 306,1 s | 572,5 s | 0,75 | Terminó naturalmente |
| 4 | 1 | 32.768 + 297 | 300,0 s | 300,0 s | 567,5 s | 1,11 | Terminó naturalmente |
| 4 | 2 | 33.096 + 368 | 445,0 s | 445,0 s | 887,9 s | 0,83 | Terminó naturalmente |
| 4 | 3 | 33.492 + 185 | 244,2 s | 244,2 s | 423,5 s | 1,03 | Terminó naturalmente |
| 5 | 1 | 32.768 + 340 | 498,5 s | 498,5 s | 992,9 s | 0,69 | Terminó naturalmente |
| 5 | 2 | 33.139 + 524 | 302,2 s | 302,2 s | 870,0 s | 0,92 | Terminó naturalmente |
| 5 | 3 | 33.691 + 212 | 211,8 s | 211,8 s | 311,6 s | 2,11 | Terminó naturalmente |
| 6 | 1 | 32.768 + 333 | 120,4 s | 120,4 s | 430,9 s | 1,07 | Terminó naturalmente |
| 6 | 2 | 33.132 + 389 | 257,8 s | 257,8 s | 826,3 s | 0,68 | Terminó naturalmente |
| 6 | 3 | 33.549 + 237 | 266,5 s | 266,5 s | 495,0 s | 1,03 | Terminó naturalmente |
| 7 | 1 | 32.768 + 386 | 591,4 s | 591,4 s | 1.176,6 s | 0,66 | Terminó naturalmente |
| 7 | 2 | 33.185 + 751 | 343,0 s | 343,0 s | 1.036,8 s | 1,08 | Terminó naturalmente |
| 7 | 3 | 33.964 + 220 | 23,9 s | 23,9 s | 43,7 s | 11,04 | Terminó naturalmente |
| 8 | 1 | 32.768 + 325 | 332,3 s | 332,3 s | 638,6 s | 1,06 | Terminó naturalmente |
| 8 | 2 | 33.125 + 365 | 470,5 s | 470,5 s | 910,6 s | 0,83 | Terminó naturalmente |
| 8 | 3 | 33.518 + 193 | 330,8 s | 330,8 s | 566,2 s | 0,82 | Terminó naturalmente |
| 9 | 1 | 32.768 + 302 | 94,8 s | 94,8 s | 390,1 s | 1,02 | Terminó naturalmente |
| 9 | 2 | 33.100 + 260 | 265,5 s | 265,5 s | 650,4 s | 0,67 | Terminó naturalmente |
| 9 | 3 | 33.388 + 158 | 298,6 s | 298,6 s | 439,0 s | 1,12 | Terminó naturalmente |
| 10 | 1 | 32.768 + 318 | 235,2 s | 235,2 s | 536,6 s | 1,05 | Terminó naturalmente |
| 10 | 2 | 33.117 + 416 | 440,0 s | 440,0 s | 966,0 s | 0,79 | Terminó naturalmente |
| 10 | 3 | 33.561 + 198 | 243,5 s | 243,5 s | 511,7 s | 0,73 | Terminó naturalmente |
| 11 | 1 | 32.768 + 312 | 204,7 s | 204,7 s | 496,2 s | 1,07 | Terminó naturalmente |
| 11 | 2 | 33.111 + 403 | 390,5 s | 390,5 s | 892,7 s | 0,80 | Terminó naturalmente |
| 11 | 3 | 33.542 + 271 | 270,1 s | 270,1 s | 550,5 s | 0,96 | Terminó naturalmente |
| 12 | 1 | 32.768 + 320 | 267,1 s | 267,1 s | 570,4 s | 1,05 | Terminó naturalmente |
| 12 | 2 | 33.120 + 415 | 503,8 s | 503,8 s | 1.024,4 s | 0,80 | Terminó naturalmente |
| 12 | 3 | 33.563 + 169 | 352,1 s | 352,1 s | 523,8 s | 0,98 | Terminó naturalmente |
| 13 | 1 | 32.768 + 346 | 387,0 s | 387,0 s | 822,9 s | 0,79 | Terminó naturalmente |
| 13 | 2 | 33.145 + 373 | 322,1 s | 322,1 s | 771,7 s | 0,83 | Terminó naturalmente |
| 13 | 3 | 33.546 + 256 | 317,5 s | 317,5 s | 560,4 s | 1,05 | Terminó naturalmente |
| 14 | 1 | 32.767 + 312 | 561,4 s | 561,4 s | 1.016,8 s | 0,68 | Terminó naturalmente |
| 14 | 2 | 33.110 + 325 | 313,3 s | 313,3 s | 676,9 s | 0,89 | Terminó naturalmente |
| 14 | 3 | 33.463 + 193 | 286,2 s | 286,2 s | 438,1 s | 1,26 | Terminó naturalmente |
| 15 | 1 | 32.768 + 293 | 466,0 s | 466,0 s | 880,2 s | 0,70 | Terminó naturalmente |
| 15 | 2 | 33.092 + 303 | 300,3 s | 300,3 s | 636,1 s | 0,90 | Terminó naturalmente |
| 15 | 3 | 33.423 + 191 | 271,4 s | 271,4 s | 569,5 s | 0,64 | Terminó naturalmente |
| 16 | 1 | 32.768 + 351 | 424,7 s | 424,7 s | 890,1 s | 0,75 | Terminó naturalmente |
| 16 | 2 | 33.150 + 522 | 361,8 s | 361,8 s | 899,2 s | 0,97 | Terminó naturalmente |
| 16 | 3 | 33.702 + 244 | 251,6 s | 251,6 s | 386,6 s | 1,80 | Terminó naturalmente |
| 17 | 1 | 32.768 + 307 | 46,9 s | 46,9 s | 352,5 s | 1,00 | Terminó naturalmente |
| 17 | 2 | 33.106 + 433 | 271,3 s | 271,3 s | 907,5 s | 0,68 | Terminó naturalmente |
| 17 | 3 | 33.567 + 163 | 298,6 s | 298,6 s | 450,5 s | 1,07 | Terminó naturalmente |
| 18 | 1 | 32.768 + 443 | 70,4 s | 70,4 s | 535,3 s | 0,95 | Terminó naturalmente |
| 18 | 2 | 33.242 + 882 | 387,6 s | 387,6 s | 1.506,1 s | 0,79 | Terminó naturalmente |
| 18 | 3 | 34.152 + 220 | 66,3 s | 66,3 s | 137,2 s | 3,09 | Terminó naturalmente |
| 19 | 1 | 32.768 + 397 | 530,3 s | 530,3 s | 1.124,1 s | 0,67 | Terminó naturalmente |
| 19 | 2 | 33.196 + 496 | 360,8 s | 360,8 s | 999,7 s | 0,77 | Terminó naturalmente |
| 19 | 3 | 33.720 + 289 | 14,5 s | 14,5 s | 73,4 s | 4,88 | Terminó naturalmente |
| 20 | 1 | 32.767 + 319 | 621,9 s | 621,9 s | 1.099,2 s | 0,67 | Terminó naturalmente |
| 20 | 2 | 33.117 + 544 | 328,0 s | 328,0 s | 1.038,8 s | 0,76 | Terminó naturalmente |
| 20 | 3 | 33.689 + 218 | 29,2 s | 29,2 s | 54,8 s | 8,47 | Terminó naturalmente |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
