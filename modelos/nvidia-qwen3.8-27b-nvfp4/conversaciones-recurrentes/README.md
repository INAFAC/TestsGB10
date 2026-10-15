# Conversaciones recurrentes con varios usuarios

[Volver al modelo](../README.md)

**Se están realizando nuevas pruebas de conversaciones recurrentes con 10, 20 y 30 usuarios.**

El objetivo es saber cuánto espera cada persona al continuar su conversación, cómo cambia esa espera al crecer el historial y qué presupuesto de memoria conviene. La concurrencia del servidor **depende de cada prueba**; esta campaña comienza con un límite de 32 solicitudes activas para permitir hasta 30 usuarios sin imponer el antiguo límite de cuatro.

## Recorrido de las pruebas

| Etapa | Usuarios | Historial inicial | Memoria | Turnos por persona |
|---|---:|---|---|---:|
| Seleccionar memoria | 20 | 8.192 y 32.768 tokens | 40%, 70%, 85% | 3 |
| Comparar usuarios | 10 y 30 | 8.192 y 32.768 tokens | La seleccionada con las mediciones | 3 |
| Comprobar crecimiento | 10, 20 y 30 | 65.536 tokens | La seleccionada | 2 |
| Comprobar historiales muy largos | 20; también los grupos que mantengan fluidez en la etapa anterior | 131.072 tokens | La seleccionada | 2 |
| Llegar al máximo | 20 | 260.864 tokens, después 261.632 | La seleccionada | 2 |
| Afinar el presupuesto si aporta una mejora | 20 | 8.192 y 32.768 tokens | 50%; después 60% si hace falta | 3 |

Cada respuesta solicita 512 tokens. Después de recibirla, cada usuario espera 30 segundos y añade 256 tokens de mensaje, conservando el historial y la respuesta real anterior. Los primeros mensajes de cada grupo se envían simultáneamente; los siguientes siguen el ritmo de cada usuario. Los historiales son sintéticos y permiten medir rendimiento, no calidad de las respuestas.

Como referencia orientativa de fluidez se usarán una espera al primer texto de hasta cinco segundos para el 95% de las solicitudes y una velocidad de al menos diez tokens/s para el 95%. Se mostrarán por separado el primer turno y las continuaciones, los valores de cada persona y todos los errores. Estos umbrales son una referencia elegida para comparar, no una definición universal de usabilidad.

Las decisiones entre etapas se documentarán con sus mediciones. No se presentará una etapa no ejecutada como si estuviera medida. Una configuración que ya incumpla la referencia en un historial menor no garantiza fluidez hasta el máximo; se conservará de todas formas una comprobación de finalización al máximo con 20 usuarios.

[Plan y parámetros](plan.json).

<!-- resultados-inicio -->
## Resultados publicados

Se publica una prueba cuando termina. Los percentiles del primer turno y de las continuaciones se muestran separados. Las medidas parciales no se publican como resultados definitivos.

| Prueba | Memoria | Usuarios / límite | Historial inicial | Respuestas | Espera p95 primer turno | Espera p95 continuaciones | Velocidad p05 continuaciones | Caché máxima | Recálculos | Tiempo total | Continuaciones |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [20-usuarios-historial-8192-tres-turnos](memoria-40-20-usuarios-historial-8192-tres-turnos/README.md) | 40% | 20 / 32 | 8.192 | 60/60 | 151,3 s | 93,9 s | 3,14 tokens/s | 100,0% | 20 | 596,5 s | No cumple la referencia |

[Configuración y registros de esta campaña](configuracion-y-registros/metadata.json).
