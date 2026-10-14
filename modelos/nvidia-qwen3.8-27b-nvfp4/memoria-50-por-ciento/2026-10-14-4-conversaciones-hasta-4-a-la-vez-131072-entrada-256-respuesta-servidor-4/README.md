# 4 conversaciones, hasta 4 a la vez; 131.072 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 50% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 2/4 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 2 activas en el motor; cola máxima 3; 2 recálculos.
- **Tiempo para completar la prueba:** 469,2 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **131.072 tokens de entrada + 256 de respuesta = 131.328 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 131.072 | 256 | 256 | 131.328 | Sí | No |
| 4 | 131.072 | 256 | 256 | 131.328 | Sí | No |
| 2 | — | 256 | — | — | En curso | No acreditado |
| 3 | — | 256 | — | — | En curso | No acreditado |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 281,01 | 413,93 | 1,92 | 0,62 |
| 4 | 99,09 | 296,88 | 1,29 | 0,86 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 50% |
| Pico medido del motor / memoria del GB10 | 47,0% |
| Pico usado por todo el sistema / memoria del GB10 | 55,5% |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 190,1 s |
| Tiempo medio de respuesta completa | 355,4 s |
| Suma de los tiempos individuales | 710,8 s |
| Tiempo total de la prueba | 469,2 s |
| Tokens/s medios por conversación, incluyendo espera | 0,74 |
| Tokens/s totales del grupo | 1,09 |
| Pico de caché ocupada | 99,6% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 2 |
| Tiempo observado con cola | 414,2 s |
| Tiempo observado con caché al 95% o más | 21,4 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 83,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,16 | 281,17 | 414,08 |
| 4 | 0,16 | 99,25 | 297,04 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
