# Pruebas de modelos en el GB10

Resultados para decidir cuánta memoria reservar y cuántas conversaciones puede atender cada modelo, incluyendo historiales cercanos a su límite.



**Cada prueba indica el límite de solicitudes activas impuesto al servidor.** Ese límite debe distinguirse de la capacidad del GB10.

## Resultados por modelo

| Modelo | Máximo por conversación | Informe |
|---|---:|---|
| Qwen3.8-27B-NVFP4 | 262.144 tokens | [Resultados y configuración](modelos/nvidia-qwen3.8-27b-nvfp4/README.md) · [Conversaciones con varios usuarios](modelos/nvidia-qwen3.8-27b-nvfp4/conversaciones-recurrentes/README.md) |

<!-- conclusiones-inicio -->
## Personas que pueden conversar hasta llenar el contexto

La [comprobación por presupuesto de memoria](modelos/nvidia-qwen3.8-27b-nvfp4/capacidad-de-conversacion/README.md) sigue conversaciones desde unos 512 tokens hasta casi 262.144, conservando todos los mensajes y las respuestas reales.

| Memoria configurada | Personas que completaron todo el recorrido útil | Resultado con dos personas |
|---:|---:|---|
| 35% | 1 | Caché llena y plazos de espera agotados |
| 40% | 1 | Caché llena y un plazo de espera agotado |
| 50% | 1 | Dejó de cumplir los tiempos establecidos |
| 60% | Al menos 1 | Repetición en curso por un error del medidor anterior |
| 70% | 1 | Dejó de cumplir los tiempos establecidos |
| 85% | 1 | Dejó de cumplir los tiempos establecidos |
| 92% | 1 | Dejó de cumplir los tiempos establecidos |

**Esta tabla usa razonamiento desactivado**, respuestas solicitadas de hasta 100 palabras, mensajes simultáneos y al menos 30 segundos de pausa entre rondas. Se exige primer texto visible en un máximo de 5 segundos para el 95% de las peticiones, ninguna espera superior a 10 segundos, al menos 5 tokens/s para el 95% y respuesta completa en 120 segundos para el 95%. Debe cumplirse en todo el recorrido y en cada tramo de hasta 16 rondas.

Es la capacidad comprobada bajo esa referencia, no un máximo universal de personas conectadas. Una prueba detenida por lentitud no demuestra que las conversaciones no puedan terminar si se aceptan esperas mayores. Los controles siguientes comprueban otras cargas.

**El límite del servidor fue cuatro solicitudes activas en estos recorridos de una y dos personas.** No obligó a las dos conversaciones a ejecutarse de una en una. Los perfiles con una persona completaron 257 rondas y terminaron naturalmente a menos de 160 tokens del máximo; no se forzó una respuesta para rellenar exactamente el contexto.

[Comparar los tiempos cerca del límite, la memoria realmente ocupada y cada intento](modelos/nvidia-qwen3.8-27b-nvfp4/capacidad-de-conversacion/README.md).

## Controles anteriores con 20 personas

Estos controles usaron **70% de memoria y un límite de 32 solicitudes activas**. Cada persona conservó su historial entre mensajes.

| Carga de 20 personas | ¿Terminaron? | Espera al continuar, p95 |
|---|---|---:|
| Chat con unos 8.192 tokens, razonamiento desactivado y hasta 2.048 de salida | 60/60 respuestas visibles y terminadas naturalmente | 2,0 s |
| El mismo control con unos 32.768 tokens | 60/60 respuestas visibles y terminadas naturalmente | 7,4 min |
| Crecimiento sintético hasta 262.144 tokens | Las 20 personas llegaron al máximo; 40/40 respuestas completas | 172,9 min |

En el chat corto, el primer turno fue más lento: 103,2 s de espera visible p95. La prueba del contexto máximo pidió 512 tokens de salida por turno y tardó 346,5 minutos en total. **Poder terminar no significa poder conversar con rapidez.**

El 70% es una referencia medida, no un mínimo demostrado. El 60% obtuvo resultados cercanos en algunas cargas sintéticas, y subir al 85% no mejoró las dos comparaciones iniciales frente al 70% en estas ejecuciones. [Ver la elección de memoria, los resultados de 10 y 30 personas y sus límites](modelos/nvidia-qwen3.8-27b-nvfp4/README.md#qué-configuración-elegir).
<!-- conclusiones-fin -->

## Qué puedes comprobar

- **Si todas las conversaciones terminaron:** cuántas recibieron la respuesta completa solicitada.
- **Si llegaron al máximo de tokens:** se comprueba la suma real de historial y respuesta. También se distingue un límite reducido por falta de memoria.
- **Si respondieron a la vez o por turnos:** se muestran el solapamiento, las colas y los recálculos.
- **Cuánto tardaron y cuánta memoria usaron:** cada prueba incluye los tiempos y velocidades de cada conversación.

Un ejemplo: **262.016 tokens de historial + 128 de respuesta = 262.144 tokens en la conversación**. Llegar a ese límite no significa generar 262.144 tokens de respuesta nueva.

## Dónde está cada cosa

Entra en **modelos → nombre del modelo**. Para saber cuántas personas pueden conversar hasta el límite, elige **capacidad de conversación**. Las comparaciones iniciales y las conversaciones recurrentes conservan las otras cargas ensayadas. Cada prueba reúne su explicación en `README.md`, sus mediciones y sus registros en la misma carpeta.

- [Guía de lectura](GUIA-DE-LECTURA.md): significado de las medidas y cómo se hicieron las pruebas.
- [Herramientas de prueba](scripts): scripts para medir y actualizar los informes.

## Licencia

El contenido de este repositorio se publica bajo [CC BY 4.0](LICENSE): puedes reutilizarlo y adaptarlo citando la fuente.
