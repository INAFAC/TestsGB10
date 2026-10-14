# 128 conversaciones, hasta 128 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Límite impuesto al servidor: 128 solicitudes activas** (`--max-num-seqs 128`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 12/128 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 91 activas en el motor; cola máxima 125; 1 recálculo.
- **Tiempo para completar la prueba:** 73,0 s.

Se enviaron **128 conversaciones**, hasta **128 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

<details>
<summary>Ver tokens y finalización de las 128 conversaciones</summary>

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
| 13 | — | 128 | — | — | En curso | No acreditado |
| 14 | — | 128 | — | — | En curso | No acreditado |
| 15 | — | 128 | — | — | En curso | No acreditado |
| 16 | — | 128 | — | — | En curso | No acreditado |
| 17 | — | 128 | — | — | En curso | No acreditado |
| 18 | — | 128 | — | — | En curso | No acreditado |
| 19 | — | 128 | — | — | En curso | No acreditado |
| 20 | — | 128 | — | — | En curso | No acreditado |
| 21 | — | 128 | — | — | En curso | No acreditado |
| 22 | — | 128 | — | — | En curso | No acreditado |
| 23 | — | 128 | — | — | En curso | No acreditado |
| 24 | — | 128 | — | — | En curso | No acreditado |
| 25 | — | 128 | — | — | En curso | No acreditado |
| 26 | — | 128 | — | — | En curso | No acreditado |
| 27 | — | 128 | — | — | En curso | No acreditado |
| 28 | — | 128 | — | — | En curso | No acreditado |
| 29 | — | 128 | — | — | En curso | No acreditado |
| 30 | — | 128 | — | — | En curso | No acreditado |
| 31 | — | 128 | — | — | En curso | No acreditado |
| 32 | — | 128 | — | — | En curso | No acreditado |
| 33 | — | 128 | — | — | En curso | No acreditado |
| 34 | — | 128 | — | — | En curso | No acreditado |
| 35 | — | 128 | — | — | En curso | No acreditado |
| 36 | — | 128 | — | — | En curso | No acreditado |
| 37 | — | 128 | — | — | En curso | No acreditado |
| 38 | — | 128 | — | — | En curso | No acreditado |
| 39 | — | 128 | — | — | En curso | No acreditado |
| 40 | — | 128 | — | — | En curso | No acreditado |
| 41 | — | 128 | — | — | En curso | No acreditado |
| 42 | — | 128 | — | — | En curso | No acreditado |
| 43 | — | 128 | — | — | En curso | No acreditado |
| 44 | — | 128 | — | — | En curso | No acreditado |
| 45 | — | 128 | — | — | En curso | No acreditado |
| 46 | — | 128 | — | — | En curso | No acreditado |
| 47 | — | 128 | — | — | En curso | No acreditado |
| 48 | — | 128 | — | — | En curso | No acreditado |
| 49 | — | 128 | — | — | En curso | No acreditado |
| 50 | — | 128 | — | — | En curso | No acreditado |
| 51 | — | 128 | — | — | En curso | No acreditado |
| 52 | — | 128 | — | — | En curso | No acreditado |
| 53 | — | 128 | — | — | En curso | No acreditado |
| 54 | — | 128 | — | — | En curso | No acreditado |
| 55 | — | 128 | — | — | En curso | No acreditado |
| 56 | — | 128 | — | — | En curso | No acreditado |
| 57 | — | 128 | — | — | En curso | No acreditado |
| 58 | — | 128 | — | — | En curso | No acreditado |
| 59 | — | 128 | — | — | En curso | No acreditado |
| 60 | — | 128 | — | — | En curso | No acreditado |
| 61 | — | 128 | — | — | En curso | No acreditado |
| 62 | — | 128 | — | — | En curso | No acreditado |
| 63 | — | 128 | — | — | En curso | No acreditado |
| 64 | — | 128 | — | — | En curso | No acreditado |
| 65 | — | 128 | — | — | En curso | No acreditado |
| 66 | — | 128 | — | — | En curso | No acreditado |
| 67 | — | 128 | — | — | En curso | No acreditado |
| 68 | — | 128 | — | — | En curso | No acreditado |
| 69 | — | 128 | — | — | En curso | No acreditado |
| 70 | — | 128 | — | — | En curso | No acreditado |
| 71 | — | 128 | — | — | En curso | No acreditado |
| 72 | — | 128 | — | — | En curso | No acreditado |
| 73 | — | 128 | — | — | En curso | No acreditado |
| 74 | — | 128 | — | — | En curso | No acreditado |
| 75 | — | 128 | — | — | En curso | No acreditado |
| 76 | — | 128 | — | — | En curso | No acreditado |
| 77 | — | 128 | — | — | En curso | No acreditado |
| 78 | — | 128 | — | — | En curso | No acreditado |
| 79 | — | 128 | — | — | En curso | No acreditado |
| 80 | — | 128 | — | — | En curso | No acreditado |
| 81 | — | 128 | — | — | En curso | No acreditado |
| 82 | — | 128 | — | — | En curso | No acreditado |
| 83 | — | 128 | — | — | En curso | No acreditado |
| 84 | — | 128 | — | — | En curso | No acreditado |
| 85 | — | 128 | — | — | En curso | No acreditado |
| 86 | — | 128 | — | — | En curso | No acreditado |
| 87 | — | 128 | — | — | En curso | No acreditado |
| 88 | — | 128 | — | — | En curso | No acreditado |
| 89 | — | 128 | — | — | En curso | No acreditado |
| 90 | — | 128 | — | — | En curso | No acreditado |
| 91 | — | 128 | — | — | En curso | No acreditado |
| 92 | — | 128 | — | — | En curso | No acreditado |
| 93 | — | 128 | — | — | En curso | No acreditado |
| 94 | — | 128 | — | — | En curso | No acreditado |
| 95 | — | 128 | — | — | En curso | No acreditado |
| 96 | — | 128 | — | — | En curso | No acreditado |
| 97 | — | 128 | — | — | En curso | No acreditado |
| 98 | — | 128 | — | — | En curso | No acreditado |
| 99 | — | 128 | — | — | En curso | No acreditado |
| 100 | — | 128 | — | — | En curso | No acreditado |
| 101 | — | 128 | — | — | En curso | No acreditado |
| 102 | — | 128 | — | — | En curso | No acreditado |
| 103 | — | 128 | — | — | En curso | No acreditado |
| 104 | — | 128 | — | — | En curso | No acreditado |
| 105 | — | 128 | — | — | En curso | No acreditado |
| 106 | — | 128 | — | — | En curso | No acreditado |
| 107 | — | 128 | — | — | En curso | No acreditado |
| 108 | — | 128 | — | — | En curso | No acreditado |
| 109 | — | 128 | — | — | En curso | No acreditado |
| 110 | — | 128 | — | — | En curso | No acreditado |
| 111 | — | 128 | — | — | En curso | No acreditado |
| 112 | — | 128 | — | — | En curso | No acreditado |
| 113 | — | 128 | — | — | En curso | No acreditado |
| 114 | — | 128 | — | — | En curso | No acreditado |
| 115 | — | 128 | — | — | En curso | No acreditado |
| 116 | — | 128 | — | — | En curso | No acreditado |
| 117 | — | 128 | — | — | En curso | No acreditado |
| 118 | — | 128 | — | — | En curso | No acreditado |
| 119 | — | 128 | — | — | En curso | No acreditado |
| 120 | — | 128 | — | — | En curso | No acreditado |
| 121 | — | 128 | — | — | En curso | No acreditado |
| 122 | — | 128 | — | — | En curso | No acreditado |
| 123 | — | 128 | — | — | En curso | No acreditado |
| 124 | — | 128 | — | — | En curso | No acreditado |
| 125 | — | 128 | — | — | En curso | No acreditado |
| 126 | — | 128 | — | — | En curso | No acreditado |
| 127 | — | 128 | — | — | En curso | No acreditado |
| 128 | — | 128 | — | — | En curso | No acreditado |

</details>

<details>
<summary>Ver tiempos y velocidad de las 128 conversaciones</summary>


## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 1,42 | 67,27 | 1,93 | 1,90 |
| 2 | 2,76 | 68,46 | 1,93 | 1,87 |
| 3 | 3,41 | 69,35 | 1,93 | 1,85 |
| 4 | 2,09 | 67,75 | 1,93 | 1,89 |
| 5 | 2,09 | 67,75 | 1,93 | 1,89 |
| 6 | 4,76 | 71,14 | 1,91 | 1,80 |
| 7 | 3,41 | 69,34 | 1,93 | 1,85 |
| 8 | 4,09 | 70,16 | 1,92 | 1,82 |
| 9 | 6,10 | 72,94 | 1,90 | 1,75 |
| 10 | 4,75 | 71,14 | 1,91 | 1,80 |
| 11 | 5,44 | 72,13 | 1,90 | 1,77 |
| 12 | 6,10 | 72,94 | 1,90 | 1,75 |

</details>


## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 40% |
| Pico medido del motor / memoria del GB10 | 36,5% |
| Pico usado por todo el sistema / memoria del GB10 | 45,8% |
| Conversaciones totales | 128 |
| Máximo de peticiones enviadas a la vez | 128 |
| Límite de solicitudes del servidor | 128 |
| Máximo activo en el motor | 91 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 3,9 s |
| Tiempo medio de respuesta completa | 70,0 s |
| Mayor espera hasta primer texto, entre las completadas | 6,1 s |
| Mayor tiempo completo, entre las completadas | 72,9 s |
| Suma de los tiempos individuales | 840,4 s |
| Tiempo total de la prueba | 73,0 s |
| Tokens/s medios por conversación, incluyendo espera | 1,83 |
| Tokens/s totales del grupo | 21,04 |
| Pico de caché ocupada | 99,8% |
| Máximo de solicitudes en cola | 125 |
| Recálculos por falta de espacio en caché | 1 |
| Tiempo observado con cola | 71,8 s |
| Tiempo observado con caché al 95% o más | 25,7 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 71,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias, los máximos de tiempo y las velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,07 | 1,49 | 67,34 |
| 2 | 0,07 | 2,83 | 68,53 |
| 3 | 0,07 | 3,49 | 69,42 |
| 4 | 0,07 | 2,16 | 67,82 |
| 5 | 0,07 | 2,16 | 67,82 |
| 6 | 0,07 | 4,83 | 71,21 |
| 7 | 0,07 | 3,49 | 69,42 |
| 8 | 0,07 | 4,16 | 70,23 |
| 9 | 0,08 | 6,18 | 73,01 |
| 10 | 0,08 | 4,83 | 71,22 |
| 11 | 0,08 | 5,51 | 72,21 |
| 12 | 0,08 | 6,18 | 73,02 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
