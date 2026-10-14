# 4 conversaciones, hasta 4 a la vez; 262.016 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 92% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 3/4 (errores por tiempo de espera). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** **Solo: 3/4**.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 3; 1 error de espera.
- **Tiempo para completar la prueba:** 1.216,2 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **262.016 tokens de entrada + 128 de respuesta = 262.144 tokens**.

**3 conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**

Esta prueba llega al máximo sumando historial y respuesta. No es una generación de todo ese máximo como respuesta nueva.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | — | 128 | — | — | No | No |
| 2 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 3 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 4 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |

**Errores recibidos:**

- Conversación 1: timed out

Al menos una conexión agotó su tiempo de espera sin completar la respuesta. Este error no demuestra por sí solo falta de memoria ni imposibilidad de terminar con un plazo mayor.

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | No medido | 1.200,07 | No medido | No medido |
| 2 | 347,05 | 615,57 | 0,47 | 0,21 |
| 3 | 746,58 | 1.012,90 | 0,48 | 0,13 |
| 4 | 1.143,89 | 1.215,88 | 1,76 | 0,11 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 92% |
| Pico medido del motor / memoria del GB10 | 88,7% |
| Pico usado por todo el sistema / memoria del GB10 | 96,5% |
| Menor memoria disponible en el equipo | 4,29 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 745,8 s |
| Tiempo medio de respuesta completa | 948,1 s |
| Mayor espera hasta primer texto, entre las completadas | 1.143,9 s |
| Mayor tiempo completo, entre las completadas | 1.215,9 s |
| Suma de los tiempos individuales | 2.844,4 s |
| Tiempo total de la prueba | 1.216,2 s |
| Tokens/s medios por conversación, incluyendo espera | 0,15 |
| Tokens/s totales del grupo | 0,32 |
| Pico de caché ocupada | 81,5% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 1.140,9 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 82,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias, los máximos de tiempo y las velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,34 | No medido | 1.200,40 |
| 2 | 0,20 | 347,25 | 615,78 |
| 3 | 0,28 | 746,85 | 1.013,18 |
| 4 | 0,30 | 1.144,19 | 1.216,18 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
