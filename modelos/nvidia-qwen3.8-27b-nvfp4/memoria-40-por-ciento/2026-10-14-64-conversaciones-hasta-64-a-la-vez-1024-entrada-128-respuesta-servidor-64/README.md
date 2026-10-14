# 64 conversaciones, hasta 64 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 64 solicitudes activas** (`--max-num-seqs 64`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 0/64 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 10 activas en el motor; cola máxima 61.
- **Tiempo para completar la prueba:** 5,1 s.

Se enviaron **64 conversaciones**, hasta **64 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

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
| 17 | — | 128 | — | — | En curso | No acreditado |
| 18 | — | 128 | — | — | En curso | No acreditado |
| 19 | — | 128 | — | — | En curso | No acreditado |
| 20 | — | 128 | — | — | En curso | No acreditado |
| 21 | — | 128 | — | — | En curso | No acreditado |
| 22 | — | 128 | — | — | En curso | No acreditado |
| 23 | — | 128 | — | — | En curso | No acreditado |
| 24 | — | 128 | — | — | En curso | No acreditado |
| 25 | — | 128 | — | — | En curso | No acreditado |
| 26 | — | 128 | — | — | En curso | No acreditado |
| 27 | — | 128 | — | — | En curso | No acreditado |
| 28 | — | 128 | — | — | En curso | No acreditado |
| 29 | — | 128 | — | — | En curso | No acreditado |
| 30 | — | 128 | — | — | En curso | No acreditado |
| 31 | — | 128 | — | — | En curso | No acreditado |
| 32 | — | 128 | — | — | En curso | No acreditado |
| 33 | — | 128 | — | — | En curso | No acreditado |
| 34 | — | 128 | — | — | En curso | No acreditado |
| 35 | — | 128 | — | — | En curso | No acreditado |
| 36 | — | 128 | — | — | En curso | No acreditado |
| 37 | — | 128 | — | — | En curso | No acreditado |
| 38 | — | 128 | — | — | En curso | No acreditado |
| 39 | — | 128 | — | — | En curso | No acreditado |
| 40 | — | 128 | — | — | En curso | No acreditado |
| 41 | — | 128 | — | — | En curso | No acreditado |
| 42 | — | 128 | — | — | En curso | No acreditado |
| 43 | — | 128 | — | — | En curso | No acreditado |
| 44 | — | 128 | — | — | En curso | No acreditado |
| 45 | — | 128 | — | — | En curso | No acreditado |
| 46 | — | 128 | — | — | En curso | No acreditado |
| 47 | — | 128 | — | — | En curso | No acreditado |
| 48 | — | 128 | — | — | En curso | No acreditado |
| 49 | — | 128 | — | — | En curso | No acreditado |
| 50 | — | 128 | — | — | En curso | No acreditado |
| 51 | — | 128 | — | — | En curso | No acreditado |
| 52 | — | 128 | — | — | En curso | No acreditado |
| 53 | — | 128 | — | — | En curso | No acreditado |
| 54 | — | 128 | — | — | En curso | No acreditado |
| 55 | — | 128 | — | — | En curso | No acreditado |
| 56 | — | 128 | — | — | En curso | No acreditado |
| 57 | — | 128 | — | — | En curso | No acreditado |
| 58 | — | 128 | — | — | En curso | No acreditado |
| 59 | — | 128 | — | — | En curso | No acreditado |
| 60 | — | 128 | — | — | En curso | No acreditado |
| 61 | — | 128 | — | — | En curso | No acreditado |
| 62 | — | 128 | — | — | En curso | No acreditado |
| 63 | — | 128 | — | — | En curso | No acreditado |
| 64 | — | 128 | — | — | En curso | No acreditado |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,6% |
| Pico usado por todo el sistema / memoria del GB10 | 45,4% |
| Conversaciones totales | 64 |
| Máximo de peticiones enviadas a la vez | 64 |
| Límite de solicitudes del servidor | 64 |
| Máximo activo en el motor | 10 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | Pendiente |
| Tiempo medio de respuesta completa | Pendiente |
| Suma de los tiempos individuales | Pendiente |
| Tiempo total de la prueba | 5,1 s |
| Tokens/s medios por conversación, incluyendo espera | Pendiente |
| Tokens/s totales del grupo | Pendiente |
| Pico de caché ocupada | 12,1% |
| Máximo de solicitudes en cola | 61 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 3,0 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 47,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias y velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
