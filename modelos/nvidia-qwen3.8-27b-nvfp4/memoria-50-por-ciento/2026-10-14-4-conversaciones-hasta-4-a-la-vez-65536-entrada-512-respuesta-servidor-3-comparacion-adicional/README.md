# 4 conversaciones, hasta 4 a la vez; 65.536 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 50% del GB10.

**Límite impuesto al servidor: 3 solicitudes activas** (`--max-num-seqs 3`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 4/4**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 3 respuestas solapadas; cola máxima 3.
- **Tiempo para completar la prueba:** 327,1 s.

Se enviaron **4 conversaciones**, hasta **4 a la vez**. Cada una pidió **65.536 tokens de entrada + 512 de respuesta = 66.048 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 2 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 3 | 65.536 | 512 | 512 | 66.048 | Sí | No |
| 4 | 65.536 | 512 | 512 | 66.048 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 158,75 | 279,60 | 4,23 | 1,83 |
| 2 | 104,23 | 273,02 | 3,03 | 1,88 |
| 3 | 274,95 | 326,99 | 9,82 | 1,57 |
| 4 | 52,25 | 218,77 | 3,07 | 2,34 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 50% |
| Pico medido del motor / memoria del GB10 | 47,0% |
| Pico usado por todo el sistema / memoria del GB10 | 55,4% |
| Menor memoria disponible en el equipo | 54,26 GiB |
| Conversaciones totales | 4 |
| Máximo de peticiones enviadas a la vez | 4 |
| Límite de solicitudes del servidor | 3 |
| Máximo activo en el motor | 3 |
| Máximo de respuestas solapadas | 3 |
| Espera media hasta primer texto | 147,5 s |
| Tiempo medio de respuesta completa | 274,6 s |
| Mayor espera hasta primer texto, entre las completadas | 274,9 s |
| Mayor tiempo completo, entre las completadas | 327,0 s |
| Suma de los tiempos individuales | 1.098,4 s |
| Tiempo total de la prueba | 327,1 s |
| Tokens/s medios por conversación, incluyendo espera | 1,90 |
| Tokens/s totales del grupo | 6,26 |
| Pico de caché ocupada | 84,1% |
| Máximo de solicitudes en cola | 3 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 218,0 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 80,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,14 | 158,90 | 279,74 |
| 2 | 0,13 | 104,36 | 273,15 |
| 3 | 0,15 | 275,09 | 327,14 |
| 4 | 0,12 | 52,37 | 218,90 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
