# 20 usuarios · 70% · historial inicial de 131.072 tokens

[Volver a la comparación](../README.md)

**Prueba interrumpida por el controlador.** Se conservan **30/40** respuestas recibidas y la última medición, tomada a los **8.335,3 s**. No se completó el grupo.

El lanzador perdió su canal de salida (`BrokenPipeError`) y detuvo el cliente. Este es un fallo de ejecución de la prueba; no demuestra falta de memoria del modelo. Las mediciones originales se conservan sin cambios y su estado interno puede seguir indicando «running», porque son el último registro anterior a la interrupción. El tiempo mostrado corresponde a ese registro, no a una finalización normal. Se repite el ensayo completo como una prueba separada. [Evidencia de la interrupción](interrupcion.json).


Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 2.254,2 s | 4.761,8 s | 4.929,3 s | 5.476,1 s | 0,60 tokens/s | No cumple |
| 2 | 10/20 | 4.371,4 s | 4.558,3 s | 4.558,3 s | 5.309,0 s | 0,61 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 3.099,0 s |
| Tiempo medio de respuesta completa | 3.847,3 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 76,1% |
| Menor memoria disponible | 29,12 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 4 / 4 |
| Máximo en cola | 19 |
| Recálculos | 81 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 1,84 |
| Suma de tiempos individuales | 115.418,3 s |
| Tiempo total de la prueba, incluyendo pausas | 8.335,3 s |
| Espera máxima sin datos en una conexión | 10.800 s |
| Plazo máximo configurado para todo el grupo | 14.400 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Historial de origen

Esta prueba continúa los historiales de [la etapa anterior](../memoria-70-20-usuarios-historial-65536-dos-turnos/README.md), conservando sus respuestas reales. Antes del primer turno se añade entrada sintética hasta 131.072 tokens. No se simulan los turnos intermedios entre ambos tamaños ni se presupone que todo el historial siga en la caché de la GPU.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 1/2 | 2.847,7 s | 3.604,1 s | 3.604,1 s | 0,14 |
| 2 | 2/2 | 2.824,6 s | 3.598,9 s | 7.227,8 s | 0,14 |
| 3 | 2/2 | 2.985,1 s | 3.710,1 s | 7.450,3 s | 0,14 |
| 4 | 2/2 | 3.253,0 s | 3.968,9 s | 7.967,8 s | 0,13 |
| 5 | 2/2 | 2.576,7 s | 3.341,1 s | 6.712,1 s | 0,15 |
| 6 | 2/2 | 3.078,5 s | 3.792,1 s | 7.614,2 s | 0,13 |
| 7 | 2/2 | 2.496,4 s | 3.255,3 s | 6.540,5 s | 0,16 |
| 8 | 1/2 | 2.609,7 s | 3.332,1 s | 3.332,1 s | 0,15 |
| 9 | 1/2 | 4.761,8 s | 5.476,1 s | 5.476,1 s | 0,09 |
| 10 | 2/2 | 3.406,3 s | 4.113,8 s | 8.257,7 s | 0,12 |
| 11 | 1/2 | 3.006,3 s | 3.766,1 s | 3.766,1 s | 0,14 |
| 12 | 1/2 | 4.420,9 s | 5.119,8 s | 5.119,8 s | 0,10 |
| 13 | 1/2 | 4.929,3 s | 5.619,5 s | 5.619,5 s | 0,09 |
| 14 | 1/2 | 4.081,0 s | 4.915,1 s | 4.915,1 s | 0,10 |
| 15 | 1/2 | 3.301,3 s | 4.051,6 s | 4.051,6 s | 0,13 |
| 16 | 2/2 | 2.315,4 s | 3.082,3 s | 6.194,7 s | 0,17 |
| 17 | 1/2 | 3.620,2 s | 4.441,0 s | 4.441,0 s | 0,12 |
| 18 | 2/2 | 2.153,2 s | 2.874,3 s | 5.778,6 s | 0,18 |
| 19 | 1/2 | 3.915,6 s | 4.748,0 s | 4.748,0 s | 0,11 |
| 20 | 2/2 | 2.649,0 s | 3.435,7 s | 6.901,4 s | 0,15 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 131.072 + 512 | 2.847,7 s | 3.604,1 s | 0,68 | Completa |
| 2 | 1 | 131.072 + 512 | 1.228,7 s | 2.081,7 s | 0,60 | Completa |
| 2 | 2 | 131.840 + 512 | 4.420,5 s | 5.116,1 s | 0,73 | Completa |
| 3 | 1 | 131.072 + 512 | 1.577,5 s | 2.292,2 s | 0,71 | Completa |
| 3 | 2 | 131.840 + 512 | 4.392,8 s | 5.128,1 s | 0,69 | Completa |
| 4 | 1 | 131.072 + 512 | 2.086,5 s | 2.761,6 s | 0,76 | Completa |
| 4 | 2 | 131.840 + 512 | 4.419,4 s | 5.176,2 s | 0,68 | Completa |
| 5 | 1 | 131.072 + 512 | 865,9 s | 1.557,0 s | 0,74 | Completa |
| 5 | 2 | 131.840 + 512 | 4.287,4 s | 5.125,1 s | 0,61 | Completa |
| 6 | 1 | 131.072 + 512 | 1.914,5 s | 2.612,4 s | 0,73 | Completa |
| 6 | 2 | 131.840 + 512 | 4.242,4 s | 4.971,8 s | 0,70 | Completa |
| 7 | 1 | 131.072 + 512 | 554,8 s | 1.247,3 s | 0,74 | Completa |
| 7 | 2 | 131.840 + 512 | 4.438,0 s | 5.263,2 s | 0,62 | Completa |
| 8 | 1 | 131.072 + 512 | 2.609,7 s | 3.332,1 s | 0,71 | Completa |
| 9 | 1 | 131.072 + 512 | 4.761,8 s | 5.476,1 s | 0,72 | Completa |
| 10 | 1 | 131.072 + 512 | 2.254,2 s | 2.918,7 s | 0,77 | Completa |
| 10 | 2 | 131.840 + 512 | 4.558,3 s | 5.309,0 s | 0,68 | Completa |
| 11 | 1 | 131.072 + 512 | 3.006,3 s | 3.766,1 s | 0,67 | Completa |
| 12 | 1 | 131.072 + 512 | 4.420,9 s | 5.119,8 s | 0,73 | Completa |
| 13 | 1 | 131.072 + 512 | 4.929,3 s | 5.619,5 s | 0,74 | Completa |
| 14 | 1 | 131.072 + 512 | 4.081,0 s | 4.915,1 s | 0,61 | Completa |
| 15 | 1 | 131.072 + 512 | 3.301,3 s | 4.051,6 s | 0,68 | Completa |
| 16 | 1 | 131.072 + 512 | 259,5 s | 1.056,5 s | 0,64 | Completa |
| 16 | 2 | 131.840 + 512 | 4.371,4 s | 5.108,2 s | 0,69 | Completa |
| 17 | 1 | 131.072 + 512 | 3.620,2 s | 4.441,0 s | 0,62 | Completa |
| 18 | 1 | 131.072 + 512 | 126,5 s | 889,2 s | 0,67 | Completa |
| 18 | 2 | 131.840 + 512 | 4.179,8 s | 4.859,4 s | 0,75 | Completa |
| 19 | 1 | 131.072 + 512 | 3.915,6 s | 4.748,0 s | 0,61 | Completa |
| 20 | 1 | 131.072 + 512 | 1.061,4 s | 1.914,7 s | 0,60 | Completa |
| 20 | 2 | 131.840 + 512 | 4.236,7 s | 4.956,7 s | 0,71 | Completa |

No hay un resultado final registrado para 10 turnos previstos. Pueden incluir peticiones pendientes al interrumpirse la prueba y turnos posteriores que no llegaron a enviarse. No se cuentan como respuestas recibidas.

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)
