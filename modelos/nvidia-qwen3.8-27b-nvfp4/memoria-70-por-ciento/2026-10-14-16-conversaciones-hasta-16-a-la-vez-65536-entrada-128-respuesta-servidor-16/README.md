# 16 conversaciones, hasta 16 a la vez; 65.536 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 70% del GB10.

**Límite impuesto al servidor: 16 solicitudes activas** (`--max-num-seqs 16`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 0/16 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 activa en el motor; cola máxima 15.
- **Tiempo para completar la prueba:** 15,4 s.

Se enviaron **16 conversaciones**, hasta **16 a la vez**. Cada una pidió **65.536 tokens de entrada + 128 de respuesta = 65.664 tokens**.

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
| 9 | — | 128 | — | — | En curso | No acreditado |
| 10 | — | 128 | — | — | En curso | No acreditado |
| 11 | — | 128 | — | — | En curso | No acreditado |
| 12 | — | 128 | — | — | En curso | No acreditado |
| 13 | — | 128 | — | — | En curso | No acreditado |
| 14 | — | 128 | — | — | En curso | No acreditado |
| 15 | — | 128 | — | — | En curso | No acreditado |
| 16 | — | 128 | — | — | En curso | No acreditado |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 70% |
| Pico medido del motor / memoria del GB10 | 66,9% |
| Pico usado por todo el sistema / memoria del GB10 | 75,6% |
| Conversaciones totales | 16 |
| Máximo de peticiones enviadas a la vez | 16 |
| Límite de solicitudes del servidor | 16 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | Pendiente |
| Tiempo medio de respuesta completa | Pendiente |
| Suma de los tiempos individuales | Pendiente |
| Tiempo total de la prueba | 15,4 s |
| Tokens/s medios por conversación, incluyendo espera | Pendiente |
| Tokens/s totales del grupo | Pendiente |
| Pico de caché ocupada | 5,6% |
| Máximo de solicitudes en cola | 15 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 12,2 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 71,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias y velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
