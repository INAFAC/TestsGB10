# Pruebas con 85% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **85% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 85% | 4 activas | Conversaciones con historiales independientes | 2/2 | Terminada |
| 85% | 4 activas | Comprobación con mayor tiempo de espera | 0/1 | Pendiente |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 85% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 401,1 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 85% | **4 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 813,6 s | 3 respuestas solapadas; cola máxima 3; 1 recálculos |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 85% | **4 activas** | 262.016 + 128 | 2/4 (errores por tiempo de espera) | **Solo: 2/4** | 1.200,5 s | 1 respuesta a la vez; cola máxima 3; 2 errores de espera |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 85% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 401,1 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 85% | 81,6% | 88,7% | 131.072 + 256 | 4 / 4 / 4 / 3 | **Sí: 4/4** | 408,8 | 754,7 | 3.018,8 | 813,6 | 0,34 | 1,26 | 99,9% | 3 | 1 | Terminó con 1 recálculos |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 85% | 81,6% | 88,7% | 262.016 + 128 | 4 / 4 / 2 / 1 | 2/4 (errores por tiempo de espera) | 633,2 | 943,3 | 1.886,6 | 1.200,5 | 0,14 | 0,21 | 90,6% | 3 | 0 | Errores por tiempo de espera |

</details>
