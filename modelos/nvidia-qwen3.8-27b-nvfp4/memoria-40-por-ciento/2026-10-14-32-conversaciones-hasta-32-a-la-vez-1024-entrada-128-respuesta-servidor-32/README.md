# 32 conversaciones, hasta 32 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 32 solicitudes activas** (`--max-num-seqs 32`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 32/32**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 32 respuestas solapadas; cola máxima 29.
- **Tiempo para completar la prueba:** 34,9 s.

Se enviaron **32 conversaciones**, hasta **32 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 2 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 3 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 4 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 5 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 6 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 7 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 8 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 9 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 10 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 11 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 12 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 13 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 14 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 15 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 16 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 17 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 18 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 19 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 20 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 21 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 22 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 23 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 24 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 25 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 26 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 27 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 28 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 29 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 30 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 31 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 32 | 1.024 | 128 | 128 | 1.152 | Sí | No |

## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 4,09 | 32,90 | 4,41 | 3,89 |
| 2 | 1,69 | 32,50 | 4,12 | 3,94 |
| 3 | 2,49 | 32,64 | 4,21 | 3,92 |
| 4 | 2,49 | 32,63 | 4,21 | 3,92 |
| 5 | 3,30 | 32,77 | 4,31 | 3,91 |
| 6 | 4,09 | 32,90 | 4,41 | 3,89 |
| 7 | 6,53 | 33,27 | 4,75 | 3,85 |
| 8 | 4,90 | 33,02 | 4,52 | 3,88 |
| 9 | 5,71 | 33,15 | 4,63 | 3,86 |
| 10 | 7,33 | 33,38 | 4,87 | 3,83 |
| 11 | 5,71 | 33,15 | 4,63 | 3,86 |
| 12 | 10,64 | 33,83 | 5,47 | 3,78 |
| 13 | 7,33 | 33,39 | 4,87 | 3,83 |
| 14 | 9,80 | 33,72 | 5,31 | 3,80 |
| 15 | 8,16 | 33,50 | 5,01 | 3,82 |
| 16 | 8,97 | 33,61 | 5,15 | 3,81 |
| 17 | 8,97 | 33,61 | 5,15 | 3,81 |
| 18 | 10,63 | 33,83 | 5,47 | 3,78 |
| 19 | 11,49 | 33,93 | 5,66 | 3,77 |
| 20 | 12,36 | 34,03 | 5,86 | 3,76 |
| 21 | 14,11 | 34,23 | 6,31 | 3,74 |
| 22 | 13,23 | 34,13 | 6,08 | 3,75 |
| 23 | 12,36 | 34,03 | 5,86 | 3,76 |
| 24 | 17,40 | 34,59 | 7,39 | 3,70 |
| 25 | 17,84 | 34,67 | 7,55 | 3,69 |
| 26 | 17,97 | 34,75 | 7,57 | 3,68 |
| 27 | 17,40 | 34,59 | 7,39 | 3,70 |
| 28 | 14,11 | 34,23 | 6,31 | 3,74 |
| 29 | 15,00 | 34,32 | 6,57 | 3,73 |
| 30 | 16,80 | 34,50 | 7,18 | 3,71 |
| 31 | 15,90 | 34,41 | 6,86 | 3,72 |
| 32 | 15,90 | 34,41 | 6,86 | 3,72 |

## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,6% |
| Pico usado por todo el sistema / memoria del GB10 | 45,1% |
| Conversaciones totales | 32 |
| Máximo de peticiones enviadas a la vez | 32 |
| Límite de solicitudes del servidor | 32 |
| Máximo activo en el motor | 32 |
| Máximo de respuestas solapadas | 32 |
| Espera media hasta primer texto | 10,1 s |
| Tiempo medio de respuesta completa | 33,7 s |
| Suma de los tiempos individuales | 1.078,6 s |
| Tiempo total de la prueba | 34,9 s |
| Tokens/s medios por conversación, incluyendo espera | 3,80 |
| Tokens/s totales del grupo | 117,51 |
| Pico de caché ocupada | 34,6% |
| Máximo de solicitudes en cola | 29 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 16,4 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 60,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,08 | 4,17 | 32,98 |
| 2 | 0,08 | 1,77 | 32,58 |
| 3 | 0,08 | 2,57 | 32,71 |
| 4 | 0,08 | 2,57 | 32,71 |
| 5 | 0,08 | 3,38 | 32,84 |
| 6 | 0,08 | 4,17 | 32,97 |
| 7 | 0,08 | 6,61 | 33,35 |
| 8 | 0,08 | 4,98 | 33,10 |
| 9 | 0,08 | 5,79 | 33,23 |
| 10 | 0,08 | 7,42 | 33,47 |
| 11 | 0,08 | 5,79 | 33,23 |
| 12 | 0,08 | 10,72 | 33,91 |
| 13 | 0,08 | 7,41 | 33,47 |
| 14 | 0,08 | 9,88 | 33,81 |
| 15 | 0,08 | 8,24 | 33,58 |
| 16 | 0,09 | 9,06 | 33,69 |
| 17 | 0,09 | 9,06 | 33,70 |
| 18 | 0,09 | 10,72 | 33,92 |
| 19 | 0,09 | 11,58 | 34,02 |
| 20 | 0,09 | 12,45 | 34,12 |
| 21 | 0,09 | 14,20 | 34,32 |
| 22 | 0,09 | 13,32 | 34,22 |
| 23 | 0,09 | 12,45 | 34,12 |
| 24 | 0,09 | 17,49 | 34,68 |
| 25 | 0,09 | 17,93 | 34,76 |
| 26 | 0,09 | 18,06 | 34,84 |
| 27 | 0,09 | 17,49 | 34,68 |
| 28 | 0,09 | 14,21 | 34,32 |
| 29 | 0,09 | 15,09 | 34,41 |
| 30 | 0,09 | 16,89 | 34,59 |
| 31 | 0,09 | 16,00 | 34,50 |
| 32 | 0,09 | 15,99 | 34,50 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
