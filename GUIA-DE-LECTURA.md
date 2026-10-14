# Cómo leer las pruebas

[Volver al inicio](README.md)

## Lo primero: ¿terminó y llegó al máximo?

Cada prueba responde dos preguntas distintas:

- **¿Terminó?** Recibió todos los tokens de respuesta que se habían pedido. Por ejemplo, si se pidieron 512, debe entregar 512.
- **¿Llegó al máximo del modelo?** La suma real de entrada y respuesta alcanzó el máximo de tokens permitido por el modelo, y la respuesta se entregó completa.

Un token es una pequeña unidad de texto; no equivale necesariamente a una palabra. La **entrada** representa el historial que debe leer el modelo. La **respuesta** es lo que genera después.

Para este Qwen, el máximo es **262.144 tokens por conversación, contando entrada y respuesta**. Una prueba con 262.016 de entrada y 128 de respuesta llega exactamente a ese máximo. No significa que haya generado una respuesta nueva de 262.144 tokens.

Al reducir la memoria puede ser necesario reducir también el límite configurado. Llegar a 131.072 tokens con ese límite reducido no demuestra que se pueda llegar al máximo del modelo. El informe distingue ambos casos.

Estas pruebas fuerzan una longitud de respuesta para poder comparar el rendimiento. “Terminó” comprueba que se entregó esa longitud; no evalúa si el contenido de una respuesta real quedaría bien concluido.

## Conversaciones enviadas y conversaciones a la vez

“8 conversaciones, hasta 4 a la vez” significa que se envía un grupo de ocho y el cliente mantiene como máximo cuatro peticiones pendientes simultáneamente.

El servidor tiene además un **límite impuesto por nosotros** de solicitudes activas, configurado con `--max-num-seqs`. Las primeras baterías se ejecutaron con **cuatro**. Ver cuatro activas en ellas no demuestra que ese sea el máximo del GB10. Las pruebas posteriores con límites mayores se identifican en su propia fila. Enviar ocho a un servidor limitado a cuatro puede crear cola aunque sobre memoria.

- **Activas en el motor:** solicitudes que se están leyendo o generando.
- **Respuestas solapadas:** respuestas cuyos intervalos desde el primer texto hasta el final coinciden.
- **Cola:** solicitudes que esperan su turno. Una espera breve al empezar a leer varios historiales no demuestra por sí sola falta de memoria.
- **Recálculos:** el motor tuvo que desalojar trabajo y repetirlo por falta de espacio en caché. La conversación puede terminar, pero tardar más.

Que todas terminen no implica que todas hayan respondido a la vez. Tampoco implica que el motor genere un token para cada una en cada paso.

## Los porcentajes de memoria

| Medida | Qué significa |
|---|---|
| Memoria asignada | Presupuesto configurado para el motor con `--gpu-memory-utilization`. |
| Motor / GB10 | Pico de memoria observado del proceso del modelo, dividido entre la memoria total del equipo. |
| Sistema / GB10 | Pico usado por el equipo completo, incluyendo el modelo y los demás procesos. |
| Caché ocupada | Cuánto se ha ocupado de la reserva que guarda información de los historiales. No es un porcentaje de toda la RAM del equipo. |

El motor puede mantener memoria reservada aunque la caché esté casi vacía. La caché también puede conservar historiales anteriores. Un porcentaje alto, aislado, no basta para concluir que la prueba fallará: hay que mirar si terminó, si hubo colas y si repitió trabajo.

## Los tiempos y velocidades

| Medida | Qué permite saber |
|---|---|
| Espera hasta primer texto | Cuánto espera esa conversación antes de empezar a recibir respuesta. Incluye la cola. |
| Tiempo de respuesta completo | Cuánto tarda esa conversación en recibir toda la respuesta pedida. |
| Tiempo total de la prueba | Cuánto tarda el grupo completo. No incluye cargar el modelo, salvo en las pruebas de arranque. |
| Suma de tiempos individuales | Suma de los tiempos de todas las conversaciones. Puede superar el tiempo total porque se solapan. |
| Tokens/s durante la respuesta | Velocidad desde el primer texto recibido hasta el final. |
| Tokens/s incluyendo espera | Tokens de respuesta divididos entre todo el tiempo individual, incluida la espera. |
| Tokens/s totales | Todos los tokens de respuesta completados, divididos entre la duración del grupo. No se obtiene sumando velocidades individuales. |

La velocidad durante la respuesta se calcula como `(tokens recibidos − 1) / (tiempo completo − espera al primer texto)`. Son medidas desde el cliente, no contadores internos de pasos de la GPU.

Las medias individuales se calculan sobre las conversaciones que terminaron correctamente. Si una prueba sigue en curso o tiene fallos, hay que leerlas junto al número de conversaciones completadas. Los tokens/s del grupo cuentan los tokens de las respuestas completadas y todo el tiempo transcurrido del grupo; una cifra parcial no es su rendimiento final.

## Cómo se hicieron

Las pruebas se ejecutan directamente contra la API del modelo, sin Open WebUI. Usan entradas sintéticas de tamaño conocido, sin conversaciones personales. Se pide una salida fija con `ignore_eos=true` y temperatura cero para comparar longitudes iguales.

Las pruebas de historial nuevo usan entradas independientes. Las de reutilización repiten el mismo historial y después lo amplían. Un historial que permanezca en caché puede empezar a responder mucho antes.

Se mide la caché aproximadamente cada segundo y la memoria/temperatura GPU aproximadamente cada cinco segundos. Un pico más breve puede pasar desapercibido. Los tiempos individuales empiezan al enviar cada petición; el tiempo del grupo también incluye preparación y medición.

Los arranques fallidos, rechazos e interrupciones se conservan como resultados. Una solicitud sin entrar en ejecución puede detenerse a los 90 segundos; los ensayos de la matriz tienen un límite de 1.500 segundos. No completar dentro de ese criterio no demuestra imposibilidad absoluta.

“No medido” significa que ese dato no se recogió; no significa que falte subir un archivo. Las primeras pruebas tenían menos mediciones y se conservan en el desplegable **Histórico: primeras mediciones con menos datos**. Las tablas principales muestran las mediciones detalladas. No se rellenan huecos con estimaciones.

“No aplica” significa que esa medida no corresponde al tipo de prueba: por ejemplo, un arranque no tiene tokens por segundo de respuesta. “No se intentó” en la columna del máximo significa que se eligió una conversación más corta, no que la prueba haya fallado.

“Pendiente” significa que la prueba sigue en curso y todavía no existe esa medida; por ejemplo, aún no ha terminado ninguna respuesta para calcular su tiempo medio.

Los resultados describen las cargas y la configuración probadas. No evalúan la calidad del texto ni estabilidad durante días. El mínimo probado que funciona no tiene por qué ser el mínimo exacto posible.

## Dónde están los datos

Cada prueba reúne su explicación, `mediciones.json`, `configuracion.json` y sus registros en una sola carpeta. Los archivos de configuración del equipo conservan la imagen, los parámetros, el estado de los reinicios y un inventario que permite comprobar que los originales no se han alterado.
