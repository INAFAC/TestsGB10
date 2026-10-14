# 8 conversaciones, hasta 8 a la vez; 8.192 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 8 solicitudes activas** (`--max-num-seqs 8`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 0/8 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 5 activas en el motor; cola máxima 7.
- **Tiempo para completar la prueba:** 20,1 s.

Se enviaron **8 conversaciones**, hasta **8 a la vez**. Cada una pidió **8.192 tokens de entrada + 128 de respuesta = 8.320 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | — | 128 | — | — | En curso | No acreditado |
| 2 | — | 128 | — | — | En curso | No acreditado |
| 3 | — | 128 | — | — | En curso | No acreditado |
| 4 | — | 128 | — | — | En curso | No acreditado |
| 5 | — | 128 | — | — | En curso | No acreditado |
| 6 | — | 128 | — | — | En curso | No acreditado |
| 7 | — | 128 | — | — | En curso | No acreditado |
| 8 | — | 128 | — | — | En curso | No acreditado |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,9% |
| Pico usado por todo el sistema / memoria del GB10 | 45,1% |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 8 |
| Máximo activo en el motor | 5 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | Pendiente |
| Tiempo medio de respuesta completa | Pendiente |
| Suma de los tiempos individuales | Pendiente |
| Tiempo total de la prueba | 20,1 s |
| Tokens/s medios por conversación, incluyendo espera | Pendiente |
| Tokens/s totales del grupo | Pendiente |
| Pico de caché ocupada | 23,0% |
| Máximo de solicitudes en cola | 7 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 17,4 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 66,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias y velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
