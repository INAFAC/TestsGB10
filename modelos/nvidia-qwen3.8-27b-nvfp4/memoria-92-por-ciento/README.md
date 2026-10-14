# Pruebas con 92% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **92% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 92% | 4 activas | Conversaciones con historiales independientes | 2/2 | Terminada |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 92% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 391,1 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 92% | **4 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 556,5 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 92% | **4 activas** | 262.016 + 128 | 3/4 (errores por tiempo de espera) | **Solo: 3/4** | 1.216,2 s | 1 respuesta a la vez; cola máxima 3; 1 errores de espera |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 92% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 391,1 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 92% | 88,7% | 96,2% | 131.072 + 256 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 299,9 | 538,3 | 2.153,1 | 556,5 | 0,48 | 1,84 | 92,4% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 92% | 88,7% | 96,5% | 262.016 + 128 | 4 / 4 / 2 / 1 | 3/4 (errores por tiempo de espera) | 745,8 | 948,1 | 2.844,4 | 1.216,2 | 0,15 | 0,32 | 81,5% | 3 | 0 | Errores por tiempo de espera |

</details>
