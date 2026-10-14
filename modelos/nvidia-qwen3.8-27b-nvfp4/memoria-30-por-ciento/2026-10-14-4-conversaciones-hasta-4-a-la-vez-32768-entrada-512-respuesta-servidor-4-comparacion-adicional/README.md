# 4 conversaciones, hasta 4 a la vez; 32.768 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 30% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 1/4 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 131.072 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 2 activas en el motor; cola máxima 3.
- **Tiempo para completar la prueba:** 96,6 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **32.768 tokens de entrada + 512 de respuesta = 33.280 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 3 | 32.768 | 512 | 512 | 33.280 | Sí | No |
| 1 | — | 512 | — | — | En curso | No acreditado |
| 2 | — | 512 | — | — | En curso | No acreditado |
| 4 | — | 512 | — | — | En curso | No acreditado |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 3 | 16,44 | 81,48 | 7,86 | 6,28 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 30% |
| Pico medido del motor / memoria del GB10 | 26,8% |
| Pico usado por todo el sistema / memoria del GB10 | 34,8% |
| Menor memoria disponible en el equipo | 79,31 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 16,4 s |
| Tiempo medio de respuesta completa | 81,5 s |
| Mayor espera hasta primer texto, entre las completadas | 16,4 s |
| Mayor tiempo completo, entre las completadas | 81,5 s |
| Suma de los tiempos individuales | 81,5 s |
| Tiempo total de la prueba | 96,6 s |
| Tokens/s medios por conversación, incluyendo espera | 6,28 |
| Tokens/s totales del grupo | 5,30 |
| Pico de caché ocupada | 88,6% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 95,2 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 73,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias, los máximos de tiempo y las velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 3 | 0,09 | 16,53 | 81,57 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
