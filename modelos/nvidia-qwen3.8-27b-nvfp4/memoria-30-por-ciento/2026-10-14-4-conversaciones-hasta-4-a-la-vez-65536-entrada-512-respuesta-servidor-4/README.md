# 4 conversaciones, hasta 4 a la vez; 65.536 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 30% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 131.072 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 3.
- **Tiempo para completar la prueba:** 348,4 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **65.536 tokens de entrada + 512 de respuesta = 66.048 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 2 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 3 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 4 | 65.536 | 512 | 512 | 66.048 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 124,24 | 174,04 | 10,26 | 2,94 |
| 2 | 37,22 | 87,02 | 10,26 | 5,88 |
| 3 | 298,42 | 348,24 | 10,26 | 1,47 |
| 4 | 211,33 | 261,13 | 10,26 | 1,96 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 30% |
| Pico medido del motor / memoria del GB10 | 26,6% |
| Pico usado por todo el sistema / memoria del GB10 | 34,8% |
| Menor memoria disponible en el equipo | 79,25 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 167,8 s |
| Tiempo medio de respuesta completa | 217,6 s |
| Mayor espera hasta primer texto, entre las completadas | 298,4 s |
| Mayor tiempo completo, entre las completadas | 348,2 s |
| Suma de los tiempos individuales | 870,4 s |
| Tiempo total de la prueba | 348,4 s |
| Tokens/s medios por conversación, incluyendo espera | 3,06 |
| Tokens/s totales del grupo | 5,88 |
| Pico de caché ocupada | 91,3% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 261,2 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 80,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,13 | 124,37 | 174,17 |
| 2 | 0,10 | 37,32 | 87,12 |
| 3 | 0,14 | 298,56 | 348,38 |
| 4 | 0,14 | 211,47 | 261,27 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
