# 10 usuarios · 70% · historial inicial de 65.536 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **20/20**. Tiempo de la prueba: **2.036,6 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 10/10 | 286,0 s | 828,1 s | 828,1 s | 1.503,3 s | 0,75 tokens/s | No cumple |
| 2 | 10/10 | 357,4 s | 550,9 s | 550,9 s | 1.120,8 s | 0,74 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 402,0 s |
| Tiempo medio de respuesta completa | 940,7 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,9% |
| Menor memoria disponible | 29,34 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 7 / 7 |
| Máximo en cola | 9 |
| Recálculos | 33 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 5,03 |
| Suma de tiempos individuales | 18.814,7 s |
| Tiempo total de la prueba, incluyendo pausas | 2.036,6 s |
| Espera máxima sin datos en una conexión | 7.200 s |
| Plazo máximo configurado para todo el grupo | 10.800 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Historial de origen

Esta prueba continúa los historiales de [la etapa anterior](../memoria-70-10-usuarios-historial-32768-tres-turnos/README.md), conservando sus respuestas reales. Antes del primer turno se añade entrada sintética hasta 65.536 tokens. No se simulan los turnos intermedios entre ambos tamaños ni se presupone que todo el historial siga en la caché de la GPU.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 2/2 | 163,0 s | 773,0 s | 1.576,0 s | 0,65 |
| 2 | 2/2 | 492,6 s | 993,6 s | 2.017,3 s | 0,51 |
| 3 | 2/2 | 324,8 s | 972,0 s | 1.974,0 s | 0,52 |
| 4 | 2/2 | 555,0 s | 998,0 s | 2.026,0 s | 0,51 |
| 5 | 2/2 | 418,5 s | 983,6 s | 1.997,1 s | 0,51 |
| 6 | 2/2 | 479,8 s | 987,4 s | 2.004,7 s | 0,51 |
| 7 | 2/2 | 516,5 s | 990,7 s | 2.011,4 s | 0,51 |
| 8 | 2/2 | 624,1 s | 1.003,0 s | 2.036,0 s | 0,50 |
| 9 | 2/2 | 256,2 s | 896,8 s | 1.823,6 s | 0,56 |
| 10 | 2/2 | 189,5 s | 809,3 s | 1.648,6 s | 0,62 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 65.536 + 512 | 52,5 s | 600,4 s | 0,93 | Completa |
| 1 | 2 | 66.304 + 512 | 273,4 s | 945,6 s | 0,76 | Completa |
| 2 | 1 | 65.536 + 512 | 678,3 s | 1.360,8 s | 0,75 | Completa |
| 2 | 2 | 66.304 + 512 | 306,9 s | 626,5 s | 1,60 | Completa |
| 3 | 1 | 65.536 + 512 | 220,5 s | 823,2 s | 0,85 | Completa |
| 3 | 2 | 66.304 + 512 | 429,1 s | 1.120,8 s | 0,74 | Completa |
| 4 | 1 | 65.536 + 512 | 752,5 s | 1.430,8 s | 0,75 | Completa |
| 4 | 2 | 66.304 + 512 | 357,4 s | 565,2 s | 2,46 | Completa |
| 5 | 1 | 65.536 + 512 | 286,0 s | 899,0 s | 0,83 | Completa |
| 5 | 2 | 66.304 + 512 | 550,9 s | 1.068,1 s | 0,99 | Completa |
| 6 | 1 | 65.536 + 512 | 423,3 s | 986,2 s | 0,91 | Completa |
| 6 | 2 | 66.304 + 512 | 536,3 s | 988,5 s | 1,13 | Completa |
| 7 | 1 | 65.536 + 512 | 561,7 s | 1.123,8 s | 0,91 | Completa |
| 7 | 2 | 66.304 + 512 | 471,4 s | 857,6 s | 1,32 | Completa |
| 8 | 1 | 65.536 + 512 | 828,1 s | 1.503,3 s | 0,76 | Completa |
| 8 | 2 | 66.304 + 512 | 420,1 s | 502,7 s | 6,19 | Completa |
| 9 | 1 | 65.536 + 512 | 161,1 s | 749,3 s | 0,87 | Completa |
| 9 | 2 | 66.304 + 512 | 351,3 s | 1.044,2 s | 0,74 | Completa |
| 10 | 1 | 65.536 + 512 | 104,6 s | 673,4 s | 0,90 | Completa |
| 10 | 2 | 66.304 + 512 | 274,4 s | 945,2 s | 0,76 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
