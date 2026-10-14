# 16 conversaciones, hasta 16 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 16 solicitudes activas** (`--max-num-seqs 16`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 16/16**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 16 respuestas solapadas; cola máxima 13.
- **Tiempo para completar la prueba:** 20,3 s.

Se enviaron **16 conversaciones**, hasta **16 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

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
| 9 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 10 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 11 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 12 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 13 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 14 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 15 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 16 | 1.024 | 128 | 128 | 1.152 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 1,35 | 19,28 | 7,09 | 6,64 |
| 2 | 2,57 | 19,48 | 7,51 | 6,57 |
| 3 | 1,94 | 19,38 | 7,28 | 6,60 |
| 4 | 1,94 | 19,38 | 7,28 | 6,60 |
| 5 | 6,27 | 20,04 | 9,22 | 6,39 |
| 6 | 4,37 | 19,77 | 8,24 | 6,47 |
| 7 | 3,14 | 19,58 | 7,73 | 6,54 |
| 8 | 3,14 | 19,58 | 7,73 | 6,54 |
| 9 | 5,61 | 19,95 | 8,86 | 6,42 |
| 10 | 3,78 | 19,68 | 7,99 | 6,51 |
| 11 | 4,36 | 19,77 | 8,24 | 6,47 |
| 12 | 5,01 | 19,86 | 8,55 | 6,45 |
| 13 | 6,61 | 20,12 | 9,40 | 6,36 |
| 14 | 5,60 | 19,95 | 8,85 | 6,42 |
| 15 | 6,66 | 20,20 | 9,38 | 6,34 |
| 16 | 6,61 | 20,12 | 9,40 | 6,36 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,4% |
| Pico usado por todo el sistema / memoria del GB10 | 44,9% |
| Conversaciones totales | 16 |
| Máximo de peticiones enviadas a la vez | 16 |
| Límite de solicitudes del servidor | 16 |
| Máximo activo en el motor | 16 |
| Máximo de respuestas solapadas | 16 |
| Espera media hasta primer texto | 4,3 s |
| Tiempo medio de respuesta completa | 19,8 s |
| Mayor espera hasta primer texto, entre las completadas | 6,7 s |
| Mayor tiempo completo, entre las completadas | 20,2 s |
| Suma de los tiempos individuales | 316,1 s |
| Tiempo total de la prueba | 20,3 s |
| Tokens/s medios por conversación, incluyendo espera | 6,48 |
| Tokens/s totales del grupo | 100,92 |
| Pico de caché ocupada | 17,0% |
| Máximo de solicitudes en cola | 13 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 6,1 s |
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
| 1 | 0,07 | 1,42 | 19,35 |
| 2 | 0,07 | 2,64 | 19,56 |
| 3 | 0,07 | 2,01 | 19,46 |
| 4 | 0,07 | 2,01 | 19,45 |
| 5 | 0,07 | 6,34 | 20,12 |
| 6 | 0,07 | 4,44 | 19,85 |
| 7 | 0,07 | 3,22 | 19,66 |
| 8 | 0,08 | 3,22 | 19,66 |
| 9 | 0,08 | 5,69 | 20,03 |
| 10 | 0,08 | 3,86 | 19,75 |
| 11 | 0,08 | 4,44 | 19,85 |
| 12 | 0,08 | 5,09 | 19,94 |
| 13 | 0,08 | 6,69 | 20,20 |
| 14 | 0,08 | 5,69 | 20,03 |
| 15 | 0,08 | 6,74 | 20,28 |
| 16 | 0,08 | 6,69 | 20,20 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
