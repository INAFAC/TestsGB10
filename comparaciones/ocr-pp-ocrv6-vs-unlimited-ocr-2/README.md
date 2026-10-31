# ¿Merece la pena cambiar de lector OCR? PP-OCRv6 frente a Unlimited OCR 2

[Volver al inicio](../../README.md)

## Resumen en 30 segundos

- **Qué se probó:** dos programas que **leen el texto de una factura escaneada o fotografiada** (esto se llama OCR). Uno es el que usamos hoy, **PP-OCRv6 con Docling**. El otro es un candidato, **Unlimited OCR 2**, de Baidu.
- **Cómo:** se les dieron 80 imágenes de 16 facturas inventadas, en cuatro calidades, y se contó cuántos datos importantes leyó bien cada uno. Como las facturas se inventaron, se sabe la respuesta correcta de cada dato.
- **Qué pasó:** con documentos que se ven bien, **los dos aciertan casi todo (99,7 % y 99,8 %)**. Con escaneos muy malos, ambos bajan al 93 %. Unlimited OCR 2 se inventa muchos menos números, pero falla casi lo mismo en los datos que importan.
- **Decisión:** **mantener el lector actual.** La mejora no justifica el cambio, el candidato necesita más memoria de la que sobra y puede equivocarse sin avisar.

Fecha de la prueba: 30 de octubre de 2026, en el GB10. Esta prueba mide **exactitud de lectura**. No tiene relación con las pruebas de memoria y conversaciones de Qwen del resto del repositorio.

## Para qué sirve cada pieza

En el sistema de documentos, un documento pasa por dos pasos:

1. **Un lector OCR convierte la imagen en texto y tablas.** Es lo que se compara aquí.
2. **Qwen** (el modelo de lenguaje) toma ese texto, clasifica el documento y extrae los datos (importes, NIF, fechas…).

Si el lector se equivoca en un número, Qwen ya no puede recuperarlo. Por eso importa que el lector sea exacto.

| | PP-OCRv6 con Docling (el actual) | Unlimited OCR 2 (el candidato) |
|---|---|---|
| Qué es | Combinación de un detector y un reconocedor de texto clásicos | Un modelo de IA de 3.000 millones de parámetros que «lee» la página entera |
| Dónde corre | En el procesador (CPU) | En la tarjeta gráfica (GPU) |
| Qué entrega | Texto con la posición de cada línea y una confianza | Texto y tablas, con la posición solo por bloques y sin confianza |

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
- Cada dato se clasifica así: **exacto** (bien leído), **cambiado** (se leyó otro valor), **ausente** (no aparece en la lectura) o **inventado** (el lector escribió una cifra que no existe en el documento).
- Los dos lectores recibieron solo imágenes, nunca el PDF original. Así se mide su lectura y no el texto que ya trae el PDF.
- La degradación es simulada: no hay sellos, sombras ni papel térmico. El generador de las facturas no se publica; aquí están los resultados y las condiciones.

## Resultados globales

| | PP-OCRv6 + Docling (actual) | Unlimited OCR 2 |
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

**La diferencia en los datos que importan es pequeña:** 86 fallos frente a 80, un 7 % menos. Unlimited OCR 2 lee mejor el texto corrido y casi no inventa, pero en importes, NIF o IBAN no mejora de forma apreciable.

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

Qué se aprende de esta tabla:

- **Si el documento se ve bien, da igual cuál se use:** 99,7 % y 99,8 %. La diferencia son 3 datos de 3.228.
- **Casi todos los fallos están en el escaneo malo:** el 88 % de los de PP-OCRv6 y el 91 % de los de Unlimited OCR 2.
- **La mayor ventaja de Unlimited OCR 2 es que casi no inventa cifras con escaneo malo:** 19 frente a 218. Un lector que inventa números llena el resultado de ruido.
- Las cifras vienen de facturas inventadas con respuesta conocida. No garantizan el mismo resultado con documentos reales.

Para ver cada imagen por separado: [resultados imagen a imagen](por-imagen.md).

## Por qué se decidió mantener el lector actual

Antes de ver los resultados se fijó una regla (ver [`configuracion.json`](configuracion.json)). Para cambiar de lector, el candidato debía cometer **al menos un 30 % menos de fallos** y que la mejora fuera estadísticamente fiable.

- **No se cumplió:** 7 % menos de fallos (80 frente a 86). Al repetir el cálculo muchas veces por factura (un método llamado *bootstrap*), el peor caso razonable de la diferencia sale en −48 fallos: no hay evidencia de mejora.
- **Un defecto de la regla, reconocido:** el umbral de cifras inventadas era fijo y no estaba calibrado contra el lector actual. Aplicándolo literalmente, el resultado formal fue «descartar Unlimited OCR 2», pero esa regla también habría descartado a PP-OCRv6, que inventa aún más cifras. No se reescribió la regla después de ver los datos. La decisión se apoya en el criterio principal (los fallos en datos críticos), que no depende de ese defecto.

## Otros hallazgos

Se vieron después de tener los datos, así que sirven como pistas y no como conclusiones firmes.

- **Los dos lectores fallan en sitios distintos.** En 150 datos con algún fallo, solo 8 fallan en los dos. Unas reglas sencillas podrían decidir cuál creer: que las líneas sumen el total, que los impuestos cuadren y que el IBAN y el NIF tengan un dígito de control válido. Una simulación indica que resolverían unos 123 de esos 150 (82 %). Es una estimación optimista que no se ha implementado ni confirmado con otras facturas.
- **Unlimited OCR 2 puede equivocarse sin avisar.** En una página de escaneo malo se saltó toda la columna de importes y devolvió el resultado como si estuviera completo. Comparar la suma de las líneas con el total lo habría detectado. En datos fiscales, un error que no se nota es el más peligroso.
- **Leer varias páginas de golpe empeora a Unlimited OCR 2:** inventó 51 cifras frente a 11 leyendo página a página.
- **No sustituye al lector actual donde hace falta ubicar cada dato en la página**, porque no da la posición de cada línea ni una confianza.
- **Memoria:** Qwen reserva casi toda la memoria del GB10. Quedan unos 7–11 GiB libres y Unlimited OCR 2 necesita unos 7 GiB, así que no cabe con margen sin reducir la memoria de Qwen.

## Límites de la prueba

- Son pocas facturas (16) y de cuatro estilos, todas inventadas. Con otras facturas, o con documentos reales, las cifras pueden cambiar.
- Las 20 páginas no son independientes, porque varias pertenecen a la misma factura. Por eso la fiabilidad estadística se calculó por factura.
- El estropeado de las imágenes es simulado y solo se hizo una pasada (ambos lectores dan siempre el mismo resultado).
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
| [`configuracion.json`](configuracion.json) | Versiones, parámetros, estropeado de las imágenes y regla de decisión |

Significado de los nombres que aparecen en los archivos `.json`:

| Nombre | Significa |
|---|---|
| `exactos`, `cambiados`, `ausentes`, `inventados` | Las cuatro clases de resultado de cada dato, tal como se explica arriba |
| `errores` | Fallos: `cambiados` + `ausentes` |
| `imagenes_con_inventados` | En cuántas imágenes apareció alguna cifra inventada |
| `cer_medio`, `wer_medio` | Proporción de caracteres y de palabras mal leídos. 0 es perfecto; cuanto más bajo, mejor |
| `bow_f1_medio` | Calidad del texto sin tener en cuenta el orden. 1 es perfecto |
| `tablas` | Filas y celdas de tabla encontradas y correctas |
| `celdas_incorrectas` | Celdas de tabla con un valor mal leído |
| `tiempo_mediano_s` | Segundos por página, mediana |
| `por_calidad` | Los mismos resultados desglosados en limpia, escaneo, escaneo_malo y foto |
