# 32 conversaciones, hasta 32 a la vez; 8.192 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 32 solicitudes activas** (`--max-num-seqs 32`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 32/32**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 19 respuestas solapadas; cola máxima 31; 5 recálculos.
- **Tiempo para completar la prueba:** 158,3 s.

Se enviaron **32 conversaciones**, hasta **32 a la vez**. Cada una pidió **8.192 tokens de entrada + 128 de respuesta = 8.320 tokens**.

<details>
<summary>Ver tokens y finalización de las 32 conversaciones</summary>

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 2 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 3 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 4 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 5 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 6 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 7 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 8 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 9 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 10 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 11 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 12 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 13 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 14 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 15 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 16 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 17 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 18 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 19 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 20 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 21 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 22 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 23 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 24 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 25 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 26 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 27 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 28 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 29 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 30 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 31 | 8.192 | 128 | 128 | 8.320 | Sí | No |
| 32 | 8.192 | 128 | 128 | 8.320 | Sí | No |

</details>

<details>
<summary>Ver tiempos y velocidad de las 32 conversaciones</summary>


## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 4,57 | 82,93 | 1,62 | 1,54 |
| 2 | 29,12 | 114,63 | 1,49 | 1,12 |
| 3 | 36,82 | 123,81 | 1,46 | 1,03 |
| 4 | 21,75 | 105,43 | 1,52 | 1,21 |
| 5 | 7,92 | 87,05 | 1,60 | 1,47 |
| 6 | 32,91 | 119,19 | 1,47 | 1,07 |
| 7 | 11,28 | 91,63 | 1,58 | 1,40 |
| 8 | 44,81 | 132,96 | 1,44 | 0,96 |
| 9 | 18,19 | 100,81 | 1,54 | 1,27 |
| 10 | 14,70 | 96,21 | 1,56 | 1,33 |
| 11 | 25,35 | 110,00 | 1,50 | 1,16 |
| 12 | 40,73 | 128,35 | 1,45 | 1,00 |
| 13 | 48,93 | 137,53 | 1,43 | 0,93 |
| 14 | 53,15 | 142,11 | 1,43 | 0,90 |
| 15 | 57,46 | 143,39 | 1,48 | 0,89 |
| 16 | 61,84 | 144,11 | 1,54 | 0,89 |
| 17 | 66,28 | 144,81 | 1,62 | 0,88 |
| 18 | 88,91 | 151,86 | 2,02 | 0,84 |
| 19 | 70,83 | 145,48 | 1,70 | 0,88 |
| 20 | 78,60 | 147,33 | 1,85 | 0,87 |
| 21 | 98,09 | 153,08 | 2,31 | 0,84 |
| 22 | 93,50 | 152,47 | 2,15 | 0,84 |
| 23 | 111,87 | 154,78 | 2,96 | 0,83 |
| 24 | 102,68 | 153,66 | 2,49 | 0,83 |
| 25 | 107,26 | 154,23 | 2,70 | 0,83 |
| 26 | 134,80 | 157,25 | 5,66 | 0,81 |
| 27 | 130,21 | 156,78 | 4,78 | 0,82 |
| 28 | 116,42 | 155,29 | 3,27 | 0,82 |
| 29 | 121,01 | 155,80 | 3,65 | 0,82 |
| 30 | 125,60 | 156,29 | 4,14 | 0,82 |
| 31 | 139,38 | 157,67 | 6,94 | 0,81 |
| 32 | 142,88 | 158,08 | 8,36 | 0,81 |

</details>


## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,7% |
| Pico usado por todo el sistema / memoria del GB10 | 45,0% |
| Menor memoria disponible en el equipo | 66,85 GiB |
| Conversaciones totales | 32 |
| Máximo de peticiones enviadas a la vez | 32 |
| Límite de solicitudes del servidor | 32 |
| Máximo activo en el motor | 19 |
| Máximo de respuestas solapadas | 19 |
| Espera media hasta primer texto | 69,9 s |
| Tiempo medio de respuesta completa | 134,8 s |
| Mayor espera hasta primer texto, entre las completadas | 142,9 s |
| Mayor tiempo completo, entre las completadas | 158,1 s |
| Suma de los tiempos individuales | 4.315,0 s |
| Tiempo total de la prueba | 158,3 s |
| Tokens/s medios por conversación, incluyendo espera | 0,99 |
| Tokens/s totales del grupo | 25,88 |
| Pico de caché ocupada | 99,8% |
| Máximo de solicitudes en cola | 31 |
| Recálculos por falta de espacio en caché | 5 |
| Tiempo observado con cola | 138,3 s |
| Tiempo observado con caché al 95% o más | 60,3 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 74,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,05 | 4,62 | 82,99 |
| 2 | 0,05 | 29,17 | 114,68 |
| 3 | 0,06 | 36,88 | 123,86 |
| 4 | 0,06 | 21,82 | 105,50 |
| 5 | 0,07 | 7,99 | 87,12 |
| 6 | 0,07 | 32,98 | 119,26 |
| 7 | 0,08 | 11,36 | 91,71 |
| 8 | 0,08 | 44,89 | 133,03 |
| 9 | 0,08 | 18,27 | 100,89 |
| 10 | 0,09 | 14,78 | 96,30 |
| 11 | 0,09 | 25,44 | 110,09 |
| 12 | 0,10 | 40,83 | 128,45 |
| 13 | 0,10 | 49,03 | 137,63 |
| 14 | 0,10 | 53,26 | 142,22 |
| 15 | 0,11 | 57,57 | 143,50 |
| 16 | 0,11 | 61,95 | 144,22 |
| 17 | 0,11 | 66,39 | 144,92 |
| 18 | 0,12 | 89,03 | 151,97 |
| 19 | 0,12 | 70,95 | 145,60 |
| 20 | 0,13 | 78,73 | 147,46 |
| 21 | 0,13 | 98,22 | 153,21 |
| 22 | 0,13 | 93,63 | 152,60 |
| 23 | 0,14 | 112,01 | 154,92 |
| 24 | 0,14 | 102,82 | 153,80 |
| 25 | 0,14 | 107,40 | 154,37 |
| 26 | 0,14 | 134,95 | 157,39 |
| 27 | 0,15 | 130,36 | 156,93 |
| 28 | 0,15 | 116,58 | 155,45 |
| 29 | 0,16 | 121,17 | 155,96 |
| 30 | 0,16 | 125,76 | 156,45 |
| 31 | 0,17 | 139,54 | 157,84 |
| 32 | 0,17 | 143,06 | 158,25 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
