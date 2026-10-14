# Arrancar el modelo con límite de 262.144 tokens

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 30% del GB10.

**Resultado: **NO ARRANCÓ**.**

Se comprobó el arranque con un límite de **262.144 tokens por conversación** y hasta **4 solicitudes activas**.

Tiempo de comprobación: **310,8 segundos**.

No se pudieron enviar conversaciones con esta configuración. Que otro contexto más pequeño arranque no convierte este intento en correcto.

**Motivo:** para admitir ese historial, el motor necesitaba 16,32 GiB de caché, pero solo disponía de 11,10 GiB dentro del presupuesto asignado. Es espacio para historiales; no es toda la memoria libre del equipo.

<details>
<summary>Mensaje exacto del error</summary>

```text
(EngineCore pid=462) ERROR 10-14 12:05:45 [core.py:1374] ValueError: To serve at least one request with the model's max seq len (262144), (16.32 GiB KV cache is needed, which is larger than the available KV cache memory (11.1 GiB). Based on the available memory, the estimated maximum model length is 176400. Try increasing `gpu_memory_utilization` (which also controls CPU memory on the CPU backend) or decreasing `max_model_len` when initializing the engine. See https://docs.vllm.ai/en/latest/configuration/conserving_memory/ for more details.
(EngineCore pid=462) ValueError: To serve at least one request with the model's max seq len (262144), (16.32 GiB KV cache is needed, which is larger than the available KV cache memory (11.1 GiB). Based on the available memory, the estimated maximum model length is 176400. Try increasing `gpu_memory_utilization` (which also controls CPU memory on the CPU backend) or decreasing `max_model_len` when initializing the engine. See https://docs.vllm.ai/en/latest/configuration/conserving_memory/ for more details.
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
