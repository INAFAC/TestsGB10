# Arranque con contexto máximo 131.072

[Volver a la comparación](../README.md)

- Modelo: `nvidia/Qwen3.8-27B-NVFP4`.
- Memoria asignada: 30%.
- Límite del servidor: 4 solicitudes.
- Resultado: Arranque correcto en 366,0 s.
- No se enviaron conversaciones en esta comprobación de arranque.
- [Registro original](../results/2026-10-14/memory/memory-30/startup-131072.log).

```text
(EngineCore pid=461) INFO 10-14 12:11:48 [gpu_worker.py:860] Free memory on device (115.64/121.63 GiB) on startup. Desired GPU memory utilization is (0.3, 36.49 GiB). Actual usage is 23.27 GiB for consumed memory (weights + non-torch), 2.11 GiB for peak activation, and 0.05 GiB for CUDAGraph memory. Replace gpu_memory_utilization config with `--kv-cache-memory=11719394816` (10.91 GiB) to fit into requested memory, or `--kv-cache-memory=96703700480` (90.06 GiB) to fully utilize gpu memory. Current kv cache memory in use is 11.11 GiB.
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
  "131072"
]
```
