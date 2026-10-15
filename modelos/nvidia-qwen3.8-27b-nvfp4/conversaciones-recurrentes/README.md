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

Con **85% de memoria**, también terminaron las 60 respuestas de cada carga, pero no mejoró el rendimiento frente al 70% en estas ejecuciones. Con 8.192 tokens, el grupo pasó de 391,2 a 440,8 segundos; con 32.768, de 35,0 a 55,2 minutos. En la carga larga bajaron los recálculos de 24 a 9, mientras la espera p95 de continuaciones subió de 374,2 a 480,1 segundos y su tiempo completo p95 de 767,3 a 1.267,0 segundos. Reservar más memoria permitió reducir recálculos, pero no hizo esta conversación más rápida. Estos resultados no establecen la causa de la ralentización ni prueban qué ocurrirá con otros tamaños de historial.

El ajuste de memoria repite las dos cargas iniciales al 50%, después de las comparaciones del 70% y el 85% y de comprobar el medidor de chat. Sirve para comprobar si parte de la memoria adicional se puede ahorrar. La regla para decidir si hace falta probar el 60% se fijó antes de medir el 50%. Para considerar que conserva el rendimiento del 70%, ambas cargas deben completar todas las respuestas y mantener, en las continuaciones, la espera y el tiempo completo p95 dentro de un 15% de la referencia y la velocidad p05 por encima del 85% de la referencia. En la espera se admite al menos un segundo de diferencia. Es una tolerancia práctica para decidir la siguiente prueba, no una afirmación de equivalencia estadística.

**Se añade el 60% después de terminar las dos pruebas al 50%.** En la carga de 8.192 tokens, el 50% completó las 60 respuestas en 421,7 segundos, sin recálculos y con un pico de caché del 73,2%. La velocidad p05 de las continuaciones fue 5,44 tokens/s y su tiempo completo p95, 94,8 segundos: ambos cumplen la tolerancia frente al 70%. La espera p95 fue 9,60 segundos, por encima del límite de 8,77 segundos establecido por la regla. Esto activa la prueba del 60%; no significa que el 50% sea incapaz de atender estas conversaciones ni que una diferencia de unos dos segundos sea estable entre ejecuciones.

En la carga larga al **50%**, también terminaron las 60 respuestas, pero el grupo tardó 46,7 minutos frente a 35,0 al 70%. La espera p95 de las continuaciones fue de 11,0 minutos y su tiempo completo p95, de 17,2 minutos; hubo 85 recálculos frente a 24 al 70%. Esta carga incumplió además las tolerancias de espera y tiempo completo de la comparación. El 50% ahorra memoria y se acercó al 70% en la carga corta, pero no conservó su rendimiento con estos historiales largos.

**Se selecciona el 70% como referencia para las siguientes etapas.** Tuvo la menor espera p95 de continuaciones en las dos cargas: 7,63 segundos con 8.192 tokens y 374,22 segundos con 32.768. En la carga larga registró 24 recálculos frente a 39 al 60%. La elección prioriza la espera antes de empezar a responder. No convierte el 70% en un mínimo necesario ni demuestra que sea mejor en todas las medidas.

El **60% es una alternativa cercana que ahorra memoria**: las pruebas duraron 395,1 y 2.120,5 segundos, frente a 391,2 y 2.102,8 al 70%. En la carga larga su tiempo completo p95 fue incluso menor, 731,7 frente a 767,3 segundos, y su velocidad p05 mayor, 1,45 frente a 1,05 tokens/s; a cambio, la espera p95 fue 399,5 frente a 374,2 segundos. Estas ejecuciones no bastan para afirmar una ventaja estable en diferencias pequeñas. Ninguno de los presupuestos hizo fluida, según la referencia elegida, la carga de 20 usuarios con historiales largos.

Con el 70% se compararán 10 y 30 personas y se harán los controles de chat antes de ampliar los historiales. Los resultados de esas etapas no se darán por medidos con otros presupuestos.

[Plan y parámetros](plan.json).

<!-- resultados-inicio -->
## Cómo cambia la conversación con más personas

Comparación directa de las pruebas terminadas al **70% de memoria**. Cada persona envía tres mensajes, pide 512 tokens de respuesta por turno y espera 30 segundos antes de continuar. El 70% es el presupuesto de referencia elegido para estas pruebas, no un mínimo demostrado para cada número de personas.

| Historial inicial | Personas | Respuestas sin error | Espera p95 inicial | Espera p95 al continuar | Respuesta completa p95 al continuar | Velocidad p05 al continuar |
|---:|---:|---:|---:|---:|---:|---:|
| 8.192 | [10](memoria-70-10-usuarios-historial-8192-tres-turnos/README.md) | 30/30 | 50,4 s | 4,9 s | 68,0 s | 7,57 tokens/s |
| 8.192 | [20](memoria-70-20-usuarios-historial-8192-tres-turnos/README.md) | 60/60 | 74,7 s | 7,6 s | 93,3 s | 5,51 tokens/s |
| 8.192 | [30](memoria-70-30-usuarios-historial-8192-tres-turnos/README.md) | 90/90 | 168,1 s | 15,0 s | 122,3 s | 4,21 tokens/s |
| 32.768 | [10](memoria-70-10-usuarios-historial-32768-tres-turnos/README.md) | 30/30 | 265,1 s | 3,1 s | 99,6 s | 5,17 tokens/s |
| 32.768 | [20](memoria-70-20-usuarios-historial-32768-tres-turnos/README.md) | 60/60 | 494,0 s | 374,2 s | 767,3 s | 1,05 tokens/s |

Una prueba puede cumplir la referencia de espera y quedar por debajo de la referencia de velocidad. Las cifras de ambas columnas permiten valorar ese equilibrio; la etiqueta general de referencia no sustituye esos tiempos.

## Configuraciones utilizadas

| Configuración | Presupuesto | Límite activo | Servicio listo | Espera hasta estar listo | Reserva de caché registrada |
|---|---:|---:|---|---:|---:|
| [Seleccion memoria 40](configuracion-y-registros/seleccion-memoria-40/arranque.log) | 40% | 32 | Sí | 376,0 s | 23,18 GiB |
| [Seleccion memoria 70](configuracion-y-registros/seleccion-memoria-70/arranque.log) | 70% | 32 | Sí | 376,2 s | 59,85 GiB |
| [Seleccion memoria 85](configuracion-y-registros/seleccion-memoria-85/arranque.log) | 85% | 32 | Sí | 401,3 s | 77,84 GiB |
| [Ajuste memoria 50](configuracion-y-registros/ajuste-memoria-50/arranque.log) | 50% | 32 | Sí | 386,2 s | 35,30 GiB |
| [Ajuste memoria 60](configuracion-y-registros/ajuste-memoria-60/arranque.log) | 60% | 32 | Sí | 381,1 s | 47,47 GiB |
| [Comparacion usuarios y chat memoria 70](configuracion-y-registros/comparacion-usuarios-y-chat-memoria-70/arranque.log) | 70% | 32 | Sí | 376,1 s | 59,68 GiB |

La reserva de caché procede del registro de arranque. No equivale a memoria ocupada por conversaciones ni permite deducir por sí sola cuántas personas tendrán una respuesta fluida. El pico de ocupación de esa reserva se mide durante cada prueba.

La espera hasta estar listo se mide después de aplicar la configuración. Si la siguiente etapa conserva los mismos parámetros, Docker puede reutilizar el contenedor y esa espera será casi cero; no significa que el modelo se haya cargado desde cero en ese tiempo. La espera al primer texto de cada conversación se mide por separado.

## Resultados publicados

Se publica una prueba cuando termina. Los percentiles del primer turno y de las continuaciones se muestran separados. Las medidas parciales no se publican como resultados definitivos.

| Prueba | Memoria | Usuarios / límite | Historial inicial | Peticiones sin error | Espera p95 primer turno | Espera p95 continuaciones | Velocidad p05 continuaciones | Caché máxima | Recálculos | Tiempo total | Continuaciones |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Conversación de 3 turnos por persona](memoria-40-20-usuarios-historial-8192-tres-turnos/README.md) | 40% | 20 / 32 | 8.192 | 60/60 | 151,3 s | 93,9 s | 3,14 tokens/s | 100,0% | 20 | 596,5 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-40-20-usuarios-historial-32768-tres-turnos/README.md) | 40% | 20 / 32 | 32.768 | 60/60 | 554,8 s | 595,6 s | 2,37 tokens/s | 100,0% | 88 | 2.116,4 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-70-20-usuarios-historial-8192-tres-turnos/README.md) | 70% | 20 / 32 | 8.192 | 60/60 | 74,7 s | 7,6 s | 5,51 tokens/s | 42,9% | 0 | 391,2 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-70-20-usuarios-historial-32768-tres-turnos/README.md) | 70% | 20 / 32 | 32.768 | 60/60 | 494,0 s | 374,2 s | 1,05 tokens/s | 100,0% | 24 | 2.102,8 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-85-20-usuarios-historial-8192-tres-turnos/README.md) | 85% | 20 / 32 | 8.192 | 60/60 | 104,3 s | 12,7 s | 5,08 tokens/s | 33,1% | 0 | 440,8 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-85-20-usuarios-historial-32768-tres-turnos/README.md) | 85% | 20 / 32 | 32.768 | 60/60 | 793,4 s | 480,1 s | 0,53 tokens/s | 100,0% | 9 | 3.312,5 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-50-20-usuarios-historial-8192-tres-turnos/README.md) | 50% | 20 / 32 | 8.192 | 60/60 | 102,1 s | 9,6 s | 5,44 tokens/s | 73,2% | 0 | 421,7 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-50-20-usuarios-historial-32768-tres-turnos/README.md) | 50% | 20 / 32 | 32.768 | 60/60 | 716,5 s | 657,2 s | 1,22 tokens/s | 100,0% | 85 | 2.805,0 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-60-20-usuarios-historial-8192-tres-turnos/README.md) | 60% | 20 / 32 | 8.192 | 60/60 | 75,8 s | 9,8 s | 5,42 tokens/s | 54,2% | 0 | 395,1 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-60-20-usuarios-historial-32768-tres-turnos/README.md) | 60% | 20 / 32 | 32.768 | 60/60 | 500,2 s | 399,5 s | 1,45 tokens/s | 100,0% | 39 | 2.120,5 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-70-10-usuarios-historial-8192-tres-turnos/README.md) | 70% | 10 / 32 | 8.192 | 30/30 | 50,4 s | 4,9 s | 7,57 tokens/s | 21,7% | 0 | 300,6 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-70-30-usuarios-historial-8192-tres-turnos/README.md) | 70% | 30 / 32 | 8.192 | 90/90 | 168,1 s | 15,0 s | 4,21 tokens/s | 63,9% | 0 | 551,5 s | No cumple la referencia |
| [Conversación de 3 turnos por persona](memoria-70-10-usuarios-historial-32768-tres-turnos/README.md) | 70% | 10 / 32 | 32.768 | 30/30 | 265,1 s | 3,1 s | 5,17 tokens/s | 82,9% | 0 | 599,0 s | No cumple la referencia |

## Comprobaciones del medidor de chat

Estas pruebas pequeñas comprueban la captura de tiempos y la conservación de los mensajes. Sus respuestas tienen un límite de salida reducido; no se utilizan para decidir la memoria necesaria ni la fluidez del uso normal. Se conservan también sus errores y los casos que agotan ese límite.

| Comprobación | Memoria | Usuarios | Turnos | Límite de salida | Peticiones sin error | Con texto visible | Terminadas por el modelo | Tiempo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [Medidor: sin razonamiento](memoria-85-chat-comprobacion-medidor-sin-razonamiento/README.md) | 85% | 2 | 2 | 128 | 4/4 | 4/4 | 0/4 | 23,5 s |
| [Medidor: modo predeterminado](memoria-85-chat-comprobacion-medidor-predeterminado/README.md) | 85% | 2 | 2 | 128 | 4/4 | 0/4 | 1/4 | 23,1 s |

[Configuración y registros de esta campaña](configuracion-y-registros/metadata.json).
