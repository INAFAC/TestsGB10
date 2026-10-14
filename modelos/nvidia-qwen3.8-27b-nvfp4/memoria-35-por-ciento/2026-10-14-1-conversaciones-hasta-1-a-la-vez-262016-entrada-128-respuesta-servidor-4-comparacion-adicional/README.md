# 1 conversación, hasta 1 a la vez; 262.016 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 35% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 1/1**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** **Sí: 1/1**.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 1; 10 recálculos.
- **Tiempo para completar la prueba:** 586,5 s.

Se envió **1 conversación**, hasta **1 a la vez**. Cada una pidió **262.016 tokens de entrada + 128 de respuesta = 262.144 tokens**.

**1 conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**

Esta prueba llega al máximo sumando historial y respuesta. No es una generación de todo ese máximo como respuesta nueva.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 566,57 | 586,35 | 6,42 | 0,22 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 35% |
| Pico medido del motor / memoria del GB10 | 31,8% |
| Pico usado por todo el sistema / memoria del GB10 | 40,0% |
| Conversaciones totales | 1 |
| Máximo de peticiones enviadas a la vez | 1 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 566,6 s |
| Tiempo medio de respuesta completa | 586,4 s |
| Mayor espera hasta primer texto, entre las completadas | 566,6 s |
| Mayor tiempo completo, entre las completadas | 586,4 s |
| Suma de los tiempos individuales | 586,4 s |
| Tiempo total de la prueba | 586,5 s |
| Tokens/s medios por conversación, incluyendo espera | 0,22 |
| Tokens/s totales del grupo | 0,22 |
| Pico de caché ocupada | 99,7% |
| Máximo de solicitudes en cola | 1 |
| Recálculos por falta de espacio en caché | 10 |
| Tiempo observado con cola | 8,1 s |
| Tiempo observado con caché al 95% o más | 69,3 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 82,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,11 | 566,68 | 586,46 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
