# 1 persona · 35% de memoria

[Volver a la capacidad por memoria](../README.md)

**Cumplió durante todo el recorrido.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **257/257 previstas**. Duración: **262,6 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.533–16.893 | 16/16 | 1,2 s | 1,2 s | 11,76 tokens/s | 16,9 s | Cumple |
| 18-33 | 17.917–33.277 | 16/16 | 1,3 s | 1,3 s | 11,16 tokens/s | 20,1 s | Cumple |
| 34-49 | 34.301–49.661 | 16/16 | 1,5 s | 1,5 s | 10,63 tokens/s | 23,6 s | Cumple |
| 50-65 | 50.685–66.045 | 16/16 | 1,6 s | 1,6 s | 10,10 tokens/s | 26,6 s | Cumple |
| 66-81 | 67.069–82.429 | 16/16 | 1,7 s | 1,7 s | 9,70 tokens/s | 30,4 s | Cumple |
| 82-97 | 83.453–98.813 | 16/16 | 2,0 s | 2,0 s | 9,30 tokens/s | 33,9 s | Cumple |
| 98-113 | 99.837–115.197 | 16/16 | 2,2 s | 2,2 s | 8,92 tokens/s | 36,1 s | Cumple |
| 114-129 | 116.220–131.581 | 16/16 | 2,4 s | 2,4 s | 8,58 tokens/s | 38,9 s | Cumple |
| 130-145 | 132.605–147.965 | 16/16 | 2,5 s | 2,5 s | 8,27 tokens/s | 41,5 s | Cumple |
| 146-161 | 148.989–164.349 | 16/16 | 2,6 s | 2,6 s | 7,97 tokens/s | 43,6 s | Cumple |
| 162-177 | 165.373–180.732 | 16/16 | 2,9 s | 2,9 s | 7,69 tokens/s | 47,1 s | Cumple |
| 178-193 | 181.757–197.117 | 16/16 | 3,1 s | 3,1 s | 7,44 tokens/s | 49,9 s | Cumple |
| 194-209 | 198.141–213.501 | 16/16 | 3,3 s | 3,3 s | 7,19 tokens/s | 52,9 s | Cumple |
| 210-225 | 214.524–229.885 | 16/16 | 3,5 s | 3,5 s | 6,97 tokens/s | 55,3 s | Cumple |
| 226-241 | 230.908–246.269 | 16/16 | 3,7 s | 3,7 s | 6,75 tokens/s | 56,9 s | Cumple |
| 242-257 | 247.292–262.013 | 16/16 | 3,8 s | 3,8 s | 6,56 tokens/s | 60,1 s | Cumple |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 257 | 262.028 | 99,956% | 116 |

El objetivo del cierre deja aproximadamente 128 tokens para la respuesta y pide terminar en diez palabras. El presupuesto efectivo se calcula con la entrada real. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento llegó al cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 35% |
| Pico de memoria del motor / GB10 | 31,7% |
| Pico de memoria total del sistema / GB10 | 40,1% |
| Pico de caché | 94,5% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 1,9 s |
| Espera media al primer token, incluido razonamiento | 1,9 s |
| Tiempo medio de petición completa | 30,9 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 3,98 tokens/s |
| Suma de tiempos individuales de petición | 7.943,8 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 257/257 | 1,9 s | 30,9 s | 15.753,7 s | 3,98 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 168 | 0,2 s | 13,7 s | 12,38 | Natural |
| 1 | 2 | 1.533 | 151 | 0,6 s | 12,8 s | 12,36 | Natural |
| 1 | 3 | 2.557 | 184 | 0,8 s | 15,7 s | 12,32 | Natural |
| 1 | 4 | 3.580 | 178 | 0,6 s | 15,0 s | 12,29 | Natural |
| 1 | 5 | 4.605 | 170 | 0,7 s | 14,5 s | 12,23 | Natural |
| 1 | 6 | 5.629 | 165 | 0,9 s | 14,3 s | 12,20 | Natural |
| 1 | 7 | 6.652 | 177 | 0,6 s | 15,1 s | 12,16 | Natural |
| 1 | 8 | 7.677 | 174 | 0,7 s | 14,9 s | 12,12 | Natural |
| 1 | 9 | 8.701 | 171 | 0,9 s | 15,0 s | 12,08 | Natural |
| 1 | 10 | 9.725 | 163 | 0,6 s | 14,1 s | 12,04 | Natural |
| 1 | 11 | 10.749 | 177 | 0,7 s | 15,3 s | 12,00 | Natural |
| 1 | 12 | 11.773 | 180 | 1,2 s | 16,1 s | 11,96 | Natural |
| 1 | 13 | 12.796 | 172 | 0,6 s | 14,9 s | 11,92 | Natural |
| 1 | 14 | 13.821 | 168 | 0,7 s | 14,7 s | 11,89 | Natural |
| 1 | 15 | 14.845 | 179 | 0,8 s | 15,8 s | 11,84 | Natural |
| 1 | 16 | 15.868 | 189 | 1,0 s | 16,9 s | 11,80 | Natural |
| 1 | 17 | 16.893 | 172 | 0,7 s | 15,2 s | 11,76 | Natural |
| 1 | 18 | 17.917 | 177 | 0,8 s | 15,8 s | 11,72 | Natural |
| 1 | 19 | 18.941 | 180 | 1,0 s | 16,3 s | 11,69 | Natural |
| 1 | 20 | 19.964 | 195 | 0,7 s | 17,3 s | 11,65 | Natural |
| 1 | 21 | 20.989 | 174 | 0,8 s | 15,7 s | 11,61 | Natural |
| 1 | 22 | 22.013 | 182 | 1,3 s | 16,9 s | 11,57 | Natural |
| 1 | 23 | 23.037 | 180 | 0,7 s | 16,2 s | 11,54 | Natural |
| 1 | 24 | 24.061 | 201 | 0,8 s | 18,2 s | 11,50 | Natural |
| 1 | 25 | 25.085 | 174 | 0,9 s | 16,0 s | 11,46 | Natural |
| 1 | 26 | 26.109 | 190 | 1,1 s | 17,6 s | 11,43 | Natural |
| 1 | 27 | 27.133 | 180 | 0,8 s | 16,5 s | 11,38 | Natural |
| 1 | 28 | 28.157 | 207 | 0,9 s | 19,0 s | 11,34 | Natural |
| 1 | 29 | 29.181 | 175 | 1,1 s | 16,5 s | 11,31 | Natural |
| 1 | 30 | 30.205 | 194 | 0,8 s | 17,9 s | 11,27 | Natural |
| 1 | 31 | 31.229 | 182 | 0,9 s | 17,0 s | 11,24 | Natural |
| 1 | 32 | 32.253 | 213 | 1,1 s | 20,1 s | 11,21 | Natural |
| 1 | 33 | 33.277 | 176 | 0,8 s | 16,5 s | 11,16 | Natural |
| 1 | 34 | 34.301 | 203 | 0,9 s | 19,0 s | 11,13 | Natural |
| 1 | 35 | 35.325 | 182 | 1,2 s | 17,5 s | 11,10 | Natural |
| 1 | 36 | 36.349 | 217 | 0,8 s | 20,3 s | 11,06 | Natural |
| 1 | 37 | 37.373 | 177 | 0,9 s | 16,9 s | 11,02 | Natural |
| 1 | 38 | 38.396 | 208 | 1,0 s | 19,8 s | 10,99 | Natural |
| 1 | 39 | 39.421 | 184 | 1,3 s | 18,0 s | 10,96 | Natural |
| 1 | 40 | 40.445 | 224 | 0,9 s | 21,3 s | 10,92 | Natural |
| 1 | 41 | 41.469 | 178 | 1,0 s | 17,3 s | 10,90 | Natural |
| 1 | 42 | 42.493 | 213 | 1,3 s | 20,8 s | 10,86 | Natural |
| 1 | 43 | 43.517 | 184 | 0,9 s | 17,8 s | 10,83 | Natural |
| 1 | 44 | 44.541 | 231 | 1,0 s | 22,3 s | 10,79 | Natural |
| 1 | 45 | 45.565 | 180 | 1,3 s | 17,9 s | 10,76 | Natural |
| 1 | 46 | 46.589 | 219 | 0,9 s | 21,2 s | 10,73 | Natural |
| 1 | 47 | 47.613 | 186 | 1,0 s | 18,3 s | 10,69 | Natural |
| 1 | 48 | 48.637 | 236 | 1,5 s | 23,6 s | 10,66 | Natural |
| 1 | 49 | 49.661 | 180 | 0,9 s | 17,8 s | 10,63 | Natural |
| 1 | 50 | 50.685 | 226 | 1,0 s | 22,2 s | 10,60 | Natural |
| 1 | 51 | 51.709 | 187 | 1,1 s | 18,7 s | 10,57 | Natural |
| 1 | 52 | 52.733 | 243 | 1,4 s | 24,4 s | 10,53 | Natural |
| 1 | 53 | 53.757 | 181 | 1,0 s | 18,1 s | 10,51 | Natural |
| 1 | 54 | 54.781 | 231 | 1,2 s | 23,1 s | 10,47 | Natural |
| 1 | 55 | 55.804 | 188 | 1,4 s | 19,3 s | 10,45 | Natural |
| 1 | 56 | 56.829 | 249 | 1,0 s | 24,8 s | 10,41 | Natural |
| 1 | 57 | 57.853 | 182 | 1,1 s | 18,5 s | 10,39 | Natural |
| 1 | 58 | 58.876 | 237 | 1,4 s | 24,2 s | 10,35 | Natural |
| 1 | 59 | 59.900 | 190 | 1,0 s | 19,3 s | 10,33 | Natural |
| 1 | 60 | 60.924 | 255 | 1,1 s | 25,8 s | 10,28 | Natural |
| 1 | 61 | 61.949 | 184 | 1,5 s | 19,3 s | 10,27 | Natural |
| 1 | 62 | 62.973 | 244 | 1,0 s | 25,0 s | 10,10 | Natural |
| 1 | 63 | 63.997 | 190 | 1,1 s | 19,6 s | 10,21 | Natural |
| 1 | 64 | 65.020 | 259 | 1,3 s | 26,6 s | 10,16 | Natural |
| 1 | 65 | 66.045 | 184 | 1,6 s | 19,6 s | 10,14 | Natural |
| 1 | 66 | 67.069 | 251 | 1,1 s | 25,8 s | 10,11 | Natural |
| 1 | 67 | 68.093 | 191 | 1,3 s | 20,1 s | 10,08 | Natural |
| 1 | 68 | 69.117 | 266 | 1,6 s | 27,9 s | 10,05 | Natural |
| 1 | 69 | 70.141 | 186 | 1,1 s | 19,5 s | 10,03 | Natural |
| 1 | 70 | 71.164 | 256 | 1,3 s | 26,8 s | 9,99 | Natural |
| 1 | 71 | 72.189 | 192 | 1,6 s | 20,7 s | 9,97 | Natural |
| 1 | 72 | 73.213 | 272 | 1,1 s | 28,4 s | 9,94 | Natural |
| 1 | 73 | 74.236 | 187 | 1,3 s | 20,0 s | 9,92 | Natural |
| 1 | 74 | 75.261 | 262 | 1,4 s | 27,9 s | 9,88 | Natural |
| 1 | 75 | 76.285 | 193 | 1,7 s | 21,2 s | 9,86 | Natural |
| 1 | 76 | 77.309 | 278 | 1,2 s | 29,4 s | 9,83 | Natural |
| 1 | 77 | 78.333 | 188 | 1,4 s | 20,5 s | 9,81 | Natural |
| 1 | 78 | 79.357 | 269 | 1,7 s | 29,2 s | 9,77 | Natural |
| 1 | 79 | 80.381 | 193 | 1,2 s | 20,9 s | 9,75 | Natural |
| 1 | 80 | 81.405 | 283 | 1,4 s | 30,4 s | 9,72 | Natural |
| 1 | 81 | 82.429 | 188 | 1,7 s | 21,0 s | 9,70 | Natural |
| 1 | 82 | 83.453 | 274 | 1,2 s | 29,4 s | 9,67 | Natural |
| 1 | 83 | 84.477 | 195 | 1,4 s | 21,5 s | 9,64 | Natural |
| 1 | 84 | 85.501 | 289 | 2,0 s | 31,9 s | 9,61 | Natural |
| 1 | 85 | 86.525 | 189 | 1,2 s | 20,8 s | 9,60 | Natural |
| 1 | 86 | 87.548 | 275 | 1,4 s | 30,0 s | 9,56 | Natural |
| 1 | 87 | 88.573 | 195 | 1,5 s | 21,8 s | 9,54 | Natural |
| 1 | 88 | 89.597 | 294 | 1,9 s | 32,7 s | 9,51 | Natural |
| 1 | 89 | 90.621 | 190 | 1,3 s | 21,2 s | 9,50 | Natural |
| 1 | 90 | 91.644 | 285 | 1,5 s | 31,5 s | 9,46 | Natural |
| 1 | 91 | 92.669 | 196 | 1,9 s | 22,5 s | 9,44 | Natural |
| 1 | 92 | 93.693 | 298 | 1,3 s | 32,9 s | 9,41 | Natural |
| 1 | 93 | 94.716 | 189 | 1,5 s | 21,5 s | 9,39 | Natural |
| 1 | 94 | 95.741 | 288 | 1,9 s | 32,5 s | 9,36 | Natural |
| 1 | 95 | 96.765 | 196 | 1,3 s | 22,2 s | 9,35 | Natural |
| 1 | 96 | 97.789 | 303 | 1,5 s | 33,9 s | 9,31 | Natural |
| 1 | 97 | 98.813 | 189 | 1,9 s | 22,1 s | 9,30 | Natural |
| 1 | 98 | 99.837 | 291 | 1,3 s | 32,6 s | 9,26 | Natural |
| 1 | 99 | 100.861 | 195 | 1,4 s | 22,4 s | 9,25 | Natural |
| 1 | 100 | 101.885 | 307 | 1,6 s | 34,8 s | 9,21 | Natural |
| 1 | 101 | 102.908 | 190 | 2,0 s | 22,6 s | 9,20 | Natural |
| 1 | 102 | 103.933 | 294 | 1,4 s | 33,4 s | 9,17 | Natural |
| 1 | 103 | 104.956 | 196 | 1,7 s | 23,0 s | 9,15 | Natural |
| 1 | 104 | 105.981 | 308 | 2,1 s | 35,7 s | 9,12 | Natural |
| 1 | 105 | 107.005 | 189 | 1,4 s | 22,0 s | 9,10 | Natural |
| 1 | 106 | 108.028 | 298 | 1,6 s | 34,3 s | 9,07 | Natural |
| 1 | 107 | 109.052 | 195 | 2,0 s | 23,4 s | 9,05 | Natural |
| 1 | 108 | 110.077 | 308 | 1,4 s | 35,4 s | 9,03 | Natural |
| 1 | 109 | 111.101 | 189 | 1,6 s | 22,5 s | 9,01 | Natural |
| 1 | 110 | 112.125 | 297 | 2,2 s | 35,2 s | 8,98 | Natural |
| 1 | 111 | 113.149 | 197 | 1,3 s | 23,2 s | 8,97 | Natural |
| 1 | 112 | 114.173 | 310 | 1,5 s | 36,1 s | 8,93 | Natural |
| 1 | 113 | 115.197 | 190 | 1,8 s | 23,0 s | 8,92 | Natural |
| 1 | 114 | 116.220 | 301 | 2,2 s | 35,9 s | 8,89 | Natural |
| 1 | 115 | 117.245 | 198 | 1,6 s | 23,8 s | 8,88 | Natural |
| 1 | 116 | 118.269 | 313 | 1,8 s | 37,1 s | 8,85 | Natural |
| 1 | 117 | 119.293 | 191 | 2,1 s | 23,6 s | 8,84 | Natural |
| 1 | 118 | 120.316 | 304 | 1,5 s | 35,9 s | 8,81 | Natural |
| 1 | 119 | 121.341 | 197 | 1,7 s | 24,0 s | 8,79 | Natural |
| 1 | 120 | 122.364 | 317 | 2,1 s | 38,2 s | 8,76 | Natural |
| 1 | 121 | 123.389 | 192 | 1,5 s | 23,3 s | 8,75 | Natural |
| 1 | 122 | 124.413 | 309 | 1,7 s | 37,1 s | 8,72 | Natural |
| 1 | 123 | 125.437 | 198 | 2,0 s | 24,6 s | 8,71 | Natural |
| 1 | 124 | 126.461 | 318 | 2,3 s | 38,9 s | 8,65 | Natural |
| 1 | 125 | 127.485 | 193 | 1,7 s | 23,8 s | 8,66 | Natural |
| 1 | 126 | 128.509 | 309 | 1,9 s | 37,6 s | 8,63 | Natural |
| 1 | 127 | 129.533 | 199 | 2,4 s | 25,3 s | 8,62 | Natural |
| 1 | 128 | 130.557 | 321 | 1,7 s | 38,9 s | 8,59 | Natural |
| 1 | 129 | 131.581 | 192 | 1,9 s | 24,2 s | 8,58 | Natural |
| 1 | 130 | 132.605 | 312 | 2,3 s | 38,7 s | 8,55 | Natural |
| 1 | 131 | 133.629 | 199 | 1,6 s | 24,8 s | 8,54 | Natural |
| 1 | 132 | 134.653 | 325 | 1,8 s | 39,9 s | 8,51 | Natural |
| 1 | 133 | 135.677 | 193 | 2,3 s | 24,9 s | 8,50 | Natural |
| 1 | 134 | 136.701 | 314 | 1,6 s | 38,6 s | 8,47 | Natural |
| 1 | 135 | 137.725 | 201 | 1,8 s | 25,5 s | 8,46 | Natural |
| 1 | 136 | 138.749 | 325 | 2,0 s | 40,4 s | 8,43 | Natural |
| 1 | 137 | 139.773 | 193 | 2,5 s | 25,3 s | 8,43 | Natural |
| 1 | 138 | 140.797 | 314 | 1,8 s | 39,1 s | 8,39 | Natural |
| 1 | 139 | 141.821 | 199 | 2,0 s | 25,7 s | 8,37 | Natural |
| 1 | 140 | 142.845 | 327 | 2,5 s | 41,5 s | 8,35 | Natural |
| 1 | 141 | 143.869 | 193 | 1,8 s | 24,8 s | 8,34 | Natural |
| 1 | 142 | 144.893 | 316 | 2,0 s | 39,8 s | 8,31 | Natural |
| 1 | 143 | 145.917 | 200 | 2,4 s | 26,4 s | 8,30 | Natural |
| 1 | 144 | 146.941 | 329 | 1,7 s | 41,4 s | 8,27 | Natural |
| 1 | 145 | 147.965 | 193 | 2,0 s | 25,2 s | 8,27 | Natural |
| 1 | 146 | 148.989 | 318 | 2,6 s | 41,1 s | 8,23 | Natural |
| 1 | 147 | 150.013 | 199 | 1,7 s | 25,8 s | 8,22 | Natural |
| 1 | 148 | 151.037 | 330 | 1,9 s | 42,0 s | 8,19 | Natural |
| 1 | 149 | 152.061 | 195 | 2,1 s | 25,8 s | 8,19 | Natural |
| 1 | 150 | 153.085 | 320 | 2,6 s | 41,7 s | 8,16 | Natural |
| 1 | 151 | 154.109 | 202 | 1,9 s | 26,5 s | 8,15 | Natural |
| 1 | 152 | 155.133 | 329 | 2,1 s | 42,5 s | 8,12 | Natural |
| 1 | 153 | 156.157 | 194 | 2,6 s | 26,4 s | 8,12 | Natural |
| 1 | 154 | 157.180 | 321 | 1,8 s | 41,4 s | 8,09 | Natural |
| 1 | 155 | 158.205 | 201 | 2,1 s | 26,8 s | 8,08 | Natural |
| 1 | 156 | 159.229 | 331 | 2,6 s | 43,6 s | 8,04 | Natural |
| 1 | 157 | 160.253 | 194 | 1,8 s | 25,8 s | 8,03 | Natural |
| 1 | 158 | 161.277 | 321 | 2,1 s | 42,0 s | 8,01 | Natural |
| 1 | 159 | 162.301 | 200 | 2,6 s | 27,5 s | 8,01 | Natural |
| 1 | 160 | 163.325 | 330 | 1,7 s | 43,0 s | 7,97 | Natural |
| 1 | 161 | 164.349 | 194 | 2,0 s | 26,2 s | 7,97 | Natural |
| 1 | 162 | 165.373 | 319 | 2,3 s | 42,3 s | 7,94 | Natural |
| 1 | 163 | 166.397 | 201 | 2,8 s | 28,0 s | 7,93 | Natural |
| 1 | 164 | 167.421 | 330 | 2,0 s | 43,6 s | 7,90 | Natural |
| 1 | 165 | 168.445 | 194 | 2,3 s | 26,8 s | 7,89 | Natural |
| 1 | 166 | 169.469 | 320 | 2,7 s | 43,3 s | 7,87 | Natural |
| 1 | 167 | 170.493 | 201 | 1,9 s | 27,4 s | 7,85 | Natural |
| 1 | 168 | 171.516 | 332 | 2,2 s | 44,5 s | 7,83 | Natural |
| 1 | 169 | 172.541 | 194 | 2,7 s | 27,4 s | 7,83 | Natural |
| 1 | 170 | 173.565 | 321 | 1,9 s | 42,9 s | 7,80 | Natural |
| 1 | 171 | 174.589 | 201 | 2,2 s | 27,9 s | 7,80 | Natural |
| 1 | 172 | 175.612 | 337 | 2,5 s | 45,8 s | 7,76 | Natural |
| 1 | 173 | 176.637 | 196 | 2,9 s | 28,1 s | 7,76 | Natural |
| 1 | 174 | 177.660 | 328 | 2,1 s | 44,4 s | 7,73 | Natural |
| 1 | 175 | 178.685 | 203 | 2,4 s | 28,6 s | 7,72 | Natural |
| 1 | 176 | 179.709 | 341 | 2,9 s | 47,1 s | 7,69 | Natural |
| 1 | 177 | 180.732 | 196 | 2,1 s | 27,5 s | 7,69 | Natural |
| 1 | 178 | 181.757 | 332 | 2,4 s | 45,6 s | 7,67 | Natural |
| 1 | 179 | 182.781 | 203 | 2,9 s | 29,3 s | 7,66 | Natural |
| 1 | 180 | 183.805 | 343 | 2,1 s | 47,7 s | 7,49 | Natural |
| 1 | 181 | 184.829 | 196 | 2,4 s | 27,9 s | 7,63 | Natural |
| 1 | 182 | 185.853 | 334 | 2,9 s | 46,7 s | 7,60 | Natural |
| 1 | 183 | 186.877 | 203 | 2,0 s | 28,6 s | 7,59 | Natural |
| 1 | 184 | 187.901 | 348 | 2,3 s | 48,2 s | 7,56 | Natural |
| 1 | 185 | 188.925 | 196 | 2,5 s | 28,3 s | 7,57 | Natural |
| 1 | 186 | 189.948 | 337 | 3,1 s | 47,7 s | 7,53 | Natural |
| 1 | 187 | 190.973 | 203 | 2,2 s | 29,0 s | 7,53 | Natural |
| 1 | 188 | 191.997 | 351 | 2,6 s | 49,2 s | 7,50 | Natural |
| 1 | 189 | 193.021 | 197 | 3,1 s | 29,2 s | 7,50 | Natural |
| 1 | 190 | 194.045 | 342 | 2,3 s | 47,9 s | 7,48 | Natural |
| 1 | 191 | 195.069 | 204 | 2,4 s | 29,6 s | 7,47 | Natural |
| 1 | 192 | 196.093 | 350 | 3,0 s | 49,9 s | 7,44 | Natural |
| 1 | 193 | 197.117 | 198 | 2,1 s | 28,6 s | 7,44 | Natural |
| 1 | 194 | 198.141 | 339 | 2,4 s | 48,0 s | 7,41 | Natural |
| 1 | 195 | 199.165 | 205 | 3,0 s | 30,6 s | 7,40 | Natural |
| 1 | 196 | 200.189 | 347 | 2,2 s | 49,1 s | 7,38 | Natural |
| 1 | 197 | 201.213 | 197 | 2,3 s | 28,9 s | 7,38 | Natural |
| 1 | 198 | 202.237 | 338 | 2,6 s | 48,5 s | 7,35 | Natural |
| 1 | 199 | 203.261 | 204 | 3,2 s | 30,9 s | 7,35 | Natural |
| 1 | 200 | 204.285 | 351 | 2,3 s | 50,2 s | 7,32 | Natural |
| 1 | 201 | 205.308 | 197 | 2,7 s | 29,4 s | 7,32 | Natural |
| 1 | 202 | 206.332 | 340 | 3,3 s | 49,8 s | 7,29 | Natural |
| 1 | 203 | 207.356 | 204 | 2,2 s | 30,1 s | 7,28 | Natural |
| 1 | 204 | 208.381 | 357 | 2,5 s | 51,6 s | 7,25 | Natural |
| 1 | 205 | 209.405 | 198 | 3,2 s | 30,3 s | 7,26 | Natural |
| 1 | 206 | 210.429 | 345 | 2,2 s | 49,8 s | 7,22 | Natural |
| 1 | 207 | 211.453 | 204 | 2,6 s | 30,7 s | 7,22 | Natural |
| 1 | 208 | 212.477 | 358 | 3,3 s | 52,9 s | 7,19 | Natural |
| 1 | 209 | 213.501 | 198 | 2,1 s | 29,4 s | 7,20 | Natural |
| 1 | 210 | 214.524 | 348 | 2,4 s | 50,8 s | 7,17 | Natural |
| 1 | 211 | 215.548 | 206 | 2,8 s | 31,4 s | 7,16 | Natural |
| 1 | 212 | 216.573 | 360 | 3,4 s | 53,7 s | 7,14 | Natural |
| 1 | 213 | 217.597 | 199 | 2,5 s | 30,2 s | 7,14 | Natural |
| 1 | 214 | 218.621 | 350 | 2,8 s | 51,9 s | 7,11 | Natural |
| 1 | 215 | 219.645 | 207 | 3,3 s | 32,3 s | 7,11 | Natural |
| 1 | 216 | 220.669 | 360 | 2,4 s | 53,1 s | 7,08 | Natural |
| 1 | 217 | 221.693 | 199 | 2,7 s | 30,7 s | 7,08 | Natural |
| 1 | 218 | 222.717 | 350 | 3,3 s | 52,8 s | 7,05 | Natural |
| 1 | 219 | 223.740 | 205 | 2,4 s | 31,3 s | 7,05 | Natural |
| 1 | 220 | 224.765 | 363 | 2,7 s | 54,3 s | 7,02 | Natural |
| 1 | 221 | 225.789 | 200 | 3,1 s | 31,4 s | 7,02 | Natural |
| 1 | 222 | 226.813 | 353 | 3,5 s | 53,8 s | 6,99 | Natural |
| 1 | 223 | 227.837 | 207 | 2,6 s | 32,0 s | 6,99 | Natural |
| 1 | 224 | 228.861 | 366 | 2,9 s | 55,3 s | 6,97 | Natural |
| 1 | 225 | 229.885 | 199 | 3,5 s | 32,0 s | 6,97 | Natural |
| 1 | 226 | 230.908 | 354 | 2,5 s | 53,4 s | 6,94 | Natural |
| 1 | 227 | 231.933 | 205 | 2,9 s | 32,3 s | 6,94 | Natural |
| 1 | 228 | 232.957 | 365 | 3,4 s | 56,1 s | 6,91 | Natural |
| 1 | 229 | 233.980 | 199 | 2,4 s | 31,1 s | 6,92 | Natural |
| 1 | 230 | 235.004 | 354 | 2,8 s | 54,3 s | 6,84 | Natural |
| 1 | 231 | 236.029 | 205 | 3,5 s | 33,1 s | 6,88 | Natural |
| 1 | 232 | 237.053 | 363 | 2,5 s | 55,2 s | 6,86 | Natural |
| 1 | 233 | 238.077 | 200 | 2,8 s | 31,8 s | 6,86 | Natural |
| 1 | 234 | 239.101 | 353 | 3,0 s | 54,5 s | 6,83 | Natural |
| 1 | 235 | 240.125 | 205 | 3,7 s | 33,5 s | 6,84 | Natural |
| 1 | 236 | 241.149 | 364 | 2,6 s | 56,0 s | 6,80 | Natural |
| 1 | 237 | 242.173 | 200 | 3,0 s | 32,3 s | 6,81 | Natural |
| 1 | 238 | 243.197 | 355 | 3,7 s | 55,9 s | 6,78 | Natural |
| 1 | 239 | 244.221 | 205 | 2,7 s | 32,7 s | 6,79 | Natural |
| 1 | 240 | 245.245 | 366 | 2,9 s | 56,9 s | 6,75 | Natural |
| 1 | 241 | 246.269 | 200 | 3,6 s | 33,0 s | 6,75 | Natural |
| 1 | 242 | 247.292 | 356 | 2,6 s | 55,3 s | 6,73 | Natural |
| 1 | 243 | 248.317 | 206 | 2,9 s | 33,4 s | 6,73 | Natural |
| 1 | 244 | 249.341 | 371 | 3,7 s | 58,9 s | 6,70 | Natural |
| 1 | 245 | 250.365 | 200 | 2,6 s | 32,2 s | 6,70 | Natural |
| 1 | 246 | 251.389 | 361 | 2,8 s | 56,7 s | 6,68 | Natural |
| 1 | 247 | 252.413 | 207 | 3,2 s | 34,0 s | 6,68 | Natural |
| 1 | 248 | 253.437 | 375 | 3,8 s | 60,1 s | 6,65 | Natural |
| 1 | 249 | 254.461 | 201 | 2,8 s | 32,8 s | 6,66 | Natural |
| 1 | 250 | 255.485 | 366 | 3,2 s | 58,2 s | 6,63 | Natural |
| 1 | 251 | 256.509 | 209 | 3,8 s | 35,3 s | 6,62 | Natural |
| 1 | 252 | 257.533 | 377 | 2,6 s | 59,6 s | 6,60 | Natural |
| 1 | 253 | 258.557 | 203 | 3,0 s | 33,6 s | 6,61 | Natural |
| 1 | 254 | 259.580 | 368 | 3,7 s | 59,5 s | 6,58 | Natural |
| 1 | 255 | 260.605 | 209 | 2,6 s | 34,2 s | 6,58 | Natural |
| 1 | 256 | 261.117 | 379 | 2,2 s | 59,9 s | 6,56 | Natural |
| 1 | 257 | 262.013 | 15 | 2,4 s | 4,5 s | 6,84 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
