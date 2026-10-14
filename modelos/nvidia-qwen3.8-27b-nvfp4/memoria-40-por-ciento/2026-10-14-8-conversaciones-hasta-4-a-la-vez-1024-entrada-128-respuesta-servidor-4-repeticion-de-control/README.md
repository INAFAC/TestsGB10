# 8 conversaciones, hasta 4 a la vez; 1.024 de entrada + 128 de respuesta (control al final de la campaña)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 1.
- **Tiempo para completar la prueba:** 26,2 s.

Se enviaron **8 conversaciones**, hasta **4 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

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
| 1 | 2,06 | 12,99 | 11,62 | 9,86 |
| 2 | 1,69 | 12,90 | 11,33 | 9,92 |
| 3 | 2,08 | 13,21 | 11,42 | 9,69 |
| 4 | 2,06 | 12,98 | 11,62 | 9,86 |
| 5 | 1,84 | 13,08 | 11,30 | 9,79 |
| 6 | 2,09 | 13,08 | 11,55 | 9,79 |
| 7 | 2,08 | 13,08 | 11,55 | 9,79 |
| 8 | 1,93 | 12,94 | 11,54 | 9,90 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,8% |
| Pico usado por todo el sistema / memoria del GB10 | 45,2% |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 2,0 s |
| Tiempo medio de respuesta completa | 13,0 s |
| Mayor espera hasta primer texto, entre las completadas | 2,1 s |
| Mayor tiempo completo, entre las completadas | 13,2 s |
| Suma de los tiempos individuales | 104,3 s |
| Tiempo total de la prueba | 26,2 s |
| Tokens/s medios por conversación, incluyendo espera | 9,82 |
| Tokens/s totales del grupo | 39,03 |
| Pico de caché ocupada | 5,7% |
| Máximo de solicitudes en cola | 1 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 1,0 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 55,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,08 | 2,15 | 13,07 |
| 2 | 0,08 | 1,78 | 12,99 |
| 3 | 0,09 | 2,17 | 13,29 |
| 4 | 0,09 | 2,14 | 13,07 |
| 5 | 12,99 | 14,82 | 26,06 |
| 6 | 13,07 | 15,16 | 26,15 |
| 7 | 13,07 | 15,16 | 26,15 |
| 8 | 13,29 | 15,22 | 26,23 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
