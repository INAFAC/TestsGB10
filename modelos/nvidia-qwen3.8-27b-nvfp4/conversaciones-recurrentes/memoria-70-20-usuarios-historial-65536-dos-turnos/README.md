# 20 usuarios · 70% · historial inicial de 65.536 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **40/40**. Tiempo de la prueba: **4.289,5 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 828,0 s | 1.712,0 s | 1.868,9 s | 2.336,5 s | 0,67 tokens/s | No cumple |
| 2 | 20/20 | 1.539,9 s | 1.688,8 s | 1.691,2 s | 2.344,9 s | 0,58 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 1.215,2 s |
| Tiempo medio de respuesta completa | 1.862,5 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,9% |
| Menor memoria disponible | 29,34 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 9 / 8 |
| Máximo en cola | 19 |
| Recálculos | 70 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 4,77 |
| Suma de tiempos individuales | 74.499,8 s |
| Tiempo total de la prueba, incluyendo pausas | 4.289,5 s |
| Espera máxima sin datos en una conexión | 7.200 s |
| Plazo máximo configurado para todo el grupo | 10.800 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Historial de origen

Esta prueba continúa los historiales de [la etapa anterior](../memoria-70-20-usuarios-historial-32768-tres-turnos/README.md), conservando sus respuestas reales. Antes del primer turno se añade entrada sintética hasta 65.536 tokens. No se simulan los turnos intermedios entre ambos tamaños ni se presupone que todo el historial siga en la caché de la GPU.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 2/2 | 1.269,7 s | 1.990,0 s | 4.010,0 s | 0,26 |
| 2 | 2/2 | 758,5 s | 1.474,7 s | 2.979,4 s | 0,34 |
| 3 | 2/2 | 1.340,3 s | 2.030,0 s | 4.090,1 s | 0,25 |
| 4 | 2/2 | 1.479,0 s | 2.102,7 s | 4.235,4 s | 0,24 |
| 5 | 2/2 | 1.624,2 s | 2.119,6 s | 4.269,1 s | 0,24 |
| 6 | 2/2 | 786,8 s | 1.515,0 s | 3.059,9 s | 0,33 |
| 7 | 2/2 | 1.190,0 s | 1.911,7 s | 3.853,4 s | 0,27 |
| 8 | 2/2 | 1.230,5 s | 1.950,8 s | 3.931,6 s | 0,26 |
| 9 | 2/2 | 817,4 s | 1.555,3 s | 3.140,6 s | 0,33 |
| 10 | 2/2 | 1.422,6 s | 2.088,6 s | 4.207,1 s | 0,24 |
| 11 | 2/2 | 723,7 s | 1.385,6 s | 2.801,3 s | 0,37 |
| 12 | 2/2 | 951,7 s | 1.675,2 s | 3.380,5 s | 0,30 |
| 13 | 2/2 | 1.701,6 s | 2.125,0 s | 4.280,1 s | 0,24 |
| 14 | 2/2 | 1.704,4 s | 2.129,2 s | 4.288,3 s | 0,24 |
| 15 | 2/2 | 1.052,4 s | 1.782,9 s | 3.595,8 s | 0,28 |
| 16 | 2/2 | 850,1 s | 1.595,5 s | 3.221,1 s | 0,32 |
| 17 | 2/2 | 1.663,5 s | 2.122,5 s | 4.274,9 s | 0,24 |
| 18 | 2/2 | 1.149,8 s | 1.875,3 s | 3.780,5 s | 0,27 |
| 19 | 2/2 | 1.027,6 s | 1.709,5 s | 3.449,0 s | 0,30 |
| 20 | 2/2 | 1.559,2 s | 2.110,9 s | 4.251,9 s | 0,24 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 65.536 + 512 | 976,0 s | 1.635,0 s | 0,78 | Completa |
| 1 | 2 | 66.304 + 512 | 1.563,5 s | 2.344,9 s | 0,65 | Completa |
| 2 | 1 | 65.536 + 512 | 104,4 s | 673,3 s | 0,90 | Completa |
| 2 | 2 | 66.304 + 512 | 1.412,6 s | 2.276,1 s | 0,59 | Completa |
| 3 | 1 | 65.536 + 512 | 1.131,1 s | 1.730,0 s | 0,85 | Completa |
| 3 | 2 | 66.304 + 512 | 1.549,6 s | 2.330,1 s | 0,65 | Completa |
| 4 | 1 | 65.536 + 512 | 1.414,6 s | 2.037,8 s | 0,82 | Completa |
| 4 | 2 | 66.304 + 512 | 1.543,5 s | 2.167,6 s | 0,82 | Completa |
| 5 | 1 | 65.536 + 512 | 1.564,2 s | 2.186,8 s | 0,82 | Completa |
| 5 | 2 | 66.304 + 512 | 1.684,3 s | 2.052,3 s | 1,39 | Completa |
| 6 | 1 | 65.536 + 512 | 161,1 s | 749,2 s | 0,87 | Completa |
| 6 | 2 | 66.304 + 512 | 1.412,5 s | 2.280,7 s | 0,59 | Completa |
| 7 | 1 | 65.536 + 512 | 828,0 s | 1.485,4 s | 0,78 | Completa |
| 7 | 2 | 66.304 + 512 | 1.552,0 s | 2.337,9 s | 0,65 | Completa |
| 8 | 1 | 65.536 + 512 | 902,2 s | 1.559,2 s | 0,78 | Completa |
| 8 | 2 | 66.304 + 512 | 1.558,8 s | 2.342,4 s | 0,65 | Completa |
| 9 | 1 | 65.536 + 512 | 220,5 s | 823,1 s | 0,85 | Completa |
| 9 | 2 | 66.304 + 512 | 1.414,3 s | 2.287,5 s | 0,59 | Completa |
| 10 | 1 | 65.536 + 512 | 1.313,5 s | 1.874,7 s | 0,91 | Completa |
| 10 | 2 | 66.304 + 512 | 1.531,7 s | 2.302,4 s | 0,66 | Completa |
| 11 | 1 | 65.536 + 512 | 52,4 s | 600,4 s | 0,93 | Completa |
| 11 | 2 | 66.304 + 512 | 1.395,0 s | 2.170,9 s | 0,66 | Completa |
| 12 | 1 | 65.536 + 512 | 423,5 s | 984,5 s | 0,91 | Completa |
| 12 | 2 | 66.304 + 512 | 1.480,0 s | 2.366,0 s | 0,58 | Completa |
| 13 | 1 | 65.536 + 512 | 1.712,0 s | 2.336,5 s | 0,82 | Completa |
| 13 | 2 | 66.304 + 512 | 1.691,2 s | 1.913,6 s | 2,30 | Completa |
| 14 | 1 | 65.536 + 512 | 1.868,9 s | 2.637,1 s | 0,67 | Completa |
| 14 | 2 | 66.304 + 512 | 1.539,9 s | 1.621,2 s | 6,28 | Completa |
| 15 | 1 | 65.536 + 512 | 678,2 s | 1.336,6 s | 0,78 | Completa |
| 15 | 2 | 66.304 + 512 | 1.426,6 s | 2.229,2 s | 0,64 | Completa |
| 16 | 1 | 65.536 + 512 | 286,0 s | 899,0 s | 0,83 | Completa |
| 16 | 2 | 66.304 + 512 | 1.414,2 s | 2.292,1 s | 0,58 | Completa |
| 17 | 1 | 65.536 + 512 | 1.638,2 s | 2.260,6 s | 0,82 | Completa |
| 17 | 2 | 66.304 + 512 | 1.688,8 s | 1.984,4 s | 1,73 | Completa |
| 18 | 1 | 65.536 + 512 | 752,4 s | 1.409,6 s | 0,78 | Completa |
| 18 | 2 | 66.304 + 512 | 1.547,3 s | 2.340,9 s | 0,64 | Completa |
| 19 | 1 | 65.536 + 512 | 561,7 s | 1.121,3 s | 0,91 | Completa |
| 19 | 2 | 66.304 + 512 | 1.493,5 s | 2.297,6 s | 0,64 | Completa |
| 20 | 1 | 65.536 + 512 | 1.488,7 s | 2.111,1 s | 0,82 | Completa |
| 20 | 2 | 66.304 + 512 | 1.629,8 s | 2.110,7 s | 1,06 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
