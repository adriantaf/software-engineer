---
id: L03
materia: M21
orden: 3
titulo: Roadmap trimestral alineado a producto-saas
horas: 5.0
semana: 1
lectura: producto-saas.md — piloto → tenants → billing
evidencia: projects/m21-proyectos/roadmap-trimestre.md
---

# L03 — Roadmap trimestral alineado a producto-saas

**~5 h · Semana 1**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/roadmap-trimestre.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Redactar roadmap de un trimestre con 3–5 objetivos medibles de Vitrina (multi-tenant, staging estable, trials, handoff M23).

## Por qué empieza así

P1 exige un documento que un mentor pueda cuestionar; debe reflejar [producto-saas](../../../producto-saas.md), no features al azar.

Conceptos que debes poder explicar al cerrar:

- Outcome vs output.
- Dependencia M22/M26.
- Design partner.
- Corte explícito (MoSCoW).

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _producto-saas.md — piloto → tenants → billing_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos`.

En `projects/m21-proyectos/roadmap-trimestre.md`:

### 3. Laboratorio principal (90–120 min)

- **Visión 90 días** (3–5 bullets).
- Tabla objetivos: **qué**, **por qué ahora**, **métrica**, **issue/milestone** enlazado.
- Sección **No haremos este trimestre** (≥3 ítems) para combatir scope creep.

### 4. Endurece el entregable (40–60 min)

Relee [producto-saas.md](../../../producto-saas.md) y marca qué objetivo habilita trials comerciales y qué habilita FAQ por tenant.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l03 roadmap-trimestral-alineado-a-producto-s"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | producto-saas.md — piloto → tenants → billing | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/roadmap-trimestre.md`.
2. roadmap con 3–5 objetivos.
3. Tabla con métricas.
4. Sección ‘no haremos’.
5. Commit `docs(m21): l03 …` en el historial.

## Errores comunes

- 40 features sin orden.
- Roadmap sin enlace a milestones.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L04 — Backlog refinado y criterios de aceptación](L04-backlog-refinado-y-criterios-de-aceptacion.md)
