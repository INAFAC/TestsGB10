# 4 conversaciones, hasta 4 a la vez; 32.768 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 25% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 65.536 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 3.
- **Tiempo para completar la prueba:** 152,8 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **32.768 tokens de entrada + 256 de respuesta = 33.024 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 2 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 3 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 4 | 32.768 | 256 | 256 | 33.024 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 15,46 | 38,15 | 11,24 | 6,71 |
| 2 | 91,84 | 114,55 | 11,23 | 2,23 |
| 3 | 53,59 | 76,32 | 11,22 | 3,35 |
| 4 | 130,02 | 152,74 | 11,22 | 1,68 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 25% |
| Pico medido del motor / memoria del GB10 | 21,7% |
| Pico usado por todo el sistema / memoria del GB10 | 29,8% |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 72,7 s |
| Tiempo medio de respuesta completa | 95,4 s |
| Suma de los tiempos individuales | 381,8 s |
| Tiempo total de la prueba | 152,8 s |
| Tokens/s medios por conversación, incluyendo espera | 3,49 |
| Tokens/s totales del grupo | 6,70 |
| Pico de caché ocupada | 100,0% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 113,9 s |
| Tiempo observado con caché al 95% o más | 35,9 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 76,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,05 | 15,51 | 38,21 |
| 2 | 0,06 | 91,90 | 114,62 |
| 3 | 0,08 | 53,67 | 76,40 |
| 4 | 0,08 | 130,10 | 152,82 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
