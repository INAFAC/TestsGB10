# Sondas de medición

[Volver al índice](../README.md)

Estas herramientas miden un servidor compatible con vLLM. Cada sonda acepta la dirección del servidor mediante `--base-url`. Para consultar los argumentos y las unidades, ejecuta la sonda con `--help`.

| Herramienta | Qué mide |
|---|---|
| [Contexto](context_probe.py) | Solicitudes concurrentes con longitudes de entrada y salida fijadas. |
| [Conversaciones recurrentes](recurrent_probe.py) | Tiempo de respuesta al conservar y ampliar el historial durante varios turnos. |
| [Chat](chat_probe.py) | Tiempo hasta el primer texto visible y finalización natural con mensajes sintéticos. |
| [Crecimiento del contexto](capacity_probe_v2.py) | Evolución de los tiempos desde un historial corto hasta el límite configurado. |

## Ejemplo de medición

Ejecuta la sonda en el equipo donde corre vLLM para medir su RAM y GPU. Python toma la memoria y las muestras de NVIDIA del equipo donde se ejecuta. Las métricas de vLLM proceden del servidor indicado por `--base-url`. Si ejecutas la sonda desde otro equipo, las muestras de hardware pertenecen al cliente.

Desde la raíz del repositorio, este ejemplo solicita dos respuestas sintéticas de 128 tokens y admite dos peticiones simultáneas. Requiere Python 3, el modelo indicado ya cargado y una API de vLLM accesible en el puerto local 8000.

```bash
python3 scripts/context_probe.py --base-url http://127.0.0.1:8000 \
  --model nvidia/Qwen3.8-27B-NVFP4 --concurrency 2 --requests 2 \
  --input-tokens 1024 --output-tokens 128 --result medicion-local.json
```

Para documentar el presupuesto de memoria o el límite de solicitudes activas, pasa los valores del servidor mediante `--memory-fraction` y `--server-max-seqs`. La sonda los registra como parámetros declarados.

El [control de privacidad](validate_new_public_files.py) revisa archivos nuevos o modificados. Con `python3 scripts/validate_new_public_files.py --all` también examina todos los archivos versionados del árbol de trabajo.
