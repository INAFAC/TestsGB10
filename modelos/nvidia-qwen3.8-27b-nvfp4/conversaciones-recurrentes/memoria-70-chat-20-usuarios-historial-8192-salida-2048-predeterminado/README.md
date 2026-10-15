# 20 usuarios · 70% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Peticiones sin error: **60/60**. Respuestas con contenido visible: **57/60**. Peticiones terminadas por el modelo: **57/60**. Tiempo de la prueba: **578,6 s**.

Límite impuesto al servidor: **32 activas**. Cada persona espera 30 s tras su respuesta y conserva los mensajes reales anteriores. El historial inicial se aproxima al objetivo; la tabla muestra los tokens realmente enviados en cada turno.

Control mediante `/v1/chat/completions`, con conversaciones ficticias en español. Modo de razonamiento: **predeterminado del servidor**. Cada respuesta puede terminar antes del límite de 2048 tokens. Se distinguen primer texto del modelo, respuesta visible y finalización natural. No es una evaluación de calidad semántica.

## Resultado por turno

| Turno | Peticiones sin error | Espera mediana | Espera del 95% | Peor espera | Fin de petición del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 51,8 s | 103,3 s | 108,0 s | 408,4 s | 2,96 tokens/s | No cumple |
| 2 | 20/20 | 1,3 s | 3,0 s | 3,5 s | 98,5 s | 6,26 tokens/s | No cumple |
| 3 | 20/20 | 0,8 s | 1,0 s | 1,1 s | 44,0 s | 6,15 tokens/s | No cumple |

### Respuesta visible y finalización natural

| Turno | Respuestas con contenido visible | Terminaron sin alcanzar el límite de salida | Espera p95 al contenido visible |
|---|---:|---:|---:|
| 1 | 17/20 | 17/20 | 383,8 s |
| 2 | 20/20 | 20/20 | 72,1 s |
| 3 | 20/20 | 20/20 | 26,0 s |

En este control, cumplir la referencia requiere además que todas las respuestas tengan contenido visible antes de 5 s (p95) y terminen naturalmente. Alcanzar el límite de salida conserva la medición, pero no se presenta como una respuesta terminada naturalmente.

Que el modelo termine la petición por sí mismo (`stop`) no garantiza que haya entregado una respuesta visible: puede haber generado solo razonamiento. Por eso se muestran ambos recuentos. La velocidad incluye todos los tokens de salida, también los de razonamiento; no equivale necesariamente a la velocidad del texto que lee la persona.

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 19,4 s |
| Tiempo medio hasta fin de petición | 124,7 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,7% |
| Menor memoria disponible | 29,52 GiB |
| Pico de caché | 42,4% |
| Máximo activo / respuestas solapadas | 20 / 20 |
| Máximo en cola | 19 |
| Recálculos | 0 |
| Tokens recuperados de caché | 337.120 |
| Tokens/s de todo el grupo, incluyendo pausas | 64,45 |
| Suma de tiempos individuales | 7.481,9 s |
| Tiempo total de la prueba, incluyendo pausas | 578,6 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 12,8 s | 101,9 s | 365,8 s | 3,68 |
| 2 | 3/3 | 19,8 s | 136,0 s | 468,1 s | 4,45 |
| 3 | 3/3 | 23,5 s | 114,1 s | 402,4 s | 3,92 |
| 4 | 3/3 | 7,7 s | 93,5 s | 340,6 s | 3,43 |
| 5 | 3/3 | 21,6 s | 118,7 s | 416,2 s | 3,98 |
| 6 | 3/3 | 33,2 s | 125,1 s | 435,4 s | 4,18 |
| 7 | 3/3 | 25,4 s | 133,2 s | 459,7 s | 4,37 |
| 8 | 3/3 | 18,5 s | 172,0 s | 576,1 s | 5,42 |
| 9 | 3/3 | 31,1 s | 90,0 s | 330,0 s | 3,15 |
| 10 | 3/3 | 29,2 s | 161,2 s | 543,7 s | 4,98 |
| 11 | 3/3 | 6,2 s | 113,9 s | 401,7 s | 4,01 |
| 12 | 3/3 | 35,2 s | 120,5 s | 421,7 s | 4,03 |
| 13 | 3/3 | 16,8 s | 160,7 s | 542,1 s | 5,05 |
| 14 | 3/3 | 9,3 s | 107,4 s | 382,2 s | 3,81 |
| 15 | 3/3 | 14,5 s | 110,3 s | 391,0 s | 3,82 |
| 16 | 3/3 | 27,3 s | 166,6 s | 559,8 s | 5,22 |
| 17 | 3/3 | 4,5 s | 91,2 s | 333,7 s | 3,40 |
| 18 | 3/3 | 11,2 s | 124,7 s | 434,2 s | 4,29 |
| 19 | 3/3 | 2,9 s | 98,5 s | 355,5 s | 3,70 |
| 20 | 3/3 | 36,8 s | 154,4 s | 523,4 s | 4,82 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Espera a respuesta visible | Fin de petición | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 662 | 36,1 s | 173,1 s | 199,9 s | 4,04 | Terminó naturalmente |
| 1 | 2 | 8.883 + 491 | 1,3 s | 49,6 s | 76,4 s | 6,52 | Terminó naturalmente |
| 1 | 3 | 9.400 + 195 | 0,9 s | 7,7 s | 29,4 s | 6,80 | Terminó naturalmente |
| 2 | 1 | 8.192 + 1.477 | 57,2 s | 305,2 s | 331,5 s | 5,38 | Terminó naturalmente |
| 2 | 2 | 9.698 + 396 | 1,7 s | 35,4 s | 53,3 s | 7,66 | Terminó naturalmente |
| 2 | 3 | 10.120 + 212 | 0,6 s | 10,7 s | 23,2 s | 9,30 | Terminó naturalmente |
| 3 | 1 | 8.191 + 799 | 68,2 s | 190,4 s | 226,1 s | 5,06 | Terminó naturalmente |
| 3 | 2 | 9.019 + 490 | 1,2 s | 48,6 s | 78,0 s | 6,37 | Terminó naturalmente |
| 3 | 3 | 9.535 + 289 | 1,1 s | 20,0 s | 38,2 s | 7,75 | Terminó naturalmente |
| 4 | 1 | 8.192 + 532 | 21,2 s | 153,6 s | 178,5 s | 3,38 | Terminó naturalmente |
| 4 | 2 | 8.753 + 387 | 1,1 s | 38,3 s | 60,9 s | 6,45 | Terminó naturalmente |
| 4 | 3 | 9.166 + 249 | 0,7 s | 21,8 s | 41,1 s | 6,15 | Terminó naturalmente |
| 5 | 1 | 8.192 + 864 | 62,7 s | 208,4 s | 236,6 s | 4,96 | Terminó naturalmente |
| 5 | 2 | 9.085 + 628 | 1,2 s | 73,0 s | 98,5 s | 6,45 | Terminó naturalmente |
| 5 | 3 | 9.739 + 164 | 1,0 s | 5,3 s | 21,0 s | 8,13 | Terminó naturalmente |
| 6 | 1 | 8.192 + 1.099 | 97,3 s | 248,6 s | 276,3 s | 6,13 | Terminó naturalmente |
| 6 | 2 | 9.320 + 482 | 1,5 s | 48,3 s | 72,9 s | 6,73 | Terminó naturalmente |
| 6 | 3 | 9.828 + 240 | 0,8 s | 12,8 s | 26,1 s | 9,45 | Terminó naturalmente |
| 7 | 1 | 8.192 + 1.135 | 73,9 s | 252,5 s | 279,2 s | 5,52 | Terminó naturalmente |
| 7 | 2 | 9.356 + 556 | 1,4 s | 57,1 s | 81,3 s | 6,95 | Terminó naturalmente |
| 7 | 3 | 9.938 + 316 | 0,8 s | 26,0 s | 39,1 s | 8,23 | Terminó naturalmente |
| 8 | 1 | 8.192 + 2.048 | 51,8 s | — s | 408,4 s | 5,74 | Alcanzó el límite de salida; sin respuesta visible |
| 8 | 2 | 10.273 + 679 | 3,0 s | 55,8 s | 72,3 s | 9,79 | Terminó naturalmente |
| 8 | 3 | 10.978 + 397 | 0,7 s | 23,5 s | 35,4 s | 11,42 | Terminó naturalmente |
| 9 | 1 | 8.192 + 499 | 91,3 s | 160,5 s | 183,1 s | 5,42 | Terminó naturalmente |
| 9 | 2 | 8.720 + 303 | 1,1 s | 22,7 s | 47,8 s | 6,47 | Terminó naturalmente |
| 9 | 3 | 9.049 + 237 | 0,7 s | 16,8 s | 39,0 s | 6,17 | Terminó naturalmente |
| 10 | 1 | 8.192 + 1.996 | 85,4 s | 383,8 s | 405,9 s | 6,22 | Terminó naturalmente |
| 10 | 2 | 10.217 + 475 | 1,7 s | 40,9 s | 54,8 s | 8,92 | Terminó naturalmente |
| 10 | 3 | 10.718 + 237 | 0,5 s | 11,3 s | 22,9 s | 10,53 | Terminó naturalmente |
| 11 | 1 | 8.192 + 1.010 | 16,4 s | 224,9 s | 251,6 s | 4,29 | Terminó naturalmente |
| 11 | 2 | 9.231 + 378 | 1,3 s | 40,1 s | 60,7 s | 6,34 | Terminó naturalmente |
| 11 | 3 | 9.635 + 224 | 1,0 s | 14,0 s | 29,3 s | 7,90 | Terminó naturalmente |
| 12 | 1 | 8.192 + 901 | 103,3 s | 221,1 s | 247,3 s | 6,25 | Terminó naturalmente |
| 12 | 2 | 9.122 + 468 | 1,2 s | 52,4 s | 73,5 s | 6,46 | Terminó naturalmente |
| 12 | 3 | 9.616 + 330 | 1,0 s | 24,6 s | 40,8 s | 8,27 | Terminó naturalmente |
| 13 | 1 | 8.192 + 2.048 | 46,5 s | — s | 407,8 s | 5,67 | Alcanzó el límite de salida; sin respuesta visible |
| 13 | 2 | 10.273 + 426 | 3,5 s | 37,4 s | 49,0 s | 9,34 | Terminó naturalmente |
| 13 | 3 | 10.725 + 262 | 0,5 s | 13,3 s | 25,2 s | 10,54 | Terminó naturalmente |
| 14 | 1 | 8.192 + 519 | 26,1 s | 152,8 s | 177,3 s | 3,43 | Terminó naturalmente |
| 14 | 2 | 8.740 + 632 | 1,1 s | 72,1 s | 100,9 s | 6,33 | Terminó naturalmente |
| 14 | 3 | 9.398 + 304 | 0,8 s | 25,8 s | 44,0 s | 7,01 | Terminó naturalmente |
| 15 | 1 | 8.192 + 914 | 41,3 s | 212,8 s | 241,2 s | 4,57 | Terminó naturalmente |
| 15 | 2 | 9.135 + 341 | 1,3 s | 30,6 s | 55,6 s | 6,26 | Terminó naturalmente |
| 15 | 3 | 9.502 + 238 | 1,0 s | 19,7 s | 34,1 s | 7,14 | Terminó naturalmente |
| 16 | 1 | 8.191 + 2.048 | 79,6 s | — s | 411,4 s | 6,17 | Alcanzó el límite de salida; sin respuesta visible |
| 16 | 2 | 10.272 + 587 | 1,8 s | 47,8 s | 61,4 s | 9,83 | Terminó naturalmente |
| 16 | 3 | 10.885 + 286 | 0,5 s | 14,8 s | 27,0 s | 10,75 | Terminó naturalmente |
| 17 | 1 | 8.192 + 455 | 11,5 s | 143,4 s | 165,1 s | 2,96 | Terminó naturalmente |
| 17 | 2 | 8.676 + 369 | 1,2 s | 34,9 s | 58,6 s | 6,41 | Terminó naturalmente |
| 17 | 3 | 9.071 + 312 | 0,7 s | 28,7 s | 49,9 s | 6,33 | Terminó naturalmente |
| 18 | 1 | 8.192 + 1.134 | 31,1 s | 243,3 s | 273,0 s | 4,68 | Terminó naturalmente |
| 18 | 2 | 9.355 + 454 | 1,5 s | 44,7 s | 70,4 s | 6,57 | Terminó naturalmente |
| 18 | 3 | 9.835 + 276 | 0,9 s | 20,3 s | 30,7 s | 9,23 | Terminó naturalmente |
| 19 | 1 | 8.192 + 684 | 6,7 s | 177,8 s | 198,8 s | 3,56 | Terminó naturalmente |
| 19 | 2 | 8.905 + 429 | 1,2 s | 41,7 s | 67,0 s | 6,51 | Terminó naturalmente |
| 19 | 3 | 9.360 + 204 | 0,8 s | 13,5 s | 29,6 s | 7,05 | Terminó naturalmente |
| 20 | 1 | 8.191 + 1.788 | 108,0 s | 353,7 s | 382,8 s | 6,50 | Terminó naturalmente |
| 20 | 2 | 10.008 + 419 | 1,6 s | 35,3 s | 50,8 s | 8,49 | Terminó naturalmente |
| 20 | 3 | 10.453 + 318 | 0,8 s | 16,7 s | 29,7 s | 10,95 | Terminó naturalmente |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
