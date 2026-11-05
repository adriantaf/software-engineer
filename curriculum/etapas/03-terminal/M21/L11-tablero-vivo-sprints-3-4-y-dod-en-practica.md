---
id: L11
materia: M21
orden: 11
titulo: 'Tablero vivo, sprints 3–4 y DoD en práctica'
horas: 5
semana: 3
lectura: Scrum Guide — transparencia del incremento
evidencia: projects/m21-proyectos/sprints/sprint-03.md + sprint-04.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Actualizar board.md, esbozar sprints 3–4 y cerrar ≥3 issues
      con DoD completa.


      El proyecto de la materia es un tablero que refleja la realidad del SaaS,
      no un ejercicio.


      Conceptos que debes poder explicar al cerrar:


      - Transparencia.

      - Issues zombie.

      - Handoff M22.

      - Incremento demoable.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m21): l11 tablero-vivo-sprints-3-4-y-dod-en-pr-cti"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tablero vivo, sprints 3–4 y DoD en práctica" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m21-proyectos/sprints/sprint-03.md + sprint-04.md
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Actualizar board.md, esbozar sprints 3–4 y cerrar ≥3 issues con DoD
          completa.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      Confirma rutas bajo `projects/m21-proyectos/sprints`.

      Actualiza `projects/m21-proyectos/board.md` (fecha ≤7 días).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Crea `projects/m21-proyectos/sprints/sprint-03.md` y `sprint-04.md` con
      meta y al menos encabezado de tabla (pueden solapar semanas calendario si
      ya iterabas).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m21-proyectos/sprints/sprint-03.md +
        sprint-04.md`.
      - board.md reciente.
      - sprint-03/04 existen.
      - ≥3 issues con DoD.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — Tablero vivo, sprints 3–4 y DoD en práctica

**~5 h · Semana 3**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/sprints/sprint-03.md + sprint-04.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Actualizar board.md, esbozar sprints 3–4 y cerrar ≥3 issues con DoD completa.

## Por qué empieza así

El proyecto de la materia es un tablero que refleja la realidad del SaaS, no un ejercicio.

Conceptos que debes poder explicar al cerrar:

- Transparencia.
- Issues zombie.
- Handoff M22.
- Incremento demoable.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Scrum Guide — transparencia del incremento_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos/sprints`.

Actualiza `projects/m21-proyectos/board.md` (fecha ≤7 días).

### 3. Laboratorio principal (90–120 min)

Crea `projects/m21-proyectos/sprints/sprint-03.md` y `sprint-04.md` con meta y al menos encabezado de tabla (pueden solapar semanas calendario si ya iterabas).

### 4. Endurece el entregable (40–60 min)

Añade al backlog issues etiquetados **demo-comercial** para M22. Cierra ≥3 issues con DoD.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l11 tablero-vivo-sprints-3-4-y-dod-en-pr-cti"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Scrum Guide — transparencia del incremento | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/sprints/sprint-03.md + sprint-04.md`.
2. board.md reciente.
3. sprint-03/04 existen.
4. ≥3 issues con DoD.
5. Issues demo M22.

## Errores comunes

- Board sin URL.
- Sprints sin fechas ni meta.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L12 — Cierre M21 — P1–P3, dominio y handoff comercial](L12-cierre-m21-p1-p3-dominio-y-handoff-comercial.md)
