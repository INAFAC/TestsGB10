# 4 conversaciones, hasta 4 a la vez; 262.016 de entrada + 128 de respuesta (espera ampliada)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 2/4 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** **Por ahora: 2/4**.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 activa en el motor; cola máxima 4; 8 recálculos.
- **Tiempo para completar la prueba:** 1.119,0 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **262.016 tokens de entrada + 128 de respuesta = 262.144 tokens**.

**2 conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**

Esta prueba llega al máximo sumando historial y respuesta. No es una generación de todo ese máximo como respuesta nueva.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 2 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 3 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 1 | — | 128 | — | — | En curso | No acreditado |
| 4 | — | 128 | — | — | En curso | No acreditado |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 2 | 1.099,48 | 1.118,74 | 6,59 | 0,11 |
| 3 | 539,15 | 558,41 | 6,59 | 0,23 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,8% |
| Pico usado por todo el sistema / memoria del GB10 | 45,2% |
| Menor memoria disponible en el equipo | 66,69 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 1 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 819,3 s |
| Tiempo medio de respuesta completa | 838,6 s |
| Mayor espera hasta primer texto, entre las completadas | 1.099,5 s |
| Mayor tiempo completo, entre las completadas | 1.118,7 s |
| Suma de los tiempos individuales | 1.677,1 s |
| Tiempo total de la prueba | 1.119,0 s |
| Tokens/s medios por conversación, incluyendo espera | 0,17 |
| Tokens/s totales del grupo | 0,23 |
| Pico de caché ocupada | 99,6% |
| Máximo de solicitudes en cola | 4 |
| Recálculos por falta de espacio en caché | 8 |
| Tiempo observado con cola | 1.116,2 s |
| Tiempo observado con caché al 95% o más | 84,3 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 83,0 °C |
| Límite de espera sin datos en cada conexión | 2.700 s |
| Tiempo máximo permitido para el grupo | 3.000 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias, los máximos de tiempo y las velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 2 | 0,30 | 1.099,78 | 1.119,04 |
| 3 | 0,27 | 539,42 | 558,68 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
