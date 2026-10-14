# Qué miden estas pruebas

El objetivo es encontrar configuraciones útiles para este modelo en un solo GB10: memoria reservada, tamaño del historial, solicitudes simultáneas y espera del usuario. El límite observado corresponde a la imagen de vLLM, la precisión de caché y los parámetros registrados; cambiar esos parámetros puede cambiar el resultado.

## Cargas y tiempos

- Las entradas son listas de IDs de tokens sintéticos, con semillas guardadas. No son conversaciones reales ni pruebas de calidad o exactitud.
- Cada solicitud pide un número fijo de tokens de salida (`ignore_eos=true`, temperatura 0). Así se pueden comparar cargas del mismo tamaño sin que una termine antes por decisión del modelo.
- Las pruebas de contexto usan prefijos independientes. Las pruebas de reutilización repiten un mismo prefijo y después lo amplían. Una conversación cuyo historial permanezca en caché puede tardar mucho menos en empezar que un historial nuevo del mismo tamaño.
- El cronómetro individual comienza al enviar la petición, después de construir su entrada. Incluye la cola del servidor. El tiempo de la prueba incluye también preparación y medición; no incluye cargar el modelo salvo en las filas específicas de arranque.
- El inicio o TTFT es la llegada del primer fragmento de texto no vacío por streaming. Los tokens totales se toman de `usage`, no del número de fragmentos recibidos.
- La velocidad individual con espera es `tokens de salida / duración individual`. La velocidad durante generación se calcula como `(tokens de salida − 1) / (duración individual − TTFT)`. Es una medida desde el cliente, no un contador interno de pasos de la GPU.
- La velocidad total es `suma de tokens de salida completados / duración de la prueba`. No se obtiene sumando velocidades individuales. Tampoco debe confundirse con velocidad de procesamiento de los tokens de entrada.

## Memoria, caché y concurrencia

`--gpu-memory-utilization` es el presupuesto del motor respecto a la memoria total. Incluye pesos, caché y otras reservas; no equivale al porcentaje de caché que están utilizando las conversaciones. En el GB10 la memoria es unificada y también hay que dejar espacio al sistema y a otros procesos.

El pico del motor se mide con `nvidia-smi`; el del sistema con `MemAvailable`. Son mediciones distintas. La memoria asignada no indica que esa cantidad contenga información útil en ese momento.

Las métricas de vLLM se muestrean aproximadamente cada segundo, y memoria/temperatura GPU aproximadamente cada cinco segundos. Un pico más breve puede no verse. La caché puede conservar prefijos de peticiones anteriores: un porcentaje alto por sí solo no prueba falta de memoria. Las preempciones y las esperas aportan contexto.

Se distinguen:

1. **Concurrencia del cliente:** peticiones que puede mantener enviadas a la vez.
2. **Límite del servidor:** `--max-num-seqs`.
3. **Pico activo del motor:** solicitudes observadas en ejecución, incluyendo lectura de entrada.
4. **Respuestas solapadas:** intervalos desde el primer fragmento hasta el final que coinciden en el tiempo. Este dato está en el detalle individual; no implica un token para cada petición en cada paso.

Una cola breve al comenzar a leer varias entradas es normal. Si el pico activo permanece por debajo de las solicitudes enviadas, la prueba puede completar gracias a atenderlas por turnos. Las preempciones indican que hubo solicitudes desalojadas y trabajo repetido.

## Cómo interpretar el máximo

Una configuración es más útil cuando completa todas las solicitudes, conserva el paralelismo esperado, no repite trabajo y ofrece una espera aceptable para su uso. No existe un único máximo de conversaciones independiente de sus historiales y respuestas.

Las conclusiones distinguen el mínimo **probado** que funciona, el máximo **observado** en cada carga y los casos no ensayados. Una única ejecución de un contexto largo no demuestra estabilidad durante días ni proporciona un intervalo estadístico de confianza. La temperatura, el orden de las pruebas y la reutilización de caché también pueden influir en los tiempos.

Los arranques fallidos, rechazos de contexto e interrupciones quedan registrados. Un intento sin progreso puede detenerse a los 90 segundos; un ensayo tiene un límite de 1.500 segundos. Una interrupción no demuestra que la carga sea imposible: significa que no completó dentro del criterio aplicado.

Los archivos JSON conservan solicitudes y muestras. Los detalles enlazan esos originales. `scripts/validate_report.py` comprueba las cuentas, la cronología y los enlaces; nunca rellena métricas que no se midieron.
