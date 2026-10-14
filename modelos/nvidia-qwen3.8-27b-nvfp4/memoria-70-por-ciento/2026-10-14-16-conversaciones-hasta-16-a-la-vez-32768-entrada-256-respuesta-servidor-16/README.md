# 16 conversaciones, hasta 16 a la vez; 32.768 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 70% del GB10.

**Límite impuesto al servidor: 16 solicitudes activas** (`--max-num-seqs 16`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 16/16**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 12 respuestas solapadas; cola máxima 15.
- **Tiempo para completar la prueba:** 508,1 s.

Se enviaron **16 conversaciones**, hasta **16 a la vez**. Cada una pidió **32.768 tokens de entrada + 256 de respuesta = 33.024 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 2 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 3 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 4 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 5 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 6 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 7 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 8 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 9 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 10 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 11 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 12 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 13 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 14 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 15 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 16 | 32.768 | 256 | 256 | 33.024 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 23,58 | 336,24 | 0,82 | 0,76 |
| 2 | 69,79 | 402,88 | 0,77 | 0,64 |
| 3 | 46,28 | 369,47 | 0,79 | 0,69 |
| 4 | 119,93 | 470,50 | 0,73 | 0,54 |
| 5 | 94,32 | 436,69 | 0,74 | 0,59 |
| 6 | 266,32 | 489,96 | 1,14 | 0,52 |
| 7 | 204,07 | 483,29 | 0,91 | 0,53 |
| 8 | 146,81 | 475,78 | 0,78 | 0,54 |
| 9 | 234,55 | 486,72 | 1,01 | 0,53 |
| 10 | 174,83 | 479,62 | 0,84 | 0,53 |
| 11 | 299,08 | 492,84 | 1,32 | 0,52 |
| 12 | 472,01 | 507,77 | 7,13 | 0,50 |
| 13 | 405,47 | 503,76 | 2,59 | 0,51 |
| 14 | 331,18 | 495,62 | 1,55 | 0,52 |
| 15 | 371,67 | 501,38 | 1,97 | 0,51 |
| 16 | 439,26 | 505,85 | 3,83 | 0,51 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 70% |
| Pico medido del motor / memoria del GB10 | 66,9% |
| Pico usado por todo el sistema / memoria del GB10 | 75,8% |
| Conversaciones totales | 16 |
| Máximo de peticiones enviadas a la vez | 16 |
| Límite de solicitudes del servidor | 16 |
| Máximo activo en el motor | 12 |
| Máximo de respuestas solapadas | 12 |
| Espera media hasta primer texto | 231,2 s |
| Tiempo medio de respuesta completa | 464,9 s |
| Mayor espera hasta primer texto, entre las completadas | 472,0 s |
| Mayor tiempo completo, entre las completadas | 507,8 s |
| Suma de los tiempos individuales | 7.438,4 s |
| Tiempo total de la prueba | 508,1 s |
| Tokens/s medios por conversación, incluyendo espera | 0,56 |
| Tokens/s totales del grupo | 8,06 |
| Pico de caché ocupada | 98,3% |
| Máximo de solicitudes en cola | 15 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 436,7 s |
| Tiempo observado con caché al 95% o más | 69,7 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 76,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,12 | 23,71 | 336,36 |
| 2 | 0,13 | 69,93 | 403,02 |
| 3 | 0,15 | 46,44 | 369,63 |
| 4 | 0,17 | 120,10 | 470,67 |
| 5 | 0,16 | 94,48 | 436,85 |
| 6 | 0,18 | 266,50 | 490,14 |
| 7 | 0,24 | 204,31 | 483,53 |
| 8 | 0,21 | 147,02 | 475,99 |
| 9 | 0,22 | 234,77 | 486,94 |
| 10 | 0,23 | 175,06 | 479,85 |
| 11 | 0,28 | 299,36 | 493,13 |
| 12 | 0,31 | 472,33 | 508,09 |
| 13 | 0,29 | 405,75 | 504,04 |
| 14 | 0,30 | 331,49 | 495,93 |
| 15 | 0,30 | 371,97 | 501,68 |
| 16 | 0,33 | 439,59 | 506,18 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
