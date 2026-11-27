# Lectura de facturas escaneadas con PP-OCRv6 y Unlimited OCR 2

[Volver al inicio](../../README.md)

El 30 de octubre de 2026 se comparó la lectura de **80 imágenes de facturas sintéticas** en el GB10. PP-OCRv6 leyó exactamente 4.218 de los 4.304 valores de referencia y Unlimited OCR 2, 4.224. Ambos produjeron cifras ausentes del original en 19 imágenes. El número total de esas cifras fue de 227 y 27, respectivamente.

| Lector | Dispositivo en la prueba | Salida evaluada |
|---|---|---|
| PP-OCRv6 con Docling | CPU | Texto, posición y confianza por línea |
| Unlimited OCR 2 | GPU | Texto y tablas con posiciones por bloque |

## Cómo se hizo la prueba

- **16 facturas españolas inventadas** (20 páginas) en cuatro estilos: clásica con tabla con bordes, sin bordes, ticket y servicios profesionales con retención.
- **Cada página en cuatro calidades**, lo que da 80 imágenes:

| Calidad | Qué representa |
|---|---|
| Limpia | El PDF tal cual, sin estropear |
| Escaneo | Escáner normal: ligeramente torcido y borroso |
| Foto | Hecha con un móvil: perspectiva, luz irregular, ruido |
| Escaneo malo | Escáner muy malo: muy comprimido, torcido, tinta desvaída, manchas |

- Se evalúan **4.304 datos críticos**: importes, cantidades, precios, porcentajes, fechas, NIF/CIF, número de factura e IBAN.
- Cada valor de referencia se cuenta como **exacto**, **cambiado** o **ausente**. Se cuentan aparte las **cifras inventadas** que aparecen en la lectura y carecen de correspondencia en la referencia.
- Los dos lectores recibieron solo imágenes, nunca el PDF original. Así se mide su lectura y no el texto que ya trae el PDF.
- La degradación es simulada: no hay sellos, sombras ni papel térmico. El generador de las facturas no se publica; aquí están los resultados y las condiciones.

## Resultados globales

| | PP-OCRv6 + Docling | Unlimited OCR 2 |
|---|---:|---:|
| Datos leídos exactamente (de 4.304) | 4.218 (**98,00 %**) | 4.224 (**98,14 %**) |
| Cambiados | 36 | 24 |
| Ausentes | 50 | 56 |
| **Fallos en total** (cambiados + ausentes) | **86** | **80** |
| Cifras inventadas | 227 | 27 |
| Imágenes con alguna cifra inventada | 19 de 80 | 19 de 80 |
| Calidad del texto en general (1 = perfecto) | 0,915 | 0,980 |
| Tiempo por página (mediana) | 11,7 s | 16,3 s |
| Memoria | 3,9 GiB de RAM | unos 7 GiB de GPU |

PP-OCRv6 registró 86 valores cambiados o ausentes y Unlimited OCR 2 registró 80. La diferencia observada fue de seis fallos. El intervalo del 95 % para esa diferencia abarcó de −48 a +49 fallos, calculado con 2.000 remuestreos por factura (semilla 0). Ambas direcciones son compatibles con esta muestra.

## Exactitud según la calidad del documento

Hay 1.076 datos críticos por calidad. Una exactitud del 99,9 % significa que de cada 1.000 datos, 999 salen bien.

| Calidad | Lector | Exactitud | Fallos | Cifras inventadas | Calidad del texto |
|---|---|---:|---:|---:|---:|
| Limpia | PP-OCRv6 | 99,91 % | 1 | 3 | 0,989 |
| | Unlimited OCR 2 | 99,72 % | 3 | 3 | 0,995 |
| Escaneo | PP-OCRv6 | 99,63 % | 4 | 5 | 0,961 |
| | Unlimited OCR 2 | 99,91 % | 1 | 1 | 1,000 |
| Foto | PP-OCRv6 | 99,54 % | 5 | 1 | 0,967 |
| | Unlimited OCR 2 | 99,72 % | 3 | 4 | 0,997 |
| **Limpia + escaneo + foto** (documentos que se ven bien) | PP-OCRv6 | **99,69 %** | 10 | 9 | |
| | Unlimited OCR 2 | **99,78 %** | 7 | 8 | |
| Escaneo malo | PP-OCRv6 | 92,94 % | 76 | 218 | 0,744 |
| | Unlimited OCR 2 | 93,22 % | 73 | 19 | 0,929 |

En las variantes limpia, escaneo y foto hubo 10 y 7 fallos en 3.228 valores. La mayor parte de los fallos se concentró en el escaneo malo, con 76 para PP-OCRv6 y 73 para Unlimited OCR 2. En esa variante los lectores añadieron 218 y 19 cifras ausentes del original, respectivamente. [Resultados por imagen](por-imagen.md)

## Otras observaciones

En 78 valores falló solo PP-OCRv6, en 72 solo Unlimited OCR 2 y en ocho fallaron ambos.

- En una página con escaneo malo, Unlimited OCR 2 devolvió una tabla sin la columna de importes e indicó que había terminado la lectura.
- En el ensayo multipágina con Unlimited OCR 2 se contaron 51 cifras añadidas al leer varias páginas juntas y 11 al leer esas mismas páginas por separado.

## Límites de la prueba

- Son pocas facturas (16) y de cuatro estilos, todas inventadas. Con otras facturas, o con documentos reales, las cifras pueden cambiar.
- Las 20 páginas no son independientes, porque varias pertenecen a la misma factura. Por eso la fiabilidad estadística se calculó por factura.
- La degradación de las imágenes fue simulada. Se hizo una pasada por lector.
- Un dato cuenta como bien leído si aparece en cualquier punto de la lectura, aunque esté en el sitio equivocado. Eso favorece a ambos lectores.
- Unlimited OCR 2 se probó con una sola forma de ejecutarlo.
- No se midió el paso siguiente, en el que Qwen extrae los datos a partir de lo leído.
- Puede haber ventaja si algún lector se entrenó con facturas parecidas.

## Archivos y cómo leerlos

| Archivo | Para qué sirve |
|---|---|
| [`por-imagen.md`](por-imagen.md) | Tabla legible con el resultado de cada una de las 80 imágenes |
| [`mediciones.json`](mediciones.json) | Todos los resultados globales y por calidad, para procesarlos con un programa |
| [`por-imagen.json`](por-imagen.json) | Lo mismo que `por-imagen.md` con más detalle por tipo de dato |
| [`parametros.json`](parametros.json) | Versiones de los lectores, parámetros y degradaciones aplicadas a las imágenes |

Significado de los nombres que aparecen en los archivos `.json`:

| Nombre | Significa |
|---|---|
| `exactos`, `cambiados`, `ausentes`, `inventados` | Los tres primeros suman los valores de referencia. El último cuenta las cifras añadidas por el lector |
| `errores` | Fallos: `cambiados` + `ausentes` |
| `imagenes_con_inventados` | En cuántas imágenes apareció alguna cifra inventada |
| `cer_medio`, `wer_medio` | Proporción de caracteres y de palabras mal leídos. 0 es perfecto; cuanto más bajo, mejor |
| `bow_f1_medio` | Calidad del texto sin tener en cuenta el orden. 1 es perfecto |
| `tablas` | Filas y celdas de tabla encontradas y correctas |
| `celdas_incorrectas` | Celdas de tabla con un valor mal leído |
| `tiempo_mediano_s` | Segundos por página, mediana |
| `por_calidad` | Los mismos resultados desglosados en limpia, escaneo, escaneo_malo y foto |
