# Repetición pendiente por un error del medidor

[Volver a los resultados](README.md)

El primer intento del **60% con dos personas** terminó después de 130 rondas por un error del programa de pruebas. La respuesta real de una persona ocupó 1.003 tokens; conservarla junto con la siguiente pregunta superaba el incremento fijo de 1.024 tokens que esperaba el generador. El programa se detuvo antes de enviar la ronda siguiente.

Las 260 respuestas recibidas se conservan. El bloque de rondas 114–129 ya había superado los 120 segundos de referencia para completar una respuesta, pero **la interrupción del programa no demuestra un límite de memoria ni una frontera completa de capacidad del GB10**. La tabla deja esa frontera pendiente de repetir.

## Corrección preparada

La [segunda versión del medidor](../../../scripts/capacity_probe_v2.py) conserva íntegramente el historial. Si una respuesta larga hace imposible el siguiente incremento nominal, aumenta lo mínimo necesario el objetivo de entrada y registra el objetivo nominal, el efectivo y el tamaño mínimo del nuevo mensaje. No sustituye respuestas ni recorta mensajes anteriores.

Además, las respuestas anteriores al cierre reservan 256 tokens para la pregunta final y su respuesta. En el cierre se mantienen hasta 128 tokens de salida. Esto solo reduce el presupuesto de salida cuando queda poco espacio de contexto; cada petición publica su límite efectivo. Es una diferencia explícita respecto a la primera versión, por lo que la repetición se identifica por separado.

Si el propio medidor vuelve a fallar, guarda un estado de error del medidor en vez de dejar una última instantánea marcada como «en curso».

## Estado

- La [comprobación local de regresión](../../../scripts/check_capacity_probe_v2.py) reproduce el caso de una respuesta larga, comprueba la continuidad del historial y verifica la reserva para el cierre.
- Falta validar esta versión contra el servidor y ejecutar la repetición completa.
- El [controlador de repetición](../../../scripts/capacity_recovery.py) está preparado: exige que termine la batería original y que el servicio esté restaurado, archiva el estado anterior, conserva los intentos y restaura de nuevo al terminar. Su modo `--check-only` identifica los casos pendientes sin ejecutar pruebas ni cambiar el servicio.
- La batería original continúa con su versión original. Se conservarán sus fuentes y todos sus intentos.
- El caso del 60% se repetirá después de la batería original; cualquier otro intento interrumpido por el medidor también requerirá revisión antes de cerrar las conclusiones.

Esta comprobación local valida el programa, no mide rendimiento del modelo.
