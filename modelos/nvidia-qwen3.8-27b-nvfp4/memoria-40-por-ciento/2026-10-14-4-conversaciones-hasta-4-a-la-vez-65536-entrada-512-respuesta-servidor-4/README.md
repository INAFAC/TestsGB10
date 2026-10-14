# 4 conversaciones, hasta 4 a la vez; 65.536 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 2 respuestas solapadas; cola máxima 3.
- **Tiempo para completar la prueba:** 268,7 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **65.536 tokens de entrada + 512 de respuesta = 66.048 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 2 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 3 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 4 | 65.536 | 512 | 512 | 66.048 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 75,58 | 168,36 | 5,51 | 3,04 |
| 2 | 37,95 | 131,11 | 5,48 | 3,91 |
| 3 | 171,23 | 264,52 | 5,48 | 1,94 |
| 4 | 208,92 | 268,52 | 8,57 | 1,91 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,9% |
| Pico usado por todo el sistema / memoria del GB10 | 45,3% |
| Menor memoria disponible en el equipo | 66,54 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 2 |
| Espera media hasta primer texto | 123,4 s |
| Tiempo medio de respuesta completa | 208,1 s |
| Mayor espera hasta primer texto, entre las completadas | 208,9 s |
| Mayor tiempo completo, entre las completadas | 268,5 s |
| Suma de los tiempos individuales | 832,5 s |
| Tiempo total de la prueba | 268,7 s |
| Tokens/s medios por conversación, incluyendo espera | 2,70 |
| Tokens/s totales del grupo | 7,62 |
| Pico de caché ocupada | 85,6% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 168,9 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 83,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,06 | 75,64 | 168,43 |
| 2 | 0,08 | 38,03 | 131,19 |
| 3 | 0,13 | 171,36 | 264,65 |
| 4 | 0,13 | 209,05 | 268,65 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
