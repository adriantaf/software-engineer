---
id: L01
materia: M21
orden: 1
titulo: 'Entorno M21, Scrum de uno y Definition of Done'
horas: 5
semana: 1
lectura: Guía Scrum 2020 (ES) — roles y eventos
evidencia: projects/m21-proyectos/definition-of-done.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear la carpeta de evidencia, leer Scrum adaptado a un solo
      dev-owner y redactar Definition of Done usable en issues reales de
      Vitrina.


      Sin DoD escrito cierras issues con ‘ya quedó’; M22 y M26 dependen de un
      backlog honesto del mismo repo producto.


      Conceptos que debes poder explicar al cerrar:


      - Product Owner de uno.

      - Sprint de 1–2 semanas.

      - DoD con PR, test, doc.

      - Backlog ≠ lista de deseos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m21-proyectos/sprints
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Entorno M21, Scrum de uno y Definition of Done" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m21-proyectos/definition-of-done.md
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

      `mkdir -p projects/m21-proyectos/sprints`
    comandoEsperado:
      - mkdir -p projects/m21-proyectos/sprints
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m21-proyectos/sprints'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Crear la carpeta de evidencia, leer Scrum adaptado a un solo dev-owner
          y redactar Definition of Done usable en issues reales de Vitrina.
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
      ```bash
      mkdir -p projects/m21-proyectos/sprints
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      En `projects/m21-proyectos/definition-of-done.md` define checklist mínima:
      PR revisado (o self-review documentado), tests/CI cuando aplique, doc en
      `projects/` si la materia lo pide, staging si es deploy. Incluye **un ítem
      de seguridad** (ej. no secretos en git).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m21-proyectos/definition-of-done.md`.'
      - DoD ≥6 ítems verificables.
      - bitacora-m21.md con roles adaptados.
      - Commit docs(m21).
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L01 — Entorno M21, Scrum de uno y Definition of Done

**~5 h · Semana 1**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/definition-of-done.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Crear la carpeta de evidencia, leer Scrum adaptado a un solo dev-owner y redactar Definition of Done usable en issues reales de Vitrina.

## Por qué empieza así

Sin DoD escrito cierras issues con ‘ya quedó’; M22 y M26 dependen de un backlog honesto del mismo repo producto.

Conceptos que debes poder explicar al cerrar:

- Product Owner de uno.
- Sprint de 1–2 semanas.
- DoD con PR, test, doc.
- Backlog ≠ lista de deseos.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Guía Scrum 2020 (ES) — roles y eventos_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

```bash
mkdir -p projects/m21-proyectos/sprints
```

### 3. Laboratorio principal (90–120 min)

En `projects/m21-proyectos/definition-of-done.md` define checklist mínima: PR revisado (o self-review documentado), tests/CI cuando aplique, doc en `projects/` si la materia lo pide, staging si es deploy. Incluye **un ítem de seguridad** (ej. no secretos en git).

### 4. Endurece el entregable (40–60 min)

Añade `projects/m21-proyectos/bitacora-m21.md` con párrafo: cómo mapeas roles Scrum cuando eres solo tú + mentor ocasional.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l01 entorno-m21-scrum-de-uno-y-definition-of"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Guía Scrum 2020 (ES) — roles y eventos | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/definition-of-done.md`.
2. DoD ≥6 ítems verificables.
3. bitacora-m21.md con roles adaptados.
4. Commit docs(m21).

## Errores comunes

- DoD genérico ‘código limpio’.
- Ignorar ítem seguridad.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L02 — Milestones y cinco issues reales del producto](L02-milestones-y-cinco-issues-reales-del-producto.md)
