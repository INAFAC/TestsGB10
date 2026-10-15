# 10 usuarios · 70% · historial inicial de 32.768 tokens

[Volver a la comparación](../README.md)

**Continuaciones: no cumple la referencia.** Respuestas completas: **30/30**. Tiempo de la prueba: **599,0 s**.

Límite impuesto al servidor: **32 activas**. Cada usuario mantiene una sola petición pendiente y espera **30 s** después de su respuesta antes de añadir 256 tokens de mensaje. Se conservan los tokens reales de la respuesta anterior.

Las entradas son sintéticas y las respuestas se fuerzan a 512 tokens para comparar la carga. Se mide el primer texto recibido por la API de completions; no se evalúan la calidad de la respuesta ni la interfaz de chat. El control de chat se identificará por separado.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Respuesta completa del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 10/10 | 120,2 s | 265,1 s | 265,1 s | 350,2 s | 1,70 tokens/s | No cumple |
| 2 | 10/10 | 1,3 s | 2,0 s | 2,0 s | 98,5 s | 5,25 tokens/s | No cumple |
| 3 | 10/10 | 1,3 s | 3,2 s | 3,2 s | 100,0 s | 5,17 tokens/s | No cumple |

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 47,1 s |
| Tiempo medio de respuesta completa | 177,6 s |
| Presupuesto configurado | 70% |
| Pico del motor / GB10 | 66,7% |
| Pico del sistema / GB10 | 75,6% |
| Menor memoria disponible | 29,64 GiB |
| Pico de caché | 82,9% |
| Máximo activo / respuestas solapadas | 10 / 10 |
| Máximo en cola | 9 |
| Recálculos | 0 |
| Tokens recuperados de caché | 650.720 |
| Tokens/s de todo el grupo, incluyendo pausas | 25,64 |
| Suma de tiempos individuales | 5.327,1 s |
| Tiempo total de la prueba, incluyendo pausas | 599,0 s |
| Espera máxima sin datos en una conexión | 3.600 s |
| Plazo máximo configurado para todo el grupo | 7.200 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 3/3 | 59,5 s | 179,4 s | 598,2 s | 2,57 |
| 2 | 3/3 | 16,2 s | 174,5 s | 583,6 s | 2,63 |
| 3 | 3/3 | 8,5 s | 170,7 s | 572,0 s | 2,69 |
| 4 | 3/3 | 90,1 s | 179,5 s | 598,6 s | 2,57 |
| 5 | 3/3 | 80,0 s | 179,5 s | 598,5 s | 2,57 |
| 6 | 3/3 | 40,9 s | 178,7 s | 596,2 s | 2,58 |
| 7 | 3/3 | 24,1 s | 176,7 s | 590,1 s | 2,60 |
| 8 | 3/3 | 69,6 s | 179,5 s | 598,4 s | 2,57 |
| 9 | 3/3 | 50,0 s | 179,2 s | 597,6 s | 2,57 |
| 10 | 3/3 | 32,3 s | 178,0 s | 593,9 s | 2,59 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Respuesta completa | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 32.768 + 512 | 175,1 s | 343,9 s | 3,03 | Completa |
| 1 | 2 | 33.536 + 512 | 1,5 s | 96,4 s | 5,38 | Completa |
| 1 | 3 | 34.304 + 512 | 1,9 s | 97,9 s | 5,32 | Completa |
| 2 | 1 | 32.768 + 512 | 46,5 s | 328,8 s | 1,81 | Completa |
| 2 | 2 | 33.536 + 512 | 1,0 s | 97,1 s | 5,32 | Completa |
| 2 | 3 | 34.304 + 512 | 1,1 s | 97,7 s | 5,29 | Completa |
| 3 | 1 | 32.768 + 512 | 23,7 s | 325,1 s | 1,70 | Completa |
| 3 | 2 | 33.536 + 512 | 0,9 s | 94,5 s | 5,46 | Completa |
| 3 | 3 | 34.304 + 512 | 0,9 s | 92,4 s | 5,58 | Completa |
| 4 | 1 | 32.768 + 512 | 265,1 s | 350,2 s | 6,00 | Completa |
| 4 | 2 | 33.536 + 512 | 2,0 s | 92,3 s | 5,66 | Completa |
| 4 | 3 | 34.304 + 512 | 3,1 s | 96,1 s | 5,49 | Completa |
| 5 | 1 | 32.768 + 512 | 235,0 s | 348,4 s | 4,51 | Completa |
| 5 | 2 | 33.536 + 512 | 1,7 s | 93,7 s | 5,56 | Completa |
| 5 | 3 | 34.304 + 512 | 3,2 s | 96,5 s | 5,48 | Completa |
| 6 | 1 | 32.768 + 512 | 120,2 s | 338,5 s | 2,34 | Completa |
| 6 | 2 | 33.536 + 512 | 1,3 s | 98,2 s | 5,27 | Completa |
| 6 | 3 | 34.304 + 512 | 1,3 s | 99,5 s | 5,20 | Completa |
| 7 | 1 | 32.768 + 512 | 70,0 s | 332,2 s | 1,95 | Completa |
| 7 | 2 | 33.536 + 512 | 1,1 s | 98,3 s | 5,26 | Completa |
| 7 | 3 | 34.304 + 512 | 1,2 s | 99,6 s | 5,19 | Completa |
| 8 | 1 | 32.768 + 512 | 204,4 s | 346,2 s | 3,60 | Completa |
| 8 | 2 | 33.536 + 512 | 1,7 s | 95,2 s | 5,47 | Completa |
| 8 | 3 | 34.304 + 512 | 2,8 s | 97,0 s | 5,43 | Completa |
| 9 | 1 | 32.768 + 512 | 147,0 s | 341,3 s | 2,63 | Completa |
| 9 | 2 | 33.536 + 512 | 1,5 s | 97,4 s | 5,33 | Completa |
| 9 | 3 | 34.304 + 512 | 1,4 s | 98,9 s | 5,24 | Completa |
| 10 | 1 | 32.768 + 512 | 94,5 s | 335,5 s | 2,12 | Completa |
| 10 | 2 | 33.536 + 512 | 1,1 s | 98,5 s | 5,25 | Completa |
| 10 | 3 | 34.304 + 512 | 1,2 s | 100,0 s | 5,17 | Completa |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
