# Pruebas con 35% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se configuró un presupuesto del **35% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 35% | 4 activas | Conversaciones con historiales independientes | 2/2 | Terminada |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-4-comparacion-adicional/README.md) | 35% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 371,0 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-comparacion-adicional/README.md) | 35% | **4 activas** | 32.768 + 512 | **Sí: 4/4** | No se intentó | 140,7 s | 4 respuestas solapadas; cola máxima 3; 5 recálculos |
| [1 conversación; hasta 1 a la vez](2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4-comparacion-adicional/README.md) | 35% | **4 activas** | 262.016 + 128 | **Sí: 1/1** | **Sí: 1/1** | 586,5 s | 1 respuesta a la vez; cola máxima 1; 10 recálculos |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-4-comparacion-adicional/README.md) | 35% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 371,0 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-comparacion-adicional/README.md) | 35% | 31,8% | 40,0% | 32.768 + 512 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 44,1 | 136,0 | 543,9 | 140,7 | 3,77 | 14,56 | 99,2% | 3 | 5 | Terminó con 5 recálculos |
| [1 conversación; hasta 1 a la vez](2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4-comparacion-adicional/README.md) | 35% | 31,8% | 40,0% | 262.016 + 128 | 1 / 4 / 1 / 1 | **Sí: 1/1** | 566,6 | 586,4 | 586,4 | 586,5 | 0,22 | 0,22 | 99,7% | 1 | 10 | Terminó con 10 recálculos |

</details>
