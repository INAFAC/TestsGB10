# 4 conversaciones, hasta 4 a la vez; 131.072 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 3.
- **Tiempo para completar la prueba:** 505,2 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **131.072 tokens de entrada + 256 de respuesta = 131.328 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 131.072 | 256 | 256 | 131.328 | Sí | No |
| 2 | 131.072 | 256 | 256 | 131.328 | Sí | No |
| 3 | 131.072 | 256 | 256 | 131.328 | Sí | No |
| 4 | 131.072 | 256 | 256 | 131.328 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 96,99 | 126,32 | 8,69 | 2,03 |
| 2 | 223,20 | 252,58 | 8,68 | 1,01 |
| 3 | 349,39 | 378,76 | 8,68 | 0,68 |
| 4 | 475,61 | 504,96 | 8,69 | 0,51 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,9% |
| Pico usado por todo el sistema / memoria del GB10 | 45,3% |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 286,3 s |
| Tiempo medio de respuesta completa | 315,7 s |
| Mayor espera hasta primer texto, entre las completadas | 475,6 s |
| Mayor tiempo completo, entre las completadas | 505,0 s |
| Suma de los tiempos individuales | 1.262,6 s |
| Tiempo total de la prueba | 505,2 s |
| Tokens/s medios por conversación, incluyendo espera | 1,06 |
| Tokens/s totales del grupo | 2,03 |
| Pico de caché ocupada | 85,8% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 377,2 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 82,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,16 | 97,14 | 126,48 |
| 2 | 0,17 | 223,37 | 252,75 |
| 3 | 0,21 | 349,60 | 378,97 |
| 4 | 0,21 | 475,82 | 505,16 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
