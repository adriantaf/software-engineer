---
id: L05
materia: M21
orden: 5
titulo: Sprint planning — meta única del sprint 1
horas: 5.0
semana: 2
lectura: Scrum Guide — Sprint Planning
evidencia: projects/m21-proyectos/sprints/sprint-01.md
---

# L05 — Sprint planning — meta única del sprint 1

**~5 h · Semana 2**

Agenda Ops se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/sprints/sprint-01.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Planificar sprint 1 con **una meta** clara, WIP limitado y lista de entregables enlazados a issues.

## Por qué empieza así

Multi-tasking sin meta única es la causa #1 de carry-over; M21 te entrena a decir no.

Conceptos que debes poder explicar al cerrar:

- Meta de sprint.
- WIP.
- Compromiso realista.
- Definition of Done aplicada.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Scrum Guide — Sprint Planning_.

Subraya 3–5 frases que puedas aplicar en Agenda Ops (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos/sprints`.

Crea `projects/m21-proyectos/sprints/sprint-01.md` con plantilla de la ficha (fechas, meta, tabla Planeado/Hecho/Aprendizaje vacía).

### 3. Laboratorio principal (90–120 min)

Elige **1 meta** (ej. ‘segundo tenant en staging + 1 test cross-tenant’). Máximo **3 issues** en progreso.

### 4. Endurece el entregable (40–60 min)

Documenta estimación **24–32 h** (rango) y riesgos del sprint (1 párrafo).

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l05 sprint-planning-meta-nica-del-sprint-1"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Scrum Guide — Sprint Planning | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/sprints/sprint-01.md`.
2. sprint-01.md con meta única.
3. ≤3 issues WIP.
4. Rango horas documentado.
5. Commit `docs(m21): l05 …` en el historial.

## Errores comunes

- Meta lista de 10 verbos.
- Sin fechas de sprint.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L06 — Ejecutar sprint 1 y registro honesto](L06-ejecutar-sprint-1-y-registro-honesto.md)
