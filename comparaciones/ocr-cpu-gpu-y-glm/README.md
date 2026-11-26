# OCR en el GB10: ¿qué cambia al usar GPU y una segunda lectura?

[Volver al inicio](../../README.md)

## Resumen en 30 segundos

El 26 de noviembre de 2026, PP-OCRv6 pasó de **260 a 1.812 páginas/h** al cambiar de CPU a GPU, con una proporción similar de valores críticos reconocidos. GLM-OCR conservó mejor el texto, pero dejó pasar páginas con columnas ausentes. Al usar el texto de GLM y contrastarlo con PP-OCR, el banco envió **87 de las 150 imágenes a revisión**. Las **63 restantes** pasaron las comprobaciones de valores y columnas.

## Cómo se hizo la prueba

Se generaron 16 facturas y cuatro escritos ficticios, 25 páginas fuente en total. Se produjo cada página en seis calidades: limpia, escaneo, fotocopia, foto, escaneo malo y fax. Todos los lectores recibieron las mismas 150 imágenes. El generador proporciona el texto y los valores de referencia. Las seis variantes de una página comparten el mismo contenido.

La variante mejorada de PP-OCR prueba la orientación y recupera texto de cabeceras y pies. El híbrido compara las dos lecturas para decidir qué texto conservar y qué páginas enviar a revisión. Se evaluó tanto el uso del texto de PP-OCR como el de GLM como base.

| Lectura | Páginas/h¹ | Error de caracteres (%) | Valores críticos acertados (%) | Erróneas / páginas sin revisión² | Columnas omitidas en páginas sin revisión / total omitidas |
|---|---:|---:|---:|---:|---:|
| PP-OCR en CPU | 260 | 48,8 | 97,3 | 36/107 | 2/8 |
| PP-OCR en GPU | 1 812 | 48,8 | 97,3 | 33/105 | 2/8 |
| GPU con orientación y pies | 1 747 | 48,5 | 97,5 | 26/105 | 2/8 |
| GLM-OCR | 336 | 2,0 | 98,6 | 31/150 | 12/12 |
| Híbrido con texto de PP-OCR | 283 | 48,8 | 97,3 | 10/22 | 0/8 |
| Híbrido con texto de GLM-OCR | 282 | 2,0 | 98,7 | 0/63 | 0/12 |

¹ El ritmo se calcula dividiendo el número de páginas entre la suma de sus tiempos individuales. GLM se ejecutó con cuatro peticiones concurrentes. En los híbridos se sumaron los tiempos de ambos lectores guardados, sin cronometrar un despliegue conjunto. Estas cifras describen el trabajo por página y no el caudal de un servicio concurrente de extremo a extremo.

² A efectos de esta columna, una imagen es errónea si falta o cambia un valor crítico, aparece un número o literal sin referencia, o se pierde una columna según el puntuador. Una página sin revisión puede contener otras erratas. Un valor crítico cuenta como acertado cuando se encuentra en la página. Esta medida no certifica que el valor esté asignado a la casilla correcta.

## Qué aporta la segunda lectura

GLM por sí solo dejó 150 páginas sin revisión, incluidas 31 con errores según ese criterio. El híbrido con texto de GLM conservó **98,7 % de acierto en valores críticos**. Sus 12 omisiones de columna ocurrieron en páginas enviadas a revisión. La marca se aplica a la página completa y puede deberse a otra discrepancia. El ensayo no demuestra que se identificara individualmente cada columna perdida.

El error de caracteres compara el texto normalizado con la referencia en orden de lectura y se promedia por imagen. Puede penalizar un orden distinto o el marcado de tablas aunque los importes aparezcan en la página. Por eso conviene leerlo junto con el acierto de valores. El resultado de cero errores en 63 imágenes sin revisión describe este corpus, con reglas probadas sobre las mismas muestras. Su generalización a documentos nuevos queda sin medir.

[Mediciones globales y acierto por tipo de valor](mediciones.json) · [Configuración y corpus](configuracion.json)
