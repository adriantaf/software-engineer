---
id: L18
materia: M17
orden: 18
titulo: Botón pedido WhatsApp desde el perfil / ficha
horas: 5
semana: 5
lectura: UI + wa.me
evidencia: acción pedido WhatsApp
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - deep-link `wa.me`

      - mensaje prefijado

      - sin WhatsApp Business API en v1


      **Objetivo de esta lección:** En el perfil público (o preview), acción que
      abre `wa.me` con el pedido prefijado (ítems + total + “pago al recoger”).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Generar texto del pedido
    xp: 10
    cuerpo: >-
      ```bash

      echo "ej: https://wa.me/525500000000?text=..." >>
      projects/m17-vitrina/docs/integracion-whatsapp.md

      git add projects/m17-vitrina

      git commit -m "feat(m17): L18 pedido whatsapp wa.me"

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Botón en UI
    xp: 10
    cuerpo: >-
      ```bash

      echo "ej: https://wa.me/525500000000?text=..." >>
      projects/m17-vitrina/docs/integracion-whatsapp.md

      git add projects/m17-vitrina

      git commit -m "feat(m17): L18 pedido whatsapp wa.me"

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Botón pedido WhatsApp desde el perfil / ficha», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Botón pedido WhatsApp
          desde el perfil /…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `echo "ej: https://wa.me/525500000000?text=..." >>
      projects/m17-vitrina/docs/integracion-whatsapp.md`
    comandoEsperado:
      - >-
        echo "ej: https://wa.me/525500000000?text=..." >>
        projects/m17-vitrina/docs/integracion-whatsapp.md
      - git add projects/m17-vitrina
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: echo "ej: https://wa.me/525500000000?text=..." >>
      projects/m17-vitrina/docs/integracion-whatsapp.md
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          En el perfil público (o preview), acción que abre `wa.me` con el
          pedido prefijado (ítems + total + “pago al recoger”).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Evidencia
    xp: 10
    cuerpo: >-
      ```bash

      echo "ej: https://wa.me/525500000000?text=..." >>
      projects/m17-vitrina/docs/integracion-whatsapp.md

      git add projects/m17-vitrina

      git commit -m "feat(m17): L18 pedido whatsapp wa.me"

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Botón abre `wa.me` con ítems del carrito/pedido de prueba.
      - Evidencia en `integracion-whatsapp.md` (teléfono demo/redactado).
      - 'Commit `feat(m17): L18 pedido whatsapp wa.me`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L18 — Botón pedido WhatsApp desde el perfil / ficha

**~5.0 h · Semana 5**

Cierra el loop del comensal: ve el menú → arma mensaje → abre WhatsApp.

## Objetivo

En el perfil público (o preview), acción que abre `wa.me` con el pedido prefijado (ítems + total + “pago al recoger”).

## Conceptos clave

- deep-link `wa.me`
- mensaje prefijado
- sin WhatsApp Business API en v1

## Pasos (hazlos en orden)

### 1. Generar texto del pedido (40 min)

Función pura: lista de líneas → string URL-encoded. Ejemplo:

`Hola, quiero pedir:%0A- 2x Matcha latte%0ATotal: $130%0APago al recoger.`

### 2. Botón en UI (70–90 min)

Acción “Pedir por WhatsApp” hace `window.open` a `https://wa.me/<telefonoNegocio>?text=...`. No requiere WhatsApp Business API.

### 3. Evidencia (30 min)

```bash
echo "ej: https://wa.me/525500000000?text=..." >> projects/m17-vitrina/docs/integracion-whatsapp.md
git add projects/m17-vitrina
git commit -m "feat(m17): L18 pedido whatsapp wa.me"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| producto-saas | Pedido WhatsApp MVP | [producto-saas](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Botón abre `wa.me` con ítems del carrito/pedido de prueba.
2. Evidencia en `integracion-whatsapp.md` (teléfono demo/redactado).
3. Commit `feat(m17): L18 pedido whatsapp wa.me`.

## Errores comunes

- Exigir API oficial de WhatsApp en el piloto.
- Mandar el teléfono del cliente en la URL (el link es al negocio).

## Siguiente

[L19 — Confirmación de pedido y estados](L19-confirmacion-de-pedido-y-estados.md)
