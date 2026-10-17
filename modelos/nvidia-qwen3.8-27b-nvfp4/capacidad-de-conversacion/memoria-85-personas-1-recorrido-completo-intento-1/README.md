# 1 persona · 85% de memoria

[Volver a la capacidad por memoria](../README.md)

**Cumplió durante todo el recorrido.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **257/257 previstas**. Duración: **293,2 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.533–16.893 | 16/16 | 1,2 s | 1,2 s | 11,69 tokens/s | 19,7 s | Cumple |
| 18-33 | 17.916–33.277 | 16/16 | 1,2 s | 1,2 s | 11,07 tokens/s | 21,4 s | Cumple |
| 34-49 | 34.301–49.660 | 16/16 | 1,4 s | 1,4 s | 10,26 tokens/s | 23,3 s | Cumple |
| 50-65 | 50.685–66.045 | 16/16 | 1,7 s | 1,7 s | 9,98 tokens/s | 25,7 s | Cumple |
| 66-81 | 67.069–82.429 | 16/16 | 1,8 s | 1,8 s | 9,50 tokens/s | 29,3 s | Cumple |
| 82-97 | 83.453–98.813 | 16/16 | 2,0 s | 2,0 s | 9,00 tokens/s | 33,5 s | Cumple |
| 98-113 | 99.837–115.197 | 16/16 | 2,2 s | 2,2 s | 8,58 tokens/s | 38,0 s | Cumple |
| 114-129 | 116.221–131.581 | 16/16 | 2,7 s | 2,7 s | 8,25 tokens/s | 43,8 s | Cumple |
| 130-145 | 132.605–147.965 | 16/16 | 2,9 s | 2,9 s | 7,73 tokens/s | 48,6 s | Cumple |
| 146-161 | 148.989–164.349 | 16/16 | 3,2 s | 3,2 s | 7,50 tokens/s | 51,5 s | Cumple |
| 162-177 | 165.373–180.733 | 16/16 | 3,6 s | 3,6 s | 7,18 tokens/s | 54,9 s | Cumple |
| 178-193 | 181.757–197.117 | 16/16 | 3,9 s | 3,9 s | 6,92 tokens/s | 57,9 s | Cumple |
| 194-209 | 198.141–213.501 | 16/16 | 4,1 s | 4,1 s | 6,63 tokens/s | 61,2 s | Cumple |
| 210-225 | 214.525–229.885 | 16/16 | 4,5 s | 4,5 s | 6,41 tokens/s | 63,7 s | Cumple |
| 226-241 | 230.909–246.269 | 16/16 | 4,7 s | 4,7 s | 6,20 tokens/s | 67,1 s | Cumple |
| 242-257 | 247.293–262.012 | 16/16 | 4,9 s | 4,9 s | 6,02 tokens/s | 71,2 s | Cumple |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 257 | 262.029 | 99,956% | 115 |

El cierre previsto reserva hasta 128 tokens y pide terminar en diez palabras. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento llegó al cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 85% |
| Pico de memoria del motor / GB10 | 81,8% |
| Pico de memoria total del sistema / GB10 | 90,6% |
| Pico de caché | 21,0% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 2,3 s |
| Espera media al primer token, incluido razonamiento | 2,3 s |
| Tiempo medio de petición completa | 38,1 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 4,13 tokens/s |
| Suma de tiempos individuales de petición | 9.787,3 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 257/257 | 2,3 s | 38,1 s | 17.593,8 s | 4,13 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 162 | 0,2 s | 13,3 s | 12,32 | Natural |
| 1 | 2 | 1.533 | 198 | 0,6 s | 16,7 s | 12,28 | Natural |
| 1 | 3 | 2.557 | 184 | 0,8 s | 15,7 s | 12,27 | Natural |
| 1 | 4 | 3.581 | 173 | 0,5 s | 14,6 s | 12,23 | Natural |
| 1 | 5 | 4.605 | 187 | 0,6 s | 15,9 s | 12,18 | Natural |
| 1 | 6 | 5.629 | 207 | 0,8 s | 17,8 s | 12,15 | Natural |
| 1 | 7 | 6.653 | 227 | 0,6 s | 19,3 s | 12,09 | Natural |
| 1 | 8 | 7.677 | 159 | 0,7 s | 13,8 s | 12,07 | Natural |
| 1 | 9 | 8.701 | 224 | 1,1 s | 19,7 s | 12,01 | Natural |
| 1 | 10 | 9.725 | 201 | 0,6 s | 17,3 s | 11,98 | Natural |
| 1 | 11 | 10.749 | 211 | 0,7 s | 18,3 s | 11,93 | Natural |
| 1 | 12 | 11.773 | 155 | 1,2 s | 14,1 s | 11,90 | Natural |
| 1 | 13 | 12.797 | 221 | 0,6 s | 19,1 s | 11,85 | Natural |
| 1 | 14 | 13.821 | 196 | 0,7 s | 17,2 s | 11,81 | Natural |
| 1 | 15 | 14.845 | 209 | 0,8 s | 18,4 s | 11,76 | Natural |
| 1 | 16 | 15.869 | 153 | 1,0 s | 13,9 s | 11,74 | Natural |
| 1 | 17 | 16.893 | 223 | 0,7 s | 19,7 s | 11,69 | Natural |
| 1 | 18 | 17.916 | 195 | 0,8 s | 17,4 s | 11,65 | Natural |
| 1 | 19 | 18.940 | 210 | 1,0 s | 19,0 s | 11,62 | Natural |
| 1 | 20 | 19.965 | 153 | 0,7 s | 13,8 s | 11,56 | Natural |
| 1 | 21 | 20.988 | 223 | 0,8 s | 20,0 s | 11,53 | Natural |
| 1 | 22 | 22.013 | 193 | 1,0 s | 17,7 s | 11,49 | Natural |
| 1 | 23 | 23.036 | 217 | 0,7 s | 19,5 s | 11,46 | Natural |
| 1 | 24 | 24.061 | 157 | 0,8 s | 14,5 s | 11,41 | Natural |
| 1 | 25 | 25.085 | 225 | 0,9 s | 20,6 s | 11,38 | Natural |
| 1 | 26 | 26.109 | 195 | 1,1 s | 18,2 s | 11,34 | Natural |
| 1 | 27 | 27.133 | 220 | 0,8 s | 20,2 s | 11,31 | Natural |
| 1 | 28 | 28.157 | 162 | 0,9 s | 15,2 s | 11,26 | Natural |
| 1 | 29 | 29.181 | 228 | 1,1 s | 21,4 s | 11,23 | Natural |
| 1 | 30 | 30.205 | 200 | 0,8 s | 18,6 s | 11,18 | Natural |
| 1 | 31 | 31.229 | 225 | 0,9 s | 21,0 s | 11,15 | Natural |
| 1 | 32 | 32.253 | 164 | 1,2 s | 15,8 s | 11,12 | Natural |
| 1 | 33 | 33.277 | 229 | 0,8 s | 21,4 s | 11,07 | Natural |
| 1 | 34 | 34.301 | 204 | 0,9 s | 19,3 s | 11,04 | Natural |
| 1 | 35 | 35.325 | 227 | 1,2 s | 21,8 s | 10,99 | Natural |
| 1 | 36 | 36.349 | 162 | 0,8 s | 15,5 s | 10,97 | Natural |
| 1 | 37 | 37.372 | 227 | 0,9 s | 21,6 s | 10,91 | Natural |
| 1 | 38 | 38.396 | 200 | 1,0 s | 19,3 s | 10,89 | Natural |
| 1 | 39 | 39.421 | 225 | 1,3 s | 22,0 s | 10,84 | Natural |
| 1 | 40 | 40.444 | 164 | 0,9 s | 16,0 s | 10,82 | Natural |
| 1 | 41 | 41.469 | 228 | 1,0 s | 22,1 s | 10,76 | Natural |
| 1 | 42 | 42.493 | 203 | 1,3 s | 20,1 s | 10,74 | Natural |
| 1 | 43 | 43.517 | 226 | 0,9 s | 21,9 s | 10,69 | Natural |
| 1 | 44 | 44.541 | 164 | 1,0 s | 16,3 s | 10,65 | Natural |
| 1 | 45 | 45.565 | 228 | 1,4 s | 22,7 s | 10,63 | Natural |
| 1 | 46 | 46.588 | 202 | 0,9 s | 19,9 s | 10,58 | Natural |
| 1 | 47 | 47.613 | 227 | 1,0 s | 22,4 s | 10,56 | Natural |
| 1 | 48 | 48.637 | 167 | 1,3 s | 17,1 s | 10,52 | Natural |
| 1 | 49 | 49.660 | 230 | 1,0 s | 23,3 s | 10,26 | Natural |
| 1 | 50 | 50.685 | 204 | 1,0 s | 20,4 s | 10,44 | Natural |
| 1 | 51 | 51.708 | 230 | 1,2 s | 23,1 s | 10,41 | Natural |
| 1 | 52 | 52.733 | 171 | 1,5 s | 17,8 s | 10,40 | Natural |
| 1 | 53 | 53.757 | 232 | 1,0 s | 23,3 s | 10,35 | Natural |
| 1 | 54 | 54.781 | 208 | 1,2 s | 21,2 s | 10,33 | Natural |
| 1 | 55 | 55.805 | 234 | 1,5 s | 24,1 s | 10,28 | Natural |
| 1 | 56 | 56.829 | 177 | 1,0 s | 18,2 s | 10,25 | Natural |
| 1 | 57 | 57.853 | 235 | 1,2 s | 24,0 s | 10,24 | Natural |
| 1 | 58 | 58.877 | 213 | 1,5 s | 22,3 s | 10,18 | Natural |
| 1 | 59 | 59.901 | 240 | 1,0 s | 24,6 s | 10,15 | Natural |
| 1 | 60 | 60.925 | 183 | 1,2 s | 19,1 s | 10,14 | Natural |
| 1 | 61 | 61.949 | 238 | 1,7 s | 25,2 s | 10,09 | Natural |
| 1 | 62 | 62.973 | 218 | 1,0 s | 22,5 s | 10,08 | Natural |
| 1 | 63 | 63.997 | 246 | 1,1 s | 25,5 s | 10,02 | Natural |
| 1 | 64 | 65.021 | 189 | 1,3 s | 20,1 s | 9,99 | Natural |
| 1 | 65 | 66.045 | 241 | 1,6 s | 25,7 s | 9,98 | Natural |
| 1 | 66 | 67.069 | 223 | 1,1 s | 23,5 s | 9,94 | Natural |
| 1 | 67 | 68.093 | 252 | 1,3 s | 26,7 s | 9,88 | Natural |
| 1 | 68 | 69.116 | 195 | 1,6 s | 21,3 s | 9,86 | Natural |
| 1 | 69 | 70.140 | 244 | 1,1 s | 25,9 s | 9,78 | Natural |
| 1 | 70 | 71.165 | 227 | 1,3 s | 24,3 s | 9,81 | Natural |
| 1 | 71 | 72.189 | 258 | 1,6 s | 27,9 s | 9,78 | Natural |
| 1 | 72 | 73.213 | 201 | 1,1 s | 21,6 s | 9,75 | Natural |
| 1 | 73 | 74.236 | 247 | 1,3 s | 26,6 s | 9,72 | Natural |
| 1 | 74 | 75.261 | 233 | 1,5 s | 25,4 s | 9,70 | Natural |
| 1 | 75 | 76.285 | 263 | 1,8 s | 28,8 s | 9,68 | Natural |
| 1 | 76 | 77.309 | 207 | 1,3 s | 22,6 s | 9,64 | Natural |
| 1 | 77 | 78.332 | 250 | 1,5 s | 27,4 s | 9,61 | Natural |
| 1 | 78 | 79.357 | 238 | 1,8 s | 26,5 s | 9,58 | Natural |
| 1 | 79 | 80.381 | 269 | 1,3 s | 29,3 s | 9,57 | Natural |
| 1 | 80 | 81.405 | 213 | 1,5 s | 23,7 s | 9,53 | Natural |
| 1 | 81 | 82.429 | 253 | 1,8 s | 28,3 s | 9,50 | Natural |
| 1 | 82 | 83.453 | 243 | 1,2 s | 26,8 s | 9,47 | Natural |
| 1 | 83 | 84.477 | 276 | 1,4 s | 30,6 s | 9,44 | Natural |
| 1 | 84 | 85.500 | 219 | 1,8 s | 24,9 s | 9,44 | Natural |
| 1 | 85 | 86.525 | 256 | 1,2 s | 28,4 s | 9,38 | Natural |
| 1 | 86 | 87.549 | 248 | 1,4 s | 27,8 s | 9,36 | Natural |
| 1 | 87 | 88.573 | 282 | 1,6 s | 31,7 s | 9,33 | Natural |
| 1 | 88 | 89.597 | 225 | 2,0 s | 26,4 s | 9,20 | Natural |
| 1 | 89 | 90.621 | 259 | 1,4 s | 29,3 s | 9,23 | Natural |
| 1 | 90 | 91.645 | 253 | 1,6 s | 28,9 s | 9,22 | Natural |
| 1 | 91 | 92.669 | 288 | 2,0 s | 33,1 s | 9,21 | Natural |
| 1 | 92 | 93.693 | 231 | 1,4 s | 26,6 s | 9,14 | Natural |
| 1 | 93 | 94.717 | 262 | 1,5 s | 30,0 s | 9,16 | Natural |
| 1 | 94 | 95.741 | 257 | 2,0 s | 30,0 s | 9,14 | Natural |
| 1 | 95 | 96.765 | 294 | 1,4 s | 33,5 s | 9,12 | Natural |
| 1 | 96 | 97.789 | 237 | 1,6 s | 27,6 s | 9,09 | Natural |
| 1 | 97 | 98.813 | 265 | 2,0 s | 31,3 s | 9,00 | Natural |
| 1 | 98 | 99.837 | 263 | 1,4 s | 30,5 s | 9,00 | Natural |
| 1 | 99 | 100.860 | 299 | 1,5 s | 34,6 s | 9,01 | Natural |
| 1 | 100 | 101.885 | 243 | 1,8 s | 28,8 s | 8,97 | Natural |
| 1 | 101 | 102.909 | 268 | 2,2 s | 32,3 s | 8,87 | Natural |
| 1 | 102 | 103.933 | 268 | 1,6 s | 31,5 s | 8,95 | Natural |
| 1 | 103 | 104.957 | 306 | 1,8 s | 36,1 s | 8,90 | Natural |
| 1 | 104 | 105.980 | 249 | 2,2 s | 30,2 s | 8,87 | Natural |
| 1 | 105 | 107.005 | 271 | 1,5 s | 32,1 s | 8,84 | Natural |
| 1 | 106 | 108.029 | 272 | 1,8 s | 32,5 s | 8,81 | Natural |
| 1 | 107 | 109.052 | 312 | 2,2 s | 37,5 s | 8,79 | Natural |
| 1 | 108 | 110.077 | 255 | 1,6 s | 30,5 s | 8,77 | Natural |
| 1 | 109 | 111.100 | 274 | 1,8 s | 33,0 s | 8,74 | Natural |
| 1 | 110 | 112.125 | 278 | 2,2 s | 34,0 s | 8,72 | Natural |
| 1 | 111 | 113.149 | 318 | 1,5 s | 38,0 s | 8,67 | Natural |
| 1 | 112 | 114.173 | 261 | 1,7 s | 31,7 s | 8,65 | Natural |
| 1 | 113 | 115.197 | 277 | 2,0 s | 34,1 s | 8,58 | Natural |
| 1 | 114 | 116.221 | 283 | 2,4 s | 35,2 s | 8,61 | Natural |
| 1 | 115 | 117.245 | 324 | 1,7 s | 39,4 s | 8,58 | Natural |
| 1 | 116 | 118.268 | 267 | 2,0 s | 33,1 s | 8,56 | Natural |
| 1 | 117 | 119.293 | 281 | 2,4 s | 35,2 s | 8,54 | Natural |
| 1 | 118 | 120.317 | 288 | 1,7 s | 35,4 s | 8,52 | Natural |
| 1 | 119 | 121.341 | 330 | 1,9 s | 40,7 s | 8,49 | Natural |
| 1 | 120 | 122.365 | 273 | 2,4 s | 34,7 s | 8,43 | Natural |
| 1 | 121 | 123.389 | 283 | 1,7 s | 35,2 s | 8,42 | Natural |
| 1 | 122 | 124.413 | 293 | 2,0 s | 37,0 s | 8,34 | Natural |
| 1 | 123 | 125.437 | 336 | 2,3 s | 42,5 s | 8,35 | Natural |
| 1 | 124 | 126.461 | 279 | 2,6 s | 36,2 s | 8,27 | Natural |
| 1 | 125 | 127.485 | 286 | 1,9 s | 36,0 s | 8,35 | Natural |
| 1 | 126 | 128.509 | 298 | 2,2 s | 37,9 s | 8,32 | Natural |
| 1 | 127 | 129.532 | 342 | 2,7 s | 43,8 s | 8,30 | Natural |
| 1 | 128 | 130.557 | 285 | 1,9 s | 36,2 s | 8,27 | Natural |
| 1 | 129 | 131.581 | 289 | 2,2 s | 37,1 s | 8,25 | Natural |
| 1 | 130 | 132.605 | 303 | 2,7 s | 39,4 s | 8,23 | Natural |
| 1 | 131 | 133.629 | 348 | 1,9 s | 44,3 s | 8,18 | Natural |
| 1 | 132 | 134.653 | 291 | 2,2 s | 37,7 s | 8,18 | Natural |
| 1 | 133 | 135.677 | 292 | 2,7 s | 38,4 s | 8,16 | Natural |
| 1 | 134 | 136.701 | 308 | 1,9 s | 39,6 s | 8,13 | Natural |
| 1 | 135 | 137.725 | 353 | 2,2 s | 45,6 s | 8,11 | Natural |
| 1 | 136 | 138.749 | 297 | 2,4 s | 39,0 s | 8,08 | Natural |
| 1 | 137 | 139.773 | 295 | 2,9 s | 39,5 s | 8,04 | Natural |
| 1 | 138 | 140.797 | 313 | 2,1 s | 40,9 s | 8,04 | Natural |
| 1 | 139 | 141.821 | 360 | 2,4 s | 47,2 s | 8,01 | Natural |
| 1 | 140 | 142.845 | 300 | 2,9 s | 41,0 s | 7,85 | Natural |
| 1 | 141 | 143.869 | 296 | 2,1 s | 39,2 s | 7,96 | Natural |
| 1 | 142 | 144.893 | 314 | 2,3 s | 41,7 s | 7,94 | Natural |
| 1 | 143 | 145.917 | 363 | 2,9 s | 48,6 s | 7,92 | Natural |
| 1 | 144 | 146.941 | 300 | 2,1 s | 40,8 s | 7,73 | Natural |
| 1 | 145 | 147.965 | 296 | 2,4 s | 40,4 s | 7,77 | Natural |
| 1 | 146 | 148.989 | 315 | 3,0 s | 43,7 s | 7,72 | Natural |
| 1 | 147 | 150.013 | 363 | 2,0 s | 48,4 s | 7,81 | Natural |
| 1 | 148 | 151.037 | 301 | 2,2 s | 40,7 s | 7,81 | Natural |
| 1 | 149 | 152.061 | 297 | 2,5 s | 40,6 s | 7,78 | Natural |
| 1 | 150 | 153.084 | 314 | 3,1 s | 43,5 s | 7,76 | Natural |
| 1 | 151 | 154.108 | 364 | 2,2 s | 49,2 s | 7,72 | Natural |
| 1 | 152 | 155.133 | 301 | 2,6 s | 41,5 s | 7,72 | Natural |
| 1 | 153 | 156.157 | 297 | 3,2 s | 41,8 s | 7,67 | Natural |
| 1 | 154 | 157.181 | 315 | 2,2 s | 43,1 s | 7,67 | Natural |
| 1 | 155 | 158.205 | 363 | 2,5 s | 50,7 s | 7,51 | Natural |
| 1 | 156 | 159.229 | 304 | 3,1 s | 43,5 s | 7,51 | Natural |
| 1 | 157 | 160.253 | 298 | 2,2 s | 41,8 s | 7,50 | Natural |
| 1 | 158 | 161.277 | 317 | 2,5 s | 44,1 s | 7,60 | Natural |
| 1 | 159 | 162.301 | 367 | 3,2 s | 51,5 s | 7,57 | Natural |
| 1 | 160 | 163.325 | 304 | 2,0 s | 42,2 s | 7,55 | Natural |
| 1 | 161 | 164.349 | 298 | 2,4 s | 41,9 s | 7,52 | Natural |
| 1 | 162 | 165.373 | 317 | 2,8 s | 45,9 s | 7,33 | Natural |
| 1 | 163 | 166.396 | 367 | 3,4 s | 52,3 s | 7,48 | Natural |
| 1 | 164 | 167.421 | 305 | 2,4 s | 43,3 s | 7,44 | Natural |
| 1 | 165 | 168.445 | 299 | 2,8 s | 42,9 s | 7,44 | Natural |
| 1 | 166 | 169.469 | 319 | 3,3 s | 46,1 s | 7,42 | Natural |
| 1 | 167 | 170.493 | 368 | 2,3 s | 52,0 s | 7,38 | Natural |
| 1 | 168 | 171.517 | 309 | 2,7 s | 44,4 s | 7,38 | Natural |
| 1 | 169 | 172.540 | 301 | 3,3 s | 44,1 s | 7,36 | Natural |
| 1 | 170 | 173.565 | 323 | 2,3 s | 46,3 s | 7,32 | Natural |
| 1 | 171 | 174.589 | 372 | 2,7 s | 53,4 s | 7,32 | Natural |
| 1 | 172 | 175.613 | 313 | 3,1 s | 46,0 s | 7,27 | Natural |
| 1 | 173 | 176.637 | 303 | 3,6 s | 45,1 s | 7,28 | Natural |
| 1 | 174 | 177.661 | 326 | 2,6 s | 47,3 s | 7,26 | Natural |
| 1 | 175 | 178.685 | 376 | 3,0 s | 54,9 s | 7,22 | Natural |
| 1 | 176 | 179.709 | 315 | 3,6 s | 47,1 s | 7,22 | Natural |
| 1 | 177 | 180.733 | 304 | 2,6 s | 44,8 s | 7,18 | Natural |
| 1 | 178 | 181.757 | 328 | 3,0 s | 48,6 s | 7,18 | Natural |
| 1 | 179 | 182.781 | 377 | 3,5 s | 56,1 s | 7,15 | Natural |
| 1 | 180 | 183.805 | 315 | 2,5 s | 46,4 s | 7,15 | Natural |
| 1 | 181 | 184.829 | 304 | 2,9 s | 45,5 s | 7,11 | Natural |
| 1 | 182 | 185.853 | 328 | 3,6 s | 49,6 s | 7,12 | Natural |
| 1 | 183 | 186.877 | 378 | 2,5 s | 55,8 s | 7,08 | Natural |
| 1 | 184 | 187.901 | 316 | 2,9 s | 47,4 s | 7,07 | Natural |
| 1 | 185 | 188.925 | 305 | 3,2 s | 46,2 s | 7,06 | Natural |
| 1 | 186 | 189.948 | 329 | 3,9 s | 50,5 s | 7,04 | Natural |
| 1 | 187 | 190.973 | 379 | 2,7 s | 56,7 s | 7,00 | Natural |
| 1 | 188 | 191.996 | 318 | 3,2 s | 48,4 s | 7,00 | Natural |
| 1 | 189 | 193.021 | 306 | 3,9 s | 47,5 s | 6,98 | Natural |
| 1 | 190 | 194.045 | 331 | 2,8 s | 50,3 s | 6,95 | Natural |
| 1 | 191 | 195.069 | 381 | 3,0 s | 57,9 s | 6,93 | Natural |
| 1 | 192 | 196.093 | 319 | 3,7 s | 49,6 s | 6,93 | Natural |
| 1 | 193 | 197.117 | 306 | 2,6 s | 46,7 s | 6,92 | Natural |
| 1 | 194 | 198.141 | 331 | 3,1 s | 50,9 s | 6,90 | Natural |
| 1 | 195 | 199.165 | 382 | 3,7 s | 59,2 s | 6,87 | Natural |
| 1 | 196 | 200.189 | 316 | 2,6 s | 48,5 s | 6,87 | Natural |
| 1 | 197 | 201.213 | 303 | 2,9 s | 47,1 s | 6,83 | Natural |
| 1 | 198 | 202.237 | 329 | 3,3 s | 51,3 s | 6,84 | Natural |
| 1 | 199 | 203.261 | 380 | 4,1 s | 59,8 s | 6,80 | Natural |
| 1 | 200 | 204.284 | 321 | 2,9 s | 49,9 s | 6,80 | Natural |
| 1 | 201 | 205.309 | 307 | 3,4 s | 48,6 s | 6,77 | Natural |
| 1 | 202 | 206.332 | 333 | 4,1 s | 53,1 s | 6,77 | Natural |
| 1 | 203 | 207.357 | 384 | 2,7 s | 59,6 s | 6,74 | Natural |
| 1 | 204 | 208.381 | 321 | 3,2 s | 50,8 s | 6,72 | Natural |
| 1 | 205 | 209.405 | 307 | 3,9 s | 49,5 s | 6,72 | Natural |
| 1 | 206 | 210.429 | 333 | 2,7 s | 52,4 s | 6,69 | Natural |
| 1 | 207 | 211.453 | 384 | 3,4 s | 61,2 s | 6,63 | Natural |
| 1 | 208 | 212.476 | 324 | 3,9 s | 52,6 s | 6,64 | Natural |
| 1 | 209 | 213.501 | 309 | 2,6 s | 48,8 s | 6,67 | Natural |
| 1 | 210 | 214.525 | 335 | 3,0 s | 53,3 s | 6,65 | Natural |
| 1 | 211 | 215.549 | 387 | 3,5 s | 61,9 s | 6,60 | Natural |
| 1 | 212 | 216.573 | 326 | 4,3 s | 53,4 s | 6,62 | Natural |
| 1 | 213 | 217.597 | 310 | 3,1 s | 50,0 s | 6,58 | Natural |
| 1 | 214 | 218.620 | 336 | 3,5 s | 54,5 s | 6,57 | Natural |
| 1 | 215 | 219.645 | 389 | 4,2 s | 63,2 s | 6,57 | Natural |
| 1 | 216 | 220.669 | 326 | 2,9 s | 52,5 s | 6,54 | Natural |
| 1 | 217 | 221.693 | 310 | 3,3 s | 50,6 s | 6,54 | Natural |
| 1 | 218 | 222.717 | 336 | 4,2 s | 55,5 s | 6,53 | Natural |
| 1 | 219 | 223.740 | 389 | 2,9 s | 62,6 s | 6,50 | Natural |
| 1 | 220 | 224.765 | 328 | 3,3 s | 53,8 s | 6,48 | Natural |
| 1 | 221 | 225.788 | 311 | 3,8 s | 51,7 s | 6,48 | Natural |
| 1 | 222 | 226.813 | 338 | 4,4 s | 56,6 s | 6,45 | Natural |
| 1 | 223 | 227.837 | 391 | 3,1 s | 63,7 s | 6,44 | Natural |
| 1 | 224 | 228.861 | 328 | 3,6 s | 54,4 s | 6,44 | Natural |
| 1 | 225 | 229.885 | 311 | 4,5 s | 52,8 s | 6,41 | Natural |
| 1 | 226 | 230.909 | 337 | 3,2 s | 55,6 s | 6,42 | Natural |
| 1 | 227 | 231.933 | 392 | 3,7 s | 64,9 s | 6,39 | Natural |
| 1 | 228 | 232.957 | 329 | 4,3 s | 55,8 s | 6,37 | Natural |
| 1 | 229 | 233.981 | 312 | 3,0 s | 51,8 s | 6,38 | Natural |
| 1 | 230 | 235.005 | 339 | 3,5 s | 56,7 s | 6,36 | Natural |
| 1 | 231 | 236.028 | 392 | 4,3 s | 66,1 s | 6,33 | Natural |
| 1 | 232 | 237.053 | 331 | 3,1 s | 55,3 s | 6,32 | Natural |
| 1 | 233 | 238.077 | 313 | 3,6 s | 52,9 s | 6,32 | Natural |
| 1 | 234 | 239.101 | 341 | 3,8 s | 57,9 s | 6,29 | Natural |
| 1 | 235 | 240.125 | 393 | 4,7 s | 67,1 s | 6,28 | Natural |
| 1 | 236 | 241.149 | 334 | 3,3 s | 56,5 s | 6,26 | Natural |
| 1 | 237 | 242.173 | 315 | 3,9 s | 54,0 s | 6,27 | Natural |
| 1 | 238 | 243.197 | 343 | 4,7 s | 59,5 s | 6,24 | Natural |
| 1 | 239 | 244.221 | 396 | 3,3 s | 66,7 s | 6,23 | Natural |
| 1 | 240 | 245.245 | 337 | 3,7 s | 57,8 s | 6,21 | Natural |
| 1 | 241 | 246.269 | 316 | 4,5 s | 55,3 s | 6,20 | Natural |
| 1 | 242 | 247.293 | 345 | 3,2 s | 58,7 s | 6,20 | Natural |
| 1 | 243 | 248.317 | 400 | 3,7 s | 68,3 s | 6,18 | Natural |
| 1 | 244 | 249.341 | 338 | 4,5 s | 59,2 s | 6,16 | Natural |
| 1 | 245 | 250.365 | 316 | 3,2 s | 54,4 s | 6,15 | Natural |
| 1 | 246 | 251.389 | 346 | 3,4 s | 59,5 s | 6,15 | Natural |
| 1 | 247 | 252.413 | 400 | 4,0 s | 69,2 s | 6,12 | Natural |
| 1 | 248 | 253.436 | 341 | 4,9 s | 60,4 s | 6,12 | Natural |
| 1 | 249 | 254.461 | 317 | 3,5 s | 55,2 s | 6,12 | Natural |
| 1 | 250 | 255.485 | 348 | 4,0 s | 61,0 s | 6,09 | Natural |
| 1 | 251 | 256.509 | 404 | 4,9 s | 71,2 s | 6,08 | Natural |
| 1 | 252 | 257.533 | 343 | 3,3 s | 59,7 s | 6,06 | Natural |
| 1 | 253 | 258.556 | 318 | 3,8 s | 56,2 s | 6,05 | Natural |
| 1 | 254 | 259.581 | 351 | 4,7 s | 62,5 s | 6,05 | Natural |
| 1 | 255 | 260.605 | 406 | 3,3 s | 70,6 s | 6,02 | Natural |
| 1 | 256 | 261.117 | 345 | 2,9 s | 59,8 s | 6,04 | Natural |
| 1 | 257 | 262.012 | 17 | 3,0 s | 5,6 s | 6,30 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
