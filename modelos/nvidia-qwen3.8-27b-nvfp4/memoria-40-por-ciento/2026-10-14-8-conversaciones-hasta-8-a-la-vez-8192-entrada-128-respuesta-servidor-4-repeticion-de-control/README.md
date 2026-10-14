# 8 conversaciones, hasta 8 a la vez; 8.192 de entrada + 128 de respuesta (control al final de la campaña)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 7.
- **Tiempo para completar la prueba:** 50,2 s.

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
| 1 | 28,85 | 48,81 | 6,36 | 2,62 |
| 2 | 7,93 | 27,40 | 6,52 | 4,67 |
| 3 | 13,79 | 34,21 | 6,22 | 3,74 |
| 4 | 4,56 | 24,39 | 6,40 | 5,25 |
| 5 | 11,30 | 30,79 | 6,52 | 4,16 |
| 6 | 32,24 | 49,25 | 7,47 | 2,60 |
| 7 | 38,15 | 50,09 | 10,64 | 2,56 |
| 8 | 35,65 | 49,68 | 9,06 | 2,58 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,8% |
| Pico usado por todo el sistema / memoria del GB10 | 45,0% |
| Menor memoria disponible en el equipo | 66,90 GiB |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 21,6 s |
| Tiempo medio de respuesta completa | 39,3 s |
| Mayor espera hasta primer texto, entre las completadas | 38,2 s |
| Mayor tiempo completo, entre las completadas | 50,1 s |
| Suma de los tiempos individuales | 314,6 s |
| Tiempo total de la prueba | 50,2 s |
| Tokens/s medios por conversación, incluyendo espera | 3,52 |
| Tokens/s totales del grupo | 20,41 |
| Pico de caché ocupada | 21,1% |
| Máximo de solicitudes en cola | 7 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 34,8 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 65,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,05 | 28,90 | 48,86 |
| 2 | 0,05 | 7,98 | 27,45 |
| 3 | 0,05 | 13,84 | 34,27 |
| 4 | 0,06 | 4,61 | 24,45 |
| 5 | 0,06 | 11,36 | 30,85 |
| 6 | 0,07 | 32,31 | 49,31 |
| 7 | 0,07 | 38,22 | 50,16 |
| 8 | 0,07 | 35,73 | 49,75 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
