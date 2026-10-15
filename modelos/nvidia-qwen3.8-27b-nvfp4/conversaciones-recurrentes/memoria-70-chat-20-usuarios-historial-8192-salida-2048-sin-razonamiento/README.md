# 20 usuarios · 70% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Peticiones sin error: **60/60**. Respuestas con contenido visible: **60/60**. Peticiones terminadas por el modelo: **60/60**. Tiempo de la prueba: **504,5 s**.

Límite impuesto al servidor: **32 activas**. Cada persona espera 30 s tras su respuesta y conserva los mensajes reales anteriores. El historial inicial se aproxima al objetivo; la tabla muestra los tokens realmente enviados en cada turno.

Control mediante `/v1/chat/completions`, con conversaciones ficticias en español. Modo de razonamiento: **desactivado**. Cada respuesta puede terminar antes del límite de 2048 tokens. Se distinguen primer texto del modelo, respuesta visible y finalización natural. No es una evaluación de calidad semántica.

## Resultado por turno

| Turno | Peticiones sin error | Espera mediana | Espera del 95% | Peor espera | Fin de petición del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 51,9 s | 103,2 s | 108,0 s | 307,8 s | 2,31 tokens/s | No cumple |
| 2 | 20/20 | 0,8 s | 1,4 s | 2,2 s | 98,3 s | 5,87 tokens/s | No cumple |
| 3 | 20/20 | 1,0 s | 2,0 s | 2,2 s | 35,2 s | 6,39 tokens/s | No cumple |

### Respuesta visible y finalización natural

| Turno | Respuestas con contenido visible | Terminaron sin alcanzar el límite de salida | Espera p95 al contenido visible |
|---|---:|---:|---:|
| 1 | 20/20 | 20/20 | 103,2 s |
| 2 | 20/20 | 20/20 | 1,4 s |
| 3 | 20/20 | 20/20 | 2,0 s |

En este control, cumplir la referencia requiere además que todas las respuestas tengan contenido visible antes de 5 s (p95) y terminen naturalmente. Alcanzar el límite de salida conserva la medición, pero no se presenta como una respuesta terminada naturalmente.

Que el modelo termine la petición por sí mismo (`stop`) no garantiza que haya entregado una respuesta visible: puede haber generado solo razonamiento. Por eso se muestran ambos recuentos. La velocidad incluye todos los tokens de salida, también los de razonamiento; no equivale necesariamente a la velocidad del texto que lee la persona.

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 19,3 s |
| Tiempo medio hasta fin de petición | 92,3 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,8% |
| Menor memoria disponible | 29,47 GiB |
| Pico de caché | 41,7% |
| Máximo activo / respuestas solapadas | 20 / 20 |
| Máximo en cola | 19 |
| Recálculos | 0 |
| Tokens recuperados de caché | 320.656 |
| Tokens/s de todo el grupo, incluyendo pausas | 48,62 |
| Suma de tiempos individuales | 5.537,4 s |
| Tiempo total de la prueba, incluyendo pausas | 504,5 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 19,7 s | 94,7 s | 344,2 s | 3,87 |
| 2 | 3/3 | 35,3 s | 86,5 s | 319,6 s | 3,15 |
| 3 | 3/3 | 29,6 s | 84,8 s | 314,3 s | 3,08 |
| 4 | 3/3 | 9,2 s | 94,2 s | 342,5 s | 3,75 |
| 5 | 3/3 | 2,9 s | 87,6 s | 322,9 s | 3,47 |
| 6 | 3/3 | 27,3 s | 85,0 s | 315,2 s | 3,09 |
| 7 | 3/3 | 17,8 s | 88,2 s | 324,6 s | 3,35 |
| 8 | 3/3 | 36,8 s | 85,5 s | 316,7 s | 3,11 |
| 9 | 3/3 | 21,5 s | 93,5 s | 340,5 s | 3,55 |
| 10 | 3/3 | 32,9 s | 76,7 s | 290,1 s | 2,63 |
| 11 | 3/3 | 10,9 s | 82,9 s | 308,7 s | 3,12 |
| 12 | 3/3 | 23,3 s | 80,4 s | 301,4 s | 2,93 |
| 13 | 3/3 | 12,8 s | 119,5 s | 418,5 s | 4,86 |
| 14 | 3/3 | 14,5 s | 130,5 s | 451,7 s | 5,18 |
| 15 | 3/3 | 4,3 s | 74,6 s | 283,8 s | 2,95 |
| 16 | 3/3 | 25,2 s | 91,0 s | 333,1 s | 3,57 |
| 17 | 3/3 | 6,3 s | 147,4 s | 502,2 s | 5,69 |
| 18 | 3/3 | 31,3 s | 82,1 s | 306,5 s | 2,89 |
| 19 | 3/3 | 16,1 s | 78,1 s | 294,5 s | 2,88 |
| 20 | 3/3 | 7,7 s | 82,6 s | 307,8 s | 3,13 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Espera a respuesta visible | Fin de petición | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.191 + 516 | 57,2 s | 57,2 s | 171,9 s | 4,49 | Terminó naturalmente |
| 1 | 2 | 8.738 + 560 | 1,2 s | 1,2 s | 83,6 s | 6,79 | Terminó naturalmente |
| 1 | 3 | 9.326 + 256 | 0,6 s | 0,6 s | 28,7 s | 9,07 | Terminó naturalmente |
| 2 | 1 | 8.192 + 330 | 103,2 s | 103,2 s | 156,9 s | 6,12 | Terminó naturalmente |
| 2 | 2 | 8.553 + 447 | 0,7 s | 0,7 s | 69,5 s | 6,48 | Terminó naturalmente |
| 2 | 3 | 9.028 + 229 | 2,0 s | 2,0 s | 33,1 s | 7,34 | Terminó naturalmente |
| 3 | 1 | 8.192 + 329 | 85,4 s | 85,4 s | 155,1 s | 4,71 | Terminó naturalmente |
| 3 | 2 | 8.552 + 451 | 1,1 s | 1,1 s | 71,2 s | 6,43 | Terminó naturalmente |
| 3 | 3 | 9.031 + 187 | 2,2 s | 2,2 s | 28,0 s | 7,21 | Terminó naturalmente |
| 4 | 1 | 8.191 + 436 | 26,1 s | 26,1 s | 160,9 s | 3,23 | Terminó naturalmente |
| 4 | 2 | 8.658 + 639 | 1,1 s | 1,1 s | 98,3 s | 6,56 | Terminó naturalmente |
| 4 | 3 | 9.325 + 208 | 0,6 s | 0,6 s | 23,3 s | 9,12 | Terminó naturalmente |
| 5 | 1 | 8.192 + 391 | 6,7 s | 6,7 s | 153,5 s | 2,66 | Terminó naturalmente |
| 5 | 2 | 8.614 + 572 | 0,7 s | 0,7 s | 88,4 s | 6,51 | Terminó naturalmente |
| 5 | 3 | 9.214 + 158 | 1,1 s | 1,1 s | 20,9 s | 7,93 | Terminó naturalmente |
| 6 | 1 | 8.192 + 337 | 79,6 s | 79,6 s | 155,5 s | 4,43 | Terminó naturalmente |
| 6 | 2 | 8.560 + 394 | 1,2 s | 1,2 s | 63,6 s | 6,29 | Terminó naturalmente |
| 6 | 3 | 8.982 + 243 | 1,1 s | 1,1 s | 36,0 s | 6,93 | Terminó naturalmente |
| 7 | 1 | 8.192 + 326 | 51,9 s | 51,9 s | 150,7 s | 3,29 | Terminó naturalmente |
| 7 | 2 | 8.549 + 553 | 0,6 s | 0,6 s | 86,1 s | 6,46 | Terminó naturalmente |
| 7 | 3 | 9.130 + 209 | 1,1 s | 1,1 s | 27,8 s | 7,80 | Terminó naturalmente |
| 8 | 1 | 8.192 + 350 | 108,0 s | 108,0 s | 159,7 s | 6,75 | Terminó naturalmente |
| 8 | 2 | 8.573 + 427 | 0,8 s | 0,8 s | 66,1 s | 6,53 | Terminó naturalmente |
| 8 | 3 | 9.028 + 207 | 1,7 s | 1,7 s | 30,9 s | 7,04 | Terminó naturalmente |
| 9 | 1 | 8.191 + 334 | 62,7 s | 62,7 s | 153,2 s | 3,68 | Terminó naturalmente |
| 9 | 2 | 8.556 + 644 | 0,8 s | 0,8 s | 100,2 s | 6,47 | Terminó naturalmente |
| 9 | 3 | 9.228 + 230 | 1,1 s | 1,1 s | 27,1 s | 8,82 | Terminó naturalmente |
| 10 | 1 | 8.192 + 295 | 97,2 s | 97,2 s | 151,9 s | 5,38 | Terminó naturalmente |
| 10 | 2 | 8.518 + 277 | 0,5 s | 0,5 s | 47,5 s | 5,87 | Terminó naturalmente |
| 10 | 3 | 8.823 + 191 | 0,9 s | 0,9 s | 30,6 s | 6,40 | Terminó naturalmente |
| 11 | 1 | 8.192 + 334 | 31,1 s | 31,1 s | 148,9 s | 2,83 | Terminó naturalmente |
| 11 | 2 | 8.557 + 423 | 0,5 s | 0,5 s | 68,2 s | 6,23 | Terminó naturalmente |
| 11 | 3 | 9.008 + 205 | 1,0 s | 1,0 s | 31,5 s | 6,69 | Terminó naturalmente |
| 12 | 1 | 8.192 + 376 | 68,2 s | 68,2 s | 158,7 s | 4,14 | Terminó naturalmente |
| 12 | 2 | 8.599 + 317 | 0,8 s | 0,8 s | 51,9 s | 6,18 | Terminó naturalmente |
| 12 | 3 | 8.944 + 191 | 0,9 s | 0,9 s | 30,7 s | 6,39 | Terminó naturalmente |
| 13 | 1 | 8.192 + 1.162 | 36,2 s | 36,2 s | 265,0 s | 5,07 | Terminó naturalmente |
| 13 | 2 | 9.385 + 631 | 1,2 s | 1,2 s | 70,9 s | 9,04 | Terminó naturalmente |
| 13 | 3 | 10.044 + 239 | 1,0 s | 1,0 s | 22,5 s | 11,10 | Terminó naturalmente |
| 14 | 1 | 8.192 + 1.442 | 41,3 s | 41,3 s | 307,8 s | 5,41 | Terminó naturalmente |
| 14 | 2 | 9.665 + 654 | 1,4 s | 1,4 s | 61,2 s | 10,93 | Terminó naturalmente |
| 14 | 3 | 10.347 + 245 | 0,7 s | 0,7 s | 22,6 s | 11,13 | Terminó naturalmente |
| 15 | 1 | 8.192 + 300 | 11,5 s | 11,5 s | 140,7 s | 2,31 | Terminó naturalmente |
| 15 | 2 | 8.523 + 396 | 0,5 s | 0,5 s | 61,1 s | 6,52 | Terminó naturalmente |
| 15 | 3 | 8.947 + 141 | 0,9 s | 0,9 s | 21,9 s | 6,67 | Terminó naturalmente |
| 16 | 1 | 8.192 + 442 | 73,9 s | 73,9 s | 165,9 s | 4,79 | Terminó naturalmente |
| 16 | 2 | 8.665 + 556 | 1,1 s | 1,1 s | 84,5 s | 6,66 | Terminó naturalmente |
| 16 | 3 | 9.249 + 192 | 0,6 s | 0,6 s | 22,7 s | 8,66 | Terminó naturalmente |
| 17 | 1 | 8.191 + 2.003 | 16,3 s | 16,3 s | 364,7 s | 5,75 | Terminó naturalmente |
| 17 | 2 | 10.225 + 686 | 2,2 s | 2,2 s | 63,0 s | 11,26 | Terminó naturalmente |
| 17 | 3 | 10.939 + 169 | 0,4 s | 0,4 s | 14,4 s | 11,94 | Terminó naturalmente |
| 18 | 1 | 8.192 + 326 | 91,3 s | 91,3 s | 155,3 s | 5,08 | Terminó naturalmente |
| 18 | 2 | 8.549 + 347 | 1,3 s | 1,3 s | 57,4 s | 6,16 | Terminó naturalmente |
| 18 | 3 | 8.924 + 214 | 1,3 s | 1,3 s | 33,7 s | 6,58 | Terminó naturalmente |
| 19 | 1 | 8.192 + 361 | 46,5 s | 46,5 s | 154,8 s | 3,33 | Terminó naturalmente |
| 19 | 2 | 8.584 + 283 | 0,9 s | 0,9 s | 48,4 s | 5,94 | Terminó naturalmente |
| 19 | 3 | 8.895 + 204 | 0,9 s | 0,9 s | 31,3 s | 6,69 | Terminó naturalmente |
| 20 | 1 | 8.192 + 330 | 21,2 s | 21,2 s | 146,9 s | 2,62 | Terminó naturalmente |
| 20 | 2 | 8.553 + 408 | 0,5 s | 0,5 s | 65,7 s | 6,24 | Terminó naturalmente |
| 20 | 3 | 8.989 + 225 | 1,5 s | 1,5 s | 35,2 s | 6,64 | Terminó naturalmente |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
