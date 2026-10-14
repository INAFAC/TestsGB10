# 512 conversaciones, hasta 512 a la vez; 1.024 de entrada + 128 de respuesta

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 85% del GB10.

**Límite impuesto al servidor: 512 solicitudes activas** (`--max-num-seqs 512`). Aunque se envíen más, el motor no puede superar ese límite en esta prueba. Observar ese número no demuestra que sea el máximo del GB10.

## ¿Qué ocurrió?

- **¿Terminaron todas las conversaciones?** 171/512 (en curso). Terminar significa recibir todos los tokens de respuesta solicitados.
- **¿Llegaron al máximo del modelo (262.144 tokens)?** No se intentó.
- **Límite configurado en esta prueba:** 262.144 tokens, sumando entrada y respuesta.
- **¿Se atendieron al mismo tiempo?** 194 activas en el motor; cola máxima 506.
- **Tiempo para completar la prueba:** 280,6 s.

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
| 7 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 8 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 9 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 10 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 11 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 12 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 13 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 14 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 15 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 16 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 17 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 18 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 19 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 20 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 21 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 22 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 23 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 24 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 25 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 26 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 27 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 28 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 29 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 30 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 31 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 32 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 33 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 34 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 35 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 36 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 37 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 38 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 39 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 40 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 41 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 42 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 43 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 44 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 45 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 46 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 47 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 48 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 49 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 50 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 51 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 52 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 53 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 54 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 55 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 56 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 57 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 58 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 59 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 60 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 61 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 62 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 63 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 64 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 65 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 66 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 67 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 68 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 69 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 70 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 71 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 72 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 73 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 74 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 75 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 76 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 77 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 78 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 79 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 80 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 81 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 82 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 83 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 84 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 85 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 86 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 87 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 88 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 89 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 90 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 91 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 92 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 93 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 94 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 95 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 96 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 97 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 98 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 99 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 100 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 101 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 102 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 103 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 104 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 105 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 106 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 107 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 108 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 109 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 110 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 111 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 112 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 113 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 114 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 115 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 116 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 117 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 118 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 119 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 120 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 121 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 122 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 123 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 124 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 125 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 126 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 127 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 128 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 129 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 130 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 131 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 132 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 133 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 134 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 135 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 136 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 137 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 138 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 139 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 140 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 141 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 142 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 143 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 144 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 145 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 146 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 147 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 148 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 149 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 150 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 151 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 152 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 153 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 154 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 155 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 156 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 157 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 158 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 159 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 160 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 161 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 162 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 163 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 164 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 165 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 166 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 167 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 168 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 169 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 170 | 1.024 | 128 | 128 | 1.152 | Sí | No |
| 171 | 1.024 | 128 | 128 | 1.152 | Sí | No |
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
| 7 | 5,03 | 135,94 | 0,97 | 0,94 |
| 8 | 4,39 | 134,64 | 0,98 | 0,95 |
| 9 | 4,40 | 134,63 | 0,98 | 0,95 |
| 10 | 3,79 | 133,31 | 0,98 | 0,96 |
| 11 | 6,28 | 138,59 | 0,96 | 0,92 |
| 12 | 5,65 | 137,26 | 0,96 | 0,93 |
| 13 | 5,64 | 137,26 | 0,96 | 0,93 |
| 14 | 6,90 | 139,90 | 0,95 | 0,91 |
| 15 | 6,90 | 139,89 | 0,95 | 0,92 |
| 16 | 7,55 | 141,20 | 0,95 | 0,91 |
| 17 | 8,18 | 142,52 | 0,95 | 0,90 |
| 18 | 8,18 | 142,52 | 0,95 | 0,90 |
| 19 | 8,86 | 143,84 | 0,94 | 0,89 |
| 20 | 9,54 | 145,16 | 0,94 | 0,88 |
| 21 | 11,64 | 149,11 | 0,92 | 0,86 |
| 22 | 10,23 | 146,47 | 0,93 | 0,87 |
| 23 | 10,94 | 147,78 | 0,93 | 0,87 |
| 24 | 16,00 | 157,00 | 0,90 | 0,82 |
| 25 | 10,93 | 147,79 | 0,93 | 0,87 |
| 26 | 12,35 | 150,43 | 0,92 | 0,85 |
| 27 | 15,26 | 155,69 | 0,90 | 0,82 |
| 28 | 16,75 | 158,32 | 0,90 | 0,81 |
| 29 | 17,50 | 159,64 | 0,89 | 0,80 |
| 30 | 16,75 | 158,33 | 0,90 | 0,81 |
| 31 | 13,06 | 151,73 | 0,92 | 0,84 |
| 32 | 12,35 | 150,41 | 0,92 | 0,85 |
| 33 | 13,78 | 153,04 | 0,91 | 0,84 |
| 34 | 13,78 | 153,05 | 0,91 | 0,84 |
| 35 | 14,51 | 154,37 | 0,91 | 0,83 |
| 36 | 9,53 | 145,15 | 0,94 | 0,88 |
| 37 | 15,25 | 155,69 | 0,90 | 0,82 |
| 38 | 18,25 | 160,95 | 0,89 | 0,80 |
| 39 | 18,25 | 160,95 | 0,89 | 0,80 |
| 40 | 19,00 | 162,27 | 0,89 | 0,79 |
| 41 | 19,77 | 163,59 | 0,88 | 0,78 |
| 42 | 19,77 | 163,59 | 0,88 | 0,78 |
| 43 | 22,89 | 169,68 | 0,87 | 0,75 |
| 44 | 25,29 | 173,64 | 0,86 | 0,74 |
| 45 | 24,49 | 172,31 | 0,86 | 0,74 |
| 46 | 21,32 | 167,05 | 0,87 | 0,77 |
| 47 | 22,89 | 169,69 | 0,87 | 0,75 |
| 48 | 21,32 | 167,04 | 0,87 | 0,77 |
| 49 | 22,10 | 168,36 | 0,87 | 0,76 |
| 50 | 24,48 | 172,32 | 0,86 | 0,74 |
| 51 | 26,10 | 174,95 | 0,85 | 0,73 |
| 52 | 20,54 | 164,99 | 0,88 | 0,78 |
| 53 | 27,74 | 177,59 | 0,85 | 0,72 |
| 54 | 23,68 | 171,00 | 0,86 | 0,75 |
| 55 | 28,56 | 178,91 | 0,84 | 0,72 |
| 56 | 26,91 | 176,27 | 0,85 | 0,73 |
| 57 | 27,73 | 177,59 | 0,85 | 0,72 |
| 58 | 31,11 | 181,54 | 0,84 | 0,71 |
| 59 | 29,39 | 180,22 | 0,84 | 0,71 |
| 60 | 26,09 | 174,96 | 0,85 | 0,73 |
| 61 | 29,39 | 180,22 | 0,84 | 0,71 |
| 62 | 37,16 | 190,77 | 0,83 | 0,67 |
| 63 | 37,16 | 190,78 | 0,83 | 0,67 |
| 64 | 34,52 | 186,82 | 0,83 | 0,69 |
| 65 | 36,27 | 189,45 | 0,83 | 0,68 |
| 66 | 31,95 | 182,86 | 0,84 | 0,70 |
| 67 | 33,66 | 185,50 | 0,84 | 0,69 |
| 68 | 33,65 | 185,49 | 0,84 | 0,69 |
| 69 | 38,93 | 193,40 | 0,82 | 0,66 |
| 70 | 32,79 | 184,16 | 0,84 | 0,70 |
| 71 | 35,39 | 188,12 | 0,83 | 0,68 |
| 72 | 31,95 | 182,85 | 0,84 | 0,70 |
| 73 | 38,04 | 192,08 | 0,82 | 0,67 |
| 74 | 35,39 | 188,12 | 0,83 | 0,68 |
| 75 | 39,81 | 194,71 | 0,82 | 0,66 |
| 76 | 38,92 | 193,40 | 0,82 | 0,66 |
| 77 | 40,72 | 196,03 | 0,82 | 0,65 |
| 78 | 40,72 | 196,03 | 0,82 | 0,65 |
| 79 | 41,62 | 197,34 | 0,82 | 0,65 |
| 80 | 42,54 | 198,75 | 0,81 | 0,64 |
| 81 | 42,54 | 198,75 | 0,81 | 0,64 |
| 82 | 43,45 | 200,89 | 0,81 | 0,64 |
| 83 | 44,38 | 202,20 | 0,80 | 0,63 |
| 84 | 44,38 | 202,21 | 0,80 | 0,63 |
| 85 | 45,31 | 203,52 | 0,80 | 0,63 |
| 86 | 46,25 | 204,83 | 0,80 | 0,62 |
| 87 | 48,13 | 207,47 | 0,80 | 0,62 |
| 88 | 50,04 | 210,10 | 0,79 | 0,61 |
| 89 | 52,94 | 214,05 | 0,79 | 0,60 |
| 90 | 46,25 | 204,83 | 0,80 | 0,62 |
| 91 | 48,13 | 207,47 | 0,80 | 0,62 |
| 92 | 49,08 | 208,78 | 0,80 | 0,61 |
| 93 | 53,91 | 215,36 | 0,79 | 0,59 |
| 94 | 50,04 | 210,10 | 0,79 | 0,61 |
| 95 | 51,00 | 211,42 | 0,79 | 0,61 |
| 96 | 51,96 | 212,73 | 0,79 | 0,60 |
| 97 | 51,96 | 212,73 | 0,79 | 0,60 |
| 98 | 53,91 | 215,37 | 0,79 | 0,59 |
| 99 | 47,18 | 206,14 | 0,80 | 0,62 |
| 100 | 55,86 | 218,00 | 0,78 | 0,59 |
| 101 | 54,87 | 216,68 | 0,78 | 0,59 |
| 102 | 55,86 | 218,00 | 0,78 | 0,59 |
| 103 | 56,86 | 219,32 | 0,78 | 0,58 |
| 104 | 57,85 | 220,64 | 0,78 | 0,58 |
| 105 | 58,84 | 221,96 | 0,78 | 0,58 |
| 106 | 57,85 | 220,64 | 0,78 | 0,58 |
| 107 | 59,84 | 223,28 | 0,78 | 0,57 |
| 108 | 61,89 | 225,91 | 0,77 | 0,57 |
| 109 | 59,85 | 223,27 | 0,78 | 0,57 |
| 110 | 60,86 | 224,59 | 0,78 | 0,57 |
| 111 | 61,88 | 225,91 | 0,77 | 0,57 |
| 112 | 62,90 | 227,22 | 0,77 | 0,56 |
| 113 | 64,68 | 228,54 | 0,78 | 0,56 |
| 114 | 64,68 | 228,53 | 0,78 | 0,56 |
| 115 | 66,85 | 231,17 | 0,77 | 0,55 |
| 116 | 65,79 | 229,86 | 0,77 | 0,56 |
| 117 | 67,90 | 232,66 | 0,77 | 0,55 |
| 118 | 66,84 | 231,19 | 0,77 | 0,55 |
| 119 | 68,95 | 234,64 | 0,77 | 0,55 |
| 120 | 68,95 | 234,65 | 0,77 | 0,55 |
| 121 | 70,01 | 235,96 | 0,77 | 0,54 |
| 122 | 71,09 | 237,27 | 0,76 | 0,54 |
| 123 | 71,09 | 237,28 | 0,76 | 0,54 |
| 124 | 72,15 | 238,60 | 0,76 | 0,54 |
| 125 | 73,24 | 239,91 | 0,76 | 0,53 |
| 126 | 76,50 | 243,87 | 0,76 | 0,52 |
| 127 | 85,47 | 254,42 | 0,75 | 0,50 |
| 128 | 75,41 | 242,55 | 0,76 | 0,53 |
| 129 | 79,83 | 247,83 | 0,76 | 0,52 |
| 130 | 77,61 | 245,19 | 0,76 | 0,52 |
| 131 | 83,19 | 251,78 | 0,75 | 0,51 |
| 132 | 79,83 | 247,82 | 0,76 | 0,52 |
| 133 | 80,94 | 249,13 | 0,76 | 0,51 |
| 134 | 82,07 | 250,45 | 0,75 | 0,51 |
| 135 | 78,71 | 246,51 | 0,76 | 0,52 |
| 136 | 74,31 | 241,22 | 0,76 | 0,53 |
| 137 | 75,41 | 242,55 | 0,76 | 0,53 |
| 138 | 73,23 | 239,91 | 0,76 | 0,53 |
| 139 | 77,60 | 245,18 | 0,76 | 0,52 |
| 140 | 82,06 | 250,46 | 0,75 | 0,51 |
| 141 | 86,61 | 255,73 | 0,75 | 0,50 |
| 142 | 84,32 | 253,09 | 0,75 | 0,51 |
| 143 | 84,32 | 253,09 | 0,75 | 0,51 |
| 144 | 86,61 | 255,72 | 0,75 | 0,50 |
| 145 | 87,76 | 257,05 | 0,75 | 0,50 |
| 146 | 88,92 | 258,37 | 0,75 | 0,50 |
| 147 | 88,92 | 258,36 | 0,75 | 0,50 |
| 148 | 90,07 | 259,68 | 0,75 | 0,49 |
| 149 | 91,24 | 260,99 | 0,75 | 0,49 |
| 150 | 91,24 | 260,99 | 0,75 | 0,49 |
| 151 | 92,41 | 262,32 | 0,75 | 0,49 |
| 152 | 95,97 | 266,47 | 0,74 | 0,48 |
| 153 | 93,60 | 263,63 | 0,75 | 0,49 |
| 154 | 93,60 | 263,63 | 0,75 | 0,49 |
| 155 | 99,27 | 269,80 | 0,74 | 0,47 |
| 156 | 94,77 | 264,95 | 0,75 | 0,48 |
| 157 | 95,97 | 266,46 | 0,74 | 0,48 |
| 158 | 99,27 | 269,79 | 0,74 | 0,47 |
| 159 | 97,19 | 268,47 | 0,74 | 0,48 |
| 160 | 100,47 | 271,11 | 0,74 | 0,47 |
| 161 | 101,69 | 272,42 | 0,74 | 0,47 |
| 162 | 101,68 | 272,43 | 0,74 | 0,47 |
| 163 | 102,90 | 273,74 | 0,74 | 0,47 |
| 164 | 104,12 | 275,05 | 0,74 | 0,47 |
| 165 | 104,12 | 275,05 | 0,74 | 0,47 |
| 166 | 106,57 | 277,69 | 0,74 | 0,46 |
| 167 | 107,81 | 279,01 | 0,74 | 0,46 |
| 168 | 105,34 | 276,37 | 0,74 | 0,46 |
| 169 | 106,57 | 277,70 | 0,74 | 0,46 |
| 170 | 109,06 | 280,33 | 0,74 | 0,46 |
| 171 | 109,06 | 280,34 | 0,74 | 0,46 |

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
| Espera media hasta primer texto | 49,0 s |
| Tiempo medio de respuesta completa | 204,1 s |
| Mayor espera hasta primer texto, entre las completadas | 109,1 s |
| Mayor tiempo completo, entre las completadas | 280,3 s |
| Suma de los tiempos individuales | 34.896,5 s |
| Tiempo total de la prueba | 280,6 s |
| Tokens/s medios por conversación, incluyendo espera | 0,66 |
| Tokens/s totales del grupo | 78,01 |
| Pico de caché ocupada | 63,1% |
| Máximo de solicitudes en cola | 506 |
| Recálculos por falta de espacio en caché | 0 |
| Tiempo observado con cola | 279,4 s |
| Tiempo observado con caché al 95% o más | 0,0 s |
| Tokens recuperados de caché de prefijos | 0 |
| Temperatura GPU máxima | 73,0 °C |
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
| 7 | 0,10 | 5,13 | 136,04 |
| 8 | 0,10 | 4,49 | 134,74 |
| 9 | 0,10 | 4,50 | 134,73 |
| 10 | 0,10 | 3,89 | 133,41 |
| 11 | 0,10 | 6,38 | 138,69 |
| 12 | 0,10 | 5,75 | 137,36 |
| 13 | 0,10 | 5,75 | 137,37 |
| 14 | 0,11 | 7,00 | 140,00 |
| 15 | 0,11 | 7,01 | 139,99 |
| 16 | 0,11 | 7,65 | 141,31 |
| 17 | 0,11 | 8,29 | 142,63 |
| 18 | 0,11 | 8,29 | 142,62 |
| 19 | 0,11 | 8,97 | 143,95 |
| 20 | 0,11 | 9,65 | 145,27 |
| 21 | 0,11 | 11,75 | 149,22 |
| 22 | 0,11 | 10,34 | 146,58 |
| 23 | 0,11 | 11,05 | 147,90 |
| 24 | 0,11 | 16,11 | 157,12 |
| 25 | 0,11 | 11,05 | 147,90 |
| 26 | 0,11 | 12,47 | 150,54 |
| 27 | 0,12 | 15,38 | 155,81 |
| 28 | 0,12 | 16,86 | 158,44 |
| 29 | 0,12 | 17,61 | 159,76 |
| 30 | 0,12 | 16,86 | 158,44 |
| 31 | 0,12 | 13,17 | 151,85 |
| 32 | 0,12 | 12,47 | 150,53 |
| 33 | 0,12 | 13,90 | 153,16 |
| 34 | 0,12 | 13,90 | 153,17 |
| 35 | 0,12 | 14,63 | 154,49 |
| 36 | 0,12 | 9,65 | 145,27 |
| 37 | 0,12 | 15,37 | 155,82 |
| 38 | 0,12 | 18,37 | 161,07 |
| 39 | 0,13 | 18,37 | 161,08 |
| 40 | 0,13 | 19,13 | 162,39 |
| 41 | 0,13 | 19,90 | 163,72 |
| 42 | 0,13 | 19,90 | 163,72 |
| 43 | 0,13 | 23,02 | 169,81 |
| 44 | 0,13 | 25,42 | 173,77 |
| 45 | 0,13 | 24,62 | 172,45 |
| 46 | 0,13 | 21,45 | 167,18 |
| 47 | 0,13 | 23,02 | 169,82 |
| 48 | 0,13 | 21,45 | 167,17 |
| 49 | 0,13 | 22,23 | 168,50 |
| 50 | 0,13 | 24,61 | 172,45 |
| 51 | 0,14 | 26,24 | 175,09 |
| 52 | 0,14 | 20,68 | 165,13 |
| 53 | 0,14 | 27,87 | 177,72 |
| 54 | 0,14 | 23,82 | 171,13 |
| 55 | 0,14 | 28,69 | 179,05 |
| 56 | 0,14 | 27,05 | 176,41 |
| 57 | 0,14 | 27,87 | 177,73 |
| 58 | 0,14 | 31,25 | 181,68 |
| 59 | 0,14 | 29,53 | 180,36 |
| 60 | 0,14 | 26,23 | 175,10 |
| 61 | 0,14 | 29,54 | 180,36 |
| 62 | 0,15 | 37,30 | 190,92 |
| 63 | 0,15 | 37,30 | 190,93 |
| 64 | 0,15 | 34,67 | 186,96 |
| 65 | 0,15 | 36,42 | 189,60 |
| 66 | 0,15 | 32,10 | 183,01 |
| 67 | 0,15 | 33,81 | 185,65 |
| 68 | 0,15 | 33,81 | 185,65 |
| 69 | 0,15 | 39,09 | 193,55 |
| 70 | 0,15 | 32,94 | 184,31 |
| 71 | 0,15 | 35,54 | 188,28 |
| 72 | 0,15 | 32,10 | 183,01 |
| 73 | 0,16 | 38,19 | 192,23 |
| 74 | 0,16 | 35,55 | 188,28 |
| 75 | 0,16 | 39,97 | 194,87 |
| 76 | 0,16 | 39,08 | 193,56 |
| 77 | 0,16 | 40,88 | 196,20 |
| 78 | 0,16 | 40,88 | 196,20 |
| 79 | 0,16 | 41,79 | 197,51 |
| 80 | 0,17 | 42,71 | 198,91 |
| 81 | 0,17 | 42,71 | 198,91 |
| 82 | 0,17 | 43,62 | 201,06 |
| 83 | 0,17 | 44,55 | 202,37 |
| 84 | 0,17 | 44,55 | 202,38 |
| 85 | 0,17 | 45,48 | 203,69 |
| 86 | 0,17 | 46,42 | 205,00 |
| 87 | 0,17 | 48,31 | 207,64 |
| 88 | 0,17 | 50,21 | 210,28 |
| 89 | 0,17 | 53,12 | 214,23 |
| 90 | 0,18 | 46,43 | 205,00 |
| 91 | 0,18 | 48,31 | 207,64 |
| 92 | 0,18 | 49,26 | 208,96 |
| 93 | 0,18 | 54,09 | 215,54 |
| 94 | 0,18 | 50,22 | 210,28 |
| 95 | 0,18 | 51,18 | 211,60 |
| 96 | 0,18 | 52,15 | 212,91 |
| 97 | 0,18 | 52,15 | 212,91 |
| 98 | 0,18 | 54,10 | 215,55 |
| 99 | 0,18 | 47,36 | 206,32 |
| 100 | 0,19 | 56,05 | 218,19 |
| 101 | 0,19 | 55,06 | 216,87 |
| 102 | 0,19 | 56,05 | 218,19 |
| 103 | 0,19 | 57,04 | 219,51 |
| 104 | 0,19 | 58,04 | 220,83 |
| 105 | 0,19 | 59,03 | 222,15 |
| 106 | 0,19 | 58,04 | 220,83 |
| 107 | 0,19 | 60,04 | 223,47 |
| 108 | 0,19 | 62,08 | 226,10 |
| 109 | 0,19 | 60,04 | 223,47 |
| 110 | 0,19 | 61,05 | 224,78 |
| 111 | 0,19 | 62,08 | 226,10 |
| 112 | 0,19 | 63,09 | 227,42 |
| 113 | 0,20 | 64,88 | 228,74 |
| 114 | 0,20 | 64,88 | 228,73 |
| 115 | 0,20 | 67,05 | 231,37 |
| 116 | 0,20 | 65,99 | 230,06 |
| 117 | 0,20 | 68,10 | 232,86 |
| 118 | 0,20 | 67,04 | 231,39 |
| 119 | 0,20 | 69,15 | 234,84 |
| 120 | 0,20 | 69,15 | 234,85 |
| 121 | 0,21 | 70,22 | 236,16 |
| 122 | 0,21 | 71,29 | 237,48 |
| 123 | 0,21 | 71,29 | 237,49 |
| 124 | 0,21 | 72,36 | 238,81 |
| 125 | 0,21 | 73,45 | 240,12 |
| 126 | 0,21 | 76,71 | 244,08 |
| 127 | 0,21 | 85,68 | 254,64 |
| 128 | 0,21 | 75,62 | 242,76 |
| 129 | 0,21 | 80,04 | 248,04 |
| 130 | 0,21 | 77,82 | 245,40 |
| 131 | 0,21 | 83,40 | 252,00 |
| 132 | 0,21 | 80,04 | 248,03 |
| 133 | 0,21 | 81,15 | 249,35 |
| 134 | 0,22 | 82,28 | 250,66 |
| 135 | 0,22 | 78,93 | 246,72 |
| 136 | 0,22 | 74,52 | 241,43 |
| 137 | 0,22 | 75,63 | 242,76 |
| 138 | 0,22 | 73,45 | 240,12 |
| 139 | 0,22 | 77,82 | 245,40 |
| 140 | 0,22 | 82,28 | 250,68 |
| 141 | 0,22 | 86,83 | 255,95 |
| 142 | 0,22 | 84,55 | 253,31 |
| 143 | 0,22 | 84,55 | 253,31 |
| 144 | 0,22 | 86,83 | 255,95 |
| 145 | 0,23 | 87,99 | 257,27 |
| 146 | 0,23 | 89,14 | 258,59 |
| 147 | 0,23 | 89,14 | 258,59 |
| 148 | 0,23 | 90,30 | 259,91 |
| 149 | 0,23 | 91,46 | 261,22 |
| 150 | 0,23 | 91,47 | 261,22 |
| 151 | 0,23 | 92,65 | 262,55 |
| 152 | 0,23 | 96,21 | 266,70 |
| 153 | 0,23 | 93,83 | 263,86 |
| 154 | 0,24 | 93,83 | 263,86 |
| 155 | 0,24 | 99,50 | 270,03 |
| 156 | 0,24 | 95,01 | 265,19 |
| 157 | 0,24 | 96,21 | 266,70 |
| 158 | 0,24 | 99,51 | 270,03 |
| 159 | 0,24 | 97,43 | 268,71 |
| 160 | 0,24 | 100,71 | 271,35 |
| 161 | 0,24 | 101,93 | 272,66 |
| 162 | 0,24 | 101,92 | 272,67 |
| 163 | 0,24 | 103,14 | 273,98 |
| 164 | 0,24 | 104,36 | 275,29 |
| 165 | 0,24 | 104,37 | 275,30 |
| 166 | 0,24 | 106,82 | 277,93 |
| 167 | 0,25 | 108,05 | 279,26 |
| 168 | 0,25 | 105,59 | 276,62 |
| 169 | 0,25 | 106,82 | 277,95 |
| 170 | 0,25 | 109,30 | 280,58 |
| 171 | 0,25 | 109,30 | 280,58 |

</details>

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).
- [Registro de ejecucion](registro-de-ejecucion.log).

</details>
