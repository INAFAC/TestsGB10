# ¿Cuánto tarda procesar un documento en la nube y en el GB10?

[Volver al inicio](../../README.md)

## Resumen en 30 segundos

El 9 de noviembre de 2026, un PDF escaneado limpio de 50 páginas tardó **3 min 12 s en la nube y 14 min 27 s en el GB10**. La diferencia también dependió del formato. Un Word corto tardó menos de dos segundos en el GB10. En un lote mixto de documentos cortos, enviar ocho a la vez aceleró el servicio en la nube. En el GB10 de esa prueba, un solo trabajo podía ejecutarse a la vez y los demás esperaban en cola.

## Cómo se midió

Se generaron 168 ficheros sintéticos con contenido nuevo. Para cada combinación de formato, longitud y calidad se midió una copia en la nube (Azure Document Intelligence y Claude) y tres en el GB10 (Docling, PP-OCRv6 en CPU y Qwen). El cliente consultó el estado cada dos segundos. Los tiempos incluyen envío, espera y procesamiento hasta observar el resultado. En Word y Excel la longitud cuenta las páginas de contenido de origen, que pueden ocupar un número distinto de páginas impresas.

| Formato y calidad | Páginas de origen | Nube, segundos | GB10, mediana en segundos | GB10, mínimo–máximo |
|---|---:|---:|---:|---:|
| PDF escaneado limpio | 1 | 14,7 | 27,9 | 15,2–41,2 |
| PDF escaneado limpio | 5 | 33,1 | 95,4 | 90,7–96,1 |
| PDF escaneado limpio | 20 | 88,8 | 370,6 | 358,5–417,9 |
| PDF escaneado limpio | 50 | 192,3 | 867,2 | 831,3–902,7 |
| PDF con texto nativo | 50 | 196,1 | 513,5 | 408,0–526,4 |
| Word | 1 | 6,2 | 1,9 | 1,9–1,9 |
| Excel | 1 | 3,8 | 10,7 | 10,6–10,7 |

## Qué pasó al enviar varios a la vez

Cada fila corresponde a un lote de 24 ficheros y 33 páginas. Se mantuvo el reparto de formatos y longitudes, con contenido nuevo para evitar la caché. Los 24 ficheros de cada lote terminaron. La latencia es la espera de un fichero desde que se envía. El p95 indica el tiempo dentro del que terminó el 95 % según el medidor.

| Servicio | Envíos simultáneos | Ficheros/h | Latencia mediana (s) | Latencia p95 (s) |
|---|---:|---:|---:|---:|
| Nube | 1 | 155,9 | 21,6 | 45,8 |
| Nube | 2 | 284,4 | 21,8 | 43,3 |
| Nube | 4 | 537,0 | 21,7 | 56,6 |
| Nube | 8 | 961,0 | 23,0 | 41,7 |
| GB10 | 1 | 126,3 | 19,3 | 113,3 |
| GB10 | 2 | 117,1 | 45,6 | 154,3 |
| GB10 | 4 | 122,9 | 89,9 | 221,4 |
| GB10 | 8 | 115,8 | 275,2 | 376,1 |

En el GB10, con ocho envíos, la espera mediana en la cola del servidor fue de 237,6 s y el procesamiento mediano duró 20,5 s. La [prueba posterior de concurrencia](../concurrencia-documental-gb10/README.md) mide qué cambió al habilitar varios trabajos.

## Límites de la comparación

Se hizo una serie por nivel de carga. El límite interno de la nube era desconocido y la carga externa no se controló. Los ficheros por hora expresan el ritmo medido durante el lote. El ensayo no evaluó costes ni exactitud documental. En la serie individual hubo tres llamadas al modelo local que agotaron su plazo en PDF de 50 páginas y tres documentos con error de segmentación, aunque los trabajos constaban como terminados. Dos entradas del arranque del cliente quedaron sin cronometrar y se sustituyeron por entradas nuevas equivalentes.

[Mediciones por formato, longitud y concurrencia](mediciones.json) · [Parámetros del ensayo](parametros.json) · [Comparación de exactitud](../documentos-azure-claude-vs-pp-ocrv6-qwen/README.md)
