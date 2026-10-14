# 4 conversaciones, hasta 4 a la vez; 262.016 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 85% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 2/4 (errores por tiempo de espera). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** **Sí: 2/4**.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 3; 2 errores de espera.
- **Tiempo para completar la prueba:** 1.200,5 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **262.016 tokens de entrada + 128 de respuesta = 262.144 tokens**.

**2 conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**

Esta prueba llega al máximo sumando historial y respuesta. No es una generación de todo ese máximo como respuesta nueva.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 2 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 3 | — | 128 | — | — | No | No |
| 4 | — | 128 | — | — | No | No |

**Errores recibidos:**

- Conversación 3: timed out
- Conversación 4: timed out

Al menos una conexión agotó su tiempo de espera sin completar la respuesta. Este error no demuestra por sí solo falta de memoria ni imposibilidad de terminar con un plazo mayor.

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 406,18 | 715,68 | 0,41 | 0,18 |
| 2 | 860,22 | 1.170,91 | 0,41 | 0,11 |
| 3 | No medido | 1.200,16 | No medido | No medido |
| 4 | No medido | 1.200,17 | No medido | No medido |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 85% |
| Pico medido del motor / memoria del GB10 | 81,6% |
| Pico usado por todo el sistema / memoria del GB10 | 88,7% |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 633,2 s |
| Tiempo medio de respuesta completa | 943,3 s |
| Suma de los tiempos individuales | 1.886,6 s |
| Tiempo total de la prueba | 1.200,5 s |
| Tokens/s medios por conversación, incluyendo espera | 0,14 |
| Tokens/s totales del grupo | 0,21 |
| Pico de caché ocupada | 90,6% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 1.198,4 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 83,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias y velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,21 | 406,39 | 715,89 |
| 2 | 0,33 | 860,54 | 1.171,23 |
| 3 | 0,25 | No medido | 1.200,41 |
| 4 | 0,34 | No medido | 1.200,51 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
