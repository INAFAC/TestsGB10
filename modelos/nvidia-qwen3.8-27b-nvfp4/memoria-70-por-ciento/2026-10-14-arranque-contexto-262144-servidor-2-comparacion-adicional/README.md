# Arrancar el modelo con límite de 262.144 tokens (comprobación adicional)

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 70% del GB10.

**Límite impuesto al servidor: 2 solicitudes activas** (`--max-num-seqs 2`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

**Resultado: Arrancó.**

Se comprobó el arranque con un límite de **262.144 tokens por conversación** y hasta **2 solicitudes activas**.

Tiempo de comprobación: **376,0 segundos**.

Arrancar solo demuestra que el servicio está disponible. Las pruebas de conversaciones comprueban si las respuestas llegan a terminar.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro del servidor](registro-del-servidor.log).

</details>
