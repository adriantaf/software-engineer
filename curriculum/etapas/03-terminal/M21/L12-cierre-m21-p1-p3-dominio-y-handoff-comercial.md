---
id: L12
materia: M21
orden: 12
titulo: Cierre M21 — P1–P3, dominio y handoff comercial
horas: 5.0
semana: 3
lectura: Repaso ficha M21 criterios de dominio
evidencia: projects/m21-proyectos/cierre-m21.md
---

# L12 — Cierre M21 — P1–P3, dominio y handoff comercial

**~5 h · Semana 3**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/cierre-m21.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Auditar evidencias P1–P3, tablero, cuatro sprints y redactar handoff a M22 (trials) y M23 (métricas).

## Por qué empieza así

Cierras la materia de gestión antes de vender (M22) y medir con IA (M23).

Conceptos que debes poder explicar al cerrar:

- Checklist evidencia.
- Pitch interno 5 min roadmap.
- Handoff.
- Riesgo residual.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Repaso ficha M21 criterios de dominio_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos`.

Crea `projects/m21-proyectos/cierre-m21.md`: checklist P1–P3 + proyecto tablero; responde criterios dominio de la ficha.

### 3. Laboratorio principal (90–120 min)

Graba guion (texto) de **5 min** explicando roadmap a persona no técnica.

### 4. Endurece el entregable (40–60 min)

Commit `docs(m21): cierre materia`. Actualiza `projects/m21-proyectos/README.md` con índice L01–L12.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l12 cierre-m21-p1-p3-dominio-y-handoff-comer"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Repaso ficha M21 criterios de dominio | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/cierre-m21.md`.
2. cierre-m21.md completo.
3. README índice.
4. Commit cierre.
5. Handoff M22/M23.

## Errores comunes

- Marcar UI sin archivos.
- Roadmap desalineado del board.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
