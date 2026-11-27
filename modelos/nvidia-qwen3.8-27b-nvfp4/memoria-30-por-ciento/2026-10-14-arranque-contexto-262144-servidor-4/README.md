# Arrancar el modelo con límite de 262.144 tokens

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 30% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

**Resultado: NO ARRANCÓ.**

Se comprobó el arranque con un límite de **262.144 tokens por conversación** y hasta **4 solicitudes activas**.

Tiempo de comprobación: **310,8 segundos**.

No se pudieron enviar conversaciones con esta configuración. Que otro contexto más pequeño arranque no convierte este intento en correcto.

**Motivo:** para admitir ese historial, el motor necesitaba 16,32 GiB de caché, pero solo disponía de 11,10 GiB dentro del presupuesto asignado. Es espacio para historiales; no es toda la memoria libre del equipo.

Arrancar solo demuestra que el servicio está disponible. Las pruebas de conversaciones comprueban si las respuestas llegan a terminar.

<details>
<summary>Mediciones y parámetros de esta prueba</summary>

- [Mediciones](mediciones.json).
- [Parámetros de esta prueba](parametros.json).

</details>
