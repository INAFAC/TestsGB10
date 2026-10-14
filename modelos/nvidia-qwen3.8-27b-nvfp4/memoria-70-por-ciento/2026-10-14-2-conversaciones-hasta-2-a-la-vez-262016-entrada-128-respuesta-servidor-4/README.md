# 2 conversaciones, hasta 2 a la vez; 262.016 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 70% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 2/2**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** **Sí: 2/2**.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 1; 1 recálculo.
- **Tiempo para completar la prueba:** 722,3 s.

Se enviaron **2 conversaciones**, hasta **2 a la vez**. Cada una pidió **262.016 tokens de entrada + 128 de respuesta = 262.144 tokens**.

**2 conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**

Esta prueba llega al máximo sumando historial y respuesta. No es una generación de todo ese máximo como respuesta nueva.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 2 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 287,19 | 456,85 | 0,75 | 0,28 |
| 2 | 703,22 | 722,14 | 6,71 | 0,18 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 70% |
| Pico medido del motor / memoria del GB10 | 66,7% |
| Pico usado por todo el sistema / memoria del GB10 | 75,6% |
| Menor memoria disponible en el equipo | 29,73 GiB |
| Conversaciones totales | 2 |
| Máximo de peticiones enviadas a la vez | 2 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 495,2 s |
| Tiempo medio de respuesta completa | 589,5 s |
| Mayor espera hasta primer texto, entre las completadas | 703,2 s |
| Mayor tiempo completo, entre las completadas | 722,1 s |
| Suma de los tiempos individuales | 1.179,0 s |
| Tiempo total de la prueba | 722,3 s |
| Tokens/s medios por conversación, incluyendo espera | 0,23 |
| Tokens/s totales del grupo | 0,35 |
| Pico de caché ocupada | 100,0% |
| Máximo de solicitudes en cola | 1 |
| Recálculos por falta de espacio en caché | 1 |
| Tiempo observado con cola | 284,8 s |
| Tiempo observado con caché al 95% o más | 24,5 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 83,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,14 | 287,34 | 456,99 |
| 2 | 0,17 | 703,39 | 722,31 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
