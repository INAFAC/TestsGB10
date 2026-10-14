# 64 conversaciones, hasta 64 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 64 solicitudes activas** (`--max-num-seqs 64`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** **Sí: 64/64**. Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 64 respuestas solapadas; cola máxima 61.
- **Tiempo para completar la prueba:** 53,8 s.

Se enviaron **64 conversaciones**, hasta **64 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

<details>
<summary>Ver tokens y finalización de las 64 conversaciones</summary>

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
| 33 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 34 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 35 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 36 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 37 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 38 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 39 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 40 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 41 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 42 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 43 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 44 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 45 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 46 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 47 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 48 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 49 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 50 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 51 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 52 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 53 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 54 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 55 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 56 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 57 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 58 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 59 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 60 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 61 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 62 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 63 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 64 | 1.024 | 128 | 128 | 1.152 | Sí | No |

</details>

<details>
<summary>Ver tiempos y velocidad de las 64 conversaciones</summary>


## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 5,04 | 48,69 | 2,91 | 2,63 |
| 2 | 1,35 | 47,55 | 2,75 | 2,69 |
| 3 | 1,96 | 47,75 | 2,77 | 2,68 |
| 4 | 1,95 | 47,74 | 2,77 | 2,68 |
| 5 | 2,58 | 47,94 | 2,80 | 2,67 |
| 6 | 4,41 | 48,50 | 2,88 | 2,64 |
| 7 | 3,18 | 48,13 | 2,83 | 2,66 |
| 8 | 3,17 | 48,13 | 2,83 | 2,66 |
| 9 | 3,80 | 48,31 | 2,85 | 2,65 |
| 10 | 4,41 | 48,50 | 2,88 | 2,64 |
| 11 | 5,65 | 48,86 | 2,94 | 2,62 |
| 12 | 5,65 | 48,86 | 2,94 | 2,62 |
| 13 | 6,29 | 49,03 | 2,97 | 2,61 |
| 14 | 6,91 | 49,20 | 3,00 | 2,60 |
| 15 | 6,90 | 49,20 | 3,00 | 2,60 |
| 16 | 8,18 | 49,57 | 3,07 | 2,58 |
| 17 | 8,18 | 49,57 | 3,07 | 2,58 |
| 18 | 7,55 | 49,37 | 3,04 | 2,59 |
| 19 | 8,84 | 49,76 | 3,10 | 2,57 |
| 20 | 9,51 | 49,95 | 3,14 | 2,56 |
| 21 | 9,51 | 49,96 | 3,14 | 2,56 |
| 22 | 10,19 | 50,14 | 3,18 | 2,55 |
| 23 | 10,89 | 50,33 | 3,22 | 2,54 |
| 24 | 12,29 | 50,71 | 3,31 | 2,52 |
| 25 | 10,89 | 50,33 | 3,22 | 2,54 |
| 26 | 12,29 | 50,70 | 3,31 | 2,52 |
| 27 | 13,71 | 51,07 | 3,40 | 2,51 |
| 28 | 13,71 | 51,07 | 3,40 | 2,51 |
| 29 | 11,58 | 50,51 | 3,26 | 2,53 |
| 30 | 14,43 | 51,25 | 3,45 | 2,50 |
| 31 | 16,64 | 51,70 | 3,62 | 2,48 |
| 32 | 15,16 | 51,43 | 3,50 | 2,49 |
| 33 | 16,64 | 51,70 | 3,62 | 2,48 |
| 34 | 18,14 | 51,96 | 3,76 | 2,46 |
| 35 | 17,38 | 51,83 | 3,69 | 2,47 |
| 36 | 19,65 | 52,20 | 3,90 | 2,45 |
| 37 | 15,16 | 51,42 | 3,50 | 2,49 |
| 38 | 15,90 | 51,56 | 3,56 | 2,48 |
| 39 | 20,42 | 52,32 | 3,98 | 2,45 |
| 40 | 12,98 | 50,88 | 3,35 | 2,52 |
| 41 | 19,65 | 52,20 | 3,90 | 2,45 |
| 42 | 18,88 | 52,08 | 3,83 | 2,46 |
| 43 | 18,13 | 51,95 | 3,76 | 2,46 |
| 44 | 21,20 | 52,43 | 4,07 | 2,44 |
| 45 | 25,93 | 53,08 | 4,68 | 2,41 |
| 46 | 24,33 | 52,87 | 4,45 | 2,42 |
| 47 | 28,38 | 53,36 | 5,08 | 2,40 |
| 48 | 26,74 | 53,17 | 4,80 | 2,41 |
| 49 | 21,96 | 52,54 | 4,15 | 2,44 |
| 50 | 23,53 | 52,76 | 4,34 | 2,43 |
| 51 | 25,12 | 52,97 | 4,56 | 2,42 |
| 52 | 22,74 | 52,65 | 4,25 | 2,43 |
| 53 | 24,32 | 52,87 | 4,45 | 2,42 |
| 54 | 22,74 | 52,65 | 4,25 | 2,43 |
| 55 | 29,20 | 53,44 | 5,24 | 2,40 |
| 56 | 29,21 | 53,44 | 5,24 | 2,40 |
| 57 | 25,92 | 53,07 | 4,68 | 2,41 |
| 58 | 27,55 | 53,26 | 4,94 | 2,40 |
| 59 | 21,18 | 52,42 | 4,07 | 2,44 |
| 60 | 27,55 | 53,26 | 4,94 | 2,40 |
| 61 | 30,02 | 53,52 | 5,40 | 2,39 |
| 62 | 30,76 | 53,69 | 5,54 | 2,38 |
| 63 | 30,57 | 53,61 | 5,51 | 2,39 |
| 64 | 30,57 | 53,61 | 5,51 | 2,39 |

</details>


## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,6% |
| Pico usado por todo el sistema / memoria del GB10 | 45,4% |
| Menor memoria disponible en el equipo | 66,37 GiB |
| Conversaciones totales | 64 |
| Máximo de peticiones enviadas a la vez | 64 |
| Límite de solicitudes del servidor | 64 |
| Máximo activo en el motor | 64 |
| Máximo de respuestas solapadas | 64 |
| Espera media hasta primer texto | 15,6 s |
| Tiempo medio de respuesta completa | 51,1 s |
| Mayor espera hasta primer texto, entre las completadas | 30,8 s |
| Mayor tiempo completo, entre las completadas | 53,7 s |
| Suma de los tiempos individuales | 3.268,6 s |
| Tiempo total de la prueba | 53,8 s |
| Tokens/s medios por conversación, incluyendo espera | 2,51 |
| Tokens/s totales del grupo | 152,22 |
| Pico de caché ocupada | 68,8% |
| Máximo de solicitudes en cola | 61 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 29,7 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 63,0 °C |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,07 | 5,11 | 48,75 |
| 2 | 0,07 | 1,42 | 47,62 |
| 3 | 0,07 | 2,02 | 47,82 |
| 4 | 0,07 | 2,02 | 47,81 |
| 5 | 0,07 | 2,65 | 48,01 |
| 6 | 0,07 | 4,48 | 48,57 |
| 7 | 0,07 | 3,25 | 48,20 |
| 8 | 0,07 | 3,25 | 48,20 |
| 9 | 0,07 | 3,87 | 48,39 |
| 10 | 0,07 | 4,48 | 48,57 |
| 11 | 0,07 | 5,72 | 48,93 |
| 12 | 0,07 | 5,72 | 48,93 |
| 13 | 0,08 | 6,36 | 49,11 |
| 14 | 0,08 | 6,98 | 49,28 |
| 15 | 0,08 | 6,98 | 49,28 |
| 16 | 0,08 | 8,26 | 49,65 |
| 17 | 0,08 | 8,26 | 49,65 |
| 18 | 0,08 | 7,63 | 49,45 |
| 19 | 0,08 | 8,92 | 49,84 |
| 20 | 0,08 | 9,60 | 50,04 |
| 21 | 0,08 | 9,60 | 50,04 |
| 22 | 0,09 | 10,27 | 50,23 |
| 23 | 0,09 | 10,97 | 50,41 |
| 24 | 0,09 | 12,37 | 50,79 |
| 25 | 0,09 | 10,97 | 50,42 |
| 26 | 0,09 | 12,38 | 50,79 |
| 27 | 0,09 | 13,80 | 51,16 |
| 28 | 0,09 | 13,80 | 51,16 |
| 29 | 0,09 | 11,67 | 50,60 |
| 30 | 0,09 | 14,52 | 51,34 |
| 31 | 0,09 | 16,73 | 51,79 |
| 32 | 0,09 | 15,26 | 51,52 |
| 33 | 0,09 | 16,73 | 51,79 |
| 34 | 0,09 | 18,23 | 52,05 |
| 35 | 0,09 | 17,48 | 51,92 |
| 36 | 0,09 | 19,75 | 52,30 |
| 37 | 0,10 | 15,25 | 51,52 |
| 38 | 0,10 | 15,99 | 51,66 |
| 39 | 0,10 | 20,51 | 52,41 |
| 40 | 0,10 | 13,08 | 50,98 |
| 41 | 0,10 | 19,74 | 52,30 |
| 42 | 0,10 | 18,98 | 52,18 |
| 43 | 0,10 | 18,23 | 52,05 |
| 44 | 0,10 | 21,30 | 52,53 |
| 45 | 0,10 | 26,04 | 53,18 |
| 46 | 0,10 | 24,43 | 52,98 |
| 47 | 0,10 | 28,48 | 53,46 |
| 48 | 0,10 | 26,85 | 53,28 |
| 49 | 0,10 | 22,07 | 52,65 |
| 50 | 0,10 | 23,64 | 52,87 |
| 51 | 0,11 | 25,23 | 53,08 |
| 52 | 0,11 | 22,85 | 52,76 |
| 53 | 0,11 | 24,43 | 52,97 |
| 54 | 0,11 | 22,85 | 52,76 |
| 55 | 0,11 | 29,31 | 53,55 |
| 56 | 0,11 | 29,32 | 53,55 |
| 57 | 0,11 | 26,04 | 53,18 |
| 58 | 0,11 | 27,66 | 53,38 |
| 59 | 0,11 | 21,29 | 52,53 |
| 60 | 0,11 | 27,66 | 53,37 |
| 61 | 0,12 | 30,14 | 53,64 |
| 62 | 0,12 | 30,88 | 53,80 |
| 63 | 0,12 | 30,69 | 53,73 |
| 64 | 0,12 | 30,69 | 53,73 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
