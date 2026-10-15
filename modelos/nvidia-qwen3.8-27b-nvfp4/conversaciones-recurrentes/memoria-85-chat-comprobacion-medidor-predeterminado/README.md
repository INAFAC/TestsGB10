# 2 usuarios · 85% · historial inicial de 256 tokens

[Volver a la comparación](../README.md)

**Comprobación del medidor de chat.** Peticiones sin error: **4/4**. Esta prueba pequeña verifica la recogida de tiempos y la continuidad de los mensajes; no se utiliza para elegir la memoria ni para calificar la fluidez del uso normal.

Límite impuesto al servidor: **32 activas**. Cada persona espera 1 s tras su respuesta y conserva los mensajes reales anteriores. El historial inicial se aproxima al objetivo; la tabla muestra los tokens realmente enviados en cada turno.

Control mediante `/v1/chat/completions`, con conversaciones ficticias en español. Modo de razonamiento: **server_default**. Cada respuesta puede terminar antes del límite de 128 tokens. Se distinguen primer texto del modelo, respuesta visible y finalización natural. No es una evaluación de calidad semántica.

## Resultado por turno

| Turno | Completadas | Espera mediana | Espera del 95% | Peor espera | Fin de petición del 95% | Velocidad del 95% al menos | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 2/2 | 0,3 s | 0,4 s | 0,4 s | 11,1 s | 11,85 tokens/s | No se evalúa |
| 2 | 2/2 | 0,3 s | 0,3 s | 0,3 s | 10,9 s | 11,82 tokens/s | No se evalúa |

### Respuesta visible y finalización natural

| Turno | Respuestas con contenido visible | Terminaron sin alcanzar el límite de salida | Espera p95 al contenido visible |
|---|---:|---:|---:|
| 1 | 0/2 | 0/2 | — s |
| 2 | 0/2 | 1/2 | — s |

En este control, cumplir la referencia requiere además que todas las respuestas tengan contenido visible antes de 5 s (p95) y terminen naturalmente. Alcanzar el límite de salida conserva la medición, pero no se presenta como una respuesta terminada naturalmente.

La referencia requiere todas las respuestas completas, espera p95 de hasta 5 s y velocidad p05 de al menos 10 tokens/s. Es orientativa; las cifras permiten aplicar otro criterio. En filas con fallos, los percentiles describen solo las respuestas completadas y no garantizan el comportamiento del grupo entero.

## Memoria y comportamiento del grupo

| Medida | Resultado |
|---|---|
| Espera media al primer texto | 0,3 s |
| Tiempo medio hasta fin de petición | 9,7 s |
| Presupuesto configurado | 85% |
| Pico del motor / GB10 | 81,6% |
| Pico del sistema / GB10 | 88,6% |
| Menor memoria disponible | 13,89 GiB |
| Pico de caché | 0,5% |
| Máximo activo / respuestas solapadas | 2 / 2 |
| Máximo en cola | 0 |
| Recálculos | 0 |
| Tokens recuperados de caché | 0 |
| Tokens/s de todo el grupo, incluyendo pausas | 19,64 |
| Suma de tiempos individuales | 39,0 s |
| Tiempo total de la prueba, incluyendo pausas | 23,1 s |
| Espera máxima sin datos en una conexión | 300 s |
| Plazo máximo configurado para todo el grupo | 900 s |

Si una prueba agota uno de estos plazos, se conserva como una interrupción por tiempo de espera. Ese resultado no demuestra por sí solo que falte memoria ni que sea imposible terminar con más espera.

## Resumen por persona

| Persona | Turnos sin error | Espera media al primer texto | Tiempo medio de petición | Tiempo de sesión, incluidas pausas | Tokens/s de sesión |
|---|---:|---:|---:|---:|---:|
| 1 | 2/2 | 0,3 s | 11,0 s | 22,9 s | 11,16 |
| 2 | 2/2 | 0,3 s | 8,5 s | 18,1 s | 10,90 |

Las medias incluyen las peticiones sin error. El tiempo de sesión va desde el primer envío de esa persona hasta su última petición registrada, incluyendo las pausas. Sus tokens/s cuentan solo las salidas completadas y ese tiempo completo. En caso de fallo, no representan los turnos que no llegaron a ejecutarse.

## Cada persona y cada mensaje

| Persona | Turno | Entrada + salida | Espera al primer texto | Espera a respuesta visible | Fin de petición | Tokens/s durante la respuesta | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 255 + 128 | 0,4 s | — s | 11,1 s | 11,85 | Alcanzó el límite de salida |
| 1 | 2 | 416 + 128 | 0,3 s | — s | 10,9 s | 12,05 | Alcanzó el límite de salida |
| 2 | 1 | 256 + 128 | 0,3 s | — s | 11,0 s | 11,88 | Alcanzó el límite de salida |
| 2 | 2 | 417 + 69 | 0,3 s | — s | 6,1 s | 11,82 | Terminó naturalmente |

## Datos y reproducción

[Mediciones originales](mediciones.json) · [Configuración](configuracion.json) · [Registro de ejecución](registro-de-ejecucion.log) · [Comando ejecutado](comando-ejecutado.json)

[Historiales finales comprimidos](historiales-reproducibles.json.gz): permiten continuar las mismas conversaciones en la siguiente etapa.
