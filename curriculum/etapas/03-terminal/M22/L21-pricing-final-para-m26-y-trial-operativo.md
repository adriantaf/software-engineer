---
id: L21
materia: M22
orden: 21
titulo: Pricing final para M26 y trial operativo
horas: 5
semana: 6
lectura: Stripe docs (preview) + pricing.md
evidencia: projects/m22-bektor/pricing.md final
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Semana 6 cierra comercial de la materia con números estables.


      Conceptos que debes poder explicar al cerrar:


      - Price freeze.

      - Trial 14d.

      - Límites.

      - Handoff M26.


      **Objetivo de esta lección:** Congelar pricing Free/Pro MXN para
      integración Stripe test en M26; checklist trial operativo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l21 pricing-final-para-m26-y-trial-operativo"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l21 pricing-final-para-m26-y-trial-operativo"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pricing final para M26 y trial operativo», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pricing final para M26
          y trial operativo
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
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
          Congelar pricing Free/Pro MXN para integración Stripe test en M26;
          checklist trial operativo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Laboratorio principal
    xp: 10
    cuerpo: >-
      Lista checklist trial: alta tenant, credenciales, soporte WhatsApp,
      activación medida.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/pricing.md final`.'
      - Pricing congelado fechado.
      - Checklist trial.
      - P3 listo para UI.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L21 — Pricing final para M26 y trial operativo

**~5 h · Semana 6**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/pricing.md final`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Congelar pricing Free/Pro MXN para integración Stripe test en M26; checklist trial operativo.

## Por qué empieza así

Semana 6 cierra comercial de la materia con números estables.

Conceptos que debes poder explicar al cerrar:

- Price freeze.
- Trial 14d.
- Límites.
- Handoff M26.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Stripe docs (preview) + pricing.md_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Marca `projects/m22-bektor/pricing.md` sección **Final M22** con fecha congelación.

### 3. Laboratorio principal (90–120 min)

Lista checklist trial: alta tenant, credenciales, soporte WhatsApp, activación medida.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l21 pricing-final-para-m26-y-trial-operativo"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Stripe docs (preview) + pricing.md | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/pricing.md final`.
2. Pricing congelado fechado.
3. Checklist trial.
4. P3 listo para UI.
5. Commit `docs(m22): l21 …` en el historial.

## Errores comunes

- Cambiar precio post-cierre sin nota.
- Trial sin proceso.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L22 — Síntesis comercial para backlog M21](L22-sintesis-comercial-para-backlog-m21.md)
