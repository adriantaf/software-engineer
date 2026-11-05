---
id: L32
materia: M26
orden: 32
titulo: Cierre integrador y handoff v1.1
horas: 5
semana: 8
lectura: retrospectiva 8 semanas
evidencia: projects/m26-capstone/cierre.md
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


      - Aprendizaje

      - Mantenimiento


      **Objetivo de esta lección:** Cierre integrador + handoff v1.1 (qué sigue,
      qué no).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l32 cierre-integrador-y-handoff-v1-1"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Carta de cierre
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l32 cierre-integrador-y-handoff-v1-1"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre integrador y handoff v1.1», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre integrador y
          handoff v1.1
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
        texto: 'Cierre integrador + handoff v1.1 (qué sigue, qué no).'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M26
    xp: 25
    enunciado: >-
      Cierra **Proyecto integrador / titulación interna** con evidencia real en
      el repo. Marca la rúbrica solo si puedes demostrar cada criterio (si no
      está en git, no cuenta).
    entregables:
      - 'P1: Alcance SaaS congelado + plan de 8 semanas'
      - 'P2: Memoria técnica del SaaS v1'
      - 'P3: Demo pública / video del producto multi-tenant'
      - 'Proyecto: Vitrina SaaS en producción + egreso'
      - projects/m26-capstone/cierre.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: Existe `projects/m26-capstone/cierre.md`.
      - id: r3
        criterio: Commit en git con mensaje docs(m26).
      - id: r4
        criterio: Bitácora de la semana actualizada.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/cierre.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Materia M26 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L32 — Cierre integrador y handoff v1.1

**~5 h · Semana 8**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/cierre.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Cierre integrador + handoff v1.1 (qué sigue, qué no).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Aprendizaje
- Mantenimiento

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _retrospectiva 8 semanas_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Carta de cierre (30–40 min)

En `projects/m26-capstone/cierre.md`: qué es Vitrina hoy (3 párrafos), para quién, URL.

### 3. Handoff v1.1 (90–110 min)

Secciones: **Operar en prod** (checklist semanal), **Backlog v1.1**, **Riesgos residuales**, **Aprendizajes**.

Enlaza runbook y post-mortem.

### 4. Última bitácora (20–30 min)

`bitacora/semana-08.md`: horas totales del capstone (estimadas) + una frase de cierre.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l32 cierre-integrador-y-handoff-v1-1"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | retrospectiva 8 semanas | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/cierre.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
