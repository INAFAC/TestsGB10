# Repetición pendiente por un error del medidor

[Volver a los resultados](README.md)

El primer intento del **60% con dos personas** terminó después de 130 rondas por un error del programa de pruebas. La respuesta real de una persona ocupó 1.003 tokens; conservarla junto con la siguiente pregunta superaba el incremento fijo de 1.024 tokens que esperaba el generador. El programa se detuvo antes de enviar la ronda siguiente.

Las 260 respuestas recibidas se conservan. El bloque de rondas 114–129 ya había superado los 120 segundos de referencia para completar una respuesta, pero **la interrupción del programa no demuestra un límite de memoria ni una frontera completa de capacidad del GB10**. La tabla deja esa frontera pendiente de repetir.

## Corrección preparada

La [segunda versión del medidor](../../../scripts/capacity_probe_v2.py) conserva íntegramente el historial. Si una respuesta larga hace imposible el siguiente incremento nominal, aumenta lo mínimo necesario el objetivo de entrada y registra el objetivo nominal, el efectivo y el tamaño mínimo del nuevo mensaje. No sustituye respuestas ni recorta mensajes anteriores.

Además, las respuestas anteriores al cierre reservan 256 tokens para la pregunta final y su respuesta. En el cierre se reservan aproximadamente 128 tokens de salida, según el tamaño exacto de la entrada. Esto solo reduce el presupuesto de salida cuando queda poco espacio de contexto; cada petición publica su límite efectivo. Es una diferencia explícita respecto a la primera versión, por lo que la repetición se identifica por separado.

Si el propio medidor vuelve a fallar, guarda un estado de error del medidor en vez de dejar una última instantánea marcada como «en curso».

## Estado

- La [comprobación local de regresión](../../../scripts/check_capacity_probe_v2.py) reproduce el caso de una respuesta larga, comprueba la continuidad del historial y verifica la reserva para el cierre.
- **Comprobación con el tokenizador real superada.** Reconstruyó la ronda 131 conservando los 261 mensajes anteriores. La entrada necesitaba 133.652 tokens, veinte más que el objetivo nominal de 133.632. No generó otra respuesta ni midió capacidad.
- **Piloto real superado y verificado:** dos personas, nueve rondas y 18 respuestas visibles terminadas naturalmente, sin errores. Un [verificador independiente](../../../scripts/verify_capacity_pilot.py) comprobó los historiales, los recuentos de tokens y los tiempos. El piloto solo llegó a unos 8.192 tokens: no demuestra capacidad hasta el contexto completo. [Resultados y comprobaciones del medidor](reproduccion/comprobacion-del-medidor-corregido/README.md).
- La batería original ha terminado y su restauración al 40% con límite de cuatro solicitudes ha sido verificada.
- **Repetición del 60% con dos personas iniciada.** El [controlador](../../../scripts/capacity_recovery.py) archiva el estado anterior y conserva los intentos. Al terminar volverá a restaurar el servicio y comprobará la restauración de forma independiente.

La comprobación del programa está completada; la nueva medición de capacidad sigue pendiente de terminar.
