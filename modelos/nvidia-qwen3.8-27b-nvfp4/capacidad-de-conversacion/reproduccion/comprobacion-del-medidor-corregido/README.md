# Comprobación del medidor corregido

Este piloto valida el programa de pruebas; **no mide capacidad hasta el contexto completo**.

La comprobación con el tokenizador real reconstruye la ronda 131 del historial que provocó el fallo. Conservó los 261 mensajes anteriores y preparó 133.652 tokens de entrada, frente al objetivo nominal de 133.632, sin generar otra respuesta. Su resultado está en `regresion-tokenizador.json`.

El piloto de generación usa dos conversaciones, nueve rondas, objetivos de entrada de 512 a 8.192 tokens, pausas de dos segundos, razonamiento desactivado, presupuesto del 40% y límite del servidor de cuatro solicitudes. Las respuestas son reales y el historial se conserva. `comando.json` contiene los argumentos exactos.

**Piloto completado y verificado:** 18 respuestas visibles terminadas naturalmente, nueve por persona, sin errores. El verificador independiente comprobó la continuidad de todos los mensajes, los recuentos de tokens y los tiempos. El resultado está en `verificacion.json`.
