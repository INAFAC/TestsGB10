# 16 conversaciones, hasta 16 a la vez; 65.536 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 70% del GB10.

**Límite impuesto al servidor: 16 solicitudes activas** (`--max-num-seqs 16`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 16/16**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 15.
- **Tiempo para completar la prueba:** 960,5 s.

Se enviaron **16 conversaciones**, hasta **16 a la vez**. Cada una pidió **65.536 tokens de entrada + 128 de respuesta = 65.664 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 2 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 3 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 4 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 5 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 6 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 7 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 8 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 9 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 10 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 11 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 12 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 13 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 14 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 15 | 65.536 | 128 | 128 | 65.664 | Sí | No |
| 16 | 65.536 | 128 | 128 | 65.664 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 462,93 | 647,52 | 0,69 | 0,20 |
| 2 | 52,47 | 225,12 | 0,74 | 0,57 |
| 3 | 221,07 | 405,80 | 0,69 | 0,32 |
| 4 | 104,50 | 284,76 | 0,70 | 0,45 |
| 5 | 161,27 | 345,96 | 0,69 | 0,37 |
| 6 | 341,94 | 526,60 | 0,69 | 0,24 |
| 7 | 403,02 | 587,73 | 0,69 | 0,22 |
| 8 | 282,04 | 466,92 | 0,69 | 0,27 |
| 9 | 523,89 | 708,64 | 0,69 | 0,18 |
| 10 | 704,62 | 889,19 | 0,69 | 0,14 |
| 11 | 583,63 | 768,31 | 0,69 | 0,17 |
| 12 | 644,69 | 829,47 | 0,69 | 0,15 |
| 13 | 765,60 | 945,33 | 0,71 | 0,14 |
| 14 | 825,40 | 951,00 | 1,01 | 0,13 |
| 15 | 886,42 | 956,01 | 1,82 | 0,13 |
| 16 | 944,82 | 960,07 | 8,33 | 0,13 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 70% |
| Pico medido del motor / memoria del GB10 | 67,0% |
| Pico usado por todo el sistema / memoria del GB10 | 75,7% |
| Conversaciones totales | 16 |
| Máximo de peticiones enviadas a la vez | 16 |
| Límite de solicitudes del servidor | 16 |
| Máximo activo en el motor | 5 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 494,3 s |
| Tiempo medio de respuesta completa | 656,2 s |
| Mayor espera hasta primer texto, entre las completadas | 944,8 s |
| Mayor tiempo completo, entre las completadas | 960,1 s |
| Suma de los tiempos individuales | 10.498,4 s |
| Tiempo total de la prueba | 960,5 s |
| Tokens/s medios por conversación, incluyendo espera | 0,24 |
| Tokens/s totales del grupo | 2,13 |
| Pico de caché ocupada | 68,0% |
| Máximo de solicitudes en cola | 15 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 882,5 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 84,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,17 | 463,10 | 647,68 |
| 2 | 0,11 | 52,58 | 225,23 |
| 3 | 0,11 | 221,18 | 405,92 |
| 4 | 0,15 | 104,65 | 284,91 |
| 5 | 0,17 | 161,44 | 346,12 |
| 6 | 0,19 | 342,13 | 526,79 |
| 7 | 0,23 | 403,25 | 587,96 |
| 8 | 0,22 | 282,26 | 467,13 |
| 9 | 0,25 | 524,14 | 708,89 |
| 10 | 0,29 | 704,91 | 889,48 |
| 11 | 0,31 | 583,94 | 768,61 |
| 12 | 0,34 | 645,03 | 829,81 |
| 13 | 0,36 | 765,95 | 945,68 |
| 14 | 0,39 | 825,80 | 951,39 |
| 15 | 0,42 | 886,84 | 956,43 |
| 16 | 0,44 | 945,26 | 960,52 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
