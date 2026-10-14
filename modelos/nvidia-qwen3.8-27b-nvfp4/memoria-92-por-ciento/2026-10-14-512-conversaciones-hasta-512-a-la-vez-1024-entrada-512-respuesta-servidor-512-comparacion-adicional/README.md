# 512 conversaciones, hasta 512 a la vez; 1.024 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 92% del GB10.

**Límite impuesto al servidor: 512 solicitudes activas** (`--max-num-seqs 512`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 61/512 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 347 activas en el motor; cola máxima 508.
- **Tiempo para completar la prueba:** 598,2 s.

Se enviaron **512 conversaciones**, hasta **512 a la vez**. Cada una pidió **1.024 tokens de entrada + 512 de respuesta = 1.536 tokens**.

<details>
<summary>Ver tokens y finalización de las 512 conversaciones</summary>

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 2 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 3 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 4 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 5 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 6 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 7 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 8 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 9 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 10 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 11 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 12 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 13 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 14 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 15 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 16 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 17 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 18 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 19 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 20 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 21 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 22 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 23 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 24 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 25 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 26 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 27 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 28 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 29 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 30 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 31 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 32 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 33 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 34 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 35 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 36 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 37 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 38 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 39 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 40 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 41 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 42 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 43 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 44 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 45 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 46 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 47 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 48 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 49 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 50 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 51 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 52 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 53 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 54 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 55 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 56 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 57 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 58 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 59 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 60 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 61 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 62 | — | 512 | — | — | En curso | No acreditado |
| 63 | — | 512 | — | — | En curso | No acreditado |
| 64 | — | 512 | — | — | En curso | No acreditado |
| 65 | — | 512 | — | — | En curso | No acreditado |
| 66 | — | 512 | — | — | En curso | No acreditado |
| 67 | — | 512 | — | — | En curso | No acreditado |
| 68 | — | 512 | — | — | En curso | No acreditado |
| 69 | — | 512 | — | — | En curso | No acreditado |
| 70 | — | 512 | — | — | En curso | No acreditado |
| 71 | — | 512 | — | — | En curso | No acreditado |
| 72 | — | 512 | — | — | En curso | No acreditado |
| 73 | — | 512 | — | — | En curso | No acreditado |
| 74 | — | 512 | — | — | En curso | No acreditado |
| 75 | — | 512 | — | — | En curso | No acreditado |
| 76 | — | 512 | — | — | En curso | No acreditado |
| 77 | — | 512 | — | — | En curso | No acreditado |
| 78 | — | 512 | — | — | En curso | No acreditado |
| 79 | — | 512 | — | — | En curso | No acreditado |
| 80 | — | 512 | — | — | En curso | No acreditado |
| 81 | — | 512 | — | — | En curso | No acreditado |
| 82 | — | 512 | — | — | En curso | No acreditado |
| 83 | — | 512 | — | — | En curso | No acreditado |
| 84 | — | 512 | — | — | En curso | No acreditado |
| 85 | — | 512 | — | — | En curso | No acreditado |
| 86 | — | 512 | — | — | En curso | No acreditado |
| 87 | — | 512 | — | — | En curso | No acreditado |
| 88 | — | 512 | — | — | En curso | No acreditado |
| 89 | — | 512 | — | — | En curso | No acreditado |
| 90 | — | 512 | — | — | En curso | No acreditado |
| 91 | — | 512 | — | — | En curso | No acreditado |
| 92 | — | 512 | — | — | En curso | No acreditado |
| 93 | — | 512 | — | — | En curso | No acreditado |
| 94 | — | 512 | — | — | En curso | No acreditado |
| 95 | — | 512 | — | — | En curso | No acreditado |
| 96 | — | 512 | — | — | En curso | No acreditado |
| 97 | — | 512 | — | — | En curso | No acreditado |
| 98 | — | 512 | — | — | En curso | No acreditado |
| 99 | — | 512 | — | — | En curso | No acreditado |
| 100 | — | 512 | — | — | En curso | No acreditado |
| 101 | — | 512 | — | — | En curso | No acreditado |
| 102 | — | 512 | — | — | En curso | No acreditado |
| 103 | — | 512 | — | — | En curso | No acreditado |
| 104 | — | 512 | — | — | En curso | No acreditado |
| 105 | — | 512 | — | — | En curso | No acreditado |
| 106 | — | 512 | — | — | En curso | No acreditado |
| 107 | — | 512 | — | — | En curso | No acreditado |
| 108 | — | 512 | — | — | En curso | No acreditado |
| 109 | — | 512 | — | — | En curso | No acreditado |
| 110 | — | 512 | — | — | En curso | No acreditado |
| 111 | — | 512 | — | — | En curso | No acreditado |
| 112 | — | 512 | — | — | En curso | No acreditado |
| 113 | — | 512 | — | — | En curso | No acreditado |
| 114 | — | 512 | — | — | En curso | No acreditado |
| 115 | — | 512 | — | — | En curso | No acreditado |
| 116 | — | 512 | — | — | En curso | No acreditado |
| 117 | — | 512 | — | — | En curso | No acreditado |
| 118 | — | 512 | — | — | En curso | No acreditado |
| 119 | — | 512 | — | — | En curso | No acreditado |
| 120 | — | 512 | — | — | En curso | No acreditado |
| 121 | — | 512 | — | — | En curso | No acreditado |
| 122 | — | 512 | — | — | En curso | No acreditado |
| 123 | — | 512 | — | — | En curso | No acreditado |
| 124 | — | 512 | — | — | En curso | No acreditado |
| 125 | — | 512 | — | — | En curso | No acreditado |
| 126 | — | 512 | — | — | En curso | No acreditado |
| 127 | — | 512 | — | — | En curso | No acreditado |
| 128 | — | 512 | — | — | En curso | No acreditado |
| 129 | — | 512 | — | — | En curso | No acreditado |
| 130 | — | 512 | — | — | En curso | No acreditado |
| 131 | — | 512 | — | — | En curso | No acreditado |
| 132 | — | 512 | — | — | En curso | No acreditado |
| 133 | — | 512 | — | — | En curso | No acreditado |
| 134 | — | 512 | — | — | En curso | No acreditado |
| 135 | — | 512 | — | — | En curso | No acreditado |
| 136 | — | 512 | — | — | En curso | No acreditado |
| 137 | — | 512 | — | — | En curso | No acreditado |
| 138 | — | 512 | — | — | En curso | No acreditado |
| 139 | — | 512 | — | — | En curso | No acreditado |
| 140 | — | 512 | — | — | En curso | No acreditado |
| 141 | — | 512 | — | — | En curso | No acreditado |
| 142 | — | 512 | — | — | En curso | No acreditado |
| 143 | — | 512 | — | — | En curso | No acreditado |
| 144 | — | 512 | — | — | En curso | No acreditado |
| 145 | — | 512 | — | — | En curso | No acreditado |
| 146 | — | 512 | — | — | En curso | No acreditado |
| 147 | — | 512 | — | — | En curso | No acreditado |
| 148 | — | 512 | — | — | En curso | No acreditado |
| 149 | — | 512 | — | — | En curso | No acreditado |
| 150 | — | 512 | — | — | En curso | No acreditado |
| 151 | — | 512 | — | — | En curso | No acreditado |
| 152 | — | 512 | — | — | En curso | No acreditado |
| 153 | — | 512 | — | — | En curso | No acreditado |
| 154 | — | 512 | — | — | En curso | No acreditado |
| 155 | — | 512 | — | — | En curso | No acreditado |
| 156 | — | 512 | — | — | En curso | No acreditado |
| 157 | — | 512 | — | — | En curso | No acreditado |
| 158 | — | 512 | — | — | En curso | No acreditado |
| 159 | — | 512 | — | — | En curso | No acreditado |
| 160 | — | 512 | — | — | En curso | No acreditado |
| 161 | — | 512 | — | — | En curso | No acreditado |
| 162 | — | 512 | — | — | En curso | No acreditado |
| 163 | — | 512 | — | — | En curso | No acreditado |
| 164 | — | 512 | — | — | En curso | No acreditado |
| 165 | — | 512 | — | — | En curso | No acreditado |
| 166 | — | 512 | — | — | En curso | No acreditado |
| 167 | — | 512 | — | — | En curso | No acreditado |
| 168 | — | 512 | — | — | En curso | No acreditado |
| 169 | — | 512 | — | — | En curso | No acreditado |
| 170 | — | 512 | — | — | En curso | No acreditado |
| 171 | — | 512 | — | — | En curso | No acreditado |
| 172 | — | 512 | — | — | En curso | No acreditado |
| 173 | — | 512 | — | — | En curso | No acreditado |
| 174 | — | 512 | — | — | En curso | No acreditado |
| 175 | — | 512 | — | — | En curso | No acreditado |
| 176 | — | 512 | — | — | En curso | No acreditado |
| 177 | — | 512 | — | — | En curso | No acreditado |
| 178 | — | 512 | — | — | En curso | No acreditado |
| 179 | — | 512 | — | — | En curso | No acreditado |
| 180 | — | 512 | — | — | En curso | No acreditado |
| 181 | — | 512 | — | — | En curso | No acreditado |
| 182 | — | 512 | — | — | En curso | No acreditado |
| 183 | — | 512 | — | — | En curso | No acreditado |
| 184 | — | 512 | — | — | En curso | No acreditado |
| 185 | — | 512 | — | — | En curso | No acreditado |
| 186 | — | 512 | — | — | En curso | No acreditado |
| 187 | — | 512 | — | — | En curso | No acreditado |
| 188 | — | 512 | — | — | En curso | No acreditado |
| 189 | — | 512 | — | — | En curso | No acreditado |
| 190 | — | 512 | — | — | En curso | No acreditado |
| 191 | — | 512 | — | — | En curso | No acreditado |
| 192 | — | 512 | — | — | En curso | No acreditado |
| 193 | — | 512 | — | — | En curso | No acreditado |
| 194 | — | 512 | — | — | En curso | No acreditado |
| 195 | — | 512 | — | — | En curso | No acreditado |
| 196 | — | 512 | — | — | En curso | No acreditado |
| 197 | — | 512 | — | — | En curso | No acreditado |
| 198 | — | 512 | — | — | En curso | No acreditado |
| 199 | — | 512 | — | — | En curso | No acreditado |
| 200 | — | 512 | — | — | En curso | No acreditado |
| 201 | — | 512 | — | — | En curso | No acreditado |
| 202 | — | 512 | — | — | En curso | No acreditado |
| 203 | — | 512 | — | — | En curso | No acreditado |
| 204 | — | 512 | — | — | En curso | No acreditado |
| 205 | — | 512 | — | — | En curso | No acreditado |
| 206 | — | 512 | — | — | En curso | No acreditado |
| 207 | — | 512 | — | — | En curso | No acreditado |
| 208 | — | 512 | — | — | En curso | No acreditado |
| 209 | — | 512 | — | — | En curso | No acreditado |
| 210 | — | 512 | — | — | En curso | No acreditado |
| 211 | — | 512 | — | — | En curso | No acreditado |
| 212 | — | 512 | — | — | En curso | No acreditado |
| 213 | — | 512 | — | — | En curso | No acreditado |
| 214 | — | 512 | — | — | En curso | No acreditado |
| 215 | — | 512 | — | — | En curso | No acreditado |
| 216 | — | 512 | — | — | En curso | No acreditado |
| 217 | — | 512 | — | — | En curso | No acreditado |
| 218 | — | 512 | — | — | En curso | No acreditado |
| 219 | — | 512 | — | — | En curso | No acreditado |
| 220 | — | 512 | — | — | En curso | No acreditado |
| 221 | — | 512 | — | — | En curso | No acreditado |
| 222 | — | 512 | — | — | En curso | No acreditado |
| 223 | — | 512 | — | — | En curso | No acreditado |
| 224 | — | 512 | — | — | En curso | No acreditado |
| 225 | — | 512 | — | — | En curso | No acreditado |
| 226 | — | 512 | — | — | En curso | No acreditado |
| 227 | — | 512 | — | — | En curso | No acreditado |
| 228 | — | 512 | — | — | En curso | No acreditado |
| 229 | — | 512 | — | — | En curso | No acreditado |
| 230 | — | 512 | — | — | En curso | No acreditado |
| 231 | — | 512 | — | — | En curso | No acreditado |
| 232 | — | 512 | — | — | En curso | No acreditado |
| 233 | — | 512 | — | — | En curso | No acreditado |
| 234 | — | 512 | — | — | En curso | No acreditado |
| 235 | — | 512 | — | — | En curso | No acreditado |
| 236 | — | 512 | — | — | En curso | No acreditado |
| 237 | — | 512 | — | — | En curso | No acreditado |
| 238 | — | 512 | — | — | En curso | No acreditado |
| 239 | — | 512 | — | — | En curso | No acreditado |
| 240 | — | 512 | — | — | En curso | No acreditado |
| 241 | — | 512 | — | — | En curso | No acreditado |
| 242 | — | 512 | — | — | En curso | No acreditado |
| 243 | — | 512 | — | — | En curso | No acreditado |
| 244 | — | 512 | — | — | En curso | No acreditado |
| 245 | — | 512 | — | — | En curso | No acreditado |
| 246 | — | 512 | — | — | En curso | No acreditado |
| 247 | — | 512 | — | — | En curso | No acreditado |
| 248 | — | 512 | — | — | En curso | No acreditado |
| 249 | — | 512 | — | — | En curso | No acreditado |
| 250 | — | 512 | — | — | En curso | No acreditado |
| 251 | — | 512 | — | — | En curso | No acreditado |
| 252 | — | 512 | — | — | En curso | No acreditado |
| 253 | — | 512 | — | — | En curso | No acreditado |
| 254 | — | 512 | — | — | En curso | No acreditado |
| 255 | — | 512 | — | — | En curso | No acreditado |
| 256 | — | 512 | — | — | En curso | No acreditado |
| 257 | — | 512 | — | — | En curso | No acreditado |
| 258 | — | 512 | — | — | En curso | No acreditado |
| 259 | — | 512 | — | — | En curso | No acreditado |
| 260 | — | 512 | — | — | En curso | No acreditado |
| 261 | — | 512 | — | — | En curso | No acreditado |
| 262 | — | 512 | — | — | En curso | No acreditado |
| 263 | — | 512 | — | — | En curso | No acreditado |
| 264 | — | 512 | — | — | En curso | No acreditado |
| 265 | — | 512 | — | — | En curso | No acreditado |
| 266 | — | 512 | — | — | En curso | No acreditado |
| 267 | — | 512 | — | — | En curso | No acreditado |
| 268 | — | 512 | — | — | En curso | No acreditado |
| 269 | — | 512 | — | — | En curso | No acreditado |
| 270 | — | 512 | — | — | En curso | No acreditado |
| 271 | — | 512 | — | — | En curso | No acreditado |
| 272 | — | 512 | — | — | En curso | No acreditado |
| 273 | — | 512 | — | — | En curso | No acreditado |
| 274 | — | 512 | — | — | En curso | No acreditado |
| 275 | — | 512 | — | — | En curso | No acreditado |
| 276 | — | 512 | — | — | En curso | No acreditado |
| 277 | — | 512 | — | — | En curso | No acreditado |
| 278 | — | 512 | — | — | En curso | No acreditado |
| 279 | — | 512 | — | — | En curso | No acreditado |
| 280 | — | 512 | — | — | En curso | No acreditado |
| 281 | — | 512 | — | — | En curso | No acreditado |
| 282 | — | 512 | — | — | En curso | No acreditado |
| 283 | — | 512 | — | — | En curso | No acreditado |
| 284 | — | 512 | — | — | En curso | No acreditado |
| 285 | — | 512 | — | — | En curso | No acreditado |
| 286 | — | 512 | — | — | En curso | No acreditado |
| 287 | — | 512 | — | — | En curso | No acreditado |
| 288 | — | 512 | — | — | En curso | No acreditado |
| 289 | — | 512 | — | — | En curso | No acreditado |
| 290 | — | 512 | — | — | En curso | No acreditado |
| 291 | — | 512 | — | — | En curso | No acreditado |
| 292 | — | 512 | — | — | En curso | No acreditado |
| 293 | — | 512 | — | — | En curso | No acreditado |
| 294 | — | 512 | — | — | En curso | No acreditado |
| 295 | — | 512 | — | — | En curso | No acreditado |
| 296 | — | 512 | — | — | En curso | No acreditado |
| 297 | — | 512 | — | — | En curso | No acreditado |
| 298 | — | 512 | — | — | En curso | No acreditado |
| 299 | — | 512 | — | — | En curso | No acreditado |
| 300 | — | 512 | — | — | En curso | No acreditado |
| 301 | — | 512 | — | — | En curso | No acreditado |
| 302 | — | 512 | — | — | En curso | No acreditado |
| 303 | — | 512 | — | — | En curso | No acreditado |
| 304 | — | 512 | — | — | En curso | No acreditado |
| 305 | — | 512 | — | — | En curso | No acreditado |
| 306 | — | 512 | — | — | En curso | No acreditado |
| 307 | — | 512 | — | — | En curso | No acreditado |
| 308 | — | 512 | — | — | En curso | No acreditado |
| 309 | — | 512 | — | — | En curso | No acreditado |
| 310 | — | 512 | — | — | En curso | No acreditado |
| 311 | — | 512 | — | — | En curso | No acreditado |
| 312 | — | 512 | — | — | En curso | No acreditado |
| 313 | — | 512 | — | — | En curso | No acreditado |
| 314 | — | 512 | — | — | En curso | No acreditado |
| 315 | — | 512 | — | — | En curso | No acreditado |
| 316 | — | 512 | — | — | En curso | No acreditado |
| 317 | — | 512 | — | — | En curso | No acreditado |
| 318 | — | 512 | — | — | En curso | No acreditado |
| 319 | — | 512 | — | — | En curso | No acreditado |
| 320 | — | 512 | — | — | En curso | No acreditado |
| 321 | — | 512 | — | — | En curso | No acreditado |
| 322 | — | 512 | — | — | En curso | No acreditado |
| 323 | — | 512 | — | — | En curso | No acreditado |
| 324 | — | 512 | — | — | En curso | No acreditado |
| 325 | — | 512 | — | — | En curso | No acreditado |
| 326 | — | 512 | — | — | En curso | No acreditado |
| 327 | — | 512 | — | — | En curso | No acreditado |
| 328 | — | 512 | — | — | En curso | No acreditado |
| 329 | — | 512 | — | — | En curso | No acreditado |
| 330 | — | 512 | — | — | En curso | No acreditado |
| 331 | — | 512 | — | — | En curso | No acreditado |
| 332 | — | 512 | — | — | En curso | No acreditado |
| 333 | — | 512 | — | — | En curso | No acreditado |
| 334 | — | 512 | — | — | En curso | No acreditado |
| 335 | — | 512 | — | — | En curso | No acreditado |
| 336 | — | 512 | — | — | En curso | No acreditado |
| 337 | — | 512 | — | — | En curso | No acreditado |
| 338 | — | 512 | — | — | En curso | No acreditado |
| 339 | — | 512 | — | — | En curso | No acreditado |
| 340 | — | 512 | — | — | En curso | No acreditado |
| 341 | — | 512 | — | — | En curso | No acreditado |
| 342 | — | 512 | — | — | En curso | No acreditado |
| 343 | — | 512 | — | — | En curso | No acreditado |
| 344 | — | 512 | — | — | En curso | No acreditado |
| 345 | — | 512 | — | — | En curso | No acreditado |
| 346 | — | 512 | — | — | En curso | No acreditado |
| 347 | — | 512 | — | — | En curso | No acreditado |
| 348 | — | 512 | — | — | En curso | No acreditado |
| 349 | — | 512 | — | — | En curso | No acreditado |
| 350 | — | 512 | — | — | En curso | No acreditado |
| 351 | — | 512 | — | — | En curso | No acreditado |
| 352 | — | 512 | — | — | En curso | No acreditado |
| 353 | — | 512 | — | — | En curso | No acreditado |
| 354 | — | 512 | — | — | En curso | No acreditado |
| 355 | — | 512 | — | — | En curso | No acreditado |
| 356 | — | 512 | — | — | En curso | No acreditado |
| 357 | — | 512 | — | — | En curso | No acreditado |
| 358 | — | 512 | — | — | En curso | No acreditado |
| 359 | — | 512 | — | — | En curso | No acreditado |
| 360 | — | 512 | — | — | En curso | No acreditado |
| 361 | — | 512 | — | — | En curso | No acreditado |
| 362 | — | 512 | — | — | En curso | No acreditado |
| 363 | — | 512 | — | — | En curso | No acreditado |
| 364 | — | 512 | — | — | En curso | No acreditado |
| 365 | — | 512 | — | — | En curso | No acreditado |
| 366 | — | 512 | — | — | En curso | No acreditado |
| 367 | — | 512 | — | — | En curso | No acreditado |
| 368 | — | 512 | — | — | En curso | No acreditado |
| 369 | — | 512 | — | — | En curso | No acreditado |
| 370 | — | 512 | — | — | En curso | No acreditado |
| 371 | — | 512 | — | — | En curso | No acreditado |
| 372 | — | 512 | — | — | En curso | No acreditado |
| 373 | — | 512 | — | — | En curso | No acreditado |
| 374 | — | 512 | — | — | En curso | No acreditado |
| 375 | — | 512 | — | — | En curso | No acreditado |
| 376 | — | 512 | — | — | En curso | No acreditado |
| 377 | — | 512 | — | — | En curso | No acreditado |
| 378 | — | 512 | — | — | En curso | No acreditado |
| 379 | — | 512 | — | — | En curso | No acreditado |
| 380 | — | 512 | — | — | En curso | No acreditado |
| 381 | — | 512 | — | — | En curso | No acreditado |
| 382 | — | 512 | — | — | En curso | No acreditado |
| 383 | — | 512 | — | — | En curso | No acreditado |
| 384 | — | 512 | — | — | En curso | No acreditado |
| 385 | — | 512 | — | — | En curso | No acreditado |
| 386 | — | 512 | — | — | En curso | No acreditado |
| 387 | — | 512 | — | — | En curso | No acreditado |
| 388 | — | 512 | — | — | En curso | No acreditado |
| 389 | — | 512 | — | — | En curso | No acreditado |
| 390 | — | 512 | — | — | En curso | No acreditado |
| 391 | — | 512 | — | — | En curso | No acreditado |
| 392 | — | 512 | — | — | En curso | No acreditado |
| 393 | — | 512 | — | — | En curso | No acreditado |
| 394 | — | 512 | — | — | En curso | No acreditado |
| 395 | — | 512 | — | — | En curso | No acreditado |
| 396 | — | 512 | — | — | En curso | No acreditado |
| 397 | — | 512 | — | — | En curso | No acreditado |
| 398 | — | 512 | — | — | En curso | No acreditado |
| 399 | — | 512 | — | — | En curso | No acreditado |
| 400 | — | 512 | — | — | En curso | No acreditado |
| 401 | — | 512 | — | — | En curso | No acreditado |
| 402 | — | 512 | — | — | En curso | No acreditado |
| 403 | — | 512 | — | — | En curso | No acreditado |
| 404 | — | 512 | — | — | En curso | No acreditado |
| 405 | — | 512 | — | — | En curso | No acreditado |
| 406 | — | 512 | — | — | En curso | No acreditado |
| 407 | — | 512 | — | — | En curso | No acreditado |
| 408 | — | 512 | — | — | En curso | No acreditado |
| 409 | — | 512 | — | — | En curso | No acreditado |
| 410 | — | 512 | — | — | En curso | No acreditado |
| 411 | — | 512 | — | — | En curso | No acreditado |
| 412 | — | 512 | — | — | En curso | No acreditado |
| 413 | — | 512 | — | — | En curso | No acreditado |
| 414 | — | 512 | — | — | En curso | No acreditado |
| 415 | — | 512 | — | — | En curso | No acreditado |
| 416 | — | 512 | — | — | En curso | No acreditado |
| 417 | — | 512 | — | — | En curso | No acreditado |
| 418 | — | 512 | — | — | En curso | No acreditado |
| 419 | — | 512 | — | — | En curso | No acreditado |
| 420 | — | 512 | — | — | En curso | No acreditado |
| 421 | — | 512 | — | — | En curso | No acreditado |
| 422 | — | 512 | — | — | En curso | No acreditado |
| 423 | — | 512 | — | — | En curso | No acreditado |
| 424 | — | 512 | — | — | En curso | No acreditado |
| 425 | — | 512 | — | — | En curso | No acreditado |
| 426 | — | 512 | — | — | En curso | No acreditado |
| 427 | — | 512 | — | — | En curso | No acreditado |
| 428 | — | 512 | — | — | En curso | No acreditado |
| 429 | — | 512 | — | — | En curso | No acreditado |
| 430 | — | 512 | — | — | En curso | No acreditado |
| 431 | — | 512 | — | — | En curso | No acreditado |
| 432 | — | 512 | — | — | En curso | No acreditado |
| 433 | — | 512 | — | — | En curso | No acreditado |
| 434 | — | 512 | — | — | En curso | No acreditado |
| 435 | — | 512 | — | — | En curso | No acreditado |
| 436 | — | 512 | — | — | En curso | No acreditado |
| 437 | — | 512 | — | — | En curso | No acreditado |
| 438 | — | 512 | — | — | En curso | No acreditado |
| 439 | — | 512 | — | — | En curso | No acreditado |
| 440 | — | 512 | — | — | En curso | No acreditado |
| 441 | — | 512 | — | — | En curso | No acreditado |
| 442 | — | 512 | — | — | En curso | No acreditado |
| 443 | — | 512 | — | — | En curso | No acreditado |
| 444 | — | 512 | — | — | En curso | No acreditado |
| 445 | — | 512 | — | — | En curso | No acreditado |
| 446 | — | 512 | — | — | En curso | No acreditado |
| 447 | — | 512 | — | — | En curso | No acreditado |
| 448 | — | 512 | — | — | En curso | No acreditado |
| 449 | — | 512 | — | — | En curso | No acreditado |
| 450 | — | 512 | — | — | En curso | No acreditado |
| 451 | — | 512 | — | — | En curso | No acreditado |
| 452 | — | 512 | — | — | En curso | No acreditado |
| 453 | — | 512 | — | — | En curso | No acreditado |
| 454 | — | 512 | — | — | En curso | No acreditado |
| 455 | — | 512 | — | — | En curso | No acreditado |
| 456 | — | 512 | — | — | En curso | No acreditado |
| 457 | — | 512 | — | — | En curso | No acreditado |
| 458 | — | 512 | — | — | En curso | No acreditado |
| 459 | — | 512 | — | — | En curso | No acreditado |
| 460 | — | 512 | — | — | En curso | No acreditado |
| 461 | — | 512 | — | — | En curso | No acreditado |
| 462 | — | 512 | — | — | En curso | No acreditado |
| 463 | — | 512 | — | — | En curso | No acreditado |
| 464 | — | 512 | — | — | En curso | No acreditado |
| 465 | — | 512 | — | — | En curso | No acreditado |
| 466 | — | 512 | — | — | En curso | No acreditado |
| 467 | — | 512 | — | — | En curso | No acreditado |
| 468 | — | 512 | — | — | En curso | No acreditado |
| 469 | — | 512 | — | — | En curso | No acreditado |
| 470 | — | 512 | — | — | En curso | No acreditado |
| 471 | — | 512 | — | — | En curso | No acreditado |
| 472 | — | 512 | — | — | En curso | No acreditado |
| 473 | — | 512 | — | — | En curso | No acreditado |
| 474 | — | 512 | — | — | En curso | No acreditado |
| 475 | — | 512 | — | — | En curso | No acreditado |
| 476 | — | 512 | — | — | En curso | No acreditado |
| 477 | — | 512 | — | — | En curso | No acreditado |
| 478 | — | 512 | — | — | En curso | No acreditado |
| 479 | — | 512 | — | — | En curso | No acreditado |
| 480 | — | 512 | — | — | En curso | No acreditado |
| 481 | — | 512 | — | — | En curso | No acreditado |
| 482 | — | 512 | — | — | En curso | No acreditado |
| 483 | — | 512 | — | — | En curso | No acreditado |
| 484 | — | 512 | — | — | En curso | No acreditado |
| 485 | — | 512 | — | — | En curso | No acreditado |
| 486 | — | 512 | — | — | En curso | No acreditado |
| 487 | — | 512 | — | — | En curso | No acreditado |
| 488 | — | 512 | — | — | En curso | No acreditado |
| 489 | — | 512 | — | — | En curso | No acreditado |
| 490 | — | 512 | — | — | En curso | No acreditado |
| 491 | — | 512 | — | — | En curso | No acreditado |
| 492 | — | 512 | — | — | En curso | No acreditado |
| 493 | — | 512 | — | — | En curso | No acreditado |
| 494 | — | 512 | — | — | En curso | No acreditado |
| 495 | — | 512 | — | — | En curso | No acreditado |
| 496 | — | 512 | — | — | En curso | No acreditado |
| 497 | — | 512 | — | — | En curso | No acreditado |
| 498 | — | 512 | — | — | En curso | No acreditado |
| 499 | — | 512 | — | — | En curso | No acreditado |
| 500 | — | 512 | — | — | En curso | No acreditado |
| 501 | — | 512 | — | — | En curso | No acreditado |
| 502 | — | 512 | — | — | En curso | No acreditado |
| 503 | — | 512 | — | — | En curso | No acreditado |
| 504 | — | 512 | — | — | En curso | No acreditado |
| 505 | — | 512 | — | — | En curso | No acreditado |
| 506 | — | 512 | — | — | En curso | No acreditado |
| 507 | — | 512 | — | — | En curso | No acreditado |
| 508 | — | 512 | — | — | En curso | No acreditado |
| 509 | — | 512 | — | — | En curso | No acreditado |
| 510 | — | 512 | — | — | En curso | No acreditado |
| 511 | — | 512 | — | — | En curso | No acreditado |
| 512 | — | 512 | — | — | En curso | No acreditado |

</details>

<details>
<summary>Ver tiempos y velocidad de las 512 conversaciones</summary>


## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 1,47 | 526,12 | 0,97 | 0,97 |
| 2 | 2,07 | 527,95 | 0,97 | 0,97 |
| 3 | 2,07 | 527,95 | 0,97 | 0,97 |
| 4 | 3,92 | 533,31 | 0,97 | 0,96 |
| 5 | 2,69 | 529,81 | 0,97 | 0,97 |
| 6 | 3,28 | 531,49 | 0,97 | 0,96 |
| 7 | 3,28 | 531,49 | 0,97 | 0,96 |
| 8 | 4,51 | 535,14 | 0,96 | 0,96 |
| 9 | 4,51 | 535,13 | 0,96 | 0,96 |
| 10 | 6,41 | 540,61 | 0,96 | 0,95 |
| 11 | 5,76 | 538,79 | 0,96 | 0,95 |
| 12 | 5,15 | 536,96 | 0,96 | 0,95 |
| 13 | 7,02 | 542,43 | 0,95 | 0,94 |
| 14 | 5,76 | 538,79 | 0,96 | 0,95 |
| 15 | 7,02 | 542,43 | 0,95 | 0,94 |
| 16 | 8,30 | 546,06 | 0,95 | 0,94 |
| 17 | 7,67 | 544,24 | 0,95 | 0,94 |
| 18 | 8,99 | 547,87 | 0,95 | 0,93 |
| 19 | 8,29 | 546,06 | 0,95 | 0,94 |
| 20 | 9,64 | 549,69 | 0,95 | 0,93 |
| 21 | 9,64 | 549,69 | 0,95 | 0,93 |
| 22 | 10,34 | 551,49 | 0,94 | 0,93 |
| 23 | 11,01 | 553,32 | 0,94 | 0,93 |
| 24 | 12,41 | 556,99 | 0,94 | 0,92 |
| 25 | 13,13 | 558,89 | 0,94 | 0,92 |
| 26 | 11,01 | 553,29 | 0,94 | 0,93 |
| 27 | 15,28 | 564,27 | 0,93 | 0,91 |
| 28 | 15,28 | 564,27 | 0,93 | 0,91 |
| 29 | 16,03 | 566,06 | 0,93 | 0,90 |
| 30 | 14,57 | 562,47 | 0,93 | 0,91 |
| 31 | 12,40 | 556,99 | 0,94 | 0,92 |
| 32 | 13,82 | 560,71 | 0,93 | 0,91 |
| 33 | 13,82 | 560,68 | 0,93 | 0,91 |
| 34 | 11,72 | 555,19 | 0,94 | 0,92 |
| 35 | 16,75 | 567,83 | 0,93 | 0,90 |
| 36 | 16,75 | 567,84 | 0,93 | 0,90 |
| 37 | 17,52 | 569,63 | 0,93 | 0,90 |
| 38 | 18,25 | 571,40 | 0,92 | 0,90 |
| 39 | 18,25 | 571,43 | 0,92 | 0,90 |
| 40 | 19,01 | 573,18 | 0,92 | 0,89 |
| 41 | 19,76 | 574,96 | 0,92 | 0,89 |
| 42 | 19,76 | 574,96 | 0,92 | 0,89 |
| 43 | 21,97 | 578,74 | 0,92 | 0,88 |
| 44 | 22,80 | 580,52 | 0,92 | 0,88 |
| 45 | 20,55 | 576,84 | 0,92 | 0,89 |
| 46 | 23,57 | 582,29 | 0,91 | 0,88 |
| 47 | 21,97 | 578,76 | 0,92 | 0,88 |
| 48 | 26,06 | 587,58 | 0,91 | 0,87 |
| 49 | 23,56 | 582,28 | 0,91 | 0,88 |
| 50 | 26,87 | 589,33 | 0,91 | 0,87 |
| 51 | 25,14 | 585,81 | 0,91 | 0,87 |
| 52 | 24,36 | 584,04 | 0,91 | 0,88 |
| 53 | 26,86 | 589,32 | 0,91 | 0,87 |
| 54 | 30,13 | 596,33 | 0,90 | 0,86 |
| 55 | 27,69 | 591,08 | 0,91 | 0,87 |
| 56 | 28,49 | 592,83 | 0,91 | 0,86 |
| 57 | 25,13 | 585,81 | 0,91 | 0,87 |
| 58 | 30,13 | 596,33 | 0,90 | 0,86 |
| 59 | 29,32 | 594,58 | 0,90 | 0,86 |
| 60 | 30,98 | 598,08 | 0,90 | 0,86 |
| 61 | 28,49 | 592,83 | 0,91 | 0,86 |

</details>


## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 92% |
| Pico medido del motor / memoria del GB10 | 89,4% |
| Pico usado por todo el sistema / memoria del GB10 | 98,8% |
| Conversaciones totales | 512 |
| Máximo de peticiones enviadas a la vez | 512 |
| Límite de solicitudes del servidor | 512 |
| Máximo activo en el motor | 347 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 15,2 s |
| Tiempo medio de respuesta completa | 562,3 s |
| Mayor espera hasta primer texto, entre las completadas | 31,0 s |
| Mayor tiempo completo, entre las completadas | 598,1 s |
| Suma de los tiempos individuales | 34.301,3 s |
| Tiempo total de la prueba | 598,2 s |
| Tokens/s medios por conversación, incluyendo espera | 0,91 |
| Tokens/s totales del grupo | 52,21 |
| Pico de caché ocupada | 99,9% |
| Máximo de solicitudes en cola | 508 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 596,6 s |
| Tiempo observado con caché al 95% o más | 285,5 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 75,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias, los máximos de tiempo y las velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Cronología: cuándo se envió, empezó y terminó cada respuesta</summary>

Segundos desde el inicio de la prueba.

| Conversación | Enviada | Primer texto | Final |
|---|---:|---:|---:|
| 1 | 0,07 | 1,55 | 526,20 |
| 2 | 0,08 | 2,15 | 528,02 |
| 3 | 0,08 | 2,15 | 528,02 |
| 4 | 0,08 | 3,99 | 533,39 |
| 5 | 0,08 | 2,77 | 529,89 |
| 6 | 0,08 | 3,36 | 531,57 |
| 7 | 0,08 | 3,36 | 531,57 |
| 8 | 0,08 | 4,60 | 535,22 |
| 9 | 0,08 | 4,59 | 535,22 |
| 10 | 0,08 | 6,49 | 540,70 |
| 11 | 0,08 | 5,84 | 538,87 |
| 12 | 0,09 | 5,24 | 537,05 |
| 13 | 0,09 | 7,10 | 542,52 |
| 14 | 0,09 | 5,84 | 538,87 |
| 15 | 0,09 | 7,10 | 542,52 |
| 16 | 0,09 | 8,39 | 546,15 |
| 17 | 0,09 | 7,76 | 544,33 |
| 18 | 0,09 | 9,08 | 547,96 |
| 19 | 0,09 | 8,38 | 546,15 |
| 20 | 0,09 | 9,74 | 549,78 |
| 21 | 0,09 | 9,74 | 549,78 |
| 22 | 0,09 | 10,43 | 551,59 |
| 23 | 0,09 | 11,11 | 553,41 |
| 24 | 0,09 | 12,50 | 557,08 |
| 25 | 0,09 | 13,23 | 558,98 |
| 26 | 0,09 | 11,11 | 553,39 |
| 27 | 0,10 | 15,37 | 564,37 |
| 28 | 0,10 | 15,38 | 564,37 |
| 29 | 0,10 | 16,13 | 566,15 |
| 30 | 0,10 | 14,67 | 562,57 |
| 31 | 0,10 | 12,50 | 557,09 |
| 32 | 0,10 | 13,92 | 560,81 |
| 33 | 0,10 | 13,92 | 560,78 |
| 34 | 0,10 | 11,82 | 555,29 |
| 35 | 0,10 | 16,85 | 567,93 |
| 36 | 0,10 | 16,85 | 567,94 |
| 37 | 0,10 | 17,62 | 569,73 |
| 38 | 0,10 | 18,35 | 571,51 |
| 39 | 0,11 | 18,35 | 571,54 |
| 40 | 0,11 | 19,12 | 573,29 |
| 41 | 0,11 | 19,87 | 575,07 |
| 42 | 0,11 | 19,87 | 575,07 |
| 43 | 0,11 | 22,08 | 578,85 |
| 44 | 0,11 | 22,91 | 580,63 |
| 45 | 0,11 | 20,66 | 576,95 |
| 46 | 0,11 | 23,68 | 582,40 |
| 47 | 0,11 | 22,08 | 578,87 |
| 48 | 0,11 | 26,17 | 587,69 |
| 49 | 0,11 | 23,68 | 582,39 |
| 50 | 0,11 | 26,98 | 589,44 |
| 51 | 0,11 | 25,25 | 585,92 |
| 52 | 0,11 | 24,48 | 584,16 |
| 53 | 0,11 | 26,98 | 589,44 |
| 54 | 0,12 | 30,25 | 596,45 |
| 55 | 0,12 | 27,81 | 591,20 |
| 56 | 0,12 | 28,60 | 592,94 |
| 57 | 0,12 | 25,25 | 585,92 |
| 58 | 0,12 | 30,25 | 596,45 |
| 59 | 0,12 | 29,44 | 594,70 |
| 60 | 0,12 | 31,10 | 598,20 |
| 61 | 0,12 | 28,61 | 592,94 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
