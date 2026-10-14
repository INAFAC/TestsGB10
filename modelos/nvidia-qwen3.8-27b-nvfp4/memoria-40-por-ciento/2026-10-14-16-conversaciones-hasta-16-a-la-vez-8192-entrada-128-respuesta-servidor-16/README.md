# 16 conversaciones, hasta 16 a la vez; 8.192 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 16 solicitudes activas** (`--max-num-seqs 16`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 16/16**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 16 respuestas solapadas; cola máxima 15.
- **Tiempo para completar la prueba:** 76,0 s.

Se enviaron **16 conversaciones**, hasta **16 a la vez**. Cada una pidió **8.192 tokens de entrada + 128 de respuesta = 8.320 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 2 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 3 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 4 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 5 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 6 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 7 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 8 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 9 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 10 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 11 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 12 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 13 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 14 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 15 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 16 | 8.192 | 128 | 128 | 8.320 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 21,37 | 70,87 | 2,57 | 1,81 |
| 2 | 4,16 | 67,65 | 2,00 | 1,89 |
| 3 | 7,53 | 68,33 | 2,09 | 1,87 |
| 4 | 14,33 | 69,63 | 2,30 | 1,84 |
| 5 | 28,73 | 72,03 | 2,93 | 1,78 |
| 6 | 10,90 | 68,98 | 2,19 | 1,86 |
| 7 | 17,80 | 70,25 | 2,42 | 1,82 |
| 8 | 24,98 | 71,44 | 2,73 | 1,79 |
| 9 | 32,52 | 72,55 | 3,17 | 1,76 |
| 10 | 36,41 | 73,08 | 3,46 | 1,75 |
| 11 | 40,35 | 73,58 | 3,82 | 1,74 |
| 12 | 44,40 | 74,07 | 4,28 | 1,73 |
| 13 | 52,76 | 75,01 | 5,71 | 1,71 |
| 14 | 57,07 | 75,45 | 6,91 | 1,70 |
| 15 | 48,53 | 74,54 | 4,88 | 1,72 |
| 16 | 60,33 | 75,86 | 8,18 | 1,69 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,5% |
| Pico usado por todo el sistema / memoria del GB10 | 44,8% |
| Conversaciones totales | 16 |
| Máximo de peticiones enviadas a la vez | 16 |
| Límite de solicitudes del servidor | 16 |
| Máximo activo en el motor | 16 |
| Máximo de respuestas solapadas | 16 |
| Espera media hasta primer texto | 31,4 s |
| Tiempo medio de respuesta completa | 72,1 s |
| Mayor espera hasta primer texto, entre las completadas | 60,3 s |
| Mayor tiempo completo, entre las completadas | 75,9 s |
| Suma de los tiempos individuales | 1.153,3 s |
| Tiempo total de la prueba | 76,0 s |
| Tokens/s medios por conversación, incluyendo espera | 1,78 |
| Tokens/s totales del grupo | 26,96 |
| Pico de caché ocupada | 87,1% |
| Máximo de solicitudes en cola | 15 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 55,2 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 71,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,05 | 21,42 | 70,92 |
| 2 | 0,05 | 4,22 | 67,71 |
| 3 | 0,06 | 7,58 | 68,39 |
| 4 | 0,06 | 14,39 | 69,69 |
| 5 | 0,06 | 28,79 | 72,09 |
| 6 | 0,06 | 10,97 | 69,05 |
| 7 | 0,07 | 17,87 | 70,32 |
| 8 | 0,07 | 25,05 | 71,51 |
| 9 | 0,08 | 32,60 | 72,64 |
| 10 | 0,09 | 36,50 | 73,16 |
| 11 | 0,09 | 40,44 | 73,67 |
| 12 | 0,09 | 44,49 | 74,17 |
| 13 | 0,10 | 52,86 | 75,11 |
| 14 | 0,10 | 57,17 | 75,55 |
| 15 | 0,10 | 48,63 | 74,65 |
| 16 | 0,11 | 60,44 | 75,96 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
