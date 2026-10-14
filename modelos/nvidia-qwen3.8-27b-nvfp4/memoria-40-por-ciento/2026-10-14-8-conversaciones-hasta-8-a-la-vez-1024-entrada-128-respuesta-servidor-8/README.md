# 8 conversaciones, hasta 8 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 8 solicitudes activas** (`--max-num-seqs 8`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 8 respuestas solapadas; cola máxima 5.
- **Tiempo para completar la prueba:** 15,4 s.

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
| 1 | 3,06 | 15,17 | 10,49 | 8,44 |
| 2 | 1,34 | 14,91 | 9,36 | 8,59 |
| 3 | 1,94 | 15,00 | 9,73 | 8,54 |
| 4 | 2,56 | 15,08 | 10,14 | 8,49 |
| 5 | 3,44 | 15,25 | 10,75 | 8,39 |
| 6 | 1,93 | 14,99 | 9,73 | 8,54 |
| 7 | 3,47 | 15,33 | 10,71 | 8,35 |
| 8 | 3,06 | 15,17 | 10,49 | 8,44 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,8% |
| Pico usado por todo el sistema / memoria del GB10 | 45,1% |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 8 |
| Máximo activo en el motor | 8 |
| Máximo de respuestas solapadas | 8 |
| Espera media hasta primer texto | 2,6 s |
| Tiempo medio de respuesta completa | 15,1 s |
| Suma de los tiempos individuales | 120,9 s |
| Tiempo total de la prueba | 15,4 s |
| Tokens/s medios por conversación, incluyendo espera | 8,47 |
| Tokens/s totales del grupo | 66,28 |
| Pico de caché ocupada | 8,8% |
| Máximo de solicitudes en cola | 5 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 3,0 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 59,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,07 | 3,13 | 15,24 |
| 2 | 0,07 | 1,41 | 14,97 |
| 3 | 0,07 | 2,01 | 15,06 |
| 4 | 0,07 | 2,63 | 15,15 |
| 5 | 0,07 | 3,51 | 15,32 |
| 6 | 0,07 | 2,01 | 15,07 |
| 7 | 0,07 | 3,55 | 15,40 |
| 8 | 0,07 | 3,13 | 15,24 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
