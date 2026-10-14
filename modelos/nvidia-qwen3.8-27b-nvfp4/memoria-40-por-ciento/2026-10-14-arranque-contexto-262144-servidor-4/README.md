# Comprobar servidor ya preparado con límite de 262.144 tokens

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Resultado: Arrancó.**

Se comprobó el arranque con un límite de **262.144 tokens por conversación** y hasta **4 solicitudes activas**.

Tiempo de comprobación: **0,0 segundos**.

El servidor ya estaba preparado. Este tiempo es la comprobación de disponibilidad, no la carga del modelo.

Arrancar solo demuestra que el servicio está disponible. Las pruebas de conversaciones comprueban si las respuestas llegan a terminar.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro del servidor](registro-del-servidor.log).

</details>
