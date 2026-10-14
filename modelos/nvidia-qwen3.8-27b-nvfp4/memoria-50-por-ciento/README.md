# Pruebas con 50% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **50% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 50% | 4 activas | Conversaciones con historiales independientes | 4/4 | Terminada |
| 50% | 3 activas | Conversaciones con historiales independientes | 0/1 | En curso |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-3-comparacion-adicional/README.md) | 50% | **3 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 366,0 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-3-comparacion-adicional/README.md) | 50% | **3 activas** | 65.536 + 512 | 0/4 (en curso) | No se intentó | 20,1 s | 1 activa en el motor; cola máxima 3 |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 50% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 365,9 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 50% | **4 activas** | 32.768 + 512 | **Sí: 4/4** | No se intentó | 126,8 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 50% | **4 activas** | 65.536 + 512 | **Sí: 4/4** | No se intentó | 282,4 s | 4 respuestas solapadas; cola máxima 3; 4 recálculos |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 50% | **4 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 629,3 s | 2 respuestas solapadas; cola máxima 3; 4 recálculos |
| [1 conversación; hasta 1 a la vez](2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 50% | **4 activas** | 262.016 + 128 | **Sí: 1/1** | **Sí: 1/1** | 547,0 s | 1 respuesta a la vez; cola máxima 1; 2 recálculos |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-3-comparacion-adicional/README.md) | 50% | No aplica | No aplica | Sin conversaciones | Límite 3 | Arrancó | No aplica | No aplica | No aplica | 366,0 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-3-comparacion-adicional/README.md) | 50% | 46,9% | 55,4% | 65.536 + 512 | 4 / 3 / 1 / — | 0/4 (en curso) | Pendiente | Pendiente | Pendiente | 20,1 | Pendiente | Pendiente | 12,0% | 3 | 0 | En curso |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 50% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 365,9 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 50% | 46,9% | 55,6% | 32.768 + 512 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 41,1 | 123,6 | 494,4 | 126,8 | 4,14 | 16,15 | 55,0% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 50% | 47,0% | 55,6% | 65.536 + 512 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 112,2 | 272,2 | 1.088,9 | 282,4 | 1,88 | 7,25 | 99,9% | 3 | 4 | Terminó con 4 recálculos |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 50% | 47,0% | 55,5% | 131.072 + 256 | 4 / 4 / 2 / 2 | **Sí: 4/4** | 345,6 | 485,9 | 1.943,7 | 629,3 | 0,58 | 1,63 | 99,7% | 3 | 4 | Terminó con 4 recálculos |
| [1 conversación; hasta 1 a la vez](2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 50% | 47,0% | 55,5% | 262.016 + 128 | 1 / 4 / 1 / 1 | **Sí: 1/1** | 527,9 | 546,9 | 546,9 | 547,0 | 0,23 | 0,23 | 99,5% | 1 | 2 | Terminó con 2 recálculos |

</details>
