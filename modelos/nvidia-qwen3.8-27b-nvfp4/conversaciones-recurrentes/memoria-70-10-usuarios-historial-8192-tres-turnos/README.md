# 10 usuarios · 70% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **30/30**. Tiempo de la prueba: **300,6 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 10/10 | 25,9 s | 50,4 s | 50,4 s | 110,0 s | 5,16 tokens/s | No cumple |
| 2 | 10/10 | 1,1 s | 2,1 s | 2,1 s | 65,9 s | 7,82 tokens/s | No cumple |
| 3 | 10/10 | 3,4 s | 5,0 s | 5,0 s | 68,1 s | 7,57 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 11,1 s |
| Tiempo medio de respuesta completa | 80,0 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,8% |
| Menor memoria disponible | 29,45 GiB |
| Pico de caché | 21,7% |
| Máximo activo / respuestas solapadas | 10 / 10 |
| Máximo en cola | 9 |
| Recálculos | 0 |
| Tokens recuperados de caché | 164.640 |
| Tokens/s de todo el grupo, incluyendo pausas | 51,10 |
| Suma de tiempos individuales | 2.401,1 s |
| Tiempo total de la prueba, incluyendo pausas | 300,6 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 14,1 s | 80,1 s | 300,3 s | 5,12 |
| 2 | 3/3 | 8,5 s | 80,0 s | 300,1 s | 5,12 |
| 3 | 3/3 | 2,6 s | 79,8 s | 299,5 s | 5,13 |
| 4 | 3/3 | 17,8 s | 80,1 s | 300,4 s | 5,11 |
| 5 | 3/3 | 12,2 s | 80,1 s | 300,2 s | 5,12 |
| 6 | 3/3 | 19,1 s | 80,1 s | 300,5 s | 5,11 |
| 7 | 3/3 | 15,9 s | 80,1 s | 300,3 s | 5,12 |
| 8 | 3/3 | 6,6 s | 80,0 s | 300,0 s | 5,12 |
| 9 | 3/3 | 10,1 s | 80,0 s | 300,1 s | 5,12 |
| 10 | 3/3 | 4,7 s | 80,0 s | 299,9 s | 5,12 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 512 | 35,9 s | 108,7 s | 7,02 | Completa |
| 1 | 2 | 8.960 + 512 | 1,9 s | 64,2 s | 8,21 | Completa |
| 1 | 3 | 9.728 + 512 | 4,7 s | 67,5 s | 8,14 | Completa |
| 2 | 1 | 8.192 + 512 | 21,0 s | 107,2 s | 5,93 | Completa |
| 2 | 2 | 8.960 + 512 | 1,0 s | 65,1 s | 7,97 | Completa |
| 2 | 3 | 9.728 + 512 | 3,4 s | 67,8 s | 7,94 | Completa |
| 3 | 1 | 8.192 + 512 | 6,6 s | 105,5 s | 5,16 | Completa |
| 3 | 2 | 8.960 + 512 | 0,6 s | 65,9 s | 7,82 | Completa |
| 3 | 3 | 9.728 + 512 | 0,6 s | 68,1 s | 7,57 | Completa |
| 4 | 1 | 8.192 + 512 | 46,3 s | 109,6 s | 8,07 | Completa |
| 4 | 2 | 8.960 + 512 | 2,1 s | 63,4 s | 8,34 | Completa |
| 4 | 3 | 9.728 + 512 | 4,9 s | 67,4 s | 8,18 | Completa |
| 5 | 1 | 8.192 + 512 | 30,8 s | 108,2 s | 6,61 | Completa |
| 5 | 2 | 8.960 + 512 | 1,7 s | 64,5 s | 8,14 | Completa |
| 5 | 3 | 9.728 + 512 | 4,0 s | 67,5 s | 8,06 | Completa |
| 6 | 1 | 8.192 + 512 | 50,4 s | 110,0 s | 8,57 | Completa |
| 6 | 2 | 8.960 + 512 | 1,9 s | 63,1 s | 8,34 | Completa |
| 6 | 3 | 9.728 + 512 | 5,0 s | 67,4 s | 8,19 | Completa |
| 7 | 1 | 8.192 + 512 | 41,0 s | 109,1 s | 7,51 | Completa |
| 7 | 2 | 8.960 + 512 | 2,1 s | 63,8 s | 8,29 | Completa |
| 7 | 3 | 9.728 + 512 | 4,6 s | 67,4 s | 8,14 | Completa |
| 8 | 1 | 8.192 + 512 | 16,1 s | 106,6 s | 5,64 | Completa |
| 8 | 2 | 8.960 + 512 | 1,0 s | 65,5 s | 7,92 | Completa |
| 8 | 3 | 9.728 + 512 | 2,6 s | 67,9 s | 7,83 | Completa |
| 9 | 1 | 8.192 + 512 | 25,9 s | 107,7 s | 6,25 | Completa |
| 9 | 2 | 8.960 + 512 | 1,1 s | 64,8 s | 8,02 | Completa |
| 9 | 3 | 9.728 + 512 | 3,2 s | 67,6 s | 7,94 | Completa |
| 10 | 1 | 8.192 + 512 | 11,3 s | 106,1 s | 5,39 | Completa |
| 10 | 2 | 8.960 + 512 | 0,9 s | 65,8 s | 7,88 | Completa |
| 10 | 3 | 9.728 + 512 | 1,8 s | 68,0 s | 7,72 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
