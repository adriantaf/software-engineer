---
id: L01
materia: M26
orden: 1
titulo: Alcance SaaS v1 congelado
horas: 5.0
semana: 1
lectura: producto-saas.md completo + egreso.md
evidencia: projects/m26-capstone/alcance.md
---

# L01 — Alcance SaaS v1 congelado

**~5 h · Semana 1**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/alcance.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Congelar por escrito el alcance SaaS v1 de Agenda Ops (in/out) alineado a producto-saas y rúbrica de egreso.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- MVP vs v1.1
- In/out scope
- Congelar

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _producto-saas.md completo + egreso.md_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Crea estructura capstone (20–30 min)

```bash
mkdir -p projects/m26-capstone/{memoria,demos,bitacora}
```

Copia mentalmente [producto-saas](../../../producto-saas.md) y [egreso](../../../egreso.md) al lado.

### 3. Congela alcance.md (100–130 min)

`alcance.md` con secciones: **In scope v1**, **Out of scope**, **Dependencias** (M17/M19/M22/M25), **Criterios de egreso que toca**.

≥8 bullets in, ≥5 out. Nada de “tal vez WhatsApp” sin decidir.

### 4. Bitácora semana 1 (20–30 min)

`bitacora/semana-01.md`: horas plan vs real; 1 riesgo que ya ves.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m26): l01 alcance-saas-v1-congelado"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | producto-saas.md completo + egreso.md | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/alcance.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L02 — Plan 8 semanas y egreso-checklist honesto](L02-plan-8-semanas-y-egreso-checklist-honesto.md)
