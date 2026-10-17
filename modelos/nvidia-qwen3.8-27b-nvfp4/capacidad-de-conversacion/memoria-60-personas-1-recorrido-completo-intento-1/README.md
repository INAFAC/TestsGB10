# 1 persona · 60% de memoria

[Volver a la capacidad por memoria](../README.md)

**Cumplió durante todo el recorrido.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **257/257 previstas**. Duración: **273,6 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.533–16.893 | 16/16 | 1,0 s | 1,0 s | 11,68 tokens/s | 21,3 s | Cumple |
| 18-33 | 17.917–33.277 | 16/16 | 1,2 s | 1,2 s | 11,09 tokens/s | 23,2 s | Cumple |
| 34-49 | 34.301–49.661 | 16/16 | 1,3 s | 1,3 s | 10,56 tokens/s | 24,7 s | Cumple |
| 50-65 | 50.685–66.045 | 16/16 | 1,6 s | 1,6 s | 10,08 tokens/s | 25,9 s | Cumple |
| 66-81 | 67.069–82.429 | 16/16 | 1,7 s | 1,7 s | 9,65 tokens/s | 27,3 s | Cumple |
| 82-97 | 83.452–98.813 | 16/16 | 1,9 s | 1,9 s | 9,26 tokens/s | 29,9 s | Cumple |
| 98-113 | 99.837–115.197 | 16/16 | 2,1 s | 2,1 s | 8,87 tokens/s | 32,5 s | Cumple |
| 114-129 | 116.221–131.580 | 16/16 | 2,3 s | 2,3 s | 8,54 tokens/s | 36,2 s | Cumple |
| 130-145 | 132.605–147.965 | 16/16 | 2,5 s | 2,5 s | 8,22 tokens/s | 39,0 s | Cumple |
| 146-161 | 148.988–164.349 | 16/16 | 2,7 s | 2,7 s | 7,92 tokens/s | 41,9 s | Cumple |
| 162-177 | 165.373–180.733 | 16/16 | 3,0 s | 3,0 s | 7,49 tokens/s | 44,7 s | Cumple |
| 178-193 | 181.757–197.116 | 16/16 | 3,1 s | 3,1 s | 7,40 tokens/s | 47,9 s | Cumple |
| 194-209 | 198.140–213.501 | 16/16 | 3,3 s | 3,3 s | 7,16 tokens/s | 51,3 s | Cumple |
| 210-225 | 214.525–229.885 | 16/16 | 3,6 s | 3,6 s | 6,93 tokens/s | 54,7 s | Cumple |
| 226-241 | 230.909–246.269 | 16/16 | 3,7 s | 3,7 s | 6,72 tokens/s | 58,3 s | Cumple |
| 242-257 | 247.293–262.013 | 16/16 | 3,9 s | 3,9 s | 6,54 tokens/s | 61,8 s | Cumple |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 257 | 262.026 | 99,955% | 118 |

El objetivo del cierre deja aproximadamente 128 tokens para la respuesta y pide terminar en diez palabras. El presupuesto efectivo se calcula con la entrada real. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento llegó al cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 60% |
| Pico de memoria del motor / GB10 | 56,7% |
| Pico de memoria total del sistema / GB10 | 65,6% |
| Pico de caché | 34,5% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 1,9 s |
| Espera media al primer token, incluido razonamiento | 1,9 s |
| Tiempo medio de petición completa | 33,5 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 4,11 tokens/s |
| Suma de tiempos individuales de petición | 8.605,3 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 257/257 | 1,9 s | 33,5 s | 16.412,9 s | 4,11 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 173 | 0,2 s | 14,2 s | 12,35 | Natural |
| 1 | 2 | 1.533 | 157 | 0,6 s | 13,3 s | 12,31 | Natural |
| 1 | 3 | 2.557 | 178 | 0,8 s | 15,3 s | 12,23 | Natural |
| 1 | 4 | 3.581 | 163 | 0,6 s | 13,8 s | 12,20 | Natural |
| 1 | 5 | 4.605 | 216 | 0,6 s | 18,3 s | 12,16 | Natural |
| 1 | 6 | 5.629 | 192 | 0,9 s | 16,6 s | 12,12 | Natural |
| 1 | 7 | 6.653 | 243 | 0,6 s | 20,6 s | 12,08 | Natural |
| 1 | 8 | 7.677 | 217 | 0,7 s | 18,6 s | 12,04 | Natural |
| 1 | 9 | 8.701 | 212 | 0,9 s | 18,5 s | 11,99 | Natural |
| 1 | 10 | 9.725 | 197 | 0,6 s | 17,0 s | 11,96 | Natural |
| 1 | 11 | 10.748 | 242 | 0,7 s | 20,9 s | 11,91 | Natural |
| 1 | 12 | 11.773 | 216 | 0,9 s | 19,0 s | 11,88 | Natural |
| 1 | 13 | 12.797 | 221 | 0,6 s | 19,2 s | 11,84 | Natural |
| 1 | 14 | 13.821 | 195 | 0,7 s | 17,1 s | 11,80 | Natural |
| 1 | 15 | 14.845 | 242 | 0,8 s | 21,3 s | 11,76 | Natural |
| 1 | 16 | 15.869 | 191 | 1,0 s | 17,2 s | 11,72 | Natural |
| 1 | 17 | 16.893 | 221 | 0,7 s | 19,5 s | 11,68 | Natural |
| 1 | 18 | 17.917 | 169 | 0,8 s | 15,2 s | 11,65 | Natural |
| 1 | 19 | 18.941 | 242 | 1,0 s | 21,8 s | 11,60 | Natural |
| 1 | 20 | 19.965 | 180 | 0,7 s | 16,1 s | 11,57 | Natural |
| 1 | 21 | 20.989 | 215 | 0,8 s | 19,3 s | 11,53 | Natural |
| 1 | 22 | 22.013 | 164 | 1,0 s | 15,2 s | 11,49 | Natural |
| 1 | 23 | 23.037 | 237 | 0,7 s | 21,3 s | 11,46 | Natural |
| 1 | 24 | 24.061 | 198 | 0,8 s | 18,0 s | 11,42 | Natural |
| 1 | 25 | 25.085 | 222 | 0,9 s | 20,3 s | 11,38 | Natural |
| 1 | 26 | 26.109 | 176 | 1,1 s | 16,5 s | 11,34 | Natural |
| 1 | 27 | 27.133 | 246 | 0,8 s | 22,4 s | 11,31 | Natural |
| 1 | 28 | 28.157 | 198 | 0,9 s | 18,4 s | 11,27 | Natural |
| 1 | 29 | 29.181 | 224 | 1,2 s | 21,0 s | 11,23 | Natural |
| 1 | 30 | 30.205 | 174 | 0,8 s | 16,2 s | 11,20 | Natural |
| 1 | 31 | 31.228 | 250 | 0,9 s | 23,2 s | 11,16 | Natural |
| 1 | 32 | 32.253 | 210 | 1,1 s | 19,9 s | 11,13 | Natural |
| 1 | 33 | 33.277 | 228 | 0,8 s | 21,3 s | 11,09 | Natural |
| 1 | 34 | 34.301 | 184 | 0,9 s | 17,4 s | 11,06 | Natural |
| 1 | 35 | 35.325 | 256 | 1,1 s | 24,3 s | 11,02 | Natural |
| 1 | 36 | 36.349 | 202 | 0,8 s | 19,1 s | 10,99 | Natural |
| 1 | 37 | 37.373 | 228 | 0,9 s | 21,6 s | 10,95 | Natural |
| 1 | 38 | 38.397 | 184 | 1,0 s | 17,7 s | 10,92 | Natural |
| 1 | 39 | 39.420 | 256 | 1,3 s | 24,7 s | 10,88 | Natural |
| 1 | 40 | 40.444 | 208 | 0,9 s | 20,0 s | 10,85 | Natural |
| 1 | 41 | 41.469 | 228 | 1,0 s | 22,0 s | 10,82 | Natural |
| 1 | 42 | 42.493 | 182 | 1,3 s | 18,1 s | 10,79 | Natural |
| 1 | 43 | 43.517 | 256 | 0,9 s | 24,6 s | 10,75 | Natural |
| 1 | 44 | 44.541 | 203 | 1,0 s | 19,8 s | 10,73 | Natural |
| 1 | 45 | 45.565 | 225 | 1,3 s | 22,2 s | 10,69 | Natural |
| 1 | 46 | 46.589 | 179 | 0,9 s | 17,6 s | 10,66 | Natural |
| 1 | 47 | 47.613 | 251 | 1,0 s | 24,5 s | 10,62 | Natural |
| 1 | 48 | 48.637 | 202 | 1,3 s | 20,3 s | 10,60 | Natural |
| 1 | 49 | 49.661 | 224 | 0,9 s | 22,0 s | 10,56 | Natural |
| 1 | 50 | 50.685 | 178 | 1,0 s | 17,8 s | 10,54 | Natural |
| 1 | 51 | 51.709 | 249 | 1,1 s | 24,8 s | 10,50 | Natural |
| 1 | 52 | 52.733 | 208 | 1,4 s | 21,2 s | 10,47 | Natural |
| 1 | 53 | 53.757 | 226 | 1,0 s | 22,5 s | 10,44 | Natural |
| 1 | 54 | 54.781 | 182 | 1,2 s | 18,5 s | 10,42 | Natural |
| 1 | 55 | 55.805 | 254 | 1,5 s | 25,8 s | 10,38 | Natural |
| 1 | 56 | 56.828 | 210 | 1,0 s | 21,2 s | 10,35 | Natural |
| 1 | 57 | 57.853 | 228 | 1,1 s | 23,4 s | 10,19 | Natural |
| 1 | 58 | 58.877 | 184 | 1,4 s | 19,2 s | 10,29 | Natural |
| 1 | 59 | 59.901 | 255 | 1,0 s | 25,7 s | 10,26 | Natural |
| 1 | 60 | 60.925 | 207 | 1,1 s | 21,3 s | 10,23 | Natural |
| 1 | 61 | 61.949 | 227 | 1,4 s | 23,5 s | 10,20 | Natural |
| 1 | 62 | 62.973 | 182 | 1,0 s | 18,7 s | 10,17 | Natural |
| 1 | 63 | 63.997 | 253 | 1,1 s | 25,9 s | 10,14 | Natural |
| 1 | 64 | 65.021 | 203 | 1,2 s | 21,2 s | 10,12 | Natural |
| 1 | 65 | 66.045 | 225 | 1,6 s | 23,8 s | 10,08 | Natural |
| 1 | 66 | 67.069 | 179 | 1,1 s | 18,8 s | 10,07 | Natural |
| 1 | 67 | 68.093 | 251 | 1,3 s | 26,2 s | 10,03 | Natural |
| 1 | 68 | 69.116 | 202 | 1,5 s | 21,6 s | 10,01 | Natural |
| 1 | 69 | 70.141 | 224 | 1,1 s | 23,4 s | 9,98 | Natural |
| 1 | 70 | 71.165 | 178 | 1,2 s | 19,0 s | 9,95 | Natural |
| 1 | 71 | 72.189 | 249 | 1,5 s | 26,5 s | 9,92 | Natural |
| 1 | 72 | 73.213 | 202 | 1,1 s | 21,4 s | 9,90 | Natural |
| 1 | 73 | 74.237 | 216 | 1,3 s | 23,0 s | 9,87 | Natural |
| 1 | 74 | 75.261 | 178 | 1,4 s | 19,4 s | 9,85 | Natural |
| 1 | 75 | 76.285 | 250 | 1,7 s | 27,1 s | 9,81 | Natural |
| 1 | 76 | 77.309 | 208 | 1,2 s | 22,4 s | 9,79 | Natural |
| 1 | 77 | 78.333 | 226 | 1,4 s | 24,4 s | 9,76 | Natural |
| 1 | 78 | 79.357 | 182 | 1,7 s | 20,3 s | 9,74 | Natural |
| 1 | 79 | 80.381 | 254 | 1,2 s | 27,3 s | 9,70 | Natural |
| 1 | 80 | 81.404 | 213 | 1,4 s | 23,3 s | 9,68 | Natural |
| 1 | 81 | 82.429 | 229 | 1,7 s | 25,3 s | 9,65 | Natural |
| 1 | 82 | 83.452 | 186 | 1,2 s | 20,4 s | 9,64 | Natural |
| 1 | 83 | 84.477 | 258 | 1,4 s | 28,1 s | 9,60 | Natural |
| 1 | 84 | 85.501 | 217 | 1,8 s | 24,3 s | 9,58 | Natural |
| 1 | 85 | 86.525 | 231 | 1,2 s | 25,3 s | 9,55 | Natural |
| 1 | 86 | 87.549 | 189 | 1,4 s | 21,1 s | 9,54 | Natural |
| 1 | 87 | 88.572 | 261 | 1,5 s | 28,9 s | 9,50 | Natural |
| 1 | 88 | 89.597 | 220 | 1,9 s | 25,0 s | 9,47 | Natural |
| 1 | 89 | 90.620 | 233 | 1,3 s | 25,9 s | 9,45 | Natural |
| 1 | 90 | 91.644 | 192 | 1,5 s | 21,8 s | 9,43 | Natural |
| 1 | 91 | 92.669 | 264 | 1,9 s | 29,9 s | 9,40 | Natural |
| 1 | 92 | 93.692 | 225 | 1,4 s | 25,3 s | 9,37 | Natural |
| 1 | 93 | 94.717 | 235 | 1,5 s | 26,5 s | 9,35 | Natural |
| 1 | 94 | 95.741 | 195 | 1,9 s | 22,7 s | 9,34 | Natural |
| 1 | 95 | 96.765 | 267 | 1,3 s | 29,9 s | 9,30 | Natural |
| 1 | 96 | 97.789 | 229 | 1,5 s | 26,1 s | 9,28 | Natural |
| 1 | 97 | 98.813 | 237 | 1,9 s | 27,4 s | 9,26 | Natural |
| 1 | 98 | 99.837 | 198 | 1,3 s | 22,6 s | 9,24 | Natural |
| 1 | 99 | 100.861 | 270 | 1,4 s | 30,7 s | 9,20 | Natural |
| 1 | 100 | 101.885 | 233 | 1,6 s | 26,9 s | 9,18 | Natural |
| 1 | 101 | 102.909 | 239 | 2,0 s | 28,0 s | 9,16 | Natural |
| 1 | 102 | 103.933 | 201 | 1,4 s | 23,3 s | 9,14 | Natural |
| 1 | 103 | 104.957 | 273 | 1,6 s | 31,5 s | 9,11 | Natural |
| 1 | 104 | 105.981 | 237 | 2,1 s | 28,0 s | 9,09 | Natural |
| 1 | 105 | 107.005 | 241 | 1,4 s | 27,8 s | 9,06 | Natural |
| 1 | 106 | 108.029 | 203 | 1,6 s | 23,9 s | 9,05 | Natural |
| 1 | 107 | 109.053 | 276 | 2,0 s | 32,5 s | 9,02 | Natural |
| 1 | 108 | 110.077 | 241 | 1,4 s | 28,1 s | 9,00 | Natural |
| 1 | 109 | 111.101 | 243 | 1,6 s | 28,6 s | 8,97 | Natural |
| 1 | 110 | 112.125 | 207 | 2,0 s | 25,0 s | 8,96 | Natural |
| 1 | 111 | 113.148 | 279 | 1,3 s | 32,5 s | 8,92 | Natural |
| 1 | 112 | 114.173 | 245 | 1,5 s | 29,0 s | 8,90 | Natural |
| 1 | 113 | 115.197 | 246 | 1,7 s | 29,3 s | 8,87 | Natural |
| 1 | 114 | 116.221 | 210 | 2,2 s | 25,8 s | 8,86 | Natural |
| 1 | 115 | 117.245 | 282 | 1,6 s | 33,4 s | 8,84 | Natural |
| 1 | 116 | 118.269 | 249 | 1,8 s | 29,9 s | 8,82 | Natural |
| 1 | 117 | 119.293 | 247 | 2,1 s | 30,1 s | 8,79 | Natural |
| 1 | 118 | 120.317 | 213 | 1,5 s | 25,6 s | 8,77 | Natural |
| 1 | 119 | 121.341 | 285 | 1,7 s | 34,2 s | 8,75 | Natural |
| 1 | 120 | 122.365 | 253 | 2,1 s | 31,0 s | 8,73 | Natural |
| 1 | 121 | 123.389 | 249 | 1,5 s | 30,0 s | 8,70 | Natural |
| 1 | 122 | 124.413 | 216 | 1,7 s | 26,5 s | 8,69 | Natural |
| 1 | 123 | 125.437 | 288 | 2,0 s | 35,1 s | 8,66 | Natural |
| 1 | 124 | 126.461 | 257 | 2,3 s | 31,9 s | 8,64 | Natural |
| 1 | 125 | 127.485 | 251 | 1,7 s | 30,6 s | 8,62 | Natural |
| 1 | 126 | 128.509 | 219 | 1,9 s | 27,2 s | 8,60 | Natural |
| 1 | 127 | 129.533 | 291 | 2,3 s | 36,2 s | 8,57 | Natural |
| 1 | 128 | 130.557 | 261 | 1,7 s | 32,0 s | 8,56 | Natural |
| 1 | 129 | 131.580 | 253 | 2,0 s | 31,4 s | 8,54 | Natural |
| 1 | 130 | 132.605 | 222 | 2,3 s | 28,2 s | 8,52 | Natural |
| 1 | 131 | 133.629 | 294 | 1,6 s | 36,1 s | 8,50 | Natural |
| 1 | 132 | 134.652 | 265 | 1,8 s | 33,0 s | 8,48 | Natural |
| 1 | 133 | 135.677 | 255 | 2,4 s | 32,4 s | 8,46 | Natural |
| 1 | 134 | 136.701 | 225 | 1,6 s | 28,1 s | 8,44 | Natural |
| 1 | 135 | 137.725 | 297 | 1,9 s | 37,1 s | 8,41 | Natural |
| 1 | 136 | 138.749 | 269 | 2,0 s | 33,9 s | 8,40 | Natural |
| 1 | 137 | 139.773 | 257 | 2,5 s | 33,0 s | 8,38 | Natural |
| 1 | 138 | 140.797 | 228 | 1,8 s | 28,9 s | 8,36 | Natural |
| 1 | 139 | 141.821 | 299 | 2,0 s | 37,8 s | 8,33 | Natural |
| 1 | 140 | 142.845 | 273 | 2,5 s | 35,2 s | 8,32 | Natural |
| 1 | 141 | 143.869 | 259 | 1,8 s | 32,9 s | 8,30 | Natural |
| 1 | 142 | 144.892 | 231 | 2,0 s | 29,8 s | 8,28 | Natural |
| 1 | 143 | 145.917 | 303 | 2,4 s | 39,0 s | 8,26 | Natural |
| 1 | 144 | 146.941 | 277 | 1,7 s | 35,2 s | 8,24 | Natural |
| 1 | 145 | 147.965 | 261 | 2,0 s | 33,6 s | 8,22 | Natural |
| 1 | 146 | 148.988 | 234 | 2,4 s | 30,8 s | 8,20 | Natural |
| 1 | 147 | 150.013 | 306 | 1,7 s | 39,0 s | 8,18 | Natural |
| 1 | 148 | 151.037 | 281 | 1,9 s | 36,2 s | 8,16 | Natural |
| 1 | 149 | 152.061 | 263 | 2,1 s | 34,3 s | 8,14 | Natural |
| 1 | 150 | 153.084 | 237 | 2,6 s | 31,7 s | 8,13 | Natural |
| 1 | 151 | 154.108 | 308 | 1,9 s | 39,8 s | 8,11 | Natural |
| 1 | 152 | 155.133 | 285 | 2,2 s | 37,3 s | 8,09 | Natural |
| 1 | 153 | 156.157 | 265 | 2,7 s | 35,4 s | 8,07 | Natural |
| 1 | 154 | 157.181 | 239 | 1,8 s | 31,4 s | 8,05 | Natural |
| 1 | 155 | 158.205 | 312 | 2,1 s | 40,8 s | 8,03 | Natural |
| 1 | 156 | 159.229 | 289 | 2,6 s | 38,5 s | 8,02 | Natural |
| 1 | 157 | 160.253 | 267 | 1,8 s | 35,1 s | 8,00 | Natural |
| 1 | 158 | 161.276 | 243 | 2,1 s | 32,4 s | 7,98 | Natural |
| 1 | 159 | 162.301 | 314 | 2,6 s | 41,9 s | 7,96 | Natural |
| 1 | 160 | 163.325 | 293 | 1,7 s | 38,5 s | 7,94 | Natural |
| 1 | 161 | 164.349 | 269 | 2,0 s | 35,8 s | 7,92 | Natural |
| 1 | 162 | 165.373 | 246 | 2,3 s | 33,2 s | 7,91 | Natural |
| 1 | 163 | 166.397 | 318 | 2,8 s | 43,0 s | 7,89 | Natural |
| 1 | 164 | 167.421 | 297 | 2,0 s | 39,6 s | 7,87 | Natural |
| 1 | 165 | 168.444 | 271 | 2,3 s | 36,6 s | 7,86 | Natural |
| 1 | 166 | 169.469 | 249 | 2,7 s | 34,3 s | 7,84 | Natural |
| 1 | 167 | 170.493 | 321 | 1,9 s | 42,8 s | 7,82 | Natural |
| 1 | 168 | 171.517 | 301 | 2,2 s | 40,6 s | 7,80 | Natural |
| 1 | 169 | 172.541 | 273 | 2,7 s | 37,6 s | 7,79 | Natural |
| 1 | 170 | 173.564 | 252 | 1,9 s | 34,2 s | 7,78 | Natural |
| 1 | 171 | 174.589 | 323 | 2,2 s | 43,7 s | 7,75 | Natural |
| 1 | 172 | 175.613 | 305 | 2,5 s | 41,8 s | 7,74 | Natural |
| 1 | 173 | 176.637 | 275 | 3,0 s | 38,4 s | 7,72 | Natural |
| 1 | 174 | 177.661 | 255 | 2,1 s | 35,1 s | 7,70 | Natural |
| 1 | 175 | 178.685 | 326 | 2,4 s | 44,7 s | 7,68 | Natural |
| 1 | 176 | 179.709 | 309 | 3,0 s | 44,1 s | 7,49 | Natural |
| 1 | 177 | 180.733 | 277 | 2,1 s | 38,2 s | 7,65 | Natural |
| 1 | 178 | 181.757 | 258 | 2,4 s | 36,0 s | 7,64 | Natural |
| 1 | 179 | 182.781 | 329 | 2,9 s | 45,9 s | 7,62 | Natural |
| 1 | 180 | 183.805 | 312 | 2,0 s | 42,9 s | 7,60 | Natural |
| 1 | 181 | 184.829 | 277 | 2,3 s | 38,7 s | 7,59 | Natural |
| 1 | 182 | 185.853 | 261 | 2,9 s | 37,3 s | 7,57 | Natural |
| 1 | 183 | 186.877 | 333 | 2,0 s | 46,0 s | 7,55 | Natural |
| 1 | 184 | 187.901 | 317 | 2,3 s | 44,3 s | 7,54 | Natural |
| 1 | 185 | 188.925 | 281 | 2,5 s | 39,7 s | 7,52 | Natural |
| 1 | 186 | 189.949 | 264 | 3,1 s | 38,1 s | 7,51 | Natural |
| 1 | 187 | 190.973 | 336 | 2,2 s | 47,0 s | 7,48 | Natural |
| 1 | 188 | 191.997 | 321 | 2,5 s | 45,4 s | 7,47 | Natural |
| 1 | 189 | 193.021 | 283 | 3,1 s | 40,9 s | 7,46 | Natural |
| 1 | 190 | 194.045 | 267 | 2,2 s | 38,0 s | 7,45 | Natural |
| 1 | 191 | 195.069 | 339 | 2,4 s | 47,9 s | 7,43 | Natural |
| 1 | 192 | 196.092 | 324 | 3,0 s | 46,6 s | 7,41 | Natural |
| 1 | 193 | 197.116 | 285 | 2,1 s | 40,5 s | 7,40 | Natural |
| 1 | 194 | 198.140 | 270 | 2,4 s | 38,9 s | 7,38 | Natural |
| 1 | 195 | 199.165 | 342 | 3,0 s | 49,3 s | 7,36 | Natural |
| 1 | 196 | 200.189 | 329 | 2,1 s | 46,8 s | 7,35 | Natural |
| 1 | 197 | 201.213 | 287 | 2,3 s | 41,3 s | 7,34 | Natural |
| 1 | 198 | 202.237 | 273 | 2,6 s | 39,8 s | 7,32 | Natural |
| 1 | 199 | 203.261 | 345 | 3,2 s | 50,3 s | 7,30 | Natural |
| 1 | 200 | 204.284 | 332 | 2,3 s | 47,7 s | 7,29 | Natural |
| 1 | 201 | 205.308 | 289 | 2,6 s | 42,2 s | 7,27 | Natural |
| 1 | 202 | 206.333 | 276 | 3,3 s | 41,2 s | 7,25 | Natural |
| 1 | 203 | 207.356 | 348 | 2,2 s | 50,1 s | 7,24 | Natural |
| 1 | 204 | 208.381 | 337 | 2,6 s | 49,0 s | 7,23 | Natural |
| 1 | 205 | 209.404 | 291 | 3,1 s | 43,3 s | 7,22 | Natural |
| 1 | 206 | 210.428 | 279 | 2,2 s | 40,8 s | 7,20 | Natural |
| 1 | 207 | 211.453 | 351 | 2,6 s | 51,3 s | 7,18 | Natural |
| 1 | 208 | 212.477 | 341 | 3,2 s | 50,6 s | 7,17 | Natural |
| 1 | 209 | 213.501 | 293 | 2,1 s | 42,9 s | 7,16 | Natural |
| 1 | 210 | 214.525 | 282 | 2,4 s | 41,8 s | 7,14 | Natural |
| 1 | 211 | 215.549 | 354 | 2,8 s | 52,3 s | 7,13 | Natural |
| 1 | 212 | 216.572 | 345 | 3,4 s | 51,8 s | 7,11 | Natural |
| 1 | 213 | 217.597 | 295 | 2,4 s | 43,8 s | 7,10 | Natural |
| 1 | 214 | 218.621 | 285 | 2,8 s | 42,9 s | 7,09 | Natural |
| 1 | 215 | 219.645 | 357 | 3,3 s | 53,7 s | 7,07 | Natural |
| 1 | 216 | 220.669 | 349 | 2,3 s | 51,7 s | 7,06 | Natural |
| 1 | 217 | 221.692 | 297 | 2,7 s | 44,7 s | 7,04 | Natural |
| 1 | 218 | 222.717 | 288 | 3,3 s | 44,1 s | 7,03 | Natural |
| 1 | 219 | 223.741 | 359 | 2,3 s | 53,4 s | 7,01 | Natural |
| 1 | 220 | 224.765 | 352 | 2,7 s | 52,8 s | 7,00 | Natural |
| 1 | 221 | 225.789 | 299 | 3,1 s | 45,7 s | 6,99 | Natural |
| 1 | 222 | 226.813 | 291 | 3,5 s | 45,1 s | 6,98 | Natural |
| 1 | 223 | 227.836 | 363 | 2,5 s | 54,7 s | 6,95 | Natural |
| 1 | 224 | 228.861 | 357 | 2,9 s | 54,2 s | 6,94 | Natural |
| 1 | 225 | 229.885 | 301 | 3,6 s | 46,9 s | 6,93 | Natural |
| 1 | 226 | 230.909 | 294 | 2,6 s | 44,9 s | 6,92 | Natural |
| 1 | 227 | 231.933 | 365 | 2,9 s | 55,7 s | 6,90 | Natural |
| 1 | 228 | 232.956 | 361 | 3,4 s | 55,7 s | 6,89 | Natural |
| 1 | 229 | 233.981 | 303 | 2,4 s | 46,3 s | 6,88 | Natural |
| 1 | 230 | 235.005 | 297 | 2,8 s | 45,9 s | 6,87 | Natural |
| 1 | 231 | 236.028 | 369 | 3,4 s | 57,2 s | 6,85 | Natural |
| 1 | 232 | 237.053 | 365 | 2,4 s | 55,7 s | 6,84 | Natural |
| 1 | 233 | 238.077 | 305 | 2,8 s | 47,3 s | 6,83 | Natural |
| 1 | 234 | 239.100 | 300 | 3,0 s | 46,9 s | 6,81 | Natural |
| 1 | 235 | 240.125 | 372 | 3,7 s | 58,3 s | 6,80 | Natural |
| 1 | 236 | 241.149 | 369 | 2,7 s | 56,9 s | 6,78 | Natural |
| 1 | 237 | 242.173 | 307 | 3,0 s | 48,2 s | 6,78 | Natural |
| 1 | 238 | 243.196 | 303 | 3,7 s | 48,4 s | 6,76 | Natural |
| 1 | 239 | 244.221 | 374 | 2,6 s | 58,0 s | 6,74 | Natural |
| 1 | 240 | 245.245 | 373 | 2,9 s | 58,2 s | 6,73 | Natural |
| 1 | 241 | 246.269 | 309 | 3,6 s | 49,4 s | 6,72 | Natural |
| 1 | 242 | 247.293 | 306 | 2,5 s | 47,9 s | 6,71 | Natural |
| 1 | 243 | 248.317 | 378 | 2,9 s | 59,2 s | 6,69 | Natural |
| 1 | 244 | 249.341 | 377 | 3,6 s | 59,9 s | 6,68 | Natural |
| 1 | 245 | 250.364 | 311 | 2,5 s | 49,0 s | 6,67 | Natural |
| 1 | 246 | 251.389 | 309 | 2,7 s | 49,0 s | 6,66 | Natural |
| 1 | 247 | 252.413 | 381 | 3,2 s | 60,4 s | 6,64 | Natural |
| 1 | 248 | 253.437 | 381 | 3,8 s | 61,2 s | 6,63 | Natural |
| 1 | 249 | 254.460 | 313 | 2,8 s | 49,9 s | 6,62 | Natural |
| 1 | 250 | 255.485 | 312 | 3,2 s | 50,2 s | 6,61 | Natural |
| 1 | 251 | 256.509 | 383 | 3,9 s | 61,8 s | 6,59 | Natural |
| 1 | 252 | 257.533 | 385 | 2,6 s | 61,0 s | 6,58 | Natural |
| 1 | 253 | 258.557 | 315 | 3,0 s | 50,8 s | 6,57 | Natural |
| 1 | 254 | 259.581 | 315 | 3,7 s | 51,6 s | 6,56 | Natural |
| 1 | 255 | 260.605 | 387 | 2,6 s | 61,6 s | 6,54 | Natural |
| 1 | 256 | 261.117 | 375 | 2,3 s | 59,5 s | 6,54 | Natural |
| 1 | 257 | 262.013 | 13 | 2,5 s | 4,2 s | 6,99 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
