# 20 usuarios · 70% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **391,2 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 36,3 s | 74,7 s | 78,2 s | 154,3 s | 3,67 tokens/s | No cumple |
| 2 | 20/20 | 1,2 s | 3,6 s | 3,7 s | 90,4 s | 5,69 tokens/s | No cumple |
| 3 | 20/20 | 3,5 s | 8,1 s | 8,2 s | 93,5 s | 5,50 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 15,2 s |
| Tiempo medio de respuesta completa | 110,0 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,8% |
| Pico del sistema / GB10 | 75,7% |
| Menor memoria disponible | 29,53 GiB |
| Pico de caché | 42,9% |
| Máximo activo / respuestas solapadas | 20 / 20 |
| Máximo en cola | 19 |
| Recálculos | 0 |
| Tokens recuperados de caché | 329.280 |
| Tokens/s de todo el grupo, incluyendo pausas | 78,53 |
| Suma de tiempos individuales | 6.599,7 s |
| Tiempo total de la prueba, incluyendo pausas | 391,2 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 16,9 s | 110,1 s | 390,3 s | 3,93 |
| 2 | 3/3 | 27,2 s | 110,3 s | 390,8 s | 3,93 |
| 3 | 3/3 | 25,6 s | 110,3 s | 390,8 s | 3,93 |
| 4 | 3/3 | 3,0 s | 109,5 s | 388,5 s | 3,95 |
| 5 | 3/3 | 10,9 s | 110,0 s | 390,1 s | 3,94 |
| 6 | 3/3 | 29,8 s | 110,3 s | 390,9 s | 3,93 |
| 7 | 3/3 | 28,7 s | 110,3 s | 390,8 s | 3,93 |
| 8 | 3/3 | 9,5 s | 110,0 s | 390,0 s | 3,94 |
| 9 | 3/3 | 19,3 s | 110,2 s | 390,5 s | 3,93 |
| 10 | 3/3 | 5,3 s | 109,7 s | 389,2 s | 3,95 |
| 11 | 3/3 | 8,1 s | 109,9 s | 389,8 s | 3,94 |
| 12 | 3/3 | 13,7 s | 110,1 s | 390,2 s | 3,94 |
| 13 | 3/3 | 1,8 s | 109,1 s | 387,2 s | 3,97 |
| 14 | 3/3 | 15,5 s | 110,1 s | 390,3 s | 3,93 |
| 15 | 3/3 | 12,1 s | 110,0 s | 390,1 s | 3,94 |
| 16 | 3/3 | 6,5 s | 109,8 s | 389,5 s | 3,94 |
| 17 | 3/3 | 23,7 s | 110,2 s | 390,7 s | 3,93 |
| 18 | 3/3 | 22,1 s | 110,2 s | 390,6 s | 3,93 |
| 19 | 3/3 | 4,2 s | 109,6 s | 388,9 s | 3,95 |
| 20 | 3/3 | 20,5 s | 110,2 s | 390,6 s | 3,93 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 512 | 44,3 s | 150,8 s | 4,80 | Completa |
| 1 | 2 | 8.960 + 512 | 2,1 s | 87,6 s | 5,98 | Completa |
| 1 | 3 | 9.728 + 512 | 4,1 s | 91,9 s | 5,82 | Completa |
| 2 | 1 | 8.192 + 512 | 70,2 s | 153,8 s | 6,11 | Completa |
| 2 | 2 | 8.960 + 512 | 3,7 s | 85,1 s | 6,28 | Completa |
| 2 | 3 | 9.728 + 512 | 7,5 s | 91,8 s | 6,06 | Completa |
| 3 | 1 | 8.192 + 512 | 65,7 s | 153,4 s | 5,83 | Completa |
| 3 | 2 | 8.960 + 512 | 3,6 s | 85,4 s | 6,24 | Completa |
| 3 | 3 | 9.728 + 512 | 7,6 s | 91,9 s | 6,06 | Completa |
| 4 | 1 | 8.192 + 512 | 7,6 s | 144,2 s | 3,74 | Completa |
| 4 | 2 | 8.960 + 512 | 0,7 s | 90,6 s | 5,69 | Completa |
| 4 | 3 | 9.728 + 512 | 0,7 s | 93,7 s | 5,50 | Completa |
| 5 | 1 | 8.192 + 512 | 28,7 s | 148,4 s | 4,27 | Completa |
| 5 | 2 | 8.960 + 512 | 1,0 s | 89,1 s | 5,80 | Completa |
| 5 | 3 | 9.728 + 512 | 3,1 s | 92,5 s | 5,71 | Completa |
| 6 | 1 | 8.192 + 512 | 78,2 s | 154,7 s | 6,68 | Completa |
| 6 | 2 | 8.960 + 512 | 3,1 s | 84,3 s | 6,29 | Completa |
| 6 | 3 | 9.728 + 512 | 8,2 s | 91,9 s | 6,10 | Completa |
| 7 | 1 | 8.192 + 512 | 74,7 s | 154,3 s | 6,42 | Completa |
| 7 | 2 | 8.960 + 512 | 3,3 s | 84,6 s | 6,28 | Completa |
| 7 | 3 | 9.728 + 512 | 8,1 s | 91,9 s | 6,10 | Completa |
| 8 | 1 | 8.192 + 512 | 25,0 s | 147,8 s | 4,16 | Completa |
| 8 | 2 | 8.960 + 512 | 1,0 s | 89,5 s | 5,77 | Completa |
| 8 | 3 | 9.728 + 512 | 2,5 s | 92,7 s | 5,66 | Completa |
| 9 | 1 | 8.192 + 512 | 48,4 s | 151,4 s | 4,96 | Completa |
| 9 | 2 | 8.960 + 512 | 3,5 s | 87,2 s | 6,11 | Completa |
| 9 | 3 | 9.728 + 512 | 6,0 s | 91,9 s | 5,95 | Completa |
| 10 | 1 | 8.192 + 512 | 14,3 s | 145,7 s | 3,89 | Completa |
| 10 | 2 | 8.960 + 512 | 0,7 s | 90,3 s | 5,70 | Completa |
| 10 | 3 | 9.728 + 512 | 0,9 s | 93,2 s | 5,54 | Completa |
| 11 | 1 | 8.192 + 512 | 21,4 s | 147,1 s | 4,06 | Completa |
| 11 | 2 | 8.960 + 512 | 1,0 s | 89,9 s | 5,75 | Completa |
| 11 | 3 | 9.728 + 512 | 1,9 s | 92,8 s | 5,62 | Completa |
| 12 | 1 | 8.192 + 512 | 36,3 s | 149,7 s | 4,51 | Completa |
| 12 | 2 | 8.960 + 512 | 1,2 s | 88,4 s | 5,86 | Completa |
| 12 | 3 | 9.728 + 512 | 3,5 s | 92,2 s | 5,77 | Completa |
| 13 | 1 | 8.192 + 512 | 4,2 s | 143,4 s | 3,67 | Completa |
| 13 | 2 | 8.960 + 512 | 0,6 s | 90,4 s | 5,69 | Completa |
| 13 | 3 | 9.728 + 512 | 0,6 s | 93,3 s | 5,51 | Completa |
| 14 | 1 | 8.192 + 512 | 40,3 s | 150,2 s | 4,65 | Completa |
| 14 | 2 | 8.960 + 512 | 2,0 s | 88,1 s | 5,94 | Completa |
| 14 | 3 | 9.728 + 512 | 4,3 s | 92,0 s | 5,82 | Completa |
| 15 | 1 | 8.192 + 512 | 32,5 s | 149,0 s | 4,38 | Completa |
| 15 | 2 | 8.960 + 512 | 1,1 s | 88,8 s | 5,83 | Completa |
| 15 | 3 | 9.728 + 512 | 2,8 s | 92,3 s | 5,71 | Completa |
| 16 | 1 | 8.192 + 512 | 17,8 s | 146,4 s | 3,97 | Completa |
| 16 | 2 | 8.960 + 512 | 0,8 s | 90,2 s | 5,72 | Completa |
| 16 | 3 | 9.728 + 512 | 0,9 s | 92,9 s | 5,55 | Completa |
| 17 | 1 | 8.192 + 512 | 61,3 s | 152,9 s | 5,58 | Completa |
| 17 | 2 | 8.960 + 512 | 3,0 s | 85,8 s | 6,17 | Completa |
| 17 | 3 | 9.728 + 512 | 6,8 s | 91,9 s | 6,01 | Completa |
| 18 | 1 | 8.192 + 512 | 56,9 s | 152,4 s | 5,35 | Completa |
| 18 | 2 | 8.960 + 512 | 3,5 s | 86,3 s | 6,17 | Completa |
| 18 | 3 | 9.728 + 512 | 5,8 s | 91,8 s | 5,94 | Completa |
| 19 | 1 | 8.192 + 512 | 10,9 s | 145,0 s | 3,81 | Completa |
| 19 | 2 | 8.960 + 512 | 0,7 s | 90,4 s | 5,69 | Completa |
| 19 | 3 | 9.728 + 512 | 0,9 s | 93,5 s | 5,52 | Completa |
| 20 | 1 | 8.192 + 512 | 52,6 s | 151,9 s | 5,15 | Completa |
| 20 | 2 | 8.960 + 512 | 3,0 s | 86,7 s | 6,10 | Completa |
| 20 | 3 | 9.728 + 512 | 5,9 s | 91,9 s | 5,94 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
