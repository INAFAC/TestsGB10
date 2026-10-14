# 4 conversaciones, hasta 4 a la vez; 32.768 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 35% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 3; 5 recálculos.
- **Tiempo para completar la prueba:** 140,7 s.

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
| 1 | 16,15 | 132,14 | 4,41 | 3,87 |
| 2 | 32,07 | 134,52 | 4,99 | 3,81 |
| 3 | 79,44 | 140,56 | 8,36 | 3,64 |
| 4 | 48,58 | 136,66 | 5,80 | 3,75 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 35% |
| Pico medido del motor / memoria del GB10 | 31,8% |
| Pico usado por todo el sistema / memoria del GB10 | 40,0% |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 44,1 s |
| Tiempo medio de respuesta completa | 136,0 s |
| Mayor espera hasta primer texto, entre las completadas | 79,4 s |
| Mayor tiempo completo, entre las completadas | 140,6 s |
| Suma de los tiempos individuales | 543,9 s |
| Tiempo total de la prueba | 140,7 s |
| Tokens/s medios por conversación, incluyendo espera | 3,77 |
| Tokens/s totales del grupo | 14,56 |
| Pico de caché ocupada | 99,2% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 5 |
| Tiempo observado con cola | 48,9 s |
| Tiempo observado con caché al 95% o más | 69,7 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 79,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,09 | 16,24 | 132,23 |
| 2 | 0,09 | 32,16 | 134,61 |
| 3 | 0,12 | 79,55 | 140,67 |
| 4 | 0,11 | 48,69 | 136,77 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
