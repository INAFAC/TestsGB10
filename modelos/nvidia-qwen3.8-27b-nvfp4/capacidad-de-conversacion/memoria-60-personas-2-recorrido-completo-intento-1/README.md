# 2 personas · 60% de memoria

[Volver a la capacidad por memoria](../README.md)

**No cumple la referencia del recorrido.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **260/514 previstas**. Duración: **202,1 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **254**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.532–16.893 | 32/32 | 1,7 s | 1,8 s | 10,83 tokens/s | 25,6 s | Cumple |
| 18-33 | 17.917–33.277 | 32/32 | 2,1 s | 2,1 s | 9,87 tokens/s | 36,1 s | Cumple |
| 34-49 | 34.300–49.661 | 32/32 | 2,4 s | 2,4 s | 9,01 tokens/s | 46,7 s | Cumple |
| 50-65 | 50.685–66.045 | 32/32 | 2,7 s | 2,9 s | 8,33 tokens/s | 59,3 s | Cumple |
| 66-81 | 67.069–82.429 | 32/32 | 3,2 s | 3,2 s | 7,74 tokens/s | 72,9 s | Cumple |
| 82-97 | 83.453–98.813 | 32/32 | 3,4 s | 3,5 s | 7,27 tokens/s | 88,0 s | Cumple |
| 98-113 | 99.837–115.197 | 32/32 | 3,7 s | 3,8 s | 6,83 tokens/s | 104,4 s | Cumple |
| 114-129 | 116.221–131.581 | 32/32 | 4,3 s | 4,3 s | 6,41 tokens/s | 122,1 s | No cumple |
| 130-145 | 132.605–132.605 | 2/32 | 4,2 s | 4,2 s | 6,38 tokens/s | 130,5 s | Incompleto |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 130 | 133.608 | 50,967% | 128.536 |
| 2 | 130 | 132.807 | 50,662% | 129.337 |

El cierre previsto reserva hasta 128 tokens y pide terminar en diez palabras. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento no llegó a ese cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 60% |
| Pico de memoria del motor / GB10 | 56,7% |
| Pico de memoria total del sistema / GB10 | 65,6% |
| Pico de caché | 35,8% |
| Solicitudes activas / respuestas solapadas, máximo | 2 / 2 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 2,3 s |
| Espera media al primer token, incluido razonamiento | 2,3 s |
| Tiempo medio de petición completa | 43,3 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 7,75 tokens/s |
| Suma de tiempos individuales de petición | 11.255,6 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 130/130 | 2,3 s | 62,8 s | 12.098,9 s | 5,86 |
| 2 | 130/130 | 2,2 s | 23,7 s | 12.004,0 s | 1,92 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 146 | 0,4 s | 12,6 s | 11,92 | Natural |
| 2 | 1 | 512 | 137 | 0,4 s | 11,8 s | 11,90 | Natural |
| 1 | 2 | 1.532 | 186 | 1,1 s | 16,7 s | 11,82 | Natural |
| 2 | 2 | 1.533 | 163 | 1,2 s | 14,9 s | 11,82 | Natural |
| 1 | 3 | 2.557 | 172 | 1,5 s | 16,0 s | 11,82 | Natural |
| 2 | 3 | 2.557 | 150 | 1,5 s | 14,1 s | 11,77 | Natural |
| 1 | 4 | 3.580 | 182 | 1,1 s | 16,5 s | 11,73 | Natural |
| 2 | 4 | 3.581 | 165 | 1,0 s | 15,0 s | 11,67 | Natural |
| 1 | 5 | 4.605 | 182 | 1,2 s | 16,7 s | 11,69 | Natural |
| 2 | 5 | 4.605 | 155 | 1,1 s | 14,4 s | 11,55 | Natural |
| 1 | 6 | 5.629 | 249 | 1,5 s | 22,6 s | 11,74 | Natural |
| 2 | 6 | 5.629 | 158 | 1,6 s | 15,2 s | 11,54 | Natural |
| 1 | 7 | 6.653 | 221 | 1,0 s | 19,9 s | 11,65 | Natural |
| 2 | 7 | 6.653 | 149 | 1,1 s | 14,0 s | 11,47 | Natural |
| 1 | 8 | 7.677 | 216 | 1,1 s | 19,8 s | 11,49 | Natural |
| 2 | 8 | 7.677 | 169 | 1,3 s | 16,0 s | 11,40 | Natural |
| 1 | 9 | 8.701 | 200 | 1,6 s | 18,9 s | 11,46 | Natural |
| 2 | 9 | 8.701 | 158 | 1,5 s | 15,4 s | 11,34 | Natural |
| 1 | 10 | 9.724 | 268 | 1,1 s | 24,3 s | 11,53 | Natural |
| 2 | 10 | 9.725 | 160 | 1,0 s | 15,2 s | 11,25 | Natural |
| 1 | 11 | 10.749 | 238 | 1,3 s | 22,0 s | 11,43 | Natural |
| 2 | 11 | 10.749 | 153 | 1,1 s | 14,8 s | 11,14 | Natural |
| 1 | 12 | 11.773 | 239 | 1,6 s | 22,5 s | 11,35 | Natural |
| 2 | 12 | 11.773 | 169 | 1,6 s | 16,7 s | 11,11 | Natural |
| 1 | 13 | 12.797 | 217 | 1,1 s | 20,3 s | 11,25 | Natural |
| 2 | 13 | 12.797 | 158 | 1,2 s | 15,4 s | 11,04 | Natural |
| 1 | 14 | 13.821 | 290 | 1,3 s | 26,8 s | 11,32 | Natural |
| 2 | 14 | 13.821 | 159 | 1,1 s | 15,6 s | 10,94 | Natural |
| 1 | 15 | 14.845 | 267 | 1,3 s | 25,0 s | 11,20 | Natural |
| 2 | 15 | 14.845 | 154 | 1,5 s | 15,5 s | 10,90 | Natural |
| 1 | 16 | 15.869 | 265 | 1,8 s | 25,6 s | 11,11 | Natural |
| 2 | 16 | 15.869 | 170 | 1,7 s | 17,3 s | 10,83 | Natural |
| 1 | 17 | 16.893 | 240 | 1,1 s | 22,8 s | 11,02 | Natural |
| 2 | 17 | 16.893 | 160 | 1,3 s | 16,0 s | 10,76 | Natural |
| 1 | 18 | 17.917 | 314 | 1,5 s | 29,6 s | 11,13 | Natural |
| 2 | 18 | 17.917 | 161 | 1,3 s | 16,3 s | 10,64 | Natural |
| 1 | 19 | 18.941 | 290 | 1,8 s | 28,0 s | 11,06 | Natural |
| 2 | 19 | 18.940 | 153 | 1,8 s | 16,0 s | 10,66 | Natural |
| 1 | 20 | 19.965 | 290 | 1,3 s | 27,7 s | 10,95 | Natural |
| 2 | 20 | 19.965 | 172 | 1,2 s | 17,4 s | 10,56 | Natural |
| 1 | 21 | 20.989 | 265 | 1,3 s | 25,6 s | 10,85 | Natural |
| 2 | 21 | 20.989 | 160 | 1,5 s | 16,6 s | 10,52 | Natural |
| 1 | 22 | 22.013 | 341 | 1,8 s | 32,8 s | 10,96 | Natural |
| 2 | 22 | 22.013 | 162 | 1,8 s | 17,2 s | 10,45 | Natural |
| 1 | 23 | 23.037 | 316 | 1,2 s | 30,1 s | 10,89 | Natural |
| 2 | 23 | 23.037 | 155 | 1,3 s | 16,1 s | 10,40 | Natural |
| 1 | 24 | 24.061 | 317 | 1,5 s | 30,8 s | 10,79 | Natural |
| 2 | 24 | 24.061 | 173 | 1,3 s | 18,0 s | 10,29 | Natural |
| 1 | 25 | 25.085 | 290 | 1,5 s | 28,6 s | 10,67 | Natural |
| 2 | 25 | 25.085 | 161 | 1,7 s | 17,3 s | 10,27 | Natural |
| 1 | 26 | 26.108 | 368 | 2,0 s | 36,1 s | 10,78 | Natural |
| 2 | 26 | 26.109 | 166 | 2,0 s | 18,1 s | 10,21 | Natural |
| 1 | 27 | 27.133 | 341 | 1,5 s | 33,1 s | 10,73 | Natural |
| 2 | 27 | 27.133 | 157 | 1,3 s | 16,7 s | 10,12 | Natural |
| 1 | 28 | 28.157 | 344 | 1,7 s | 34,0 s | 10,62 | Natural |
| 2 | 28 | 28.157 | 176 | 1,5 s | 18,9 s | 10,02 | Natural |
| 1 | 29 | 29.181 | 311 | 2,1 s | 31,4 s | 10,56 | Natural |
| 2 | 29 | 29.181 | 162 | 2,0 s | 18,0 s | 10,03 | Natural |
| 1 | 30 | 30.204 | 387 | 1,4 s | 37,8 s | 10,62 | Natural |
| 2 | 30 | 30.205 | 166 | 1,3 s | 17,9 s | 9,96 | Natural |
| 1 | 31 | 31.228 | 348 | 1,5 s | 34,5 s | 10,51 | Natural |
| 2 | 31 | 31.229 | 156 | 1,7 s | 17,3 s | 9,92 | Natural |
| 1 | 32 | 32.253 | 351 | 2,1 s | 35,6 s | 10,43 | Natural |
| 2 | 32 | 32.253 | 178 | 2,0 s | 19,9 s | 9,87 | Natural |
| 1 | 33 | 33.277 | 318 | 1,4 s | 32,0 s | 10,36 | Natural |
| 2 | 33 | 33.277 | 163 | 1,5 s | 18,0 s | 9,81 | Natural |
| 1 | 34 | 34.301 | 393 | 1,7 s | 39,2 s | 10,44 | Natural |
| 2 | 34 | 34.300 | 168 | 1,5 s | 18,7 s | 9,71 | Natural |
| 1 | 35 | 35.325 | 356 | 2,0 s | 36,2 s | 10,37 | Natural |
| 2 | 35 | 35.325 | 158 | 2,1 s | 18,3 s | 9,70 | Natural |
| 1 | 36 | 36.349 | 363 | 1,5 s | 36,8 s | 10,27 | Natural |
| 2 | 36 | 36.349 | 179 | 1,4 s | 19,9 s | 9,64 | Natural |
| 1 | 37 | 37.373 | 329 | 1,7 s | 33,8 s | 10,21 | Natural |
| 2 | 37 | 37.373 | 165 | 1,5 s | 18,7 s | 9,55 | Natural |
| 1 | 38 | 38.397 | 414 | 1,9 s | 42,1 s | 10,29 | Natural |
| 2 | 38 | 38.397 | 170 | 1,7 s | 19,5 s | 9,47 | Natural |
| 1 | 39 | 39.421 | 383 | 2,3 s | 39,7 s | 10,23 | Natural |
| 2 | 39 | 39.421 | 160 | 2,2 s | 19,0 s | 9,49 | Natural |
| 1 | 40 | 40.445 | 389 | 1,7 s | 40,0 s | 10,13 | Natural |
| 2 | 40 | 40.445 | 181 | 1,5 s | 20,6 s | 9,41 | Natural |
| 1 | 41 | 41.469 | 354 | 1,9 s | 36,9 s | 10,09 | Natural |
| 2 | 41 | 41.469 | 165 | 1,7 s | 19,2 s | 9,33 | Natural |
| 1 | 42 | 42.493 | 440 | 2,4 s | 45,6 s | 10,14 | Natural |
| 2 | 42 | 42.493 | 173 | 2,3 s | 20,7 s | 9,34 | Natural |
| 1 | 43 | 43.517 | 408 | 1,5 s | 41,8 s | 10,09 | Natural |
| 2 | 43 | 43.517 | 160 | 1,6 s | 18,7 s | 9,30 | Natural |
| 1 | 44 | 44.541 | 417 | 1,7 s | 43,5 s | 9,96 | Natural |
| 2 | 44 | 44.541 | 184 | 1,9 s | 21,7 s | 9,25 | Natural |
| 1 | 45 | 45.565 | 379 | 2,4 s | 40,3 s | 9,96 | Natural |
| 2 | 45 | 45.565 | 167 | 2,3 s | 20,3 s | 9,21 | Natural |
| 1 | 46 | 46.589 | 464 | 1,7 s | 48,0 s | 10,01 | Natural |
| 2 | 46 | 46.589 | 174 | 1,6 s | 20,5 s | 9,13 | Natural |
| 1 | 47 | 47.613 | 430 | 1,7 s | 44,8 s | 9,95 | Natural |
| 2 | 47 | 47.613 | 160 | 1,9 s | 19,3 s | 9,11 | Natural |
| 1 | 48 | 48.637 | 439 | 2,3 s | 46,7 s | 9,86 | Natural |
| 2 | 48 | 48.637 | 186 | 1,9 s | 22,5 s | 8,96 | Natural |
| 1 | 49 | 49.661 | 400 | 1,7 s | 42,3 s | 9,83 | Natural |
| 2 | 49 | 49.661 | 167 | 1,5 s | 20,0 s | 9,01 | Natural |
| 1 | 50 | 50.685 | 490 | 1,7 s | 51,3 s | 9,86 | Natural |
| 2 | 50 | 50.685 | 176 | 1,9 s | 21,4 s | 8,97 | Natural |
| 1 | 51 | 51.709 | 451 | 1,9 s | 47,8 s | 9,79 | Natural |
| 2 | 51 | 51.709 | 163 | 2,2 s | 20,3 s | 8,93 | Natural |
| 1 | 52 | 52.732 | 463 | 2,6 s | 50,1 s | 9,73 | Natural |
| 2 | 52 | 52.733 | 189 | 2,5 s | 23,7 s | 8,88 | Natural |
| 1 | 53 | 53.757 | 421 | 1,8 s | 45,1 s | 9,70 | Natural |
| 2 | 53 | 53.756 | 168 | 1,7 s | 20,6 s | 8,81 | Natural |
| 1 | 54 | 54.780 | 514 | 2,1 s | 54,8 s | 9,74 | Natural |
| 2 | 54 | 54.781 | 180 | 1,9 s | 22,4 s | 8,73 | Natural |
| 1 | 55 | 55.805 | 469 | 2,6 s | 50,8 s | 9,71 | Natural |
| 2 | 55 | 55.805 | 164 | 2,5 s | 21,1 s | 8,75 | Natural |
| 1 | 56 | 56.829 | 482 | 1,8 s | 51,9 s | 9,60 | Natural |
| 2 | 56 | 56.829 | 190 | 1,6 s | 23,4 s | 8,68 | Natural |
| 1 | 57 | 57.853 | 438 | 2,1 s | 47,8 s | 9,57 | Natural |
| 2 | 57 | 57.853 | 169 | 1,9 s | 21,4 s | 8,59 | Natural |
| 1 | 58 | 58.877 | 533 | 2,5 s | 57,9 s | 9,61 | Natural |
| 2 | 58 | 58.877 | 180 | 2,6 s | 23,4 s | 8,63 | Natural |
| 1 | 59 | 59.900 | 489 | 1,8 s | 52,7 s | 9,59 | Natural |
| 2 | 59 | 59.901 | 164 | 1,7 s | 20,7 s | 8,56 | Natural |
| 1 | 60 | 60.925 | 505 | 2,1 s | 55,3 s | 9,48 | Natural |
| 2 | 60 | 60.925 | 192 | 1,9 s | 24,4 s | 8,49 | Natural |
| 1 | 61 | 61.949 | 458 | 2,6 s | 50,9 s | 9,46 | Natural |
| 2 | 61 | 61.949 | 170 | 2,1 s | 22,2 s | 8,39 | Natural |
| 1 | 62 | 62.973 | 556 | 1,9 s | 60,3 s | 9,50 | Natural |
| 2 | 62 | 62.973 | 182 | 1,7 s | 23,1 s | 8,45 | Natural |
| 1 | 63 | 63.997 | 517 | 2,1 s | 56,5 s | 9,47 | Natural |
| 2 | 63 | 63.997 | 166 | 1,9 s | 21,6 s | 8,38 | Natural |
| 1 | 64 | 65.021 | 534 | 2,4 s | 59,3 s | 9,36 | Natural |
| 2 | 64 | 65.021 | 194 | 2,1 s | 25,4 s | 8,30 | Natural |
| 1 | 65 | 66.045 | 483 | 2,9 s | 54,4 s | 9,35 | Natural |
| 2 | 65 | 66.045 | 171 | 2,7 s | 23,1 s | 8,33 | Natural |
| 1 | 66 | 67.069 | 585 | 2,0 s | 64,6 s | 9,34 | Natural |
| 2 | 66 | 67.069 | 184 | 1,8 s | 24,0 s | 8,27 | Natural |
| 1 | 67 | 68.093 | 544 | 2,1 s | 60,2 s | 9,33 | Natural |
| 2 | 67 | 68.093 | 165 | 2,4 s | 22,2 s | 8,25 | Natural |
| 1 | 68 | 69.117 | 562 | 2,9 s | 63,5 s | 9,25 | Natural |
| 2 | 68 | 69.117 | 197 | 2,8 s | 26,6 s | 8,21 | Natural |
| 1 | 69 | 70.141 | 508 | 2,1 s | 56,9 s | 9,24 | Natural |
| 2 | 69 | 70.141 | 172 | 1,9 s | 22,8 s | 8,16 | Natural |
| 1 | 70 | 71.165 | 613 | 2,4 s | 68,4 s | 9,27 | Natural |
| 2 | 70 | 71.165 | 186 | 2,1 s | 25,0 s | 8,07 | Natural |
| 1 | 71 | 72.189 | 571 | 2,8 s | 64,4 s | 9,27 | Natural |
| 2 | 71 | 72.189 | 167 | 2,7 s | 23,2 s | 8,12 | Natural |
| 1 | 72 | 73.213 | 590 | 1,9 s | 66,3 s | 9,14 | Natural |
| 2 | 72 | 73.213 | 198 | 2,0 s | 26,5 s | 8,06 | Natural |
| 1 | 73 | 74.237 | 533 | 2,3 s | 60,5 s | 9,14 | Natural |
| 2 | 73 | 74.236 | 174 | 2,0 s | 23,7 s | 7,98 | Natural |
| 1 | 74 | 75.260 | 641 | 2,7 s | 72,5 s | 9,16 | Natural |
| 2 | 74 | 75.261 | 189 | 2,3 s | 26,1 s | 7,91 | Natural |
| 1 | 75 | 76.285 | 585 | 3,2 s | 67,0 s | 9,15 | Natural |
| 2 | 75 | 76.285 | 167 | 3,0 s | 23,9 s | 7,95 | Natural |
| 1 | 76 | 77.309 | 606 | 2,0 s | 69,2 s | 9,01 | Natural |
| 2 | 76 | 77.309 | 201 | 2,3 s | 27,5 s | 7,93 | Natural |
| 1 | 77 | 78.333 | 541 | 2,7 s | 62,5 s | 9,02 | Natural |
| 2 | 77 | 78.333 | 175 | 2,3 s | 24,6 s | 7,81 | Natural |
| 1 | 78 | 79.357 | 652 | 3,1 s | 75,2 s | 9,04 | Natural |
| 2 | 78 | 79.356 | 195 | 3,0 s | 27,7 s | 7,85 | Natural |
| 1 | 79 | 80.381 | 608 | 2,2 s | 69,3 s | 9,05 | Natural |
| 2 | 79 | 80.381 | 169 | 2,0 s | 23,6 s | 7,79 | Natural |
| 1 | 80 | 81.405 | 629 | 2,6 s | 72,9 s | 8,94 | Natural |
| 2 | 80 | 81.405 | 202 | 2,3 s | 28,3 s | 7,73 | Natural |
| 1 | 81 | 82.429 | 566 | 3,2 s | 66,5 s | 8,92 | Natural |
| 2 | 81 | 82.429 | 176 | 3,0 s | 25,6 s | 7,74 | Natural |
| 1 | 82 | 83.453 | 679 | 2,0 s | 77,9 s | 8,93 | Natural |
| 2 | 82 | 83.453 | 192 | 2,3 s | 27,0 s | 7,72 | Natural |
| 1 | 83 | 84.477 | 626 | 2,6 s | 72,5 s | 8,95 | Natural |
| 2 | 83 | 84.476 | 169 | 2,3 s | 24,3 s | 7,62 | Natural |
| 1 | 84 | 85.500 | 652 | 3,1 s | 76,8 s | 8,84 | Natural |
| 2 | 84 | 85.501 | 203 | 2,5 s | 29,3 s | 7,55 | Natural |
| 1 | 85 | 86.525 | 593 | 2,2 s | 69,2 s | 8,83 | Natural |
| 2 | 85 | 86.525 | 177 | 2,0 s | 25,2 s | 7,59 | Natural |
| 1 | 86 | 87.549 | 711 | 2,5 s | 82,8 s | 8,85 | Natural |
| 2 | 86 | 87.549 | 195 | 2,2 s | 28,0 s | 7,53 | Natural |
| 1 | 87 | 88.573 | 661 | 2,5 s | 77,3 s | 8,82 | Natural |
| 2 | 87 | 88.573 | 170 | 2,9 s | 25,3 s | 7,55 | Natural |
| 1 | 88 | 89.597 | 686 | 3,5 s | 81,8 s | 8,74 | Natural |
| 2 | 88 | 89.597 | 206 | 3,3 s | 30,6 s | 7,50 | Natural |
| 1 | 89 | 90.621 | 615 | 2,5 s | 72,8 s | 8,74 | Natural |
| 2 | 89 | 90.621 | 177 | 2,3 s | 25,9 s | 7,45 | Natural |
| 1 | 90 | 91.645 | 737 | 2,8 s | 87,0 s | 8,74 | Natural |
| 2 | 90 | 91.645 | 200 | 2,5 s | 29,4 s | 7,39 | Natural |
| 1 | 91 | 92.668 | 687 | 3,4 s | 81,7 s | 8,77 | Natural |
| 2 | 91 | 92.669 | 171 | 3,3 s | 26,2 s | 7,42 | Natural |
| 1 | 92 | 93.693 | 713 | 2,4 s | 84,7 s | 8,65 | Natural |
| 2 | 92 | 93.693 | 208 | 2,2 s | 30,3 s | 7,37 | Natural |
| 1 | 93 | 94.717 | 637 | 2,8 s | 76,3 s | 8,65 | Natural |
| 2 | 93 | 94.717 | 178 | 2,5 s | 26,7 s | 7,30 | Natural |
| 1 | 94 | 95.741 | 757 | 3,3 s | 90,7 s | 8,65 | Natural |
| 2 | 94 | 95.741 | 199 | 3,4 s | 30,5 s | 7,33 | Natural |
| 1 | 95 | 96.764 | 704 | 2,2 s | 83,5 s | 8,65 | Natural |
| 2 | 95 | 96.765 | 173 | 2,5 s | 26,0 s | 7,31 | Natural |
| 1 | 96 | 97.789 | 731 | 2,4 s | 88,0 s | 8,53 | Natural |
| 2 | 96 | 97.789 | 208 | 2,7 s | 31,2 s | 7,27 | Natural |
| 1 | 97 | 98.813 | 657 | 3,2 s | 79,9 s | 8,56 | Natural |
| 2 | 97 | 98.813 | 179 | 3,3 s | 27,9 s | 7,25 | Natural |
| 1 | 98 | 99.837 | 783 | 2,2 s | 93,5 s | 8,56 | Natural |
| 2 | 98 | 99.837 | 198 | 2,4 s | 29,7 s | 7,22 | Natural |
| 1 | 99 | 100.861 | 735 | 2,7 s | 88,2 s | 8,59 | Natural |
| 2 | 99 | 100.861 | 173 | 2,5 s | 26,5 s | 7,15 | Natural |
| 1 | 100 | 101.885 | 758 | 2,7 s | 92,6 s | 8,42 | Natural |
| 2 | 100 | 101.884 | 208 | 3,1 s | 32,0 s | 7,16 | Natural |
| 1 | 101 | 102.909 | 681 | 3,8 s | 84,0 s | 8,47 | Natural |
| 2 | 101 | 102.909 | 179 | 3,6 s | 28,6 s | 7,12 | Natural |
| 1 | 102 | 103.933 | 809 | 2,6 s | 97,8 s | 8,49 | Natural |
| 2 | 102 | 103.932 | 198 | 2,4 s | 30,2 s | 7,08 | Natural |
| 1 | 103 | 104.956 | 761 | 3,0 s | 92,4 s | 8,50 | Natural |
| 2 | 103 | 104.957 | 173 | 2,6 s | 27,2 s | 7,00 | Natural |
| 1 | 104 | 105.981 | 786 | 3,5 s | 97,2 s | 8,38 | Natural |
| 2 | 104 | 105.980 | 208 | 3,7 s | 33,1 s | 7,04 | Natural |
| 1 | 105 | 107.005 | 701 | 2,6 s | 86,1 s | 8,39 | Natural |
| 2 | 105 | 107.005 | 179 | 2,4 s | 27,8 s | 6,99 | Natural |
| 1 | 106 | 108.029 | 832 | 3,1 s | 102,0 s | 8,40 | Natural |
| 2 | 106 | 108.029 | 198 | 2,7 s | 31,1 s | 6,93 | Natural |
| 1 | 107 | 109.053 | 782 | 3,7 s | 96,5 s | 8,41 | Natural |
| 2 | 107 | 109.053 | 173 | 3,6 s | 28,3 s | 6,96 | Natural |
| 1 | 108 | 110.077 | 807 | 2,6 s | 99,6 s | 8,31 | Natural |
| 2 | 108 | 110.077 | 208 | 2,3 s | 32,3 s | 6,92 | Natural |
| 1 | 109 | 111.100 | 731 | 2,9 s | 90,7 s | 8,32 | Natural |
| 2 | 109 | 111.101 | 178 | 2,6 s | 28,4 s | 6,86 | Natural |
| 1 | 110 | 112.125 | 864 | 3,5 s | 107,3 s | 8,32 | Natural |
| 2 | 110 | 112.125 | 199 | 3,6 s | 32,4 s | 6,88 | Natural |
| 1 | 111 | 113.149 | 812 | 2,6 s | 99,8 s | 8,34 | Natural |
| 2 | 111 | 113.149 | 172 | 2,4 s | 27,3 s | 6,85 | Natural |
| 1 | 112 | 114.173 | 837 | 2,6 s | 104,4 s | 8,21 | Natural |
| 2 | 112 | 114.173 | 208 | 2,9 s | 33,2 s | 6,83 | Natural |
| 1 | 113 | 115.197 | 760 | 2,9 s | 95,4 s | 8,21 | Natural |
| 2 | 113 | 115.197 | 179 | 3,4 s | 29,5 s | 6,81 | Natural |
| 1 | 114 | 116.221 | 896 | 3,9 s | 112,5 s | 8,24 | Natural |
| 2 | 114 | 116.221 | 199 | 3,8 s | 33,0 s | 6,77 | Natural |
| 1 | 115 | 117.245 | 844 | 2,5 s | 104,7 s | 8,25 | Natural |
| 2 | 115 | 117.245 | 173 | 2,8 s | 28,3 s | 6,75 | Natural |
| 1 | 116 | 118.269 | 873 | 3,3 s | 110,1 s | 8,16 | Natural |
| 2 | 116 | 118.268 | 207 | 2,9 s | 33,8 s | 6,66 | Natural |
| 1 | 117 | 119.293 | 792 | 4,0 s | 100,8 s | 8,17 | Natural |
| 2 | 117 | 119.293 | 179 | 3,8 s | 30,4 s | 6,70 | Natural |
| 1 | 118 | 120.316 | 932 | 2,9 s | 116,8 s | 8,17 | Natural |
| 2 | 118 | 120.317 | 199 | 2,6 s | 32,4 s | 6,65 | Natural |
| 1 | 119 | 121.341 | 871 | 3,3 s | 109,6 s | 8,18 | Natural |
| 2 | 119 | 121.341 | 174 | 2,9 s | 29,1 s | 6,59 | Natural |
| 1 | 120 | 122.365 | 899 | 3,9 s | 114,9 s | 8,09 | Natural |
| 2 | 120 | 122.365 | 209 | 3,1 s | 35,0 s | 6,54 | Natural |
| 1 | 121 | 123.389 | 811 | 2,5 s | 102,8 s | 8,08 | Natural |
| 2 | 121 | 123.389 | 179 | 2,7 s | 29,7 s | 6,60 | Natural |
| 1 | 122 | 124.413 | 961 | 3,2 s | 121,7 s | 8,10 | Natural |
| 2 | 122 | 124.413 | 199 | 2,8 s | 33,1 s | 6,53 | Natural |
| 1 | 123 | 125.437 | 900 | 3,7 s | 114,5 s | 8,11 | Natural |
| 2 | 123 | 125.437 | 172 | 3,2 s | 29,6 s | 6,46 | Natural |
| 1 | 124 | 126.460 | 928 | 4,3 s | 120,1 s | 8,00 | Natural |
| 2 | 124 | 126.460 | 211 | 4,1 s | 36,3 s | 6,52 | Natural |
| 1 | 125 | 127.485 | 835 | 2,8 s | 107,1 s | 7,99 | Natural |
| 2 | 125 | 127.485 | 179 | 3,1 s | 30,5 s | 6,50 | Natural |
| 1 | 126 | 128.509 | 979 | 3,6 s | 125,7 s | 8,01 | Natural |
| 2 | 126 | 128.508 | 201 | 3,1 s | 34,3 s | 6,41 | Natural |
| 1 | 127 | 129.532 | 863 | 4,3 s | 113,0 s | 7,93 | Natural |
| 2 | 127 | 129.533 | 174 | 4,1 s | 30,9 s | 6,45 | Natural |
| 1 | 128 | 130.557 | 945 | 3,0 s | 122,1 s | 7,92 | Natural |
| 2 | 128 | 130.557 | 212 | 2,7 s | 35,7 s | 6,41 | Natural |
| 1 | 129 | 131.581 | 856 | 3,0 s | 111,1 s | 7,91 | Natural |
| 2 | 129 | 131.581 | 180 | 3,5 s | 31,4 s | 6,41 | Natural |
| 1 | 130 | 132.605 | 1.003 | 4,2 s | 130,5 s | 7,93 | Natural |
| 2 | 130 | 132.605 | 202 | 4,1 s | 35,5 s | 6,38 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
