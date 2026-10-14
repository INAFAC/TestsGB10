# Equipo, configuración y registros

[Volver a los resultados del modelo](../README.md)

Estos archivos permiten verificar con qué equipo y parámetros se hizo cada prueba. Los resultados y las explicaciones de cada conversación están en las carpetas de memoria del modelo.

- [Equipo y modelo](equipo.json): memoria total, tamaño de los pesos, imagen de vLLM y límite del modelo.
- [Plan y estado de la campaña](2026-10-14/plan-de-las-pruebas/plan-y-estado-general.json).
- [Configuraciones y estado de las pruebas al 30%](2026-10-14/pruebas-con-30-por-ciento/configuracion-y-estado.json).
- [Configuraciones y estado de la comparación de memoria y concurrencia](2026-10-14/comparacion-de-memoria-y-concurrencia/configuracion-y-estado.json).
- [Comparaciones adicionales y repeticiones de control](2026-10-14/comparaciones-adicionales/configuracion-y-estado.json).
- [Verificaciones finales del 30%, 40% y 92%](2026-10-14/comparaciones-adicionales/verificacion-final/configuracion-y-estado.json).
- [Inventario de archivos originales](2026-10-14/inventario-de-archivos-originales.json): conserva las huellas de los archivos para comprobar su integridad.

Durante el cambio de orden de las pruebas, después del 30%, se interrumpió una recreación de Docker. El primer intento de restauración coincidió con ella. Se recuperó ejecutando el Compose original y restituyendo el nombre del contenedor, y después se verificaron la configuración del 40% y su disponibilidad. Las cuatro pruebas al 30% ya habían terminado. Esta incidencia de coordinación se conserva en los registros; no se cuenta como un límite de capacidad del modelo.

## Comprobación final del servicio restaurado

Verificación realizada el **14 de octubre de 2026 a las 21:45 UTC** (23:45 en Madrid), después de terminar todas las pruebas.

| Comprobación | Resultado |
|---|---|
| Contenedor | `vllm-qwen38`, en ejecución |
| Presupuesto de memoria | 40% |
| Límite de solicitudes activas | 4 |
| Contexto máximo | 262.144 tokens por conversación |
| Estado de salud | HTTP 200 |
| Generación de comprobación | 16 tokens de entrada y los 16 de respuesta pedidos; 1,36 s |
| Solicitudes activas / en cola al terminar | 0 / 0 |
| Comando, imagen y archivo Compose | Coinciden con la configuración original; Compose sin cambios |

La campaña contiene **67 pruebas detalladas de conversaciones**: 65 completaron todas sus solicitudes y dos registraron errores de espera. En total son **2.128 solicitudes completadas y tres fallidas**. Se conservan además 11 mediciones históricas, 26 comprobaciones de arranque (dos fallidas) y un rechazo esperado por exceder el contexto. Las repeticiones no borran los fallos anteriores.

- [Resultado original de la comprobación](2026-10-14/plan-de-las-pruebas/comprobacion-final-del-servicio.json): incluye el comando, las huellas del Compose y de la imagen, la respuesta de la API y los contadores finales.
- [Script utilizado para verificar la restauración](2026-10-14/plan-de-las-pruebas/verificacion-final-del-servicio.py).
