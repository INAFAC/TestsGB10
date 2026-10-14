# Arranque con contexto máximo 131.072

[Volver a la comparación](../README.md)

- Modelo: `nvidia/Qwen3.8-27B-NVFP4`.
- Memoria asignada: 30%.
- Límite del servidor: 4 solicitudes.
- Resultado: Arranque correcto en 366,0 s.
- No se enviaron conversaciones en esta comprobación de arranque.
- La duración mide la espera hasta disponibilidad o fallo tras recrear el servicio.
- [Registro original](../results/2026-10-14/memory/memory-30/startup-131072.log).

```text
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
