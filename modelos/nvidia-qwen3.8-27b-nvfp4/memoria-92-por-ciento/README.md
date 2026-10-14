# Pruebas con 92% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **92% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

## Estado de la batería prevista

Esta tabla distingue las pruebas terminadas de las que todavía faltan. No incluye las primeras mediciones del histórico. Una prueba terminada puede tener errores; el resultado de cada fila indica si las conversaciones se completaron.

| Memoria | Límite impuesto | Tipo de prueba | Terminadas / previstas | Estado |
|---:|---:|---|---:|---|
| 92% | 4 activas | Conversaciones con historiales independientes | 2/2 | Terminada |
| 92% | 4 activas | Comprobación con mayor tiempo de espera | 1/1 | Terminada |
| 92% | 512 activas | Conversaciones con historiales independientes | 1/1 | Terminada |

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 92% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 391,1 s | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-4-comparacion-adicional-espera-ampliada/README.md) | 92% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 391,1 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 92% | **4 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 556,5 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 92% | **4 activas** | 262.016 + 128 | 3/4 (errores por tiempo de espera) | **Solo: 3/4** | 1.216,2 s | 1 respuesta a la vez; cola máxima 3; 1 error de espera |
| [4 conversaciones; hasta 4 a la vez · espera ampliada](2026-10-14-4-conversaciones-hasta-4-a-la-vez-262016-entrada-128-respuesta-servidor-4-comparacion-adicional-espera-ampliada/README.md) | 92% | **4 activas** | 262.016 + 128 | **Sí: 4/4** | **Sí: 4/4** | 1.540,7 s | 1 respuesta a la vez; cola máxima 3 |
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-512-comparacion-adicional/README.md) | 92% | **512 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 436,4 s | Arrancó |
| [512 conversaciones; hasta 512 a la vez](2026-10-14-512-conversaciones-hasta-512-a-la-vez-1024-entrada-512-respuesta-servidor-512-comparacion-adicional/README.md) | 92% | **512 activas** | 1.024 + 512 | **Sí: 512/512** | No se intentó | 998,4 s | 347 respuestas solapadas; cola máxima 508 |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 92% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 391,1 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-4-comparacion-adicional-espera-ampliada/README.md) | 92% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 391,1 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 92% | 88,7% | 96,2% | 131.072 + 256 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 299,9 | 538,3 | 2.153,1 | 556,5 | 0,48 | 1,84 | 92,4% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 92% | 88,7% | 96,5% | 262.016 + 128 | 4 / 4 / 2 / 1 | 3/4 (errores por tiempo de espera) | 745,8 | 948,1 | 2.844,4 | 1.216,2 | 0,15 | 0,32 | 81,5% | 3 | 0 | Errores por tiempo de espera |
| [4 conversaciones; hasta 4 a la vez · espera ampliada](2026-10-14-4-conversaciones-hasta-4-a-la-vez-262016-entrada-128-respuesta-servidor-4-comparacion-adicional-espera-ampliada/README.md) | 92% | 88,6% | 96,0% | 262.016 + 128 | 4 / 4 / 2 / 1 | **Sí: 4/4** | 930,2 | 1.132,9 | 4.531,4 | 1.540,7 | 0,13 | 0,33 | 81,6% | 3 | 0 | Terminó atendiendo por turnos |
| [Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)](2026-10-14-arranque-contexto-262144-servidor-512-comparacion-adicional/README.md) | 92% | No aplica | No aplica | Sin conversaciones | Límite 512 | Arrancó | No aplica | No aplica | No aplica | 436,4 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [512 conversaciones; hasta 512 a la vez](2026-10-14-512-conversaciones-hasta-512-a-la-vez-1024-entrada-512-respuesta-servidor-512-comparacion-adicional/README.md) | 92% | 89,4% | 98,8% | 1.024 + 512 | 512 / 512 / 347 / 347 | **Sí: 512/512** | 303,4 | 799,7 | 409.432,6 | 998,4 | 0,66 | 262,56 | 99,9% | 508 | 0 | Terminó atendiendo por turnos |

</details>
