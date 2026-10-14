# 8 conversaciones, hasta 1 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 0.
- **Tiempo para completar la prueba:** 85,3 s.

Se enviaron **8 conversaciones**, hasta **1 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 2 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 3 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 4 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 5 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 6 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 7 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 8 | 1.024 | 128 | 128 | 1.152 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 0,51 | 10,65 | 12,52 | 12,02 |
| 2 | 0,49 | 10,63 | 12,52 | 12,04 |
| 3 | 0,49 | 10,63 | 12,52 | 12,04 |
| 4 | 0,49 | 10,65 | 12,51 | 12,02 |
| 5 | 0,49 | 10,66 | 12,49 | 12,01 |
| 6 | 0,49 | 10,66 | 12,49 | 12,00 |
| 7 | 0,49 | 10,66 | 12,48 | 12,01 |
| 8 | 0,49 | 10,66 | 12,49 | 12,00 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,7% |
| Pico usado por todo el sistema / memoria del GB10 | 45,3% |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 1 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 0,5 s |
| Tiempo medio de respuesta completa | 10,7 s |
| Mayor espera hasta primer texto, entre las completadas | 0,5 s |
| Mayor tiempo completo, entre las completadas | 10,7 s |
| Suma de los tiempos individuales | 85,2 s |
| Tiempo total de la prueba | 85,3 s |
| Tokens/s medios por conversación, incluyendo espera | 12,02 |
| Tokens/s totales del grupo | 12,01 |
| Pico de caché ocupada | 1,6% |
| Máximo de solicitudes en cola | 0 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 0,0 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 61,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,09 | 0,59 | 10,73 |
| 2 | 10,73 | 11,22 | 21,37 |
| 3 | 21,37 | 21,86 | 32,00 |
| 4 | 32,00 | 32,49 | 42,65 |
| 5 | 42,65 | 43,13 | 53,30 |
| 6 | 53,30 | 53,79 | 63,96 |
| 7 | 63,97 | 64,45 | 74,63 |
| 8 | 74,63 | 75,12 | 85,29 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
