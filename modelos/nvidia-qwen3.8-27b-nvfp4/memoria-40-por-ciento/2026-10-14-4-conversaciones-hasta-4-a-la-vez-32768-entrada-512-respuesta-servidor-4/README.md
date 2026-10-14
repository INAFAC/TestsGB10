# 4 conversaciones, hasta 4 a la vez; 32.768 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 3.
- **Tiempo para completar la prueba:** 126,4 s.

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
| 1 | 49,13 | 124,43 | 6,79 | 4,11 |
| 2 | 65,79 | 126,29 | 8,45 | 4,05 |
| 3 | 32,44 | 122,32 | 5,69 | 4,19 |
| 4 | 16,37 | 119,99 | 4,93 | 4,27 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,9% |
| Pico usado por todo el sistema / memoria del GB10 | 45,2% |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 40,9 s |
| Tiempo medio de respuesta completa | 123,3 s |
| Mayor espera hasta primer texto, entre las completadas | 65,8 s |
| Mayor tiempo completo, entre las completadas | 126,3 s |
| Suma de los tiempos individuales | 493,0 s |
| Tiempo total de la prueba | 126,4 s |
| Tokens/s medios por conversación, incluyendo espera | 4,16 |
| Tokens/s totales del grupo | 16,20 |
| Pico de caché ocupada | 84,0% |
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
| 1 | 0,08 | 49,20 | 124,51 |
| 2 | 0,08 | 65,87 | 126,37 |
| 3 | 0,07 | 32,51 | 122,39 |
| 4 | 0,07 | 16,44 | 120,06 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
