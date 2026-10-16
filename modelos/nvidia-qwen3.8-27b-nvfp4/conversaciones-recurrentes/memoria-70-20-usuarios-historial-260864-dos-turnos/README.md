# 20 usuarios · 70% · historial inicial de 260.864 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **40/40**. Tiempo de la prueba: **20.787,1 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 4.947,2 s | 9.615,8 s | 10.114,6 s | 9.945,4 s | 0,77 tokens/s | No cumple |
| 2 | 20/20 | 9.968,0 s | 10.375,8 s | 10.379,7 s | 10.775,1 s | 0,77 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 7.609,8 s |
| Tiempo medio de respuesta completa | 8.121,1 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,6% |
| Pico del sistema / GB10 | 76,3% |
| Menor memoria disponible | 28,82 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 2 / 2 |
| Máximo en cola | 19 |
| Recálculos | 97 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 0,99 |
| Suma de tiempos individuales | 324.843,8 s |
| Tiempo total de la prueba, incluyendo pausas | 20.787,1 s |
| Espera máxima sin datos en una conexión | 21.600 s |
| Plazo máximo configurado para todo el grupo | 28.800 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Historial de origen

Esta prueba continúa los historiales de [la etapa anterior](../memoria-70-20-usuarios-historial-131072-dos-turnos-repeticion-por-interrupcion/README.md), conservando sus respuestas reales. Antes del primer turno se añade entrada sintética hasta 260.864 tokens. No se simulan los turnos intermedios entre ambos tamaños ni se presupone que todo el historial siga en la caché de la GPU.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 2/2 | 7.474,1 s | 8.006,5 s | 16.043,1 s | 0,06 |
| 2 | 2/2 | 6.590,5 s | 7.183,9 s | 14.397,7 s | 0,07 |
| 3 | 2/2 | 4.984,0 s | 5.611,9 s | 11.253,8 s | 0,09 |
| 4 | 2/2 | 8.670,6 s | 9.299,8 s | 18.629,5 s | 0,05 |
| 5 | 2/2 | 7.294,6 s | 7.826,3 s | 15.682,7 s | 0,07 |
| 6 | 2/2 | 6.310,5 s | 6.675,6 s | 13.381,2 s | 0,08 |
| 7 | 2/2 | 8.433,5 s | 9.027,3 s | 18.084,7 s | 0,06 |
| 8 | 2/2 | 5.943,4 s | 6.476,3 s | 12.982,7 s | 0,08 |
| 9 | 2/2 | 6.828,6 s | 7.456,1 s | 14.942,2 s | 0,07 |
| 10 | 2/2 | 9.318,1 s | 9.850,6 s | 19.731,2 s | 0,05 |
| 11 | 2/2 | 8.154,3 s | 8.518,5 s | 17.067,0 s | 0,06 |
| 12 | 2/2 | 9.997,8 s | 10.362,7 s | 20.755,5 s | 0,05 |
| 13 | 2/2 | 5.629,1 s | 6.161,5 s | 12.353,0 s | 0,08 |
| 14 | 2/2 | 9.632,4 s | 10.163,8 s | 20.357,6 s | 0,05 |
| 15 | 2/2 | 7.788,5 s | 8.320,1 s | 16.670,3 s | 0,06 |
| 16 | 2/2 | 8.185,5 s | 8.647,6 s | 17.325,3 s | 0,06 |
| 17 | 2/2 | 9.138,3 s | 9.670,5 s | 19.371,0 s | 0,05 |
| 18 | 2/2 | 5.450,3 s | 5.981,4 s | 11.992,8 s | 0,09 |
| 19 | 2/2 | 6.343,2 s | 6.804,8 s | 13.639,6 s | 0,08 |
| 20 | 2/2 | 10.028,2 s | 10.376,6 s | 20.783,2 s | 0,05 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 260.864 + 512 | 4.947,2 s | 5.611,3 s | 0,77 | Completa |
| 1 | 2 | 261.632 + 512 | 10.000,9 s | 10.401,7 s | 1,27 | Completa |
| 2 | 1 | 260.864 + 512 | 3.294,5 s | 3.889,2 s | 0,86 | Completa |
| 2 | 2 | 261.632 + 512 | 9.886,4 s | 10.478,5 s | 0,86 | Completa |
| 3 | 1 | 260.864 + 512 | 284,3 s | 946,8 s | 0,77 | Completa |
| 3 | 2 | 261.632 + 512 | 9.683,6 s | 10.277,0 s | 0,86 | Completa |
| 4 | 1 | 260.864 + 512 | 7.643,0 s | 8.308,7 s | 0,77 | Completa |
| 4 | 2 | 261.632 + 512 | 9.698,3 s | 10.290,9 s | 0,86 | Completa |
| 5 | 1 | 260.864 + 512 | 4.586,4 s | 4.984,8 s | 1,28 | Completa |
| 5 | 2 | 261.632 + 512 | 10.002,8 s | 10.667,9 s | 0,77 | Completa |
| 6 | 1 | 260.864 + 512 | 2.254,2 s | 2.583,5 s | 1,55 | Completa |
| 6 | 2 | 261.632 + 512 | 10.366,7 s | 10.767,7 s | 1,27 | Completa |
| 7 | 1 | 260.864 + 512 | 6.974,5 s | 7.568,3 s | 0,86 | Completa |
| 7 | 2 | 261.632 + 512 | 9.892,6 s | 10.486,3 s | 0,86 | Completa |
| 8 | 1 | 260.864 + 512 | 1.930,4 s | 2.329,4 s | 1,28 | Completa |
| 8 | 2 | 261.632 + 512 | 9.956,5 s | 10.623,3 s | 0,77 | Completa |
| 9 | 1 | 260.864 + 512 | 3.963,8 s | 4.626,4 s | 0,77 | Completa |
| 9 | 2 | 261.632 + 512 | 9.693,5 s | 10.285,8 s | 0,86 | Completa |
| 10 | 1 | 260.864 + 512 | 8.629,8 s | 9.294,3 s | 0,77 | Completa |
| 10 | 2 | 261.632 + 512 | 10.006,3 s | 10.407,0 s | 1,28 | Completa |
| 11 | 1 | 260.864 + 512 | 5.932,8 s | 6.261,9 s | 1,55 | Completa |
| 11 | 2 | 261.632 + 512 | 10.375,8 s | 10.775,1 s | 1,28 | Completa |
| 12 | 1 | 260.864 + 512 | 9.615,8 s | 9.945,4 s | 1,55 | Completa |
| 12 | 2 | 261.632 + 512 | 10.379,7 s | 10.780,1 s | 1,28 | Completa |
| 13 | 1 | 260.864 + 512 | 1.268,1 s | 1.932,6 s | 0,77 | Completa |
| 13 | 2 | 261.632 + 512 | 9.990,1 s | 10.390,4 s | 1,28 | Completa |
| 14 | 1 | 260.864 + 512 | 9.291,9 s | 9.691,0 s | 1,28 | Completa |
| 14 | 2 | 261.632 + 512 | 9.973,0 s | 10.636,6 s | 0,77 | Completa |
| 15 | 1 | 260.864 + 512 | 5.609,0 s | 6.007,9 s | 1,28 | Completa |
| 15 | 2 | 261.632 + 512 | 9.968,0 s | 10.632,3 s | 0,77 | Completa |
| 16 | 1 | 260.864 + 512 | 6.431,2 s | 7.022,2 s | 0,86 | Completa |
| 16 | 2 | 261.632 + 512 | 9.939,8 s | 10.273,0 s | 1,53 | Completa |
| 17 | 1 | 260.864 + 512 | 8.268,7 s | 8.667,2 s | 1,28 | Completa |
| 17 | 2 | 261.632 + 512 | 10.007,9 s | 10.673,7 s | 0,77 | Completa |
| 18 | 1 | 260.864 + 512 | 906,8 s | 1.305,6 s | 1,28 | Completa |
| 18 | 2 | 261.632 + 512 | 9.993,7 s | 10.657,1 s | 0,77 | Completa |
| 19 | 1 | 260.864 + 512 | 2.752,4 s | 3.342,3 s | 0,87 | Completa |
| 19 | 2 | 261.632 + 512 | 9.934,1 s | 10.267,3 s | 1,53 | Completa |
| 20 | 1 | 260.864 + 512 | 10.114,6 s | 10.708,6 s | 0,86 | Completa |
| 20 | 2 | 261.632 + 512 | 9.941,8 s | 10.044,6 s | 4,97 | Completa |

**Llegaron exactamente al máximo de 262.144 tokens y completaron la respuesta: 20 conversaciones.**

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
