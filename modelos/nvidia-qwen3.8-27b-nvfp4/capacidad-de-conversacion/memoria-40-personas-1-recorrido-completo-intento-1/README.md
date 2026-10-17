# 1 persona · 40% de memoria

[Volver a la capacidad por memoria](../README.md)

**Cumplió durante todo el recorrido.**

Modelo: `nvidia/Qwen3.8-27B-NVFP4`. Razonamiento: **desactivado**. Límite impuesto al servidor: **4 solicitudes activas**. Presupuesto de salida: **hasta 1.024 tokens por respuesta**, con petición de hasta 100 palabras.

Respuestas recibidas sin error: **257/257 previstas**. Duración: **223,2 min**, incluidas las pausas. Se conservan todos los mensajes y las respuestas reales desde el comienzo; no se salta ni recorta el historial.

Peticiones con error: **0**. Peticiones previstas que no llegaron a enviarse: **0**. No se cuentan como errores las peticiones omitidas después de detener el ensayo.

Los plazos de espera del cliente no demuestran un error de memoria. Un corte por límite de salida tampoco. Los percentiles de una prueba incompleta describen únicamente las respuestas recibidas.

## Resultado durante el crecimiento

| Turnos | Historial enviado | Respuestas medidas / previstas | Espera visible p95 | Peor espera | Velocidad p05 | Respuesta completa p95 | Referencia |
|---|---:|---:|---:|---:|---:|---:|---|
| 2-17 | 1.533–16.893 | 16/16 | 1,0 s | 1,0 s | 11,73 tokens/s | 15,1 s | Cumple |
| 18-33 | 17.917–33.277 | 16/16 | 1,2 s | 1,2 s | 11,13 tokens/s | 15,7 s | Cumple |
| 34-49 | 34.300–49.661 | 16/16 | 1,3 s | 1,3 s | 10,61 tokens/s | 17,0 s | Cumple |
| 50-65 | 50.685–66.045 | 16/16 | 1,6 s | 1,6 s | 10,13 tokens/s | 17,5 s | Cumple |
| 66-81 | 67.069–82.429 | 16/16 | 1,7 s | 1,7 s | 9,70 tokens/s | 18,8 s | Cumple |
| 82-97 | 83.452–98.813 | 16/16 | 1,9 s | 1,9 s | 9,30 tokens/s | 20,1 s | Cumple |
| 98-113 | 99.837–115.197 | 16/16 | 2,1 s | 2,1 s | 8,93 tokens/s | 20,8 s | Cumple |
| 114-129 | 116.221–131.581 | 16/16 | 2,4 s | 2,4 s | 8,57 tokens/s | 24,4 s | Cumple |
| 130-145 | 132.605–147.965 | 16/16 | 2,5 s | 2,5 s | 8,26 tokens/s | 27,3 s | Cumple |
| 146-161 | 148.988–164.349 | 16/16 | 2,7 s | 2,7 s | 7,97 tokens/s | 30,2 s | Cumple |
| 162-177 | 165.373–180.733 | 16/16 | 3,0 s | 3,0 s | 7,68 tokens/s | 33,3 s | Cumple |
| 178-193 | 181.757–197.117 | 16/16 | 3,1 s | 3,1 s | 7,42 tokens/s | 36,6 s | Cumple |
| 194-209 | 198.141–213.501 | 16/16 | 3,3 s | 3,3 s | 7,18 tokens/s | 39,1 s | Cumple |
| 210-225 | 214.525–229.885 | 16/16 | 3,6 s | 3,6 s | 6,97 tokens/s | 40,9 s | Cumple |
| 226-241 | 230.909–246.269 | 16/16 | 3,7 s | 3,7 s | 6,75 tokens/s | 44,1 s | Cumple |
| 242-257 | 247.293–262.013 | 16/16 | 3,9 s | 3,9 s | 6,56 tokens/s | 46,1 s | Cumple |

## Contexto alcanzado por persona

| Persona | Último turno sin error | Tokens totales alcanzados | Contexto utilizado | Espacio restante |
|---:|---:|---:|---:|---:|
| 1 | 257 | 262.026 | 99,955% | 118 |

El objetivo del cierre deja aproximadamente 128 tokens para la respuesta y pide terminar en diez palabras. El presupuesto efectivo se calcula con la entrada real. No se fuerza al modelo a rellenar el espacio restante ni se afirma haber llegado exactamente a 262.144. Este intento llegó al cierre.

## Memoria, colas y rendimiento del grupo

| Medida | Resultado |
|---|---:|
| Presupuesto configurado | 40% |
| Pico de memoria del motor / GB10 | 36,7% |
| Pico de memoria total del sistema / GB10 | 45,3% |
| Pico de caché | 70,5% |
| Solicitudes activas / respuestas solapadas, máximo | 1 / 1 |
| Cola máxima / segundos con cola | 0 / 0,0 s |
| Espera media al primer texto visible | 1,9 s |
| Espera media al primer token, incluido razonamiento | 1,9 s |
| Tiempo medio de petición completa | 21,7 s |
| Recálculos por falta de espacio de caché | 0 |
| Velocidad global, incluidas pausas | 3,18 tokens/s |
| Suma de tiempos individuales de petición | 5.578,3 s |

## Resumen por persona

| Persona | Respuestas sin error | Espera visible media | Respuesta completa media | Tiempo de sesión, con pausas | Tokens/s de sesión |
|---:|---:|---:|---:|---:|---:|
| 1 | 257/257 | 1,9 s | 21,7 s | 13.389,4 s | 3,18 |

<details>
<summary>Cada persona y cada respuesta</summary>

| Persona | Turno | Entrada | Salida | Espera visible | Respuesta completa | Tokens/s | Finalización |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 512 | 190 | 0,2 s | 15,6 s | 12,34 | Natural |
| 1 | 2 | 1.533 | 157 | 0,7 s | 13,3 s | 12,31 | Natural |
| 1 | 3 | 2.557 | 161 | 0,8 s | 13,9 s | 12,27 | Natural |
| 1 | 4 | 3.580 | 135 | 0,6 s | 11,5 s | 12,24 | Natural |
| 1 | 5 | 4.605 | 173 | 0,7 s | 14,8 s | 12,20 | Natural |
| 1 | 6 | 5.629 | 159 | 0,9 s | 13,9 s | 12,16 | Natural |
| 1 | 7 | 6.653 | 177 | 0,6 s | 15,1 s | 12,12 | Natural |
| 1 | 8 | 7.677 | 131 | 0,7 s | 11,5 s | 12,08 | Natural |
| 1 | 9 | 8.701 | 122 | 0,8 s | 10,9 s | 12,04 | Natural |
| 1 | 10 | 9.724 | 155 | 0,6 s | 13,4 s | 12,00 | Natural |
| 1 | 11 | 10.749 | 168 | 0,7 s | 14,7 s | 11,96 | Natural |
| 1 | 12 | 11.773 | 129 | 0,8 s | 11,6 s | 11,92 | Natural |
| 1 | 13 | 12.797 | 122 | 0,6 s | 10,8 s | 11,89 | Natural |
| 1 | 14 | 13.820 | 153 | 0,7 s | 13,5 s | 11,85 | Natural |
| 1 | 15 | 14.845 | 165 | 0,8 s | 14,7 s | 11,80 | Natural |
| 1 | 16 | 15.869 | 100 | 1,0 s | 9,4 s | 11,77 | Natural |
| 1 | 17 | 16.893 | 122 | 0,7 s | 11,0 s | 11,73 | Natural |
| 1 | 18 | 17.917 | 130 | 0,8 s | 11,8 s | 11,69 | Natural |
| 1 | 19 | 18.941 | 157 | 1,0 s | 14,4 s | 11,65 | Natural |
| 1 | 20 | 19.964 | 103 | 0,7 s | 9,4 s | 11,62 | Natural |
| 1 | 21 | 20.989 | 120 | 0,8 s | 11,1 s | 11,57 | Natural |
| 1 | 22 | 22.013 | 133 | 0,9 s | 12,4 s | 11,54 | Natural |
| 1 | 23 | 23.037 | 161 | 0,7 s | 14,6 s | 11,49 | Natural |
| 1 | 24 | 24.061 | 102 | 0,8 s | 9,6 s | 11,46 | Natural |
| 1 | 25 | 25.085 | 118 | 0,9 s | 11,2 s | 11,43 | Natural |
| 1 | 26 | 26.109 | 132 | 1,1 s | 12,6 s | 11,39 | Natural |
| 1 | 27 | 27.133 | 160 | 0,8 s | 14,8 s | 11,35 | Natural |
| 1 | 28 | 28.157 | 106 | 0,9 s | 10,2 s | 11,31 | Natural |
| 1 | 29 | 29.180 | 118 | 1,1 s | 11,5 s | 11,28 | Natural |
| 1 | 30 | 30.205 | 136 | 0,8 s | 12,8 s | 11,24 | Natural |
| 1 | 31 | 31.229 | 166 | 0,9 s | 15,7 s | 11,20 | Natural |
| 1 | 32 | 32.253 | 105 | 1,2 s | 10,5 s | 11,17 | Natural |
| 1 | 33 | 33.277 | 120 | 0,8 s | 11,5 s | 11,13 | Natural |
| 1 | 34 | 34.300 | 135 | 0,9 s | 13,0 s | 11,10 | Natural |
| 1 | 35 | 35.325 | 164 | 1,1 s | 15,8 s | 11,07 | Natural |
| 1 | 36 | 36.349 | 109 | 0,8 s | 10,6 s | 11,04 | Natural |
| 1 | 37 | 37.373 | 120 | 0,9 s | 11,8 s | 10,99 | Natural |
| 1 | 38 | 38.397 | 139 | 1,0 s | 13,6 s | 10,96 | Natural |
| 1 | 39 | 39.421 | 170 | 1,3 s | 16,7 s | 10,93 | Natural |
| 1 | 40 | 40.445 | 113 | 0,9 s | 11,2 s | 10,91 | Natural |
| 1 | 41 | 41.469 | 124 | 1,1 s | 12,6 s | 10,66 | Natural |
| 1 | 42 | 42.493 | 143 | 1,3 s | 14,4 s | 10,83 | Natural |
| 1 | 43 | 43.517 | 175 | 0,9 s | 17,0 s | 10,80 | Natural |
| 1 | 44 | 44.541 | 110 | 1,0 s | 11,2 s | 10,77 | Natural |
| 1 | 45 | 45.565 | 126 | 1,2 s | 12,8 s | 10,74 | Natural |
| 1 | 46 | 46.588 | 140 | 0,9 s | 13,9 s | 10,70 | Natural |
| 1 | 47 | 47.613 | 170 | 1,0 s | 16,9 s | 10,67 | Natural |
| 1 | 48 | 48.637 | 108 | 1,2 s | 11,3 s | 10,65 | Natural |
| 1 | 49 | 49.661 | 122 | 0,9 s | 12,3 s | 10,61 | Natural |
| 1 | 50 | 50.685 | 138 | 1,0 s | 13,9 s | 10,58 | Natural |
| 1 | 51 | 51.709 | 168 | 1,2 s | 17,0 s | 10,54 | Natural |
| 1 | 52 | 52.733 | 108 | 1,4 s | 11,6 s | 10,53 | Natural |
| 1 | 53 | 53.757 | 122 | 1,0 s | 12,5 s | 10,49 | Natural |
| 1 | 54 | 54.781 | 138 | 1,2 s | 14,3 s | 10,46 | Natural |
| 1 | 55 | 55.805 | 168 | 1,5 s | 17,5 s | 10,42 | Natural |
| 1 | 56 | 56.829 | 106 | 1,0 s | 11,1 s | 10,40 | Natural |
| 1 | 57 | 57.853 | 122 | 1,1 s | 12,8 s | 10,37 | Natural |
| 1 | 58 | 58.877 | 136 | 1,3 s | 14,4 s | 10,33 | Natural |
| 1 | 59 | 59.901 | 165 | 1,0 s | 16,9 s | 10,30 | Natural |
| 1 | 60 | 60.925 | 105 | 1,1 s | 11,3 s | 10,28 | Natural |
| 1 | 61 | 61.949 | 120 | 1,4 s | 13,0 s | 10,25 | Natural |
| 1 | 62 | 62.973 | 135 | 0,9 s | 14,1 s | 10,21 | Natural |
| 1 | 63 | 63.997 | 164 | 1,1 s | 17,1 s | 10,19 | Natural |
| 1 | 64 | 65.021 | 109 | 1,3 s | 11,9 s | 10,17 | Natural |
| 1 | 65 | 66.045 | 120 | 1,6 s | 13,3 s | 10,13 | Natural |
| 1 | 66 | 67.069 | 139 | 1,1 s | 14,8 s | 10,11 | Natural |
| 1 | 67 | 68.093 | 170 | 1,3 s | 18,1 s | 10,07 | Natural |
| 1 | 68 | 69.117 | 111 | 1,6 s | 12,5 s | 10,06 | Natural |
| 1 | 69 | 70.141 | 124 | 1,1 s | 13,3 s | 10,02 | Natural |
| 1 | 70 | 71.165 | 141 | 1,3 s | 15,3 s | 9,99 | Natural |
| 1 | 71 | 72.189 | 172 | 1,5 s | 18,6 s | 9,96 | Natural |
| 1 | 72 | 73.212 | 109 | 1,1 s | 11,9 s | 9,94 | Natural |
| 1 | 73 | 74.237 | 124 | 1,3 s | 13,7 s | 9,91 | Natural |
| 1 | 74 | 75.260 | 139 | 1,4 s | 15,4 s | 9,88 | Natural |
| 1 | 75 | 76.285 | 169 | 1,7 s | 18,8 s | 9,84 | Natural |
| 1 | 76 | 77.309 | 108 | 1,2 s | 12,1 s | 9,83 | Natural |
| 1 | 77 | 78.332 | 122 | 1,4 s | 13,7 s | 9,81 | Natural |
| 1 | 78 | 79.356 | 138 | 1,7 s | 15,8 s | 9,78 | Natural |
| 1 | 79 | 80.381 | 168 | 1,2 s | 18,4 s | 9,74 | Natural |
| 1 | 80 | 81.405 | 110 | 1,4 s | 12,6 s | 9,73 | Natural |
| 1 | 81 | 82.429 | 122 | 1,6 s | 14,1 s | 9,70 | Natural |
| 1 | 82 | 83.452 | 140 | 1,2 s | 15,5 s | 9,67 | Natural |
| 1 | 83 | 84.477 | 171 | 1,4 s | 19,0 s | 9,64 | Natural |
| 1 | 84 | 85.501 | 113 | 1,6 s | 13,3 s | 9,62 | Natural |
| 1 | 85 | 86.525 | 124 | 1,2 s | 14,0 s | 9,60 | Natural |
| 1 | 86 | 87.549 | 143 | 1,4 s | 16,2 s | 9,57 | Natural |
| 1 | 87 | 88.573 | 175 | 1,5 s | 19,8 s | 9,53 | Natural |
| 1 | 88 | 89.597 | 112 | 1,9 s | 13,5 s | 9,52 | Natural |
| 1 | 89 | 90.620 | 126 | 1,3 s | 14,5 s | 9,50 | Natural |
| 1 | 90 | 91.645 | 142 | 1,5 s | 16,4 s | 9,46 | Natural |
| 1 | 91 | 92.669 | 173 | 1,9 s | 20,1 s | 9,43 | Natural |
| 1 | 92 | 93.693 | 111 | 1,3 s | 13,0 s | 9,42 | Natural |
| 1 | 93 | 94.717 | 124 | 1,5 s | 14,6 s | 9,39 | Natural |
| 1 | 94 | 95.741 | 141 | 1,7 s | 16,7 s | 9,37 | Natural |
| 1 | 95 | 96.765 | 172 | 1,3 s | 19,6 s | 9,34 | Natural |
| 1 | 96 | 97.789 | 111 | 1,5 s | 13,3 s | 9,33 | Natural |
| 1 | 97 | 98.813 | 124 | 1,7 s | 15,0 s | 9,30 | Natural |
| 1 | 98 | 99.837 | 141 | 1,3 s | 16,4 s | 9,27 | Natural |
| 1 | 99 | 100.861 | 172 | 1,4 s | 19,9 s | 9,24 | Natural |
| 1 | 100 | 101.884 | 111 | 1,6 s | 13,6 s | 9,22 | Natural |
| 1 | 101 | 102.908 | 124 | 2,0 s | 15,4 s | 9,20 | Natural |
| 1 | 102 | 103.933 | 141 | 1,5 s | 16,7 s | 9,17 | Natural |
| 1 | 103 | 104.957 | 172 | 1,7 s | 20,4 s | 9,14 | Natural |
| 1 | 104 | 105.981 | 111 | 2,1 s | 14,1 s | 9,14 | Natural |
| 1 | 105 | 107.005 | 124 | 1,4 s | 14,9 s | 9,10 | Natural |
| 1 | 106 | 108.029 | 141 | 1,6 s | 17,0 s | 9,08 | Natural |
| 1 | 107 | 109.053 | 172 | 1,9 s | 20,8 s | 9,05 | Natural |
| 1 | 108 | 110.077 | 113 | 1,4 s | 13,8 s | 9,04 | Natural |
| 1 | 109 | 111.100 | 124 | 1,6 s | 15,3 s | 9,02 | Natural |
| 1 | 110 | 112.125 | 143 | 1,9 s | 17,7 s | 8,99 | Natural |
| 1 | 111 | 113.149 | 175 | 1,3 s | 20,8 s | 8,96 | Natural |
| 1 | 112 | 114.173 | 116 | 1,5 s | 14,4 s | 8,95 | Natural |
| 1 | 113 | 115.197 | 126 | 1,8 s | 15,8 s | 8,93 | Natural |
| 1 | 114 | 116.221 | 146 | 2,2 s | 18,5 s | 8,89 | Natural |
| 1 | 115 | 117.245 | 179 | 1,6 s | 21,6 s | 8,86 | Natural |
| 1 | 116 | 118.269 | 119 | 1,8 s | 15,1 s | 8,86 | Natural |
| 1 | 117 | 119.293 | 128 | 2,1 s | 16,5 s | 8,83 | Natural |
| 1 | 118 | 120.317 | 149 | 1,5 s | 18,3 s | 8,81 | Natural |
| 1 | 119 | 121.341 | 183 | 1,7 s | 22,5 s | 8,77 | Natural |
| 1 | 120 | 122.365 | 122 | 2,1 s | 15,9 s | 8,77 | Natural |
| 1 | 121 | 123.389 | 130 | 1,5 s | 16,2 s | 8,74 | Natural |
| 1 | 122 | 124.413 | 152 | 1,8 s | 19,1 s | 8,72 | Natural |
| 1 | 123 | 125.437 | 187 | 2,0 s | 23,4 s | 8,69 | Natural |
| 1 | 124 | 126.461 | 125 | 2,3 s | 16,6 s | 8,68 | Natural |
| 1 | 125 | 127.484 | 132 | 1,6 s | 16,8 s | 8,66 | Natural |
| 1 | 126 | 128.509 | 155 | 1,9 s | 19,7 s | 8,64 | Natural |
| 1 | 127 | 129.533 | 191 | 2,4 s | 24,4 s | 8,61 | Natural |
| 1 | 128 | 130.557 | 128 | 1,7 s | 16,4 s | 8,61 | Natural |
| 1 | 129 | 131.581 | 134 | 1,9 s | 17,4 s | 8,57 | Natural |
| 1 | 130 | 132.605 | 158 | 2,3 s | 20,6 s | 8,55 | Natural |
| 1 | 131 | 133.629 | 195 | 1,6 s | 24,3 s | 8,53 | Natural |
| 1 | 132 | 134.652 | 131 | 1,9 s | 17,1 s | 8,52 | Natural |
| 1 | 133 | 135.677 | 136 | 2,2 s | 18,1 s | 8,50 | Natural |
| 1 | 134 | 136.701 | 161 | 1,6 s | 20,5 s | 8,47 | Natural |
| 1 | 135 | 137.725 | 199 | 1,9 s | 25,3 s | 8,44 | Natural |
| 1 | 136 | 138.749 | 134 | 2,0 s | 17,8 s | 8,44 | Natural |
| 1 | 137 | 139.773 | 138 | 2,5 s | 18,8 s | 8,41 | Natural |
| 1 | 138 | 140.797 | 164 | 1,8 s | 21,2 s | 8,39 | Natural |
| 1 | 139 | 141.821 | 203 | 2,0 s | 26,2 s | 8,36 | Natural |
| 1 | 140 | 142.845 | 137 | 2,5 s | 18,8 s | 8,36 | Natural |
| 1 | 141 | 143.869 | 140 | 1,8 s | 18,4 s | 8,34 | Natural |
| 1 | 142 | 144.893 | 167 | 2,0 s | 21,9 s | 8,31 | Natural |
| 1 | 143 | 145.916 | 207 | 2,4 s | 27,3 s | 8,28 | Natural |
| 1 | 144 | 146.941 | 140 | 1,7 s | 18,5 s | 8,28 | Natural |
| 1 | 145 | 147.965 | 142 | 2,0 s | 19,1 s | 8,26 | Natural |
| 1 | 146 | 148.988 | 170 | 2,3 s | 22,8 s | 8,23 | Natural |
| 1 | 147 | 150.013 | 211 | 1,7 s | 27,3 s | 8,21 | Natural |
| 1 | 148 | 151.037 | 143 | 1,9 s | 19,2 s | 8,20 | Natural |
| 1 | 149 | 152.061 | 144 | 2,2 s | 19,6 s | 8,18 | Natural |
| 1 | 150 | 153.084 | 173 | 2,6 s | 23,7 s | 8,16 | Natural |
| 1 | 151 | 154.109 | 215 | 1,9 s | 28,2 s | 8,13 | Natural |
| 1 | 152 | 155.133 | 146 | 2,2 s | 20,0 s | 8,13 | Natural |
| 1 | 153 | 156.157 | 146 | 2,7 s | 20,5 s | 8,11 | Natural |
| 1 | 154 | 157.181 | 176 | 1,8 s | 23,4 s | 8,09 | Natural |
| 1 | 155 | 158.205 | 219 | 2,1 s | 29,2 s | 8,06 | Natural |
| 1 | 156 | 159.229 | 149 | 2,6 s | 21,0 s | 8,05 | Natural |
| 1 | 157 | 160.252 | 148 | 1,8 s | 20,1 s | 8,04 | Natural |
| 1 | 158 | 161.277 | 179 | 2,1 s | 24,3 s | 8,02 | Natural |
| 1 | 159 | 162.300 | 223 | 2,4 s | 30,2 s | 7,99 | Natural |
| 1 | 160 | 163.324 | 152 | 1,7 s | 20,6 s | 7,99 | Natural |
| 1 | 161 | 164.349 | 150 | 2,0 s | 20,7 s | 7,97 | Natural |
| 1 | 162 | 165.373 | 182 | 2,3 s | 25,1 s | 7,94 | Natural |
| 1 | 163 | 166.397 | 227 | 2,8 s | 31,4 s | 7,91 | Natural |
| 1 | 164 | 167.421 | 155 | 2,0 s | 21,5 s | 7,90 | Natural |
| 1 | 165 | 168.445 | 152 | 2,3 s | 21,4 s | 7,89 | Natural |
| 1 | 166 | 169.469 | 185 | 2,7 s | 26,1 s | 7,86 | Natural |
| 1 | 167 | 170.493 | 231 | 1,9 s | 31,2 s | 7,84 | Natural |
| 1 | 168 | 171.517 | 158 | 2,2 s | 22,3 s | 7,84 | Natural |
| 1 | 169 | 172.541 | 154 | 2,6 s | 22,1 s | 7,83 | Natural |
| 1 | 170 | 173.565 | 188 | 1,9 s | 25,9 s | 7,80 | Natural |
| 1 | 171 | 174.589 | 235 | 2,2 s | 32,3 s | 7,77 | Natural |
| 1 | 172 | 175.613 | 161 | 2,5 s | 23,1 s | 7,76 | Natural |
| 1 | 173 | 176.637 | 156 | 2,9 s | 22,9 s | 7,75 | Natural |
| 1 | 174 | 177.661 | 191 | 2,1 s | 26,7 s | 7,73 | Natural |
| 1 | 175 | 178.684 | 239 | 2,4 s | 33,3 s | 7,71 | Natural |
| 1 | 176 | 179.709 | 164 | 3,0 s | 24,1 s | 7,70 | Natural |
| 1 | 177 | 180.733 | 158 | 2,1 s | 22,5 s | 7,68 | Natural |
| 1 | 178 | 181.757 | 194 | 2,5 s | 27,7 s | 7,66 | Natural |
| 1 | 179 | 182.781 | 243 | 2,9 s | 34,5 s | 7,64 | Natural |
| 1 | 180 | 183.805 | 167 | 2,0 s | 23,8 s | 7,63 | Natural |
| 1 | 181 | 184.828 | 160 | 2,3 s | 23,2 s | 7,62 | Natural |
| 1 | 182 | 185.853 | 197 | 2,7 s | 28,5 s | 7,60 | Natural |
| 1 | 183 | 186.877 | 247 | 2,0 s | 34,5 s | 7,57 | Natural |
| 1 | 184 | 187.901 | 170 | 2,4 s | 24,7 s | 7,57 | Natural |
| 1 | 185 | 188.925 | 162 | 2,6 s | 23,9 s | 7,55 | Natural |
| 1 | 186 | 189.949 | 200 | 3,1 s | 29,5 s | 7,53 | Natural |
| 1 | 187 | 190.973 | 251 | 2,2 s | 35,7 s | 7,46 | Natural |
| 1 | 188 | 191.997 | 173 | 2,6 s | 25,5 s | 7,51 | Natural |
| 1 | 189 | 193.020 | 164 | 3,1 s | 24,9 s | 7,49 | Natural |
| 1 | 190 | 194.044 | 203 | 2,2 s | 29,3 s | 7,47 | Natural |
| 1 | 191 | 195.069 | 255 | 2,5 s | 36,6 s | 7,45 | Natural |
| 1 | 192 | 196.093 | 176 | 3,0 s | 26,5 s | 7,44 | Natural |
| 1 | 193 | 197.117 | 166 | 2,1 s | 24,3 s | 7,42 | Natural |
| 1 | 194 | 198.141 | 206 | 2,5 s | 30,2 s | 7,41 | Natural |
| 1 | 195 | 199.164 | 259 | 2,8 s | 37,8 s | 7,39 | Natural |
| 1 | 196 | 200.189 | 179 | 2,1 s | 26,2 s | 7,38 | Natural |
| 1 | 197 | 201.213 | 168 | 2,3 s | 25,0 s | 7,35 | Natural |
| 1 | 198 | 202.237 | 209 | 2,7 s | 31,0 s | 7,34 | Natural |
| 1 | 199 | 203.261 | 263 | 3,3 s | 39,0 s | 7,32 | Natural |
| 1 | 200 | 204.285 | 180 | 2,3 s | 26,8 s | 7,32 | Natural |
| 1 | 201 | 205.309 | 170 | 2,7 s | 25,8 s | 7,30 | Natural |
| 1 | 202 | 206.333 | 210 | 3,3 s | 32,0 s | 7,28 | Natural |
| 1 | 203 | 207.357 | 264 | 2,2 s | 38,4 s | 7,27 | Natural |
| 1 | 204 | 208.381 | 180 | 2,6 s | 27,2 s | 7,25 | Natural |
| 1 | 205 | 209.404 | 170 | 3,2 s | 26,5 s | 7,25 | Natural |
| 1 | 206 | 210.429 | 210 | 2,2 s | 31,1 s | 7,23 | Natural |
| 1 | 207 | 211.453 | 264 | 2,6 s | 39,1 s | 7,20 | Natural |
| 1 | 208 | 212.477 | 182 | 3,2 s | 28,3 s | 7,20 | Natural |
| 1 | 209 | 213.501 | 170 | 2,1 s | 25,6 s | 7,18 | Natural |
| 1 | 210 | 214.525 | 212 | 2,5 s | 31,9 s | 7,17 | Natural |
| 1 | 211 | 215.549 | 267 | 2,8 s | 40,0 s | 7,14 | Natural |
| 1 | 212 | 216.573 | 183 | 3,4 s | 28,9 s | 7,14 | Natural |
| 1 | 213 | 217.597 | 172 | 2,4 s | 26,4 s | 7,12 | Natural |
| 1 | 214 | 218.621 | 213 | 2,8 s | 32,6 s | 7,11 | Natural |
| 1 | 215 | 219.645 | 268 | 3,3 s | 40,9 s | 7,09 | Natural |
| 1 | 216 | 220.669 | 183 | 2,3 s | 28,0 s | 7,08 | Natural |
| 1 | 217 | 221.693 | 172 | 2,7 s | 26,9 s | 7,07 | Natural |
| 1 | 218 | 222.717 | 213 | 3,0 s | 33,1 s | 7,05 | Natural |
| 1 | 219 | 223.741 | 268 | 2,3 s | 40,3 s | 7,03 | Natural |
| 1 | 220 | 224.765 | 183 | 2,7 s | 28,6 s | 7,03 | Natural |
| 1 | 221 | 225.788 | 172 | 3,0 s | 27,4 s | 7,01 | Natural |
| 1 | 222 | 226.813 | 213 | 3,5 s | 33,8 s | 7,00 | Natural |
| 1 | 223 | 227.837 | 268 | 2,6 s | 40,8 s | 6,97 | Natural |
| 1 | 224 | 228.861 | 185 | 2,9 s | 29,3 s | 6,97 | Natural |
| 1 | 225 | 229.885 | 172 | 3,6 s | 28,2 s | 6,97 | Natural |
| 1 | 226 | 230.909 | 215 | 2,6 s | 33,4 s | 6,94 | Natural |
| 1 | 227 | 231.933 | 271 | 3,0 s | 42,0 s | 6,92 | Natural |
| 1 | 228 | 232.956 | 188 | 3,4 s | 30,5 s | 6,91 | Natural |
| 1 | 229 | 233.981 | 174 | 2,4 s | 27,5 s | 6,90 | Natural |
| 1 | 230 | 235.005 | 218 | 2,8 s | 34,3 s | 6,89 | Natural |
| 1 | 231 | 236.029 | 275 | 3,5 s | 43,4 s | 6,87 | Natural |
| 1 | 232 | 237.053 | 189 | 2,4 s | 29,8 s | 6,86 | Natural |
| 1 | 233 | 238.077 | 176 | 2,8 s | 28,4 s | 6,85 | Natural |
| 1 | 234 | 239.101 | 219 | 3,0 s | 34,9 s | 6,83 | Natural |
| 1 | 235 | 240.124 | 276 | 3,7 s | 44,1 s | 6,81 | Natural |
| 1 | 236 | 241.149 | 189 | 2,7 s | 30,3 s | 6,81 | Natural |
| 1 | 237 | 242.173 | 176 | 3,1 s | 28,8 s | 6,80 | Natural |
| 1 | 238 | 243.196 | 219 | 3,7 s | 35,9 s | 6,78 | Natural |
| 1 | 239 | 244.221 | 276 | 2,7 s | 43,4 s | 6,76 | Natural |
| 1 | 240 | 245.245 | 189 | 2,9 s | 30,7 s | 6,77 | Natural |
| 1 | 241 | 246.269 | 176 | 3,6 s | 29,5 s | 6,75 | Natural |
| 1 | 242 | 247.293 | 219 | 2,5 s | 34,9 s | 6,74 | Natural |
| 1 | 243 | 248.317 | 276 | 2,9 s | 43,9 s | 6,71 | Natural |
| 1 | 244 | 249.341 | 191 | 3,7 s | 32,2 s | 6,66 | Natural |
| 1 | 245 | 250.365 | 176 | 2,6 s | 28,7 s | 6,70 | Natural |
| 1 | 246 | 251.389 | 221 | 2,7 s | 35,7 s | 6,68 | Natural |
| 1 | 247 | 252.413 | 279 | 3,2 s | 44,9 s | 6,66 | Natural |
| 1 | 248 | 253.437 | 192 | 3,9 s | 32,5 s | 6,66 | Natural |
| 1 | 249 | 254.461 | 178 | 2,8 s | 29,4 s | 6,65 | Natural |
| 1 | 250 | 255.484 | 222 | 3,2 s | 36,5 s | 6,63 | Natural |
| 1 | 251 | 256.509 | 280 | 3,9 s | 46,1 s | 6,61 | Natural |
| 1 | 252 | 257.533 | 192 | 2,6 s | 31,5 s | 6,61 | Natural |
| 1 | 253 | 258.557 | 178 | 3,1 s | 29,9 s | 6,60 | Natural |
| 1 | 254 | 259.581 | 222 | 3,7 s | 37,3 s | 6,58 | Natural |
| 1 | 255 | 260.604 | 280 | 2,6 s | 45,2 s | 6,56 | Natural |
| 1 | 256 | 261.117 | 192 | 2,3 s | 31,4 s | 6,57 | Natural |
| 1 | 257 | 262.013 | 13 | 2,5 s | 4,2 s | 7,11 | Natural |

</details>

[Mediciones](mediciones.json) · [Configuración](configuracion.json) · [Historial reproducible](historiales.json.gz)

La velocidad cuenta todos los tokens de salida. Con razonamiento activado no equivale exclusivamente a la velocidad del texto visible.
