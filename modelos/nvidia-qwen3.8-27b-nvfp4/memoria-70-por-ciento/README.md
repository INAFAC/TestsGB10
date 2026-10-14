# Pruebas con 70% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **70% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 70% | 4 activas | Conversaciones con historiales independientes | 3/3 | Terminada |
| 70% | 16 activas | Conversaciones con historiales independientes | 2/2 | Terminada |
| 70% | 2 activas | Conversaciones con historiales independientes | 1/1 | Terminada |
| 70% | 4 activas | Repetir y ampliar el mismo historial | 0/6 | En curso |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-2-comparacion-adicional/README.md) | 70% | **2 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 376,0 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-2-comparacion-adicional/README.md) | 70% | **2 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 477,1 s | 2 respuestas solapadas; cola máxima 3 |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 70% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 375,9 s | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-4-comparacion-adicional/README.md) | 70% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 370,9 s | Arrancó |
| [Historial nuevo: 65.536 + 128 tokens](2026-10-14-1-conversaciones-hasta-1-a-la-vez-65536-entrada-128-respuesta-servidor-4-1-historial-nuevo/README.md) | 70% | **4 activas** | 65.536 + 128 | 0/1 (en curso) | No se intentó | 35,2 s | 1 activa en el motor; cola máxima 0 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 70% | **4 activas** | 65.536 + 512 | **Sí: 4/4** | No se intentó | 238,0 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 70% | **4 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 604,9 s | 3 respuestas solapadas; cola máxima 3; 2 recálculos |
| [2 conversaciones; hasta 2 a la vez](2026-10-14-2-conversaciones-hasta-2-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 70% | **4 activas** | 262.016 + 128 | **Sí: 2/2** | **Sí: 2/2** | 722,3 s | 1 respuesta a la vez; cola máxima 1; 1 recálculo |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-16/README.md) | 70% | **16 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 396,0 s | Arrancó |
| [16 conversaciones; hasta 16 a la vez](2026-10-14-16-conversaciones-hasta-16-a-la-vez-32768-entrada-256-respuesta-servidor-16/README.md) | 70% | **16 activas** | 32.768 + 256 | **Sí: 16/16** | No se intentó | 508,1 s | 12 respuestas solapadas; cola máxima 15 |
| [16 conversaciones; hasta 16 a la vez](2026-10-14-16-conversaciones-hasta-16-a-la-vez-65536-entrada-128-respuesta-servidor-16/README.md) | 70% | **16 activas** | 65.536 + 128 | **Sí: 16/16** | No se intentó | 960,5 s | 4 respuestas solapadas; cola máxima 15 |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-2-comparacion-adicional/README.md) | 70% | No aplica | No aplica | Sin conversaciones | Límite 2 | Arrancó | No aplica | No aplica | No aplica | 376,0 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-2-comparacion-adicional/README.md) | 70% | 66,7% | 75,4% | 131.072 + 256 | 4 / 2 / 2 / 2 | **Sí: 4/4** | 269,0 | 376,3 | 1.505,1 | 477,1 | 0,74 | 2,15 | 66,9% | 3 | 0 | Terminó atendiendo por turnos |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 70% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 375,9 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-4-comparacion-adicional/README.md) | 70% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 370,9 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [Historial nuevo: 65.536 + 128 tokens](2026-10-14-1-conversaciones-hasta-1-a-la-vez-65536-entrada-128-respuesta-servidor-4-1-historial-nuevo/README.md) | 70% | 66,8% | 75,6% | 65.536 + 128 | 1 / 4 / 1 / — | 0/1 (en curso) | Pendiente | Pendiente | Pendiente | 35,2 | Pendiente | Pendiente | 12,4% | 0 | 0 | En curso |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 70% | 66,7% | 75,7% | 65.536 + 512 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 98,8 | 231,0 | 924,1 | 238,0 | 2,22 | 8,60 | 67,1% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 70% | 66,7% | 75,5% | 131.072 + 256 | 4 / 4 / 4 / 3 | **Sí: 4/4** | 329,3 | 555,2 | 2.220,9 | 604,9 | 0,47 | 1,69 | 99,7% | 3 | 2 | Terminó con 2 recálculos |
| [2 conversaciones; hasta 2 a la vez](2026-10-14-2-conversaciones-hasta-2-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 70% | 66,7% | 75,6% | 262.016 + 128 | 2 / 4 / 2 / 1 | **Sí: 2/2** | 495,2 | 589,5 | 1.179,0 | 722,3 | 0,23 | 0,35 | 100,0% | 1 | 1 | Terminó con 1 recálculo |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-16/README.md) | 70% | No aplica | No aplica | Sin conversaciones | Límite 16 | Arrancó | No aplica | No aplica | No aplica | 396,0 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [16 conversaciones; hasta 16 a la vez](2026-10-14-16-conversaciones-hasta-16-a-la-vez-32768-entrada-256-respuesta-servidor-16/README.md) | 70% | 66,9% | 75,8% | 32.768 + 256 | 16 / 16 / 12 / 12 | **Sí: 16/16** | 231,2 | 464,9 | 7.438,4 | 508,1 | 0,56 | 8,06 | 98,3% | 15 | 0 | Terminó atendiendo por turnos |
| [16 conversaciones; hasta 16 a la vez](2026-10-14-16-conversaciones-hasta-16-a-la-vez-65536-entrada-128-respuesta-servidor-16/README.md) | 70% | 67,0% | 75,7% | 65.536 + 128 | 16 / 16 / 5 / 4 | **Sí: 16/16** | 494,3 | 656,2 | 10.498,4 | 960,5 | 0,24 | 2,13 | 68,0% | 15 | 0 | Terminó atendiendo por turnos |

</details>
