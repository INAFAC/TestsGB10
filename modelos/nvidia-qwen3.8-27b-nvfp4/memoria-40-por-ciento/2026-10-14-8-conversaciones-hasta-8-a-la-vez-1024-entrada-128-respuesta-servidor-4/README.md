# 8 conversaciones, hasta 8 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 5.
- **Tiempo para completar la prueba:** 26,1 s.

Se enviaron **8 conversaciones**, hasta **8 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

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
| 1 | 2,03 | 13,17 | 11,40 | 9,72 |
| 2 | 1,70 | 12,93 | 11,31 | 9,90 |
| 3 | 2,03 | 13,17 | 11,40 | 9,72 |
| 4 | 15,01 | 26,01 | 11,54 | 4,92 |
| 5 | 15,01 | 26,01 | 11,54 | 4,92 |
| 6 | 2,09 | 13,80 | 10,85 | 9,28 |
| 7 | 14,67 | 25,92 | 11,29 | 4,94 |
| 8 | 15,07 | 26,08 | 11,53 | 4,91 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,8% |
| Pico usado por todo el sistema / memoria del GB10 | 45,1% |
| Menor memoria disponible en el equipo | 66,72 GiB |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 8,5 s |
| Tiempo medio de respuesta completa | 19,6 s |
| Mayor espera hasta primer texto, entre las completadas | 15,1 s |
| Mayor tiempo completo, entre las completadas | 26,1 s |
| Suma de los tiempos individuales | 157,1 s |
| Tiempo total de la prueba | 26,1 s |
| Tokens/s medios por conversación, incluyendo espera | 7,29 |
| Tokens/s totales del grupo | 39,17 |
| Pico de caché ocupada | 5,7% |
| Máximo de solicitudes en cola | 5 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 14,3 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 64,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,05 | 2,07 | 13,22 |
| 2 | 0,05 | 1,75 | 12,98 |
| 3 | 0,05 | 2,07 | 13,21 |
| 4 | 0,05 | 15,05 | 26,06 |
| 5 | 0,05 | 15,05 | 26,06 |
| 6 | 0,05 | 2,14 | 13,84 |
| 7 | 0,05 | 14,72 | 25,97 |
| 8 | 0,05 | 15,12 | 26,14 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
