# 20 usuarios · 40% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **596,5 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 37,2 s | 151,3 s | 154,9 s | 276,0 s | 3,58 tokens/s | No cumple |
| 2 | 20/20 | 29,4 s | 93,9 s | 133,8 s | 244,4 s | 3,36 tokens/s | No cumple |
| 3 | 20/20 | 21,7 s | 69,8 s | 105,5 s | 176,9 s | 3,14 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 38,8 s |
| Tiempo medio de respuesta completa | 165,3 s |
| Presupuesto configurado | 40% |
| Pico del motor / GB10 | 36,6% |
| Pico del sistema / GB10 | 45,1% |
| Menor memoria disponible | 66,71 GiB |
| Pico de caché | 100,0% |
| Máximo activo / respuestas solapadas | 19 / 18 |
| Máximo en cola | 19 |
| Recálculos | 20 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 51,50 |
| Suma de tiempos individuales | 9.918,1 s |
| Tiempo total de la prueba, incluyendo pausas | 596,5 s |

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 68,7 s | 178,7 s | 596,2 s | 2,58 |
| 2 | 3/3 | 14,5 s | 161,4 s | 544,2 s | 2,82 |
| 3 | 3/3 | 45,8 s | 163,6 s | 550,7 s | 2,79 |
| 4 | 3/3 | 72,7 s | 172,6 s | 577,8 s | 2,66 |
| 5 | 3/3 | 18,4 s | 161,7 s | 545,1 s | 2,82 |
| 6 | 3/3 | 7,9 s | 159,2 s | 537,7 s | 2,86 |
| 7 | 3/3 | 60,8 s | 172,9 s | 578,7 s | 2,65 |
| 8 | 3/3 | 35,4 s | 162,8 s | 548,3 s | 2,80 |
| 9 | 3/3 | 5,6 s | 154,2 s | 522,7 s | 2,94 |
| 10 | 3/3 | 4,4 s | 151,3 s | 513,9 s | 2,99 |
| 11 | 3/3 | 71,7 s | 176,4 s | 589,1 s | 2,61 |
| 12 | 3/3 | 52,4 s | 164,8 s | 554,5 s | 2,77 |
| 13 | 3/3 | 63,9 s | 177,1 s | 591,4 s | 2,60 |
| 14 | 3/3 | 22,6 s | 162,0 s | 545,9 s | 2,81 |
| 15 | 3/3 | 10,5 s | 160,9 s | 542,8 s | 2,83 |
| 16 | 3/3 | 26,7 s | 162,2 s | 546,7 s | 2,81 |
| 17 | 3/3 | 64,5 s | 173,3 s | 579,9 s | 2,65 |
| 18 | 3/3 | 58,1 s | 165,3 s | 555,9 s | 2,76 |
| 19 | 3/3 | 31,1 s | 162,5 s | 547,5 s | 2,81 |
| 20 | 3/3 | 40,6 s | 163,0 s | 549,0 s | 2,80 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 512 | 154,9 s | 280,1 s | 4,08 | Completa |
| 1 | 2 | 8.960 + 512 | 31,9 s | 184,1 s | 3,36 | Completa |
| 1 | 3 | 9.728 + 512 | 19,4 s | 72,0 s | 9,72 | Completa |
| 2 | 1 | 8.192 + 512 | 18,4 s | 156,0 s | 3,71 | Completa |
| 2 | 2 | 8.960 + 512 | 12,5 s | 156,9 s | 3,54 | Completa |
| 2 | 3 | 9.728 + 512 | 12,5 s | 171,3 s | 3,22 | Completa |
| 3 | 1 | 8.192 + 512 | 45,2 s | 160,4 s | 4,44 | Completa |
| 3 | 2 | 8.960 + 512 | 41,5 s | 157,4 s | 4,41 | Completa |
| 3 | 3 | 9.728 + 512 | 50,6 s | 172,9 s | 4,18 | Completa |
| 4 | 1 | 8.192 + 512 | 58,0 s | 162,0 s | 4,91 | Completa |
| 4 | 2 | 8.960 + 512 | 54,4 s | 157,6 s | 4,95 | Completa |
| 4 | 3 | 9.728 + 512 | 105,5 s | 198,2 s | 5,51 | Completa |
| 5 | 1 | 8.192 + 512 | 22,0 s | 156,7 s | 3,79 | Completa |
| 5 | 2 | 8.960 + 512 | 16,0 s | 156,9 s | 3,63 | Completa |
| 5 | 3 | 9.728 + 512 | 17,1 s | 171,5 s | 3,31 | Completa |
| 6 | 1 | 8.192 + 512 | 11,4 s | 154,0 s | 3,58 | Completa |
| 6 | 2 | 8.960 + 512 | 5,7 s | 154,5 s | 3,44 | Completa |
| 6 | 3 | 9.728 + 512 | 6,7 s | 169,2 s | 3,14 | Completa |
| 7 | 1 | 8.192 + 512 | 62,4 s | 162,5 s | 5,11 | Completa |
| 7 | 2 | 8.960 + 512 | 90,9 s | 239,8 s | 3,43 | Completa |
| 7 | 3 | 9.728 + 512 | 29,1 s | 116,5 s | 5,85 | Completa |
| 8 | 1 | 8.192 + 512 | 37,2 s | 159,2 s | 4,19 | Completa |
| 8 | 2 | 8.960 + 512 | 32,5 s | 157,2 s | 4,10 | Completa |
| 8 | 3 | 9.728 + 512 | 36,5 s | 171,8 s | 3,78 | Completa |
| 9 | 1 | 8.192 + 512 | 8,0 s | 149,4 s | 3,61 | Completa |
| 9 | 2 | 8.960 + 512 | 4,1 s | 149,4 s | 3,52 | Completa |
| 9 | 3 | 9.728 + 512 | 4,7 s | 163,9 s | 3,21 | Completa |
| 10 | 1 | 8.192 + 512 | 4,6 s | 145,3 s | 3,63 | Completa |
| 10 | 2 | 8.960 + 512 | 4,0 s | 147,2 s | 3,57 | Completa |
| 10 | 3 | 9.728 + 512 | 4,5 s | 161,5 s | 3,26 | Completa |
| 11 | 1 | 8.192 + 512 | 70,4 s | 164,5 s | 5,43 | Completa |
| 11 | 2 | 8.960 + 512 | 133,8 s | 284,5 s | 3,39 | Completa |
| 11 | 3 | 9.728 + 512 | 10,9 s | 80,0 s | 7,39 | Completa |
| 12 | 1 | 8.192 + 512 | 49,4 s | 161,0 s | 4,58 | Completa |
| 12 | 2 | 8.960 + 512 | 46,6 s | 157,5 s | 4,61 | Completa |
| 12 | 3 | 9.728 + 512 | 61,2 s | 176,1 s | 4,45 | Completa |
| 13 | 1 | 8.192 + 512 | 151,3 s | 276,0 s | 4,10 | Completa |
| 13 | 2 | 8.960 + 512 | 29,4 s | 181,5 s | 3,36 | Completa |
| 13 | 3 | 9.728 + 512 | 11,1 s | 73,8 s | 8,14 | Completa |
| 14 | 1 | 8.192 + 512 | 25,6 s | 157,4 s | 3,88 | Completa |
| 14 | 2 | 8.960 + 512 | 20,4 s | 157,1 s | 3,74 | Completa |
| 14 | 3 | 9.728 + 512 | 21,7 s | 171,5 s | 3,41 | Completa |
| 15 | 1 | 8.192 + 512 | 14,9 s | 155,3 s | 3,64 | Completa |
| 15 | 2 | 8.960 + 512 | 8,4 s | 156,8 s | 3,45 | Completa |
| 15 | 3 | 9.728 + 512 | 8,2 s | 170,8 s | 3,14 | Completa |
| 16 | 1 | 8.192 + 512 | 29,4 s | 158,0 s | 3,97 | Completa |
| 16 | 2 | 8.960 + 512 | 24,1 s | 157,1 s | 3,84 | Completa |
| 16 | 3 | 9.728 + 512 | 26,5 s | 171,6 s | 3,52 | Completa |
| 17 | 1 | 8.192 + 512 | 66,9 s | 163,0 s | 5,32 | Completa |
| 17 | 2 | 8.960 + 512 | 93,9 s | 244,4 s | 3,40 | Completa |
| 17 | 3 | 9.728 + 512 | 32,9 s | 112,6 s | 6,41 | Completa |
| 18 | 1 | 8.192 + 512 | 53,7 s | 161,5 s | 4,74 | Completa |
| 18 | 2 | 8.960 + 512 | 50,9 s | 157,5 s | 4,79 | Completa |
| 18 | 3 | 9.728 + 512 | 69,8 s | 176,9 s | 4,77 | Completa |
| 19 | 1 | 8.192 + 512 | 33,2 s | 158,6 s | 4,08 | Completa |
| 19 | 2 | 8.960 + 512 | 28,6 s | 157,2 s | 3,97 | Completa |
| 19 | 3 | 9.728 + 512 | 31,4 s | 171,6 s | 3,64 | Completa |
| 20 | 1 | 8.192 + 512 | 41,2 s | 159,8 s | 4,31 | Completa |
| 20 | 2 | 8.960 + 512 | 38,2 s | 157,4 s | 4,29 | Completa |
| 20 | 3 | 9.728 + 512 | 42,5 s | 171,8 s | 3,95 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
