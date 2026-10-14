# Qwen3.8-27B-NVFP4

[Volver al inicio](../../README.md) · [Cómo leer las medidas](../../GUIA-DE-LECTURA.md)

**Modelo exacto:** `nvidia/Qwen3.8-27B-NVFP4`.

**Estado:** pruebas en curso. Los resultados se actualizan a medida que terminan.

**Máximo por conversación: 262.144 tokens, sumando historial y respuesta.** La memoria asignada puede obligar a configurar un límite menor.

**Hasta ahora, las pruebas de conversaciones publicadas tienen un límite impuesto de cuatro solicitudes activas** (`--max-num-seqs 4`). Que aparezcan cuatro como máximo no demuestra el techo del GB10. Enviar ocho peticiones no levanta ese límite: pueden quedar en cola.

“Terminó” significa que entregó todos los tokens de respuesta solicitados. “Llegó al máximo” exige además que la suma real de entrada y respuesta alcance ese máximo; arrancar el servidor no basta.

## ¿Puede llegar al máximo y terminar?

- **30% de memoria:** Hasta ahora se ha completado una conversación de **131.072 tokens**. Aún no demuestra alcanzar 262.144. **El arranque con el máximo del modelo falló.**
- **40% de memoria:** **Sí:** 1/1 completadas con 262.144 tokens y toda la respuesta solicitada. 1 respuesta a la vez; cola máxima 1; 4 recálculos.

## Qué configuración elegir

<!-- interpretacion-inicio -->
- **30%:** ha atendido cuatro historiales de 8.192 tokens a la vez. Con historiales de 32.768 mantiene dos activas, y con 65.536, una. Con este presupuesto no pudo arrancar con el máximo de 262.144 tokens.
- **40%:** las pruebas repetidas de 32.768 tokens han terminado con cuatro respuestas solapadas; las de 65.536, con dos. Los grupos tardaron unos 126 y 269 segundos, respectivamente.
- **Llegar al máximo puede ser lento:** en la repetición al 40%, una conversación llegó exactamente a 262.144 tokens y entregó los 128 de respuesta solicitados. Tardó unos **561 segundos**, con unos **542 segundos hasta el primer texto**, y necesitó **cuatro recálculos**. Puede terminar, pero este caso tiene una espera larga.

La elección final sigue pendiente de terminar los presupuestos mayores y menores, las concurrencias superiores y la reutilización de historiales.
<!-- interpretacion-fin -->

## Todas las pruebas

Abre el nombre de una prueba para ver cada conversación, sus tiempos, los tokens recibidos y sus registros. Las primeras mediciones se conservan y están identificadas.

| Prueba | Memoria asignada | Límite impuesto al servidor | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 131.072 tokens](memoria-30-por-ciento/2026-10-14-arranque-contexto-131072-servidor-4/README.md) | 30% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 366,0 s | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens](memoria-30-por-ciento/2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 30% | **4 activas** | Sin conversaciones | **NO ARRANCÓ** | No se enviaron conversaciones | 310,8 s | **NO ARRANCÓ** |
| [4 conversaciones; hasta 4 a la vez](memoria-30-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4/README.md) | 30% | **4 activas** | 8.192 + 128 | **Sí: 4/4** | No se intentó | 25,6 s | 4 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](memoria-30-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 30% | **4 activas** | 32.768 + 512 | **Sí: 4/4** | No se intentó | 164,8 s | 2 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](memoria-30-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 30% | **4 activas** | 65.536 + 512 | **Sí: 4/4** | No se intentó | 348,4 s | 1 respuesta a la vez; cola máxima 3 |
| [1 conversación; hasta 1 a la vez](memoria-30-por-ciento/2026-10-14-1-conversaciones-hasta-1-a-la-vez-130816-entrada-256-respuesta-servidor-4/README.md) | 30% | **4 activas** | 130.816 + 256 | **Sí: 1/1** | Llegó a 131.072; límite reducido | 207,5 s | 1 respuesta a la vez; cola máxima 1; 4 recálculos |
| [Comprobar servidor ya preparado con límite de 262.144 tokens](memoria-40-por-ciento/2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 40% | **4 activas** | Sin conversaciones | Arrancó | No se enviaron conversaciones | 0,0 s | Arrancó |
| [8 conversaciones; hasta 1 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-1-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | **4 activas** | 1.024 + 128 | **Sí: 8/8** | No se intentó | 85,3 s | 1 respuesta a la vez; cola máxima 0 |
| [20 conversaciones; hasta 1 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-20-conversaciones-hasta-1-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 1.024 + 128 | **Sí: 20/20** | No se intentó | 212,5 s | No se guardó este detalle |
| [8 conversaciones; hasta 2 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-2-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | **4 activas** | 1.024 + 128 | **Sí: 8/8** | No se intentó | 46,0 s | 2 respuestas solapadas; cola máxima 0 |
| [20 conversaciones; hasta 2 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-20-conversaciones-hasta-2-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 1.024 + 128 | **Sí: 20/20** | No se intentó | 116,5 s | No se guardó este detalle |
| [8 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-4-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | **4 activas** | 1.024 + 128 | **Sí: 8/8** | No se intentó | 26,2 s | 4 respuestas solapadas; cola máxima 1 |
| [20 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-20-conversaciones-hasta-4-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 1.024 + 128 | **Sí: 20/20** | No se intentó | 63,6 s | No se guardó este detalle |
| [8 conversaciones; hasta 8 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-8-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | **4 activas** | 1.024 + 128 | **Sí: 8/8** | No se intentó | 26,1 s | 4 respuestas solapadas; cola máxima 5 |
| [20 conversaciones; hasta 8 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-20-conversaciones-hasta-8-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 1.024 + 128 | **Sí: 20/20** | No se intentó | 62,6 s | No se guardó este detalle |
| [8 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4/README.md) | 40% | **4 activas** | 8.192 + 128 | **Sí: 8/8** | No se intentó | 50,6 s | 4 respuestas solapadas; cola máxima 3 |
| [12 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-12-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 8.192 + 128 | **Sí: 12/12** | No se intentó | 71,2 s | No se guardó este detalle |
| [4 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-2048-respuesta-servidor-4/README.md) | 40% | **4 activas** | 8.192 + 2.048 | **Sí: 4/4** | No se intentó | 209,7 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 40% | **4 activas** | 32.768 + 512 | **Sí: 4/4** | No se intentó | 126,4 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 32.768 + 512 | **Sí: 4/4** | No se intentó | 125,5 s | 4 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 40% | **4 activas** | 65.536 + 512 | **Sí: 4/4** | No se intentó | 268,7 s | 2 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 65.536 + 512 | **Sí: 4/4** | No se intentó | 267,3 s | 2 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 40% | **4 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 505,2 s | 1 respuesta a la vez; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 131.072 + 256 | **Sí: 4/4** | No se intentó | 504,5 s | 1 activa en el motor; cola máxima 3 |
| [1 conversación; hasta 1 a la vez](memoria-40-por-ciento/2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 40% | **4 activas** | 262.016 + 128 | **Sí: 1/1** | **Sí: 1/1** | 560,8 s | 1 respuesta a la vez; cola máxima 1; 4 recálculos |
| [1 conversación; hasta 1 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | **4 activas** | 262.016 + 128 | **Sí: 1/1** | **Sí: 1/1** | 558,0 s | 1 activa en el motor; cola máxima 1; 4 recálculos |
| [Enviar más tokens que el límite permitido](memoria-40-por-ciento/2026-10-14-rechazo-por-superar-el-limite-de-contexto/README.md) | 40% | **4 activas** | 262.145 + 1 | Rechazada, como se esperaba | Superarlo fue rechazado | 0,0 s | Rechazo esperado: HTTP 400 |

<details>
<summary>Comparación completa de memoria, tiempos y tokens por segundo</summary>

| Prueba | Memoria asignada | Motor / GB10 | Sistema / GB10 | Entrada + respuesta | Enviadas / límite servidor / activas / respuestas solapadas | Terminadas | Espera media (s) | Respuesta media (s) | Suma individual (s) | Tiempo prueba (s) | Tokens/s por conversación | Tokens/s totales | Pico caché | Cola máxima | Recálculos | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Arrancar el modelo con límite de 131.072 tokens](memoria-30-por-ciento/2026-10-14-arranque-contexto-131072-servidor-4/README.md) | 30% | No medido | No medido | Sin conversaciones | 0 / 4 / — / — | Arrancó | No medido | No medido | No medido | 366,0 | No medido | No medido | No medido | — | — | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens](memoria-30-por-ciento/2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 30% | No medido | No medido | Sin conversaciones | 0 / 4 / — / — | **NO ARRANCÓ** | No medido | No medido | No medido | 310,8 | No medido | No medido | No medido | — | — | **NO ARRANCÓ** |
| [4 conversaciones; hasta 4 a la vez](memoria-30-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4/README.md) | 30% | 26,6% | 35,0% | 8.192 + 128 | 4 / 4 / 4 / — | **Sí: 4/4** | 9,2 | 24,9 | 99,5 | 25,6 | 5,15 | 20,00 | 45,0% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](memoria-30-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 30% | 26,6% | 34,9% | 32.768 + 512 | 4 / 4 / 2 / — | **Sí: 4/4** | 65,0 | 126,3 | 505,4 | 164,8 | 4,46 | 12,43 | 90,9% | 3 | 0 | Terminó atendiendo por turnos |
| [4 conversaciones; hasta 4 a la vez](memoria-30-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 30% | 26,6% | 34,8% | 65.536 + 512 | 4 / 4 / 1 / 1 | **Sí: 4/4** | 167,8 | 217,6 | 870,4 | 348,4 | 3,06 | 5,88 | 91,3% | 3 | 0 | Terminó atendiendo por turnos |
| [1 conversación; hasta 1 a la vez](memoria-30-por-ciento/2026-10-14-1-conversaciones-hasta-1-a-la-vez-130816-entrada-256-respuesta-servidor-4/README.md) | 30% | 26,6% | 34,8% | 130.816 + 256 | 1 / 4 / 1 / 1 | **Sí: 1/1** | 178,1 | 207,4 | 207,4 | 207,5 | 1,23 | 1,23 | 99,6% | 1 | 4 | Terminó con 4 recálculos |
| [Comprobar servidor ya preparado con límite de 262.144 tokens](memoria-40-por-ciento/2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 40% | No medido | No medido | Sin conversaciones | 0 / 4 / — / — | Arrancó | No medido | No medido | No medido | 0,0 | No medido | No medido | No medido | — | — | Arrancó |
| [8 conversaciones; hasta 1 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-1-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | 36,7% | 45,3% | 1.024 + 128 | 1 / 4 / 1 / 1 | **Sí: 8/8** | 0,5 | 10,7 | 85,2 | 85,3 | 12,02 | 12,01 | 1,6% | 0 | 0 | Terminó |
| [20 conversaciones; hasta 1 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-20-conversaciones-hasta-1-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 1.024 + 128 | 1 / 4 / — / — | **Sí: 20/20** | 0,7 | 10,6 | 212,5 | 212,5 | No medido | 12,05 | No medido | — | — | Terminó |
| [8 conversaciones; hasta 2 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-2-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | 36,7% | 45,0% | 1.024 + 128 | 2 / 4 / 2 / 2 | **Sí: 8/8** | 0,9 | 11,5 | 91,7 | 46,0 | 11,16 | 22,28 | 3,2% | 0 | 0 | Terminó |
| [20 conversaciones; hasta 2 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-20-conversaciones-hasta-2-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 1.024 + 128 | 2 / 4 / — / — | **Sí: 20/20** | 1,0 | 11,6 | 232,8 | 116,5 | No medido | 21,98 | No medido | — | — | Terminó |
| [8 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-4-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | 36,8% | 45,1% | 1.024 + 128 | 4 / 4 / 4 / 4 | **Sí: 8/8** | 2,0 | 13,0 | 104,3 | 26,2 | 9,82 | 39,07 | 5,9% | 1 | 0 | Terminó |
| [20 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-20-conversaciones-hasta-4-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 1.024 + 128 | 4 / 4 / — / — | **Sí: 20/20** | 1,4 | 12,7 | 254,1 | 63,6 | No medido | 40,23 | No medido | — | — | Terminó |
| [8 conversaciones; hasta 8 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-8-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | 36,8% | 45,1% | 1.024 + 128 | 8 / 4 / 4 / 4 | **Sí: 8/8** | 8,5 | 19,6 | 157,1 | 26,1 | 7,29 | 39,17 | 5,7% | 5 | 0 | Terminó atendiendo por turnos |
| [20 conversaciones; hasta 8 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-20-conversaciones-hasta-8-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 1.024 + 128 | 8 / 4 / — / — | **Sí: 20/20** | 11,2 | 22,6 | 451,3 | 62,6 | No medido | 40,90 | No medido | — | — | Terminó |
| [8 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-8-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4/README.md) | 40% | 36,9% | 45,2% | 8.192 + 128 | 4 / 4 / 4 / 4 | **Sí: 8/8** | 7,3 | 24,9 | 199,4 | 50,6 | 5,38 | 20,25 | 21,1% | 3 | 0 | Terminó |
| [12 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-12-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 8.192 + 128 | 4 / 4 / — / — | **Sí: 12/12** | 5,2 | 23,5 | 282,3 | 71,2 | No medido | 21,57 | No medido | — | — | Terminó |
| [4 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-2048-respuesta-servidor-4/README.md) | 40% | 36,9% | 45,3% | 8.192 + 2.048 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 9,5 | 209,0 | 835,8 | 209,7 | 9,80 | 39,07 | 23,5% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 40% | 36,9% | 45,2% | 32.768 + 512 | 4 / 4 / 4 / 4 | **Sí: 4/4** | 40,9 | 123,3 | 493,0 | 126,4 | 4,16 | 16,20 | 84,0% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 32.768 + 512 | 4 / 4 / 4 / — | **Sí: 4/4** | 40,8 | 122,5 | 490,0 | 125,5 | 4,18 | 16,32 | 84,3% | 3 | 0 | Terminó |
| [4 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 40% | 36,9% | 45,3% | 65.536 + 512 | 4 / 4 / 2 / 2 | **Sí: 4/4** | 123,4 | 208,1 | 832,5 | 268,7 | 2,70 | 7,62 | 85,6% | 3 | 0 | Terminó atendiendo por turnos |
| [4 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 65.536 + 512 | 4 / 4 / 2 / — | **Sí: 4/4** | 123,1 | 207,2 | 828,7 | 267,3 | 2,71 | 7,66 | 85,6% | 3 | 0 | Terminó atendiendo por turnos |
| [4 conversaciones; hasta 4 a la vez](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 40% | 36,9% | 45,3% | 131.072 + 256 | 4 / 4 / 1 / 1 | **Sí: 4/4** | 286,3 | 315,7 | 1.262,6 | 505,2 | 1,06 | 2,03 | 85,8% | 3 | 0 | Terminó atendiendo por turnos |
| [4 conversaciones; hasta 4 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 131.072 + 256 | 4 / 4 / 1 / — | **Sí: 4/4** | 286,4 | 315,5 | 1.261,8 | 504,5 | 1,06 | 2,03 | 86,0% | 3 | 0 | Terminó atendiendo por turnos |
| [1 conversación; hasta 1 a la vez](memoria-40-por-ciento/2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 40% | 36,9% | 45,3% | 262.016 + 128 | 1 / 4 / 1 / 1 | **Sí: 1/1** | 541,6 | 560,6 | 560,6 | 560,8 | 0,23 | 0,23 | 99,4% | 1 | 4 | Terminó con 4 recálculos |
| [1 conversación; hasta 1 a la vez · primera medición](memoria-40-por-ciento/2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | No medido | No medido | 262.016 + 128 | 1 / 4 / 1 / — | **Sí: 1/1** | 539,1 | 557,9 | 557,9 | 558,0 | 0,23 | 0,23 | 99,6% | 1 | 4 | Terminó con 4 recálculos |
| [Enviar más tokens que el límite permitido](memoria-40-por-ciento/2026-10-14-rechazo-por-superar-el-limite-de-contexto/README.md) | 40% | No medido | No medido | 262.145 + 1 | 1 / 4 / — / — | Rechazada, como se esperaba | No medido | No medido | No medido | 0,0 | No medido | No medido | No medido | — | — | Rechazo esperado: HTTP 400 |

</details>

## Carpetas por memoria

- [30% de memoria](memoria-30-por-ciento/README.md).
- [40% de memoria](memoria-40-por-ciento/README.md).

## Equipo y configuración

GB10: 121,63 GiB. Pesos del modelo: 19,95 GiB.
Imagen: `nvcr.io/nvidia/vllm:26.09-py3`. vLLM: `0.29.0+5013de39.dev`.

[Configuración y registros del equipo](configuracion-del-equipo).
