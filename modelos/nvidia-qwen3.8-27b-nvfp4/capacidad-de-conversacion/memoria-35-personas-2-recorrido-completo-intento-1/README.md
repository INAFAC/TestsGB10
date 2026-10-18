# 2 personas · 35% de memoria

[Volver a la capacidad por memoria](../README.md)

**Error de API o plazo de espera del cliente.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **268/514 previstas**. Duración: **120,4 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Peticiones con error: **2**. Peticiones previstas que no llegaron a enviarse: **244**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.532–16.893 | 32/32 | 2,2 s | 2,2 s | 10,83 tokens/s | 19,9 s | Cumple |
| 18-33 | 17.917–33.277 | 32/32 | 2,4 s | 2,4 s | 9,90 tokens/s | 20,6 s | Cumple |
| 34-49 | 34.301–49.661 | 32/32 | 2,8 s | 2,9 s | 9,09 tokens/s | 23,0 s | Cumple |
| 50-65 | 50.685–66.045 | 32/32 | 3,2 s | 3,2 s | 8,40 tokens/s | 25,1 s | Cumple |
| 66-81 | 67.068–82.429 | 32/32 | 3,5 s | 3,5 s | 7,80 tokens/s | 26,7 s | Cumple |
| 82-97 | 83.453–98.813 | 32/32 | 3,8 s | 3,9 s | 7,30 tokens/s | 28,1 s | Cumple |
| 98-113 | 99.837–115.197 | 32/32 | 4,1 s | 4,1 s | 6,86 tokens/s | 30,1 s | Cumple |
| 114-129 | 116.220–131.581 | 32/32 | 4,5 s | 4,6 s | 6,42 tokens/s | 32,4 s | Cumple |
| 130-145 | 132.604–137.725 | 12/32 | 5,3 s | 5,3 s | 5,61 tokens/s | 32,5 s | Incompleto |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 134 | 136.869 | 52,211% | 125.275 |
| 2 | 134 | 136.846 | 52,203% | 125.298 |

El objetivo del cierre deja aproximadamente 128 tokens para la respuesta y pide terminar en diez palabras. El presupuesto efectivo se calcula con la entrada real. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento no llegó a ese cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 35% |
| Pico de memoria del motor / GB10 | 31,7% |
| Pico de memoria total del sistema / GB10 | 40,1% |
| Pico de caché | 100,0% |
| Solicitudes activas / respuestas solapadas, máximo | 2 / 2 |
| Cola máxima / segundos con cola | 2 / 121,4 s |
| Espera media al primer texto visible | 2,5 s |
| Espera media al primer token, incluido razonamiento | 2,5 s |
| Tiempo medio de petición completa | 20,4 s |
| Recálculos por falta de espacio de caché | 2 |
| Velocidad global, incluidas pausas | 5,66 tokens/s |
| Suma de tiempos individuales de petición | 5.714,1 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 134/135 | 2,5 s | 21,7 s | 7.222,4 s | 3,07 |
| 2 | 134/135 | 2,4 s | 19,1 s | 7.222,1 s | 2,59 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 146 | 0,4 s | 12,6 s | 11,91 | Natural |
| 2 | 1 | 512 | 137 | 0,4 s | 11,9 s | 11,89 | Natural |
| 1 | 2 | 1.532 | 207 | 1,2 s | 18,4 s | 11,98 | Natural |
| 2 | 2 | 1.533 | 138 | 1,1 s | 12,7 s | 11,74 | Natural |
| 1 | 3 | 2.557 | 169 | 1,9 s | 16,0 s | 11,88 | Natural |
| 2 | 3 | 2.557 | 122 | 1,8 s | 12,1 s | 11,75 | Natural |
| 1 | 4 | 3.581 | 168 | 1,0 s | 15,3 s | 11,66 | Natural |
| 2 | 4 | 3.580 | 185 | 1,1 s | 16,8 s | 11,72 | Natural |
| 1 | 5 | 4.605 | 159 | 1,2 s | 14,8 s | 11,68 | Natural |
| 2 | 5 | 4.605 | 137 | 1,1 s | 12,9 s | 11,53 | Natural |
| 1 | 6 | 5.629 | 211 | 1,9 s | 19,8 s | 11,71 | Natural |
| 2 | 6 | 5.629 | 147 | 1,8 s | 14,5 s | 11,55 | Natural |
| 1 | 7 | 6.653 | 224 | 1,0 s | 20,0 s | 11,69 | Natural |
| 2 | 7 | 6.653 | 135 | 1,1 s | 12,8 s | 11,45 | Natural |
| 1 | 8 | 7.677 | 140 | 1,1 s | 13,4 s | 11,33 | Natural |
| 2 | 8 | 7.677 | 163 | 1,3 s | 15,4 s | 11,48 | Natural |
| 1 | 9 | 8.701 | 158 | 2,2 s | 15,8 s | 11,51 | Natural |
| 2 | 9 | 8.701 | 114 | 2,1 s | 12,1 s | 11,35 | Natural |
| 1 | 10 | 9.725 | 179 | 1,3 s | 16,9 s | 11,37 | Natural |
| 2 | 10 | 9.725 | 144 | 1,4 s | 14,1 s | 11,25 | Natural |
| 1 | 11 | 10.749 | 214 | 1,1 s | 19,8 s | 11,43 | Natural |
| 2 | 11 | 10.749 | 135 | 1,3 s | 13,3 s | 11,18 | Natural |
| 1 | 12 | 11.772 | 137 | 2,2 s | 14,3 s | 11,16 | Natural |
| 2 | 12 | 11.773 | 163 | 2,2 s | 16,6 s | 11,23 | Natural |
| 1 | 13 | 12.797 | 158 | 1,4 s | 15,3 s | 11,27 | Natural |
| 2 | 13 | 12.797 | 114 | 1,3 s | 11,5 s | 11,05 | Natural |
| 1 | 14 | 13.820 | 175 | 1,2 s | 16,9 s | 11,12 | Natural |
| 2 | 14 | 13.821 | 145 | 1,1 s | 14,3 s | 10,94 | Natural |
| 1 | 15 | 14.845 | 208 | 1,3 s | 19,9 s | 11,14 | Natural |
| 2 | 15 | 14.845 | 136 | 1,5 s | 13,9 s | 10,89 | Natural |
| 1 | 16 | 15.869 | 130 | 2,1 s | 14,0 s | 10,83 | Natural |
| 2 | 16 | 15.869 | 163 | 2,1 s | 16,8 s | 11,02 | Natural |
| 1 | 17 | 16.893 | 159 | 1,2 s | 15,6 s | 11,03 | Natural |
| 2 | 17 | 16.893 | 114 | 1,1 s | 11,7 s | 10,75 | Natural |
| 1 | 18 | 17.917 | 165 | 1,5 s | 16,6 s | 10,82 | Natural |
| 2 | 18 | 17.917 | 145 | 1,3 s | 14,8 s | 10,64 | Natural |
| 1 | 19 | 18.941 | 205 | 2,1 s | 20,7 s | 10,97 | Natural |
| 2 | 19 | 18.941 | 137 | 2,2 s | 14,9 s | 10,65 | Natural |
| 1 | 20 | 19.965 | 124 | 1,6 s | 13,2 s | 10,59 | Natural |
| 2 | 20 | 19.965 | 163 | 1,5 s | 16,5 s | 10,79 | Natural |
| 1 | 21 | 20.989 | 155 | 1,5 s | 15,7 s | 10,80 | Natural |
| 2 | 21 | 20.989 | 114 | 1,3 s | 12,1 s | 10,47 | Natural |
| 1 | 22 | 22.013 | 162 | 2,4 s | 17,7 s | 10,56 | Natural |
| 2 | 22 | 22.013 | 145 | 2,4 s | 16,1 s | 10,48 | Natural |
| 1 | 23 | 23.037 | 198 | 1,5 s | 19,9 s | 10,70 | Natural |
| 2 | 23 | 23.036 | 136 | 1,6 s | 14,6 s | 10,40 | Natural |
| 1 | 24 | 24.061 | 124 | 1,3 s | 13,3 s | 10,28 | Natural |
| 2 | 24 | 24.061 | 163 | 1,5 s | 16,8 s | 10,59 | Natural |
| 1 | 25 | 25.085 | 153 | 1,8 s | 16,4 s | 10,45 | Natural |
| 2 | 25 | 25.085 | 114 | 2,1 s | 13,1 s | 10,28 | Natural |
| 1 | 26 | 26.109 | 162 | 2,4 s | 18,0 s | 10,33 | Natural |
| 2 | 26 | 26.109 | 145 | 2,3 s | 16,4 s | 10,22 | Natural |
| 1 | 27 | 27.133 | 196 | 1,3 s | 19,9 s | 10,47 | Natural |
| 2 | 27 | 27.133 | 136 | 1,5 s | 14,7 s | 10,17 | Natural |
| 1 | 28 | 28.157 | 123 | 1,7 s | 13,8 s | 10,12 | Natural |
| 2 | 28 | 28.156 | 163 | 1,5 s | 17,2 s | 10,30 | Natural |
| 1 | 29 | 29.180 | 152 | 2,3 s | 16,9 s | 10,34 | Natural |
| 2 | 29 | 29.181 | 114 | 2,4 s | 13,6 s | 10,06 | Natural |
| 1 | 30 | 30.205 | 161 | 1,4 s | 17,3 s | 10,11 | Natural |
| 2 | 30 | 30.204 | 145 | 1,3 s | 15,7 s | 9,97 | Natural |
| 1 | 31 | 31.228 | 197 | 1,5 s | 20,6 s | 10,25 | Natural |
| 2 | 31 | 31.229 | 135 | 1,7 s | 15,2 s | 9,94 | Natural |
| 1 | 32 | 32.252 | 123 | 2,4 s | 14,7 s | 9,90 | Natural |
| 2 | 32 | 32.252 | 163 | 2,3 s | 18,2 s | 10,18 | Natural |
| 1 | 33 | 33.277 | 152 | 1,6 s | 16,6 s | 10,09 | Natural |
| 2 | 33 | 33.277 | 114 | 1,8 s | 13,3 s | 9,84 | Natural |
| 1 | 34 | 34.301 | 161 | 1,7 s | 18,2 s | 9,68 | Natural |
| 2 | 34 | 34.301 | 145 | 1,5 s | 16,6 s | 9,52 | Natural |
| 1 | 35 | 35.325 | 196 | 2,7 s | 22,0 s | 10,10 | Natural |
| 2 | 35 | 35.325 | 136 | 2,6 s | 16,5 s | 9,73 | Natural |
| 1 | 36 | 36.349 | 129 | 1,6 s | 14,9 s | 9,65 | Natural |
| 2 | 36 | 36.349 | 163 | 1,8 s | 18,1 s | 9,93 | Natural |
| 1 | 37 | 37.373 | 156 | 1,7 s | 17,2 s | 9,97 | Natural |
| 2 | 37 | 37.373 | 114 | 1,5 s | 13,3 s | 9,58 | Natural |
| 1 | 38 | 38.397 | 168 | 2,3 s | 19,4 s | 9,74 | Natural |
| 2 | 38 | 38.397 | 145 | 2,0 s | 17,2 s | 9,49 | Natural |
| 1 | 39 | 39.421 | 203 | 2,7 s | 23,0 s | 9,95 | Natural |
| 2 | 39 | 39.421 | 135 | 2,6 s | 16,6 s | 9,52 | Natural |
| 1 | 40 | 40.445 | 126 | 1,5 s | 14,8 s | 9,44 | Natural |
| 2 | 40 | 40.445 | 163 | 1,7 s | 18,3 s | 9,77 | Natural |
| 1 | 41 | 41.469 | 154 | 1,9 s | 17,6 s | 9,76 | Natural |
| 2 | 41 | 41.468 | 114 | 1,7 s | 13,8 s | 9,33 | Natural |
| 1 | 42 | 42.492 | 165 | 2,6 s | 19,9 s | 9,53 | Natural |
| 2 | 42 | 42.493 | 145 | 2,6 s | 17,9 s | 9,38 | Natural |
| 1 | 43 | 43.517 | 200 | 1,5 s | 21,9 s | 9,72 | Natural |
| 2 | 43 | 43.517 | 136 | 1,6 s | 16,1 s | 9,33 | Natural |
| 1 | 44 | 44.541 | 130 | 1,9 s | 15,8 s | 9,27 | Natural |
| 2 | 44 | 44.541 | 163 | 1,7 s | 18,8 s | 9,47 | Natural |
| 1 | 45 | 45.565 | 156 | 2,7 s | 18,8 s | 9,60 | Natural |
| 2 | 45 | 45.564 | 114 | 2,6 s | 14,8 s | 9,25 | Natural |
| 1 | 46 | 46.589 | 170 | 2,0 s | 20,0 s | 9,38 | Natural |
| 2 | 46 | 46.589 | 145 | 1,8 s | 17,6 s | 9,15 | Natural |
| 1 | 47 | 47.613 | 204 | 1,9 s | 23,0 s | 9,61 | Natural |
| 2 | 47 | 47.613 | 135 | 1,7 s | 16,4 s | 9,09 | Natural |
| 1 | 48 | 48.637 | 128 | 2,8 s | 16,8 s | 9,11 | Natural |
| 2 | 48 | 48.637 | 163 | 2,9 s | 20,2 s | 9,38 | Natural |
| 1 | 49 | 49.661 | 156 | 1,8 s | 18,3 s | 9,38 | Natural |
| 2 | 49 | 49.661 | 114 | 1,9 s | 14,4 s | 9,05 | Natural |
| 1 | 50 | 50.685 | 168 | 1,7 s | 20,0 s | 9,13 | Natural |
| 2 | 50 | 50.685 | 145 | 1,9 s | 17,9 s | 9,00 | Natural |
| 1 | 51 | 51.709 | 203 | 1,9 s | 23,6 s | 9,32 | Natural |
| 2 | 51 | 51.708 | 137 | 2,2 s | 17,4 s | 8,95 | Natural |
| 1 | 52 | 52.733 | 131 | 3,0 s | 17,6 s | 8,91 | Natural |
| 2 | 52 | 52.733 | 163 | 2,8 s | 20,5 s | 9,16 | Natural |
| 1 | 53 | 53.757 | 156 | 1,6 s | 18,5 s | 9,21 | Natural |
| 2 | 53 | 53.757 | 114 | 1,8 s | 14,5 s | 8,87 | Natural |
| 1 | 54 | 54.781 | 171 | 2,1 s | 20,9 s | 9,03 | Natural |
| 2 | 54 | 54.781 | 145 | 1,9 s | 18,3 s | 8,74 | Natural |
| 1 | 55 | 55.805 | 208 | 2,9 s | 25,2 s | 9,28 | Natural |
| 2 | 55 | 55.805 | 136 | 2,8 s | 18,2 s | 8,79 | Natural |
| 1 | 56 | 56.829 | 129 | 1,8 s | 16,5 s | 8,74 | Natural |
| 2 | 56 | 56.829 | 163 | 1,7 s | 19,7 s | 8,98 | Natural |
| 1 | 57 | 57.853 | 156 | 1,9 s | 19,1 s | 9,01 | Natural |
| 2 | 57 | 57.853 | 114 | 2,1 s | 15,1 s | 8,70 | Natural |
| 1 | 58 | 58.877 | 168 | 3,2 s | 22,1 s | 8,85 | Natural |
| 2 | 58 | 58.877 | 145 | 3,1 s | 19,7 s | 8,66 | Natural |
| 1 | 59 | 59.901 | 204 | 2,1 s | 24,4 s | 9,11 | Natural |
| 2 | 59 | 59.900 | 136 | 1,9 s | 17,7 s | 8,59 | Natural |
| 1 | 60 | 60.925 | 131 | 1,9 s | 17,1 s | 8,51 | Natural |
| 2 | 60 | 60.925 | 163 | 2,1 s | 20,4 s | 8,86 | Natural |
| 1 | 61 | 61.949 | 156 | 3,1 s | 20,4 s | 8,94 | Natural |
| 2 | 61 | 61.949 | 114 | 3,2 s | 16,4 s | 8,54 | Natural |
| 1 | 62 | 62.973 | 171 | 2,1 s | 21,6 s | 8,72 | Natural |
| 2 | 62 | 62.972 | 145 | 1,9 s | 18,9 s | 8,49 | Natural |
| 1 | 63 | 63.997 | 208 | 2,1 s | 25,1 s | 8,98 | Natural |
| 2 | 63 | 63.996 | 136 | 1,8 s | 17,9 s | 8,40 | Natural |
| 1 | 64 | 65.021 | 131 | 2,4 s | 17,9 s | 8,41 | Natural |
| 2 | 64 | 65.021 | 163 | 2,1 s | 20,9 s | 8,59 | Natural |
| 1 | 65 | 66.045 | 157 | 3,0 s | 20,8 s | 8,78 | Natural |
| 2 | 65 | 66.045 | 114 | 3,2 s | 16,6 s | 8,37 | Natural |
| 1 | 66 | 67.068 | 171 | 2,0 s | 21,9 s | 8,56 | Natural |
| 2 | 66 | 67.069 | 145 | 1,8 s | 19,2 s | 8,30 | Natural |
| 1 | 67 | 68.093 | 206 | 2,4 s | 25,6 s | 8,82 | Natural |
| 2 | 67 | 68.093 | 137 | 2,1 s | 18,6 s | 8,21 | Natural |
| 1 | 68 | 69.117 | 129 | 3,2 s | 18,7 s | 8,25 | Natural |
| 2 | 68 | 69.117 | 163 | 3,1 s | 22,0 s | 8,55 | Natural |
| 1 | 69 | 70.141 | 156 | 2,2 s | 20,2 s | 8,58 | Natural |
| 2 | 69 | 70.141 | 114 | 2,4 s | 16,1 s | 8,23 | Natural |
| 1 | 70 | 71.165 | 168 | 2,4 s | 22,3 s | 8,39 | Natural |
| 2 | 70 | 71.165 | 144 | 2,1 s | 19,8 s | 8,10 | Natural |
| 1 | 71 | 72.189 | 203 | 3,4 s | 26,7 s | 8,66 | Natural |
| 2 | 71 | 72.188 | 136 | 3,3 s | 19,8 s | 8,15 | Natural |
| 1 | 72 | 73.213 | 128 | 2,1 s | 17,8 s | 8,07 | Natural |
| 2 | 72 | 73.213 | 163 | 2,3 s | 21,5 s | 8,44 | Natural |
| 1 | 73 | 74.237 | 159 | 2,3 s | 20,8 s | 8,52 | Natural |
| 2 | 73 | 74.237 | 114 | 2,1 s | 16,2 s | 8,01 | Natural |
| 1 | 74 | 75.261 | 164 | 2,6 s | 22,8 s | 8,09 | Natural |
| 2 | 74 | 75.261 | 145 | 3,0 s | 20,9 s | 8,03 | Natural |
| 1 | 75 | 76.285 | 200 | 3,5 s | 26,9 s | 8,52 | Natural |
| 2 | 75 | 76.284 | 135 | 3,3 s | 20,1 s | 7,98 | Natural |
| 1 | 76 | 77.309 | 131 | 2,3 s | 18,6 s | 7,96 | Natural |
| 2 | 76 | 77.309 | 163 | 2,0 s | 21,8 s | 8,21 | Natural |
| 1 | 77 | 78.333 | 160 | 2,7 s | 21,6 s | 8,39 | Natural |
| 2 | 77 | 78.333 | 114 | 2,3 s | 16,8 s | 7,80 | Natural |
| 1 | 78 | 79.357 | 164 | 3,4 s | 23,6 s | 8,07 | Natural |
| 2 | 78 | 79.357 | 145 | 3,3 s | 21,6 s | 7,89 | Natural |
| 1 | 79 | 80.381 | 201 | 2,0 s | 26,0 s | 8,33 | Natural |
| 2 | 79 | 80.380 | 136 | 2,2 s | 19,4 s | 7,85 | Natural |
| 1 | 80 | 81.405 | 130 | 2,6 s | 19,1 s | 7,83 | Natural |
| 2 | 80 | 81.405 | 163 | 2,3 s | 22,4 s | 8,05 | Natural |
| 1 | 81 | 82.429 | 160 | 3,5 s | 22,7 s | 8,26 | Natural |
| 2 | 81 | 82.429 | 114 | 3,3 s | 17,8 s | 7,79 | Natural |
| 1 | 82 | 83.453 | 164 | 2,5 s | 23,0 s | 7,94 | Natural |
| 2 | 82 | 83.453 | 144 | 2,3 s | 20,8 s | 7,71 | Natural |
| 1 | 83 | 84.476 | 201 | 2,3 s | 26,8 s | 8,16 | Natural |
| 2 | 83 | 84.477 | 137 | 2,6 s | 20,2 s | 7,72 | Natural |
| 1 | 84 | 85.501 | 131 | 3,4 s | 20,3 s | 7,69 | Natural |
| 2 | 84 | 85.501 | 163 | 2,8 s | 23,5 s | 7,84 | Natural |
| 1 | 85 | 86.525 | 161 | 2,4 s | 22,1 s | 8,14 | Natural |
| 2 | 85 | 86.525 | 114 | 2,3 s | 17,1 s | 7,63 | Natural |
| 1 | 86 | 87.549 | 165 | 2,2 s | 23,4 s | 7,74 | Natural |
| 2 | 86 | 87.549 | 145 | 2,5 s | 21,4 s | 7,62 | Natural |
| 1 | 87 | 88.573 | 202 | 3,2 s | 28,0 s | 8,13 | Natural |
| 2 | 87 | 88.573 | 137 | 2,8 s | 21,0 s | 7,49 | Natural |
| 1 | 88 | 89.597 | 130 | 3,6 s | 20,7 s | 7,54 | Natural |
| 2 | 88 | 89.597 | 163 | 3,8 s | 24,3 s | 7,88 | Natural |
| 1 | 89 | 90.621 | 161 | 2,5 s | 22,5 s | 8,02 | Natural |
| 2 | 89 | 90.621 | 114 | 2,3 s | 17,4 s | 7,47 | Natural |
| 1 | 90 | 91.645 | 165 | 2,8 s | 24,1 s | 7,69 | Natural |
| 2 | 90 | 91.645 | 144 | 2,5 s | 21,8 s | 7,40 | Natural |
| 1 | 91 | 92.669 | 202 | 3,7 s | 28,8 s | 8,01 | Natural |
| 2 | 91 | 92.669 | 136 | 3,6 s | 21,7 s | 7,47 | Natural |
| 1 | 92 | 93.693 | 132 | 2,2 s | 19,9 s | 7,40 | Natural |
| 2 | 92 | 93.693 | 163 | 2,4 s | 23,3 s | 7,75 | Natural |
| 1 | 93 | 94.717 | 161 | 2,5 s | 23,0 s | 7,80 | Natural |
| 2 | 93 | 94.717 | 114 | 2,8 s | 18,1 s | 7,41 | Natural |
| 1 | 94 | 95.741 | 165 | 3,8 s | 25,4 s | 7,59 | Natural |
| 2 | 94 | 95.741 | 144 | 3,1 s | 22,9 s | 7,22 | Natural |
| 1 | 95 | 96.765 | 202 | 2,5 s | 28,1 s | 7,84 | Natural |
| 2 | 95 | 96.765 | 136 | 2,7 s | 21,1 s | 7,34 | Natural |
| 1 | 96 | 97.789 | 131 | 2,7 s | 20,5 s | 7,31 | Natural |
| 2 | 96 | 97.789 | 163 | 2,4 s | 23,9 s | 7,56 | Natural |
| 1 | 97 | 98.813 | 162 | 3,9 s | 24,5 s | 7,78 | Natural |
| 2 | 97 | 98.813 | 114 | 3,8 s | 19,2 s | 7,30 | Natural |
| 1 | 98 | 99.837 | 166 | 2,7 s | 24,8 s | 7,46 | Natural |
| 2 | 98 | 99.837 | 145 | 2,5 s | 22,4 s | 7,23 | Natural |
| 1 | 99 | 100.861 | 203 | 2,7 s | 28,6 s | 7,79 | Natural |
| 2 | 99 | 100.861 | 135 | 2,4 s | 21,1 s | 7,17 | Natural |
| 1 | 100 | 101.885 | 133 | 3,1 s | 21,5 s | 7,18 | Natural |
| 2 | 100 | 101.885 | 163 | 2,7 s | 24,7 s | 7,38 | Natural |
| 1 | 101 | 102.909 | 163 | 3,9 s | 25,1 s | 7,64 | Natural |
| 2 | 101 | 102.909 | 114 | 4,1 s | 19,8 s | 7,16 | Natural |
| 1 | 102 | 103.933 | 166 | 2,6 s | 25,6 s | 7,19 | Natural |
| 2 | 102 | 103.933 | 145 | 2,4 s | 23,1 s | 6,95 | Natural |
| 1 | 103 | 104.956 | 204 | 2,6 s | 29,4 s | 7,58 | Natural |
| 2 | 103 | 104.957 | 136 | 3,0 s | 22,0 s | 7,10 | Natural |
| 1 | 104 | 105.981 | 133 | 3,9 s | 22,5 s | 7,08 | Natural |
| 2 | 104 | 105.981 | 163 | 4,0 s | 25,9 s | 7,38 | Natural |
| 1 | 105 | 107.005 | 163 | 2,4 s | 24,0 s | 7,50 | Natural |
| 2 | 105 | 107.005 | 114 | 2,6 s | 18,6 s | 7,05 | Natural |
| 1 | 106 | 108.029 | 166 | 2,7 s | 25,8 s | 7,15 | Natural |
| 2 | 106 | 108.029 | 145 | 3,0 s | 23,5 s | 7,03 | Natural |
| 1 | 107 | 109.053 | 204 | 3,8 s | 30,8 s | 7,54 | Natural |
| 2 | 107 | 109.053 | 137 | 4,0 s | 23,4 s | 6,99 | Natural |
| 1 | 108 | 110.077 | 133 | 2,8 s | 21,7 s | 6,97 | Natural |
| 2 | 108 | 110.077 | 163 | 2,6 s | 25,0 s | 7,22 | Natural |
| 1 | 109 | 111.101 | 163 | 2,6 s | 24,6 s | 7,38 | Natural |
| 2 | 109 | 111.101 | 114 | 2,9 s | 19,2 s | 6,95 | Natural |
| 1 | 110 | 112.125 | 167 | 4,1 s | 27,4 s | 7,12 | Natural |
| 2 | 110 | 112.125 | 146 | 4,0 s | 24,9 s | 6,92 | Natural |
| 1 | 111 | 113.149 | 206 | 2,7 s | 30,1 s | 7,48 | Natural |
| 2 | 111 | 113.149 | 135 | 2,6 s | 22,1 s | 6,87 | Natural |
| 1 | 112 | 114.173 | 133 | 2,9 s | 22,1 s | 6,86 | Natural |
| 2 | 112 | 114.172 | 163 | 2,6 s | 25,4 s | 7,10 | Natural |
| 1 | 113 | 115.197 | 163 | 3,4 s | 25,4 s | 7,35 | Natural |
| 2 | 113 | 115.197 | 114 | 2,9 s | 19,8 s | 6,71 | Natural |
| 1 | 114 | 116.220 | 167 | 4,2 s | 27,9 s | 7,01 | Natural |
| 2 | 114 | 116.221 | 146 | 4,1 s | 25,4 s | 6,80 | Natural |
| 1 | 115 | 117.245 | 205 | 2,8 s | 30,5 s | 7,36 | Natural |
| 2 | 115 | 117.245 | 137 | 2,5 s | 22,7 s | 6,75 | Natural |
| 1 | 116 | 118.268 | 133 | 2,8 s | 22,7 s | 6,67 | Natural |
| 2 | 116 | 118.269 | 163 | 3,3 s | 26,2 s | 7,06 | Natural |
| 1 | 117 | 119.293 | 164 | 4,3 s | 26,7 s | 7,26 | Natural |
| 2 | 117 | 119.293 | 114 | 4,1 s | 20,9 s | 6,73 | Natural |
| 1 | 118 | 120.317 | 167 | 3,1 s | 27,1 s | 6,92 | Natural |
| 2 | 118 | 120.317 | 145 | 2,8 s | 24,5 s | 6,66 | Natural |
| 1 | 119 | 121.341 | 206 | 3,2 s | 31,5 s | 7,26 | Natural |
| 2 | 119 | 121.341 | 136 | 2,9 s | 23,3 s | 6,60 | Natural |
| 1 | 120 | 122.365 | 134 | 4,1 s | 24,1 s | 6,66 | Natural |
| 2 | 120 | 122.365 | 163 | 3,4 s | 27,2 s | 6,81 | Natural |
| 1 | 121 | 123.389 | 163 | 3,0 s | 25,6 s | 7,15 | Natural |
| 2 | 121 | 123.389 | 114 | 2,7 s | 19,9 s | 6,60 | Natural |
| 1 | 122 | 124.413 | 167 | 3,1 s | 27,5 s | 6,83 | Natural |
| 2 | 122 | 124.413 | 145 | 2,8 s | 24,8 s | 6,56 | Natural |
| 1 | 123 | 125.437 | 205 | 3,9 s | 32,4 s | 7,16 | Natural |
| 2 | 123 | 125.437 | 137 | 3,4 s | 24,5 s | 6,47 | Natural |
| 1 | 124 | 126.461 | 135 | 4,4 s | 24,9 s | 6,55 | Natural |
| 2 | 124 | 126.461 | 163 | 4,6 s | 28,2 s | 6,85 | Natural |
| 1 | 125 | 127.485 | 164 | 3,1 s | 26,2 s | 7,07 | Natural |
| 2 | 125 | 127.485 | 114 | 2,8 s | 20,2 s | 6,48 | Natural |
| 1 | 126 | 128.509 | 168 | 3,6 s | 28,3 s | 6,75 | Natural |
| 2 | 126 | 128.508 | 144 | 3,1 s | 25,4 s | 6,42 | Natural |
| 1 | 127 | 129.533 | 206 | 4,3 s | 33,4 s | 7,05 | Natural |
| 2 | 127 | 129.533 | 137 | 4,5 s | 25,5 s | 6,49 | Natural |
| 1 | 128 | 130.557 | 134 | 3,0 s | 23,5 s | 6,47 | Natural |
| 2 | 128 | 130.557 | 163 | 2,7 s | 26,8 s | 6,71 | Natural |
| 1 | 129 | 131.581 | 164 | 3,5 s | 26,9 s | 6,97 | Natural |
| 2 | 129 | 131.580 | 114 | 3,1 s | 20,9 s | 6,34 | Natural |
| 1 | 130 | 132.605 | 168 | 4,5 s | 29,6 s | 6,65 | Natural |
| 2 | 130 | 132.604 | 145 | 3,7 s | 26,6 s | 6,27 | Natural |
| 1 | 131 | 133.629 | 206 | 3,0 s | 32,5 s | 6,94 | Natural |
| 2 | 131 | 133.629 | 136 | 3,3 s | 24,4 s | 6,40 | Natural |
| 1 | 132 | 134.653 | 133 | 3,5 s | 24,2 s | 6,37 | Natural |
| 2 | 132 | 134.653 | 163 | 3,1 s | 27,7 s | 6,60 | Natural |
| 1 | 133 | 135.677 | 164 | 2,5 s | 28,3 s | 6,33 | Natural |
| 2 | 133 | 135.677 | 114 | 5,0 s | 22,8 s | 6,36 | Natural |
| 1 | 134 | 136.701 | 168 | 5,3 s | 30,7 s | 6,59 | Natural |
| 2 | 134 | 136.701 | 145 | 1,6 s | 27,3 s | 5,61 | Natural |
| 1 | 135 | 137.725 | — | — s | 120,5 s | — | Sin respuesta visible / error |
| 2 | 135 | 137.725 | — | — s | 120,2 s | — | Sin respuesta visible / error |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
