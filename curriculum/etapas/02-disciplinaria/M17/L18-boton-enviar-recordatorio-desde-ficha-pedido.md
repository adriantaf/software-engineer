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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** En el perfil público (o preview), acción que abre `wa.me`
      con el pedido prefijado (ítems + total + “pago al recoger”).


      - deep-link `wa.me`

      - mensaje prefijado

      - sin WhatsApp Business API en v1
  - id: s2
    tipo: ejemplo
    titulo: 1. Generar texto del pedido
    xp: 10
    cuerpo: >-
      ```bash

      echo "ej: https://wa.me/525500000000?text=..." >>
      projects/m17-vitrina/docs/integracion-whatsapp.md

      git add projects/m17-vitrina

      git commit -m "feat(m17): L18 pedido whatsapp wa.me"

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Botón pedido WhatsApp desde el perfil / ficha" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: acción pedido WhatsApp
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `echo "ej: https://wa.me/525500000000?text=..." >>
      projects/m17-vitrina/docs/integracion-whatsapp.md`
    comandoEsperado:
      - >-
        echo "ej: https://wa.me/525500000000?text=..." >>
        projects/m17-vitrina/docs/integracion-whatsapp.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: echo "ej: https://wa.me/525500000000?text=..." >>
      projects/m17-vitrina/docs/integracion-whatsapp.md
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          En el perfil público (o preview), acción que abre `wa.me` con el
          pedido prefijado (ítems + total + “pago al recoger”).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Botón en UI
    xp: 10
    cuerpo: >-
      Acción “Pedir por WhatsApp” hace `window.open` a
      `https://wa.me/<telefonoNegocio>?text=...`. No requiere WhatsApp Business
      API.
  - id: s7
    tipo: ejemplo
    titulo: 3. Evidencia
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
