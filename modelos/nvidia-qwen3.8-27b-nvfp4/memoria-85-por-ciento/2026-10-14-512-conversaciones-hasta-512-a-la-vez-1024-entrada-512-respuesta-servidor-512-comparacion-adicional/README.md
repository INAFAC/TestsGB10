# 512 conversaciones, hasta 512 a la vez; 1.024 de entrada + 512 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 85% del GB10.

**Límite impuesto al servidor: 512 solicitudes activas** (`--max-num-seqs 512`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 142/512 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 309 activas en el motor; cola máxima 507.
- **Tiempo para completar la prueba:** 637,4 s.

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
| 62 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 63 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 64 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 65 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 66 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 67 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 68 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 69 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 70 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 71 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 72 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 73 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 74 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 75 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 76 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 77 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 78 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 79 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 80 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 81 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 82 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 83 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 84 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 85 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 86 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 87 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 88 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 89 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 90 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 91 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 92 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 93 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 94 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 95 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 96 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 97 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 98 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 99 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 100 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 101 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 102 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 103 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 104 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 105 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 106 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 107 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 108 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 109 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 110 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 111 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 112 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 113 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 114 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 115 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 116 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 117 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 118 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 119 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 120 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 121 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 122 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 123 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 124 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 125 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 126 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 127 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 129 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 131 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 134 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 135 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 136 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 137 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 138 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 140 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 141 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 144 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 145 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 146 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 148 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 149 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 150 | 1.024 | 512 | 512 | 1.536 | Sí | No |
| 128 | — | 512 | — | — | En curso | No acreditado |
| 130 | — | 512 | — | — | En curso | No acreditado |
| 132 | — | 512 | — | — | En curso | No acreditado |
| 133 | — | 512 | — | — | En curso | No acreditado |
| 139 | — | 512 | — | — | En curso | No acreditado |
| 142 | — | 512 | — | — | En curso | No acreditado |
| 143 | — | 512 | — | — | En curso | No acreditado |
| 147 | — | 512 | — | — | En curso | No acreditado |
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
| 1 | 1,73 | 483,70 | 1,06 | 1,06 |
| 2 | 1,73 | 483,70 | 1,06 | 1,06 |
| 3 | 2,33 | 485,39 | 1,06 | 1,05 |
| 4 | 2,96 | 487,22 | 1,06 | 1,05 |
| 5 | 2,33 | 485,38 | 1,06 | 1,05 |
| 6 | 3,57 | 488,85 | 1,05 | 1,05 |
| 7 | 3,57 | 488,85 | 1,05 | 1,05 |
| 8 | 4,82 | 492,33 | 1,05 | 1,04 |
| 9 | 4,20 | 490,50 | 1,05 | 1,04 |
| 10 | 4,81 | 492,33 | 1,05 | 1,04 |
| 11 | 5,46 | 494,07 | 1,05 | 1,04 |
| 12 | 6,08 | 495,76 | 1,04 | 1,03 |
| 13 | 6,08 | 495,76 | 1,04 | 1,03 |
| 14 | 6,73 | 498,02 | 1,04 | 1,03 |
| 15 | 7,36 | 500,09 | 1,04 | 1,02 |
| 16 | 7,36 | 500,09 | 1,04 | 1,02 |
| 17 | 8,71 | 503,46 | 1,03 | 1,02 |
| 18 | 8,03 | 501,77 | 1,03 | 1,02 |
| 19 | 9,39 | 505,12 | 1,03 | 1,01 |
| 20 | 8,71 | 503,45 | 1,03 | 1,02 |
| 21 | 10,09 | 506,81 | 1,03 | 1,01 |
| 22 | 10,08 | 506,81 | 1,03 | 1,01 |
| 23 | 10,79 | 508,50 | 1,03 | 1,01 |
| 24 | 12,93 | 513,52 | 1,02 | 1,00 |
| 25 | 11,49 | 510,18 | 1,02 | 1,00 |
| 26 | 11,49 | 510,16 | 1,02 | 1,00 |
| 27 | 12,20 | 511,84 | 1,02 | 1,00 |
| 28 | 12,92 | 513,51 | 1,02 | 1,00 |
| 29 | 13,65 | 515,18 | 1,02 | 0,99 |
| 30 | 15,11 | 518,50 | 1,02 | 0,99 |
| 31 | 14,38 | 516,84 | 1,02 | 0,99 |
| 32 | 14,38 | 516,86 | 1,02 | 0,99 |
| 33 | 15,87 | 520,15 | 1,01 | 0,98 |
| 34 | 15,87 | 520,15 | 1,01 | 0,98 |
| 35 | 16,61 | 521,81 | 1,01 | 0,98 |
| 36 | 17,37 | 523,47 | 1,01 | 0,98 |
| 37 | 17,37 | 523,47 | 1,01 | 0,98 |
| 38 | 18,89 | 526,79 | 1,01 | 0,97 |
| 39 | 18,12 | 525,13 | 1,01 | 0,97 |
| 40 | 18,89 | 526,79 | 1,01 | 0,97 |
| 41 | 21,41 | 530,11 | 1,00 | 0,97 |
| 42 | 20,56 | 528,45 | 1,01 | 0,97 |
| 43 | 21,40 | 530,11 | 1,00 | 0,97 |
| 44 | 22,18 | 532,38 | 1,00 | 0,96 |
| 45 | 22,96 | 534,36 | 1,00 | 0,96 |
| 46 | 24,56 | 537,65 | 1,00 | 0,95 |
| 47 | 23,76 | 536,01 | 1,00 | 0,96 |
| 48 | 22,96 | 534,36 | 1,00 | 0,96 |
| 49 | 25,36 | 539,29 | 0,99 | 0,95 |
| 50 | 24,56 | 537,65 | 1,00 | 0,95 |
| 51 | 26,17 | 540,92 | 0,99 | 0,95 |
| 52 | 26,17 | 540,92 | 0,99 | 0,95 |
| 53 | 26,98 | 542,55 | 0,99 | 0,94 |
| 54 | 27,80 | 544,18 | 0,99 | 0,94 |
| 55 | 27,80 | 544,18 | 0,99 | 0,94 |
| 56 | 28,62 | 545,80 | 0,99 | 0,94 |
| 57 | 29,46 | 547,42 | 0,99 | 0,94 |
| 58 | 29,46 | 547,42 | 0,99 | 0,94 |
| 59 | 30,30 | 549,03 | 0,99 | 0,93 |
| 60 | 31,16 | 550,64 | 0,98 | 0,93 |
| 61 | 31,16 | 550,65 | 0,98 | 0,93 |
| 62 | 34,58 | 557,10 | 0,98 | 0,92 |
| 63 | 37,21 | 561,91 | 0,97 | 0,91 |
| 64 | 39,88 | 567,71 | 0,97 | 0,90 |
| 65 | 38,09 | 563,51 | 0,97 | 0,91 |
| 66 | 35,44 | 558,70 | 0,98 | 0,92 |
| 67 | 32,85 | 553,87 | 0,98 | 0,92 |
| 68 | 33,70 | 555,49 | 0,98 | 0,92 |
| 69 | 36,32 | 560,30 | 0,98 | 0,91 |
| 70 | 38,09 | 563,50 | 0,97 | 0,91 |
| 71 | 38,98 | 565,10 | 0,97 | 0,91 |
| 72 | 32,84 | 553,89 | 0,98 | 0,92 |
| 73 | 34,57 | 557,11 | 0,98 | 0,92 |
| 74 | 41,70 | 570,86 | 0,97 | 0,90 |
| 75 | 36,32 | 560,30 | 0,98 | 0,91 |
| 76 | 31,98 | 552,25 | 0,98 | 0,93 |
| 77 | 40,78 | 569,27 | 0,97 | 0,90 |
| 78 | 39,87 | 567,67 | 0,97 | 0,90 |
| 79 | 42,61 | 570,85 | 0,97 | 0,90 |
| 80 | 42,60 | 572,43 | 0,96 | 0,89 |
| 81 | 43,53 | 574,02 | 0,96 | 0,89 |
| 82 | 43,53 | 574,03 | 0,96 | 0,89 |
| 83 | 44,45 | 575,61 | 0,96 | 0,89 |
| 84 | 45,38 | 577,18 | 0,96 | 0,89 |
| 85 | 45,39 | 577,18 | 0,96 | 0,89 |
| 86 | 46,32 | 578,76 | 0,96 | 0,88 |
| 87 | 47,26 | 580,34 | 0,96 | 0,88 |
| 88 | 47,26 | 580,35 | 0,96 | 0,88 |
| 89 | 48,21 | 581,91 | 0,96 | 0,88 |
| 90 | 49,16 | 583,47 | 0,96 | 0,88 |
| 91 | 49,16 | 583,50 | 0,96 | 0,88 |
| 92 | 50,11 | 585,03 | 0,96 | 0,88 |
| 93 | 51,07 | 586,59 | 0,95 | 0,87 |
| 94 | 51,08 | 586,61 | 0,95 | 0,87 |
| 95 | 52,04 | 588,17 | 0,95 | 0,87 |
| 96 | 55,87 | 592,83 | 0,95 | 0,86 |
| 97 | 53,15 | 589,72 | 0,95 | 0,87 |
| 98 | 53,16 | 589,71 | 0,95 | 0,87 |
| 99 | 54,88 | 591,26 | 0,95 | 0,87 |
| 100 | 55,86 | 592,82 | 0,95 | 0,86 |
| 101 | 56,86 | 594,38 | 0,95 | 0,86 |
| 102 | 57,84 | 595,91 | 0,95 | 0,86 |
| 103 | 58,84 | 597,45 | 0,95 | 0,86 |
| 104 | 57,85 | 595,91 | 0,95 | 0,86 |
| 105 | 59,85 | 599,01 | 0,95 | 0,85 |
| 106 | 59,85 | 599,01 | 0,95 | 0,85 |
| 107 | 60,85 | 601,51 | 0,95 | 0,85 |
| 108 | 61,87 | 603,07 | 0,94 | 0,85 |
| 109 | 61,87 | 603,07 | 0,94 | 0,85 |
| 110 | 63,91 | 606,13 | 0,94 | 0,84 |
| 111 | 62,88 | 604,59 | 0,94 | 0,85 |
| 112 | 63,91 | 606,13 | 0,94 | 0,84 |
| 113 | 64,94 | 607,66 | 0,94 | 0,84 |
| 114 | 65,99 | 609,19 | 0,94 | 0,84 |
| 115 | 65,99 | 609,21 | 0,94 | 0,84 |
| 116 | 67,04 | 610,71 | 0,94 | 0,84 |
| 117 | 68,09 | 612,24 | 0,94 | 0,84 |
| 118 | 68,09 | 612,23 | 0,94 | 0,84 |
| 119 | 69,15 | 613,76 | 0,94 | 0,83 |
| 120 | 70,21 | 615,28 | 0,94 | 0,83 |
| 121 | 70,21 | 615,28 | 0,94 | 0,83 |
| 122 | 71,27 | 616,78 | 0,94 | 0,83 |
| 123 | 72,35 | 618,30 | 0,94 | 0,83 |
| 124 | 72,35 | 618,30 | 0,94 | 0,83 |
| 125 | 73,43 | 619,81 | 0,94 | 0,83 |
| 126 | 81,16 | 630,33 | 0,93 | 0,81 |
| 127 | 75,60 | 622,82 | 0,93 | 0,82 |
| 129 | 83,41 | 633,30 | 0,93 | 0,81 |
| 131 | 78,93 | 627,32 | 0,93 | 0,82 |
| 134 | 76,71 | 624,33 | 0,93 | 0,82 |
| 135 | 82,28 | 631,80 | 0,93 | 0,81 |
| 136 | 85,68 | 637,25 | 0,93 | 0,80 |
| 137 | 80,03 | 628,81 | 0,93 | 0,81 |
| 138 | 78,92 | 627,31 | 0,93 | 0,82 |
| 140 | 74,51 | 621,30 | 0,93 | 0,82 |
| 141 | 83,41 | 633,29 | 0,93 | 0,81 |
| 144 | 85,67 | 637,26 | 0,93 | 0,80 |
| 145 | 74,50 | 621,30 | 0,93 | 0,82 |
| 146 | 81,15 | 630,31 | 0,93 | 0,81 |
| 148 | 84,54 | 635,67 | 0,93 | 0,81 |
| 149 | 76,69 | 624,31 | 0,93 | 0,82 |
| 150 | 77,80 | 625,81 | 0,93 | 0,82 |

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
| Máximo activo en el motor | 309 |
| Máximo de respuestas solapadas | — |
| Espera media hasta primer texto | 39,6 s |
| Tiempo medio de respuesta completa | 561,9 s |
| Mayor espera hasta primer texto, entre las completadas | 85,7 s |
| Mayor tiempo completo, entre las completadas | 637,3 s |
| Suma de los tiempos individuales | 79.784,8 s |
| Tiempo total de la prueba | 637,4 s |
| Tokens/s medios por conversación, incluyendo espera | 0,92 |
| Tokens/s totales del grupo | 114,06 |
| Pico de caché ocupada | 100,0% |
| Máximo de solicitudes en cola | 507 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 635,5 s |
| Tiempo observado con caché al 95% o más | 284,7 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 76,0 °C |
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
| 1 | 0,05 | 1,78 | 483,75 |
| 2 | 0,05 | 1,78 | 483,76 |
| 3 | 0,05 | 2,38 | 485,44 |
| 4 | 0,05 | 3,01 | 487,27 |
| 5 | 0,05 | 2,38 | 485,43 |
| 6 | 0,05 | 3,63 | 488,91 |
| 7 | 0,06 | 3,63 | 488,91 |
| 8 | 0,06 | 4,87 | 492,39 |
| 9 | 0,06 | 4,26 | 490,56 |
| 10 | 0,06 | 4,88 | 492,39 |
| 11 | 0,06 | 5,52 | 494,13 |
| 12 | 0,06 | 6,15 | 495,82 |
| 13 | 0,06 | 6,15 | 495,82 |
| 14 | 0,06 | 6,79 | 498,08 |
| 15 | 0,07 | 7,43 | 500,16 |
| 16 | 0,07 | 7,42 | 500,16 |
| 17 | 0,07 | 8,78 | 503,52 |
| 18 | 0,07 | 8,10 | 501,84 |
| 19 | 0,07 | 9,46 | 505,19 |
| 20 | 0,07 | 8,78 | 503,52 |
| 21 | 0,07 | 10,16 | 506,89 |
| 22 | 0,07 | 10,16 | 506,88 |
| 23 | 0,07 | 10,86 | 508,57 |
| 24 | 0,07 | 13,00 | 513,59 |
| 25 | 0,08 | 11,57 | 510,25 |
| 26 | 0,08 | 11,57 | 510,24 |
| 27 | 0,08 | 12,28 | 511,91 |
| 28 | 0,08 | 13,00 | 513,59 |
| 29 | 0,08 | 13,73 | 515,26 |
| 30 | 0,08 | 15,19 | 518,58 |
| 31 | 0,08 | 14,46 | 516,92 |
| 32 | 0,08 | 14,46 | 516,94 |
| 33 | 0,08 | 15,95 | 520,24 |
| 34 | 0,08 | 15,95 | 520,24 |
| 35 | 0,09 | 16,69 | 521,90 |
| 36 | 0,09 | 17,46 | 523,56 |
| 37 | 0,09 | 17,46 | 523,56 |
| 38 | 0,09 | 18,98 | 526,88 |
| 39 | 0,09 | 18,21 | 525,22 |
| 40 | 0,09 | 18,98 | 526,88 |
| 41 | 0,09 | 21,50 | 530,20 |
| 42 | 0,09 | 20,65 | 528,54 |
| 43 | 0,09 | 21,50 | 530,20 |
| 44 | 0,09 | 22,27 | 532,47 |
| 45 | 0,09 | 23,06 | 534,45 |
| 46 | 0,09 | 24,65 | 537,75 |
| 47 | 0,10 | 23,85 | 536,10 |
| 48 | 0,10 | 23,05 | 534,46 |
| 49 | 0,10 | 25,45 | 539,38 |
| 50 | 0,10 | 24,65 | 537,75 |
| 51 | 0,10 | 26,27 | 541,02 |
| 52 | 0,10 | 26,27 | 541,02 |
| 53 | 0,10 | 27,08 | 542,66 |
| 54 | 0,10 | 27,91 | 544,28 |
| 55 | 0,11 | 27,90 | 544,28 |
| 56 | 0,11 | 28,73 | 545,90 |
| 57 | 0,11 | 29,57 | 547,53 |
| 58 | 0,11 | 29,57 | 547,53 |
| 59 | 0,11 | 30,41 | 549,14 |
| 60 | 0,11 | 31,27 | 550,75 |
| 61 | 0,11 | 31,26 | 550,76 |
| 62 | 0,11 | 34,69 | 557,21 |
| 63 | 0,11 | 37,32 | 562,02 |
| 64 | 0,11 | 40,00 | 567,82 |
| 65 | 0,11 | 38,21 | 563,62 |
| 66 | 0,11 | 35,55 | 558,82 |
| 67 | 0,11 | 32,96 | 553,99 |
| 68 | 0,12 | 33,82 | 555,60 |
| 69 | 0,12 | 36,44 | 560,42 |
| 70 | 0,12 | 38,20 | 563,62 |
| 71 | 0,12 | 39,10 | 565,22 |
| 72 | 0,12 | 32,96 | 554,01 |
| 73 | 0,12 | 34,69 | 557,23 |
| 74 | 0,12 | 41,82 | 570,98 |
| 75 | 0,12 | 36,44 | 560,42 |
| 76 | 0,12 | 32,10 | 552,37 |
| 77 | 0,12 | 40,90 | 569,40 |
| 78 | 0,13 | 40,00 | 567,80 |
| 79 | 0,13 | 42,73 | 570,98 |
| 80 | 0,13 | 42,73 | 572,56 |
| 81 | 0,13 | 43,65 | 574,15 |
| 82 | 0,13 | 43,66 | 574,16 |
| 83 | 0,13 | 44,58 | 575,74 |
| 84 | 0,13 | 45,51 | 577,31 |
| 85 | 0,13 | 45,52 | 577,31 |
| 86 | 0,13 | 46,45 | 578,89 |
| 87 | 0,13 | 47,39 | 580,47 |
| 88 | 0,13 | 47,39 | 580,48 |
| 89 | 0,13 | 48,34 | 582,04 |
| 90 | 0,13 | 49,29 | 583,61 |
| 91 | 0,13 | 49,29 | 583,63 |
| 92 | 0,14 | 50,25 | 585,17 |
| 93 | 0,14 | 51,21 | 586,73 |
| 94 | 0,14 | 51,22 | 586,75 |
| 95 | 0,14 | 52,18 | 588,30 |
| 96 | 0,14 | 56,00 | 592,96 |
| 97 | 0,14 | 53,29 | 589,86 |
| 98 | 0,14 | 53,30 | 589,85 |
| 99 | 0,14 | 55,02 | 591,41 |
| 100 | 0,14 | 56,00 | 592,96 |
| 101 | 0,14 | 57,00 | 594,52 |
| 102 | 0,14 | 57,99 | 596,06 |
| 103 | 0,15 | 58,99 | 597,60 |
| 104 | 0,15 | 57,99 | 596,06 |
| 105 | 0,15 | 60,00 | 599,16 |
| 106 | 0,15 | 60,00 | 599,16 |
| 107 | 0,15 | 61,00 | 601,66 |
| 108 | 0,15 | 62,02 | 603,21 |
| 109 | 0,15 | 62,02 | 603,22 |
| 110 | 0,15 | 64,06 | 606,28 |
| 111 | 0,15 | 63,04 | 604,75 |
| 112 | 0,15 | 64,07 | 606,28 |
| 113 | 0,15 | 65,09 | 607,82 |
| 114 | 0,16 | 66,14 | 609,34 |
| 115 | 0,16 | 66,14 | 609,36 |
| 116 | 0,16 | 67,19 | 610,87 |
| 117 | 0,16 | 68,25 | 612,40 |
| 118 | 0,16 | 68,24 | 612,39 |
| 119 | 0,16 | 69,30 | 613,92 |
| 120 | 0,16 | 70,37 | 615,44 |
| 121 | 0,16 | 70,37 | 615,44 |
| 122 | 0,16 | 71,43 | 616,94 |
| 123 | 0,16 | 72,51 | 618,46 |
| 124 | 0,16 | 72,52 | 618,46 |
| 125 | 0,16 | 73,60 | 619,97 |
| 126 | 0,16 | 81,33 | 630,49 |
| 127 | 0,17 | 75,77 | 622,98 |
| 129 | 0,17 | 83,58 | 633,47 |
| 131 | 0,17 | 79,09 | 627,49 |
| 134 | 0,17 | 76,88 | 624,50 |
| 135 | 0,17 | 82,45 | 631,97 |
| 136 | 0,17 | 85,86 | 637,42 |
| 137 | 0,17 | 80,21 | 628,98 |
| 138 | 0,17 | 79,09 | 627,49 |
| 140 | 0,18 | 74,68 | 621,48 |
| 141 | 0,18 | 83,58 | 633,47 |
| 144 | 0,18 | 85,85 | 637,44 |
| 145 | 0,18 | 74,68 | 621,48 |
| 146 | 0,18 | 81,33 | 630,49 |
| 148 | 0,18 | 84,72 | 635,85 |
| 149 | 0,18 | 76,88 | 624,50 |
| 150 | 0,18 | 77,98 | 625,99 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
