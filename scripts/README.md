# Herramientas de prueba

[Volver a los resultados](../README.md)

| Herramienta | Uso |
|---|---|
| `context_probe.py` | Envía conversaciones a un modelo ya arrancado y mide tokens, tiempos, memoria y caché. |
| `memory_matrix.py` | Ejecuta una batería de configuraciones temporales y restaura la configuración original al terminar. |
| `followup_tests.py` | Comprueba qué ocurre al repetir y ampliar un mismo historial. |
| `short_benchmark.sh` | Reproduce las primeras pruebas cortas con la herramienta oficial de vLLM. |
| `import_measurements.py` | Organiza las mediciones de esta campaña por modelo, memoria y prueba. |
| `build_report.py` | Genera los informes a partir de los datos guardados junto a cada prueba. No necesita conectarse al GB10. |
| `validate_report.py` | Comprueba tokens, tiempos, enlaces y conservación de los archivos originales. Si la campaña se marca como terminada, verifica también que todos los bloques previstos estén resueltos y exista una comprobación final de restauración. |
| `sync_results.py` | Descarga la campaña en curso, actualiza los informes y puede publicarlos en GitHub. |

## Medir una configuración ya desplegada

Ejecutar en el GB10, porque la telemetría de hardware corresponde a la máquina que ejecuta el script:

```bash
python3 context_probe.py --model nvidia/Qwen3.8-27B-NVFP4 \
  --concurrency 4 --requests 4 --input-tokens 32768 --output-tokens 512 \
  --memory-fraction 0.4 --server-max-seqs 4 \
  --result /tmp/prueba-4-conversaciones.json
```

Los argumentos de memoria y límite del servidor registran la configuración existente; no la cambian.

## Actualizar el informe guardado

Desde la raíz del repositorio:

```bash
python3 scripts/build_report.py
python3 scripts/validate_report.py
```

El generador lee las carpetas de `modelos/`. Cada prueba contiene la configuración que describe qué se pidió y las mediciones originales que muestran qué ocurrió. Para otro modelo, se utiliza otra carpeta de modelo; no se mezclan sus resultados con los de Qwen.
