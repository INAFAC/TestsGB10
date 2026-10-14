# 20 conversaciones, hasta 2 a la vez; 1.024 de entrada + 128 de respuesta (primera medición)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 20/20**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** No se guardó este detalle.
- **Tiempo para completar la prueba:** 116,5 s.

Se enviaron **20 conversaciones**, hasta **2 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

<details>
<summary>Ver tokens y finalización de las 20 conversaciones</summary>

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|

En esta primera medición solo se guardaron cifras del grupo; no se inventan datos individuales.

</details>

<details>
<summary>Ver tiempos y velocidad de las 20 conversaciones</summary>


## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|

</details>


## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | No medido |
| Pico usado por todo el sistema / memoria del GB10 | No medido |
| Conversaciones totales | 20 |
| Máximo de peticiones enviadas a la vez | 2 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | — |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 1,0 s |
| Tiempo medio de respuesta completa | 11,6 s |
| Mayor espera hasta primer texto, entre las completadas | No medido s |
| Mayor tiempo completo, entre las completadas | No medido s |
| Suma de los tiempos individuales | 232,8 s |
| Tiempo total de la prueba | 116,5 s |
| Tokens/s medios por conversación, incluyendo espera | No medido |
| Tokens/s totales del grupo | 21,98 |
| Pico de caché ocupada | No medido |
| Máximo de solicitudes en cola | — |
| Recálculos por falta de espacio en caché | — |
| Tiempo observado con cola | No medido s |
| Tiempo observado con caché al 95% o más | No medido s |
| Tokens recuperados de caché de prefijos | — |
| Temperatura GPU máxima | No medido °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
