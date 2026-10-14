# 4 conversaciones, hasta 4 a la vez; 131.072 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 70% del GB10.

**Límite impuesto al servidor: 2 solicitudes activas** (`--max-num-seqs 2`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 2 respuestas solapadas; cola máxima 3.
- **Tiempo para completar la prueba:** 477,1 s.

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
| 1 | 97,59 | 228,77 | 1,94 | 1,12 |
| 2 | 202,04 | 332,27 | 1,96 | 0,77 |
| 3 | 335,81 | 467,17 | 1,94 | 0,55 |
| 4 | 440,45 | 476,85 | 7,01 | 0,54 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 70% |
| Pico medido del motor / memoria del GB10 | 66,7% |
| Pico usado por todo el sistema / memoria del GB10 | 75,4% |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 2 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 2 |
| Espera media hasta primer texto | 269,0 s |
| Tiempo medio de respuesta completa | 376,3 s |
| Suma de los tiempos individuales | 1.505,1 s |
| Tiempo total de la prueba | 477,1 s |
| Tokens/s medios por conversación, incluyendo espera | 0,74 |
| Tokens/s totales del grupo | 2,15 |
| Pico de caché ocupada | 66,9% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 332,3 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 82,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,13 | 97,73 | 228,91 |
| 2 | 0,21 | 202,25 | 332,48 |
| 3 | 0,18 | 335,99 | 467,35 |
| 4 | 0,22 | 440,67 | 477,07 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
