# 512 conversaciones, hasta 512 a la vez; 1.024 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 85% del GB10.

**Límite impuesto al servidor: 512 solicitudes activas** (`--max-num-seqs 512`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 0/512 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 61 activas en el motor; cola máxima 507.
- **Tiempo para completar la prueba:** 30,6 s.

Se enviaron **512 conversaciones**, hasta **512 a la vez**. Cada una pidió **1.024 tokens de entrada + 512 de respuesta = 1.536 tokens**.

<details>
<summary>Ver tokens y finalización de las 512 conversaciones</summary>

## Cada conversación: tokens y finalización

| Conversación | Entrada | Respuesta pedida | Respuesta recibida | Total alcanzado | ¿Terminó? | ¿Llegó al máximo del modelo? |
|---|---:|---:|---:|---:|---|---|
| 1 | — | 512 | — | — | En curso | No acreditado |
| 2 | — | 512 | — | — | En curso | No acreditado |
| 3 | — | 512 | — | — | En curso | No acreditado |
| 4 | — | 512 | — | — | En curso | No acreditado |
| 5 | — | 512 | — | — | En curso | No acreditado |
| 6 | — | 512 | — | — | En curso | No acreditado |
| 7 | — | 512 | — | — | En curso | No acreditado |
| 8 | — | 512 | — | — | En curso | No acreditado |
| 9 | — | 512 | — | — | En curso | No acreditado |
| 10 | — | 512 | — | — | En curso | No acreditado |
| 11 | — | 512 | — | — | En curso | No acreditado |
| 12 | — | 512 | — | — | En curso | No acreditado |
| 13 | — | 512 | — | — | En curso | No acreditado |
| 14 | — | 512 | — | — | En curso | No acreditado |
| 15 | — | 512 | — | — | En curso | No acreditado |
| 16 | — | 512 | — | — | En curso | No acreditado |
| 17 | — | 512 | — | — | En curso | No acreditado |
| 18 | — | 512 | — | — | En curso | No acreditado |
| 19 | — | 512 | — | — | En curso | No acreditado |
| 20 | — | 512 | — | — | En curso | No acreditado |
| 21 | — | 512 | — | — | En curso | No acreditado |
| 22 | — | 512 | — | — | En curso | No acreditado |
| 23 | — | 512 | — | — | En curso | No acreditado |
| 24 | — | 512 | — | — | En curso | No acreditado |
| 25 | — | 512 | — | — | En curso | No acreditado |
| 26 | — | 512 | — | — | En curso | No acreditado |
| 27 | — | 512 | — | — | En curso | No acreditado |
| 28 | — | 512 | — | — | En curso | No acreditado |
| 29 | — | 512 | — | — | En curso | No acreditado |
| 30 | — | 512 | — | — | En curso | No acreditado |
| 31 | — | 512 | — | — | En curso | No acreditado |
| 32 | — | 512 | — | — | En curso | No acreditado |
| 33 | — | 512 | — | — | En curso | No acreditado |
| 34 | — | 512 | — | — | En curso | No acreditado |
| 35 | — | 512 | — | — | En curso | No acreditado |
| 36 | — | 512 | — | — | En curso | No acreditado |
| 37 | — | 512 | — | — | En curso | No acreditado |
| 38 | — | 512 | — | — | En curso | No acreditado |
| 39 | — | 512 | — | — | En curso | No acreditado |
| 40 | — | 512 | — | — | En curso | No acreditado |
| 41 | — | 512 | — | — | En curso | No acreditado |
| 42 | — | 512 | — | — | En curso | No acreditado |
| 43 | — | 512 | — | — | En curso | No acreditado |
| 44 | — | 512 | — | — | En curso | No acreditado |
| 45 | — | 512 | — | — | En curso | No acreditado |
| 46 | — | 512 | — | — | En curso | No acreditado |
| 47 | — | 512 | — | — | En curso | No acreditado |
| 48 | — | 512 | — | — | En curso | No acreditado |
| 49 | — | 512 | — | — | En curso | No acreditado |
| 50 | — | 512 | — | — | En curso | No acreditado |
| 51 | — | 512 | — | — | En curso | No acreditado |
| 52 | — | 512 | — | — | En curso | No acreditado |
| 53 | — | 512 | — | — | En curso | No acreditado |
| 54 | — | 512 | — | — | En curso | No acreditado |
| 55 | — | 512 | — | — | En curso | No acreditado |
| 56 | — | 512 | — | — | En curso | No acreditado |
| 57 | — | 512 | — | — | En curso | No acreditado |
| 58 | — | 512 | — | — | En curso | No acreditado |
| 59 | — | 512 | — | — | En curso | No acreditado |
| 60 | — | 512 | — | — | En curso | No acreditado |
| 61 | — | 512 | — | — | En curso | No acreditado |
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
| Máximo activo en el motor | 61 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | Pendiente |
| Tiempo medio de respuesta completa | Pendiente |
| Mayor espera hasta primer texto, entre las completadas | Pendiente |
| Mayor tiempo completo, entre las completadas | Pendiente |
| Suma de los tiempos individuales | Pendiente |
| Tiempo total de la prueba | 30,6 s |
| Tokens/s medios por conversación, incluyendo espera | Pendiente |
| Tokens/s totales del grupo | Pendiente |
| Pico de caché ocupada | 20,2% |
| Máximo de solicitudes en cola | 507 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 28,6 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 75,0 °C |
| Límite de espera sin datos en cada conexión | 1.200 s |
| Tiempo máximo permitido para el grupo | 1.500 s |

La caché guarda información del historial. Un recálculo significa que el motor tuvo que desalojar trabajo y repetirlo. Una cola breve durante la lectura inicial no prueba por sí sola falta de memoria.

Los tiempos individuales se solapan: su suma puede superar el tiempo total de la prueba. Las velocidades cuentan tokens de respuesta, no tokens de entrada.

Las medias, los máximos de tiempo y las velocidades individuales corresponden solo a las conversaciones completadas correctamente. Las cifras de una prueba en curso son parciales; no describen todavía el rendimiento final del grupo.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
