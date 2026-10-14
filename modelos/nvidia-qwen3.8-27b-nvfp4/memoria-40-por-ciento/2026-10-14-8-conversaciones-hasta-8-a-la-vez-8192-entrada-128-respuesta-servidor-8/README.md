# 8 conversaciones, hasta 8 a la vez; 8.192 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 8 solicitudes activas** (`--max-num-seqs 8`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 8 respuestas solapadas; cola máxima 7.
- **Tiempo para completar la prueba:** 52,5 s.

Se enviaron **8 conversaciones**, hasta **8 a la vez**. Cada una pidió **8.192 tokens de entrada + 128 de respuesta = 8.320 tokens**.

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
| 1 | 6,02 | 49,10 | 2,95 | 2,61 |
| 2 | 10,75 | 49,62 | 3,27 | 2,58 |
| 3 | 20,29 | 50,62 | 4,19 | 2,53 |
| 4 | 25,14 | 51,10 | 4,89 | 2,50 |
| 5 | 30,05 | 51,56 | 5,90 | 2,48 |
| 6 | 15,48 | 50,13 | 3,67 | 2,55 |
| 7 | 35,03 | 52,00 | 7,49 | 2,46 |
| 8 | 38,99 | 52,41 | 9,46 | 2,44 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,9% |
| Pico usado por todo el sistema / memoria del GB10 | 45,1% |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 8 |
| Máximo activo en el motor | 8 |
| Máximo de respuestas solapadas | 8 |
| Espera media hasta primer texto | 22,7 s |
| Tiempo medio de respuesta completa | 50,8 s |
| Suma de los tiempos individuales | 406,5 s |
| Tiempo total de la prueba | 52,5 s |
| Tokens/s medios por conversación, incluyendo espera | 2,52 |
| Tokens/s totales del grupo | 19,51 |
| Pico de caché ocupada | 43,2% |
| Máximo de solicitudes en cola | 7 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 32,7 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 71,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,05 | 6,06 | 49,14 |
| 2 | 0,05 | 10,80 | 49,67 |
| 3 | 0,05 | 20,34 | 50,67 |
| 4 | 0,05 | 25,19 | 51,15 |
| 5 | 0,05 | 30,10 | 51,62 |
| 6 | 0,06 | 15,54 | 50,18 |
| 7 | 0,06 | 35,09 | 52,06 |
| 8 | 0,06 | 39,05 | 52,47 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
