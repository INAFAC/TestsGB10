# 20 conversaciones, hasta 8 a la vez; 1.024 de entrada + 128 de respuesta (primera medición)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 20/20**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** No se guardó este detalle.
- **Tiempo para completar la prueba:** 62,6 s.

Se enviaron **20 conversaciones**, hasta **8 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|

En esta primera medición solo se guardaron cifras del grupo; no se inventan datos individuales.

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | No medido |
| Pico usado por todo el sistema / memoria del GB10 | No medido |
| Conversaciones totales | 20 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | — |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 11,2 s |
| Tiempo medio de respuesta completa | 22,6 s |
| Suma de los tiempos individuales | 451,3 s |
| Tiempo total de la prueba | 62,6 s |
| Tokens/s medios por conversación, incluyendo espera | No medido |
| Tokens/s totales del grupo | 40,90 |
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
