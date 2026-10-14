# 8 conversaciones, hasta 8 a la vez; 32.768 de entrada + 256 de respuesta (control al final de la campaña)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 2/8 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 activas en el motor; cola máxima 7.
- **Tiempo para completar la prueba:** 110,1 s.

Se enviaron **8 conversaciones**, hasta **8 a la vez**. Cada una pidió **32.768 tokens de entrada + 256 de respuesta = 33.024 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 2 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 6 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 1 | — | 256 | — | — | En curso | No acreditado |
| 3 | — | 256 | — | — | En curso | No acreditado |
| 4 | — | 256 | — | — | En curso | No acreditado |
| 5 | — | 256 | — | — | En curso | No acreditado |
| 7 | — | 256 | — | — | En curso | No acreditado |
| 8 | — | 256 | — | — | En curso | No acreditado |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 2 | 16,14 | 88,16 | 3,54 | 2,90 |
| 6 | 31,91 | 105,03 | 3,49 | 2,44 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,8% |
| Pico usado por todo el sistema / memoria del GB10 | 45,0% |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 24,0 s |
| Tiempo medio de respuesta completa | 96,6 s |
| Mayor espera hasta primer texto, entre las completadas | 31,9 s |
| Mayor tiempo completo, entre las completadas | 105,0 s |
| Suma de los tiempos individuales | 193,2 s |
| Tiempo total de la prueba | 110,1 s |
| Tokens/s medios por conversación, incluyendo espera | 2,67 |
| Tokens/s totales del grupo | 4,65 |
| Pico de caché ocupada | 84,1% |
| Máximo de solicitudes en cola | 7 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 108,6 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 76,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias, los máximos de tiempo y las velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 2 | 0,06 | 16,20 | 88,22 |
| 6 | 0,10 | 32,01 | 105,13 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
