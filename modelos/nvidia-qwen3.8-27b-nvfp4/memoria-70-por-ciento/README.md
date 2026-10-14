# Pruebas con 70% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **70% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 70% | 4 activas | Conversaciones con historiales independientes | 2/3 | En curso |
| 70% | 16 activas | Conversaciones con historiales independientes | 0/2 | Pendiente |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 70% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 375,9 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 70% | **4 activas** | 65.536 + 512 | **Sí: 4/4** | No se intentó | 238,0 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 70% | **4 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 604,9 s | 3 respuestas solapadas; cola máxima 3; 2 recálculos |
| [2 conversaciones; hasta 2 a la vez](2026-10-14-2-conversaciones-hasta-2-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 70% | **4 activas** | 262.016 + 128 | 0/2 (en curso) | Todavía no | 20,1 s | 1 activa en el motor; cola máxima 1 |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 70% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 375,9 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 70% | 66,7% | 75,7% | 65.536 + 512 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 98,8 | 231,0 | 924,1 | 238,0 | 2,22 | 8,60 | 67,1% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 70% | 66,7% | 75,5% | 131.072 + 256 | 4 / 4 / 4 / 3 | **Sí: 4/4** | 329,3 | 555,2 | 2.220,9 | 604,9 | 0,47 | 1,69 | 99,7% | 3 | 2 | Terminó con 2 recálculos |
| [2 conversaciones; hasta 2 a la vez](2026-10-14-2-conversaciones-hasta-2-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 70% | 66,7% | 75,5% | 262.016 + 128 | 2 / 4 / 1 / — | 0/2 (en curso) | No medido | No medido | No medido | 20,1 | No medido | No medido | 10,0% | 1 | 0 | En curso |

</details>
