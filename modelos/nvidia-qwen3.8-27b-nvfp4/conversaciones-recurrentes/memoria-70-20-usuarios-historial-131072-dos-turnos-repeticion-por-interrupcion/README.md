# 20 usuarios · 70% · historial inicial de 131.072 tokens · repetición tras interrupción

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **40/40**. Tiempo de la prueba: **8.496,0 s**.

Se repite la carga del [intento interrumpido](../memoria-70-20-usuarios-historial-131072-dos-turnos/README.md), después de recrear el contenedor. Ambos intentos se conservan por separado. Las cifras de este informe corresponden exclusivamente a esta repetición; no se suman respuestas del intento anterior.


Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 1.855,1 s | 3.930,5 s | 4.068,9 s | 4.527,5 s | 0,72 tokens/s | No cumple |
| 2 | 20/20 | 3.624,0 s | 3.747,5 s | 3.767,6 s | 4.357,9 s | 0,74 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 2.824,2 s |
| Tiempo medio de respuesta completa | 3.416,1 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,6% |
| Pico del sistema / GB10 | 76,0% |
| Menor memoria disponible | 29,23 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 4 / 4 |
| Máximo en cola | 19 |
| Recálculos | 95 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 2,41 |
| Suma de tiempos individuales | 136.644,1 s |
| Tiempo total de la prueba, incluyendo pausas | 8.496,0 s |
| Espera máxima sin datos en una conexión | 10.800 s |
| Plazo máximo configurado para todo el grupo | 14.400 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Historial de origen

Esta prueba continúa los historiales de [la etapa anterior](../memoria-70-20-usuarios-historial-65536-dos-turnos/README.md), conservando sus respuestas reales. Antes del primer turno se añade entrada sintética hasta 131.072 tokens. No se simulan los turnos intermedios entre ambos tamaños ni se presupone que todo el historial siga en la caché de la GPU.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 2/2 | 2.536,4 s | 3.131,3 s | 6.292,7 s | 0,16 |
| 2 | 2/2 | 2.055,5 s | 2.687,8 s | 5.405,5 s | 0,19 |
| 3 | 2/2 | 2.180,4 s | 2.837,9 s | 5.705,9 s | 0,18 |
| 4 | 2/2 | 2.120,5 s | 2.758,0 s | 5.546,1 s | 0,18 |
| 5 | 2/2 | 2.857,3 s | 3.459,7 s | 6.949,4 s | 0,15 |
| 6 | 2/2 | 3.201,4 s | 3.796,0 s | 7.622,1 s | 0,13 |
| 7 | 2/2 | 3.908,2 s | 4.232,0 s | 8.494,0 s | 0,12 |
| 8 | 2/2 | 3.771,0 s | 4.217,6 s | 8.465,2 s | 0,12 |
| 9 | 2/2 | 2.811,3 s | 3.398,6 s | 6.827,2 s | 0,15 |
| 10 | 2/2 | 2.683,4 s | 3.278,1 s | 6.586,3 s | 0,16 |
| 11 | 2/2 | 3.074,7 s | 3.634,6 s | 7.299,3 s | 0,14 |
| 12 | 2/2 | 2.459,1 s | 3.064,0 s | 6.158,1 s | 0,17 |
| 13 | 2/2 | 2.959,0 s | 3.570,0 s | 7.169,9 s | 0,14 |
| 14 | 2/2 | 2.327,4 s | 2.973,8 s | 5.977,7 s | 0,17 |
| 15 | 2/2 | 3.502,1 s | 4.177,2 s | 8.384,4 s | 0,12 |
| 16 | 2/2 | 1.912,4 s | 2.544,2 s | 5.118,5 s | 0,20 |
| 17 | 2/2 | 3.652,1 s | 4.205,3 s | 8.440,6 s | 0,12 |
| 18 | 2/2 | 3.283,2 s | 3.904,3 s | 7.838,7 s | 0,13 |
| 19 | 2/2 | 1.779,1 s | 2.370,9 s | 4.771,8 s | 0,21 |
| 20 | 2/2 | 3.409,0 s | 4.080,6 s | 8.191,1 s | 0,13 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 131.072 + 512 | 1.573,5 s | 2.159,8 s | 0,87 | Completa |
| 1 | 2 | 131.840 + 512 | 3.499,4 s | 4.102,8 s | 0,85 | Completa |
| 2 | 1 | 131.072 + 512 | 437,3 s | 1.017,6 s | 0,88 | Completa |
| 2 | 2 | 131.840 + 512 | 3.673,7 s | 4.357,9 s | 0,75 | Completa |
| 3 | 1 | 131.072 + 512 | 859,2 s | 1.573,7 s | 0,72 | Completa |
| 3 | 2 | 131.840 + 512 | 3.501,5 s | 4.102,2 s | 0,85 | Completa |
| 4 | 1 | 131.072 + 512 | 694,5 s | 1.275,5 s | 0,88 | Completa |
| 4 | 2 | 131.840 + 512 | 3.546,6 s | 4.240,6 s | 0,74 | Completa |
| 5 | 1 | 131.072 + 512 | 2.157,2 s | 2.752,6 s | 0,86 | Completa |
| 5 | 2 | 131.840 + 512 | 3.557,5 s | 4.166,8 s | 0,84 | Completa |
| 6 | 1 | 131.072 + 512 | 2.721,8 s | 3.340,9 s | 0,83 | Completa |
| 6 | 2 | 131.840 + 512 | 3.681,0 s | 4.251,2 s | 0,90 | Completa |
| 7 | 1 | 131.072 + 512 | 4.068,9 s | 4.642,2 s | 0,89 | Completa |
| 7 | 2 | 131.840 + 512 | 3.747,5 s | 3.821,8 s | 6,88 | Completa |
| 8 | 1 | 131.072 + 512 | 3.930,5 s | 4.527,5 s | 0,86 | Completa |
| 8 | 2 | 131.840 + 512 | 3.611,5 s | 3.907,7 s | 1,73 | Completa |
| 9 | 1 | 131.072 + 512 | 1.855,1 s | 2.408,2 s | 0,92 | Completa |
| 9 | 2 | 131.840 + 512 | 3.767,6 s | 4.389,0 s | 0,82 | Completa |
| 10 | 1 | 131.072 + 512 | 1.715,6 s | 2.279,7 s | 0,91 | Completa |
| 10 | 2 | 131.840 + 512 | 3.651,1 s | 4.276,6 s | 0,82 | Completa |
| 11 | 1 | 131.072 + 512 | 2.479,5 s | 3.108,8 s | 0,81 | Completa |
| 11 | 2 | 131.840 + 512 | 3.670,0 s | 4.160,5 s | 1,04 | Completa |
| 12 | 1 | 131.072 + 512 | 1.292,5 s | 1.892,9 s | 0,85 | Completa |
| 12 | 2 | 131.840 + 512 | 3.625,6 s | 4.235,2 s | 0,84 | Completa |
| 13 | 1 | 131.072 + 512 | 2.351,1 s | 2.976,0 s | 0,82 | Completa |
| 13 | 2 | 131.840 + 512 | 3.566,9 s | 4.163,9 s | 0,86 | Completa |
| 14 | 1 | 131.072 + 512 | 999,0 s | 1.711,6 s | 0,72 | Completa |
| 14 | 2 | 131.840 + 512 | 3.655,7 s | 4.236,1 s | 0,88 | Completa |
| 15 | 1 | 131.072 + 512 | 3.365,6 s | 4.056,9 s | 0,74 | Completa |
| 15 | 2 | 131.840 + 512 | 3.638,7 s | 4.297,5 s | 0,78 | Completa |
| 16 | 1 | 131.072 + 512 | 200,8 s | 855,2 s | 0,78 | Completa |
| 16 | 2 | 131.840 + 512 | 3.624,0 s | 4.233,3 s | 0,84 | Completa |
| 17 | 1 | 131.072 + 512 | 3.646,3 s | 4.230,0 s | 0,88 | Completa |
| 17 | 2 | 131.840 + 512 | 3.657,8 s | 4.180,7 s | 0,98 | Completa |
| 18 | 1 | 131.072 + 512 | 2.989,3 s | 3.666,5 s | 0,75 | Completa |
| 18 | 2 | 131.840 + 512 | 3.577,1 s | 4.142,2 s | 0,90 | Completa |
| 19 | 1 | 131.072 + 512 | 96,8 s | 717,7 s | 0,82 | Completa |
| 19 | 2 | 131.840 + 512 | 3.461,5 s | 4.024,1 s | 0,91 | Completa |
| 20 | 1 | 131.072 + 512 | 3.229,3 s | 3.919,0 s | 0,74 | Completa |
| 20 | 2 | 131.840 + 512 | 3.588,6 s | 4.242,2 s | 0,78 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
