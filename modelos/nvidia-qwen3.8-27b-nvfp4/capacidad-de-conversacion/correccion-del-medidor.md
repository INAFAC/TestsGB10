# Corrección del medidor y repetición completada

[Volver a los resultados](README.md)

El primer intento del **60% con dos personas** terminó después de 130 rondas por un error del programa de pruebas. La respuesta real de una persona ocupó 1.003 tokens; conservarla junto con la siguiente pregunta superaba el incremento fijo de 1.024 tokens que esperaba el generador. El programa se detuvo antes de enviar la ronda siguiente.

Las 260 respuestas recibidas se conservan. El bloque de rondas 114–129 ya había superado los 120 segundos de referencia para completar una respuesta, pero **la interrupción del programa no demuestra un límite de memoria ni una frontera completa de capacidad del GB10**. La frontera se cerró con una nueva ejecución, sin borrar este intento.

## Qué se corrigió

La [segunda versión del medidor](../../../scripts/capacity_probe_v2.py) conserva íntegramente el historial. Si una respuesta larga hace imposible el siguiente incremento nominal, aumenta lo mínimo necesario el objetivo de entrada y registra el objetivo nominal, el efectivo y el tamaño mínimo del nuevo mensaje. No sustituye respuestas ni recorta mensajes anteriores.

Además, las respuestas anteriores al cierre reservan 256 tokens para la pregunta final y su respuesta. En el cierre se reservan aproximadamente 128 tokens de salida, según el tamaño exacto de la entrada. Esto solo reduce el presupuesto de salida cuando queda poco espacio de contexto; cada petición publica su límite efectivo. Es una diferencia explícita respecto a la primera versión, por lo que la repetición se identifica por separado.

Si el propio medidor vuelve a fallar, guarda un estado de error del medidor en vez de dejar una última instantánea marcada como «en curso».

## Comprobaciones realizadas

- La [comprobación local de regresión](../../../scripts/check_capacity_probe_v2.py) reprodujo una respuesta larga, comprobó la continuidad del historial y verificó la reserva para el cierre.
- **Comprobación con el tokenizador real superada.** Reconstruyó la ronda 131 del intento fallido conservando los 261 mensajes anteriores, incluida la respuesta de 1.003 tokens. La entrada necesitaba 133.652 tokens, veinte más que el objetivo nominal de 133.632. No generó otra respuesta ni midió capacidad.
- **Piloto real superado y verificado:** dos personas, nueve rondas y 18 respuestas visibles terminadas naturalmente, sin errores. Un [verificador independiente](../../../scripts/verify_capacity_pilot.py) comprobó los historiales, los recuentos de tokens y los tiempos. Este piloto solo llegó a unos 8.192 tokens. [Resultados y comprobaciones](reproduccion/comprobacion-del-medidor-corregido/README.md).
- El [controlador de repetición](../../../scripts/capacity_recovery.py) archivó el estado y la comprobación de restauración anteriores. Conserva todos los intentos y restaura la configuración original al terminar.

## Resultado de la repetición

La [nueva ejecución del 60% con dos personas](memoria-60-personas-2-recorrido-completo-intento-2/README.md) terminó con **209 rondas por persona y 418 respuestas visibles terminadas naturalmente**, sin errores, colas ni recálculos. Duró **231,0 minutos**, incluidas las pausas. Las conversaciones alcanzaron **213.623 y 213.659 tokens**, aproximadamente el 81,5% del contexto máximo.

Se detuvo por tres rondas seguidas fuera de la referencia: en las rondas 207, 208 y 209 la velocidad mínima medida fue de **4,94, 4,90 y 4,99 tokens/s**, por debajo de los 5 exigidos. El primer bloque completo fuera de referencia había sido el **162–177**, por una espera visible p95 de **5,29 segundos**. La caché solo alcanzó el **56,3%**; la parada no fue un error de memoria.

El resultado final al 60% es **una persona con recorrido completo y útil bajo los criterios del ensayo**. Las dos personas no mantuvieron esos criterios hasta el contexto máximo. Esto no demuestra que no puedan terminar si se admiten esperas mayores y menor velocidad.

## Por qué se conservan los dos intentos

Las respuestas reales variaron entre ejecuciones. Comparando el mismo bloque de rondas 114–129:

| Medida | Primer intento | Repetición |
|---|---:|---:|
| Respuestas medidas | 32 | 32 |
| Tokens de salida por respuesta, media | 538,5 | 205,3 |
| Mayor respuesta del bloque | 979 tokens | 354 tokens |
| Tiempo completo p95 | 122,1 s | 49,5 s |

La repetición produjo respuestas más cortas en ese bloque. **La diferencia de tiempo no demuestra que corregir el medidor acelerase el modelo.** Las observaciones lentas del primer intento siguen siendo válidas y se conservan. La repetición no necesitó aumentar ningún objetivo nominal; la corrección del caso de 1.003 tokens se comprobó por separado con su historial exacto y el tokenizador real.

La comprobación final de restauración, realizada después de todas las pruebas, se publica en los [registros de reproducción](reproduccion/README.md).
