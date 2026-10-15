# 30 usuarios · 70% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **90/90**. Tiempo de la prueba: **551,5 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 30/30 | 79,6 s | 168,1 s | 173,7 s | 264,8 s | 2,18 tokens/s | No cumple |
| 2 | 30/30 | 2,2 s | 5,2 s | 5,2 s | 115,3 s | 4,46 tokens/s | No cumple |
| 3 | 30/30 | 5,4 s | 15,8 s | 16,1 s | 122,5 s | 4,20 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 31,5 s |
| Tiempo medio de respuesta completa | 163,0 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,6% |
| Menor memoria disponible | 29,67 GiB |
| Pico de caché | 63,9% |
| Máximo activo / respuestas solapadas | 30 / 30 |
| Máximo en cola | 29 |
| Recálculos | 0 |
| Tokens recuperados de caché | 493.920 |
| Tokens/s de todo el grupo, incluyendo pausas | 83,55 |
| Suma de tiempos individuales | 14.669,8 s |
| Tiempo total de la prueba, incluyendo pausas | 551,5 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 42,5 s | 163,5 s | 550,5 s | 2,79 |
| 2 | 3/3 | 64,9 s | 163,7 s | 551,2 s | 2,79 |
| 3 | 3/3 | 2,7 s | 159,4 s | 538,2 s | 2,85 |
| 4 | 3/3 | 7,6 s | 161,9 s | 545,6 s | 2,82 |
| 5 | 3/3 | 26,6 s | 163,3 s | 550,0 s | 2,79 |
| 6 | 3/3 | 48,4 s | 163,6 s | 550,9 s | 2,79 |
| 7 | 3/3 | 12,7 s | 162,9 s | 548,6 s | 2,80 |
| 8 | 3/3 | 16,4 s | 163,1 s | 549,3 s | 2,80 |
| 9 | 3/3 | 56,0 s | 163,7 s | 551,0 s | 2,79 |
| 10 | 3/3 | 60,5 s | 163,7 s | 551,1 s | 2,79 |
| 11 | 3/3 | 52,7 s | 163,6 s | 550,9 s | 2,79 |
| 12 | 3/3 | 63,0 s | 163,7 s | 551,1 s | 2,79 |
| 13 | 3/3 | 20,5 s | 163,2 s | 549,7 s | 2,79 |
| 14 | 3/3 | 9,2 s | 162,2 s | 546,5 s | 2,81 |
| 15 | 3/3 | 22,6 s | 163,3 s | 549,8 s | 2,79 |
| 16 | 3/3 | 24,4 s | 163,3 s | 549,8 s | 2,79 |
| 17 | 3/3 | 33,4 s | 163,4 s | 550,3 s | 2,79 |
| 18 | 3/3 | 18,4 s | 163,2 s | 549,5 s | 2,80 |
| 19 | 3/3 | 10,9 s | 162,6 s | 547,7 s | 2,80 |
| 20 | 3/3 | 14,4 s | 163,0 s | 549,0 s | 2,80 |
| 21 | 3/3 | 4,3 s | 160,5 s | 541,5 s | 2,84 |
| 22 | 3/3 | 41,1 s | 163,5 s | 550,6 s | 2,79 |
| 23 | 3/3 | 38,0 s | 163,5 s | 550,4 s | 2,79 |
| 24 | 3/3 | 29,1 s | 163,4 s | 550,1 s | 2,79 |
| 25 | 3/3 | 49,9 s | 163,6 s | 550,8 s | 2,79 |
| 26 | 3/3 | 45,2 s | 163,5 s | 550,6 s | 2,79 |
| 27 | 3/3 | 36,0 s | 163,5 s | 550,4 s | 2,79 |
| 28 | 3/3 | 57,7 s | 163,7 s | 551,0 s | 2,79 |
| 29 | 3/3 | 31,1 s | 163,4 s | 550,1 s | 2,79 |
| 30 | 3/3 | 5,9 s | 161,3 s | 543,8 s | 2,82 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 512 | 115,5 s | 260,7 s | 3,52 | Completa |
| 1 | 2 | 8.960 + 512 | 3,3 s | 109,4 s | 4,82 | Completa |
| 1 | 3 | 9.728 + 512 | 8,8 s | 120,4 s | 4,58 | Completa |
| 2 | 1 | 8.192 + 512 | 173,7 s | 265,2 s | 5,59 | Completa |
| 2 | 2 | 8.960 + 512 | 4,8 s | 105,5 s | 5,07 | Completa |
| 2 | 3 | 9.728 + 512 | 16,1 s | 120,5 s | 4,89 | Completa |
| 3 | 1 | 8.192 + 512 | 6,7 s | 245,2 s | 2,14 | Completa |
| 3 | 2 | 8.960 + 512 | 0,6 s | 114,0 s | 4,51 | Completa |
| 3 | 3 | 9.728 + 512 | 0,7 s | 119,1 s | 4,32 | Completa |
| 4 | 1 | 8.192 + 512 | 21,1 s | 248,0 s | 2,25 | Completa |
| 4 | 2 | 8.960 + 512 | 0,8 s | 115,3 s | 4,46 | Completa |
| 4 | 3 | 9.728 + 512 | 0,8 s | 122,3 s | 4,21 | Completa |
| 5 | 1 | 8.192 + 512 | 73,8 s | 256,2 s | 2,80 | Completa |
| 5 | 2 | 8.960 + 512 | 1,5 s | 113,0 s | 4,58 | Completa |
| 5 | 3 | 9.728 + 512 | 4,6 s | 120,8 s | 4,40 | Completa |
| 6 | 1 | 8.192 + 512 | 128,2 s | 261,9 s | 3,82 | Completa |
| 6 | 2 | 8.960 + 512 | 4,4 s | 108,5 s | 4,91 | Completa |
| 6 | 3 | 9.728 + 512 | 12,8 s | 120,5 s | 4,74 | Completa |
| 7 | 1 | 8.192 + 512 | 36,1 s | 250,7 s | 2,38 | Completa |
| 7 | 2 | 8.960 + 512 | 0,8 s | 115,4 s | 4,46 | Completa |
| 7 | 3 | 9.728 + 512 | 1,1 s | 122,5 s | 4,21 | Completa |
| 8 | 1 | 8.192 + 512 | 46,5 s | 252,4 s | 2,48 | Completa |
| 8 | 2 | 8.960 + 512 | 0,8 s | 114,9 s | 4,48 | Completa |
| 8 | 3 | 9.728 + 512 | 1,9 s | 122,0 s | 4,25 | Completa |
| 9 | 1 | 8.192 + 512 | 147,7 s | 263,4 s | 4,42 | Completa |
| 9 | 2 | 8.960 + 512 | 5,2 s | 107,1 s | 5,01 | Completa |
| 9 | 3 | 9.728 + 512 | 15,1 s | 120,5 s | 4,85 | Completa |
| 10 | 1 | 8.192 + 512 | 161,2 s | 264,3 s | 4,96 | Completa |
| 10 | 2 | 8.960 + 512 | 5,2 s | 106,3 s | 5,06 | Completa |
| 10 | 3 | 9.728 + 512 | 15,0 s | 120,4 s | 4,85 | Completa |
| 11 | 1 | 8.192 + 512 | 141,1 s | 262,9 s | 4,20 | Completa |
| 11 | 2 | 8.960 + 512 | 4,4 s | 107,5 s | 4,96 | Completa |
| 11 | 3 | 9.728 + 512 | 12,7 s | 120,4 s | 4,74 | Completa |
| 12 | 1 | 8.192 + 512 | 168,1 s | 264,8 s | 5,29 | Completa |
| 12 | 2 | 8.960 + 512 | 5,2 s | 105,9 s | 5,07 | Completa |
| 12 | 3 | 9.728 + 512 | 15,8 s | 120,4 s | 4,88 | Completa |
| 13 | 1 | 8.192 + 512 | 57,1 s | 254,0 s | 2,60 | Completa |
| 13 | 2 | 8.960 + 512 | 1,2 s | 114,2 s | 4,52 | Completa |
| 13 | 3 | 9.728 + 512 | 3,2 s | 121,4 s | 4,32 | Completa |
| 14 | 1 | 8.192 + 512 | 26,1 s | 248,9 s | 2,29 | Completa |
| 14 | 2 | 8.960 + 512 | 0,7 s | 115,3 s | 4,46 | Completa |
| 14 | 3 | 9.728 + 512 | 0,7 s | 122,3 s | 4,20 | Completa |
| 15 | 1 | 8.192 + 512 | 62,6 s | 254,7 s | 2,66 | Completa |
| 15 | 2 | 8.960 + 512 | 1,2 s | 113,8 s | 4,54 | Completa |
| 15 | 3 | 9.728 + 512 | 4,0 s | 121,3 s | 4,36 | Completa |
| 16 | 1 | 8.192 + 512 | 68,2 s | 255,5 s | 2,73 | Completa |
| 16 | 2 | 8.960 + 512 | 1,3 s | 113,4 s | 4,56 | Completa |
| 16 | 3 | 9.728 + 512 | 3,7 s | 120,9 s | 4,36 | Completa |
| 17 | 1 | 8.192 + 512 | 91,2 s | 258,3 s | 3,06 | Completa |
| 17 | 2 | 8.960 + 512 | 2,5 s | 111,5 s | 4,69 | Completa |
| 17 | 3 | 9.728 + 512 | 6,5 s | 120,5 s | 4,48 | Completa |
| 18 | 1 | 8.192 + 512 | 51,8 s | 253,2 s | 2,54 | Completa |
| 18 | 2 | 8.960 + 512 | 0,9 s | 114,6 s | 4,49 | Completa |
| 18 | 3 | 9.728 + 512 | 2,5 s | 121,7 s | 4,29 | Completa |
| 19 | 1 | 8.192 + 512 | 31,0 s | 249,8 s | 2,34 | Completa |
| 19 | 2 | 8.960 + 512 | 0,7 s | 115,3 s | 4,46 | Completa |
| 19 | 3 | 9.728 + 512 | 0,8 s | 122,5 s | 4,20 | Completa |
| 20 | 1 | 8.192 + 512 | 41,3 s | 251,5 s | 2,43 | Completa |
| 20 | 2 | 8.960 + 512 | 0,9 s | 115,2 s | 4,47 | Completa |
| 20 | 3 | 9.728 + 512 | 1,1 s | 122,2 s | 4,22 | Completa |
| 21 | 1 | 8.192 + 512 | 11,5 s | 246,1 s | 2,18 | Completa |
| 21 | 2 | 8.960 + 512 | 0,7 s | 114,6 s | 4,48 | Completa |
| 21 | 3 | 9.728 + 512 | 0,7 s | 120,8 s | 4,26 | Completa |
| 22 | 1 | 8.192 + 512 | 109,3 s | 260,1 s | 3,39 | Completa |
| 22 | 2 | 8.960 + 512 | 3,9 s | 110,0 s | 4,82 | Completa |
| 22 | 3 | 9.728 + 512 | 10,2 s | 120,5 s | 4,63 | Completa |
| 23 | 1 | 8.192 + 512 | 103,2 s | 259,5 s | 3,27 | Completa |
| 23 | 2 | 8.960 + 512 | 3,3 s | 110,4 s | 4,77 | Completa |
| 23 | 3 | 9.728 + 512 | 7,6 s | 120,4 s | 4,53 | Completa |
| 24 | 1 | 8.192 + 512 | 79,6 s | 256,9 s | 2,88 | Completa |
| 24 | 2 | 8.960 + 512 | 2,2 s | 112,5 s | 4,63 | Completa |
| 24 | 3 | 9.728 + 512 | 5,6 s | 120,7 s | 4,44 | Completa |
| 25 | 1 | 8.192 + 512 | 134,6 s | 262,4 s | 4,00 | Completa |
| 25 | 2 | 8.960 + 512 | 3,8 s | 107,9 s | 4,91 | Completa |
| 25 | 3 | 9.728 + 512 | 11,3 s | 120,4 s | 4,68 | Completa |
| 26 | 1 | 8.192 + 512 | 121,8 s | 261,3 s | 3,66 | Completa |
| 26 | 2 | 8.960 + 512 | 3,7 s | 108,9 s | 4,86 | Completa |
| 26 | 3 | 9.728 + 512 | 10,1 s | 120,4 s | 4,63 | Completa |
| 27 | 1 | 8.192 + 512 | 97,2 s | 258,9 s | 3,16 | Completa |
| 27 | 2 | 8.960 + 512 | 2,9 s | 110,9 s | 4,73 | Completa |
| 27 | 3 | 9.728 + 512 | 7,7 s | 120,5 s | 4,53 | Completa |
| 28 | 1 | 8.192 + 512 | 154,5 s | 263,9 s | 4,67 | Completa |
| 28 | 2 | 8.960 + 512 | 4,7 s | 106,7 s | 5,01 | Completa |
| 28 | 3 | 9.728 + 512 | 14,0 s | 120,4 s | 4,80 | Completa |
| 29 | 1 | 8.192 + 512 | 85,4 s | 257,6 s | 2,97 | Completa |
| 29 | 2 | 8.960 + 512 | 2,4 s | 112,0 s | 4,66 | Completa |
| 29 | 3 | 9.728 + 512 | 5,4 s | 120,5 s | 4,44 | Completa |
| 30 | 1 | 8.192 + 512 | 16,3 s | 247,1 s | 2,21 | Completa |
| 30 | 2 | 8.960 + 512 | 0,7 s | 115,1 s | 4,47 | Completa |
| 30 | 3 | 9.728 + 512 | 0,7 s | 121,6 s | 4,22 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
