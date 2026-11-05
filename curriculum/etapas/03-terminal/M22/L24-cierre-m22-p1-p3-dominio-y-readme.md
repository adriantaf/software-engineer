---
id: L24
materia: M22
orden: 24
titulo: 'Cierre M22 — P1–P3, dominio y README'
horas: 5
semana: 6
lectura: Repaso ficha M22
evidencia: projects/m22-bektor/cierre-m22.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras venta consultiva antes de IA aplicada (M23).


      Conceptos que debes poder explicar al cerrar:


      - Evidencia.

      - Dominio.

      - Honestidad bitácora.

      - Handoff M23.


      **Objetivo de esta lección:** Auditar oferta, 10 demos, pricing, pivote;
      responder checklist dominio; commit cierre.


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
      git commit -m "docs(m22): l24 cierre-m22-p1-p3-dominio-y-readme"
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
      git commit -m "docs(m22): l24 cierre-m22-p1-p3-dominio-y-readme"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M22 — P1–P3, dominio y README», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M22 — P1–P3,
          dominio y README
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
          Auditar oferta, 10 demos, pricing, pivote; responder checklist
          dominio; commit cierre.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M22
    xp: 25
    enunciado: >-
      Cierra **Emprendimiento de negocios de software** con evidencia real en el
      repo. Marca la rúbrica solo si puedes demostrar cada criterio (si no está
      en git, no cuenta).
    entregables:
      - 'P1: Oferta SaaS de UN solo producto (suscripción, no agencia)'
      - 'P2: 10 demos/trials a negocios reales documentadas'
      - 'P3: Pricing MXN (Free/Pro) + propuesta escrita'
      - 'Proyecto: Bektor pivoteado a Vitrina (SaaS)'
      - projects/m22-bektor/cierre-m22.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: 'Existe el entregable: `projects/m22-bektor/cierre-m22.md`.'
      - id: r3
        criterio: cierre-m22.md.
      - id: r4
        criterio: Commit cierre.
      - id: r5
        criterio: README L01–L24.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/cierre-m22.md`.'
      - cierre-m22.md.
      - Commit cierre.
      - README L01–L24.
    siguiente: Materia M22 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L24 — Cierre M22 — P1–P3, dominio y README

**~5 h · Semana 6**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/cierre-m22.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Auditar oferta, 10 demos, pricing, pivote; responder checklist dominio; commit cierre.

## Por qué empieza así

Cierras venta consultiva antes de IA aplicada (M23).

Conceptos que debes poder explicar al cerrar:

- Evidencia.
- Dominio.
- Honestidad bitácora.
- Handoff M23.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Repaso ficha M22_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

`projects/m22-bektor/cierre-m22.md` checklist P1–P3 + proyecto. Verifica ICP único 6 semanas.

### 3. Laboratorio principal (90–120 min)

Commit `docs(m22): cierre materia`. README con índice L01–L24.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l24 cierre-m22-p1-p3-dominio-y-readme"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Repaso ficha M22 | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/cierre-m22.md`.
2. cierre-m22.md.
3. Commit cierre.
4. README L01–L24.

## Errores comunes

- Marcar UI sin 10 demos.
- Inflar métricas.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
