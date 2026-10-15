# 20 usuarios · 50% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **421,7 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 51,1 s | 102,1 s | 107,0 s | 182,8 s | 3,09 tokens/s | No cumple |
| 2 | 20/20 | 1,4 s | 4,3 s | 4,5 s | 91,3 s | 5,63 tokens/s | No cumple |
| 3 | 20/20 | 4,6 s | 9,8 s | 10,0 s | 94,9 s | 5,42 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 20,8 s |
| Tiempo medio de respuesta completa | 120,2 s |
| Presupuesto configurado | 50% |
| Pico del motor / GB10 | 46,6% |
| Pico del sistema / GB10 | 55,2% |
| Menor memoria disponible | 54,53 GiB |
| Pico de caché | 73,2% |
| Máximo activo / respuestas solapadas | 20 / 20 |
| Máximo en cola | 19 |
| Recálculos | 0 |
| Tokens recuperados de caché | 329.280 |
| Tokens/s de todo el grupo, incluyendo pausas | 72,85 |
| Suma de tiempos individuales | 7.212,3 s |
| Tiempo total de la prueba, incluyendo pausas | 421,7 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 36,8 s | 120,5 s | 421,4 s | 3,65 |
| 2 | 3/3 | 38,8 s | 120,5 s | 421,4 s | 3,64 |
| 3 | 3/3 | 40,2 s | 120,5 s | 421,4 s | 3,64 |
| 4 | 3/3 | 34,4 s | 120,4 s | 421,3 s | 3,65 |
| 5 | 3/3 | 25,6 s | 120,3 s | 421,1 s | 3,65 |
| 6 | 3/3 | 15,0 s | 120,2 s | 420,6 s | 3,65 |
| 7 | 3/3 | 31,9 s | 120,4 s | 421,2 s | 3,65 |
| 8 | 3/3 | 17,0 s | 120,2 s | 420,7 s | 3,65 |
| 9 | 3/3 | 2,5 s | 119,4 s | 418,1 s | 3,67 |
| 10 | 3/3 | 13,4 s | 120,2 s | 420,6 s | 3,65 |
| 11 | 3/3 | 21,1 s | 120,3 s | 420,8 s | 3,65 |
| 12 | 3/3 | 27,7 s | 120,4 s | 421,1 s | 3,65 |
| 13 | 3/3 | 19,1 s | 120,3 s | 420,8 s | 3,65 |
| 14 | 3/3 | 5,9 s | 119,9 s | 419,7 s | 3,66 |
| 15 | 3/3 | 7,5 s | 120,0 s | 420,0 s | 3,66 |
| 16 | 3/3 | 30,5 s | 120,4 s | 421,3 s | 3,65 |
| 17 | 3/3 | 23,2 s | 120,3 s | 420,9 s | 3,65 |
| 18 | 3/3 | 11,4 s | 120,1 s | 420,4 s | 3,65 |
| 19 | 3/3 | 9,5 s | 120,1 s | 420,3 s | 3,65 |
| 20 | 3/3 | 4,4 s | 119,8 s | 419,4 s | 3,66 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 512 | 96,2 s | 182,4 s | 5,93 | Completa |
| 1 | 2 | 8.960 + 512 | 4,5 s | 85,7 s | 6,30 | Completa |
| 1 | 3 | 9.728 + 512 | 9,6 s | 93,3 s | 6,11 | Completa |
| 2 | 1 | 8.192 + 512 | 102,1 s | 182,8 s | 6,33 | Completa |
| 2 | 2 | 8.960 + 512 | 4,1 s | 85,2 s | 6,30 | Completa |
| 2 | 3 | 9.728 + 512 | 10,0 s | 93,4 s | 6,13 | Completa |
| 3 | 1 | 8.192 + 512 | 107,0 s | 183,2 s | 6,70 | Completa |
| 3 | 2 | 8.960 + 512 | 3,9 s | 84,9 s | 6,31 | Completa |
| 3 | 3 | 9.728 + 512 | 9,8 s | 93,3 s | 6,12 | Completa |
| 4 | 1 | 8.192 + 512 | 90,3 s | 181,9 s | 5,58 | Completa |
| 4 | 2 | 8.960 + 512 | 4,3 s | 86,0 s | 6,25 | Completa |
| 4 | 3 | 9.728 + 512 | 8,7 s | 93,3 s | 6,04 | Completa |
| 5 | 1 | 8.192 + 512 | 67,4 s | 179,9 s | 4,54 | Completa |
| 5 | 2 | 8.960 + 512 | 2,8 s | 87,7 s | 6,02 | Completa |
| 5 | 3 | 9.728 + 512 | 6,6 s | 93,4 s | 5,89 | Completa |
| 6 | 1 | 8.192 + 512 | 40,7 s | 176,9 s | 3,75 | Completa |
| 6 | 2 | 8.960 + 512 | 1,1 s | 89,7 s | 5,77 | Completa |
| 6 | 3 | 9.728 + 512 | 3,2 s | 93,9 s | 5,64 | Completa |
| 7 | 1 | 8.192 + 512 | 84,5 s | 181,4 s | 5,27 | Completa |
| 7 | 2 | 8.960 + 512 | 3,6 s | 86,4 s | 6,17 | Completa |
| 7 | 3 | 9.728 + 512 | 7,6 s | 93,3 s | 5,96 | Completa |
| 8 | 1 | 8.192 + 512 | 45,8 s | 177,6 s | 3,88 | Completa |
| 8 | 2 | 8.960 + 512 | 1,2 s | 89,4 s | 5,80 | Completa |
| 8 | 3 | 9.728 + 512 | 4,0 s | 93,8 s | 5,69 | Completa |
| 9 | 1 | 8.192 + 512 | 6,4 s | 172,0 s | 3,09 | Completa |
| 9 | 2 | 8.960 + 512 | 0,6 s | 91,3 s | 5,63 | Completa |
| 9 | 3 | 9.728 + 512 | 0,6 s | 94,8 s | 5,42 | Completa |
| 10 | 1 | 8.192 + 512 | 35,5 s | 176,3 s | 3,63 | Completa |
| 10 | 2 | 8.960 + 512 | 1,0 s | 90,1 s | 5,74 | Completa |
| 10 | 3 | 9.728 + 512 | 3,5 s | 94,2 s | 5,64 | Completa |
| 11 | 1 | 8.192 + 512 | 56,4 s | 178,8 s | 4,18 | Completa |
| 11 | 2 | 8.960 + 512 | 2,1 s | 88,6 s | 5,91 | Completa |
| 11 | 3 | 9.728 + 512 | 4,6 s | 93,4 s | 5,75 | Completa |
| 12 | 1 | 8.192 + 512 | 73,0 s | 180,4 s | 4,76 | Completa |
| 12 | 2 | 8.960 + 512 | 3,4 s | 87,3 s | 6,09 | Completa |
| 12 | 3 | 9.728 + 512 | 6,5 s | 93,3 s | 5,89 | Completa |
| 13 | 1 | 8.192 + 512 | 51,1 s | 178,2 s | 4,02 | Completa |
| 13 | 2 | 8.960 + 512 | 1,4 s | 89,0 s | 5,83 | Completa |
| 13 | 3 | 9.728 + 512 | 4,8 s | 93,6 s | 5,75 | Completa |
| 14 | 1 | 8.192 + 512 | 15,9 s | 173,5 s | 3,24 | Completa |
| 14 | 2 | 8.960 + 512 | 0,8 s | 91,3 s | 5,64 | Completa |
| 14 | 3 | 9.728 + 512 | 0,9 s | 94,9 s | 5,44 | Completa |
| 15 | 1 | 8.192 + 512 | 20,7 s | 174,2 s | 3,33 | Completa |
| 15 | 2 | 8.960 + 512 | 0,7 s | 91,0 s | 5,66 | Completa |
| 15 | 3 | 9.728 + 512 | 1,1 s | 94,7 s | 5,46 | Completa |
| 16 | 1 | 8.192 + 512 | 78,7 s | 180,9 s | 5,00 | Completa |
| 16 | 2 | 8.960 + 512 | 4,1 s | 86,9 s | 6,17 | Completa |
| 16 | 3 | 9.728 + 512 | 8,8 s | 93,4 s | 6,04 | Completa |
| 17 | 1 | 8.192 + 512 | 61,9 s | 179,3 s | 4,35 | Completa |
| 17 | 2 | 8.960 + 512 | 2,3 s | 88,2 s | 5,95 | Completa |
| 17 | 3 | 9.728 + 512 | 5,6 s | 93,4 s | 5,82 | Completa |
| 18 | 1 | 8.192 + 512 | 30,5 s | 175,6 s | 3,52 | Completa |
| 18 | 2 | 8.960 + 512 | 1,0 s | 90,5 s | 5,71 | Completa |
| 18 | 3 | 9.728 + 512 | 2,7 s | 94,3 s | 5,58 | Completa |
| 19 | 1 | 8.192 + 512 | 25,6 s | 174,9 s | 3,42 | Completa |
| 19 | 2 | 8.960 + 512 | 1,1 s | 90,9 s | 5,69 | Completa |
| 19 | 3 | 9.728 + 512 | 2,0 s | 94,4 s | 5,53 | Completa |
| 20 | 1 | 8.192 + 512 | 11,2 s | 172,8 s | 3,16 | Completa |
| 20 | 2 | 8.960 + 512 | 0,7 s | 91,5 s | 5,63 | Completa |
| 20 | 3 | 9.728 + 512 | 1,2 s | 95,1 s | 5,44 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
