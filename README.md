# Pruebas de modelos en el GB10

Resultados para decidir cuánta memoria reservar y cuántas conversaciones puede atender cada modelo, incluyendo historiales cercanos a su límite.



**Cada prueba indica el límite de solicitudes activas impuesto al servidor.** Ese límite debe distinguirse de la capacidad del GB10.

## Resultados por modelo

| Modelo | Máximo por conversación | Informe |
|---|---:|---|
| Qwen3.8-27B-NVFP4 | 262.144 tokens | [Resultados y configuración](modelos/nvidia-qwen3.8-27b-nvfp4/README.md) · [Conversaciones con varios usuarios](modelos/nvidia-qwen3.8-27b-nvfp4/conversaciones-recurrentes/README.md) |

<!-- conclusiones-inicio -->
## Resultado práctico de Qwen3.8

Estos controles usaron **70% de memoria y un límite de 32 solicitudes activas**. Cada persona conservó su historial entre mensajes.

| Carga de 20 personas | ¿Terminaron? | Espera al continuar, p95 |
|---|---|---:|
| Chat con unos 8.192 tokens, razonamiento desactivado y hasta 2.048 de salida | 60/60 respuestas visibles y terminadas naturalmente | 2,0 s |
| El mismo control con unos 32.768 tokens | 60/60 respuestas visibles y terminadas naturalmente | 7,4 min |
| Crecimiento sintético hasta 262.144 tokens | Las 20 personas llegaron al máximo; 40/40 respuestas completas | 172,9 min |

En el chat corto, el primer turno fue más lento: 103,2 s de espera visible p95. La prueba del contexto máximo pidió 512 tokens de salida por turno y tardó 346,5 minutos en total. **Poder terminar no significa poder conversar con rapidez.**

El 70% es una referencia medida, no un mínimo demostrado. El 60% obtuvo resultados cercanos en algunas cargas sintéticas, y subir al 85% no mejoró las dos comparaciones iniciales frente al 70% en estas ejecuciones. [Ver la elección de memoria, los resultados de 10 y 30 personas y sus límites](modelos/nvidia-qwen3.8-27b-nvfp4/README.md#qué-configuración-elegir).
<!-- conclusiones-fin -->

## Qué puedes comprobar

- **Si todas las conversaciones terminaron:** cuántas recibieron la respuesta completa solicitada.
- **Si llegaron al máximo de tokens:** se comprueba la suma real de historial y respuesta. También se distingue un límite reducido por falta de memoria.
- **Si respondieron a la vez o por turnos:** se muestran el solapamiento, las colas y los recálculos.
- **Cuánto tardaron y cuánta memoria usaron:** cada prueba incluye los tiempos y velocidades de cada conversación.

Un ejemplo: **262.016 tokens de historial + 128 de respuesta = 262.144 tokens en la conversación**. Llegar a ese límite no significa generar 262.144 tokens de respuesta nueva.

## Dónde está cada cosa

Entra en **modelos → nombre del modelo** y elige la comparación de memoria o las conversaciones recurrentes. Cada prueba reúne su explicación en `README.md`, sus mediciones y sus registros en la misma carpeta.

- [Guía de lectura](GUIA-DE-LECTURA.md): significado de las medidas y cómo se hicieron las pruebas.
- [Herramientas de prueba](scripts): scripts para medir y actualizar los informes.

## Licencia

El contenido de este repositorio se publica bajo [CC BY 4.0](LICENSE): puedes reutilizarlo y adaptarlo citando la fuente.
