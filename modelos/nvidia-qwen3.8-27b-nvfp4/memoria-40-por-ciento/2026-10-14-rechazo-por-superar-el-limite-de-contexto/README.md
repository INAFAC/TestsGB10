# Enviar más tokens que el límite permitido

[Volver al modelo](../../README.md) · [Ver las pruebas con esta memoria](../README.md)

**Modelo:** `nvidia/Qwen3.8-27B-NVFP4`. **Memoria asignada:** 40% del GB10.

**Resultado: rechazo esperado.**

Se enviaron 262.145 tokens de entrada y se pidió 1 de respuesta: la suma supera el límite configurado.

La API respondió HTTP 400 en 0,046 s. Esto comprueba el límite de tokens, no un fallo de memoria.

<details>
<summary>Mediciones originales y registros de esta prueba</summary>

- [Mediciones originales](mediciones.json).
- [Configuración de esta prueba](configuracion.json).

</details>
