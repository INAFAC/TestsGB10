# Cuántas personas pueden conversar hasta llenar el contexto

[Volver al modelo](../README.md)

**La pregunta medida es cuántas personas mantienen una conversación útil desde el principio hasta el límite de contexto, para cada presupuesto de memoria.** Cada persona conserva todos sus mensajes y las respuestas reales.

## Qué se considera útil

Las respuestas deben tener texto visible y terminar naturalmente. En cada bloque de hasta 16 rondas se exige primer texto en 5 s o menos para el 95% de las peticiones, ninguna espera superior a 10 s, al menos 5 tokens/s para el 95% y respuesta completa en 120 s o menos para el 95%. También se comprueba el conjunto del recorrido. Son criterios explícitos de comparación, no una definición universal de comodidad.

**La tabla principal usa razonamiento desactivado**, respuestas solicitadas de hasta 100 palabras y un límite de 1.024 tokens de salida. No se debe aplicar ese número de personas al modo de razonamiento predeterminado: sus controles se muestran aparte.

## Capacidad comprobada por memoria

| Presupuesto del modelo | Personas con recorrido completo y útil | Siguiente grupo ensayado | Estado de la comprobación |
|---:|---:|---:|---|
| 35% | 1 | 2 | Comprobado: el siguiente grupo no cumple |
| 40% | 1 | 2 | Comprobado: el siguiente grupo no cumple |
| 50% | 1 | 2 | Comprobado: el siguiente grupo no cumple |
| 60% | Al menos 1 | 2 (en curso) | Buscando el máximo; mínimo ya comprobado; repetición del medidor pendiente; frontera sin cerrar |
| 70% | 1 | 2 | Comprobado: el siguiente grupo no cumple |
| 85% | 1 | 2 | Comprobado: el siguiente grupo no cumple |
| 92% | 1 | 2 | Comprobado: el siguiente grupo no cumple |

El presupuesto de memoria no es un límite estricto de toda la RAM del GB10. El límite activo del servidor es el mayor entre cuatro y las personas de la prueba; nunca es inferior al grupo enviado. La búsqueda llega hasta 32 personas: si se alcanza ese techo se informa como un mínimo demostrado, nunca como el máximo del equipo. La búsqueda acota los grupos ensayados; no demuestra todas las configuraciones posibles.

## Cómo responde una persona cerca del límite

Estos son los últimos 16 turnos de los recorridos completos, aproximadamente de 247.000 a 262.000 tokens de entrada. La memoria y la caché muestran el pico de todo el recorrido. Cada porcentaje corresponde a una ejecución; las diferencias pequeñas no prueban por sí solas que un porcentaje sea más rápido.

| Presupuesto | Primer texto p95, tramo final | Velocidad p05, tramo final | Respuesta completa p95, tramo final | Pico del motor / GB10 | Pico de caché |
|---:|---:|---:|---:|---:|---:|
| [35%](memoria-35-personas-1-recorrido-completo-intento-1/README.md) | 3,84 s | 6,56 tokens/s | 60,1 s | 31,7% | 94,5% |
| [40%](memoria-40-personas-1-recorrido-completo-intento-1/README.md) | 3,88 s | 6,56 tokens/s | 46,1 s | 36,7% | 70,5% |
| [50%](memoria-50-personas-1-recorrido-completo-intento-1/README.md) | 3,88 s | 6,57 tokens/s | 40,0 s | 46,6% | 46,3% |
| [60%](memoria-60-personas-1-recorrido-completo-intento-1/README.md) | 3,90 s | 6,54 tokens/s | 61,8 s | 56,7% | 34,5% |
| [70%](memoria-70-personas-1-recorrido-completo-intento-1/README.md) | 3,87 s | 6,55 tokens/s | 63,7 s | 66,8% | 27,1% |
| [85%](memoria-85-personas-1-recorrido-completo-intento-1/README.md) | 4,90 s | 6,02 tokens/s | 71,2 s | 81,8% | 21,0% |
| [92%](memoria-92-personas-1-recorrido-completo-intento-1/README.md) | 4,97 s | 6,05 tokens/s | 69,9 s | 88,8% | 19,0% |

## Recorridos y controles individuales

| Prueba | Memoria | Personas | Rondas medidas | Mayor contexto alcanzado | Espera visible p95 al continuar | Velocidad p05 | Tiempo del grupo | Resultado |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [Recorrido desde el principio](memoria-70-personas-1-recorrido-completo-intento-1/README.md) | 70% | 1 | 257 | 262.029 | 3,4 s | 6,69 tokens/s | 248,1 min | Cumple |
| [Recorrido desde el principio](memoria-70-personas-2-recorrido-completo-intento-1/README.md) | 70% | 2 | 210 | 214.768 | 5,4 s | 5,17 tokens/s | 213,2 min | Tres rondas seguidas con tiempos fuera de referencia |
| [Control con razonamiento](memoria-70-personas-1-control-con-razonamiento-intento-3/README.md) | 70% | 1 | 5 | 11.239 | 42,5 s | 11,92 tokens/s | 6,2 min | No cumple |
| [Recorrido desde el principio](memoria-40-personas-1-recorrido-completo-intento-1/README.md) | 40% | 1 | 257 | 262.026 | 3,3 s | 6,70 tokens/s | 223,2 min | Cumple |
| [Recorrido desde el principio](memoria-40-personas-2-recorrido-completo-intento-1/README.md) | 40% | 2 | 183 | 187.084 | 4,6 s | 5,59 tokens/s | 172,7 min | Plazo de espera agotado: 1 petición, turno 183 |
| [Control con razonamiento](memoria-40-personas-1-control-con-razonamiento-intento-3/README.md) | 40% | 1 | 5 | 11.587 | 74,3 s | 11,86 tokens/s | 6,7 min | No cumple |
| [Recorrido desde el principio](memoria-50-personas-1-recorrido-completo-intento-1/README.md) | 50% | 1 | 257 | 262.029 | 3,3 s | 6,71 tokens/s | 238,7 min | Cumple |
| [Recorrido desde el principio](memoria-50-personas-2-recorrido-completo-intento-1/README.md) | 50% | 2 | 210 | 214.876 | 5,5 s | 5,25 tokens/s | 221,3 min | Tres rondas seguidas con tiempos fuera de referencia |
| [Control con razonamiento](memoria-50-personas-1-control-con-razonamiento-intento-3/README.md) | 50% | 1 | 5 | 11.538 | 46,2 s | 11,90 tokens/s | 6,6 min | No cumple |
| [Recorrido desde el principio](memoria-60-personas-1-recorrido-completo-intento-1/README.md) | 60% | 1 | 257 | 262.026 | 3,3 s | 6,68 tokens/s | 273,6 min | Cumple |
| [Recorrido desde el principio](memoria-60-personas-2-recorrido-completo-intento-1/README.md) | 60% | 2 | 130 | 133.608 | 3,7 s | 6,65 tokens/s | 202,1 min | Medidor interrumpido; repetición pendiente |
| [Control con razonamiento](memoria-60-personas-1-control-con-razonamiento-intento-3/README.md) | 60% | 1 | 5 | 10.807 | 38,3 s | 11,87 tokens/s | 5,6 min | No cumple |
| [Recorrido desde el principio](memoria-85-personas-1-recorrido-completo-intento-1/README.md) | 85% | 1 | 257 | 262.029 | 4,2 s | 6,16 tokens/s | 293,2 min | Cumple |
| [Recorrido desde el principio](memoria-85-personas-2-recorrido-completo-intento-1/README.md) | 85% | 2 | 186 | 190.125 | 6,4 s | 5,45 tokens/s | 164,4 min | Tres rondas seguidas con tiempos fuera de referencia |
| [Control con razonamiento](memoria-85-personas-1-control-con-razonamiento-intento-3/README.md) | 85% | 1 | 5 | 10.942 | 50,7 s | 11,86 tokens/s | 5,8 min | No cumple |
| [Recorrido desde el principio](memoria-35-personas-1-recorrido-completo-intento-1/README.md) | 35% | 1 | 257 | 262.028 | 3,3 s | 6,70 tokens/s | 262,6 min | Cumple |
| [Recorrido desde el principio](memoria-35-personas-2-recorrido-completo-intento-1/README.md) | 35% | 2 | 135 | 136.869 | 4,1 s | 6,56 tokens/s | 120,4 min | Plazo de espera agotado: 2 peticiones, turno 135 |
| [Control con razonamiento](memoria-35-personas-1-control-con-razonamiento-intento-3/README.md) | 35% | 1 | 5 | 10.885 | 45,3 s | 11,97 tokens/s | 5,7 min | No cumple |
| [Recorrido desde el principio](memoria-92-personas-1-recorrido-completo-intento-1/README.md) | 92% | 1 | 257 | 262.029 | 4,2 s | 6,19 tokens/s | 275,6 min | Cumple |
| [Recorrido desde el principio](memoria-92-personas-2-recorrido-completo-intento-1/README.md) | 92% | 2 | 173 | 176.853 | 5,9 s | 5,75 tokens/s | 167,5 min | Tres rondas seguidas con tiempos fuera de referencia |
| [Control con razonamiento](memoria-92-personas-1-control-con-razonamiento-intento-3/README.md) | 92% | 1 | 5 | 11.336 | 41,2 s | 11,86 tokens/s | 6,4 min | No cumple |
| Recorrido desde el principio | 60% | 2 | 144 | 147.309 | 3,9 s | 6,36 tokens/s | 140,8 min | En curso; no es un resultado final |

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

Los objetivos de entrada admiten hasta 32 tokens de diferencia al construir el mensaje. Por eso los 128 tokens reservados para el cierre son aproximados: su presupuesto efectivo se calcula con la entrada real. Cada respuesta registra tanto ese presupuesto como los tokens que finalmente utilizó.

**La repetición usa la versión 2 del medidor.** Conserva todo el historial y aumenta el siguiente objetivo lo mínimo necesario si una respuesta larga rebasa el incremento nominal. Antes del cierre reserva 256 tokens para poder añadir la pregunta final y terminar; esto reduce la salida disponible cerca del límite. Cada petición registra sus objetivos y su presupuesto efectivo. El intento original y la repetición se conservan por separado. [Corrección y comprobaciones](correccion-del-medidor.md).

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

