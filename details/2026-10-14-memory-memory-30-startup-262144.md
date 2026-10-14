# Arranque con contexto máximo 262.144

[Volver a la comparación](../README.md)

- Modelo: `nvidia/Qwen3.8-27B-NVFP4`.
- Memoria asignada: 30%.
- Límite del servidor: 4 solicitudes.
- Resultado: **FALLO DE ARRANQUE** en 310,8 s.
- No se enviaron conversaciones en esta comprobación de arranque.
- La duración mide la espera hasta disponibilidad o fallo tras recrear el servicio.
- [Registro original](../results/2026-10-14/memory/memory-30/startup-262144.log).

```text
(EngineCore pid=462) ERROR 10-14 12:05:45 [core.py:1374] ValueError: To serve at least one request with the model's max seq len (262144), (16.32 GiB KV cache is needed, which is larger than the available KV cache memory (11.1 GiB). Based on the available memory, the estimated maximum model length is 176400. Try increasing `gpu_memory_utilization` (which also controls CPU memory on the CPU backend) or decreasing `max_model_len` when initializing the engine. See https://docs.vllm.ai/en/latest/configuration/conserving_memory/ for more details.
(EngineCore pid=462) ValueError: To serve at least one request with the model's max seq len (262144), (16.32 GiB KV cache is needed, which is larger than the available KV cache memory (11.1 GiB). Based on the available memory, the estimated maximum model length is 176400. Try increasing `gpu_memory_utilization` (which also controls CPU memory on the CPU backend) or decreasing `max_model_len` when initializing the engine. See https://docs.vllm.ai/en/latest/configuration/conserving_memory/ for more details.
(APIServer pid=1) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
```

Comando utilizado:

```json
[
  "vllm",
  "serve",
  "nvidia/Qwen3.8-27B-NVFP4",
  "--max-num-seqs",
  "4",
  "--enable-auto-tool-choice",
  "--tool-call-parser",
  "qwen3_coder",
  "--reasoning-parser",
  "qwen3",
  "--gpu-memory-utilization",
  "0.3",
  "--max-model-len",
  "262144"
]
```
