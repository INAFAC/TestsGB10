# ¿Cuánto se acerca el servicio local del GB10 al de la nube? Escritos y facturas escaneados

[Volver al inicio](../../README.md)

## Resumen en 30 segundos

- **Qué se probó:** dos servicios completos que convierten un documento escaneado en texto y, si es una factura, en datos (número, NIF, importes, IVA…). Uno funciona **en la nube**: Azure AI Document Intelligence lee la imagen y Claude interpreta el contenido. El otro funciona **en el GB10, sin que los documentos salgan del equipo**: Docling con PP-OCRv6 lee la imagen y Qwen interpreta el contenido.
- **Cómo:** se les dieron 114 PDF de 19 documentos inventados (15 escritos y 4 facturas), cada uno en seis calidades, desde una imagen limpia hasta un fax. Como los documentos se inventaron, se sabe cuál es cada palabra y cada dato correcto.
- **Qué pasó:** la nube leyó bien el **97,9 %** de las palabras y el servicio local, el **89,9 %**. La prueba destapó dos fallos del servicio local. Se corrigieron y se repitió la prueba con las mismas imágenes: el local sube al **93,1 %** de las palabras y, en los datos de las facturas, del **68,1 % al 83,5 %**, al nivel de la nube (**82,2 %**).
- **Conclusión:** la nube sigue leyendo mejor el texto, sobre todo las cifras de los escaneos malos y los faxes. En los datos de las facturas, el servicio local corregido ya la iguala en conjunto en esta prueba. Con documentos reales las cifras pueden ser otras.

Fechas de la prueba: del 3 al 6 de noviembre de 2026. Mide la **exactitud del servicio completo**, desde la imagen hasta el texto y los datos. No tiene relación con las pruebas de memoria y conversaciones de Qwen del resto del repositorio. La [comparación de lectores OCR](../ocr-pp-ocrv6-vs-unlimited-ocr-2/README.md) midió solo el primer paso, con otras facturas.

## Para qué sirve cada pieza

Los dos servicios trabajan en dos pasos:

1. **Un lector OCR convierte la imagen en texto y tablas.** Aquí se mide con el texto que devuelve cada servicio.
2. **Un modelo de lenguaje clasifica el documento y extrae sus datos.** Aquí se mide con los datos de las facturas.

| | Servicio en la nube | Servicio local (GB10) |
|---|---|---|
| Lee la imagen | Azure AI Document Intelligence, modelo de diseño (`prebuilt-layout`) en alta resolución | Docling con PP-OCRv6 medium (RapidOCR), en el procesador |
| Interpreta | Claude, de Anthropic. Puede volver a mirar la imagen cuando duda | Qwen3.8 Flash Next en FP4, en la tarjeta gráfica del GB10 |
| Dónde se procesan los documentos | En servidores externos | Dentro del GB10 |

Se midieron cuatro series con las mismas imágenes:

| Serie | Fecha | Qué cambia |
|---|---|---|
| **Nube** | 3 de noviembre | El servicio en la nube tal como funcionaba ese día |
| **Local inicial** | 3 de noviembre | El servicio local tal como funcionaba ese día |
| **Local + giro corregido** | 5 de noviembre | Corrige el fallo que hacía perder líneas enteras de texto |
| **Local + IVA verificado** | 6 de noviembre | Además, conserva el IVA que cuadra con los importes impresos y no descarta facturas de una sola página |

Las dos correcciones se explican en [los dos fallos encontrados](#los-dos-fallos-encontrados-y-corregidos).

## Cómo se hizo la prueba

- **19 documentos españoles inventados:**
  - 15 escritos de cinco tipos: cartas, alegaciones ante Hacienda, contratos de arrendamiento, actas de junta y avisos bancarios. Cada tipo aparece en tres tamaños de letra, de 7,5 a 12,5 puntos.
  - 4 facturas: clásica con tabla con bordes, sin bordes, ticket y servicios profesionales con retención de IRPF.
- **Cada documento en seis calidades**, lo que da 114 PDF y 138 páginas:

| Calidad | Qué representa | Cómo se estropeó la imagen |
|---|---|---|
| Limpia | El documento tal cual | 300 dpi, sin pérdida |
| Escaneo | Escáner normal | 200 dpi en gris, JPEG 75, giro de 0,3 a 1°, desenfoque y ruido leves |
| Fotocopia | Copia de oficina | 200 dpi en gris, JPEG 70, giro de 0,2 a 0,8°, contraste duro y tres rayas de tóner |
| Foto | Hecha con un móvil | 200 dpi en color, JPEG 60, perspectiva de hasta un 3 %, luz irregular y ruido |
| Escaneo malo | Escáner muy malo | 150 dpi en gris, JPEG 35, giro de 1,5 a 3°, tinta desvaída al 60 %, ruido fuerte y motas |
| Fax | Fax recibido | 100 dpi, solo blanco y negro, giro de 0,4 a 1,2° y ruido |

- **Los PDF solo llevan la imagen**, sin texto incrustado, así que cada servicio tiene que leerla. Los dos servicios recibieron los mismos archivos, con sus opciones predeterminadas y dos documentos a la vez. La nube se midió en su entorno real, con su carga habitual.
- **Qué se cuenta:**
  - **34.854 palabras por serie** (5.809 por calidad). Una palabra cuenta como bien leída solo si aparece en su sitio. Aparte, se mide cuántas aparecen en cualquier orden.
  - **2.844 apariciones de datos** (474 por calidad): fechas, importes, NIF, IBAN, porcentajes, referencias, teléfonos…
  - **738 comprobaciones de los datos extraídos** de las 24 facturas: número, fecha, NIF, base, IVA, total, retención y líneas.
- **Las mismas imágenes en las cuatro series.** Para repetir la prueba sin reutilizar resultados guardados, cada repetición usó copias de los PDF con un metadato distinto. Sus imágenes son idénticas byte a byte.
- **Todos los envíos terminaron:** 456 de 456.
- **Las comparaciones son pareadas:** cada serie se compara con otra sobre las mismas imágenes.
- El generador de los documentos y el programa de puntuación no se publican. Aquí están los resultados y las condiciones.

## Resultados globales

|  | Nube | Local inicial | Local + giro corregido | Local + IVA verificado |
|---|---:|---:|---:|---:|
| Palabras en su sitio (de 34.854) | 97,90 % | 89,89 % | 93,07 % | 93,07 % |
| Sin contar tildes ni mayúsculas | 98,60 % | 90,45 % | 93,64 % | 93,64 % |
| Palabras encontradas en cualquier orden | 97,94 % | 92,00 % | 95,36 % | 95,36 % |
| Números (palabras con alguna cifra) | 95,39 % | 81,84 % | 83,41 % | 83,41 % |
| Palabras con tilde o eñe | 91,46 % | 87,14 % | 89,34 % | 89,34 % |
| Palabras perdidas | 42 | 2.078 | 1.038 | 1.038 |
| Palabras cambiadas por otra | 445 | 1.252 | 1.179 | 1.179 |
| Errores solo de tilde o mayúscula | 246 | 193 | 199 | 199 |
| Cifras inventadas (documentos afectados) | 184 (48) | 309 (57) | 306 (55) | 306 (55) |
| Error por carácter, aproximado (0 es perfecto) | 0,79 % | 9,37 % | 6,54 % | 6,54 % |
| Documentos que piden revisión humana | 35 | 114 | 114 | 114 |
| Tiempo por documento (mediana) | 20,7 s | 29,4 s | 29,2 s | 29,4 s |
| **Datos de factura correctos** (de 738) | **82,25 %** | **68,08 %**¹ | **68,08 %**¹ | **83,47 %** |

¹ Sobre 730 comprobaciones: en las dos facturas que estas series descartaban, el programa de puntuación no cuenta los datos de impuestos. Contándolos como ausentes, el resultado sería del 67,34 %.

La cuarta serie da exactamente la misma lectura que la tercera, documento a documento. Solo cambia la extracción de datos de las facturas.

- **La nube gana en el texto con claridad.** Antes de las correcciones acertaba 8,0 puntos más y ganaba en 112 de los 114 documentos. Después, la diferencia baja a 4,8 puntos y la nube gana en 110. [Ver si las diferencias son fiables](#las-diferencias-son-fiables).
- **La corrección del giro reduce a la mitad las palabras perdidas** del servicio local: de 2.078 a 1.038.
- **El servicio local inventa más cifras** (306 frente a 184) y pide revisión humana en todos los documentos.

## Según la calidad del documento

Hay 5.809 palabras por calidad. Los números son palabras con alguna cifra: importes, fechas, NIF, IBAN… **Local corregido** reúne la tercera y la cuarta serie, que leen igual.

| Calidad | Serie | Palabras en su sitio | Números | Palabras perdidas | Cifras inventadas |
|---|---|---:|---:|---:|---:|
| Limpia | Nube | 99,52 % | 99,28 % | 11 | 5 |
|  | Local inicial | 91,08 % | 87,84 % | 447 | 9 |
|  | Local corregido | 97,45 % | 91,61 % | 108 | 7 |
| Escaneo | Nube | 99,81 % | 99,57 % | 1 | 3 |
|  | Local inicial | 94,13 % | 85,67 % | 260 | 15 |
|  | Local corregido | 96,18 % | 86,98 % | 150 | 15 |
| Fotocopia | Nube | 99,79 % | 99,42 % | 1 | 5 |
|  | Local inicial | 94,06 % | 88,71 % | 265 | 13 |
|  | Local corregido | 96,83 % | 89,87 % | 118 | 12 |
| Foto | Nube | 99,85 % | 99,57 % | 2 | 3 |
|  | Local inicial | 94,30 % | 88,13 % | 262 | 3 |
|  | Local corregido | 96,32 % | 89,15 % | 151 | 2 |
| Escaneo malo | Nube | 97,21 % | 91,46 % | 21 | 53 |
|  | Local inicial | 83,08 % | 66,57 % | 467 | 140 |
|  | Local corregido | 84,92 % | 67,15 % | 360 | 140 |
| Fax | Nube | 91,20 % | 83,07 % | 6 | 115 |
|  | Local inicial | 82,70 % | 74,10 % | 377 | 129 |
|  | Local corregido | 86,71 % | 75,69 % | 151 | 130 |

Qué se aprende de esta tabla:

- **Con imágenes buenas, la nube es casi perfecta:** del 99,5 % al 99,9 % de las palabras.
- **Con imágenes buenas, el local inicial ya perdía de 5 a 9 puntos**, y más con la imagen limpia que con el escaneo normal. No era la calidad: era el fallo de las líneas giradas. Con la corrección, la imagen limpia pasa del 91,1 % al 97,5 %.
- **El escaneo malo y el fax son lo más difícil para los dos.** Donde más se separan es en los números: con escaneo malo, 91,5 % la nube frente a 67,2 % el local corregido.
- **Casi todas las cifras inventadas están en escaneo malo y fax:** el 91 % de las de la nube y el 88 % de las del local corregido.

### Por tipo de documento y tamaño de letra

| Grupo | Palabras | Nube | Local inicial | Local corregido |
|---|---:|---:|---:|---:|
| Escritos | 31.728 | 98,07 % | 90,96 % | 94,42 % |
| Facturas | 3.126 | 96,16 % | 79,08 % | 79,33 % |
| Letra pequeña (7,5–9 pt) | 10.482 | 96,74 % | 89,29 % | 91,57 % |
| Letra normal (9–11 pt) | 10.560 | 98,44 % | 91,09 % | 95,85 % |
| Letra grande (10,5–12,5 pt) | 10.686 | 99,01 % | 92,47 % | 95,81 % |

Las facturas son lo más difícil para el servicio local. En los escaneos malos, repite el texto de las celdas combinadas en varias columnas y desordena las tablas.

### Por tipo de dato

Un dato cuenta como **presente** si su valor completo aparece en cualquier punto de la lectura.

| Dato | Apariciones | Nube | Local inicial | Local corregido |
|---|---:|---:|---:|---:|
| Importe | 678 | 90,1 % | 87,2 % | 88,1 % |
| Cantidad | 378 | 94,2 % | 92,3 % | 93,7 % |
| Fecha | 288 | 99,0 % | 96,2 % | 98,6 % |
| Porcentaje | 276 | 97,8 % | 94,9 % | 94,9 % |
| NIF | 186 | 97,3 % | 96,2 % | 97,8 % |
| Referencia | 180 | 98,9 % | 96,7 % | 97,8 % |
| Concepto | 144 | 93,1 % | 89,6 % | 90,3 % |
| Precio unitario | 126 | 81,0 % | 85,7 % | 85,7 % |
| Ejercicio fiscal | 108 | 100,0 % | 100,0 % | 100,0 % |
| Número de factura | 96 | 99,0 % | 97,9 % | 97,9 % |
| IBAN | 90 | 92,2 % | 88,9 % | 90,0 % |
| Código postal | 72 | 98,6 % | 90,3 % | 97,2 % |
| Correo electrónico | 54 | 94,4 % | 92,6 % | 92,6 % |
| Teléfono | 54 | 96,3 % | 100,0 % | 100,0 % |
| Nombre | 42 | 97,6 % | 85,7 % | 85,7 % |
| Hora | 36 | 91,7 % | 72,2 % | 97,2 % |
| Periodo | 36 | 100,0 % | 100,0 % | 100,0 % |

- **El local encuentra casi tantos importes como la nube, pero muchos fuera de su sitio:** en cualquier punto, 88,1 % frente a 90,1 %; en su sitio, 72,9 % frente a 90,0 %. La diferencia se concentra en las tablas de las facturas, donde quedan en su sitio el 60,4 % frente al 87,1 %.
- **La hora y el código postal son los que más mejoran con la corrección del giro:** del 72,2 % al 97,2 % y del 90,3 % al 97,2 %.
- **En cuatro tipos de dato el local corregido supera a la nube:** hora, teléfono, precio unitario y NIF.
- **Tildes en fax:** con fax, la nube pierde la tilde en muchas palabras. Acierta el 61,5 % de las palabras con tilde, y el local corregido, el 79,6 %.

## Facturas: los datos extraídos

Porcentaje de comprobaciones correctas en las 24 facturas.

| Dato | Comprobaciones | Nube | Local inicial | Local + giro | Local + IVA |
|---|---:|---:|---:|---:|---:|
| Número de factura | 24 | 75,0 % | 87,5 % | 87,5 % | 95,8 % |
| Fecha | 24 | 100,0 % | 87,5 % | 87,5 % | 95,8 % |
| NIF del emisor | 24 | 75,0 % | 91,7 % | 91,7 % | 100,0 % |
| NIF del cliente | 18 | 100,0 % | 94,4 % | 94,4 % | 100,0 % |
| Base imponible | 24 | 75,0 % | 100,0 %¹ | 100,0 %¹ | 100,0 % |
| Desglose por tipo: base | 48 | 87,5 % | 0,0 %¹ | 0,0 %¹ | 72,9 % |
| Desglose por tipo: cuota | 48 | 87,5 % | 0,0 %¹ | 0,0 %¹ | 72,9 % |
| Desglose por tipo: recargo de equivalencia | 18 | 83,3 % | 0,0 % | 0,0 % | 66,7 % |
| Total IVA | 24 | 95,8 % | 22,7 %¹ | 22,7 %¹ | 87,5 % |
| Retención IRPF | 6 | 100,0 % | 83,3 % | 83,3 % | 100,0 % |
| Total | 24 | 100,0 % | 91,7 % | 91,7 % | 100,0 % |
| Número de líneas | 24 | 100,0 % | 91,7 % | 91,7 % | 100,0 % |
| Líneas: importe | 144 | 97,9 % | 94,4 % | 94,4 % | 99,3 % |
| Líneas: cantidad | 144 | 70,8 % | 70,8 % | 70,8 % | 70,8 % |
| Líneas: precio unitario | 144 | 63,9 % | 70,8 % | 70,8 % | 70,8 % |

¹ Las dos facturas que estas series descartaban no se cuentan, porque no tienen datos de impuestos. Contándolas como ausentes: base imponible 91,7 %, total IVA 20,8 % y desglose 0 %.

Por calidad:

| Calidad | Nube | Local inicial | Local + giro | Local + IVA |
|---|---:|---:|---:|---:|
| Limpia | 82,93 % | 70,73 % | 70,73 % | 86,99 % |
| Escaneo | 78,86 % | 70,73 % | 70,73 % | 86,99 % |
| Fotocopia | 82,93 % | 70,73 % | 70,73 % | 86,99 % |
| Foto | 82,93 % | 70,73 % | 70,73 % | 86,99 % |
| Escaneo malo | 84,55 % | 63,03 %¹ | 63,03 %¹ | 78,05 % |
| Fax | 81,30 % | 62,18 %¹ | 62,18 %¹ | 74,80 % |
| **Todas** | **82,25 %** | **68,08 %**¹ | **68,08 %**¹ | **83,47 %** |

Qué se aprende:

- **Antes de corregirlo, el servicio local dejaba vacío el desglose del IVA**, casi siempre también el total de IVA, y descartaba dos facturas enteras.
- **Con el IVA verificado acierta el total de IVA en el 87,5 % y el desglose en el 72,9 %, sin ningún IVA erróneo publicado.** En las tres facturas en las que lo retiene, la regla no podía comprobarlo. En una, Qwen había intercambiado dos tipos de IVA y las cuentas no cuadraban. En dos faxes, el lector leyó la coma decimal como un punto.
- **El desglose del IVA sigue siendo mejor en la nube.** Sin contar el ticket, que ninguno de los dos desglosa, la nube acierta todas las bases y cuotas, y el local corregido, el 83,3 %. A cambio, la nube publicó un total de IVA erróneo, y el local, ninguno.
- **En el ticket, la nube no extrae el número, el NIF del emisor ni la base** en ninguna de las seis calidades. El servicio local sí.
- **Las cantidades y los precios de las líneas fallan en todas las series.** En parte es un defecto de la referencia: el precio se guardó redondeado a dos decimales y la factura imprime tres, y el ticket no imprime cantidad ni precio por línea.
- **Revisión humana:** el servicio local la pide en todos los documentos, por diseño, mientras su lectura no esté validada con documentos reales. La nube la pidió en 35 de 114.

## Los dos fallos encontrados y corregidos

### 1. El lector daba la vuelta a líneas que estaban derechas

El servicio local perdía 2.078 palabras, casi siempre líneas enteras en mitad de un párrafo, incluso con la imagen limpia. De un párrafo de tres líneas conservaba el principio y el final, y la línea del medio no aparecía en ninguna parte. No se perdía en Qwen ni al montar el texto, sino dentro del lector:

- Antes de reconocer cada línea, RapidOCR usa un clasificador pequeño (`ch_ppocr_mobile_v2.0_cls`) para decidir si está boca abajo. Ese clasificador reduce cada recorte a 48 × 192 píxeles. Una línea de párrafo es unas 47 veces más ancha que alta, así que queda aplastada e ilegible, y a veces el clasificador responde «boca abajo» con mucha seguridad.
- Entonces gira una línea que estaba derecha. El reconocedor la lee al revés y devuelve basura con poca confianza. Si la confianza queda por debajo de 0,5, **la línea se descarta sin dejar rastro**.
- En las 114 lecturas, el clasificador giró 102 de 4.635 líneas (2,2 %). En 98 de ellas, la lectura sin girar tenía más confianza. 31 desaparecieron y las otras 71 quedaron cambiadas o convertidas en basura.

**Corrección:** cuando el clasificador gira una línea, se lee también sin girar y se publica la lectura con más confianza. Si la lectura girada es una cifra plausible, no se elige por confianza: se marca como dudosa, como antes. Cada sustitución queda registrada con las dos lecturas.

**Efecto:**

- Midiendo solo el lector, las palabras correctas pasan del 91,6 % al 95,0 %. Es lo mismo que se obtiene apagando el clasificador, que se mantiene porque en recortes cortos a veces acierta.
- En el servicio completo, pasan del 89,9 % al 93,1 %, y las palabras perdidas bajan de 2.078 a 1.038. Mejoran 47 documentos, 66 quedan igual y 1 empeora. Ese documento no pierde texto: recupera un párrafo entero, pero Docling lo coloca antes del que debería precederlo y la puntuación por posición lo penaliza.

### 2. El IVA correcto se retiraba y dos facturas se descartaban

- **IVA retirado.** Qwen proponía bien el total de IVA en las 17 facturas que clasificaba como tales, y el desglose en 16. Pero el servicio local, para no publicar un impuesto inventado, solo lo aceptaba si un extractor estricto lo encontraba por su cuenta en la página. Ese extractor no reconocía ninguna de las tres maquetas de factura de la prueba, así que el IVA salía vacío.
- **Facturas descartadas.** En 2 de las 24 facturas (el ticket con escaneo malo y la de servicios en fax), una comprobación previa creyó ver varias cabeceras en la página. La clasificó como «otro» y no extrajo nada, sin llegar a consultar a Qwen.

**Corrección:**

- **El IVA propuesto se conserva solo si cuadra con los importes impresos:**
  - cada base, cuota y total aparece tal cual en la lectura;
  - base × tipo = cuota en cada fila, también para el recargo de equivalencia;
  - la suma de las bases da la base imponible;
  - bases + IVA + recargo − retención = total.

  Si no cuadra, se retira como antes. No calcula ningún dato que el modelo no haya propuesto, y lo que el extractor estricto encuentre en la página sigue teniendo prioridad.
- **Una página sin indicios de contener varios documentos se extrae como una sola factura**, con un aviso que obliga a revisarla. Los indicios son dos códigos QR fiscales, dos cabeceras o dos totales.

**Efecto:** los datos de factura correctos pasan del 68,1 % al 83,5 %, sin ningún IVA erróneo publicado. Antes de instalar la corrección, se comprobó sobre las lecturas guardadas: publicaba el IVA de 15 de las 17 facturas, todos correctos.

## ¿Las diferencias son fiables?

| Comparación | Palabras: diferencia en puntos | Números: diferencia en puntos | Documentos ganados |
|---|---:|---:|---|
| Nube frente a local inicial | +8,0 (6,2 a 10,1) | +13,6 (10,7 a 16,2) | nube 112, local 1, empate 1 |
| Nube frente a local corregido | +4,8 (3,4 a 6,9) | +12,0 (8,8 a 15,3) | nube 110, local 3, empate 1 |
| Local corregido frente a local inicial | +3,2 (1,8 a 4,6) | +1,6 (0,5 a 2,9) | corregido 47, inicial 1, empate 66 |

- **Diferencia:** puntos de acierto de la primera serie menos la segunda. Entre paréntesis, el intervalo de confianza del 95 %, calculado con *bootstrap*: se repite el cálculo 4.000 veces eligiendo al azar documentos de origen, cada uno con sus seis calidades.
- **Ningún intervalo incluye el cero**, así que las tres diferencias son claras. La prueba de Wilcoxon por documento lo confirma, con p < 0,0001 en los tres casos.
- La prueba de McNemar, palabra a palabra, también coincide. Pero supone que las palabras de un documento son independientes, así que su resultado es optimista y no se usa como referencia.

## Lo que todavía separa al servicio local de la nube

- **Pies de página.** Docling quita «Página N de M» del texto aunque el lector lo lee: son 431 de las 1.038 palabras que aún se pierden. La nube devuelve los pies como comentario, y aquí cuentan como leídos.
- **Orden de lectura en escaneos malos.** Docling a veces cambia el orden de los bloques. El texto está, pero fuera de sitio: con escaneo malo, el acierto en cualquier orden supera en 7,7 puntos al acierto en su sitio. En el resto de calidades la diferencia es de 0,8 a 1,5 puntos, y en la nube no llega a 0,2.
- **Cifras en imágenes muy degradadas.** Con escaneo malo y fax, el local acierta el 67 % y el 76 % de los números, frente al 91 % y el 83 % de la nube.
- **Decimales en fax.** El lector local confunde a veces la coma decimal con un punto.
- **Páginas boca abajo.** El clasificador de orientación no endereza una página escaneada al revés. Con él o sin él se pierde casi todo el texto, así que hace falta detectar la orientación de la página antes de leerla. Se comprobó con seis copias giradas de documentos de la prueba.
- **Velocidad.** Con dos documentos a la vez, la nube tardó una mediana de 20,7 s por documento, y el local, unos 29 s. El lector local trabaja en el procesador y atiende un documento cada vez.

## Límites de la prueba

- **Documentos inventados:** de una columna, con fuentes estándar y degradación simulada. No hay sellos, firmas, manuscritos, logotipos ni papel térmico. Con documentos reales las cifras pueden cambiar.
- **Pocos documentos de origen:** son 19, y las seis calidades de un mismo documento no son independientes. Por eso la fiabilidad estadística se calcula por documento de origen.
- **Sin regla de decisión previa.** Las medidas se definieron antes de ver los resultados completos, salvo dos ajustes hechos al ver salidas reales. Los dos son neutrales o favorables al servicio local: se ignora una nota fija que el local añade a las tablas reconstruidas, y la retención se compara sin signo.
- **Las correcciones se diseñaron mirando estos mismos documentos.** Las mejoras de la tercera y la cuarta serie pueden ser optimistas hasta repetirlas con documentos nuevos.
- **«Presente» es una medida generosa:** busca el dato en cualquier punto de la lectura, así que puede dar por buena una cifra corta que aparezca en otro sitio. «En su sitio» es la medida estricta.
- **Defectos de la referencia** en las cantidades y los precios de las líneas, explicados arriba. Afectan a todas las series.
- **Una sola ejecución por serie.** No se midió el coste de la nube. La versión exacta de Claude no queda registrada en sus respuestas.
- **Tercera serie:** 31 documentos se procesaron con una versión previa que solo se diferenciaba en un fallo al registrar las sustituciones, corregido durante la ejecución, y su texto es el mismo. En 4 documentos, el tiempo es el de proceso en el servidor, no el medido desde el cliente.

## Archivos y cómo leerlos

| Archivo | Para qué sirve |
|---|---|
| [`por-documento.md`](por-documento.md) | Tabla legible con el resultado de cada uno de los 114 documentos |
| [`mediciones.json`](mediciones.json) | Todos los resultados: globales, por calidad, por tipo de documento, de letra, de palabra y de dato, los datos de factura, las comparaciones estadísticas y el diagnóstico del lector |
| [`por-documento.json`](por-documento.json) | Lo mismo que `por-documento.md`, con todos los recuentos de cada serie |
| [`configuracion.json`](configuracion.json) | Versiones, envío, estropeado de las imágenes y cómo se puntuó |

Significado de los nombres que aparecen en los archivos `.json`:

| Nombre | Significa |
|---|---|
| `nube`, `local_inicial`, `local_giro_corregido`, `local_iva_verificado` | Las cuatro series |
| `limpia`, `escaneo`, `fotocopia`, `foto`, `escaneo_malo`, `fax` | Las seis calidades |
| `correcto`, `tilde_mayuscula`, `sustituido`, `omitido` | Cada palabra de la referencia: bien leída en su sitio, con error solo de tilde o mayúscula, cambiada por otra, o perdida |
| `insertadas` | Palabras de la lectura que sobran al alinearla con la referencia |
| `inventadas` | Palabras sobrantes que no existen en ninguna parte del documento |
| `cifras_inventadas` | Números de la lectura que no existen en el documento o que aparecen más veces de las que tiene |
| `cualquier_orden`, `recuperacion_cualquier_orden` | Palabras de la referencia encontradas en la lectura sin importar el orden |
| `acierto_palabras` | Proporción de palabras `correcto`. 1 es perfecto |
| `acierto_ignorando_tildes` | Lo mismo, aceptando los errores solo de tilde o mayúscula |
| `acierto_solo_letras`, `acierto_numeros`, `acierto_con_tilde` | Acierto en palabras solo de letras, en palabras con alguna cifra y en palabras con tilde o eñe |
| `wer` | Palabras con algún error (cambiadas, perdidas, de tilde o sobrantes) entre las palabras de la referencia. 0 es perfecto |
| `cer_aprox` | Lo mismo por caracteres, aproximado a partir de la alineación de palabras |
| `docs_requieren_revision`, `requiere_revision` | Documentos que el servicio marcó para revisión humana |
| `segundos_mediana`, `segundos` | Tiempo por documento medido desde el cliente, con dos documentos a la vez por servicio |
| `posicional`, `presente` | Un dato está bien en su sitio, o aparece en cualquier punto de la lectura |
| `facturas_json` | Comprobaciones de los datos extraídos: `acierto`, `ausente` (no lo dio) e `incorrecto` (dio otro valor) |
| `contrastes` | Cada par de series sobre las mismas imágenes: `ambos_bien`, `solo_<serie>` y `ambos_mal` por palabra; `victorias` por documento; `wilcoxon` por documento; y `bootstrap` con la diferencia (primera serie menos segunda) y su intervalo del 95 % |
| `mcnemar_p` | p de la prueba de McNemar por palabra. Un 0 significa que es más pequeño de lo que el cálculo puede representar |
