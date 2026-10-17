# 1 persona · 50% de memoria

[Volver a la capacidad por memoria](../README.md)

**Cumplió durante todo el recorrido.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **257/257 previstas**. Duración: **238,7 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.533–16.892 | 16/16 | 1,2 s | 1,2 s | 11,76 tokens/s | 18,2 s | Cumple |
| 18-33 | 17.917–33.277 | 16/16 | 1,2 s | 1,2 s | 11,15 tokens/s | 19,5 s | Cumple |
| 34-49 | 34.301–49.660 | 16/16 | 1,6 s | 1,6 s | 10,62 tokens/s | 20,5 s | Cumple |
| 50-65 | 50.685–66.045 | 16/16 | 1,7 s | 1,7 s | 10,14 tokens/s | 21,8 s | Cumple |
| 66-81 | 67.069–82.429 | 16/16 | 1,8 s | 1,8 s | 9,69 tokens/s | 23,4 s | Cumple |
| 82-97 | 83.453–98.813 | 16/16 | 2,1 s | 2,1 s | 9,29 tokens/s | 25,0 s | Cumple |
| 98-113 | 99.837–115.197 | 16/16 | 2,2 s | 2,2 s | 8,92 tokens/s | 26,5 s | Cumple |
| 114-129 | 116.221–131.581 | 16/16 | 2,4 s | 2,4 s | 8,58 tokens/s | 28,7 s | Cumple |
| 130-145 | 132.605–147.965 | 16/16 | 2,5 s | 2,5 s | 8,26 tokens/s | 30,2 s | Cumple |
| 146-161 | 148.989–164.349 | 16/16 | 2,8 s | 2,8 s | 7,96 tokens/s | 31,6 s | Cumple |
| 162-177 | 165.373–180.733 | 16/16 | 3,0 s | 3,0 s | 7,68 tokens/s | 32,5 s | Cumple |
| 178-193 | 181.756–197.117 | 16/16 | 3,1 s | 3,1 s | 7,43 tokens/s | 33,8 s | Cumple |
| 194-209 | 198.141–213.501 | 16/16 | 3,3 s | 3,3 s | 7,18 tokens/s | 35,2 s | Cumple |
| 210-225 | 214.525–229.885 | 16/16 | 3,6 s | 3,6 s | 6,96 tokens/s | 36,6 s | Cumple |
| 226-241 | 230.908–246.269 | 16/16 | 3,8 s | 3,8 s | 6,75 tokens/s | 38,4 s | Cumple |
| 242-257 | 247.293–262.013 | 16/16 | 3,9 s | 3,9 s | 6,57 tokens/s | 40,0 s | Cumple |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 257 | 262.029 | 99,956% | 115 |

El objetivo del cierre deja aproximadamente 128 tokens para la respuesta y pide terminar en diez palabras. El presupuesto efectivo se calcula con la entrada real. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento llegó al cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 50% |
| Pico de memoria del motor / GB10 | 46,6% |
| Pico de memoria total del sistema / GB10 | 55,3% |
| Pico de caché | 46,3% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 2,0 s |
| Espera media al primer token, incluido razonamiento | 2,0 s |
| Tiempo medio de petición completa | 25,3 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 3,59 tokens/s |
| Suma de tiempos individuales de petición | 6.509,6 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 257/257 | 2,0 s | 25,3 s | 14.318,8 s | 3,59 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 173 | 0,2 s | 14,1 s | 12,37 | Natural |
| 1 | 2 | 1.533 | 193 | 0,7 s | 16,2 s | 12,34 | Natural |
| 1 | 3 | 2.557 | 213 | 0,9 s | 18,1 s | 12,30 | Natural |
| 1 | 4 | 3.581 | 165 | 0,6 s | 14,0 s | 12,27 | Natural |
| 1 | 5 | 4.605 | 180 | 0,7 s | 15,3 s | 12,23 | Natural |
| 1 | 6 | 5.629 | 183 | 0,9 s | 15,8 s | 12,20 | Natural |
| 1 | 7 | 6.653 | 213 | 0,6 s | 18,1 s | 12,15 | Natural |
| 1 | 8 | 7.677 | 170 | 0,7 s | 14,7 s | 12,11 | Natural |
| 1 | 9 | 8.701 | 186 | 0,9 s | 16,2 s | 12,07 | Natural |
| 1 | 10 | 9.725 | 180 | 0,6 s | 15,5 s | 12,03 | Natural |
| 1 | 11 | 10.749 | 210 | 0,7 s | 18,2 s | 11,99 | Natural |
| 1 | 12 | 11.773 | 165 | 1,2 s | 14,9 s | 11,95 | Natural |
| 1 | 13 | 12.796 | 185 | 0,6 s | 16,1 s | 11,91 | Natural |
| 1 | 14 | 13.821 | 177 | 0,7 s | 15,5 s | 11,87 | Natural |
| 1 | 15 | 14.845 | 207 | 0,8 s | 18,2 s | 11,83 | Natural |
| 1 | 16 | 15.868 | 165 | 1,0 s | 14,9 s | 11,79 | Natural |
| 1 | 17 | 16.892 | 185 | 0,7 s | 16,3 s | 11,76 | Natural |
| 1 | 18 | 17.917 | 177 | 0,8 s | 15,8 s | 11,72 | Natural |
| 1 | 19 | 18.941 | 207 | 1,0 s | 18,7 s | 11,68 | Natural |
| 1 | 20 | 19.965 | 165 | 0,7 s | 14,8 s | 11,64 | Natural |
| 1 | 21 | 20.988 | 185 | 0,8 s | 16,7 s | 11,59 | Natural |
| 1 | 22 | 22.013 | 177 | 1,0 s | 16,3 s | 11,56 | Natural |
| 1 | 23 | 23.037 | 207 | 0,7 s | 18,6 s | 11,53 | Natural |
| 1 | 24 | 24.061 | 166 | 0,8 s | 15,2 s | 11,49 | Natural |
| 1 | 25 | 25.085 | 186 | 0,9 s | 17,1 s | 11,45 | Natural |
| 1 | 26 | 26.109 | 178 | 1,1 s | 16,7 s | 11,41 | Natural |
| 1 | 27 | 27.133 | 208 | 0,8 s | 19,0 s | 11,37 | Natural |
| 1 | 28 | 28.157 | 167 | 0,9 s | 15,6 s | 11,33 | Natural |
| 1 | 29 | 29.180 | 187 | 1,2 s | 17,6 s | 11,30 | Natural |
| 1 | 30 | 30.204 | 179 | 0,8 s | 16,6 s | 11,26 | Natural |
| 1 | 31 | 31.229 | 209 | 0,9 s | 19,5 s | 11,22 | Natural |
| 1 | 32 | 32.253 | 168 | 1,2 s | 16,1 s | 11,20 | Natural |
| 1 | 33 | 33.277 | 188 | 0,8 s | 17,6 s | 11,15 | Natural |
| 1 | 34 | 34.301 | 172 | 0,9 s | 16,3 s | 11,12 | Natural |
| 1 | 35 | 35.325 | 210 | 1,4 s | 20,3 s | 11,08 | Natural |
| 1 | 36 | 36.349 | 167 | 0,8 s | 15,8 s | 11,06 | Natural |
| 1 | 37 | 37.373 | 187 | 0,9 s | 17,8 s | 11,01 | Natural |
| 1 | 38 | 38.397 | 179 | 1,0 s | 17,2 s | 10,98 | Natural |
| 1 | 39 | 39.420 | 209 | 1,3 s | 20,3 s | 10,94 | Natural |
| 1 | 40 | 40.445 | 167 | 0,9 s | 16,1 s | 10,92 | Natural |
| 1 | 41 | 41.469 | 187 | 1,0 s | 18,1 s | 10,88 | Natural |
| 1 | 42 | 42.493 | 179 | 1,3 s | 17,7 s | 10,85 | Natural |
| 1 | 43 | 43.517 | 209 | 0,9 s | 20,1 s | 10,81 | Natural |
| 1 | 44 | 44.541 | 167 | 1,1 s | 16,4 s | 10,79 | Natural |
| 1 | 45 | 45.565 | 187 | 1,3 s | 18,6 s | 10,76 | Natural |
| 1 | 46 | 46.588 | 179 | 0,9 s | 17,5 s | 10,72 | Natural |
| 1 | 47 | 47.613 | 209 | 1,0 s | 20,5 s | 10,68 | Natural |
| 1 | 48 | 48.637 | 167 | 1,6 s | 17,1 s | 10,66 | Natural |
| 1 | 49 | 49.660 | 187 | 0,9 s | 18,4 s | 10,62 | Natural |
| 1 | 50 | 50.685 | 179 | 1,0 s | 17,8 s | 10,59 | Natural |
| 1 | 51 | 51.709 | 209 | 1,2 s | 21,2 s | 10,42 | Natural |
| 1 | 52 | 52.733 | 168 | 1,5 s | 17,3 s | 10,53 | Natural |
| 1 | 53 | 53.757 | 188 | 1,0 s | 18,8 s | 10,49 | Natural |
| 1 | 54 | 54.781 | 172 | 1,2 s | 17,5 s | 10,47 | Natural |
| 1 | 55 | 55.805 | 210 | 1,5 s | 21,5 s | 10,43 | Natural |
| 1 | 56 | 56.829 | 169 | 1,0 s | 17,1 s | 10,41 | Natural |
| 1 | 57 | 57.852 | 189 | 1,2 s | 19,3 s | 10,37 | Natural |
| 1 | 58 | 58.876 | 181 | 1,4 s | 18,9 s | 10,34 | Natural |
| 1 | 59 | 59.900 | 211 | 1,0 s | 21,4 s | 10,31 | Natural |
| 1 | 60 | 60.925 | 170 | 1,2 s | 17,6 s | 10,29 | Natural |
| 1 | 61 | 61.949 | 190 | 1,7 s | 20,1 s | 10,26 | Natural |
| 1 | 62 | 62.973 | 182 | 1,0 s | 18,7 s | 10,23 | Natural |
| 1 | 63 | 63.997 | 212 | 1,1 s | 21,8 s | 10,19 | Natural |
| 1 | 64 | 65.020 | 171 | 1,3 s | 18,0 s | 10,17 | Natural |
| 1 | 65 | 66.045 | 191 | 1,6 s | 20,3 s | 10,14 | Natural |
| 1 | 66 | 67.069 | 183 | 1,1 s | 19,1 s | 10,11 | Natural |
| 1 | 67 | 68.093 | 213 | 1,3 s | 22,3 s | 10,08 | Natural |
| 1 | 68 | 69.117 | 172 | 1,6 s | 18,6 s | 10,05 | Natural |
| 1 | 69 | 70.141 | 192 | 1,1 s | 20,2 s | 10,03 | Natural |
| 1 | 70 | 71.165 | 176 | 1,3 s | 18,8 s | 10,00 | Natural |
| 1 | 71 | 72.189 | 214 | 1,8 s | 23,2 s | 9,97 | Natural |
| 1 | 72 | 73.213 | 173 | 1,1 s | 18,4 s | 9,95 | Natural |
| 1 | 73 | 74.237 | 193 | 1,3 s | 20,6 s | 9,92 | Natural |
| 1 | 74 | 75.261 | 185 | 1,5 s | 20,1 s | 9,89 | Natural |
| 1 | 75 | 76.284 | 215 | 1,7 s | 23,4 s | 9,86 | Natural |
| 1 | 76 | 77.309 | 174 | 1,2 s | 18,8 s | 9,84 | Natural |
| 1 | 77 | 78.333 | 194 | 1,4 s | 21,1 s | 9,80 | Natural |
| 1 | 78 | 79.357 | 186 | 1,8 s | 20,7 s | 9,78 | Natural |
| 1 | 79 | 80.381 | 216 | 1,2 s | 23,3 s | 9,75 | Natural |
| 1 | 80 | 81.405 | 175 | 1,4 s | 19,3 s | 9,72 | Natural |
| 1 | 81 | 82.429 | 195 | 1,7 s | 21,7 s | 9,69 | Natural |
| 1 | 82 | 83.453 | 179 | 1,2 s | 19,6 s | 9,68 | Natural |
| 1 | 83 | 84.477 | 217 | 1,4 s | 23,8 s | 9,64 | Natural |
| 1 | 84 | 85.501 | 176 | 1,8 s | 20,0 s | 9,62 | Natural |
| 1 | 85 | 86.525 | 196 | 1,2 s | 21,6 s | 9,60 | Natural |
| 1 | 86 | 87.549 | 188 | 1,4 s | 21,0 s | 9,57 | Natural |
| 1 | 87 | 88.573 | 218 | 1,5 s | 24,3 s | 9,54 | Natural |
| 1 | 88 | 89.596 | 177 | 1,9 s | 20,4 s | 9,52 | Natural |
| 1 | 89 | 90.621 | 197 | 1,3 s | 22,0 s | 9,50 | Natural |
| 1 | 90 | 91.645 | 189 | 1,5 s | 21,4 s | 9,47 | Natural |
| 1 | 91 | 92.669 | 219 | 1,9 s | 25,0 s | 9,43 | Natural |
| 1 | 92 | 93.693 | 178 | 1,3 s | 20,1 s | 9,41 | Natural |
| 1 | 93 | 94.717 | 198 | 1,5 s | 22,5 s | 9,39 | Natural |
| 1 | 94 | 95.741 | 182 | 1,9 s | 21,2 s | 9,37 | Natural |
| 1 | 95 | 96.765 | 220 | 1,3 s | 24,8 s | 9,34 | Natural |
| 1 | 96 | 97.789 | 179 | 1,5 s | 20,6 s | 9,32 | Natural |
| 1 | 97 | 98.813 | 199 | 2,1 s | 23,4 s | 9,29 | Natural |
| 1 | 98 | 99.837 | 183 | 1,3 s | 20,9 s | 9,28 | Natural |
| 1 | 99 | 100.860 | 221 | 1,4 s | 25,2 s | 9,25 | Natural |
| 1 | 100 | 101.885 | 180 | 1,7 s | 21,1 s | 9,22 | Natural |
| 1 | 101 | 102.909 | 200 | 2,0 s | 23,7 s | 9,19 | Natural |
| 1 | 102 | 103.933 | 192 | 1,4 s | 22,3 s | 9,18 | Natural |
| 1 | 103 | 104.957 | 222 | 1,7 s | 25,9 s | 9,15 | Natural |
| 1 | 104 | 105.981 | 181 | 2,1 s | 21,8 s | 9,13 | Natural |
| 1 | 105 | 107.005 | 201 | 1,4 s | 23,4 s | 9,10 | Natural |
| 1 | 106 | 108.029 | 185 | 1,6 s | 21,9 s | 9,08 | Natural |
| 1 | 107 | 109.052 | 223 | 2,0 s | 26,5 s | 9,06 | Natural |
| 1 | 108 | 110.077 | 182 | 1,4 s | 21,4 s | 9,04 | Natural |
| 1 | 109 | 111.101 | 202 | 1,6 s | 23,9 s | 9,01 | Natural |
| 1 | 110 | 112.125 | 186 | 2,2 s | 22,8 s | 8,99 | Natural |
| 1 | 111 | 113.149 | 224 | 1,3 s | 26,2 s | 8,96 | Natural |
| 1 | 112 | 114.173 | 183 | 1,6 s | 21,9 s | 8,94 | Natural |
| 1 | 113 | 115.197 | 203 | 1,8 s | 24,4 s | 8,92 | Natural |
| 1 | 114 | 116.221 | 187 | 2,2 s | 23,1 s | 8,90 | Natural |
| 1 | 115 | 117.245 | 225 | 1,6 s | 26,8 s | 8,87 | Natural |
| 1 | 116 | 118.269 | 184 | 1,8 s | 22,5 s | 8,85 | Natural |
| 1 | 117 | 119.293 | 204 | 2,2 s | 25,2 s | 8,83 | Natural |
| 1 | 118 | 120.317 | 188 | 1,5 s | 22,7 s | 8,80 | Natural |
| 1 | 119 | 121.341 | 226 | 1,7 s | 27,4 s | 8,78 | Natural |
| 1 | 120 | 122.365 | 185 | 2,2 s | 23,2 s | 8,76 | Natural |
| 1 | 121 | 123.389 | 205 | 1,6 s | 25,0 s | 8,70 | Natural |
| 1 | 122 | 124.413 | 197 | 1,7 s | 24,2 s | 8,72 | Natural |
| 1 | 123 | 125.437 | 227 | 2,0 s | 28,0 s | 8,69 | Natural |
| 1 | 124 | 126.461 | 186 | 2,3 s | 23,6 s | 8,68 | Natural |
| 1 | 125 | 127.485 | 206 | 1,6 s | 25,3 s | 8,65 | Natural |
| 1 | 126 | 128.509 | 198 | 2,0 s | 24,8 s | 8,64 | Natural |
| 1 | 127 | 129.532 | 228 | 2,4 s | 28,7 s | 8,61 | Natural |
| 1 | 128 | 130.556 | 187 | 1,7 s | 23,3 s | 8,60 | Natural |
| 1 | 129 | 131.581 | 207 | 2,0 s | 26,0 s | 8,58 | Natural |
| 1 | 130 | 132.605 | 191 | 2,3 s | 24,5 s | 8,56 | Natural |
| 1 | 131 | 133.629 | 229 | 1,6 s | 28,3 s | 8,53 | Natural |
| 1 | 132 | 134.653 | 188 | 1,9 s | 23,8 s | 8,52 | Natural |
| 1 | 133 | 135.677 | 208 | 2,5 s | 26,9 s | 8,49 | Natural |
| 1 | 134 | 136.701 | 200 | 1,7 s | 25,1 s | 8,48 | Natural |
| 1 | 135 | 137.725 | 230 | 1,9 s | 29,0 s | 8,45 | Natural |
| 1 | 136 | 138.749 | 189 | 2,0 s | 24,3 s | 8,43 | Natural |
| 1 | 137 | 139.773 | 209 | 2,5 s | 27,2 s | 8,41 | Natural |
| 1 | 138 | 140.797 | 201 | 1,8 s | 25,6 s | 8,39 | Natural |
| 1 | 139 | 141.821 | 231 | 2,1 s | 29,5 s | 8,37 | Natural |
| 1 | 140 | 142.845 | 189 | 2,5 s | 25,1 s | 8,35 | Natural |
| 1 | 141 | 143.868 | 209 | 1,8 s | 26,8 s | 8,33 | Natural |
| 1 | 142 | 144.893 | 193 | 2,0 s | 25,1 s | 8,30 | Natural |
| 1 | 143 | 145.917 | 231 | 2,5 s | 30,2 s | 8,29 | Natural |
| 1 | 144 | 146.941 | 189 | 1,7 s | 24,4 s | 8,27 | Natural |
| 1 | 145 | 147.965 | 209 | 2,0 s | 27,2 s | 8,26 | Natural |
| 1 | 146 | 148.989 | 193 | 2,6 s | 25,9 s | 8,24 | Natural |
| 1 | 147 | 150.013 | 231 | 1,7 s | 29,8 s | 8,21 | Natural |
| 1 | 148 | 151.036 | 189 | 1,9 s | 24,8 s | 8,20 | Natural |
| 1 | 149 | 152.061 | 209 | 2,2 s | 27,6 s | 8,18 | Natural |
| 1 | 150 | 153.085 | 201 | 2,7 s | 27,2 s | 8,16 | Natural |
| 1 | 151 | 154.109 | 231 | 1,9 s | 30,2 s | 8,14 | Natural |
| 1 | 152 | 155.133 | 189 | 2,2 s | 25,3 s | 8,12 | Natural |
| 1 | 153 | 156.157 | 209 | 2,7 s | 28,4 s | 8,10 | Natural |
| 1 | 154 | 157.181 | 193 | 1,8 s | 25,6 s | 8,09 | Natural |
| 1 | 155 | 158.205 | 231 | 2,1 s | 30,6 s | 8,07 | Natural |
| 1 | 156 | 159.229 | 189 | 2,6 s | 26,0 s | 8,05 | Natural |
| 1 | 157 | 160.253 | 209 | 1,9 s | 27,8 s | 8,03 | Natural |
| 1 | 158 | 161.277 | 193 | 2,1 s | 26,1 s | 8,02 | Natural |
| 1 | 159 | 162.301 | 231 | 2,8 s | 31,6 s | 7,99 | Natural |
| 1 | 160 | 163.325 | 189 | 1,7 s | 25,3 s | 7,98 | Natural |
| 1 | 161 | 164.349 | 209 | 2,0 s | 28,1 s | 7,96 | Natural |
| 1 | 162 | 165.373 | 201 | 2,3 s | 27,5 s | 7,95 | Natural |
| 1 | 163 | 166.397 | 231 | 2,8 s | 31,9 s | 7,92 | Natural |
| 1 | 164 | 167.421 | 189 | 2,0 s | 25,8 s | 7,91 | Natural |
| 1 | 165 | 168.445 | 209 | 2,3 s | 28,7 s | 7,89 | Natural |
| 1 | 166 | 169.469 | 193 | 2,7 s | 27,1 s | 7,87 | Natural |
| 1 | 167 | 170.493 | 231 | 2,0 s | 31,2 s | 7,85 | Natural |
| 1 | 168 | 171.517 | 190 | 2,3 s | 26,4 s | 7,84 | Natural |
| 1 | 169 | 172.541 | 210 | 2,8 s | 29,5 s | 7,82 | Natural |
| 1 | 170 | 173.565 | 194 | 2,0 s | 26,7 s | 7,81 | Natural |
| 1 | 171 | 174.588 | 232 | 2,3 s | 31,9 s | 7,78 | Natural |
| 1 | 172 | 175.613 | 191 | 2,5 s | 27,0 s | 7,77 | Natural |
| 1 | 173 | 176.637 | 211 | 2,9 s | 30,0 s | 7,75 | Natural |
| 1 | 174 | 177.661 | 195 | 2,1 s | 27,2 s | 7,73 | Natural |
| 1 | 175 | 178.685 | 233 | 2,4 s | 32,5 s | 7,72 | Natural |
| 1 | 176 | 179.709 | 192 | 3,0 s | 27,8 s | 7,70 | Natural |
| 1 | 177 | 180.733 | 212 | 2,2 s | 29,6 s | 7,68 | Natural |
| 1 | 178 | 181.756 | 196 | 2,4 s | 27,9 s | 7,67 | Natural |
| 1 | 179 | 182.781 | 234 | 2,9 s | 33,4 s | 7,65 | Natural |
| 1 | 180 | 183.805 | 192 | 2,1 s | 27,1 s | 7,64 | Natural |
| 1 | 181 | 184.829 | 212 | 2,4 s | 30,1 s | 7,62 | Natural |
| 1 | 182 | 185.853 | 196 | 2,9 s | 28,6 s | 7,59 | Natural |
| 1 | 183 | 186.876 | 234 | 2,0 s | 32,8 s | 7,58 | Natural |
| 1 | 184 | 187.901 | 193 | 2,4 s | 27,7 s | 7,57 | Natural |
| 1 | 185 | 188.924 | 213 | 2,5 s | 30,6 s | 7,55 | Natural |
| 1 | 186 | 189.949 | 205 | 3,1 s | 30,2 s | 7,53 | Natural |
| 1 | 187 | 190.973 | 235 | 2,2 s | 33,3 s | 7,52 | Natural |
| 1 | 188 | 191.997 | 193 | 2,6 s | 28,1 s | 7,51 | Natural |
| 1 | 189 | 193.021 | 213 | 3,1 s | 31,4 s | 7,49 | Natural |
| 1 | 190 | 194.045 | 205 | 2,2 s | 29,5 s | 7,48 | Natural |
| 1 | 191 | 195.069 | 235 | 2,5 s | 33,8 s | 7,46 | Natural |
| 1 | 192 | 196.092 | 193 | 3,1 s | 28,8 s | 7,45 | Natural |
| 1 | 193 | 197.117 | 213 | 2,2 s | 30,7 s | 7,43 | Natural |
| 1 | 194 | 198.141 | 205 | 2,4 s | 30,0 s | 7,41 | Natural |
| 1 | 195 | 199.165 | 235 | 3,2 s | 34,8 s | 7,40 | Natural |
| 1 | 196 | 200.189 | 193 | 2,2 s | 28,2 s | 7,39 | Natural |
| 1 | 197 | 201.213 | 213 | 2,3 s | 31,1 s | 7,36 | Natural |
| 1 | 198 | 202.237 | 197 | 2,7 s | 29,3 s | 7,35 | Natural |
| 1 | 199 | 203.261 | 235 | 3,3 s | 35,2 s | 7,33 | Natural |
| 1 | 200 | 204.285 | 193 | 2,3 s | 28,5 s | 7,32 | Natural |
| 1 | 201 | 205.308 | 213 | 2,7 s | 31,7 s | 7,30 | Natural |
| 1 | 202 | 206.333 | 197 | 3,3 s | 30,2 s | 7,29 | Natural |
| 1 | 203 | 207.357 | 235 | 2,2 s | 34,4 s | 7,27 | Natural |
| 1 | 204 | 208.381 | 194 | 2,6 s | 29,2 s | 7,27 | Natural |
| 1 | 205 | 209.405 | 214 | 3,1 s | 32,6 s | 7,24 | Natural |
| 1 | 206 | 210.429 | 206 | 2,2 s | 30,6 s | 7,24 | Natural |
| 1 | 207 | 211.453 | 236 | 2,6 s | 35,2 s | 7,22 | Natural |
| 1 | 208 | 212.477 | 194 | 3,2 s | 30,0 s | 7,21 | Natural |
| 1 | 209 | 213.501 | 214 | 2,1 s | 31,8 s | 7,18 | Natural |
| 1 | 210 | 214.525 | 198 | 2,5 s | 29,9 s | 7,18 | Natural |
| 1 | 211 | 215.549 | 236 | 2,8 s | 35,7 s | 7,16 | Natural |
| 1 | 212 | 216.573 | 195 | 3,4 s | 30,6 s | 7,14 | Natural |
| 1 | 213 | 217.597 | 215 | 2,4 s | 32,5 s | 7,13 | Natural |
| 1 | 214 | 218.621 | 207 | 2,8 s | 31,8 s | 7,12 | Natural |
| 1 | 215 | 219.645 | 237 | 3,3 s | 36,6 s | 7,10 | Natural |
| 1 | 216 | 220.669 | 195 | 2,3 s | 29,7 s | 7,09 | Natural |
| 1 | 217 | 221.693 | 215 | 2,7 s | 33,0 s | 7,08 | Natural |
| 1 | 218 | 222.717 | 199 | 3,3 s | 31,4 s | 7,06 | Natural |
| 1 | 219 | 223.741 | 237 | 2,4 s | 35,9 s | 7,04 | Natural |
| 1 | 220 | 224.765 | 195 | 2,7 s | 30,3 s | 7,04 | Natural |
| 1 | 221 | 225.789 | 215 | 3,1 s | 33,6 s | 7,01 | Natural |
| 1 | 222 | 226.813 | 207 | 3,6 s | 33,0 s | 7,01 | Natural |
| 1 | 223 | 227.837 | 237 | 2,5 s | 36,3 s | 6,98 | Natural |
| 1 | 224 | 228.861 | 196 | 3,0 s | 30,9 s | 6,97 | Natural |
| 1 | 225 | 229.885 | 216 | 3,6 s | 34,5 s | 6,96 | Natural |
| 1 | 226 | 230.908 | 208 | 2,6 s | 32,3 s | 6,95 | Natural |
| 1 | 227 | 231.933 | 230 | 3,0 s | 36,0 s | 6,94 | Natural |
| 1 | 228 | 232.957 | 196 | 3,4 s | 31,6 s | 6,92 | Natural |
| 1 | 229 | 233.981 | 216 | 2,5 s | 33,6 s | 6,91 | Natural |
| 1 | 230 | 235.005 | 200 | 2,8 s | 31,7 s | 6,90 | Natural |
| 1 | 231 | 236.029 | 238 | 3,5 s | 37,9 s | 6,88 | Natural |
| 1 | 232 | 237.053 | 196 | 2,5 s | 30,8 s | 6,87 | Natural |
| 1 | 233 | 238.077 | 216 | 2,9 s | 34,2 s | 6,85 | Natural |
| 1 | 234 | 239.100 | 208 | 3,0 s | 33,3 s | 6,84 | Natural |
| 1 | 235 | 240.125 | 238 | 3,7 s | 38,4 s | 6,82 | Natural |
| 1 | 236 | 241.149 | 197 | 2,7 s | 31,4 s | 6,82 | Natural |
| 1 | 237 | 242.173 | 217 | 3,1 s | 34,8 s | 6,80 | Natural |
| 1 | 238 | 243.197 | 201 | 3,8 s | 33,2 s | 6,81 | Natural |
| 1 | 239 | 244.221 | 239 | 2,7 s | 37,9 s | 6,77 | Natural |
| 1 | 240 | 245.245 | 197 | 3,1 s | 32,1 s | 6,75 | Natural |
| 1 | 241 | 246.269 | 217 | 3,6 s | 35,6 s | 6,75 | Natural |
| 1 | 242 | 247.293 | 201 | 2,6 s | 32,2 s | 6,74 | Natural |
| 1 | 243 | 248.317 | 239 | 3,0 s | 38,4 s | 6,73 | Natural |
| 1 | 244 | 249.341 | 197 | 3,6 s | 32,8 s | 6,71 | Natural |
| 1 | 245 | 250.364 | 217 | 2,6 s | 34,8 s | 6,70 | Natural |
| 1 | 246 | 251.388 | 209 | 2,7 s | 33,8 s | 6,69 | Natural |
| 1 | 247 | 252.413 | 239 | 3,2 s | 38,9 s | 6,67 | Natural |
| 1 | 248 | 253.437 | 198 | 3,9 s | 33,4 s | 6,67 | Natural |
| 1 | 249 | 254.461 | 218 | 2,8 s | 35,4 s | 6,65 | Natural |
| 1 | 250 | 255.484 | 210 | 3,2 s | 34,7 s | 6,64 | Natural |
| 1 | 251 | 256.509 | 240 | 3,9 s | 40,0 s | 6,62 | Natural |
| 1 | 252 | 257.533 | 198 | 2,6 s | 32,4 s | 6,61 | Natural |
| 1 | 253 | 258.556 | 218 | 3,1 s | 36,0 s | 6,60 | Natural |
| 1 | 254 | 259.581 | 210 | 3,7 s | 35,5 s | 6,59 | Natural |
| 1 | 255 | 260.605 | 240 | 2,7 s | 39,0 s | 6,57 | Natural |
| 1 | 256 | 261.117 | 198 | 2,3 s | 32,3 s | 6,58 | Natural |
| 1 | 257 | 262.013 | 16 | 2,4 s | 4,6 s | 6,89 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
