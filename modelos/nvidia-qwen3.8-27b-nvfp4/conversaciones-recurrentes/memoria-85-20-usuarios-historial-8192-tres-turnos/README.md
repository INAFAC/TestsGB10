# 20 usuarios · 85% · historial inicial de 8.192 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **60/60**. Tiempo de la prueba: **440,8 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 20/20 | 52,6 s | 104,3 s | 109,3 s | 188,8 s | 2,99 tokens/s | No cumple |
| 2 | 20/20 | 2,1 s | 4,7 s | 5,0 s | 98,0 s | 5,25 tokens/s | No cumple |
| 3 | 20/20 | 6,7 s | 12,8 s | 12,8 s | 102,5 s | 5,02 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 22,1 s |
| Tiempo medio de respuesta completa | 126,6 s |
| Presupuesto configurado | 85% |
| Pico del motor / GB10 | 81,6% |
| Pico del sistema / GB10 | 88,6% |
| Menor memoria disponible | 13,90 GiB |
| Pico de caché | 33,1% |
| Máximo activo / respuestas solapadas | 20 / 20 |
| Máximo en cola | 19 |
| Recálculos | 0 |
| Tokens recuperados de caché | 329.280 |
| Tokens/s de todo el grupo, incluyendo pausas | 69,69 |
| Suma de tiempos individuales | 7.596,5 s |
| Tiempo total de la prueba, incluyendo pausas | 440,8 s |

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 10,4 s | 126,5 s | 439,4 s | 3,50 |
| 2 | 3/3 | 26,9 s | 126,7 s | 440,2 s | 3,49 |
| 3 | 3/3 | 4,9 s | 126,3 s | 439,0 s | 3,50 |
| 4 | 3/3 | 8,6 s | 126,5 s | 439,4 s | 3,50 |
| 5 | 3/3 | 31,6 s | 126,7 s | 440,2 s | 3,49 |
| 6 | 3/3 | 2,7 s | 126,2 s | 438,5 s | 3,50 |
| 7 | 3/3 | 14,6 s | 126,5 s | 439,7 s | 3,49 |
| 8 | 3/3 | 33,8 s | 126,8 s | 440,3 s | 3,49 |
| 9 | 3/3 | 40,5 s | 126,8 s | 440,4 s | 3,49 |
| 10 | 3/3 | 29,4 s | 126,7 s | 440,1 s | 3,49 |
| 11 | 3/3 | 36,0 s | 126,8 s | 440,3 s | 3,49 |
| 12 | 3/3 | 38,7 s | 126,8 s | 440,5 s | 3,49 |
| 13 | 3/3 | 22,2 s | 126,6 s | 439,9 s | 3,49 |
| 14 | 3/3 | 20,4 s | 126,6 s | 439,9 s | 3,49 |
| 15 | 3/3 | 24,5 s | 126,7 s | 440,0 s | 3,49 |
| 16 | 3/3 | 42,1 s | 126,8 s | 440,5 s | 3,49 |
| 17 | 3/3 | 16,2 s | 126,5 s | 439,6 s | 3,49 |
| 18 | 3/3 | 12,4 s | 126,5 s | 439,5 s | 3,49 |
| 19 | 3/3 | 18,7 s | 126,6 s | 439,8 s | 3,49 |
| 20 | 3/3 | 6,7 s | 126,4 s | 439,2 s | 3,50 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 8.192 + 512 | 26,7 s | 180,8 s | 3,32 | Completa |
| 1 | 2 | 8.960 + 512 | 1,4 s | 96,6 s | 5,36 | Completa |
| 1 | 3 | 9.728 + 512 | 3,1 s | 101,9 s | 5,17 | Completa |
| 2 | 1 | 8.192 + 512 | 69,1 s | 185,8 s | 4,38 | Completa |
| 2 | 2 | 8.960 + 512 | 2,9 s | 92,9 s | 5,67 | Completa |
| 2 | 3 | 9.728 + 512 | 8,8 s | 101,4 s | 5,52 | Completa |
| 3 | 1 | 8.192 + 512 | 11,4 s | 178,5 s | 3,06 | Completa |
| 3 | 2 | 8.960 + 512 | 1,2 s | 98,0 s | 5,28 | Completa |
| 3 | 3 | 9.728 + 512 | 2,0 s | 102,5 s | 5,08 | Completa |
| 4 | 1 | 8.192 + 512 | 21,0 s | 180,1 s | 3,21 | Completa |
| 4 | 2 | 8.960 + 512 | 1,3 s | 97,1 s | 5,33 | Completa |
| 4 | 3 | 9.728 + 512 | 3,4 s | 102,2 s | 5,17 | Completa |
| 5 | 1 | 8.192 + 512 | 80,5 s | 186,9 s | 4,80 | Completa |
| 5 | 2 | 8.960 + 512 | 4,3 s | 92,1 s | 5,82 | Completa |
| 5 | 3 | 9.728 + 512 | 9,9 s | 101,3 s | 5,59 | Completa |
| 6 | 1 | 8.192 + 512 | 6,6 s | 177,7 s | 2,99 | Completa |
| 6 | 2 | 8.960 + 512 | 0,8 s | 98,1 s | 5,25 | Completa |
| 6 | 3 | 9.728 + 512 | 0,8 s | 102,7 s | 5,02 | Completa |
| 7 | 1 | 8.192 + 512 | 36,8 s | 182,2 s | 3,52 | Completa |
| 7 | 2 | 8.960 + 512 | 2,1 s | 95,8 s | 5,45 | Completa |
| 7 | 3 | 9.728 + 512 | 4,8 s | 101,6 s | 5,27 | Completa |
| 8 | 1 | 8.192 + 512 | 86,3 s | 187,4 s | 5,06 | Completa |
| 8 | 2 | 8.960 + 512 | 3,8 s | 91,6 s | 5,82 | Completa |
| 8 | 3 | 9.728 + 512 | 11,3 s | 101,4 s | 5,67 | Completa |
| 9 | 1 | 8.192 + 512 | 104,3 s | 188,8 s | 6,05 | Completa |
| 9 | 2 | 8.960 + 512 | 4,6 s | 90,4 s | 5,96 | Completa |
| 9 | 3 | 9.728 + 512 | 12,8 s | 101,3 s | 5,77 | Completa |
| 10 | 1 | 8.192 + 512 | 74,7 s | 186,4 s | 4,58 | Completa |
| 10 | 2 | 8.960 + 512 | 3,6 s | 92,5 s | 5,75 | Completa |
| 10 | 3 | 9.728 + 512 | 10,0 s | 101,3 s | 5,60 | Completa |
| 11 | 1 | 8.192 + 512 | 92,2 s | 187,9 s | 5,34 | Completa |
| 11 | 2 | 8.960 + 512 | 4,7 s | 91,2 s | 5,91 | Completa |
| 11 | 3 | 9.728 + 512 | 11,2 s | 101,3 s | 5,67 | Completa |
| 12 | 1 | 8.192 + 512 | 98,2 s | 188,3 s | 5,67 | Completa |
| 12 | 2 | 8.960 + 512 | 5,0 s | 90,8 s | 5,96 | Completa |
| 12 | 3 | 9.728 + 512 | 12,8 s | 101,4 s | 5,77 | Completa |
| 13 | 1 | 8.192 + 512 | 58,0 s | 184,7 s | 4,03 | Completa |
| 13 | 2 | 8.960 + 512 | 2,2 s | 93,8 s | 5,57 | Completa |
| 13 | 3 | 9.728 + 512 | 6,6 s | 101,4 s | 5,39 | Completa |
| 14 | 1 | 8.192 + 512 | 52,6 s | 184,1 s | 3,89 | Completa |
| 14 | 2 | 8.960 + 512 | 2,1 s | 94,3 s | 5,54 | Completa |
| 14 | 3 | 9.728 + 512 | 6,7 s | 101,5 s | 5,39 | Completa |
| 15 | 1 | 8.192 + 512 | 63,5 s | 185,3 s | 4,20 | Completa |
| 15 | 2 | 8.960 + 512 | 2,3 s | 93,4 s | 5,61 | Completa |
| 15 | 3 | 9.728 + 512 | 7,6 s | 101,4 s | 5,45 | Completa |
| 16 | 1 | 8.192 + 512 | 109,3 s | 189,2 s | 6,40 | Completa |
| 16 | 2 | 8.960 + 512 | 4,4 s | 90,1 s | 5,97 | Completa |
| 16 | 3 | 9.728 + 512 | 12,7 s | 101,3 s | 5,77 | Completa |
| 17 | 1 | 8.192 + 512 | 42,0 s | 182,8 s | 3,63 | Completa |
| 17 | 2 | 8.960 + 512 | 2,1 s | 95,3 s | 5,48 | Completa |
| 17 | 3 | 9.728 + 512 | 4,6 s | 101,5 s | 5,27 | Completa |
| 18 | 1 | 8.192 + 512 | 31,7 s | 181,5 s | 3,41 | Completa |
| 18 | 2 | 8.960 + 512 | 1,5 s | 96,2 s | 5,40 | Completa |
| 18 | 3 | 9.728 + 512 | 3,9 s | 101,8 s | 5,22 | Completa |
| 19 | 1 | 8.192 + 512 | 47,2 s | 183,5 s | 3,75 | Completa |
| 19 | 2 | 8.960 + 512 | 2,1 s | 94,8 s | 5,51 | Completa |
| 19 | 3 | 9.728 + 512 | 6,8 s | 101,5 s | 5,40 | Completa |
| 20 | 1 | 8.192 + 512 | 16,2 s | 179,3 s | 3,13 | Completa |
| 20 | 2 | 8.960 + 512 | 1,2 s | 97,5 s | 5,31 | Completa |
| 20 | 3 | 9.728 + 512 | 2,7 s | 102,4 s | 5,13 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
