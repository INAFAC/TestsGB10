# 4 conversaciones, hasta 4 a la vez; 131.072 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 50% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 2 respuestas solapadas; cola máxima 3; 4 recálculos.
- **Tiempo para completar la prueba:** 629,3 s.

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
| 1 | 281,01 | 413,93 | 1,92 | 0,62 |
| 2 | 404,03 | 603,77 | 1,28 | 0,42 |
| 3 | 598,34 | 629,14 | 8,28 | 0,41 |
| 4 | 99,09 | 296,88 | 1,29 | 0,86 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 50% |
| Pico medido del motor / memoria del GB10 | 47,0% |
| Pico usado por todo el sistema / memoria del GB10 | 55,5% |
| Menor memoria disponible en el equipo | 54,08 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 2 |
| Espera media hasta primer texto | 345,6 s |
| Tiempo medio de respuesta completa | 485,9 s |
| Mayor espera hasta primer texto, entre las completadas | 598,3 s |
| Mayor tiempo completo, entre las completadas | 629,1 s |
| Suma de los tiempos individuales | 1.943,7 s |
| Tiempo total de la prueba | 629,3 s |
| Tokens/s medios por conversación, incluyendo espera | 0,58 |
| Tokens/s totales del grupo | 1,63 |
| Pico de caché ocupada | 99,7% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 4 |
| Tiempo observado con cola | 415,2 s |
| Tiempo observado con caché al 95% o más | 44,9 s |
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
| 2 | 0,18 | 404,21 | 603,95 |
| 3 | 0,20 | 598,54 | 629,34 |
| 4 | 0,16 | 99,25 | 297,04 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
