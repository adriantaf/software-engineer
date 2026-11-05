---
id: L20
materia: M26
orden: 20
titulo: Webhooks Stripe verificados en deploy
horas: 5
semana: 5
lectura: Signing secret
evidencia: projects/m26-capstone/memoria/webhooks-stripe.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Idempotencia

      - Replay


      **Objetivo de esta lección:** Webhooks Stripe verificados en deploy (firma
      + idempotencia básica).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      # ejemplo Stripe CLI — solo test mode
      stripe listen --forward-to localhost:3000/api/webhooks/stripe
      stripe trigger checkout.session.completed
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Endpoint webhook en deploy
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l20 webhooks-stripe-verificados-en-deploy"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Webhooks Stripe verificados en deploy», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Webhooks Stripe
          verificados en deploy
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

      `git add projects/`
    comandoEsperado:
      - git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/'
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
        texto: Webhooks Stripe verificados en deploy (firma + idempotencia básica).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Verifica firma e idempotencia
    xp: 10
    cuerpo: >-
      Confirma verificación de firma Stripe en código desplegado. Prueba evento
      (CLI o dashboard): Documenta: replay del mismo event id no duplica side
      effects.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/memoria/webhooks-stripe.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Webhooks Stripe verificados en deploy

**~5 h · Semana 5**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/webhooks-stripe.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Webhooks Stripe verificados en deploy (firma + idempotencia básica).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Idempotencia
- Replay

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Signing secret_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Endpoint webhook en deploy (30–40 min)

En `projects/m26-capstone/memoria/webhooks-stripe.md`: URL pública staging/prod, eventos suscritos (`checkout.session.completed`, etc.).

### 3. Verifica firma e idempotencia (100–120 min)

Confirma verificación de firma Stripe en código desplegado. Prueba evento (CLI o dashboard):

```bash
# ejemplo Stripe CLI — solo test mode
stripe listen --forward-to localhost:3000/api/webhooks/stripe
stripe trigger checkout.session.completed
```

Documenta: replay del mismo event id no duplica side effects.

### 4. Logs seguros (25–35 min)

Qué se loguea (tipo evento, id) y qué no (PAN). Bitácora semana-05.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l20 webhooks-stripe-verificados-en-deploy"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Signing secret | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/webhooks-stripe.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L21 — Re-ejecutar review M25 y cerrar gaps](L21-re-ejecutar-review-m25-y-cerrar-gaps.md)
