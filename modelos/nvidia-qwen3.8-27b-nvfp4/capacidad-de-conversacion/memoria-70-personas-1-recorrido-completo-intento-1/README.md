# 1 persona · 70% de memoria

[Volver a la capacidad por memoria](../README.md)

**Cumplió durante todo el recorrido.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **257/257 previstas**. Duración: **248,1 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.533–16.893 | 16/16 | 1,2 s | 1,2 s | 11,75 tokens/s | 18,1 s | Cumple |
| 18-33 | 17.917–33.277 | 16/16 | 1,3 s | 1,3 s | 10,98 tokens/s | 17,5 s | Cumple |
| 34-49 | 34.301–49.661 | 16/16 | 1,6 s | 1,6 s | 10,64 tokens/s | 20,3 s | Cumple |
| 50-65 | 50.685–66.045 | 16/16 | 1,7 s | 1,7 s | 10,14 tokens/s | 23,3 s | Cumple |
| 66-81 | 67.069–82.429 | 16/16 | 1,7 s | 1,7 s | 9,70 tokens/s | 27,1 s | Cumple |
| 82-97 | 83.453–98.813 | 16/16 | 2,0 s | 2,0 s | 9,29 tokens/s | 30,5 s | Cumple |
| 98-113 | 99.837–115.197 | 16/16 | 2,2 s | 2,2 s | 8,92 tokens/s | 34,1 s | Cumple |
| 114-129 | 116.221–131.581 | 16/16 | 2,3 s | 2,3 s | 8,57 tokens/s | 35,3 s | Cumple |
| 130-145 | 132.604–147.965 | 16/16 | 2,5 s | 2,5 s | 8,26 tokens/s | 37,6 s | Cumple |
| 146-161 | 148.989–164.349 | 16/16 | 2,8 s | 2,8 s | 7,96 tokens/s | 39,7 s | Cumple |
| 162-177 | 165.373–180.733 | 16/16 | 3,0 s | 3,0 s | 7,68 tokens/s | 42,4 s | Cumple |
| 178-193 | 181.757–197.117 | 16/16 | 3,1 s | 3,1 s | 7,42 tokens/s | 45,1 s | Cumple |
| 194-209 | 198.141–213.501 | 16/16 | 3,3 s | 3,3 s | 7,18 tokens/s | 48,4 s | Cumple |
| 210-225 | 214.525–229.885 | 16/16 | 3,5 s | 3,5 s | 6,95 tokens/s | 54,1 s | Cumple |
| 226-241 | 230.909–246.269 | 16/16 | 3,7 s | 3,7 s | 6,73 tokens/s | 58,9 s | Cumple |
| 242-257 | 247.293–262.013 | 16/16 | 3,9 s | 3,9 s | 6,55 tokens/s | 63,7 s | Cumple |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 257 | 262.029 | 99,956% | 115 |

El cierre previsto reserva hasta 128 tokens y pide terminar en diez palabras. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento llegó al cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 70% |
| Pico de memoria del motor / GB10 | 66,8% |
| Pico de memoria total del sistema / GB10 | 75,9% |
| Pico de caché | 27,1% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto del modelo | 1,9 s |
| Tiempo medio de petición completa | 27,5 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 3,69 tokens/s |
| Suma de tiempos individuales de petición | 7.075,0 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 257/257 | 1,9 s | 27,5 s | 14.885,1 s | 3,69 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 168 | 0,3 s | 13,7 s | 12,39 | Natural |
| 1 | 2 | 1.533 | 216 | 0,7 s | 18,1 s | 12,34 | Natural |
| 1 | 3 | 2.557 | 129 | 0,8 s | 11,2 s | 12,31 | Natural |
| 1 | 4 | 3.581 | 155 | 0,6 s | 13,1 s | 12,27 | Natural |
| 1 | 5 | 4.605 | 150 | 0,7 s | 12,9 s | 12,23 | Natural |
| 1 | 6 | 5.628 | 184 | 0,8 s | 15,9 s | 12,19 | Natural |
| 1 | 7 | 6.653 | 131 | 0,6 s | 11,3 s | 12,15 | Natural |
| 1 | 8 | 7.677 | 152 | 0,7 s | 13,2 s | 12,11 | Natural |
| 1 | 9 | 8.701 | 150 | 1,2 s | 13,5 s | 12,07 | Natural |
| 1 | 10 | 9.725 | 181 | 0,6 s | 15,5 s | 12,03 | Natural |
| 1 | 11 | 10.749 | 131 | 0,7 s | 11,5 s | 11,99 | Natural |
| 1 | 12 | 11.773 | 150 | 1,2 s | 13,6 s | 11,96 | Natural |
| 1 | 13 | 12.797 | 149 | 0,6 s | 13,0 s | 11,91 | Natural |
| 1 | 14 | 13.821 | 179 | 0,7 s | 15,7 s | 11,88 | Natural |
| 1 | 15 | 14.845 | 130 | 0,8 s | 11,7 s | 11,83 | Natural |
| 1 | 16 | 15.869 | 148 | 1,0 s | 13,5 s | 11,79 | Natural |
| 1 | 17 | 16.893 | 149 | 0,7 s | 13,3 s | 11,75 | Natural |
| 1 | 18 | 17.917 | 177 | 0,8 s | 15,8 s | 11,71 | Natural |
| 1 | 19 | 18.941 | 130 | 1,0 s | 12,0 s | 11,68 | Natural |
| 1 | 20 | 19.965 | 150 | 0,7 s | 13,5 s | 11,64 | Natural |
| 1 | 21 | 20.989 | 149 | 0,8 s | 13,5 s | 11,60 | Natural |
| 1 | 22 | 22.013 | 179 | 1,3 s | 16,7 s | 11,57 | Natural |
| 1 | 23 | 23.037 | 130 | 0,7 s | 11,9 s | 11,53 | Natural |
| 1 | 24 | 24.061 | 155 | 0,8 s | 14,2 s | 11,49 | Natural |
| 1 | 25 | 25.085 | 150 | 0,9 s | 13,9 s | 11,45 | Natural |
| 1 | 26 | 26.109 | 184 | 1,1 s | 17,2 s | 11,41 | Natural |
| 1 | 27 | 27.133 | 131 | 0,8 s | 12,2 s | 11,38 | Natural |
| 1 | 28 | 28.157 | 160 | 0,9 s | 14,9 s | 11,34 | Natural |
| 1 | 29 | 29.181 | 151 | 1,1 s | 14,4 s | 11,31 | Natural |
| 1 | 30 | 30.204 | 189 | 0,8 s | 17,5 s | 11,26 | Natural |
| 1 | 31 | 31.229 | 132 | 0,9 s | 12,9 s | 10,98 | Natural |
| 1 | 32 | 32.253 | 165 | 1,1 s | 15,8 s | 11,19 | Natural |
| 1 | 33 | 33.277 | 152 | 0,8 s | 14,3 s | 11,16 | Natural |
| 1 | 34 | 34.301 | 194 | 0,9 s | 18,3 s | 11,12 | Natural |
| 1 | 35 | 35.325 | 133 | 1,4 s | 13,3 s | 11,09 | Natural |
| 1 | 36 | 36.349 | 170 | 0,8 s | 16,1 s | 11,06 | Natural |
| 1 | 37 | 37.373 | 153 | 0,9 s | 14,7 s | 11,02 | Natural |
| 1 | 38 | 38.397 | 199 | 1,0 s | 19,1 s | 10,98 | Natural |
| 1 | 39 | 39.421 | 134 | 1,3 s | 13,4 s | 10,95 | Natural |
| 1 | 40 | 40.445 | 175 | 0,9 s | 16,8 s | 10,92 | Natural |
| 1 | 41 | 41.469 | 154 | 1,0 s | 15,1 s | 10,89 | Natural |
| 1 | 42 | 42.493 | 204 | 1,3 s | 20,0 s | 10,85 | Natural |
| 1 | 43 | 43.517 | 135 | 0,9 s | 13,3 s | 10,83 | Natural |
| 1 | 44 | 44.541 | 180 | 1,0 s | 17,6 s | 10,79 | Natural |
| 1 | 45 | 45.565 | 155 | 1,3 s | 15,6 s | 10,76 | Natural |
| 1 | 46 | 46.589 | 209 | 0,9 s | 20,3 s | 10,72 | Natural |
| 1 | 47 | 47.613 | 136 | 1,1 s | 13,7 s | 10,70 | Natural |
| 1 | 48 | 48.637 | 185 | 1,6 s | 18,8 s | 10,67 | Natural |
| 1 | 49 | 49.661 | 156 | 0,9 s | 15,5 s | 10,64 | Natural |
| 1 | 50 | 50.685 | 214 | 1,0 s | 21,1 s | 10,59 | Natural |
| 1 | 51 | 51.709 | 137 | 1,2 s | 14,0 s | 10,57 | Natural |
| 1 | 52 | 52.733 | 190 | 1,4 s | 19,4 s | 10,53 | Natural |
| 1 | 53 | 53.757 | 157 | 1,0 s | 15,9 s | 10,50 | Natural |
| 1 | 54 | 54.781 | 219 | 1,2 s | 22,0 s | 10,47 | Natural |
| 1 | 55 | 55.804 | 138 | 1,5 s | 14,6 s | 10,45 | Natural |
| 1 | 56 | 56.829 | 195 | 1,0 s | 19,6 s | 10,41 | Natural |
| 1 | 57 | 57.853 | 158 | 1,1 s | 16,3 s | 10,38 | Natural |
| 1 | 58 | 58.877 | 224 | 1,7 s | 23,2 s | 10,34 | Natural |
| 1 | 59 | 59.901 | 139 | 1,0 s | 14,4 s | 10,33 | Natural |
| 1 | 60 | 60.925 | 200 | 1,2 s | 20,5 s | 10,29 | Natural |
| 1 | 61 | 61.949 | 159 | 1,7 s | 17,1 s | 10,26 | Natural |
| 1 | 62 | 62.973 | 229 | 1,0 s | 23,3 s | 10,22 | Natural |
| 1 | 63 | 63.996 | 140 | 1,1 s | 14,7 s | 10,21 | Natural |
| 1 | 64 | 65.021 | 205 | 1,3 s | 21,3 s | 10,16 | Natural |
| 1 | 65 | 66.045 | 160 | 1,6 s | 17,3 s | 10,14 | Natural |
| 1 | 66 | 67.069 | 234 | 1,1 s | 24,2 s | 10,10 | Natural |
| 1 | 67 | 68.092 | 141 | 1,3 s | 15,2 s | 10,09 | Natural |
| 1 | 68 | 69.117 | 210 | 1,6 s | 22,4 s | 10,05 | Natural |
| 1 | 69 | 70.141 | 161 | 1,1 s | 17,0 s | 10,02 | Natural |
| 1 | 70 | 71.165 | 239 | 1,3 s | 25,1 s | 9,99 | Natural |
| 1 | 71 | 72.189 | 142 | 1,6 s | 15,7 s | 9,98 | Natural |
| 1 | 72 | 73.213 | 215 | 1,1 s | 22,6 s | 9,94 | Natural |
| 1 | 73 | 74.237 | 162 | 1,3 s | 17,5 s | 9,91 | Natural |
| 1 | 74 | 75.261 | 244 | 1,4 s | 26,0 s | 9,88 | Natural |
| 1 | 75 | 76.285 | 143 | 1,7 s | 16,1 s | 9,86 | Natural |
| 1 | 76 | 77.309 | 220 | 1,2 s | 23,5 s | 9,82 | Natural |
| 1 | 77 | 78.332 | 163 | 1,4 s | 17,9 s | 9,80 | Natural |
| 1 | 78 | 79.357 | 249 | 1,7 s | 27,1 s | 9,76 | Natural |
| 1 | 79 | 80.381 | 144 | 1,2 s | 15,9 s | 9,76 | Natural |
| 1 | 80 | 81.404 | 225 | 1,4 s | 24,5 s | 9,71 | Natural |
| 1 | 81 | 82.429 | 164 | 1,7 s | 18,5 s | 9,70 | Natural |
| 1 | 82 | 83.453 | 254 | 1,2 s | 27,4 s | 9,66 | Natural |
| 1 | 83 | 84.477 | 145 | 1,4 s | 16,3 s | 9,64 | Natural |
| 1 | 84 | 85.501 | 230 | 2,0 s | 25,8 s | 9,61 | Natural |
| 1 | 85 | 86.525 | 165 | 1,2 s | 18,3 s | 9,59 | Natural |
| 1 | 86 | 87.549 | 259 | 1,4 s | 28,4 s | 9,56 | Natural |
| 1 | 87 | 88.572 | 146 | 1,5 s | 16,7 s | 9,55 | Natural |
| 1 | 88 | 89.596 | 235 | 1,9 s | 26,5 s | 9,50 | Natural |
| 1 | 89 | 90.621 | 166 | 1,3 s | 18,7 s | 9,49 | Natural |
| 1 | 90 | 91.645 | 264 | 1,5 s | 29,4 s | 9,45 | Natural |
| 1 | 91 | 92.669 | 147 | 1,9 s | 17,4 s | 9,44 | Natural |
| 1 | 92 | 93.693 | 240 | 1,3 s | 26,8 s | 9,41 | Natural |
| 1 | 93 | 94.717 | 167 | 1,5 s | 19,2 s | 9,39 | Natural |
| 1 | 94 | 95.741 | 269 | 1,9 s | 30,5 s | 9,35 | Natural |
| 1 | 95 | 96.765 | 148 | 1,3 s | 17,0 s | 9,35 | Natural |
| 1 | 96 | 97.788 | 245 | 1,5 s | 27,7 s | 9,31 | Natural |
| 1 | 97 | 98.813 | 168 | 1,9 s | 19,9 s | 9,29 | Natural |
| 1 | 98 | 99.837 | 274 | 1,3 s | 30,8 s | 9,26 | Natural |
| 1 | 99 | 100.861 | 149 | 1,4 s | 17,4 s | 9,25 | Natural |
| 1 | 100 | 101.885 | 250 | 1,7 s | 28,7 s | 9,21 | Natural |
| 1 | 101 | 102.909 | 169 | 2,0 s | 20,3 s | 9,19 | Natural |
| 1 | 102 | 103.933 | 279 | 1,5 s | 31,8 s | 9,15 | Natural |
| 1 | 103 | 104.957 | 150 | 1,7 s | 18,3 s | 8,93 | Natural |
| 1 | 104 | 105.981 | 255 | 2,1 s | 29,9 s | 9,11 | Natural |
| 1 | 105 | 107.005 | 170 | 1,4 s | 20,0 s | 9,09 | Natural |
| 1 | 106 | 108.029 | 284 | 1,7 s | 32,9 s | 9,06 | Natural |
| 1 | 107 | 109.053 | 151 | 2,0 s | 18,6 s | 9,05 | Natural |
| 1 | 108 | 110.077 | 258 | 1,4 s | 29,9 s | 9,02 | Natural |
| 1 | 109 | 111.101 | 171 | 1,6 s | 20,5 s | 9,00 | Natural |
| 1 | 110 | 112.125 | 287 | 2,2 s | 34,1 s | 8,97 | Natural |
| 1 | 111 | 113.149 | 152 | 1,3 s | 18,2 s | 8,96 | Natural |
| 1 | 112 | 114.173 | 258 | 1,5 s | 30,3 s | 8,93 | Natural |
| 1 | 113 | 115.197 | 171 | 1,8 s | 20,9 s | 8,92 | Natural |
| 1 | 114 | 116.221 | 287 | 2,2 s | 34,4 s | 8,88 | Natural |
| 1 | 115 | 117.245 | 152 | 1,6 s | 18,6 s | 8,87 | Natural |
| 1 | 116 | 118.269 | 258 | 1,8 s | 30,9 s | 8,84 | Natural |
| 1 | 117 | 119.293 | 171 | 2,2 s | 21,4 s | 8,83 | Natural |
| 1 | 118 | 120.317 | 287 | 1,5 s | 34,0 s | 8,79 | Natural |
| 1 | 119 | 121.341 | 152 | 1,8 s | 18,9 s | 8,79 | Natural |
| 1 | 120 | 122.365 | 258 | 2,3 s | 31,7 s | 8,75 | Natural |
| 1 | 121 | 123.389 | 171 | 1,5 s | 20,9 s | 8,74 | Natural |
| 1 | 122 | 124.413 | 287 | 1,8 s | 34,6 s | 8,71 | Natural |
| 1 | 123 | 125.437 | 152 | 2,0 s | 19,3 s | 8,70 | Natural |
| 1 | 124 | 126.461 | 260 | 2,3 s | 32,2 s | 8,66 | Natural |
| 1 | 125 | 127.485 | 171 | 1,7 s | 21,3 s | 8,66 | Natural |
| 1 | 126 | 128.509 | 289 | 1,9 s | 35,3 s | 8,62 | Natural |
| 1 | 127 | 129.533 | 152 | 2,3 s | 19,9 s | 8,62 | Natural |
| 1 | 128 | 130.557 | 265 | 1,7 s | 32,4 s | 8,58 | Natural |
| 1 | 129 | 131.581 | 172 | 1,9 s | 21,9 s | 8,57 | Natural |
| 1 | 130 | 132.604 | 294 | 2,3 s | 36,6 s | 8,54 | Natural |
| 1 | 131 | 133.629 | 153 | 1,6 s | 19,4 s | 8,53 | Natural |
| 1 | 132 | 134.652 | 268 | 1,9 s | 33,3 s | 8,50 | Natural |
| 1 | 133 | 135.677 | 173 | 2,3 s | 22,6 s | 8,49 | Natural |
| 1 | 134 | 136.701 | 297 | 1,6 s | 36,6 s | 8,46 | Natural |
| 1 | 135 | 137.725 | 154 | 1,9 s | 20,0 s | 8,46 | Natural |
| 1 | 136 | 138.748 | 268 | 2,1 s | 33,8 s | 8,42 | Natural |
| 1 | 137 | 139.773 | 173 | 2,5 s | 22,9 s | 8,41 | Natural |
| 1 | 138 | 140.797 | 297 | 1,8 s | 37,1 s | 8,38 | Natural |
| 1 | 139 | 141.821 | 154 | 2,0 s | 20,3 s | 8,37 | Natural |
| 1 | 140 | 142.845 | 268 | 2,5 s | 34,5 s | 8,34 | Natural |
| 1 | 141 | 143.869 | 173 | 1,8 s | 22,5 s | 8,33 | Natural |
| 1 | 142 | 144.892 | 297 | 2,0 s | 37,6 s | 8,29 | Natural |
| 1 | 143 | 145.917 | 154 | 2,4 s | 20,9 s | 8,29 | Natural |
| 1 | 144 | 146.941 | 270 | 1,7 s | 34,3 s | 8,26 | Natural |
| 1 | 145 | 147.965 | 173 | 2,0 s | 22,8 s | 8,26 | Natural |
| 1 | 146 | 148.989 | 299 | 2,6 s | 38,9 s | 8,22 | Natural |
| 1 | 147 | 150.013 | 154 | 1,7 s | 20,4 s | 8,21 | Natural |
| 1 | 148 | 151.037 | 273 | 1,9 s | 35,1 s | 8,18 | Natural |
| 1 | 149 | 152.061 | 174 | 2,2 s | 23,3 s | 8,18 | Natural |
| 1 | 150 | 153.084 | 302 | 2,6 s | 39,6 s | 8,14 | Natural |
| 1 | 151 | 154.109 | 155 | 1,9 s | 20,8 s | 8,15 | Natural |
| 1 | 152 | 155.133 | 273 | 2,2 s | 35,7 s | 8,11 | Natural |
| 1 | 153 | 156.157 | 174 | 2,7 s | 24,0 s | 8,11 | Natural |
| 1 | 154 | 157.181 | 302 | 1,8 s | 39,1 s | 8,07 | Natural |
| 1 | 155 | 158.204 | 155 | 2,1 s | 21,2 s | 8,07 | Natural |
| 1 | 156 | 159.229 | 273 | 2,8 s | 36,6 s | 8,04 | Natural |
| 1 | 157 | 160.253 | 174 | 1,8 s | 23,4 s | 8,03 | Natural |
| 1 | 158 | 161.277 | 302 | 2,1 s | 39,7 s | 8,00 | Natural |
| 1 | 159 | 162.301 | 155 | 2,6 s | 21,9 s | 8,00 | Natural |
| 1 | 160 | 163.325 | 275 | 1,7 s | 36,1 s | 7,97 | Natural |
| 1 | 161 | 164.349 | 174 | 2,0 s | 23,8 s | 7,96 | Natural |
| 1 | 162 | 165.373 | 304 | 2,3 s | 40,5 s | 7,93 | Natural |
| 1 | 163 | 166.397 | 155 | 2,8 s | 22,2 s | 7,93 | Natural |
| 1 | 164 | 167.420 | 280 | 2,0 s | 37,4 s | 7,89 | Natural |
| 1 | 165 | 168.445 | 175 | 2,3 s | 24,4 s | 7,89 | Natural |
| 1 | 166 | 169.469 | 309 | 2,7 s | 42,0 s | 7,85 | Natural |
| 1 | 167 | 170.492 | 156 | 1,9 s | 21,6 s | 7,85 | Natural |
| 1 | 168 | 171.517 | 283 | 2,2 s | 38,3 s | 7,82 | Natural |
| 1 | 169 | 172.541 | 176 | 2,7 s | 25,1 s | 7,82 | Natural |
| 1 | 170 | 173.564 | 312 | 1,9 s | 41,9 s | 7,78 | Natural |
| 1 | 171 | 174.589 | 157 | 2,2 s | 22,3 s | 7,78 | Natural |
| 1 | 172 | 175.613 | 283 | 2,5 s | 38,9 s | 7,76 | Natural |
| 1 | 173 | 176.637 | 176 | 2,9 s | 25,5 s | 7,75 | Natural |
| 1 | 174 | 177.661 | 312 | 2,1 s | 42,4 s | 7,72 | Natural |
| 1 | 175 | 178.685 | 157 | 2,4 s | 22,6 s | 7,72 | Natural |
| 1 | 176 | 179.709 | 283 | 3,0 s | 39,7 s | 7,68 | Natural |
| 1 | 177 | 180.733 | 176 | 2,1 s | 24,9 s | 7,69 | Natural |
| 1 | 178 | 181.757 | 312 | 2,5 s | 43,1 s | 7,65 | Natural |
| 1 | 179 | 182.781 | 157 | 2,9 s | 23,3 s | 7,65 | Natural |
| 1 | 180 | 183.805 | 285 | 2,0 s | 39,3 s | 7,62 | Natural |
| 1 | 181 | 184.828 | 176 | 2,4 s | 25,3 s | 7,62 | Natural |
| 1 | 182 | 185.853 | 314 | 3,0 s | 44,3 s | 7,58 | Natural |
| 1 | 183 | 186.877 | 157 | 2,0 s | 22,6 s | 7,59 | Natural |
| 1 | 184 | 187.901 | 288 | 2,4 s | 40,4 s | 7,55 | Natural |
| 1 | 185 | 188.925 | 177 | 2,5 s | 25,8 s | 7,55 | Natural |
| 1 | 186 | 189.949 | 317 | 3,1 s | 45,1 s | 7,52 | Natural |
| 1 | 187 | 190.973 | 158 | 2,2 s | 23,1 s | 7,53 | Natural |
| 1 | 188 | 191.997 | 288 | 2,6 s | 40,9 s | 7,49 | Natural |
| 1 | 189 | 193.021 | 177 | 3,1 s | 26,6 s | 7,49 | Natural |
| 1 | 190 | 194.044 | 317 | 2,3 s | 44,6 s | 7,45 | Natural |
| 1 | 191 | 195.069 | 158 | 2,5 s | 23,5 s | 7,46 | Natural |
| 1 | 192 | 196.093 | 290 | 3,0 s | 41,9 s | 7,43 | Natural |
| 1 | 193 | 197.117 | 177 | 2,1 s | 25,8 s | 7,42 | Natural |
| 1 | 194 | 198.141 | 319 | 2,5 s | 45,5 s | 7,39 | Natural |
| 1 | 195 | 199.165 | 158 | 3,0 s | 24,2 s | 7,41 | Natural |
| 1 | 196 | 200.189 | 295 | 2,2 s | 42,1 s | 7,36 | Natural |
| 1 | 197 | 201.213 | 178 | 2,3 s | 26,4 s | 7,37 | Natural |
| 1 | 198 | 202.237 | 324 | 2,6 s | 46,7 s | 7,33 | Natural |
| 1 | 199 | 203.261 | 159 | 3,2 s | 24,8 s | 7,34 | Natural |
| 1 | 200 | 204.285 | 300 | 2,4 s | 43,3 s | 7,30 | Natural |
| 1 | 201 | 205.309 | 179 | 2,7 s | 27,1 s | 7,31 | Natural |
| 1 | 202 | 206.333 | 329 | 3,3 s | 48,4 s | 7,27 | Natural |
| 1 | 203 | 207.357 | 160 | 2,2 s | 24,1 s | 7,28 | Natural |
| 1 | 204 | 208.381 | 305 | 2,6 s | 44,5 s | 7,24 | Natural |
| 1 | 205 | 209.405 | 180 | 3,1 s | 27,9 s | 7,24 | Natural |
| 1 | 206 | 210.428 | 334 | 2,2 s | 48,4 s | 7,21 | Natural |
| 1 | 207 | 211.453 | 161 | 2,6 s | 24,7 s | 7,22 | Natural |
| 1 | 208 | 212.477 | 310 | 3,3 s | 46,3 s | 7,18 | Natural |
| 1 | 209 | 213.501 | 181 | 2,1 s | 27,2 s | 7,18 | Natural |
| 1 | 210 | 214.525 | 339 | 2,4 s | 49,7 s | 7,15 | Natural |
| 1 | 211 | 215.549 | 162 | 2,8 s | 25,3 s | 7,15 | Natural |
| 1 | 212 | 216.573 | 315 | 3,4 s | 47,5 s | 7,12 | Natural |
| 1 | 213 | 217.597 | 182 | 2,5 s | 27,8 s | 7,13 | Natural |
| 1 | 214 | 218.621 | 344 | 2,8 s | 51,2 s | 7,10 | Natural |
| 1 | 215 | 219.645 | 163 | 3,3 s | 26,1 s | 7,09 | Natural |
| 1 | 216 | 220.669 | 320 | 2,4 s | 47,5 s | 7,07 | Natural |
| 1 | 217 | 221.693 | 183 | 2,8 s | 28,5 s | 7,07 | Natural |
| 1 | 218 | 222.717 | 349 | 3,4 s | 52,8 s | 7,03 | Natural |
| 1 | 219 | 223.741 | 164 | 2,3 s | 25,5 s | 7,04 | Natural |
| 1 | 220 | 224.765 | 325 | 2,7 s | 49,2 s | 6,97 | Natural |
| 1 | 221 | 225.789 | 184 | 3,1 s | 29,2 s | 7,00 | Natural |
| 1 | 222 | 226.813 | 354 | 3,5 s | 54,1 s | 6,97 | Natural |
| 1 | 223 | 227.837 | 165 | 2,6 s | 26,0 s | 6,99 | Natural |
| 1 | 224 | 228.861 | 330 | 2,9 s | 50,3 s | 6,95 | Natural |
| 1 | 225 | 229.885 | 185 | 3,5 s | 30,0 s | 6,95 | Natural |
| 1 | 226 | 230.909 | 359 | 2,6 s | 54,3 s | 6,93 | Natural |
| 1 | 227 | 231.933 | 166 | 2,9 s | 26,7 s | 6,93 | Natural |
| 1 | 228 | 232.957 | 335 | 3,4 s | 51,9 s | 6,90 | Natural |
| 1 | 229 | 233.981 | 186 | 2,4 s | 29,2 s | 6,91 | Natural |
| 1 | 230 | 235.005 | 364 | 2,8 s | 55,7 s | 6,86 | Natural |
| 1 | 231 | 236.029 | 167 | 3,5 s | 27,7 s | 6,88 | Natural |
| 1 | 232 | 237.053 | 340 | 2,4 s | 52,0 s | 6,84 | Natural |
| 1 | 233 | 238.077 | 187 | 2,8 s | 30,0 s | 6,84 | Natural |
| 1 | 234 | 239.101 | 369 | 3,0 s | 57,1 s | 6,81 | Natural |
| 1 | 235 | 240.125 | 168 | 3,7 s | 28,2 s | 6,82 | Natural |
| 1 | 236 | 241.149 | 345 | 2,7 s | 53,4 s | 6,79 | Natural |
| 1 | 237 | 242.173 | 188 | 3,0 s | 30,6 s | 6,79 | Natural |
| 1 | 238 | 243.197 | 374 | 3,7 s | 58,9 s | 6,76 | Natural |
| 1 | 239 | 244.221 | 169 | 2,7 s | 27,5 s | 6,77 | Natural |
| 1 | 240 | 245.245 | 350 | 2,9 s | 54,8 s | 6,73 | Natural |
| 1 | 241 | 246.269 | 189 | 3,6 s | 31,5 s | 6,74 | Natural |
| 1 | 242 | 247.293 | 379 | 2,5 s | 58,9 s | 6,70 | Natural |
| 1 | 243 | 248.317 | 170 | 2,9 s | 28,1 s | 6,71 | Natural |
| 1 | 244 | 249.341 | 355 | 3,7 s | 56,7 s | 6,68 | Natural |
| 1 | 245 | 250.365 | 190 | 2,5 s | 30,8 s | 6,69 | Natural |
| 1 | 246 | 251.389 | 384 | 2,8 s | 60,3 s | 6,66 | Natural |
| 1 | 247 | 252.413 | 171 | 3,2 s | 28,7 s | 6,67 | Natural |
| 1 | 248 | 253.437 | 360 | 3,8 s | 58,0 s | 6,63 | Natural |
| 1 | 249 | 254.461 | 191 | 2,8 s | 31,4 s | 6,64 | Natural |
| 1 | 250 | 255.485 | 389 | 3,2 s | 61,9 s | 6,61 | Natural |
| 1 | 251 | 256.509 | 172 | 3,9 s | 29,8 s | 6,61 | Natural |
| 1 | 252 | 257.533 | 365 | 2,6 s | 57,9 s | 6,58 | Natural |
| 1 | 253 | 258.557 | 192 | 3,1 s | 32,0 s | 6,59 | Natural |
| 1 | 254 | 259.581 | 394 | 3,7 s | 63,7 s | 6,56 | Natural |
| 1 | 255 | 260.605 | 173 | 2,7 s | 28,9 s | 6,56 | Natural |
| 1 | 256 | 261.117 | 370 | 2,3 s | 58,7 s | 6,55 | Natural |
| 1 | 257 | 262.013 | 16 | 2,4 s | 4,6 s | 6,81 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
