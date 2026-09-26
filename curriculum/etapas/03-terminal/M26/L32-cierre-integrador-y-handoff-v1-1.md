---
id: L32
materia: M26
orden: 32
titulo: Cierre integrador y handoff v1.1
horas: 5.0
semana: 8
lectura: retrospectiva 8 semanas
evidencia: projects/m26-capstone/cierre.md
---

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

En `projects/m26-capstone/cierre.md`: qué es Agenda Ops hoy (3 párrafos), para quién, URL.

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
