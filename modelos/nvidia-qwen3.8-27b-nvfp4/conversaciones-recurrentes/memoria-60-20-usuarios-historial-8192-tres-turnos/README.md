# 20 usuarios · 60% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **395,1 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 37,0 s | 75,8 s | 79,4 s | 155,3 s | 3,65 tokens/s | No cumple |
| 2 | 20/20 | 1,4 s | 4,7 s | 4,9 s | 91,9 s | 5,60 tokens/s | No cumple |
| 3 | 20/20 | 4,7 s | 9,9 s | 10,0 s | 95,2 s | 5,41 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 16,0 s |
| Tiempo medio de respuesta completa | 111,4 s |
| Presupuesto configurado | 60% |
| Pico del motor / GB10 | 56,6% |
| Pico del sistema / GB10 | 65,6% |
| Menor memoria disponible | 41,89 GiB |
| Pico de caché | 54,2% |
| Máximo activo / respuestas solapadas | 20 / 20 |
| Máximo en cola | 19 |
| Recálculos | 0 |
| Tokens recuperados de caché | 329.280 |
| Tokens/s de todo el grupo, incluyendo pausas | 77,75 |
| Suma de tiempos individuales | 6.681,2 s |
| Tiempo total de la prueba, incluyendo pausas | 395,1 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 17,9 s | 111,5 s | 394,4 s | 3,89 |
| 2 | 3/3 | 12,8 s | 111,4 s | 394,2 s | 3,90 |
| 3 | 3/3 | 26,8 s | 111,6 s | 394,7 s | 3,89 |
| 4 | 3/3 | 16,0 s | 111,4 s | 394,3 s | 3,90 |
| 5 | 3/3 | 21,8 s | 111,5 s | 394,6 s | 3,89 |
| 6 | 3/3 | 31,3 s | 111,6 s | 394,9 s | 3,89 |
| 7 | 3/3 | 25,1 s | 111,6 s | 394,7 s | 3,89 |
| 8 | 3/3 | 10,0 s | 111,3 s | 394,0 s | 3,90 |
| 9 | 3/3 | 3,2 s | 110,9 s | 392,7 s | 3,91 |
| 10 | 3/3 | 4,4 s | 111,0 s | 393,1 s | 3,91 |
| 11 | 3/3 | 22,7 s | 111,5 s | 394,5 s | 3,89 |
| 12 | 3/3 | 1,9 s | 110,5 s | 391,4 s | 3,92 |
| 13 | 3/3 | 7,1 s | 111,2 s | 393,7 s | 3,90 |
| 14 | 3/3 | 19,8 s | 111,5 s | 394,5 s | 3,89 |
| 15 | 3/3 | 14,4 s | 111,4 s | 394,3 s | 3,90 |
| 16 | 3/3 | 30,2 s | 111,6 s | 394,9 s | 3,89 |
| 17 | 3/3 | 11,2 s | 111,3 s | 394,0 s | 3,90 |
| 18 | 3/3 | 8,6 s | 111,3 s | 393,9 s | 3,90 |
| 19 | 3/3 | 28,5 s | 111,6 s | 394,8 s | 3,89 |
| 20 | 3/3 | 5,5 s | 111,2 s | 393,5 s | 3,90 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 512 | 45,1 s | 151,9 s | 4,79 | Completa |
| 1 | 2 | 8.960 + 512 | 3,1 s | 88,9 s | 5,95 | Completa |
| 1 | 3 | 9.728 + 512 | 5,6 s | 93,6 s | 5,81 | Completa |
| 2 | 1 | 8.192 + 512 | 33,1 s | 150,1 s | 4,37 | Completa |
| 2 | 2 | 8.960 + 512 | 1,2 s | 90,1 s | 5,75 | Completa |
| 2 | 3 | 9.728 + 512 | 4,1 s | 94,0 s | 5,68 | Completa |
| 3 | 1 | 8.192 + 512 | 66,7 s | 154,4 s | 5,82 | Completa |
| 3 | 2 | 8.960 + 512 | 4,9 s | 86,8 s | 6,24 | Completa |
| 3 | 3 | 9.728 + 512 | 8,7 s | 93,5 s | 6,03 | Completa |
| 4 | 1 | 8.192 + 512 | 41,0 s | 151,3 s | 4,63 | Completa |
| 4 | 2 | 8.960 + 512 | 2,4 s | 89,4 s | 5,88 | Completa |
| 4 | 3 | 9.728 + 512 | 4,7 s | 93,6 s | 5,74 | Completa |
| 5 | 1 | 8.192 + 512 | 53,5 s | 152,9 s | 5,14 | Completa |
| 5 | 2 | 8.960 + 512 | 4,3 s | 88,1 s | 6,10 | Completa |
| 5 | 3 | 9.728 + 512 | 7,7 s | 93,6 s | 5,95 | Completa |
| 6 | 1 | 8.192 + 512 | 79,4 s | 155,7 s | 6,69 | Completa |
| 6 | 2 | 8.960 + 512 | 4,5 s | 85,6 s | 6,30 | Completa |
| 6 | 3 | 9.728 + 512 | 9,9 s | 93,5 s | 6,11 | Completa |
| 7 | 1 | 8.192 + 512 | 62,2 s | 153,9 s | 5,57 | Completa |
| 7 | 2 | 8.960 + 512 | 4,4 s | 87,2 s | 6,17 | Completa |
| 7 | 3 | 9.728 + 512 | 8,8 s | 93,6 s | 6,03 | Completa |
| 8 | 1 | 8.192 + 512 | 25,5 s | 148,8 s | 4,15 | Completa |
| 8 | 2 | 8.960 + 512 | 1,1 s | 90,9 s | 5,69 | Completa |
| 8 | 3 | 9.728 + 512 | 3,6 s | 94,4 s | 5,63 | Completa |
| 9 | 1 | 8.192 + 512 | 7,9 s | 145,3 s | 3,72 | Completa |
| 9 | 2 | 8.960 + 512 | 0,7 s | 92,1 s | 5,60 | Completa |
| 9 | 3 | 9.728 + 512 | 1,0 s | 95,4 s | 5,42 | Completa |
| 10 | 1 | 8.192 + 512 | 11,3 s | 146,0 s | 3,79 | Completa |
| 10 | 2 | 8.960 + 512 | 0,8 s | 91,9 s | 5,60 | Completa |
| 10 | 3 | 9.728 + 512 | 1,0 s | 95,2 s | 5,42 | Completa |
| 11 | 1 | 8.192 + 512 | 57,8 s | 153,4 s | 5,34 | Completa |
| 11 | 2 | 8.960 + 512 | 3,7 s | 87,6 s | 6,10 | Completa |
| 11 | 3 | 9.728 + 512 | 6,5 s | 93,5 s | 5,88 | Completa |
| 12 | 1 | 8.192 + 512 | 4,6 s | 144,5 s | 3,65 | Completa |
| 12 | 2 | 8.960 + 512 | 0,6 s | 91,9 s | 5,60 | Completa |
| 12 | 3 | 9.728 + 512 | 0,6 s | 95,0 s | 5,41 | Completa |
| 13 | 1 | 8.192 + 512 | 18,3 s | 147,4 s | 3,96 | Completa |
| 13 | 2 | 8.960 + 512 | 0,8 s | 91,5 s | 5,63 | Completa |
| 13 | 3 | 9.728 + 512 | 2,2 s | 94,8 s | 5,52 | Completa |
| 14 | 1 | 8.192 + 512 | 49,2 s | 152,4 s | 4,95 | Completa |
| 14 | 2 | 8.960 + 512 | 3,6 s | 88,5 s | 6,02 | Completa |
| 14 | 3 | 9.728 + 512 | 6,7 s | 93,6 s | 5,88 | Completa |
| 15 | 1 | 8.192 + 512 | 37,0 s | 150,7 s | 4,50 | Completa |
| 15 | 2 | 8.960 + 512 | 1,4 s | 89,7 s | 5,78 | Completa |
| 15 | 3 | 9.728 + 512 | 4,9 s | 93,9 s | 5,74 | Completa |
| 16 | 1 | 8.192 + 512 | 75,8 s | 155,3 s | 6,43 | Completa |
| 16 | 2 | 8.960 + 512 | 4,7 s | 86,0 s | 6,29 | Completa |
| 16 | 3 | 9.728 + 512 | 10,0 s | 93,6 s | 6,11 | Completa |
| 17 | 1 | 8.192 + 512 | 29,3 s | 149,4 s | 4,25 | Completa |
| 17 | 2 | 8.960 + 512 | 1,1 s | 90,5 s | 5,72 | Completa |
| 17 | 3 | 9.728 + 512 | 3,3 s | 94,1 s | 5,63 | Completa |
| 18 | 1 | 8.192 + 512 | 21,9 s | 148,1 s | 4,05 | Completa |
| 18 | 2 | 8.960 + 512 | 1,1 s | 91,3 s | 5,67 | Completa |
| 18 | 3 | 9.728 + 512 | 2,8 s | 94,5 s | 5,57 | Completa |
| 19 | 1 | 8.192 + 512 | 71,2 s | 154,9 s | 6,11 | Completa |
| 19 | 2 | 8.960 + 512 | 4,4 s | 86,3 s | 6,24 | Completa |
| 19 | 3 | 9.728 + 512 | 9,8 s | 93,6 s | 6,09 | Completa |
| 20 | 1 | 8.192 + 512 | 14,8 s | 146,7 s | 3,87 | Completa |
| 20 | 2 | 8.960 + 512 | 0,8 s | 91,8 s | 5,62 | Completa |
| 20 | 3 | 9.728 + 512 | 1,0 s | 94,9 s | 5,44 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
