# 1 conversación, hasta 1 a la vez; 130.816 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 30% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 1/1**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** Llegó a 131.072; límite reducido.
- **Límite configurado en esta prueba:** 131.072 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 1; 4 recálculos.
- **Tiempo para completar la prueba:** 207,5 s.

Se envió **1 conversación**, hasta **1 a la vez**. Cada una pidió **130.816 tokens de entrada + 256 de respuesta = 131.072 tokens**.

**1 conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 130.816 | 256 | 256 | 131.072 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 178,06 | 207,39 | 8,69 | 1,23 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 30% |
| Pico medido del motor / memoria del GB10 | 26,6% |
| Pico usado por todo el sistema / memoria del GB10 | 34,8% |
| Conversaciones totales | 1 |
| Máximo de peticiones enviadas a la vez | 1 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 178,1 s |
| Tiempo medio de respuesta completa | 207,4 s |
| Mayor espera hasta primer texto, entre las completadas | 178,1 s |
| Mayor tiempo completo, entre las completadas | 207,4 s |
| Suma de los tiempos individuales | 207,4 s |
| Tiempo total de la prueba | 207,5 s |
| Tokens/s medios por conversación, incluyendo espera | 1,23 |
| Tokens/s totales del grupo | 1,23 |
| Pico de caché ocupada | 99,6% |
| Máximo de solicitudes en cola | 1 |
| Recálculos por falta de espacio en caché | 4 |
| Tiempo observado con cola | 1,0 s |
| Tiempo observado con caché al 95% o más | 15,4 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 83,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,08 | 178,14 | 207,47 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
