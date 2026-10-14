# Pruebas con 50% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **50% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 50% | 4 activas | Conversaciones con historiales independientes | 2/4 | En curso |
| 50% | 3 activas | Conversaciones con historiales independientes | 0/1 | Pendiente |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 50% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 365,9 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 50% | **4 activas** | 32.768 + 512 | **Sí: 4/4** | No se intentó | 126,8 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 50% | **4 activas** | 65.536 + 512 | **Sí: 4/4** | No se intentó | 282,4 s | 4 respuestas solapadas; cola máxima 3; 4 recálculos |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 50% | **4 activas** | 131.072 + 256 | 2/4 (en curso) | No se intentó | 469,2 s | 2 activas en el motor; cola máxima 3; 2 recálculos |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 50% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 365,9 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 50% | 46,9% | 55,6% | 32.768 + 512 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 41,1 | 123,6 | 494,4 | 126,8 | 4,14 | 16,15 | 55,0% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 50% | 47,0% | 55,6% | 65.536 + 512 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 112,2 | 272,2 | 1.088,9 | 282,4 | 1,88 | 7,25 | 99,9% | 3 | 4 | Terminó con 4 recálculos |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 50% | 47,0% | 55,5% | 131.072 + 256 | 4 / 4 / 2 / — | 2/4 (en curso) | 190,1 | 355,4 | 710,8 | 469,2 | 0,74 | 1,09 | 99,6% | 3 | 2 | En curso |

</details>
