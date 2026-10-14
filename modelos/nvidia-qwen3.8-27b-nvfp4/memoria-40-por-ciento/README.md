# Pruebas con 40% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **40% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

| Prueba | Memoria asignada | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---|---|---:|---|
| [Comprobar servidor ya preparado con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 40% | Sin conversaciones | Arrancó | No se enviaron conversaciones | 0,0 s | Arrancó |
| [8 conversaciones; hasta 1 a la vez](2026-10-14-8-conversaciones-hasta-1-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | 1.024 + 128 | **Sí: 8/8** | No se intentó | 85,3 s | 1 respuesta a la vez; cola máxima 0 |
| [20 conversaciones; hasta 1 a la vez · primera medición](2026-10-14-20-conversaciones-hasta-1-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 1.024 + 128 | **Sí: 20/20** | No se intentó | 212,5 s | No se guardó este detalle |
| [8 conversaciones; hasta 2 a la vez](2026-10-14-8-conversaciones-hasta-2-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | 1.024 + 128 | **Sí: 8/8** | No se intentó | 46,0 s | 2 respuestas solapadas; cola máxima 0 |
| [20 conversaciones; hasta 2 a la vez · primera medición](2026-10-14-20-conversaciones-hasta-2-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 1.024 + 128 | **Sí: 20/20** | No se intentó | 116,5 s | No se guardó este detalle |
| [8 conversaciones; hasta 4 a la vez](2026-10-14-8-conversaciones-hasta-4-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | 1.024 + 128 | **Sí: 8/8** | No se intentó | 26,2 s | 4 respuestas solapadas; cola máxima 1 |
| [20 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-20-conversaciones-hasta-4-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 1.024 + 128 | **Sí: 20/20** | No se intentó | 63,6 s | No se guardó este detalle |
| [8 conversaciones; hasta 8 a la vez](2026-10-14-8-conversaciones-hasta-8-a-la-vez-1024-entrada-128-respuesta-servidor-4/README.md) | 40% | 1.024 + 128 | **Sí: 8/8** | No se intentó | 26,1 s | 4 respuestas solapadas; cola máxima 5 |
| [20 conversaciones; hasta 8 a la vez · primera medición](2026-10-14-20-conversaciones-hasta-8-a-la-vez-1024-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 1.024 + 128 | **Sí: 20/20** | No se intentó | 62,6 s | No se guardó este detalle |
| [8 conversaciones; hasta 4 a la vez](2026-10-14-8-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4/README.md) | 40% | 8.192 + 128 | **Sí: 8/8** | No se intentó | 50,6 s | 4 respuestas solapadas; cola máxima 3 |
| [12 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-12-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 8.192 + 128 | **Sí: 12/12** | No se intentó | 71,2 s | No se guardó este detalle |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-2048-respuesta-servidor-4/README.md) | 40% | 8.192 + 2.048 | 0/4 (en curso) | No se intentó | 195,3 s | 4 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 40% | 32.768 + 512 | **Sí: 4/4** | No se intentó | 126,4 s | 4 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 32.768 + 512 | **Sí: 4/4** | No se intentó | 125,5 s | 4 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 40% | 65.536 + 512 | **Sí: 4/4** | No se intentó | 268,7 s | 2 respuestas solapadas; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 65.536 + 512 | **Sí: 4/4** | No se intentó | 267,3 s | 2 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4/README.md) | 40% | 131.072 + 256 | **Sí: 4/4** | No se intentó | 505,2 s | 1 respuesta a la vez; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez · primera medición](2026-10-14-4-conversaciones-hasta-4-a-la-vez-131072-entrada-256-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 131.072 + 256 | **Sí: 4/4** | No se intentó | 504,5 s | 1 activa en el motor; cola máxima 3 |
| [1 conversación; hasta 1 a la vez](2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4/README.md) | 40% | 262.016 + 128 | **Sí: 1/1** | **Sí: 1/1** | 560,8 s | 1 respuesta a la vez; cola máxima 1; 4 recálculos |
| [1 conversación; hasta 1 a la vez · primera medición](2026-10-14-1-conversaciones-hasta-1-a-la-vez-262016-entrada-128-respuesta-servidor-4-medicion-inicial/README.md) | 40% | 262.016 + 128 | **Sí: 1/1** | **Sí: 1/1** | 558,0 s | 1 activa en el motor; cola máxima 1; 4 recálculos |
| [Enviar más tokens que el límite permitido](2026-10-14-rechazo-por-superar-el-limite-de-contexto/README.md) | 40% | 262.145 + 1 | Rechazada, como se esperaba | Superarlo fue rechazado | 0,0 s | Rechazo esperado: HTTP 400 |
