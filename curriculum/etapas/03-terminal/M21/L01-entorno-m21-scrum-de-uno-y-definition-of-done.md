---
id: L01
materia: M21
orden: 1
titulo: Entorno M21, Scrum de uno y Definition of Done
horas: 5.0
semana: 1
lectura: Guía Scrum 2020 (ES) — roles y eventos
evidencia: projects/m21-proyectos/definition-of-done.md
---

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
