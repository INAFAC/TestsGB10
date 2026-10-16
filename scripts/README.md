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
| `recurrent_probe.py` | Mantiene varios usuarios durante varios turnos y reutiliza los tokens realmente generados en sus respuestas. |
| `chat_probe.py` | Control con mensajes de chat ficticios: conserva las respuestas y distingue razonamiento, texto visible y finalización natural. |
| `recurrent_campaign.py` | Ejecuta la cola de configuraciones temporales de conversaciones recurrentes y restaura el servicio capturado al comenzar. |
| `recurrent_report.py` | Publica únicamente las pruebas recurrentes terminadas, con sus tablas, registros sanitizados y huellas de procedencia. |
| `finalize_recurrent_campaign.py` | Espera al último ensayo, comprueba que estén registrados todos los intentos previstos, cierra la cola y verifica la restauración. |
| `verify_recurrent_restore.py` | Comprueba al finalizar la configuración restaurada, la salud del servicio, una generación breve y la ausencia de solicitudes pendientes. |
| `validate_recurrent.py` | Verifica la continuidad real de las conversaciones y, al cerrar la campaña, su cobertura y restauración. |
| `validate_new_public_files.py` | Revisa los archivos nuevos o modificados antes de publicar para detectar posibles datos sensibles; complementa la revisión manual. |
| `capacity_probe.py` | Sigue conversaciones desde unos 512 tokens hasta el límite utilizable, conservando todos los mensajes y las respuestas reales. |
| `capacity_campaign.py` | Busca por presupuesto de memoria el mayor grupo medido con tiempos aceptables durante todo el recorrido y restaura la configuración capturada. |
| `capacity_report.py` | Publica el avance, las trayectorias y la frontera medida de usuarios por memoria; no presenta un recorrido en curso como capacidad demostrada. |
| `validate_capacity.py` | Comprueba la continuidad de cada mensaje, los tokens, los tiempos, los scripts ejecutados y las afirmaciones de capacidad. |
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

## Medir varias rondas de conversación

Ejemplo para ejecutar en el GB10 contra un servidor **ya configurado** al 70% y con límite de 32 solicitudes activas:

```bash
python3 recurrent_probe.py --model nvidia/Qwen3.8-27B-NVFP4 \
  --concurrency 20 --server-max-seqs 32 --memory-fraction 0.7 \
  --input-tokens 8192 --output-tokens 512 --turns 3 \
  --think-seconds 30 --new-message-tokens 256 \
  --seed 20008192 --case-id 20-usuarios-historial-8192-tres-turnos \
  --result /tmp/prueba-recurrente/mediciones.json \
  --state-output /tmp/prueba-recurrente/historiales.json.gz
```

Cada persona conserva su propia conversación. La prueba guarda mediciones parciales mientras se ejecuta, pero el publicador solo incorpora un resultado cuando el controlador registra su finalización. El archivo comprimido permite ampliar esos mismos historiales mediante `--parent-state` en otra prueba.

Para el control con mensajes legibles se utiliza `chat_probe.py` con los mismos argumentos. Un identificador que termine en `-sin-razonamiento` desactiva el razonamiento; en otro caso se mantiene el modo predeterminado del servidor. El tamaño inicial es aproximado, los turnos siguientes incluyen los mensajes reales y cada respuesta puede terminar antes del límite de salida. Los tokens enviados y recibidos se registran en cada petición.

## Publicación de las conversaciones recurrentes

La [cola publicada](../modelos/nvidia-qwen3.8-27b-nvfp4/conversaciones-recurrentes/configuracion-y-registros/queue.json) y el [plan](../modelos/nvidia-qwen3.8-27b-nvfp4/conversaciones-recurrentes/plan.json) describen los parámetros utilizados. El controlador conserva el comando del servicio al comenzar y lo restaura al cerrar la cola. Mientras la cola permanece abierta, espera las decisiones de la siguiente etapa.

`recurrent_report.py` lee los originales de una caché local privada. La opción `--sync --host ALIAS_SSH` los descarga del GB10; `--publish` añade el commit y lo sube después de generar y validar los informes. El alias SSH se configura localmente y no se guarda en el repositorio. Los originales completos permanecen fuera de GitHub; los registros publicados sustituyen rutas personales y direcciones privadas y conservan sus huellas en el inventario.

Las versiones archivadas bajo `configuracion-y-registros/scripts/versions/` permiten identificar el código ejecutado por cada prueba. Una corrección posterior de las herramientas no cambia el código ni los resultados de las pruebas anteriores.

## Reanudar una campaña sin perder sus resultados

`recurrent_campaign.py --root RUTA --resume --check` comprueba la configuración capturada y enumera las etapas ya registradas y las pendientes. Con `--resume` se conserva la configuración original para la restauración y se omiten los intentos registrados. Un intento interrumpido se conserva y su repetición recibe un nombre diferente. El primer arranque de la reanudación recrea el servicio para retirar peticiones antiguas.

El controlador debe ejecutarse en el GB10 con entrada desconectada y salida a un archivo, independiente de la sesión SSH. La pérdida del canal de salida ya no aborta su registro de progreso. Un bloqueo de archivo evita dos controladores sobre la misma campaña.

`advance_recurrent_maximum.py --root RUTA` espera a que exista una prueba completa de veinte usuarios con 131.072 tokens. Comprueba los historiales y las respuestas conservadas antes de añadir la prueba de contexto máximo. Mantiene la cola abierta para la revisión y restauración finales.

`finalize_recurrent_campaign.py --root RUTA --check` informa sin cerrar la cola. Sin `--check`, espera también de forma independiente de SSH: solo cierra cuando existe el intento de contexto máximo y están registradas todas las cargas requeridas. Tras la restauración del controlador ejecuta la comprobación independiente. Los intentos interrumpidos no sustituyen las pruebas requeridas. El cierre automático no publica conclusiones ni sustituye la revisión final del informe.
