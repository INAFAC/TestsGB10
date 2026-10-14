### Lectura provisional de los resultados

La capacidad depende del historial y de la longitud de la respuesta. **Aceptar cuatro peticiones no implica procesar cuatro historiales largos simultáneamente.** La repetición completa al 40% y los presupuestos adicionales siguen pendientes.

- **30%:** no arranca con contexto máximo de 262.144 tokens. Sí arranca al limitarlo a 131.072. Con cuatro solicitudes de 8.192 tokens se observaron cuatro activas; con 32.768, dos; con 65.536, una. Estas tres pruebas terminaron sin errores ni preempciones. Una solicitud de 130.816 tokens de entrada y 256 de salida terminó en 207 segundos, con la caché al 99,6% y cuatro preempciones.
- **40%, primera serie:** se observaron cuatro activas con entradas de 32.768 tokens, dos con 65.536 y una con 131.072. Cerca del máximo de 262.144 tokens, una sola solicitud terminó, pero necesitó cuatro preempciones y unos 539 segundos hasta el primer token. Este caso requiere más margen aunque el servidor consiga arrancar.
- **Las colas importan:** al 30%, cuatro entradas de 65.536 tokens con 512 de salida tardaron unos 348 segundos en completar el grupo. Que todas terminen no las convierte en cuatro conversaciones simultáneas.

Son máximos observados en estas cargas sintéticas y esta configuración de vLLM. No representan un límite universal de cualquier modelo, precisión de caché o longitud de respuesta. Las recomendaciones finales se incorporarán al terminar la matriz.
