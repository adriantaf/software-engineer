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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Perfil público del tenant: menú + botón **Pedir por
      WhatsApp** (`wa.me`) con mensaje prefijado; default **pago al recoger**.
      Documenta el flag futuro/activo de checkout online.


      Capstone: SaaS multi-tenant en producción. Hoy entregas
      **`projects/m26-capstone/integraciones.md`**.
  - id: s2
    tipo: ejemplo
    titulo: 1. Spec en integraciones.md
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m26-capstone/integraciones.md
      git commit -m "docs(m26): l13 pedido whatsapp perfil"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Pedido WhatsApp y pago al recoger (perfil)" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/integraciones.md
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
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/m26-capstone/integraciones.md`
    comandoEsperado:
      - git add projects/m26-capstone/integraciones.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m26-capstone/integraciones.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Perfil público del tenant: menú + botón **Pedir por WhatsApp**
          (`wa.me`) con mensaje prefijado; default **pago al recoger**.
          Documenta el f…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementa / verifica deep-link
    xp: 10
    cuerpo: >-
      - Genera `https://wa.me/<tel>?text=` con ítems + total.

      - Sin WhatsApp Business API en v1.

      - Si el tenant tiene `pago_online=true`, documenta enlace a Stripe
      Checkout (L17–L19); si no, solo al recoger.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
