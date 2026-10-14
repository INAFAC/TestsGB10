# Pruebas con 25% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **25% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

Las tablas principales muestran la batería con medición detallada. Cada fila enlaza los datos de todas sus conversaciones. Los arranques y rechazos tienen medidas que no corresponden a una generación: se marcan como «No aplica».

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 65.536 tokens](2026-10-14-arranque-contexto-65536-servidor-4/README.md) | 25% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 365,9 s | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 25% | **4 activas** | 1.024 + 128 | **Sí: 4/4** | No se intentó | 13,1 s | 4 respuestas solapadas; cola máxima 1 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4/README.md) | 25% | **4 activas** | 8.192 + 128 | **Sí: 4/4** | No se intentó | 25,9 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-256-respuesta-servidor-4/README.md) | 25% | **4 activas** | 32.768 + 256 | 3/4 (en curso) | No se intentó | 119,6 s | 1 activa en el motor; cola máxima 3 |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 65.536 tokens](2026-10-14-arranque-contexto-65536-servidor-4/README.md) | 25% | No aplica | No aplica | Sin conversaciones | Límite 4 | Arrancó | No aplica | No aplica | No aplica | 365,9 | No aplica | No aplica | No aplica | No aplica | No aplica | Arrancó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 25% | 21,7% | 29,9% | 1.024 + 128 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 2,1 | 13,0 | 51,9 | 13,1 | 9,86 | 38,96 | 25,9% | 1 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4/README.md) | 25% | 21,7% | 29,9% | 8.192 + 128 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 9,5 | 25,2 | 100,9 | 25,9 | 5,08 | 19,75 | 96,3% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-256-respuesta-servidor-4/README.md) | 25% | 21,7% | 29,8% | 32.768 + 256 | 4 / 4 / 1 / — | 3/4 (en curso) | 53,6 | 76,3 | 229,0 | 119,6 | 4,10 | 6,42 | 100,0% | 3 | 0 | En curso |

</details>
