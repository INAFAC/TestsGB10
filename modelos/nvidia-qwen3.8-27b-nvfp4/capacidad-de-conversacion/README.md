# Cuántas personas pueden conversar hasta llenar el contexto

[Volver al modelo](../README.md)

**La pregunta medida es cuántas personas mantienen una conversación útil desde el principio hasta el límite de contexto, para cada presupuesto de memoria.** Cada persona conserva todos sus mensajes y las respuestas reales.

## Qué se considera útil

Las respuestas deben tener texto visible y terminar naturalmente. En cada bloque de hasta 16 rondas se exige primer texto en 5 s o menos para el 95% de las peticiones, ninguna espera superior a 10 s, al menos 5 tokens/s para el 95% y respuesta completa en 120 s o menos para el 95%. También se comprueba el conjunto del recorrido. Son criterios explícitos de comparación, no una definición universal de comodidad.

**La tabla principal usa razonamiento desactivado**, respuestas solicitadas de hasta 100 palabras y un límite de 1.024 tokens de salida. No se debe aplicar ese número de personas al modo de razonamiento predeterminado: sus controles se muestran aparte.

## Capacidad comprobada por memoria

| Presupuesto del modelo | Personas con recorrido completo y útil | Siguiente grupo ensayado | Estado de la comprobación |
|---:|---:|---:|---|
| 70% | 1 | 2 | Frontera local medida |
| 40% | 1 | 2 | Frontera local medida |
| 50% | 1 | 2 | Frontera local medida |
| 60% | Al menos 1 | 2 | Repetición pendiente por error del medidor; frontera sin cerrar |
| 85% | Pendiente de completar el recorrido | 1 (en curso) | En curso |
| 35% | Pendiente de completar el recorrido | — | Pendiente |
| 92% | Pendiente de completar el recorrido | — | Pendiente |

El presupuesto de memoria no es un límite estricto de toda la RAM del GB10. El límite activo del servidor es el mayor entre cuatro y las personas de la prueba; nunca es inferior al grupo enviado. La búsqueda llega hasta 32 personas: si se alcanza ese techo se informa como un mínimo demostrado, nunca como el máximo del equipo. La búsqueda acota los grupos ensayados; no demuestra todas las configuraciones posibles.

## Recorridos y controles individuales

| Prueba | Memoria | Personas | Rondas medidas | Mayor contexto alcanzado | Espera visible p95 al continuar | Velocidad p05 | Tiempo del grupo | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [Recorrido desde el principio](memoria-70-personas-1-recorrido-completo-intento-1/README.md) | 70% | 1 | 257 | 262.029 | 3,4 s | 6,69 tokens/s | 248,1 min | Cumple |
| [Recorrido desde el principio](memoria-70-personas-2-recorrido-completo-intento-1/README.md) | 70% | 2 | 210 | 214.768 | 5,4 s | 5,17 tokens/s | 213,2 min | Tres rondas seguidas con tiempos fuera de referencia |
| [Control con razonamiento](memoria-70-personas-1-control-con-razonamiento-intento-3/README.md) | 70% | 1 | 5 | 11.239 | 42,5 s | 11,92 tokens/s | 6,2 min | No cumple |
| [Recorrido desde el principio](memoria-40-personas-1-recorrido-completo-intento-1/README.md) | 40% | 1 | 257 | 262.026 | 3,3 s | 6,70 tokens/s | 223,2 min | Cumple |
| [Recorrido desde el principio](memoria-40-personas-2-recorrido-completo-intento-1/README.md) | 40% | 2 | 183 | 187.084 | 4,6 s | 5,59 tokens/s | 172,7 min | Error de API o plazo de espera del cliente |
| [Control con razonamiento](memoria-40-personas-1-control-con-razonamiento-intento-3/README.md) | 40% | 1 | 5 | 11.587 | 74,3 s | 11,86 tokens/s | 6,7 min | No cumple |
| [Recorrido desde el principio](memoria-50-personas-1-recorrido-completo-intento-1/README.md) | 50% | 1 | 257 | 262.029 | 3,3 s | 6,71 tokens/s | 238,7 min | Cumple |
| [Recorrido desde el principio](memoria-50-personas-2-recorrido-completo-intento-1/README.md) | 50% | 2 | 210 | 214.876 | 5,5 s | 5,25 tokens/s | 221,3 min | Tres rondas seguidas con tiempos fuera de referencia |
| [Control con razonamiento](memoria-50-personas-1-control-con-razonamiento-intento-3/README.md) | 50% | 1 | 5 | 11.538 | 46,2 s | 11,90 tokens/s | 6,6 min | No cumple |
| [Recorrido desde el principio](memoria-60-personas-1-recorrido-completo-intento-1/README.md) | 60% | 1 | 257 | 262.026 | 3,3 s | 6,68 tokens/s | 273,6 min | Cumple |
| [Recorrido desde el principio](memoria-60-personas-2-recorrido-completo-intento-1/README.md) | 60% | 2 | 130 | 133.608 | 3,7 s | 6,65 tokens/s | 202,1 min | Medidor interrumpido; repetición pendiente |
| [Control con razonamiento](memoria-60-personas-1-control-con-razonamiento-intento-3/README.md) | 60% | 1 | 5 | 10.807 | 38,3 s | 11,87 tokens/s | 5,6 min | No cumple |
| Recorrido desde el principio | 85% | 1 | 144 | 147.241 | 2,4 s | 8,04 tokens/s | 137,0 min | En curso; no es un resultado final |

El intento de **60% con 2 personas** fue interrumpido por el medidor. [Causa y repetición pendiente](correccion-del-medidor.md). No se usa ese error para atribuir un límite al GB10.

## Cómo avanza cada conversación

1. Cada conversación empieza con aproximadamente 512 tokens.
2. El historial completo avanza aproximadamente 1024 tokens por turno, sumando la respuesta anterior y un mensaje nuevo con notas ficticias. Nunca se reemplaza, recorta ni salta el historial anterior.
3. Se piden respuestas de hasta 100 palabras y se permiten hasta 1024 tokens de salida.
4. Cada persona espera al menos 30 segundos. La siguiente ronda empieza cuando todas están listas: se comprueban mensajes simultáneos durante todo el recorrido.
5. El penúltimo objetivo reserva 1024 tokens para la respuesta; el último deja 128 y pide un cierre de hasta diez palabras. Se publica el total real alcanzado por cada persona.
6. Se detiene un intento con tres rondas seguidas fuera de la referencia después de al menos ocho rondas, o ante errores, ausencia de texto visible o respuestas cortadas. Se conserva el punto y la causa.
7. Se aumenta 1, 2, 4, 8... personas y se acota con valores intermedios hasta un grupo que cumple y el siguiente que no cumple. Si una persona falla se comprueban también dos.
8. Un recorrido completo por tamaño de grupo; no se presentan esos resultados como repeticiones independientes.
9. Se hacen controles separados del razonamiento predeterminado con 8192 tokens iniciales, cinco turnos y hasta 4096 tokens de salida. Estos controles no establecen su límite completo.
10. El límite activo del servidor es el mayor entre cuatro y el número de personas de la prueba; nunca se impone un límite inferior al grupo enviado. Cada cambio se registra.

## Alcance de la respuesta

- El resultado depende del ritmo, longitud de mensajes, respuestas y modo de razonamiento aquí descritos.
- Si 32 personas cumplen se publica al menos 32, sin afirmar un máximo del hardware.
- La búsqueda comprueba una frontera local y los grupos ensayados; no garantiza monotonicidad de todos los grupos posibles.
- La conversación mantiene datos ficticios y respuestas reales; no se evalúa la calidad semántica ni la recuperación perfecta de toda la información.
- No se fuerza una respuesta a ocupar los últimos tokens: se reserva espacio para terminar naturalmente y se publica cuánto queda libre.
- En las pruebas previas, el 30% falló al arrancar con el contexto completo; el 25% se probó con un máximo reducido de 65536 tokens y el 20% falló incluso con 8192. Esos resultados no equivalen a completar una conversación útil de 262144 tokens.
- El porcentaje configurado es el presupuesto del motor, no un límite estricto de toda la RAM del sistema.

La prueba mide tiempos y finalización. No garantiza que todas las respuestas sean correctas ni que el modelo recuerde perfectamente todos los detalles del historial.

[Plan exacto](plan.json) · [Datos de ejecución y scripts reproducibles](reproduccion/README.md)

