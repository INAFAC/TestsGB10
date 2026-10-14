# 1 conversación, hasta 1 a la vez; 65.280 de entrada + 256 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 25% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 1/1**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** Llegó a 65.536; límite reducido.
- **Límite configurado en esta prueba:** 65.536 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 1; 6 recálculos.
- **Tiempo para completar la prueba:** 96,4 s.

Se envió **1 conversación**, hasta **1 a la vez**. Cada una pidió **65.280 tokens de entrada + 256 de respuesta = 65.536 tokens**.

**1 conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 65.280 | 256 | 256 | 65.536 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 71,39 | 96,35 | 10,22 | 2,66 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 25% |
| Pico medido del motor / memoria del GB10 | 21,7% |
| Pico usado por todo el sistema / memoria del GB10 | 29,8% |
| Conversaciones totales | 1 |
| Máximo de peticiones enviadas a la vez | 1 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 71,4 s |
| Tiempo medio de respuesta completa | 96,3 s |
| Mayor espera hasta primer texto, entre las completadas | 71,4 s |
| Mayor tiempo completo, entre las completadas | 96,3 s |
| Suma de los tiempos individuales | 96,3 s |
| Tiempo total de la prueba | 96,4 s |
| Tokens/s medios por conversación, incluyendo espera | 2,66 |
| Tokens/s totales del grupo | 2,65 |
| Pico de caché ocupada | 97,2% |
| Máximo de solicitudes en cola | 1 |
| Recálculos por falta de espacio en caché | 6 |
| Tiempo observado con cola | 2,0 s |
| Tiempo observado con caché al 95% o más | 4,2 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 82,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,07 | 71,46 | 96,42 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
