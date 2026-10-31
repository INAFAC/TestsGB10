# Resultados imagen a imagen

[Volver a la comparación](README.md)

Cada fila es una imagen. **Valores** es cuántos datos críticos (importes, fechas, NIF, IBAN…) tiene esa página. **Fallos** son los que el lector leyó mal o no encontró. **Inventadas** son cifras que el lector escribió y que no existen en el documento. Un 0 es lo ideal.

Una factura de varias páginas aparece en varias filas (p. 1, p. 2…). Los estilos se repiten en ciclo: clásica (tabla con bordes), sin bordes (columnas sin rejilla), ticket (factura simplificada estrecha) y servicios (profesional con retención).

| Factura | Estilo | Pág. | Calidad | Valores | PP-OCRv6: fallos | PP-OCRv6: inventadas | Unlimited 2: fallos | Unlimited 2: inventadas |
|---|---|---:|---|---:|---:|---:|---:|---:|
| INV-001 | clásica | 1 | limpia | 65 | 0 | 0 | 0 | 0 |
| INV-001 | clásica | 1 | escaneo | 65 | 0 | 0 | 0 | 0 |
| INV-001 | clásica | 1 | foto | 65 | 0 | 0 | 0 | 0 |
| INV-001 | clásica | 1 | escaneo malo | 65 | 10 | 1 | 1 | 1 |
| INV-002 | sin bordes | 1 | limpia | 21 | 0 | 0 | 1 | 1 |
| INV-002 | sin bordes | 1 | escaneo | 21 | 1 | 0 | 0 | 0 |
| INV-002 | sin bordes | 1 | foto | 21 | 1 | 0 | 0 | 0 |
| INV-002 | sin bordes | 1 | escaneo malo | 21 | 2 | 7 | 5 | 0 |
| INV-003 | ticket | 1 | limpia | 24 | 0 | 1 | 0 | 0 |
| INV-003 | ticket | 1 | escaneo | 24 | 0 | 0 | 0 | 0 |
| INV-003 | ticket | 1 | foto | 24 | 0 | 0 | 1 | 1 |
| INV-003 | ticket | 1 | escaneo malo | 24 | 5 | 2 | 4 | 2 |
| INV-004 | servicios | 1 | limpia | 10 | 0 | 0 | 0 | 0 |
| INV-004 | servicios | 1 | escaneo | 10 | 0 | 0 | 0 | 0 |
| INV-004 | servicios | 1 | foto | 10 | 0 | 0 | 0 | 0 |
| INV-004 | servicios | 1 | escaneo malo | 10 | 1 | 4 | 1 | 4 |
| INV-005 | clásica | 1 | limpia | 134 | 0 | 0 | 0 | 0 |
| INV-005 | clásica | 1 | escaneo | 134 | 0 | 0 | 0 | 0 |
| INV-005 | clásica | 1 | foto | 134 | 1 | 0 | 0 | 0 |
| INV-005 | clásica | 1 | escaneo malo | 134 | 4 | 5 | 4 | 1 |
| INV-005 | clásica | 2 | limpia | 88 | 0 | 0 | 0 | 0 |
| INV-005 | clásica | 2 | escaneo | 88 | 0 | 0 | 0 | 0 |
| INV-005 | clásica | 2 | foto | 88 | 0 | 0 | 0 | 0 |
| INV-005 | clásica | 2 | escaneo malo | 88 | 13 | 92 | 9 | 4 |
| INV-006 | sin bordes | 1 | limpia | 102 | 0 | 0 | 1 | 1 |
| INV-006 | sin bordes | 1 | escaneo | 102 | 0 | 0 | 0 | 0 |
| INV-006 | sin bordes | 1 | foto | 102 | 0 | 0 | 0 | 1 |
| INV-006 | sin bordes | 1 | escaneo malo | 102 | 7 | 5 | 32 | 0 |
| INV-006 | sin bordes | 2 | limpia | 71 | 1 | 2 | 0 | 0 |
| INV-006 | sin bordes | 2 | escaneo | 71 | 1 | 0 | 0 | 0 |
| INV-006 | sin bordes | 2 | foto | 71 | 1 | 0 | 0 | 0 |
| INV-006 | sin bordes | 2 | escaneo malo | 71 | 3 | 1 | 0 | 0 |
| INV-007 | ticket | 1 | limpia | 27 | 0 | 0 | 0 | 0 |
| INV-007 | ticket | 1 | escaneo | 27 | 0 | 0 | 0 | 0 |
| INV-007 | ticket | 1 | foto | 27 | 0 | 0 | 0 | 0 |
| INV-007 | ticket | 1 | escaneo malo | 27 | 9 | 1 | 1 | 1 |
| INV-008 | servicios | 1 | limpia | 10 | 0 | 0 | 0 | 0 |
| INV-008 | servicios | 1 | escaneo | 10 | 0 | 0 | 0 | 0 |
| INV-008 | servicios | 1 | foto | 10 | 0 | 0 | 0 | 0 |
| INV-008 | servicios | 1 | escaneo malo | 10 | 0 | 0 | 0 | 0 |
| INV-009 | clásica | 1 | limpia | 78 | 0 | 0 | 0 | 0 |
| INV-009 | clásica | 1 | escaneo | 78 | 0 | 1 | 0 | 0 |
| INV-009 | clásica | 1 | foto | 78 | 0 | 0 | 0 | 0 |
| INV-009 | clásica | 1 | escaneo malo | 78 | 4 | 41 | 4 | 0 |
| INV-010 | sin bordes | 1 | limpia | 29 | 0 | 0 | 1 | 1 |
| INV-010 | sin bordes | 1 | escaneo | 29 | 1 | 0 | 0 | 0 |
| INV-010 | sin bordes | 1 | foto | 29 | 1 | 0 | 1 | 1 |
| INV-010 | sin bordes | 1 | escaneo malo | 29 | 1 | 0 | 3 | 1 |
| INV-011 | ticket | 1 | limpia | 18 | 0 | 0 | 0 | 0 |
| INV-011 | ticket | 1 | escaneo | 18 | 0 | 4 | 0 | 0 |
| INV-011 | ticket | 1 | foto | 18 | 0 | 0 | 0 | 0 |
| INV-011 | ticket | 1 | escaneo malo | 18 | 4 | 0 | 3 | 2 |
| INV-012 | servicios | 1 | limpia | 11 | 0 | 0 | 0 | 0 |
| INV-012 | servicios | 1 | escaneo | 11 | 0 | 0 | 0 | 0 |
| INV-012 | servicios | 1 | foto | 11 | 0 | 0 | 0 | 0 |
| INV-012 | servicios | 1 | escaneo malo | 11 | 0 | 0 | 0 | 0 |
| INV-013 | clásica | 1 | limpia | 133 | 0 | 0 | 0 | 0 |
| INV-013 | clásica | 1 | escaneo | 133 | 0 | 0 | 0 | 0 |
| INV-013 | clásica | 1 | foto | 133 | 0 | 1 | 0 | 0 |
| INV-013 | clásica | 1 | escaneo malo | 133 | 5 | 7 | 3 | 0 |
| INV-013 | clásica | 2 | limpia | 74 | 0 | 0 | 0 | 0 |
| INV-013 | clásica | 2 | escaneo | 74 | 0 | 0 | 0 | 0 |
| INV-013 | clásica | 2 | foto | 74 | 0 | 0 | 0 | 0 |
| INV-013 | clásica | 2 | escaneo malo | 74 | 4 | 48 | 1 | 0 |
| INV-014 | sin bordes | 1 | limpia | 102 | 0 | 0 | 0 | 0 |
| INV-014 | sin bordes | 1 | escaneo | 102 | 0 | 0 | 1 | 1 |
| INV-014 | sin bordes | 1 | foto | 102 | 0 | 0 | 1 | 1 |
| INV-014 | sin bordes | 1 | escaneo malo | 102 | 0 | 3 | 1 | 1 |
| INV-014 | sin bordes | 2 | limpia | 47 | 0 | 0 | 0 | 0 |
| INV-014 | sin bordes | 2 | escaneo | 47 | 1 | 0 | 0 | 0 |
| INV-014 | sin bordes | 2 | foto | 47 | 1 | 0 | 0 | 0 |
| INV-014 | sin bordes | 2 | escaneo malo | 47 | 1 | 0 | 0 | 1 |
| INV-015 | ticket | 1 | limpia | 21 | 0 | 0 | 0 | 0 |
| INV-015 | ticket | 1 | escaneo | 21 | 0 | 0 | 0 | 0 |
| INV-015 | ticket | 1 | foto | 21 | 0 | 0 | 0 | 0 |
| INV-015 | ticket | 1 | escaneo malo | 21 | 3 | 1 | 1 | 1 |
| INV-016 | servicios | 1 | limpia | 11 | 0 | 0 | 0 | 0 |
| INV-016 | servicios | 1 | escaneo | 11 | 0 | 0 | 0 | 0 |
| INV-016 | servicios | 1 | foto | 11 | 0 | 0 | 0 | 0 |
| INV-016 | servicios | 1 | escaneo malo | 11 | 0 | 0 | 0 | 0 |
