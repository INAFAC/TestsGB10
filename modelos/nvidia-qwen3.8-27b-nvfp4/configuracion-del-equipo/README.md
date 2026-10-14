# Equipo, configuración y registros

[Volver a los resultados del modelo](../README.md)

Estos archivos permiten verificar con qué equipo y parámetros se hizo cada prueba. Los resultados y las explicaciones de cada conversación están en las carpetas de memoria del modelo.

- [Equipo y modelo](equipo.json): memoria total, tamaño de los pesos, imagen de vLLM y límite del modelo.
- [Plan y estado de la campaña](2026-10-14/plan-de-las-pruebas/plan-y-estado-general.json).
- [Configuraciones y estado de las pruebas al 30%](2026-10-14/pruebas-con-30-por-ciento/configuracion-y-estado.json).
- [Configuraciones y estado de la comparación de memoria y concurrencia](2026-10-14/comparacion-de-memoria-y-concurrencia/configuracion-y-estado.json).
- [Inventario de archivos originales](2026-10-14/inventario-de-archivos-originales.json): conserva las huellas de los archivos para comprobar su integridad.

Durante el cambio de orden de las pruebas, después del 30%, se interrumpió una recreación de Docker. El primer intento de restauración coincidió con ella. Se recuperó ejecutando el Compose original y restituyendo el nombre del contenedor, y después se verificaron la configuración del 40% y su disponibilidad. Las cuatro pruebas al 30% ya habían terminado. Esta incidencia de coordinación se conserva en los registros; no se cuenta como un límite de capacidad del modelo.
