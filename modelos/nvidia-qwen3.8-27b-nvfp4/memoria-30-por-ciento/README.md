# Pruebas con 30% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se configuró un presupuesto del **30% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 30% | 4 activas | Conversaciones con historiales independientes | 4/4 | Terminada |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 131.072 tokens](2026-10-14-arranque-contexto-131072-servidor-4/README.md) | 30% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 366,0 s | Arrancó |
| [Arrancar el modelo con límite de 131.072 tokens (comprobación adicional)](2026-10-14-arranque-contexto-131072-servidor-4-comparacion-adicional/README.md) | 30% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 376,1 s | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 30% | **4 activas** | Sin conversaciones | **NO ARRANCÓ** | No se enviaron conversaciones | 310,8 s | **NO ARRANCÓ** |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4-comparacion-adicional/README.md) | 30% | **4 activas** | 8.192 + 128 | **Sí: 4/4** | No se intentó | 25,7 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-comparacion-adicional/README.md) | 30% | **4 activas** | 32.768 + 512 | **Sí: 4/4** | No se intentó | 165,7 s | 2 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 30% | **4 activas** | 65.536 + 512 | **Sí: 4/4** | No se intentó | 348,4 s | 1 respuesta a la vez; cola máxima 3 |
| [1 conversación; hasta 1 a la vez](2026-10-14-1-conversaciones-hasta-1-a-la-vez-130816-entrada-256-respuesta-servidor-4/README.md) | 30% | **4 activas** | 130.816 + 256 | **Sí: 1/1** | Llegó a 131.072; límite reducido | 207,5 s | 1 respuesta a la vez; cola máxima 1; 4 recálculos |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 131.072 tokens](2026-10-14-arranque-contexto-131072-servidor-4/README.md) | 30% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 366,0 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [Arrancar el modelo con límite de 131.072 tokens (comprobación adicional)](2026-10-14-arranque-contexto-131072-servidor-4-comparacion-adicional/README.md) | 30% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 376,1 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 30% | No aplica | No aplica | Sin conversaciones | Límite 4 | **NO ARRANCÓ** | No aplica | No aplica | No aplica | 310,8 | No aplica | No aplica | No aplica | No aplica | No aplica | **NO ARRANCÓ** |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4-comparacion-adicional/README.md) | 30% | 26,8% | 34,9% | 8.192 + 128 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 9,1 | 24,9 | 99,6 | 25,7 | 5,14 | 19,94 | 43,9% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-comparacion-adicional/README.md) | 30% | 26,8% | 34,8% | 32.768 + 512 | 4 / 4 / 2 / 2 | **Sí: 4/4** | 65,1 | 127,0 | 507,9 | 165,7 | 4,44 | 12,36 | 88,6% | 3 | 0 | Terminó atendiendo por turnos |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 30% | 26,6% | 34,8% | 65.536 + 512 | 4 / 4 / 1 / 1 | **Sí: 4/4** | 167,8 | 217,6 | 870,4 | 348,4 | 3,06 | 5,88 | 91,3% | 3 | 0 | Terminó atendiendo por turnos |
| [1 conversación; hasta 1 a la vez](2026-10-14-1-conversaciones-hasta-1-a-la-vez-130816-entrada-256-respuesta-servidor-4/README.md) | 30% | 26,6% | 34,8% | 130.816 + 256 | 1 / 4 / 1 / 1 | **Sí: 1/1** | 178,1 | 207,4 | 207,4 | 207,5 | 1,23 | 1,23 | 99,6% | 1 | 4 | Terminó con 4 recálculos |

</details>

<details>
<summary>Histórico: primeras mediciones con menos datos</summary>

Estas pruebas anteriores sí se realizaron, pero no recogían todas las medidas. «No medido» aquí significa que el dato no se registró, no que falte subirlo. Las repeticiones con medición detallada están en las tablas principales; sus cargas y cantidades se indican en cada fila.

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [4 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 30% | **4 activas** | 8.192 + 128 | **Sí: 4/4** | No se intentó | 25,6 s | 4 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-medicion-inicial/README.md) | 30% | **4 activas** | 32.768 + 512 | **Sí: 4/4** | No se intentó | 164,8 s | 2 activas en el motor; cola máxima 3 |

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [4 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 30% | 26,6% | 35,0% | 8.192 + 128 | 4 / 4 / 4 / — | **Sí: 4/4** | 9,2 | 24,9 | 99,5 | 25,6 | 5,15 | 20,00 | 45,0% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-medicion-inicial/README.md) | 30% | 26,6% | 34,9% | 32.768 + 512 | 4 / 4 / 2 / — | **Sí: 4/4** | 65,0 | 126,3 | 505,4 | 164,8 | 4,46 | 12,43 | 90,9% | 3 | 0 | Terminó atendiendo por turnos |

</details>
