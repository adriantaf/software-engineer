---
id: L29
materia: M26
orden: 29
titulo: Video demo público multi-tenant
horas: 5.0
semana: 8
lectura: guion demo
evidencia: projects/m26-capstone/demo.md
---

# L29 — Video demo público multi-tenant

**~5 h · Semana 8**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/demo.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Video demo público multi-tenant (sin tutorial de fondo).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- YouTube/Loom
- Sin tutorial fondo

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _guion demo_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Guion del video (40–50 min)

`demo.md`: guion ≤8 min — login A, cita, login B, prueba de aislamiento, pricing/checkout test, cierre.

### 3. Graba (90–120 min)

Graba pantalla (Loom/OBS). Sin tutorial de terceros de fondo. URLs de staging/prod reales.

### 4. Publica enlace (20–30 min)

Enlace unlisted/público en `demo.md` + duración + fecha. Si el video es privado, no cuenta para egreso.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m26): l29 video-demo-p-blico-multi-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | guion demo | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/demo.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L30 — Checklist egreso con evidencia enlazada](L30-checklist-egreso-con-evidencia-enlazada.md)
