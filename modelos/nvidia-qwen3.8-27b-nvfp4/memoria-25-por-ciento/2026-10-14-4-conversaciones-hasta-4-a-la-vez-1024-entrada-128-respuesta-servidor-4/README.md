# 4 conversaciones, hasta 4 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 25% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 65.536 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 1.
- **Tiempo para completar la prueba:** 13,1 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 2 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 3 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 4 | 1.024 | 128 | 128 | 1.152 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 2,04 | 12,90 | 11,70 | 9,92 |
| 2 | 2,08 | 13,06 | 11,56 | 9,80 |
| 3 | 2,04 | 12,99 | 11,60 | 9,86 |
| 4 | 2,04 | 12,98 | 11,61 | 9,86 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 25% |
| Pico medido del motor / memoria del GB10 | 21,7% |
| Pico usado por todo el sistema / memoria del GB10 | 29,9% |
| Menor memoria disponible en el equipo | 85,21 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 2,1 s |
| Tiempo medio de respuesta completa | 13,0 s |
| Mayor espera hasta primer texto, entre las completadas | 2,1 s |
| Mayor tiempo completo, entre las completadas | 13,1 s |
| Suma de los tiempos individuales | 51,9 s |
| Tiempo total de la prueba | 13,1 s |
| Tokens/s medios por conversación, incluyendo espera | 9,86 |
| Tokens/s totales del grupo | 38,96 |
| Pico de caché ocupada | 25,9% |
| Máximo de solicitudes en cola | 1 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 1,0 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 54,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,07 | 2,12 | 12,97 |
| 2 | 0,07 | 2,15 | 13,13 |
| 3 | 0,07 | 2,12 | 13,06 |
| 4 | 0,07 | 2,12 | 13,06 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
