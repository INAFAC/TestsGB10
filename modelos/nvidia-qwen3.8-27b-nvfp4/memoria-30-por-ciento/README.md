# Pruebas con 30% de memoria

[Volver a todas las pruebas del modelo](../README.md)

En estas pruebas se reservó el **30% de la memoria del GB10** para el motor. El uso medido y la caché ocupada se muestran dentro de cada prueba.

| Prueba | Memoria asignada | Tokens por conversación: entrada + respuesta | ¿Terminaron? | ¿Llegaron al máximo del modelo? | Tiempo total | Simultaneidad, colas y problemas |
|---|---:|---:|---|---|---:|---|
| [Arrancar el modelo con límite de 131.072 tokens](2026-10-14-arranque-contexto-131072-servidor-4/README.md) | 30% | Sin conversaciones | Arrancó | No se enviaron conversaciones | 366,0 s | Arrancó |
| [Arrancar el modelo con límite de 262.144 tokens](2026-10-14-arranque-contexto-262144-servidor-4/README.md) | 30% | Sin conversaciones | **NO ARRANCÓ** | No se enviaron conversaciones | 310,8 s | **NO ARRANCÓ** |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-8192-entrada-128-respuesta-servidor-4/README.md) | 30% | 8.192 + 128 | **Sí: 4/4** | No se intentó | 25,6 s | 4 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-32768-entrada-512-respuesta-servidor-4/README.md) | 30% | 32.768 + 512 | **Sí: 4/4** | No se intentó | 164,8 s | 2 activas en el motor; cola máxima 3 |
| [4 conversaciones; hasta 4 a la vez](2026-10-14-4-conversaciones-hasta-4-a-la-vez-65536-entrada-512-respuesta-servidor-4/README.md) | 30% | 65.536 + 512 | **Sí: 4/4** | No se intentó | 348,4 s | 1 respuesta a la vez; cola máxima 3 |
| [1 conversación; hasta 1 a la vez](2026-10-14-1-conversaciones-hasta-1-a-la-vez-130816-entrada-256-respuesta-servidor-4/README.md) | 30% | 130.816 + 256 | **Sí: 1/1** | Llegó a 131.072; límite reducido | 207,5 s | 1 respuesta a la vez; cola máxima 1; 4 recálculos |
