# 8 conversaciones, hasta 8 a la vez; 32.768 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 8 solicitudes activas** (`--max-num-seqs 8`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 5 respuestas solapadas; cola máxima 7; 2 recálculos.
- **Tiempo para completar la prueba:** 261,9 s.

Se enviaron **8 conversaciones**, hasta **8 a la vez**. Cada una pidió **32.768 tokens de entrada + 256 de respuesta = 33.024 tokens**.

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

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 24,54 | 157,52 | 1,92 | 1,63 |
| 2 | 137,09 | 237,96 | 2,53 | 1,08 |
| 3 | 46,23 | 182,32 | 1,87 | 1,40 |
| 4 | 69,57 | 207,15 | 1,85 | 1,24 |
| 5 | 93,89 | 232,36 | 1,84 | 1,10 |
| 6 | 183,86 | 257,74 | 3,45 | 0,99 |
| 7 | 209,08 | 259,86 | 5,02 | 0,99 |
| 8 | 233,43 | 261,75 | 9,00 | 0,98 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,9% |
| Pico usado por todo el sistema / memoria del GB10 | 45,0% |
| Menor memoria disponible en el equipo | 66,85 GiB |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 8 |
| Máximo activo en el motor | 5 |
| Máximo de respuestas solapadas | 5 |
| Espera media hasta primer texto | 124,7 s |
| Tiempo medio de respuesta completa | 224,6 s |
| Mayor espera hasta primer texto, entre las completadas | 233,4 s |
| Mayor tiempo completo, entre las completadas | 261,7 s |
| Suma de los tiempos individuales | 1.796,7 s |
| Tiempo total de la prueba | 261,9 s |
| Tokens/s medios por conversación, incluyendo espera | 1,17 |
| Tokens/s totales del grupo | 7,82 |
| Pico de caché ocupada | 99,0% |
| Máximo de solicitudes en cola | 7 |
| Recálculos por falta de espacio en caché | 2 |
| Tiempo observado con cola | 206,8 s |
| Tiempo observado con caché al 95% o más | 33,8 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 79,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,05 | 24,59 | 157,57 |
| 2 | 0,10 | 137,18 | 238,06 |
| 3 | 0,08 | 46,32 | 182,40 |
| 4 | 0,09 | 69,66 | 207,24 |
| 5 | 0,09 | 93,99 | 232,45 |
| 6 | 0,10 | 183,96 | 257,84 |
| 7 | 0,12 | 209,20 | 259,98 |
| 8 | 0,12 | 233,55 | 261,87 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
