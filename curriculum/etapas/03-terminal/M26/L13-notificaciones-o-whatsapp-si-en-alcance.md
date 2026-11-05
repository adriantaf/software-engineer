---
id: L13
materia: M26
orden: 13
titulo: Pedido WhatsApp y pago al recoger (perfil)
horas: 5
semana: 4
lectura: producto-saas — pedido WA + flag pago online
evidencia: projects/m26-capstone/integraciones.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Capstone: SaaS multi-tenant en producción. Hoy entregas
      **`projects/m26-capstone/integraciones.md`**.


      **Objetivo de esta lección:** Perfil público del tenant: menú + botón
      **Pedir por WhatsApp** (`wa.me`) con mensaje prefijado; default **pago al
      recoger**. Documenta el flag futuro/activo de checkout online.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Spec en integraciones.md
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m26-capstone/integraciones.md
      git commit -m "docs(m26): l13 pedido whatsapp perfil"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementa / verifica deep-link
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m26-capstone/integraciones.md
      git commit -m "docs(m26): l13 pedido whatsapp perfil"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pedido WhatsApp y pago al recoger (perfil)», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Al menos 1 tenant demo con pedido WA reproducible.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pedido WhatsApp y pago
          al recoger (perf…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git add projects/m26-capstone/integraciones.md`
    comandoEsperado:
      - git add projects/m26-capstone/integraciones.md
      - 'git commit -m "docs(m26): l13 pedido whatsapp perfil"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m26-capstone/integraciones.md'
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
          Perfil público del tenant: menú + botón Pedir por WhatsApp (`wa.me`)
          con mensaje prefijado; default pago al recoger. Documenta el flag
          futuro/activo de checkou…
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m26-capstone/integraciones.md
      git commit -m "docs(m26): l13 pedido whatsapp perfil"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Al menos 1 tenant demo con pedido WA reproducible.
      - '`integraciones.md` describe pago al recoger vs online.'
      - Commit en git.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — Pedido WhatsApp y pago al recoger (perfil)

**~5 h · Semana 4**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/integraciones.md`**.

## Objetivo

Perfil público del tenant: menú + botón **Pedir por WhatsApp** (`wa.me`) con mensaje prefijado; default **pago al recoger**. Documenta el flag futuro/activo de checkout online.

## Pasos (hazlos en orden)

### 1. Spec en integraciones.md (40 min)

Tabla por tenant: teléfono WA, plantilla de mensaje, pago default, ¿checkout online activado?

### 2. Implementa / verifica deep-link (90–120 min)

- Genera `https://wa.me/<tel>?text=` con ítems + total.
- Sin WhatsApp Business API en v1.
- Si el tenant tiene `pago_online=true`, documenta enlace a Stripe Checkout (L17–L19); si no, solo al recoger.

### 3. Commit (15 min)

```bash
git add projects/m26-capstone/integraciones.md
git commit -m "docs(m26): l13 pedido whatsapp perfil"
```

## Hecho cuando

1. Al menos 1 tenant demo con pedido WA reproducible.
2. `integraciones.md` describe pago al recoger vs online.
3. Commit en git.

## Errores comunes

- Exigir API oficial de WhatsApp para egreso.
- Mezclar el teléfono del comensal con el del negocio en `wa.me`.

## Siguiente

[L14 — App móvil M20 conectada o plan cierre](L14-app-movil-m20-conectada-o-plan-cierre.md)
