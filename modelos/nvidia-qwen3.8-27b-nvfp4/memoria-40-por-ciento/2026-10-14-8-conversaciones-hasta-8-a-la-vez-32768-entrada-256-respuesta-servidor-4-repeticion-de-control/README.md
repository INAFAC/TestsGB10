# 8 conversaciones, hasta 8 a la vez; 32.768 de entrada + 256 de respuesta (control al final de la campaña)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 8/8**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 4 respuestas solapadas; cola máxima 7.
- **Tiempo para completar la prueba:** 187,7 s.

Se enviaron **8 conversaciones**, hasta **8 a la vez**. Cada una pidió **32.768 tokens de entrada + 256 de respuesta = 33.024 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 2 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 3 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 4 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 5 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 6 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 7 | 32.768 | 256 | 256 | 33.024 | Sí | No |
| 8 | 32.768 | 256 | 256 | 33.024 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 106,39 | 181,24 | 3,41 | 1,41 |
| 2 | 16,14 | 88,16 | 3,54 | 2,90 |
| 3 | 141,03 | 185,66 | 5,71 | 1,38 |
| 4 | 48,37 | 122,19 | 3,45 | 2,10 |
| 5 | 64,75 | 139,54 | 3,41 | 1,83 |
| 6 | 31,91 | 105,03 | 3,49 | 2,44 |
| 7 | 157,78 | 187,51 | 8,58 | 1,37 |
| 8 | 123,68 | 183,51 | 4,26 | 1,39 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,8% |
| Pico usado por todo el sistema / memoria del GB10 | 45,0% |
| Menor memoria disponible en el equipo | 66,95 GiB |
| Conversaciones totales | 8 |
| Máximo de peticiones enviadas a la vez | 8 |
| Límite de solicitudes del servidor | 4 |
| Máximo activo en el motor | 4 |
| Máximo de respuestas solapadas | 4 |
| Espera media hasta primer texto | 86,3 s |
| Tiempo medio de respuesta completa | 149,1 s |
| Mayor espera hasta primer texto, entre las completadas | 157,8 s |
| Mayor tiempo completo, entre las completadas | 187,5 s |
| Suma de los tiempos individuales | 1.192,8 s |
| Tiempo total de la prueba | 187,7 s |
| Tokens/s medios por conversación, incluyendo espera | 1,85 |
| Tokens/s totales del grupo | 10,91 |
| Pico de caché ocupada | 85,6% |
| Máximo de solicitudes en cola | 7 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 139,3 s |
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
| 1 | 0,06 | 106,45 | 181,30 |
| 2 | 0,06 | 16,20 | 88,22 |
| 3 | 0,11 | 141,14 | 185,77 |
| 4 | 0,10 | 48,46 | 122,29 |
| 5 | 0,09 | 64,84 | 139,63 |
| 6 | 0,10 | 32,01 | 105,13 |
| 7 | 0,13 | 157,91 | 187,64 |
| 8 | 0,12 | 123,80 | 183,64 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
