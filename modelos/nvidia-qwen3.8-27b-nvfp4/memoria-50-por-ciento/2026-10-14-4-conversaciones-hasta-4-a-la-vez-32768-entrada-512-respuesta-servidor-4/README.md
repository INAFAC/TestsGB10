# 4 conversaciones, hasta 4 a la vez; 32.768 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 50% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 3.
- **Tiempo para completar la prueba:** 126,8 s.

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
| 1 | 32,52 | 122,67 | 5,67 | 4,17 |
| 2 | 16,39 | 120,32 | 4,92 | 4,26 |
| 3 | 66,09 | 126,63 | 8,44 | 4,04 |
| 4 | 49,26 | 124,75 | 6,77 | 4,10 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 50% |
| Pico medido del motor / memoria del GB10 | 46,9% |
| Pico usado por todo el sistema / memoria del GB10 | 55,6% |
| Menor memoria disponible en el equipo | 53,95 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 41,1 s |
| Tiempo medio de respuesta completa | 123,6 s |
| Mayor espera hasta primer texto, entre las completadas | 66,1 s |
| Mayor tiempo completo, entre las completadas | 126,6 s |
| Suma de los tiempos individuales | 494,4 s |
| Tiempo total de la prueba | 126,8 s |
| Tokens/s medios por conversación, incluyendo espera | 4,14 |
| Tokens/s totales del grupo | 16,15 |
| Pico de caché ocupada | 55,0% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 46,9 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 78,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,11 | 32,62 | 122,78 |
| 2 | 0,12 | 16,51 | 120,44 |
| 3 | 0,14 | 66,23 | 126,77 |
| 4 | 0,15 | 49,41 | 124,90 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
