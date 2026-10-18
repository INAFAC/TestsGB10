# 1 persona · 92% de memoria

[Volver a la capacidad por memoria](../README.md)

**Cumplió durante todo el recorrido.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **257/257 previstas**. Duración: **275,6 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.533–16.892 | 16/16 | 1,2 s | 1,2 s | 11,69 tokens/s | 18,6 s | Cumple |
| 18-33 | 17.917–33.277 | 16/16 | 1,2 s | 1,2 s | 11,07 tokens/s | 19,2 s | Cumple |
| 34-49 | 34.301–49.661 | 16/16 | 1,6 s | 1,6 s | 10,50 tokens/s | 22,3 s | Cumple |
| 50-65 | 50.684–66.045 | 16/16 | 1,7 s | 1,7 s | 9,98 tokens/s | 24,7 s | Cumple |
| 66-81 | 67.068–82.429 | 16/16 | 1,9 s | 1,9 s | 9,50 tokens/s | 28,5 s | Cumple |
| 82-97 | 83.453–98.812 | 16/16 | 2,1 s | 2,1 s | 9,08 tokens/s | 32,2 s | Cumple |
| 98-113 | 99.837–115.197 | 16/16 | 2,3 s | 2,3 s | 8,65 tokens/s | 36,2 s | Cumple |
| 114-129 | 116.221–131.581 | 16/16 | 2,7 s | 2,7 s | 8,27 tokens/s | 37,8 s | Cumple |
| 130-145 | 132.605–147.965 | 16/16 | 3,0 s | 3,0 s | 7,75 tokens/s | 40,1 s | Cumple |
| 146-161 | 148.989–164.349 | 16/16 | 3,3 s | 3,3 s | 7,55 tokens/s | 43,1 s | Cumple |
| 162-177 | 165.372–180.732 | 16/16 | 3,7 s | 3,7 s | 7,23 tokens/s | 46,0 s | Cumple |
| 178-193 | 181.757–197.117 | 16/16 | 3,9 s | 3,9 s | 6,95 tokens/s | 49,2 s | Cumple |
| 194-209 | 198.141–213.501 | 16/16 | 4,1 s | 4,1 s | 6,69 tokens/s | 53,6 s | Cumple |
| 210-225 | 214.525–229.885 | 16/16 | 4,6 s | 4,6 s | 6,45 tokens/s | 59,1 s | Cumple |
| 226-241 | 230.909–246.269 | 16/16 | 4,7 s | 4,7 s | 6,20 tokens/s | 64,6 s | Cumple |
| 242-257 | 247.292–262.013 | 16/16 | 5,0 s | 5,0 s | 6,05 tokens/s | 69,9 s | Cumple |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 257 | 262.029 | 99,956% | 115 |

El objetivo del cierre deja aproximadamente 128 tokens para la respuesta y pide terminar en diez palabras. El presupuesto efectivo se calcula con la entrada real. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento llegó al cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 92% |
| Pico de memoria del motor / GB10 | 88,8% |
| Pico de memoria total del sistema / GB10 | 96,3% |
| Pico de caché | 19,0% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 2,3 s |
| Espera media al primer token, incluido razonamiento | 2,3 s |
| Tiempo medio de petición completa | 34,0 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 3,93 tokens/s |
| Suma de tiempos individuales de petición | 8.728,9 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 257/257 | 2,3 s | 34,0 s | 16.537,7 s | 3,93 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 168 | 0,3 s | 13,8 s | 12,37 | Natural |
| 1 | 2 | 1.533 | 204 | 0,7 s | 17,1 s | 12,32 | Natural |
| 1 | 3 | 2.557 | 157 | 0,9 s | 13,6 s | 12,28 | Natural |
| 1 | 4 | 3.580 | 185 | 0,6 s | 15,6 s | 12,24 | Natural |
| 1 | 5 | 4.605 | 170 | 0,7 s | 14,5 s | 12,19 | Natural |
| 1 | 6 | 5.629 | 216 | 0,9 s | 18,6 s | 12,15 | Natural |
| 1 | 7 | 6.653 | 200 | 0,6 s | 17,0 s | 12,10 | Natural |
| 1 | 8 | 7.676 | 189 | 0,7 s | 16,3 s | 12,06 | Natural |
| 1 | 9 | 8.701 | 179 | 0,9 s | 15,7 s | 12,02 | Natural |
| 1 | 10 | 9.725 | 214 | 0,6 s | 18,4 s | 11,98 | Natural |
| 1 | 11 | 10.749 | 200 | 0,7 s | 17,4 s | 11,94 | Natural |
| 1 | 12 | 11.773 | 186 | 1,2 s | 16,7 s | 11,89 | Natural |
| 1 | 13 | 12.797 | 181 | 0,6 s | 15,8 s | 11,86 | Natural |
| 1 | 14 | 13.821 | 181 | 0,7 s | 15,9 s | 11,81 | Natural |
| 1 | 15 | 14.844 | 199 | 0,8 s | 17,6 s | 11,77 | Natural |
| 1 | 16 | 15.869 | 188 | 1,0 s | 17,0 s | 11,73 | Natural |
| 1 | 17 | 16.892 | 179 | 0,7 s | 15,9 s | 11,69 | Natural |
| 1 | 18 | 17.917 | 183 | 0,8 s | 16,8 s | 11,38 | Natural |
| 1 | 19 | 18.941 | 194 | 1,0 s | 17,6 s | 11,61 | Natural |
| 1 | 20 | 19.965 | 191 | 0,7 s | 17,1 s | 11,57 | Natural |
| 1 | 21 | 20.989 | 180 | 0,8 s | 16,3 s | 11,53 | Natural |
| 1 | 22 | 22.013 | 186 | 1,1 s | 17,2 s | 11,50 | Natural |
| 1 | 23 | 23.037 | 195 | 0,7 s | 17,6 s | 11,45 | Natural |
| 1 | 24 | 24.060 | 193 | 0,8 s | 17,6 s | 11,42 | Natural |
| 1 | 25 | 25.084 | 184 | 0,9 s | 17,0 s | 11,37 | Natural |
| 1 | 26 | 26.109 | 191 | 1,1 s | 17,9 s | 11,34 | Natural |
| 1 | 27 | 27.133 | 194 | 0,8 s | 17,9 s | 11,31 | Natural |
| 1 | 28 | 28.156 | 199 | 0,9 s | 18,5 s | 11,27 | Natural |
| 1 | 29 | 29.181 | 186 | 1,2 s | 17,7 s | 11,22 | Natural |
| 1 | 30 | 30.205 | 196 | 0,8 s | 18,2 s | 11,19 | Natural |
| 1 | 31 | 31.229 | 196 | 0,9 s | 18,4 s | 11,15 | Natural |
| 1 | 32 | 32.253 | 202 | 1,2 s | 19,2 s | 11,12 | Natural |
| 1 | 33 | 33.277 | 190 | 0,8 s | 17,9 s | 11,07 | Natural |
| 1 | 34 | 34.301 | 201 | 0,9 s | 19,1 s | 11,03 | Natural |
| 1 | 35 | 35.325 | 197 | 1,2 s | 19,0 s | 11,00 | Natural |
| 1 | 36 | 36.349 | 205 | 0,8 s | 19,4 s | 10,96 | Natural |
| 1 | 37 | 37.373 | 192 | 1,0 s | 18,4 s | 10,93 | Natural |
| 1 | 38 | 38.397 | 205 | 1,1 s | 19,8 s | 10,89 | Natural |
| 1 | 39 | 39.420 | 197 | 1,3 s | 19,4 s | 10,85 | Natural |
| 1 | 40 | 40.445 | 211 | 0,9 s | 20,4 s | 10,82 | Natural |
| 1 | 41 | 41.469 | 196 | 1,1 s | 19,2 s | 10,77 | Natural |
| 1 | 42 | 42.493 | 211 | 1,4 s | 20,9 s | 10,74 | Natural |
| 1 | 43 | 43.517 | 198 | 1,0 s | 19,4 s | 10,71 | Natural |
| 1 | 44 | 44.541 | 213 | 1,1 s | 20,9 s | 10,67 | Natural |
| 1 | 45 | 45.565 | 199 | 1,3 s | 19,9 s | 10,64 | Natural |
| 1 | 46 | 46.589 | 215 | 0,9 s | 21,1 s | 10,60 | Natural |
| 1 | 47 | 47.613 | 201 | 1,1 s | 20,0 s | 10,57 | Natural |
| 1 | 48 | 48.637 | 219 | 1,6 s | 22,3 s | 10,53 | Natural |
| 1 | 49 | 49.661 | 201 | 0,9 s | 20,0 s | 10,50 | Natural |
| 1 | 50 | 50.684 | 221 | 1,0 s | 22,1 s | 10,46 | Natural |
| 1 | 51 | 51.709 | 201 | 1,2 s | 20,4 s | 10,43 | Natural |
| 1 | 52 | 52.733 | 222 | 1,5 s | 22,7 s | 10,40 | Natural |
| 1 | 53 | 53.757 | 204 | 1,0 s | 20,6 s | 10,37 | Natural |
| 1 | 54 | 54.781 | 226 | 1,2 s | 23,0 s | 10,32 | Natural |
| 1 | 55 | 55.805 | 203 | 1,5 s | 21,1 s | 10,30 | Natural |
| 1 | 56 | 56.829 | 227 | 1,0 s | 23,1 s | 10,26 | Natural |
| 1 | 57 | 57.853 | 208 | 1,2 s | 21,4 s | 10,23 | Natural |
| 1 | 58 | 58.877 | 232 | 1,5 s | 24,1 s | 10,20 | Natural |
| 1 | 59 | 59.901 | 203 | 1,0 s | 20,9 s | 10,17 | Natural |
| 1 | 60 | 60.925 | 231 | 1,2 s | 23,9 s | 10,13 | Natural |
| 1 | 61 | 61.949 | 211 | 1,5 s | 22,3 s | 10,10 | Natural |
| 1 | 62 | 62.973 | 237 | 1,0 s | 24,4 s | 10,07 | Natural |
| 1 | 63 | 63.997 | 204 | 1,1 s | 21,4 s | 10,04 | Natural |
| 1 | 64 | 65.021 | 235 | 1,3 s | 24,7 s | 10,01 | Natural |
| 1 | 65 | 66.045 | 214 | 1,7 s | 23,0 s | 9,98 | Natural |
| 1 | 66 | 67.068 | 240 | 1,2 s | 25,2 s | 9,95 | Natural |
| 1 | 67 | 68.093 | 204 | 1,3 s | 21,8 s | 9,92 | Natural |
| 1 | 68 | 69.117 | 239 | 1,6 s | 25,7 s | 9,87 | Natural |
| 1 | 69 | 70.141 | 217 | 1,1 s | 23,0 s | 9,86 | Natural |
| 1 | 70 | 71.165 | 247 | 1,3 s | 26,4 s | 9,84 | Natural |
| 1 | 71 | 72.189 | 207 | 1,6 s | 22,8 s | 9,76 | Natural |
| 1 | 72 | 73.213 | 242 | 1,1 s | 25,8 s | 9,77 | Natural |
| 1 | 73 | 74.237 | 220 | 1,3 s | 23,8 s | 9,75 | Natural |
| 1 | 74 | 75.261 | 251 | 1,5 s | 27,3 s | 9,71 | Natural |
| 1 | 75 | 76.285 | 207 | 1,8 s | 23,1 s | 9,69 | Natural |
| 1 | 76 | 77.308 | 246 | 1,3 s | 26,7 s | 9,65 | Natural |
| 1 | 77 | 78.333 | 223 | 1,5 s | 24,5 s | 9,62 | Natural |
| 1 | 78 | 79.356 | 256 | 1,9 s | 28,5 s | 9,57 | Natural |
| 1 | 79 | 80.381 | 208 | 1,3 s | 22,9 s | 9,58 | Natural |
| 1 | 80 | 81.405 | 251 | 1,5 s | 27,8 s | 9,52 | Natural |
| 1 | 81 | 82.429 | 226 | 1,8 s | 25,5 s | 9,50 | Natural |
| 1 | 82 | 83.453 | 261 | 1,3 s | 28,7 s | 9,48 | Natural |
| 1 | 83 | 84.477 | 209 | 1,5 s | 23,5 s | 9,46 | Natural |
| 1 | 84 | 85.501 | 255 | 1,8 s | 28,8 s | 9,42 | Natural |
| 1 | 85 | 86.525 | 228 | 1,3 s | 25,4 s | 9,40 | Natural |
| 1 | 86 | 87.549 | 267 | 1,5 s | 29,9 s | 9,36 | Natural |
| 1 | 87 | 88.572 | 210 | 1,6 s | 24,4 s | 9,19 | Natural |
| 1 | 88 | 89.597 | 258 | 2,0 s | 29,8 s | 9,26 | Natural |
| 1 | 89 | 90.621 | 231 | 1,4 s | 26,3 s | 9,25 | Natural |
| 1 | 90 | 91.645 | 271 | 1,6 s | 30,8 s | 9,25 | Natural |
| 1 | 91 | 92.669 | 211 | 2,0 s | 24,9 s | 9,20 | Natural |
| 1 | 92 | 93.693 | 262 | 1,5 s | 29,8 s | 9,21 | Natural |
| 1 | 93 | 94.716 | 235 | 1,6 s | 27,2 s | 9,16 | Natural |
| 1 | 94 | 95.741 | 277 | 2,0 s | 32,2 s | 9,15 | Natural |
| 1 | 95 | 96.764 | 211 | 1,4 s | 24,4 s | 9,13 | Natural |
| 1 | 96 | 97.789 | 265 | 1,6 s | 30,7 s | 9,09 | Natural |
| 1 | 97 | 98.812 | 237 | 2,1 s | 28,0 s | 9,08 | Natural |
| 1 | 98 | 99.837 | 282 | 1,4 s | 32,5 s | 9,04 | Natural |
| 1 | 99 | 100.861 | 213 | 1,6 s | 25,1 s | 9,02 | Natural |
| 1 | 100 | 101.884 | 271 | 1,8 s | 31,8 s | 8,98 | Natural |
| 1 | 101 | 102.909 | 240 | 2,2 s | 28,9 s | 8,96 | Natural |
| 1 | 102 | 103.933 | 286 | 1,6 s | 33,5 s | 8,93 | Natural |
| 1 | 103 | 104.957 | 215 | 1,8 s | 25,9 s | 8,91 | Natural |
| 1 | 104 | 105.981 | 273 | 2,3 s | 32,9 s | 8,89 | Natural |
| 1 | 105 | 107.005 | 244 | 1,5 s | 29,0 s | 8,85 | Natural |
| 1 | 106 | 108.029 | 291 | 1,8 s | 34,6 s | 8,83 | Natural |
| 1 | 107 | 109.053 | 215 | 2,2 s | 26,5 s | 8,81 | Natural |
| 1 | 108 | 110.077 | 278 | 1,6 s | 33,1 s | 8,78 | Natural |
| 1 | 109 | 111.101 | 247 | 1,8 s | 29,9 s | 8,75 | Natural |
| 1 | 110 | 112.125 | 297 | 2,3 s | 36,2 s | 8,72 | Natural |
| 1 | 111 | 113.149 | 217 | 1,5 s | 26,4 s | 8,67 | Natural |
| 1 | 112 | 114.173 | 277 | 1,7 s | 33,6 s | 8,67 | Natural |
| 1 | 113 | 115.197 | 245 | 2,0 s | 30,2 s | 8,65 | Natural |
| 1 | 114 | 116.221 | 293 | 2,5 s | 36,5 s | 8,59 | Natural |
| 1 | 115 | 117.245 | 216 | 1,8 s | 26,9 s | 8,58 | Natural |
| 1 | 116 | 118.268 | 277 | 2,0 s | 34,3 s | 8,55 | Natural |
| 1 | 117 | 119.293 | 245 | 2,4 s | 31,0 s | 8,52 | Natural |
| 1 | 118 | 120.317 | 292 | 1,7 s | 36,0 s | 8,49 | Natural |
| 1 | 119 | 121.340 | 215 | 2,0 s | 27,2 s | 8,49 | Natural |
| 1 | 120 | 122.365 | 279 | 2,5 s | 35,5 s | 8,42 | Natural |
| 1 | 121 | 123.389 | 247 | 1,7 s | 30,9 s | 8,43 | Natural |
| 1 | 122 | 124.413 | 296 | 2,0 s | 37,0 s | 8,43 | Natural |
| 1 | 123 | 125.437 | 217 | 2,3 s | 28,1 s | 8,39 | Natural |
| 1 | 124 | 126.461 | 279 | 2,7 s | 35,8 s | 8,38 | Natural |
| 1 | 125 | 127.485 | 246 | 1,9 s | 31,2 s | 8,36 | Natural |
| 1 | 126 | 128.509 | 297 | 2,2 s | 37,8 s | 8,33 | Natural |
| 1 | 127 | 129.533 | 216 | 2,7 s | 28,6 s | 8,30 | Natural |
| 1 | 128 | 130.557 | 280 | 1,9 s | 35,6 s | 8,28 | Natural |
| 1 | 129 | 131.581 | 248 | 2,3 s | 32,1 s | 8,27 | Natural |
| 1 | 130 | 132.605 | 298 | 2,7 s | 38,7 s | 8,24 | Natural |
| 1 | 131 | 133.629 | 217 | 1,9 s | 28,2 s | 8,22 | Natural |
| 1 | 132 | 134.653 | 284 | 2,2 s | 36,7 s | 8,19 | Natural |
| 1 | 133 | 135.677 | 252 | 2,7 s | 33,4 s | 8,17 | Natural |
| 1 | 134 | 136.701 | 303 | 1,9 s | 39,0 s | 8,14 | Natural |
| 1 | 135 | 137.725 | 218 | 2,2 s | 28,9 s | 8,12 | Natural |
| 1 | 136 | 138.749 | 285 | 2,4 s | 37,4 s | 8,10 | Natural |
| 1 | 137 | 139.772 | 252 | 2,9 s | 34,0 s | 8,08 | Natural |
| 1 | 138 | 140.797 | 303 | 2,1 s | 39,6 s | 8,05 | Natural |
| 1 | 139 | 141.821 | 218 | 2,4 s | 29,4 s | 8,05 | Natural |
| 1 | 140 | 142.845 | 283 | 3,0 s | 38,2 s | 8,01 | Natural |
| 1 | 141 | 143.869 | 252 | 2,1 s | 33,5 s | 7,99 | Natural |
| 1 | 142 | 144.893 | 302 | 2,3 s | 40,1 s | 7,96 | Natural |
| 1 | 143 | 145.917 | 218 | 2,9 s | 30,2 s | 7,96 | Natural |
| 1 | 144 | 146.940 | 288 | 2,0 s | 38,3 s | 7,91 | Natural |
| 1 | 145 | 147.965 | 255 | 2,4 s | 35,2 s | 7,75 | Natural |
| 1 | 146 | 148.989 | 309 | 2,9 s | 42,0 s | 7,88 | Natural |
| 1 | 147 | 150.013 | 220 | 2,0 s | 29,9 s | 7,86 | Natural |
| 1 | 148 | 151.037 | 288 | 2,2 s | 38,9 s | 7,83 | Natural |
| 1 | 149 | 152.061 | 254 | 2,6 s | 35,0 s | 7,80 | Natural |
| 1 | 150 | 153.085 | 309 | 3,2 s | 42,7 s | 7,79 | Natural |
| 1 | 151 | 154.109 | 219 | 2,2 s | 30,8 s | 7,64 | Natural |
| 1 | 152 | 155.133 | 289 | 2,7 s | 39,9 s | 7,74 | Natural |
| 1 | 153 | 156.157 | 254 | 3,3 s | 36,0 s | 7,72 | Natural |
| 1 | 154 | 157.180 | 308 | 2,2 s | 42,0 s | 7,70 | Natural |
| 1 | 155 | 158.205 | 219 | 2,5 s | 30,9 s | 7,68 | Natural |
| 1 | 156 | 159.229 | 291 | 3,1 s | 41,0 s | 7,66 | Natural |
| 1 | 157 | 160.253 | 256 | 2,2 s | 35,6 s | 7,64 | Natural |
| 1 | 158 | 161.277 | 310 | 2,6 s | 43,1 s | 7,62 | Natural |
| 1 | 159 | 162.301 | 219 | 3,2 s | 31,9 s | 7,60 | Natural |
| 1 | 160 | 163.325 | 292 | 2,1 s | 40,4 s | 7,58 | Natural |
| 1 | 161 | 164.349 | 258 | 2,4 s | 36,5 s | 7,55 | Natural |
| 1 | 162 | 165.372 | 314 | 2,8 s | 44,4 s | 7,53 | Natural |
| 1 | 163 | 166.397 | 221 | 3,4 s | 32,7 s | 7,51 | Natural |
| 1 | 164 | 167.420 | 293 | 2,4 s | 41,4 s | 7,49 | Natural |
| 1 | 165 | 168.445 | 257 | 2,8 s | 37,1 s | 7,47 | Natural |
| 1 | 166 | 169.469 | 314 | 3,3 s | 45,4 s | 7,44 | Natural |
| 1 | 167 | 170.493 | 220 | 2,3 s | 31,8 s | 7,43 | Natural |
| 1 | 168 | 171.517 | 295 | 2,7 s | 42,4 s | 7,40 | Natural |
| 1 | 169 | 172.541 | 258 | 3,4 s | 38,1 s | 7,39 | Natural |
| 1 | 170 | 173.565 | 315 | 2,4 s | 45,0 s | 7,37 | Natural |
| 1 | 171 | 174.589 | 219 | 2,8 s | 32,4 s | 7,35 | Natural |
| 1 | 172 | 175.613 | 294 | 3,1 s | 43,1 s | 7,33 | Natural |
| 1 | 173 | 176.637 | 259 | 3,6 s | 38,9 s | 7,31 | Natural |
| 1 | 174 | 177.661 | 317 | 2,6 s | 46,0 s | 7,28 | Natural |
| 1 | 175 | 178.685 | 220 | 3,0 s | 33,2 s | 7,27 | Natural |
| 1 | 176 | 179.709 | 294 | 3,7 s | 44,1 s | 7,25 | Natural |
| 1 | 177 | 180.732 | 258 | 2,6 s | 38,2 s | 7,23 | Natural |
| 1 | 178 | 181.757 | 316 | 3,0 s | 46,7 s | 7,22 | Natural |
| 1 | 179 | 182.781 | 219 | 3,5 s | 33,8 s | 7,21 | Natural |
| 1 | 180 | 183.805 | 295 | 2,4 s | 43,5 s | 7,17 | Natural |
| 1 | 181 | 184.829 | 260 | 2,9 s | 39,1 s | 7,16 | Natural |
| 1 | 182 | 185.852 | 319 | 3,6 s | 48,1 s | 7,14 | Natural |
| 1 | 183 | 186.877 | 221 | 2,5 s | 33,4 s | 7,12 | Natural |
| 1 | 184 | 187.901 | 298 | 2,9 s | 44,8 s | 7,09 | Natural |
| 1 | 185 | 188.925 | 263 | 3,2 s | 40,1 s | 7,09 | Natural |
| 1 | 186 | 189.949 | 321 | 3,9 s | 49,2 s | 7,06 | Natural |
| 1 | 187 | 190.973 | 222 | 2,8 s | 34,1 s | 7,05 | Natural |
| 1 | 188 | 191.997 | 300 | 3,2 s | 45,8 s | 7,03 | Natural |
| 1 | 189 | 193.021 | 263 | 3,9 s | 41,3 s | 7,01 | Natural |
| 1 | 190 | 194.045 | 322 | 2,8 s | 48,7 s | 6,99 | Natural |
| 1 | 191 | 195.069 | 222 | 3,0 s | 34,7 s | 6,98 | Natural |
| 1 | 192 | 196.093 | 303 | 3,7 s | 47,2 s | 6,96 | Natural |
| 1 | 193 | 197.117 | 265 | 2,6 s | 40,6 s | 6,95 | Natural |
| 1 | 194 | 198.141 | 326 | 3,1 s | 50,0 s | 6,92 | Natural |
| 1 | 195 | 199.165 | 223 | 3,8 s | 35,9 s | 6,92 | Natural |
| 1 | 196 | 200.189 | 306 | 2,6 s | 47,6 s | 6,79 | Natural |
| 1 | 197 | 201.213 | 267 | 2,9 s | 41,6 s | 6,88 | Natural |
| 1 | 198 | 202.237 | 331 | 3,4 s | 51,5 s | 6,86 | Natural |
| 1 | 199 | 203.261 | 224 | 4,1 s | 36,7 s | 6,85 | Natural |
| 1 | 200 | 204.284 | 309 | 2,9 s | 48,0 s | 6,83 | Natural |
| 1 | 201 | 205.309 | 271 | 3,4 s | 43,0 s | 6,81 | Natural |
| 1 | 202 | 206.333 | 337 | 4,1 s | 53,6 s | 6,79 | Natural |
| 1 | 203 | 207.356 | 223 | 2,7 s | 35,4 s | 6,79 | Natural |
| 1 | 204 | 208.381 | 313 | 3,2 s | 49,3 s | 6,76 | Natural |
| 1 | 205 | 209.405 | 271 | 3,9 s | 44,0 s | 6,74 | Natural |
| 1 | 206 | 210.429 | 339 | 2,8 s | 53,0 s | 6,73 | Natural |
| 1 | 207 | 211.452 | 224 | 3,2 s | 36,4 s | 6,72 | Natural |
| 1 | 208 | 212.477 | 315 | 4,1 s | 51,0 s | 6,69 | Natural |
| 1 | 209 | 213.501 | 273 | 2,6 s | 43,3 s | 6,69 | Natural |
| 1 | 210 | 214.525 | 341 | 3,1 s | 54,1 s | 6,66 | Natural |
| 1 | 211 | 215.548 | 225 | 3,5 s | 37,1 s | 6,66 | Natural |
| 1 | 212 | 216.573 | 317 | 4,3 s | 51,9 s | 6,63 | Natural |
| 1 | 213 | 217.597 | 274 | 3,0 s | 44,3 s | 6,62 | Natural |
| 1 | 214 | 218.621 | 346 | 3,6 s | 55,8 s | 6,61 | Natural |
| 1 | 215 | 219.644 | 225 | 4,1 s | 38,1 s | 6,59 | Natural |
| 1 | 216 | 220.669 | 320 | 2,9 s | 51,4 s | 6,57 | Natural |
| 1 | 217 | 221.693 | 276 | 3,4 s | 45,3 s | 6,56 | Natural |
| 1 | 218 | 222.716 | 350 | 4,2 s | 57,5 s | 6,54 | Natural |
| 1 | 219 | 223.741 | 224 | 2,9 s | 37,0 s | 6,54 | Natural |
| 1 | 220 | 224.764 | 324 | 3,4 s | 53,0 s | 6,52 | Natural |
| 1 | 221 | 225.789 | 279 | 3,9 s | 46,6 s | 6,50 | Natural |
| 1 | 222 | 226.813 | 355 | 4,5 s | 59,1 s | 6,49 | Natural |
| 1 | 223 | 227.837 | 226 | 3,2 s | 37,9 s | 6,48 | Natural |
| 1 | 224 | 228.861 | 329 | 3,7 s | 54,5 s | 6,46 | Natural |
| 1 | 225 | 229.885 | 282 | 4,6 s | 48,1 s | 6,45 | Natural |
| 1 | 226 | 230.909 | 361 | 3,2 s | 59,2 s | 6,43 | Natural |
| 1 | 227 | 231.933 | 227 | 3,8 s | 39,0 s | 6,42 | Natural |
| 1 | 228 | 232.957 | 331 | 4,3 s | 55,9 s | 6,40 | Natural |
| 1 | 229 | 233.981 | 285 | 3,0 s | 47,4 s | 6,39 | Natural |
| 1 | 230 | 235.005 | 365 | 3,5 s | 60,7 s | 6,37 | Natural |
| 1 | 231 | 236.029 | 224 | 4,4 s | 39,4 s | 6,37 | Natural |
| 1 | 232 | 237.053 | 337 | 3,1 s | 56,0 s | 6,35 | Natural |
| 1 | 233 | 238.076 | 288 | 3,6 s | 48,8 s | 6,34 | Natural |
| 1 | 234 | 239.101 | 370 | 3,9 s | 62,3 s | 6,32 | Natural |
| 1 | 235 | 240.125 | 229 | 4,7 s | 40,8 s | 6,32 | Natural |
| 1 | 236 | 241.149 | 340 | 3,4 s | 57,2 s | 6,30 | Natural |
| 1 | 237 | 242.173 | 291 | 3,9 s | 50,0 s | 6,28 | Natural |
| 1 | 238 | 243.197 | 376 | 4,7 s | 64,6 s | 6,27 | Natural |
| 1 | 239 | 244.221 | 230 | 3,4 s | 40,0 s | 6,26 | Natural |
| 1 | 240 | 245.245 | 344 | 3,7 s | 58,6 s | 6,25 | Natural |
| 1 | 241 | 246.269 | 295 | 4,6 s | 52,0 s | 6,20 | Natural |
| 1 | 242 | 247.292 | 381 | 3,1 s | 64,3 s | 6,21 | Natural |
| 1 | 243 | 248.317 | 231 | 3,7 s | 40,7 s | 6,21 | Natural |
| 1 | 244 | 249.341 | 348 | 4,6 s | 60,6 s | 6,19 | Natural |
| 1 | 245 | 250.365 | 298 | 3,2 s | 51,2 s | 6,18 | Natural |
| 1 | 246 | 251.389 | 385 | 3,5 s | 65,8 s | 6,16 | Natural |
| 1 | 247 | 252.413 | 232 | 4,0 s | 41,6 s | 6,16 | Natural |
| 1 | 248 | 253.436 | 353 | 4,9 s | 62,3 s | 6,14 | Natural |
| 1 | 249 | 254.460 | 300 | 3,5 s | 52,3 s | 6,13 | Natural |
| 1 | 250 | 255.485 | 390 | 4,1 s | 67,7 s | 6,11 | Natural |
| 1 | 251 | 256.508 | 232 | 5,0 s | 42,8 s | 6,11 | Natural |
| 1 | 252 | 257.533 | 356 | 3,3 s | 61,6 s | 6,09 | Natural |
| 1 | 253 | 258.557 | 304 | 3,9 s | 53,7 s | 6,08 | Natural |
| 1 | 254 | 259.581 | 396 | 4,8 s | 69,9 s | 6,07 | Natural |
| 1 | 255 | 260.605 | 233 | 3,4 s | 41,6 s | 6,06 | Natural |
| 1 | 256 | 261.117 | 361 | 2,8 s | 62,3 s | 6,05 | Natural |
| 1 | 257 | 262.013 | 16 | 3,1 s | 5,4 s | 6,32 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
