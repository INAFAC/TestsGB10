# Conversaciones recurrentes con varios usuarios

[Volver al modelo](../README.md)

**Se están realizando nuevas pruebas de conversaciones recurrentes con 10, 20 y 30 usuarios.**

El objetivo es saber cuánto espera cada persona al continuar su conversación, cómo cambia esa espera al crecer el historial y qué presupuesto de memoria conviene. La concurrencia del servidor **depende de cada prueba**; esta campaña comienza con un límite de 32 solicitudes activas para permitir hasta 30 usuarios sin imponer el antiguo límite de cuatro.

## Cómo interpretar los resultados

**Completar todas las respuestas y poder conversar con comodidad son dos cosas diferentes.** En cada prueba se indican ambas. Una espera de 90 segundos puede acabar en una respuesta correcta en longitud, pero esa espera sigue siendo parte de la experiencia de cada persona.

El porcentaje de memoria configurado es el presupuesto del servidor. El porcentaje de caché indica cuánto se ha ocupado del espacio disponible para los historiales: llegar al 100% de caché no significa que todo el GB10 esté al 100%. Las tablas detalladas muestran también la memoria del motor, la del sistema, las colas y los recálculos de historiales.

“Espera p95” significa que el 95% de las respuestas medidas empezó antes de ese tiempo; algunas tardaron más. “Velocidad p05” muestra la velocidad que alcanzó o superó el 95% de las respuestas. Las tablas por persona permiten comprobar los casos más lentos. Los tiempos incluyen la competencia con los demás usuarios de la prueba; no se extrapolan multiplicando una prueba individual.

## Recorrido de las pruebas

| Etapa | Usuarios | Historial inicial | Memoria | Turnos por persona |
|---|---:|---|---|---:|
| Seleccionar memoria | 20 | 8.192 y 32.768 tokens | 40%, 70%, 85% | 3 |
| Comparar usuarios | 10 y 30 | 8.192 y 32.768 tokens | La seleccionada con las mediciones | 3 |
| Comprobar crecimiento | 10, 20 y 30 | 65.536 tokens | La seleccionada | 2 |
| Comprobar historiales muy largos | 20; también los grupos que mantengan fluidez en la etapa anterior | 131.072 tokens | La seleccionada | 2 |
| Llegar al máximo | 20 | 260.864 tokens, después 261.632 | La seleccionada | 2 |
| Control con mensajes de chat | 20 | Aproximadamente 8.192 y 32.768 tokens | La seleccionada | 3 |
| Afinar el presupuesto si aporta una mejora | 20 | 8.192 y 32.768 tokens | 50%; después 60% si hace falta | 3 |

Cada respuesta solicita 512 tokens. Después de recibirla, cada usuario espera 30 segundos y añade 256 tokens de mensaje, conservando el historial y la respuesta real anterior. Los primeros mensajes de cada grupo se envían simultáneamente; los siguientes siguen el ritmo de cada usuario. Los historiales son sintéticos y permiten medir rendimiento, no calidad de las respuestas.

Para las etapas de crecimiento se conserva el historial medido en la etapa anterior, incluidas sus respuestas reales, y se añaden tokens sintéticos hasta el tamaño objetivo. Después se miden los nuevos turnos. Esto comprueba la carga de continuar con ese historial, pero no simula todos los turnos intermedios desde una conversación vacía ni una jornada completa de uso. El primer turno de cada etapa puede necesitar reconstruir información que ya no siga en la caché del servidor.

Como referencia orientativa de fluidez se usarán una espera al primer texto de hasta cinco segundos para el 95% de las solicitudes y una velocidad de al menos diez tokens/s para el 95%. Se mostrarán por separado el primer turno y las continuaciones, los valores de cada persona y todos los errores. Estos umbrales son una referencia elegida para comparar, no una definición universal de usabilidad.

Las decisiones entre etapas se documentarán con sus mediciones. No se presentará una etapa no ejecutada como si estuviera medida. Una configuración que ya incumpla la referencia en un historial menor no garantiza fluidez hasta el máximo; se conservará de todas formas una comprobación de finalización al máximo con 20 usuarios.

El control de chat usa mensajes ficticios en español y conserva las respuestas reales. Solicita hasta 512 tokens, permite terminar antes y distingue la primera salida del modelo de la primera respuesta visible. Se mide con razonamiento desactivado en ambos tamaños y con el modo predeterminado en 8.192 tokens. El tratamiento del razonamiento sigue la [documentación de vLLM](https://docs.vllm.ai/en/v0.22.0/features/reasoning_outputs/); se comprobará además el comportamiento de la versión instalada.

## Decisiones entre etapas

**Se añade el 50% a la comparación de memoria.** Con 20 usuarios y 8.192 tokens iniciales, el 70% redujo la espera p95 de las continuaciones de 93,9 a 7,6 segundos, y los recálculos de 20 a cero. La velocidad p05 pasó de 3,14 a 5,51 tokens/s. Es una mejora importante, aunque todavía no cumple la referencia elegida de espera y velocidad.

Con **32.768 tokens iniciales**, el cambio del 40% al 70% redujo la espera p95 de las continuaciones de 595,6 a 374,2 segundos, pero el tiempo del grupo apenas cambió: 35,3 frente a 35,0 minutos. La velocidad p05 durante las continuaciones bajó de 2,37 a 1,05 tokens/s. La respuesta empezó antes en parte de los casos, pero siguió tardando varios minutos en completarse. Esta carga de 20 usuarios no cumple la referencia con ninguno de esos dos presupuestos.

Se repetirán las dos cargas iniciales al 50% después de las comparaciones del 70% y el 85% y de comprobar el medidor de chat. Esto permitirá comprobar si parte de la memoria adicional se puede ahorrar. La decisión sobre probar el 60% se tomará con los resultados del 50%. Para considerar que conserva el rendimiento del 70%, ambas cargas deben completar todas las respuestas y mantener, en las continuaciones, la espera y el tiempo completo p95 dentro de un 15% de la referencia y la velocidad p05 por encima del 85% de la referencia. En la espera se admite al menos un segundo de diferencia. Es una tolerancia práctica para decidir la siguiente prueba, no una afirmación de equivalencia estadística.

[Plan y parámetros](plan.json).

<!-- resultados-inicio -->
## Configuraciones utilizadas

| Configuración | Presupuesto | Límite activo | Arrancó | Tiempo de arranque | Reserva de caché al arrancar |
|---|---:|---:|---|---:|---:|
| [seleccion-memoria-40](configuracion-y-registros/seleccion-memoria-40/arranque.log) | 40% | 32 | Sí | 376,0 s | 23,18 GiB |
| [seleccion-memoria-70](configuracion-y-registros/seleccion-memoria-70/arranque.log) | 70% | 32 | Sí | 376,2 s | 59,85 GiB |
| [seleccion-memoria-85](configuracion-y-registros/seleccion-memoria-85/arranque.log) | 85% | 32 | Sí | 401,3 s | 77,84 GiB |

La reserva de caché procede del registro de arranque. No equivale a memoria ocupada por conversaciones ni permite deducir por sí sola cuántas personas tendrán una respuesta fluida. El pico de ocupación de esa reserva se mide durante cada prueba.

## Resultados publicados

Se publica una prueba cuando termina. Los percentiles del primer turno y de las continuaciones se muestran separados. Las medidas parciales no se publican como resultados definitivos.

| Prueba | Memoria | Usuarios / límite | Historial inicial | Peticiones sin error | Espera p95 primer turno | Espera p95 continuaciones | Velocidad p05 continuaciones | Caché máxima | Recálculos | Tiempo total | Continuaciones |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [20-usuarios-historial-8192-tres-turnos](memoria-40-20-usuarios-historial-8192-tres-turnos/README.md) | 40% | 20 / 32 | 8.192 | 60/60 | 151,3 s | 93,9 s | 3,14 tokens/s | 100,0% | 20 | 596,5 s | No cumple la referencia |
| [20-usuarios-historial-32768-tres-turnos](memoria-40-20-usuarios-historial-32768-tres-turnos/README.md) | 40% | 20 / 32 | 32.768 | 60/60 | 554,8 s | 595,6 s | 2,37 tokens/s | 100,0% | 88 | 2.116,4 s | No cumple la referencia |
| [20-usuarios-historial-8192-tres-turnos](memoria-70-20-usuarios-historial-8192-tres-turnos/README.md) | 70% | 20 / 32 | 8.192 | 60/60 | 74,7 s | 7,6 s | 5,51 tokens/s | 42,9% | 0 | 391,2 s | No cumple la referencia |
| [20-usuarios-historial-32768-tres-turnos](memoria-70-20-usuarios-historial-32768-tres-turnos/README.md) | 70% | 20 / 32 | 32.768 | 60/60 | 494,0 s | 374,2 s | 1,05 tokens/s | 100,0% | 24 | 2.102,8 s | No cumple la referencia |
| [20-usuarios-historial-8192-tres-turnos](memoria-85-20-usuarios-historial-8192-tres-turnos/README.md) | 85% | 20 / 32 | 8.192 | 60/60 | 104,3 s | 12,7 s | 5,08 tokens/s | 33,1% | 0 | 440,8 s | No cumple la referencia |

[Configuración y registros de esta campaña](configuracion-y-registros/metadata.json).
