# 4 conversaciones, hasta 4 a la vez; 32.768 de entrada + 512 de respuesta (primera medición)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 activas en el motor; cola máxima 3.
- **Tiempo para completar la prueba:** 125,5 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **32.768 tokens de entrada + 512 de respuesta = 33.280 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 32.768 | 512 | 512 | 33.280 | Sí | No |
| 2 | 32.768 | 512 | 512 | 33.280 | Sí | No |
| 3 | 32.768 | 512 | 512 | 33.280 | Sí | No |
| 4 | 32.768 | 512 | 512 | 33.280 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 16,29 | 119,29 | 4,96 | 4,29 |
| 2 | 65,64 | 125,48 | 8,54 | 4,08 |
| 3 | 32,24 | 121,55 | 5,72 | 4,21 |
| 4 | 48,87 | 123,64 | 6,83 | 4,14 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | No medido |
| Pico usado por todo el sistema / memoria del GB10 | No medido |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 40,8 s |
| Tiempo medio de respuesta completa | 122,5 s |
| Suma de los tiempos individuales | 490,0 s |
| Tiempo total de la prueba | 125,5 s |
| Tokens/s medios por conversación, incluyendo espera | 4,18 |
| Tokens/s totales del grupo | 16,32 |
| Pico de caché ocupada | 84,3% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | No medido s |
| Tiempo observado con caché al 95% o más | No medido s |
| Tokens recuperados de caché de prefijos | — |
| Temperatura GPU máxima | No medido °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).

</details>
