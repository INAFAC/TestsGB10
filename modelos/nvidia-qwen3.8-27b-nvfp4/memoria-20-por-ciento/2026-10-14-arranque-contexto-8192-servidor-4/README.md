# Arrancar el modelo con límite de 8.192 tokens

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 20% del GB10.

**Límite impuesto al servidor: 4 solicitudes activas** (`--max-num-seqs 4`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

**Resultado: **NO ARRANCÓ**.**

Se comprobó el arranque con un límite de **8.192 tokens por conversación** y hasta **4 solicitudes activas**.

Tiempo de comprobación: **310,8 segundos**.

No se pudieron enviar conversaciones con esta configuración. Que otro contexto más pequeño arranque no convierte este intento en correcto.

<details>
<summary>Mensaje exacto del error</summary>

```text
(EngineCore pid=461) ERROR 10-14 13:20:44 [core.py:1374] ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine (this flag also controls CPU memory reservation on the CPU backend, despite its name). See https://docs.vllm.ai/en/latest/configuration/conserving_memory/ for more details.
(EngineCore pid=461) ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine (this flag also controls CPU memory reservation on the CPU backend, despite its name). See https://docs.vllm.ai/en/latest/configuration/conserving_memory/ for more details.
(APIServer pid=1) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
```

</details>

Arrancar solo demuestra que el servicio está disponible. Las pruebas de conversaciones comprueban si las respuestas llegan a terminar.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro del servidor](registro-del-servidor.log).

</details>
