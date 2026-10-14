# 8 conversaciones, hasta 4 a la vez; 8.192 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 3.
- **Tiempo para completar la prueba:** 50,6 s.

Se enviaron **8 conversaciones**, hasta **4 a la vez**. Cada una pidió **8.192 tokens de entrada + 128 de respuesta = 8.320 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 2 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 3 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 4 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 5 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 6 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 7 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 8 | 8.192 | 128 | 128 | 8.320 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 4,62 | 24,59 | 6,36 | 5,20 |
| 2 | 8,05 | 27,06 | 6,68 | 4,73 |
| 3 | 11,47 | 30,50 | 6,68 | 4,20 |
| 4 | 14,02 | 33,94 | 6,37 | 3,77 |
| 5 | 4,60 | 24,61 | 6,35 | 5,20 |
| 6 | 5,58 | 22,60 | 7,46 | 5,66 |
| 7 | 5,58 | 19,59 | 9,07 | 6,53 |
| 8 | 4,69 | 16,55 | 10,71 | 7,73 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,9% |
| Pico usado por todo el sistema / memoria del GB10 | 45,2% |
| Menor memoria disponible en el equipo | 66,69 GiB |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 7,3 s |
| Tiempo medio de respuesta completa | 24,9 s |
| Mayor espera hasta primer texto, entre las completadas | 14,0 s |
| Mayor tiempo completo, entre las completadas | 33,9 s |
| Suma de los tiempos individuales | 199,4 s |
| Tiempo total de la prueba | 50,6 s |
| Tokens/s medios por conversación, incluyendo espera | 5,38 |
| Tokens/s totales del grupo | 20,25 |
| Pico de caché ocupada | 21,1% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 10,2 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 74,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,05 | 4,67 | 24,64 |
| 2 | 0,05 | 8,09 | 27,10 |
| 3 | 0,05 | 11,52 | 30,55 |
| 4 | 0,05 | 14,07 | 34,00 |
| 5 | 24,64 | 29,24 | 49,26 |
| 6 | 27,11 | 32,69 | 49,71 |
| 7 | 30,55 | 36,14 | 50,14 |
| 8 | 34,00 | 38,69 | 50,55 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
