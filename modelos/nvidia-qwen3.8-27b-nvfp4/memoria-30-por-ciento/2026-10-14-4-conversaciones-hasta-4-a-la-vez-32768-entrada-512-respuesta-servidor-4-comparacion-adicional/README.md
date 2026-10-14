# 4 conversaciones, hasta 4 a la vez; 32.768 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 30% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 131.072 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 2 respuestas solapadas; cola máxima 3.
- **Tiempo para completar la prueba:** 165,7 s.

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
| 1 | 98,34 | 163,74 | 7,81 | 3,13 |
| 2 | 31,66 | 97,06 | 7,81 | 5,27 |
| 3 | 16,44 | 81,48 | 7,86 | 6,28 |
| 4 | 113,84 | 165,59 | 9,88 | 3,09 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 30% |
| Pico medido del motor / memoria del GB10 | 26,8% |
| Pico usado por todo el sistema / memoria del GB10 | 34,8% |
| Menor memoria disponible en el equipo | 79,31 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 2 |
| Espera media hasta primer texto | 65,1 s |
| Tiempo medio de respuesta completa | 127,0 s |
| Mayor espera hasta primer texto, entre las completadas | 113,8 s |
| Mayor tiempo completo, entre las completadas | 165,6 s |
| Suma de los tiempos individuales | 507,9 s |
| Tiempo total de la prueba | 165,7 s |
| Tokens/s medios por conversación, incluyendo espera | 4,44 |
| Tokens/s totales del grupo | 12,36 |
| Pico de caché ocupada | 88,6% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 97,3 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 77,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,06 | 98,40 | 163,80 |
| 2 | 0,08 | 31,74 | 97,15 |
| 3 | 0,09 | 16,53 | 81,57 |
| 4 | 0,10 | 113,94 | 165,69 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
