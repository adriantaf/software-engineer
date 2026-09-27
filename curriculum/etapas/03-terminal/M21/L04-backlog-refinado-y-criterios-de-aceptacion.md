---
id: L04
materia: M21
orden: 4
titulo: Backlog refinado y criterios de aceptación
horas: 5.0
semana: 1
lectura: Scrum Guide — refinamiento del Product Backlog
evidencia: projects/m21-proyectos/roadmap-trimestre.md sección backlog
---

# L04 — Backlog refinado y criterios de aceptación

**~5 h · Semana 1**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/roadmap-trimestre.md sección backlog`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Refinar las historias del backlog: criterios de aceptación testeables y tamaño ≤ un sprint para las top 5.

## Por qué empieza así

Cierras semana 1 con P1 casi listo: el roadmap debe ser ejecutable, no aspiracional.

Conceptos que debes poder explicar al cerrar:

- Historia de usuario.
- Criterio Given/When/Then.
- INVEST (selecto).
- Deuda etiquetada.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Scrum Guide — refinamiento del Product Backlog_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos`.

Para las **5 issues** prioritarias añade en el issue (o anexo `projects/m21-proyectos/backlog-refinado.md`) criterios de aceptación numerados.

### 3. Laboratorio principal (90–120 min)

Verifica que cada criterio sea **observable** (URL, test, archivo). Etiqueta deuda técnica explícita.

### 4. Endurece el entregable (40–60 min)

Retro semana 1 en `bitacora-m21.md`: estimación inicial en rangos (optimista/realista/pesimista) para la issue #1.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l04 backlog-refinado-y-criterios-de-aceptaci"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Scrum Guide — refinamiento del Product Backlog | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/roadmap-trimestre.md sección backlog`.
2. 5 historias con criterios.
3. Retro semana 1 escrita.
4. P1 roadmap revisable.
5. Commit `docs(m21): l04 …` en el historial.

## Errores comunes

- Criterios ‘funciona bien’.
- Historias gigantes multi-sprint sin split.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L05 — Sprint planning — meta única del sprint 1](L05-sprint-planning-meta-unica-del-sprint-1.md)
