# 20 usuarios · 70% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Peticiones sin error: **60/60**. Respuestas con contenido visible: **60/60**. Peticiones terminadas por el modelo: **49/60**. Tiempo de la prueba: **342,4 s**.

Límite impuesto al servidor: **32 activas**. Cada persona espera 30 s tras su respuesta y conserva los mensajes reales anteriores. El historial inicial se aproxima al objetivo; la tabla muestra los tokens realmente enviados en cada turno.

Control mediante `/v1/chat/completions`, con conversaciones ficticias en español. Modo de razonamiento: **desactivado**. Cada respuesta puede terminar antes del límite de 512 tokens. Se distinguen primer texto del modelo, respuesta visible y finalización natural. No es una evaluación de calidad semántica.

## Resultado por turno

| Turno | Peticiones sin error | Espera mediana | Espera del 95% | Peor espera | Fin de petición del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 51,8 s | 103,2 s | 108,0 s | 175,1 s | 2,47 tokens/s | No cumple |
| 2 | 20/20 | 0,7 s | 1,6 s | 1,8 s | 78,4 s | 6,08 tokens/s | No cumple |
| 3 | 20/20 | 1,0 s | 3,0 s | 3,3 s | 36,9 s | 6,71 tokens/s | No cumple |

### Respuesta visible y finalización natural

| Turno | Respuestas con contenido visible | Terminaron sin alcanzar el límite de salida | Espera p95 al contenido visible |
|---|---:|---:|---:|
| 1 | 20/20 | 14/20 | 103,2 s |
| 2 | 20/20 | 15/20 | 1,6 s |
| 3 | 20/20 | 20/20 | 3,0 s |

En este control, cumplir la referencia requiere además que todas las respuestas tengan contenido visible antes de 5 s (p95) y terminen naturalmente. Alcanzar el límite de salida conserva la medición, pero no se presenta como una respuesta terminada naturalmente.

Que el modelo termine la petición por sí mismo (`stop`) no garantiza que haya entregado una respuesta visible: puede haber generado solo razonamiento. Por eso se muestran ambos recuentos. La velocidad incluye todos los tokens de salida, también los de razonamiento; no equivale necesariamente a la velocidad del texto que lee la persona.

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 19,3 s |
| Tiempo medio hasta fin de petición | 85,0 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,6% |
| Menor memoria disponible | 29,63 GiB |
| Pico de caché | 41,7% |
| Máximo activo / respuestas solapadas | 20 / 20 |
| Máximo en cola | 19 |
| Recálculos | 0 |
| Tokens recuperados de caché | 318.304 |
| Tokens/s de todo el grupo, incluyendo pausas | 60,81 |
| Suma de tiempos individuales | 5.098,2 s |
| Tiempo total de la prueba, incluyendo pausas | 342,4 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 14,3 s | 82,6 s | 307,7 s | 3,15 |
| 2 | 3/3 | 4,5 s | 76,7 s | 290,1 s | 3,08 |
| 3 | 3/3 | 23,3 s | 93,4 s | 340,2 s | 3,91 |
| 4 | 3/3 | 2,8 s | 89,3 s | 327,9 s | 3,54 |
| 5 | 3/3 | 29,0 s | 79,9 s | 299,8 s | 2,94 |
| 6 | 3/3 | 7,5 s | 82,0 s | 306,2 s | 3,19 |
| 7 | 3/3 | 31,8 s | 88,9 s | 326,7 s | 3,30 |
| 8 | 3/3 | 16,0 s | 79,9 s | 299,8 s | 3,02 |
| 9 | 3/3 | 21,4 s | 77,0 s | 291,0 s | 2,90 |
| 10 | 3/3 | 33,0 s | 82,8 s | 308,6 s | 2,96 |
| 11 | 3/3 | 5,9 s | 88,0 s | 323,9 s | 3,44 |
| 12 | 3/3 | 27,8 s | 88,0 s | 324,0 s | 3,28 |
| 13 | 3/3 | 9,8 s | 88,6 s | 325,7 s | 3,56 |
| 14 | 3/3 | 19,9 s | 88,1 s | 324,3 s | 3,50 |
| 15 | 3/3 | 35,6 s | 88,8 s | 326,6 s | 3,52 |
| 16 | 3/3 | 36,7 s | 91,4 s | 334,3 s | 3,72 |
| 17 | 3/3 | 17,9 s | 80,6 s | 301,8 s | 3,05 |
| 18 | 3/3 | 11,7 s | 89,0 s | 327,0 s | 3,59 |
| 19 | 3/3 | 25,2 s | 76,5 s | 289,5 s | 2,83 |
| 20 | 3/3 | 12,6 s | 88,0 s | 324,2 s | 3,39 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Espera a respuesta visible | Fin de petición | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.191 + 374 | 41,3 s | 41,3 s | 155,5 s | 3,27 | Terminó naturalmente |
| 1 | 2 | 8.596 + 415 | 0,6 s | 0,6 s | 65,2 s | 6,41 | Terminó naturalmente |
| 1 | 3 | 9.039 + 179 | 1,0 s | 1,0 s | 26,9 s | 6,86 | Terminó naturalmente |
| 2 | 1 | 8.192 + 333 | 11,5 s | 11,5 s | 145,9 s | 2,47 | Terminó naturalmente |
| 2 | 2 | 8.556 + 336 | 0,7 s | 0,7 s | 53,1 s | 6,39 | Terminó naturalmente |
| 2 | 3 | 8.920 + 224 | 1,2 s | 1,2 s | 31,1 s | 7,47 | Terminó naturalmente |
| 3 | 1 | 8.192 + 512 | 68,2 s | 68,2 s | 172,4 s | 4,91 | Alcanzó el límite de salida |
| 3 | 2 | 8.736 + 502 | 1,1 s | 1,1 s | 73,7 s | 6,90 | Terminó naturalmente |
| 3 | 3 | 9.266 + 317 | 0,6 s | 0,6 s | 34,0 s | 9,46 | Terminó naturalmente |
| 4 | 1 | 8.191 + 384 | 6,7 s | 6,7 s | 152,4 s | 2,63 | Terminó naturalmente |
| 4 | 2 | 8.606 + 512 | 0,6 s | 0,6 s | 78,5 s | 6,56 | Alcanzó el límite de salida |
| 4 | 3 | 9.145 + 264 | 1,2 s | 1,2 s | 36,9 s | 7,36 | Terminó naturalmente |
| 5 | 1 | 8.192 + 380 | 85,4 s | 85,4 s | 160,7 s | 5,04 | Terminó naturalmente |
| 5 | 2 | 8.603 + 274 | 0,7 s | 0,7 s | 45,3 s | 6,12 | Terminó naturalmente |
| 5 | 3 | 8.907 + 228 | 0,8 s | 0,8 s | 33,7 s | 6,89 | Terminó naturalmente |
| 6 | 1 | 8.192 + 320 | 21,2 s | 21,2 s | 145,4 s | 2,57 | Terminó naturalmente |
| 6 | 2 | 8.543 + 446 | 0,4 s | 0,4 s | 69,0 s | 6,49 | Terminó naturalmente |
| 6 | 3 | 9.017 + 211 | 0,9 s | 0,9 s | 31,7 s | 6,82 | Terminó naturalmente |
| 7 | 1 | 8.192 + 347 | 91,3 s | 91,3 s | 157,6 s | 5,22 | Terminó naturalmente |
| 7 | 2 | 8.570 + 512 | 0,9 s | 0,9 s | 78,1 s | 6,62 | Alcanzó el límite de salida |
| 7 | 3 | 9.111 + 219 | 3,3 s | 3,3 s | 30,9 s | 7,89 | Terminó naturalmente |
| 8 | 1 | 8.192 + 297 | 46,5 s | 46,5 s | 145,7 s | 2,98 | Terminó naturalmente |
| 8 | 2 | 8.520 + 419 | 0,7 s | 0,7 s | 65,3 s | 6,47 | Terminó naturalmente |
| 8 | 3 | 8.967 + 188 | 0,9 s | 0,9 s | 28,8 s | 6,71 | Terminó naturalmente |
| 9 | 1 | 8.191 + 339 | 62,7 s | 62,7 s | 153,7 s | 3,72 | Terminó naturalmente |
| 9 | 2 | 8.561 + 308 | 0,6 s | 0,6 s | 50,7 s | 6,12 | Terminó naturalmente |
| 9 | 3 | 8.897 + 196 | 1,0 s | 1,0 s | 26,6 s | 7,61 | Terminó naturalmente |
| 10 | 1 | 8.192 + 292 | 97,3 s | 97,3 s | 151,4 s | 5,38 | Terminó naturalmente |
| 10 | 2 | 8.515 + 413 | 0,5 s | 0,5 s | 65,6 s | 6,33 | Terminó naturalmente |
| 10 | 3 | 8.956 + 209 | 1,2 s | 1,2 s | 31,5 s | 6,85 | Terminó naturalmente |
| 11 | 1 | 8.192 + 346 | 16,3 s | 16,3 s | 148,5 s | 2,61 | Terminó naturalmente |
| 11 | 2 | 8.569 + 382 | 0,5 s | 0,5 s | 60,8 s | 6,32 | Terminó naturalmente |
| 11 | 3 | 8.979 + 387 | 0,8 s | 0,8 s | 54,5 s | 7,19 | Terminó naturalmente |
| 12 | 1 | 8.192 + 356 | 79,6 s | 79,6 s | 157,5 s | 4,56 | Terminó naturalmente |
| 12 | 2 | 8.579 + 512 | 0,8 s | 0,8 s | 78,1 s | 6,61 | Alcanzó el límite de salida |
| 12 | 3 | 9.120 + 195 | 3,0 s | 3,0 s | 28,3 s | 7,67 | Terminó naturalmente |
| 13 | 1 | 8.192 + 512 | 26,1 s | 26,1 s | 168,6 s | 3,58 | Alcanzó el límite de salida |
| 13 | 2 | 8.735 + 438 | 1,6 s | 1,6 s | 67,2 s | 6,67 | Terminó naturalmente |
| 13 | 3 | 9.201 + 211 | 1,8 s | 1,8 s | 29,9 s | 7,49 | Terminó naturalmente |
| 14 | 1 | 8.192 + 512 | 57,2 s | 57,2 s | 171,5 s | 4,47 | Alcanzó el límite de salida |
| 14 | 2 | 8.736 + 423 | 1,5 s | 1,5 s | 64,0 s | 6,75 | Terminó naturalmente |
| 14 | 3 | 9.187 + 199 | 0,9 s | 0,9 s | 28,7 s | 7,13 | Terminó naturalmente |
| 15 | 1 | 8.192 + 512 | 103,2 s | 103,2 s | 175,1 s | 7,12 | Alcanzó el límite de salida |
| 15 | 2 | 8.736 + 420 | 1,8 s | 1,8 s | 62,3 s | 6,93 | Terminó naturalmente |
| 15 | 3 | 9.184 + 218 | 1,7 s | 1,7 s | 29,2 s | 7,89 | Terminó naturalmente |
| 16 | 1 | 8.192 + 512 | 108,0 s | 108,0 s | 175,5 s | 7,58 | Alcanzó el límite de salida |
| 16 | 2 | 8.736 + 512 | 1,5 s | 1,5 s | 74,5 s | 7,00 | Alcanzó el límite de salida |
| 16 | 3 | 9.277 + 218 | 0,6 s | 0,6 s | 24,3 s | 9,16 | Terminó naturalmente |
| 17 | 1 | 8.191 + 401 | 51,8 s | 51,8 s | 159,7 s | 3,71 | Terminó naturalmente |
| 17 | 2 | 8.623 + 363 | 0,7 s | 0,7 s | 57,9 s | 6,33 | Terminó naturalmente |
| 17 | 3 | 9.014 + 156 | 1,0 s | 1,0 s | 24,1 s | 6,73 | Terminó naturalmente |
| 18 | 1 | 8.192 + 512 | 31,1 s | 31,1 s | 169,1 s | 3,70 | Alcanzó el límite de salida |
| 18 | 2 | 8.736 + 438 | 1,3 s | 1,3 s | 66,8 s | 6,67 | Terminó naturalmente |
| 18 | 3 | 9.202 + 223 | 2,8 s | 2,8 s | 31,1 s | 7,85 | Terminó naturalmente |
| 19 | 1 | 8.192 + 308 | 73,9 s | 73,9 s | 150,9 s | 3,99 | Terminó naturalmente |
| 19 | 2 | 8.531 + 293 | 0,4 s | 0,4 s | 48,5 s | 6,08 | Terminó naturalmente |
| 19 | 3 | 8.852 + 218 | 1,2 s | 1,2 s | 30,1 s | 7,51 | Terminó naturalmente |
| 20 | 1 | 8.192 + 360 | 36,1 s | 36,1 s | 153,2 s | 3,07 | Terminó naturalmente |
| 20 | 2 | 8.583 + 512 | 0,6 s | 0,6 s | 78,4 s | 6,57 | Alcanzó el límite de salida |
| 20 | 3 | 9.124 + 226 | 1,1 s | 1,1 s | 32,6 s | 7,14 | Terminó naturalmente |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
