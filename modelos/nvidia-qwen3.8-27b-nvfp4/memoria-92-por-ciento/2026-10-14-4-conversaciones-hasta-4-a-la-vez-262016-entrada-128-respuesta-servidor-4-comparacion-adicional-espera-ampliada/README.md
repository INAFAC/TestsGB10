# 4 conversaciones, hasta 4 a la vez; 262.016 de entrada + 128 de respuesta (espera ampliada)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 92% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** **Sí: 4/4**.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 1 respuesta a la vez; cola máxima 3.
- **Tiempo para completar la prueba:** 1.540,7 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **262.016 tokens de entrada + 128 de respuesta = 262.144 tokens**.

**4 conversación(es) alcanzaron exactamente el límite configurado y recibieron toda la respuesta solicitada.**

Esta prueba llega al máximo sumando historial y respuesta. No es una generación de todo ese máximo como respuesta nueva.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 2 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 3 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |
| 4 | 262.016 | 128 | 128 | 262.144 | Sí | Sí |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 733,15 | 996,83 | 0,48 | 0,13 |
| 2 | 1.126,24 | 1.390,77 | 0,48 | 0,09 |
| 3 | 341,82 | 603,63 | 0,49 | 0,21 |
| 4 | 1.519,47 | 1.540,22 | 6,12 | 0,08 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 92% |
| Pico medido del motor / memoria del GB10 | 88,6% |
| Pico usado por todo el sistema / memoria del GB10 | 96,0% |
| Menor memoria disponible en el equipo | 4,89 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 2 |
| Máximo de respuestas solapadas | 1 |
| Espera media hasta primer texto | 930,2 s |
| Tiempo medio de respuesta completa | 1.132,9 s |
| Mayor espera hasta primer texto, entre las completadas | 1.519,5 s |
| Mayor tiempo completo, entre las completadas | 1.540,2 s |
| Suma de los tiempos individuales | 4.531,4 s |
| Tiempo total de la prueba | 1.540,7 s |
| Tokens/s medios por conversación, incluyendo espera | 0,13 |
| Tokens/s totales del grupo | 0,33 |
| Pico de caché ocupada | 81,6% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 1.124,0 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 82,0 °C |
| Límite de espera sin datos en cada conexión | 2.700 s |
| Tiempo máximo permitido para el grupo | 3.000 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,29 | 733,44 | 997,12 |
| 2 | 0,35 | 1.126,59 | 1.391,12 |
| 3 | 0,25 | 342,07 | 603,88 |
| 4 | 0,42 | 1.519,89 | 1.540,64 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
