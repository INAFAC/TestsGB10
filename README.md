# Pruebas de modelos en el GB10

Resultados para decidir cuánta memoria reservar y cuántas conversaciones puede atender cada modelo, incluyendo historiales cercanos a su límite.

**Se están realizando nuevas pruebas de conversaciones recurrentes con 10, 20 y 30 usuarios.**

**Cada prueba indica el límite de solicitudes activas impuesto al servidor.** Ese límite debe distinguirse de la capacidad del GB10.

## Resultados por modelo

| Modelo | Máximo por conversación | Informe |
|---|---:|---|
| Qwen3.8-27B-NVFP4 | 262.144 tokens | [Resultados y configuración](modelos/nvidia-qwen3.8-27b-nvfp4/README.md) · [Conversaciones con varios usuarios](modelos/nvidia-qwen3.8-27b-nvfp4/conversaciones-recurrentes/README.md) |

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
