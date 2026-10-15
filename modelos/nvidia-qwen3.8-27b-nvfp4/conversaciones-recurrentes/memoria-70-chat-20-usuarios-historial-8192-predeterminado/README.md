# 20 usuarios · 70% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Peticiones sin error: **60/60**. Respuestas con contenido visible: **40/60**. Peticiones terminadas por el modelo: **37/60**. Tiempo de la prueba: **367,8 s**.

Límite impuesto al servidor: **32 activas**. Cada persona espera 30 s tras su respuesta y conserva los mensajes reales anteriores. El historial inicial se aproxima al objetivo; la tabla muestra los tokens realmente enviados en cada turno.

Control mediante `/v1/chat/completions`, con conversaciones ficticias en español. Modo de razonamiento: **predeterminado del servidor**. Cada respuesta puede terminar antes del límite de 512 tokens. Se distinguen primer texto del modelo, respuesta visible y finalización natural. No es una evaluación de calidad semántica.

## Resultado por turno

| Turno | Peticiones sin error | Espera mediana | Espera del 95% | Peor espera | Fin de petición del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 51,9 s | 103,3 s | 108,1 s | 183,5 s | 2,75 tokens/s | No cumple |
| 2 | 20/20 | 1,1 s | 2,8 s | 2,9 s | 80,7 s | 4,14 tokens/s | No cumple |
| 3 | 20/20 | 0,6 s | 0,9 s | 1,3 s | 49,1 s | 5,75 tokens/s | No cumple |

### Respuesta visible y finalización natural

| Turno | Respuestas con contenido visible | Terminaron sin alcanzar el límite de salida | Espera p95 al contenido visible |
|---|---:|---:|---:|
| 1 | 4/20 | 2/20 | 171,3 s |
| 2 | 17/20 | 16/20 | 54,2 s |
| 3 | 19/20 | 19/20 | 24,8 s |

En este control, cumplir la referencia requiere además que todas las respuestas tengan contenido visible antes de 5 s (p95) y terminen naturalmente. Alcanzar el límite de salida conserva la medición, pero no se presenta como una respuesta terminada naturalmente.

Que el modelo termine la petición por sí mismo (`stop`) no garantiza que haya entregado una respuesta visible: puede haber generado solo razonamiento. Por eso se muestran ambos recuentos. La velocidad incluye todos los tokens de salida, también los de razonamiento; no equivale necesariamente a la velocidad del texto que lee la persona.

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 19,3 s |
| Tiempo medio hasta fin de petición | 90,9 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,7% |
| Menor memoria disponible | 29,58 GiB |
| Pico de caché | 41,7% |
| Máximo activo / respuestas solapadas | 20 / 20 |
| Máximo en cola | 19 |
| Recálculos | 0 |
| Tokens recuperados de caché | 328.496 |
| Tokens/s de todo el grupo, incluyendo pausas | 62,26 |
| Suma de tiempos individuales | 5.452,3 s |
| Tiempo total de la prueba, incluyendo pausas | 367,8 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 4,4 s | 97,1 s | 351,5 s | 3,77 |
| 2 | 3/3 | 35,5 s | 96,6 s | 349,9 s | 3,57 |
| 3 | 3/3 | 29,4 s | 86,4 s | 319,3 s | 3,14 |
| 4 | 3/3 | 6,0 s | 78,0 s | 294,0 s | 3,44 |
| 5 | 3/3 | 19,7 s | 92,8 s | 338,5 s | 3,42 |
| 6 | 3/3 | 23,5 s | 85,3 s | 315,9 s | 3,13 |
| 7 | 3/3 | 9,2 s | 86,6 s | 319,8 s | 3,41 |
| 8 | 3/3 | 14,2 s | 80,6 s | 301,8 s | 3,17 |
| 9 | 3/3 | 16,0 s | 89,9 s | 329,7 s | 3,31 |
| 10 | 3/3 | 33,7 s | 92,0 s | 336,1 s | 3,34 |
| 11 | 3/3 | 10,8 s | 91,4 s | 334,3 s | 3,38 |
| 12 | 3/3 | 36,9 s | 88,9 s | 326,9 s | 3,27 |
| 13 | 3/3 | 27,4 s | 95,7 s | 347,1 s | 3,52 |
| 14 | 3/3 | 2,7 s | 96,6 s | 350,0 s | 3,74 |
| 15 | 3/3 | 17,9 s | 98,4 s | 355,3 s | 3,81 |
| 16 | 3/3 | 31,6 s | 92,0 s | 336,1 s | 3,33 |
| 17 | 3/3 | 21,7 s | 86,1 s | 318,2 s | 3,14 |
| 18 | 3/3 | 12,6 s | 101,8 s | 365,5 s | 4,04 |
| 19 | 3/3 | 7,6 s | 95,1 s | 345,5 s | 3,58 |
| 20 | 3/3 | 25,5 s | 86,0 s | 318,1 s | 3,09 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Espera a respuesta visible | Fin de petición | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 512 | 11,5 s | — s | 173,6 s | 3,15 | Alcanzó el límite de salida; sin respuesta visible |
| 1 | 2 | 8.737 + 512 | 0,7 s | — s | 80,7 s | 6,39 | Alcanzó el límite de salida; sin respuesta visible |
| 1 | 3 | 9.278 + 300 | 0,8 s | 23,0 s | 37,1 s | 8,25 | Terminó naturalmente |
| 2 | 1 | 8.192 + 512 | 103,3 s | — s | 183,5 s | 6,37 | Alcanzó el límite de salida; sin respuesta visible |
| 2 | 2 | 8.737 + 414 | 2,5 s | 47,7 s | 64,2 s | 6,69 | Terminó naturalmente |
| 2 | 3 | 9.177 + 325 | 0,6 s | 24,8 s | 42,2 s | 7,78 | Terminó naturalmente |
| 3 | 1 | 8.191 + 512 | 85,5 s | — s | 182,1 s | 5,29 | Alcanzó el límite de salida; sin respuesta visible |
| 3 | 2 | 8.736 + 318 | 2,4 s | 21,0 s | 52,7 s | 6,30 | Terminó naturalmente |
| 3 | 3 | 9.080 + 173 | 0,4 s | 6,2 s | 24,4 s | 7,16 | Terminó naturalmente |
| 4 | 1 | 8.192 + 379 | 16,4 s | 133,8 s | 154,0 s | 2,75 | Terminó naturalmente |
| 4 | 2 | 8.600 + 359 | 0,4 s | 22,3 s | 46,6 s | 7,75 | Terminó naturalmente |
| 4 | 3 | 8.985 + 273 | 1,3 s | 18,3 s | 33,4 s | 8,49 | Terminó naturalmente |
| 5 | 1 | 8.192 + 512 | 57,2 s | 171,3 s | 179,5 s | 4,18 | Alcanzó el límite de salida |
| 5 | 2 | 8.734 + 443 | 1,2 s | 53,8 s | 70,8 s | 6,35 | Terminó naturalmente |
| 5 | 3 | 9.203 + 201 | 0,7 s | 15,9 s | 28,1 s | 7,29 | Terminó naturalmente |
| 6 | 1 | 8.192 + 512 | 68,3 s | — s | 180,6 s | 4,55 | Alcanzó el límite de salida; sin respuesta visible |
| 6 | 2 | 8.737 + 311 | 1,8 s | 26,3 s | 52,8 s | 6,08 | Terminó naturalmente |
| 6 | 3 | 9.074 + 165 | 0,4 s | 5,4 s | 22,4 s | 7,46 | Terminó naturalmente |
| 7 | 1 | 8.192 + 512 | 26,1 s | — s | 175,7 s | 3,42 | Alcanzó el límite de salida; sin respuesta visible |
| 7 | 2 | 8.736 + 67 | 0,7 s | — s | 16,7 s | 4,14 | Terminó naturalmente; sin respuesta visible |
| 7 | 3 | 8.832 + 512 | 0,6 s | 17,4 s | 67,4 s | 7,66 | Alcanzó el límite de salida |
| 8 | 1 | 8.192 + 457 | 41,3 s | 148,2 s | 169,8 s | 3,55 | Terminó naturalmente |
| 8 | 2 | 8.678 + 286 | 0,6 s | 29,0 s | 48,4 s | 5,97 | Terminó naturalmente |
| 8 | 3 | 8.990 + 215 | 0,5 s | 9,0 s | 23,5 s | 9,31 | Terminó naturalmente |
| 9 | 1 | 8.192 + 512 | 46,6 s | — s | 178,3 s | 3,88 | Alcanzó el límite de salida; sin respuesta visible |
| 9 | 2 | 8.737 + 314 | 1,0 s | 30,1 s | 54,6 s | 5,85 | Terminó naturalmente |
| 9 | 3 | 9.077 + 266 | 0,5 s | 16,7 s | 36,8 s | 7,30 | Terminó naturalmente |
| 10 | 1 | 8.192 + 512 | 97,3 s | — s | 183,0 s | 5,96 | Alcanzó el límite de salida; sin respuesta visible |
| 10 | 2 | 8.737 + 431 | 2,9 s | 40,1 s | 66,8 s | 6,73 | Terminó naturalmente |
| 10 | 3 | 9.194 + 181 | 0,9 s | 8,2 s | 26,2 s | 7,12 | Terminó naturalmente |
| 11 | 1 | 8.192 + 512 | 31,1 s | — s | 176,4 s | 3,52 | Alcanzó el límite de salida; sin respuesta visible |
| 11 | 2 | 8.737 + 379 | 0,7 s | 32,8 s | 63,9 s | 5,98 | Terminó naturalmente |
| 11 | 3 | 9.142 + 239 | 0,5 s | 18,3 s | 33,9 s | 7,11 | Terminó naturalmente |
| 12 | 1 | 8.192 + 512 | 108,1 s | — s | 183,9 s | 6,74 | Alcanzó el límite de salida; sin respuesta visible |
| 12 | 2 | 8.737 + 292 | 2,2 s | 19,6 s | 46,8 s | 6,52 | Terminó naturalmente |
| 12 | 3 | 9.055 + 265 | 0,4 s | 11,5 s | 36,1 s | 7,39 | Terminó naturalmente |
| 13 | 1 | 8.192 + 512 | 79,7 s | — s | 181,6 s | 5,01 | Alcanzó el límite de salida; sin respuesta visible |
| 13 | 2 | 8.737 + 380 | 2,0 s | 42,6 s | 61,4 s | 6,38 | Terminó naturalmente |
| 13 | 3 | 9.143 + 331 | 0,5 s | 23,0 s | 43,9 s | 7,59 | Terminó naturalmente |
| 14 | 1 | 8.192 + 512 | 6,7 s | 149,8 s | 172,9 s | 3,08 | Alcanzó el límite de salida |
| 14 | 2 | 8.734 + 512 | 0,6 s | — s | 80,9 s | 6,37 | Alcanzó el límite de salida; sin respuesta visible |
| 14 | 3 | 9.276 + 286 | 0,7 s | 22,6 s | 36,1 s | 8,06 | Terminó naturalmente |
| 15 | 1 | 8.192 + 512 | 51,9 s | — s | 178,9 s | 4,02 | Alcanzó el límite de salida; sin respuesta visible |
| 15 | 2 | 8.737 + 512 | 1,1 s | 13,8 s | 78,4 s | 6,61 | Alcanzó el límite de salida |
| 15 | 3 | 9.274 + 329 | 0,8 s | 24,6 s | 38,0 s | 8,80 | Terminó naturalmente |
| 16 | 1 | 8.191 + 512 | 91,4 s | — s | 182,6 s | 5,60 | Alcanzó el límite de salida; sin respuesta visible |
| 16 | 2 | 8.736 + 393 | 2,8 s | 35,8 s | 62,4 s | 6,58 | Terminó naturalmente |
| 16 | 3 | 9.155 + 214 | 0,6 s | 16,2 s | 31,1 s | 6,98 | Terminó naturalmente |
| 17 | 1 | 8.192 + 512 | 62,7 s | — s | 180,0 s | 4,36 | Alcanzó el límite de salida; sin respuesta visible |
| 17 | 2 | 8.737 + 320 | 1,8 s | 29,9 s | 54,5 s | 6,04 | Terminó naturalmente |
| 17 | 3 | 9.083 + 166 | 0,6 s | 4,7 s | 23,6 s | 7,17 | Terminó naturalmente |
| 18 | 1 | 8.192 + 512 | 36,2 s | — s | 177,0 s | 3,63 | Alcanzó el límite de salida; sin respuesta visible |
| 18 | 2 | 8.737 + 512 | 0,8 s | 13,4 s | 79,3 s | 6,51 | Alcanzó el límite de salida |
| 18 | 3 | 9.276 + 454 | 0,8 s | 8,6 s | 49,1 s | 9,37 | Terminó naturalmente |
| 19 | 1 | 8.192 + 512 | 21,2 s | — s | 175,0 s | 3,32 | Alcanzó el límite de salida; sin respuesta visible |
| 19 | 2 | 8.737 + 457 | 0,7 s | 54,2 s | 74,5 s | 6,18 | Terminó naturalmente |
| 19 | 3 | 9.220 + 267 | 0,8 s | 21,7 s | 35,8 s | 7,60 | Terminó naturalmente |
| 20 | 1 | 8.191 + 512 | 73,9 s | — s | 181,1 s | 4,77 | Alcanzó el límite de salida; sin respuesta visible |
| 20 | 2 | 8.736 + 408 | 1,9 s | 44,8 s | 65,4 s | 6,41 | Terminó naturalmente |
| 20 | 3 | 9.170 + 64 | 0,6 s | — s | 11,5 s | 5,75 | Terminó naturalmente; sin respuesta visible |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
