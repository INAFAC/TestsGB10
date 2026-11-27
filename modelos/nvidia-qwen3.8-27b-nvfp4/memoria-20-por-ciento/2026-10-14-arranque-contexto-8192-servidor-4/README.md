# Arrancar el modelo con límite de 8.192 tokens

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 20% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

**Resultado: NO ARRANCÓ.**

Se comprobó el arranque con un límite de **8.192 tokens por conversación** y hasta **4 solicitudes activas**.

Tiempo de comprobación: **310,8 segundos**.

No se pudieron enviar conversaciones con esta configuración. Que otro contexto más pequeño arranque no convierte este intento en correcto.

**Motivo:** después de preparar el modelo, no quedaba memoria dentro del presupuesto asignado para reservar la caché de los historiales. Falló antes de atender conversaciones, incluso con este límite de contexto reducido.

Arrancar solo demuestra que el servicio está disponible. Las pruebas de conversaciones comprueban si las respuestas llegan a terminar.

<details>
<summary>Mediciones y parámetros de esta prueba</summary>

- [Mediciones](mediciones.json).
- [Parámetros de esta prueba](parametros.json).

</details>
