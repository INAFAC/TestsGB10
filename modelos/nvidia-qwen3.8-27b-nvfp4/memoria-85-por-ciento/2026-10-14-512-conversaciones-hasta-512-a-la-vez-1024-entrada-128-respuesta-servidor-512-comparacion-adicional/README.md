# 512 conversaciones, hasta 512 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 85% del GB10.

**Límite impuesto al servidor: 512 solicitudes activas** (`--max-num-seqs 512`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 6/512 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 194 activas en el motor; cola máxima 506.
- **Tiempo para completar la prueba:** 131,2 s.

Se enviaron **512 conversaciones**, hasta **512 a la vez**. Cada una pidió **1.024 tokens de entrada + 128 de respuesta = 1.152 tokens**.

<details>
<summary>Ver tokens y finalización de las 512 conversaciones</summary>

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 2 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 3 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 4 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 5 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 6 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 7 | — | 128 | — | — | En curso | No acreditado |
| 8 | — | 128 | — | — | En curso | No acreditado |
| 9 | — | 128 | — | — | En curso | No acreditado |
| 10 | — | 128 | — | — | En curso | No acreditado |
| 11 | — | 128 | — | — | En curso | No acreditado |
| 12 | — | 128 | — | — | En curso | No acreditado |
| 13 | — | 128 | — | — | En curso | No acreditado |
| 14 | — | 128 | — | — | En curso | No acreditado |
| 15 | — | 128 | — | — | En curso | No acreditado |
| 16 | — | 128 | — | — | En curso | No acreditado |
| 17 | — | 128 | — | — | En curso | No acreditado |
| 18 | — | 128 | — | — | En curso | No acreditado |
| 19 | — | 128 | — | — | En curso | No acreditado |
| 20 | — | 128 | — | — | En curso | No acreditado |
| 21 | — | 128 | — | — | En curso | No acreditado |
| 22 | — | 128 | — | — | En curso | No acreditado |
| 23 | — | 128 | — | — | En curso | No acreditado |
| 24 | — | 128 | — | — | En curso | No acreditado |
| 25 | — | 128 | — | — | En curso | No acreditado |
| 26 | — | 128 | — | — | En curso | No acreditado |
| 27 | — | 128 | — | — | En curso | No acreditado |
| 28 | — | 128 | — | — | En curso | No acreditado |
| 29 | — | 128 | — | — | En curso | No acreditado |
| 30 | — | 128 | — | — | En curso | No acreditado |
| 31 | — | 128 | — | — | En curso | No acreditado |
| 32 | — | 128 | — | — | En curso | No acreditado |
| 33 | — | 128 | — | — | En curso | No acreditado |
| 34 | — | 128 | — | — | En curso | No acreditado |
| 35 | — | 128 | — | — | En curso | No acreditado |
| 36 | — | 128 | — | — | En curso | No acreditado |
| 37 | — | 128 | — | — | En curso | No acreditado |
| 38 | — | 128 | — | — | En curso | No acreditado |
| 39 | — | 128 | — | — | En curso | No acreditado |
| 40 | — | 128 | — | — | En curso | No acreditado |
| 41 | — | 128 | — | — | En curso | No acreditado |
| 42 | — | 128 | — | — | En curso | No acreditado |
| 43 | — | 128 | — | — | En curso | No acreditado |
| 44 | — | 128 | — | — | En curso | No acreditado |
| 45 | — | 128 | — | — | En curso | No acreditado |
| 46 | — | 128 | — | — | En curso | No acreditado |
| 47 | — | 128 | — | — | En curso | No acreditado |
| 48 | — | 128 | — | — | En curso | No acreditado |
| 49 | — | 128 | — | — | En curso | No acreditado |
| 50 | — | 128 | — | — | En curso | No acreditado |
| 51 | — | 128 | — | — | En curso | No acreditado |
| 52 | — | 128 | — | — | En curso | No acreditado |
| 53 | — | 128 | — | — | En curso | No acreditado |
| 54 | — | 128 | — | — | En curso | No acreditado |
| 55 | — | 128 | — | — | En curso | No acreditado |
| 56 | — | 128 | — | — | En curso | No acreditado |
| 57 | — | 128 | — | — | En curso | No acreditado |
| 58 | — | 128 | — | — | En curso | No acreditado |
| 59 | — | 128 | — | — | En curso | No acreditado |
| 60 | — | 128 | — | — | En curso | No acreditado |
| 61 | — | 128 | — | — | En curso | No acreditado |
| 62 | — | 128 | — | — | En curso | No acreditado |
| 63 | — | 128 | — | — | En curso | No acreditado |
| 64 | — | 128 | — | — | En curso | No acreditado |
| 65 | — | 128 | — | — | En curso | No acreditado |
| 66 | — | 128 | — | — | En curso | No acreditado |
| 67 | — | 128 | — | — | En curso | No acreditado |
| 68 | — | 128 | — | — | En curso | No acreditado |
| 69 | — | 128 | — | — | En curso | No acreditado |
| 70 | — | 128 | — | — | En curso | No acreditado |
| 71 | — | 128 | — | — | En curso | No acreditado |
| 72 | — | 128 | — | — | En curso | No acreditado |
| 73 | — | 128 | — | — | En curso | No acreditado |
| 74 | — | 128 | — | — | En curso | No acreditado |
| 75 | — | 128 | — | — | En curso | No acreditado |
| 76 | — | 128 | — | — | En curso | No acreditado |
| 77 | — | 128 | — | — | En curso | No acreditado |
| 78 | — | 128 | — | — | En curso | No acreditado |
| 79 | — | 128 | — | — | En curso | No acreditado |
| 80 | — | 128 | — | — | En curso | No acreditado |
| 81 | — | 128 | — | — | En curso | No acreditado |
| 82 | — | 128 | — | — | En curso | No acreditado |
| 83 | — | 128 | — | — | En curso | No acreditado |
| 84 | — | 128 | — | — | En curso | No acreditado |
| 85 | — | 128 | — | — | En curso | No acreditado |
| 86 | — | 128 | — | — | En curso | No acreditado |
| 87 | — | 128 | — | — | En curso | No acreditado |
| 88 | — | 128 | — | — | En curso | No acreditado |
| 89 | — | 128 | — | — | En curso | No acreditado |
| 90 | — | 128 | — | — | En curso | No acreditado |
| 91 | — | 128 | — | — | En curso | No acreditado |
| 92 | — | 128 | — | — | En curso | No acreditado |
| 93 | — | 128 | — | — | En curso | No acreditado |
| 94 | — | 128 | — | — | En curso | No acreditado |
| 95 | — | 128 | — | — | En curso | No acreditado |
| 96 | — | 128 | — | — | En curso | No acreditado |
| 97 | — | 128 | — | — | En curso | No acreditado |
| 98 | — | 128 | — | — | En curso | No acreditado |
| 99 | — | 128 | — | — | En curso | No acreditado |
| 100 | — | 128 | — | — | En curso | No acreditado |
| 101 | — | 128 | — | — | En curso | No acreditado |
| 102 | — | 128 | — | — | En curso | No acreditado |
| 103 | — | 128 | — | — | En curso | No acreditado |
| 104 | — | 128 | — | — | En curso | No acreditado |
| 105 | — | 128 | — | — | En curso | No acreditado |
| 106 | — | 128 | — | — | En curso | No acreditado |
| 107 | — | 128 | — | — | En curso | No acreditado |
| 108 | — | 128 | — | — | En curso | No acreditado |
| 109 | — | 128 | — | — | En curso | No acreditado |
| 110 | — | 128 | — | — | En curso | No acreditado |
| 111 | — | 128 | — | — | En curso | No acreditado |
| 112 | — | 128 | — | — | En curso | No acreditado |
| 113 | — | 128 | — | — | En curso | No acreditado |
| 114 | — | 128 | — | — | En curso | No acreditado |
| 115 | — | 128 | — | — | En curso | No acreditado |
| 116 | — | 128 | — | — | En curso | No acreditado |
| 117 | — | 128 | — | — | En curso | No acreditado |
| 118 | — | 128 | — | — | En curso | No acreditado |
| 119 | — | 128 | — | — | En curso | No acreditado |
| 120 | — | 128 | — | — | En curso | No acreditado |
| 121 | — | 128 | — | — | En curso | No acreditado |
| 122 | — | 128 | — | — | En curso | No acreditado |
| 123 | — | 128 | — | — | En curso | No acreditado |
| 124 | — | 128 | — | — | En curso | No acreditado |
| 125 | — | 128 | — | — | En curso | No acreditado |
| 126 | — | 128 | — | — | En curso | No acreditado |
| 127 | — | 128 | — | — | En curso | No acreditado |
| 128 | — | 128 | — | — | En curso | No acreditado |
| 129 | — | 128 | — | — | En curso | No acreditado |
| 130 | — | 128 | — | — | En curso | No acreditado |
| 131 | — | 128 | — | — | En curso | No acreditado |
| 132 | — | 128 | — | — | En curso | No acreditado |
| 133 | — | 128 | — | — | En curso | No acreditado |
| 134 | — | 128 | — | — | En curso | No acreditado |
| 135 | — | 128 | — | — | En curso | No acreditado |
| 136 | — | 128 | — | — | En curso | No acreditado |
| 137 | — | 128 | — | — | En curso | No acreditado |
| 138 | — | 128 | — | — | En curso | No acreditado |
| 139 | — | 128 | — | — | En curso | No acreditado |
| 140 | — | 128 | — | — | En curso | No acreditado |
| 141 | — | 128 | — | — | En curso | No acreditado |
| 142 | — | 128 | — | — | En curso | No acreditado |
| 143 | — | 128 | — | — | En curso | No acreditado |
| 144 | — | 128 | — | — | En curso | No acreditado |
| 145 | — | 128 | — | — | En curso | No acreditado |
| 146 | — | 128 | — | — | En curso | No acreditado |
| 147 | — | 128 | — | — | En curso | No acreditado |
| 148 | — | 128 | — | — | En curso | No acreditado |
| 149 | — | 128 | — | — | En curso | No acreditado |
| 150 | — | 128 | — | — | En curso | No acreditado |
| 151 | — | 128 | — | — | En curso | No acreditado |
| 152 | — | 128 | — | — | En curso | No acreditado |
| 153 | — | 128 | — | — | En curso | No acreditado |
| 154 | — | 128 | — | — | En curso | No acreditado |
| 155 | — | 128 | — | — | En curso | No acreditado |
| 156 | — | 128 | — | — | En curso | No acreditado |
| 157 | — | 128 | — | — | En curso | No acreditado |
| 158 | — | 128 | — | — | En curso | No acreditado |
| 159 | — | 128 | — | — | En curso | No acreditado |
| 160 | — | 128 | — | — | En curso | No acreditado |
| 161 | — | 128 | — | — | En curso | No acreditado |
| 162 | — | 128 | — | — | En curso | No acreditado |
| 163 | — | 128 | — | — | En curso | No acreditado |
| 164 | — | 128 | — | — | En curso | No acreditado |
| 165 | — | 128 | — | — | En curso | No acreditado |
| 166 | — | 128 | — | — | En curso | No acreditado |
| 167 | — | 128 | — | — | En curso | No acreditado |
| 168 | — | 128 | — | — | En curso | No acreditado |
| 169 | — | 128 | — | — | En curso | No acreditado |
| 170 | — | 128 | — | — | En curso | No acreditado |
| 171 | — | 128 | — | — | En curso | No acreditado |
| 172 | — | 128 | — | — | En curso | No acreditado |
| 173 | — | 128 | — | — | En curso | No acreditado |
| 174 | — | 128 | — | — | En curso | No acreditado |
| 175 | — | 128 | — | — | En curso | No acreditado |
| 176 | — | 128 | — | — | En curso | No acreditado |
| 177 | — | 128 | — | — | En curso | No acreditado |
| 178 | — | 128 | — | — | En curso | No acreditado |
| 179 | — | 128 | — | — | En curso | No acreditado |
| 180 | — | 128 | — | — | En curso | No acreditado |
| 181 | — | 128 | — | — | En curso | No acreditado |
| 182 | — | 128 | — | — | En curso | No acreditado |
| 183 | — | 128 | — | — | En curso | No acreditado |
| 184 | — | 128 | — | — | En curso | No acreditado |
| 185 | — | 128 | — | — | En curso | No acreditado |
| 186 | — | 128 | — | — | En curso | No acreditado |
| 187 | — | 128 | — | — | En curso | No acreditado |
| 188 | — | 128 | — | — | En curso | No acreditado |
| 189 | — | 128 | — | — | En curso | No acreditado |
| 190 | — | 128 | — | — | En curso | No acreditado |
| 191 | — | 128 | — | — | En curso | No acreditado |
| 192 | — | 128 | — | — | En curso | No acreditado |
| 193 | — | 128 | — | — | En curso | No acreditado |
| 194 | — | 128 | — | — | En curso | No acreditado |
| 195 | — | 128 | — | — | En curso | No acreditado |
| 196 | — | 128 | — | — | En curso | No acreditado |
| 197 | — | 128 | — | — | En curso | No acreditado |
| 198 | — | 128 | — | — | En curso | No acreditado |
| 199 | — | 128 | — | — | En curso | No acreditado |
| 200 | — | 128 | — | — | En curso | No acreditado |
| 201 | — | 128 | — | — | En curso | No acreditado |
| 202 | — | 128 | — | — | En curso | No acreditado |
| 203 | — | 128 | — | — | En curso | No acreditado |
| 204 | — | 128 | — | — | En curso | No acreditado |
| 205 | — | 128 | — | — | En curso | No acreditado |
| 206 | — | 128 | — | — | En curso | No acreditado |
| 207 | — | 128 | — | — | En curso | No acreditado |
| 208 | — | 128 | — | — | En curso | No acreditado |
| 209 | — | 128 | — | — | En curso | No acreditado |
| 210 | — | 128 | — | — | En curso | No acreditado |
| 211 | — | 128 | — | — | En curso | No acreditado |
| 212 | — | 128 | — | — | En curso | No acreditado |
| 213 | — | 128 | — | — | En curso | No acreditado |
| 214 | — | 128 | — | — | En curso | No acreditado |
| 215 | — | 128 | — | — | En curso | No acreditado |
| 216 | — | 128 | — | — | En curso | No acreditado |
| 217 | — | 128 | — | — | En curso | No acreditado |
| 218 | — | 128 | — | — | En curso | No acreditado |
| 219 | — | 128 | — | — | En curso | No acreditado |
| 220 | — | 128 | — | — | En curso | No acreditado |
| 221 | — | 128 | — | — | En curso | No acreditado |
| 222 | — | 128 | — | — | En curso | No acreditado |
| 223 | — | 128 | — | — | En curso | No acreditado |
| 224 | — | 128 | — | — | En curso | No acreditado |
| 225 | — | 128 | — | — | En curso | No acreditado |
| 226 | — | 128 | — | — | En curso | No acreditado |
| 227 | — | 128 | — | — | En curso | No acreditado |
| 228 | — | 128 | — | — | En curso | No acreditado |
| 229 | — | 128 | — | — | En curso | No acreditado |
| 230 | — | 128 | — | — | En curso | No acreditado |
| 231 | — | 128 | — | — | En curso | No acreditado |
| 232 | — | 128 | — | — | En curso | No acreditado |
| 233 | — | 128 | — | — | En curso | No acreditado |
| 234 | — | 128 | — | — | En curso | No acreditado |
| 235 | — | 128 | — | — | En curso | No acreditado |
| 236 | — | 128 | — | — | En curso | No acreditado |
| 237 | — | 128 | — | — | En curso | No acreditado |
| 238 | — | 128 | — | — | En curso | No acreditado |
| 239 | — | 128 | — | — | En curso | No acreditado |
| 240 | — | 128 | — | — | En curso | No acreditado |
| 241 | — | 128 | — | — | En curso | No acreditado |
| 242 | — | 128 | — | — | En curso | No acreditado |
| 243 | — | 128 | — | — | En curso | No acreditado |
| 244 | — | 128 | — | — | En curso | No acreditado |
| 245 | — | 128 | — | — | En curso | No acreditado |
| 246 | — | 128 | — | — | En curso | No acreditado |
| 247 | — | 128 | — | — | En curso | No acreditado |
| 248 | — | 128 | — | — | En curso | No acreditado |
| 249 | — | 128 | — | — | En curso | No acreditado |
| 250 | — | 128 | — | — | En curso | No acreditado |
| 251 | — | 128 | — | — | En curso | No acreditado |
| 252 | — | 128 | — | — | En curso | No acreditado |
| 253 | — | 128 | — | — | En curso | No acreditado |
| 254 | — | 128 | — | — | En curso | No acreditado |
| 255 | — | 128 | — | — | En curso | No acreditado |
| 256 | — | 128 | — | — | En curso | No acreditado |
| 257 | — | 128 | — | — | En curso | No acreditado |
| 258 | — | 128 | — | — | En curso | No acreditado |
| 259 | — | 128 | — | — | En curso | No acreditado |
| 260 | — | 128 | — | — | En curso | No acreditado |
| 261 | — | 128 | — | — | En curso | No acreditado |
| 262 | — | 128 | — | — | En curso | No acreditado |
| 263 | — | 128 | — | — | En curso | No acreditado |
| 264 | — | 128 | — | — | En curso | No acreditado |
| 265 | — | 128 | — | — | En curso | No acreditado |
| 266 | — | 128 | — | — | En curso | No acreditado |
| 267 | — | 128 | — | — | En curso | No acreditado |
| 268 | — | 128 | — | — | En curso | No acreditado |
| 269 | — | 128 | — | — | En curso | No acreditado |
| 270 | — | 128 | — | — | En curso | No acreditado |
| 271 | — | 128 | — | — | En curso | No acreditado |
| 272 | — | 128 | — | — | En curso | No acreditado |
| 273 | — | 128 | — | — | En curso | No acreditado |
| 274 | — | 128 | — | — | En curso | No acreditado |
| 275 | — | 128 | — | — | En curso | No acreditado |
| 276 | — | 128 | — | — | En curso | No acreditado |
| 277 | — | 128 | — | — | En curso | No acreditado |
| 278 | — | 128 | — | — | En curso | No acreditado |
| 279 | — | 128 | — | — | En curso | No acreditado |
| 280 | — | 128 | — | — | En curso | No acreditado |
| 281 | — | 128 | — | — | En curso | No acreditado |
| 282 | — | 128 | — | — | En curso | No acreditado |
| 283 | — | 128 | — | — | En curso | No acreditado |
| 284 | — | 128 | — | — | En curso | No acreditado |
| 285 | — | 128 | — | — | En curso | No acreditado |
| 286 | — | 128 | — | — | En curso | No acreditado |
| 287 | — | 128 | — | — | En curso | No acreditado |
| 288 | — | 128 | — | — | En curso | No acreditado |
| 289 | — | 128 | — | — | En curso | No acreditado |
| 290 | — | 128 | — | — | En curso | No acreditado |
| 291 | — | 128 | — | — | En curso | No acreditado |
| 292 | — | 128 | — | — | En curso | No acreditado |
| 293 | — | 128 | — | — | En curso | No acreditado |
| 294 | — | 128 | — | — | En curso | No acreditado |
| 295 | — | 128 | — | — | En curso | No acreditado |
| 296 | — | 128 | — | — | En curso | No acreditado |
| 297 | — | 128 | — | — | En curso | No acreditado |
| 298 | — | 128 | — | — | En curso | No acreditado |
| 299 | — | 128 | — | — | En curso | No acreditado |
| 300 | — | 128 | — | — | En curso | No acreditado |
| 301 | — | 128 | — | — | En curso | No acreditado |
| 302 | — | 128 | — | — | En curso | No acreditado |
| 303 | — | 128 | — | — | En curso | No acreditado |
| 304 | — | 128 | — | — | En curso | No acreditado |
| 305 | — | 128 | — | — | En curso | No acreditado |
| 306 | — | 128 | — | — | En curso | No acreditado |
| 307 | — | 128 | — | — | En curso | No acreditado |
| 308 | — | 128 | — | — | En curso | No acreditado |
| 309 | — | 128 | — | — | En curso | No acreditado |
| 310 | — | 128 | — | — | En curso | No acreditado |
| 311 | — | 128 | — | — | En curso | No acreditado |
| 312 | — | 128 | — | — | En curso | No acreditado |
| 313 | — | 128 | — | — | En curso | No acreditado |
| 314 | — | 128 | — | — | En curso | No acreditado |
| 315 | — | 128 | — | — | En curso | No acreditado |
| 316 | — | 128 | — | — | En curso | No acreditado |
| 317 | — | 128 | — | — | En curso | No acreditado |
| 318 | — | 128 | — | — | En curso | No acreditado |
| 319 | — | 128 | — | — | En curso | No acreditado |
| 320 | — | 128 | — | — | En curso | No acreditado |
| 321 | — | 128 | — | — | En curso | No acreditado |
| 322 | — | 128 | — | — | En curso | No acreditado |
| 323 | — | 128 | — | — | En curso | No acreditado |
| 324 | — | 128 | — | — | En curso | No acreditado |
| 325 | — | 128 | — | — | En curso | No acreditado |
| 326 | — | 128 | — | — | En curso | No acreditado |
| 327 | — | 128 | — | — | En curso | No acreditado |
| 328 | — | 128 | — | — | En curso | No acreditado |
| 329 | — | 128 | — | — | En curso | No acreditado |
| 330 | — | 128 | — | — | En curso | No acreditado |
| 331 | — | 128 | — | — | En curso | No acreditado |
| 332 | — | 128 | — | — | En curso | No acreditado |
| 333 | — | 128 | — | — | En curso | No acreditado |
| 334 | — | 128 | — | — | En curso | No acreditado |
| 335 | — | 128 | — | — | En curso | No acreditado |
| 336 | — | 128 | — | — | En curso | No acreditado |
| 337 | — | 128 | — | — | En curso | No acreditado |
| 338 | — | 128 | — | — | En curso | No acreditado |
| 339 | — | 128 | — | — | En curso | No acreditado |
| 340 | — | 128 | — | — | En curso | No acreditado |
| 341 | — | 128 | — | — | En curso | No acreditado |
| 342 | — | 128 | — | — | En curso | No acreditado |
| 343 | — | 128 | — | — | En curso | No acreditado |
| 344 | — | 128 | — | — | En curso | No acreditado |
| 345 | — | 128 | — | — | En curso | No acreditado |
| 346 | — | 128 | — | — | En curso | No acreditado |
| 347 | — | 128 | — | — | En curso | No acreditado |
| 348 | — | 128 | — | — | En curso | No acreditado |
| 349 | — | 128 | — | — | En curso | No acreditado |
| 350 | — | 128 | — | — | En curso | No acreditado |
| 351 | — | 128 | — | — | En curso | No acreditado |
| 352 | — | 128 | — | — | En curso | No acreditado |
| 353 | — | 128 | — | — | En curso | No acreditado |
| 354 | — | 128 | — | — | En curso | No acreditado |
| 355 | — | 128 | — | — | En curso | No acreditado |
| 356 | — | 128 | — | — | En curso | No acreditado |
| 357 | — | 128 | — | — | En curso | No acreditado |
| 358 | — | 128 | — | — | En curso | No acreditado |
| 359 | — | 128 | — | — | En curso | No acreditado |
| 360 | — | 128 | — | — | En curso | No acreditado |
| 361 | — | 128 | — | — | En curso | No acreditado |
| 362 | — | 128 | — | — | En curso | No acreditado |
| 363 | — | 128 | — | — | En curso | No acreditado |
| 364 | — | 128 | — | — | En curso | No acreditado |
| 365 | — | 128 | — | — | En curso | No acreditado |
| 366 | — | 128 | — | — | En curso | No acreditado |
| 367 | — | 128 | — | — | En curso | No acreditado |
| 368 | — | 128 | — | — | En curso | No acreditado |
| 369 | — | 128 | — | — | En curso | No acreditado |
| 370 | — | 128 | — | — | En curso | No acreditado |
| 371 | — | 128 | — | — | En curso | No acreditado |
| 372 | — | 128 | — | — | En curso | No acreditado |
| 373 | — | 128 | — | — | En curso | No acreditado |
| 374 | — | 128 | — | — | En curso | No acreditado |
| 375 | — | 128 | — | — | En curso | No acreditado |
| 376 | — | 128 | — | — | En curso | No acreditado |
| 377 | — | 128 | — | — | En curso | No acreditado |
| 378 | — | 128 | — | — | En curso | No acreditado |
| 379 | — | 128 | — | — | En curso | No acreditado |
| 380 | — | 128 | — | — | En curso | No acreditado |
| 381 | — | 128 | — | — | En curso | No acreditado |
| 382 | — | 128 | — | — | En curso | No acreditado |
| 383 | — | 128 | — | — | En curso | No acreditado |
| 384 | — | 128 | — | — | En curso | No acreditado |
| 385 | — | 128 | — | — | En curso | No acreditado |
| 386 | — | 128 | — | — | En curso | No acreditado |
| 387 | — | 128 | — | — | En curso | No acreditado |
| 388 | — | 128 | — | — | En curso | No acreditado |
| 389 | — | 128 | — | — | En curso | No acreditado |
| 390 | — | 128 | — | — | En curso | No acreditado |
| 391 | — | 128 | — | — | En curso | No acreditado |
| 392 | — | 128 | — | — | En curso | No acreditado |
| 393 | — | 128 | — | — | En curso | No acreditado |
| 394 | — | 128 | — | — | En curso | No acreditado |
| 395 | — | 128 | — | — | En curso | No acreditado |
| 396 | — | 128 | — | — | En curso | No acreditado |
| 397 | — | 128 | — | — | En curso | No acreditado |
| 398 | — | 128 | — | — | En curso | No acreditado |
| 399 | — | 128 | — | — | En curso | No acreditado |
| 400 | — | 128 | — | — | En curso | No acreditado |
| 401 | — | 128 | — | — | En curso | No acreditado |
| 402 | — | 128 | — | — | En curso | No acreditado |
| 403 | — | 128 | — | — | En curso | No acreditado |
| 404 | — | 128 | — | — | En curso | No acreditado |
| 405 | — | 128 | — | — | En curso | No acreditado |
| 406 | — | 128 | — | — | En curso | No acreditado |
| 407 | — | 128 | — | — | En curso | No acreditado |
| 408 | — | 128 | — | — | En curso | No acreditado |
| 409 | — | 128 | — | — | En curso | No acreditado |
| 410 | — | 128 | — | — | En curso | No acreditado |
| 411 | — | 128 | — | — | En curso | No acreditado |
| 412 | — | 128 | — | — | En curso | No acreditado |
| 413 | — | 128 | — | — | En curso | No acreditado |
| 414 | — | 128 | — | — | En curso | No acreditado |
| 415 | — | 128 | — | — | En curso | No acreditado |
| 416 | — | 128 | — | — | En curso | No acreditado |
| 417 | — | 128 | — | — | En curso | No acreditado |
| 418 | — | 128 | — | — | En curso | No acreditado |
| 419 | — | 128 | — | — | En curso | No acreditado |
| 420 | — | 128 | — | — | En curso | No acreditado |
| 421 | — | 128 | — | — | En curso | No acreditado |
| 422 | — | 128 | — | — | En curso | No acreditado |
| 423 | — | 128 | — | — | En curso | No acreditado |
| 424 | — | 128 | — | — | En curso | No acreditado |
| 425 | — | 128 | — | — | En curso | No acreditado |
| 426 | — | 128 | — | — | En curso | No acreditado |
| 427 | — | 128 | — | — | En curso | No acreditado |
| 428 | — | 128 | — | — | En curso | No acreditado |
| 429 | — | 128 | — | — | En curso | No acreditado |
| 430 | — | 128 | — | — | En curso | No acreditado |
| 431 | — | 128 | — | — | En curso | No acreditado |
| 432 | — | 128 | — | — | En curso | No acreditado |
| 433 | — | 128 | — | — | En curso | No acreditado |
| 434 | — | 128 | — | — | En curso | No acreditado |
| 435 | — | 128 | — | — | En curso | No acreditado |
| 436 | — | 128 | — | — | En curso | No acreditado |
| 437 | — | 128 | — | — | En curso | No acreditado |
| 438 | — | 128 | — | — | En curso | No acreditado |
| 439 | — | 128 | — | — | En curso | No acreditado |
| 440 | — | 128 | — | — | En curso | No acreditado |
| 441 | — | 128 | — | — | En curso | No acreditado |
| 442 | — | 128 | — | — | En curso | No acreditado |
| 443 | — | 128 | — | — | En curso | No acreditado |
| 444 | — | 128 | — | — | En curso | No acreditado |
| 445 | — | 128 | — | — | En curso | No acreditado |
| 446 | — | 128 | — | — | En curso | No acreditado |
| 447 | — | 128 | — | — | En curso | No acreditado |
| 448 | — | 128 | — | — | En curso | No acreditado |
| 449 | — | 128 | — | — | En curso | No acreditado |
| 450 | — | 128 | — | — | En curso | No acreditado |
| 451 | — | 128 | — | — | En curso | No acreditado |
| 452 | — | 128 | — | — | En curso | No acreditado |
| 453 | — | 128 | — | — | En curso | No acreditado |
| 454 | — | 128 | — | — | En curso | No acreditado |
| 455 | — | 128 | — | — | En curso | No acreditado |
| 456 | — | 128 | — | — | En curso | No acreditado |
| 457 | — | 128 | — | — | En curso | No acreditado |
| 458 | — | 128 | — | — | En curso | No acreditado |
| 459 | — | 128 | — | — | En curso | No acreditado |
| 460 | — | 128 | — | — | En curso | No acreditado |
| 461 | — | 128 | — | — | En curso | No acreditado |
| 462 | — | 128 | — | — | En curso | No acreditado |
| 463 | — | 128 | — | — | En curso | No acreditado |
| 464 | — | 128 | — | — | En curso | No acreditado |
| 465 | — | 128 | — | — | En curso | No acreditado |
| 466 | — | 128 | — | — | En curso | No acreditado |
| 467 | — | 128 | — | — | En curso | No acreditado |
| 468 | — | 128 | — | — | En curso | No acreditado |
| 469 | — | 128 | — | — | En curso | No acreditado |
| 470 | — | 128 | — | — | En curso | No acreditado |
| 471 | — | 128 | — | — | En curso | No acreditado |
| 472 | — | 128 | — | — | En curso | No acreditado |
| 473 | — | 128 | — | — | En curso | No acreditado |
| 474 | — | 128 | — | — | En curso | No acreditado |
| 475 | — | 128 | — | — | En curso | No acreditado |
| 476 | — | 128 | — | — | En curso | No acreditado |
| 477 | — | 128 | — | — | En curso | No acreditado |
| 478 | — | 128 | — | — | En curso | No acreditado |
| 479 | — | 128 | — | — | En curso | No acreditado |
| 480 | — | 128 | — | — | En curso | No acreditado |
| 481 | — | 128 | — | — | En curso | No acreditado |
| 482 | — | 128 | — | — | En curso | No acreditado |
| 483 | — | 128 | — | — | En curso | No acreditado |
| 484 | — | 128 | — | — | En curso | No acreditado |
| 485 | — | 128 | — | — | En curso | No acreditado |
| 486 | — | 128 | — | — | En curso | No acreditado |
| 487 | — | 128 | — | — | En curso | No acreditado |
| 488 | — | 128 | — | — | En curso | No acreditado |
| 489 | — | 128 | — | — | En curso | No acreditado |
| 490 | — | 128 | — | — | En curso | No acreditado |
| 491 | — | 128 | — | — | En curso | No acreditado |
| 492 | — | 128 | — | — | En curso | No acreditado |
| 493 | — | 128 | — | — | En curso | No acreditado |
| 494 | — | 128 | — | — | En curso | No acreditado |
| 495 | — | 128 | — | — | En curso | No acreditado |
| 496 | — | 128 | — | — | En curso | No acreditado |
| 497 | — | 128 | — | — | En curso | No acreditado |
| 498 | — | 128 | — | — | En curso | No acreditado |
| 499 | — | 128 | — | — | En curso | No acreditado |
| 500 | — | 128 | — | — | En curso | No acreditado |
| 501 | — | 128 | — | — | En curso | No acreditado |
| 502 | — | 128 | — | — | En curso | No acreditado |
| 503 | — | 128 | — | — | En curso | No acreditado |
| 504 | — | 128 | — | — | En curso | No acreditado |
| 505 | — | 128 | — | — | En curso | No acreditado |
| 506 | — | 128 | — | — | En curso | No acreditado |
| 507 | — | 128 | — | — | En curso | No acreditado |
| 508 | — | 128 | — | — | En curso | No acreditado |
| 509 | — | 128 | — | — | En curso | No acreditado |
| 510 | — | 128 | — | — | En curso | No acreditado |
| 511 | — | 128 | — | — | En curso | No acreditado |
| 512 | — | 128 | — | — | En curso | No acreditado |

</details>

<details>
<summary>Ver tiempos y velocidad de las 512 conversaciones</summary>


## Cada conversación: tiempos y velocidad

| Conversación | Espera hasta primer texto (s) | Tiempo completo (s) | Tokens/s durante la respuesta | Tokens/s incluyendo la espera |
|---|---:|---:|---:|---:|
| 1 | 1,34 | 127,16 | 1,01 | 1,01 |
| 2 | 1,95 | 128,48 | 1,00 | 1,00 |
| 3 | 1,95 | 128,48 | 1,00 | 1,00 |
| 4 | 3,17 | 131,15 | 0,99 | 0,98 |
| 5 | 3,17 | 131,14 | 0,99 | 0,98 |
| 6 | 2,56 | 129,80 | 1,00 | 0,99 |

</details>


## Todas las medidas del grupo

| Medida | Resultado |
|---|---|
| Memoria asignada al motor | 85% |
| Pico medido del motor / memoria del GB10 | 81,6% |
| Pico usado por todo el sistema / memoria del GB10 | 92,0% |
| Conversaciones totales | 512 |
| Máximo de peticiones enviadas a la vez | 512 |
| Límite de solicitudes del servidor | 512 |
| Máximo activo en el motor | 194 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 2,4 s |
| Tiempo medio de respuesta completa | 129,4 s |
| Mayor espera hasta primer texto, entre las completadas | 3,2 s |
| Mayor tiempo completo, entre las completadas | 131,1 s |
| Suma de los tiempos individuales | 776,2 s |
| Tiempo total de la prueba | 131,2 s |
| Tokens/s medios por conversación, incluyendo espera | 0,99 |
| Tokens/s totales del grupo | 5,85 |
| Pico de caché ocupada | 63,1% |
| Máximo de solicitudes en cola | 506 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 129,2 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 70,0 °C |
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
| 1 | 0,10 | 1,44 | 127,26 |
| 2 | 0,10 | 2,04 | 128,58 |
| 3 | 0,10 | 2,04 | 128,58 |
| 4 | 0,10 | 3,27 | 131,25 |
| 5 | 0,10 | 3,26 | 131,24 |
| 6 | 0,10 | 2,66 | 129,89 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
