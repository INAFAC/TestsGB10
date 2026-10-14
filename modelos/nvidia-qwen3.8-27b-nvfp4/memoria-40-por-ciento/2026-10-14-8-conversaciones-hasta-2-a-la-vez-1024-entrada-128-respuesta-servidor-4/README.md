# 8 conversaciones, hasta 2 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 2 respuestas solapadas; cola máxima 0.
- **Tiempo para completar la prueba:** 46,0 s.

Se enviaron **8 conversaciones**, hasta **2 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

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
| 1 | 0,82 | 11,41 | 12,00 | 11,22 |
| 2 | 0,89 | 11,48 | 11,99 | 11,15 |
| 3 | 0,89 | 11,48 | 11,99 | 11,15 |
| 4 | 0,88 | 11,48 | 11,99 | 11,15 |
| 5 | 0,89 | 11,47 | 12,00 | 11,16 |
| 6 | 0,88 | 11,47 | 11,99 | 11,16 |
| 7 | 0,89 | 11,48 | 11,99 | 11,15 |
| 8 | 0,88 | 11,48 | 11,99 | 11,15 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,7% |
| Pico usado por todo el sistema / memoria del GB10 | 45,0% |
| Menor memoria disponible en el equipo | 66,86 GiB |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 2 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 2 |
| Espera media hasta primer texto | 0,9 s |
| Tiempo medio de respuesta completa | 11,5 s |
| Mayor espera hasta primer texto, entre las completadas | 0,9 s |
| Mayor tiempo completo, entre las completadas | 11,5 s |
| Suma de los tiempos individuales | 91,7 s |
| Tiempo total de la prueba | 46,0 s |
| Tokens/s medios por conversación, incluyendo espera | 11,16 |
| Tokens/s totales del grupo | 22,28 |
| Pico de caché ocupada | 3,2% |
| Máximo de solicitudes en cola | 0 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 0,0 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 62,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,04 | 0,87 | 11,45 |
| 2 | 0,04 | 0,94 | 11,53 |
| 3 | 11,45 | 12,34 | 22,93 |
| 4 | 11,53 | 12,41 | 23,00 |
| 5 | 22,93 | 23,81 | 34,40 |
| 6 | 23,00 | 23,88 | 34,48 |
| 7 | 34,40 | 35,29 | 45,88 |
| 8 | 34,48 | 35,36 | 45,96 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
