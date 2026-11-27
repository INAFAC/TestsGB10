# ¿Cuántos ficheros puede procesar el GB10 a la vez?

[Volver al inicio](../../README.md)

## Resumen en 30 segundos

En lotes cortos comparables, el GB10 pasó de **120 a 268 ficheros por hora**. El primer valor corresponde al servicio del 9 de noviembre con un solo trabajo activo. El segundo se obtuvo el día 10 con ocho trabajos y un lector reservado para ficheros cortos. Durante la lectura de un escaneado de **300 páginas**, doce facturas nuevas de una página terminaron en **6,5 minutos** desde su envío.

## Cómo se hizo la prueba

Los documentos eran inventados. El servicio completo recibió los ficheros, los puso en cola, leyó el contenido con Docling y PP-OCRv6 en CPU y lo interpretó con Qwen. Los lotes cortos de 48 ficheros contenían 66 páginas con el mismo reparto de formatos. Cada configuración recibió contenido nuevo. El límite de memoria del proceso de trabajo fue de 10 GiB.

| Configuración | Lectores | Turnos para Qwen | Ficheros | Minutos | Ficheros/h |
|---|---:|---:|---:|---:|---:|
| Referencia, un trabajo | 1 | 4 | 96 | 47,9 | 120 |
| Cuatro trabajos | 1 | 4 | 48 | 15,0 | 192 |
| Seis trabajos | 1 | 4 | 48 | 12,0 | 239 |
| Ocho trabajos | 1 | 8 | 48 | 10,7 | 270 |
| Dos procesos con cuatro trabajos cada uno | 2 | 8 | 48 | 9,7 | 297 |
| Ocho trabajos con lector reservado para documentos cortos | 2 | 8 | 48 | 10,7 | 268 |

La referencia agrupa cuatro lotes del día anterior. Los 297 ficheros/h se midieron con dos procesos en un lote corto. La configuración final, de un solo proceso, dedicó dos de los ocho trabajos y un lector a documentos de hasta diez páginas para reducir su espera tras los expedientes largos.

## Qué ocurre cuando entra un expediente largo

Se enviaron el escaneado de 300 páginas y 48 ficheros cortos. Ocho minutos después llegaron otras doce facturas. Los tiempos se cuentan desde el envío de cada grupo y los intervalos se solapan.

| Grupo | Terminaron | Tiempo hasta el último resultado |
|---|---:|---:|
| Escaneado de 300 páginas | 1/1 | 86,8 min |
| Lote mixto inicial | 48/48 | 14,4 min |
| Facturas llegadas durante la lectura | 12/12 | 6,5 min |

El pico conjunto del proceso de trabajo fue de **8,2 GiB**. En las pruebas anteriores con un solo lector, las facturas cortas llegaron a esperar entre 37 y 40 minutos para poder leerse. El expediente largo terminó con 105 subdocumentos extraídos. La exactitud de cada división y de sus campos quedó fuera de la medición.

## Intentos y límites

Un ensayo intermedio con un expediente de 150 páginas y un lote corto terminó con 23 de 25 ficheros completados. En una primera prueba de 300 páginas con la agrupación de regiones en serie se canceló el expediente al observar el retraso. El recorrido completo de 86,8 minutos se midió después de paralelizar esa etapa. Son intentos diferentes.

Se hizo una serie por configuración en un equipo con inferencia compartida. Al cambiar los trabajos también variaron los hilos, los lectores o los turnos del modelo. El aumento de caudal corresponde al conjunto de la configuración y depende de la mezcla de documentos.

[Mediciones por carga y perfil](mediciones.json) · [Configuraciones de los lectores y del modelo](parametros.json) · [Línea base del día anterior](../tiempos-documentos-nube-vs-gb10/README.md)
