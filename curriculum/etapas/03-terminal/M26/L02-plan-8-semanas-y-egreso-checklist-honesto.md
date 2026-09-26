---
id: L02
materia: M26
orden: 2
titulo: Plan 8 semanas y egreso-checklist honesto
horas: 5.0
semana: 1
lectura: egreso.md rúbrica
evidencia: projects/m26-capstone/plan-8-semanas.md
---

# L02 — Plan 8 semanas y egreso-checklist honesto

**~5 h · Semana 1**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/plan-8-semanas.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Publicar plan de 8 semanas con hitos semanales y checklist de egreso honesto (gaps visibles).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Sprint semanal
- Demo interna
- Riesgos

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _egreso.md rúbrica_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Esqueleto de 8 sprints (30–40 min)

En `projects/m26-capstone/plan-8-semanas.md` tabla:

| Semana | Entregable | Demo | Riesgo |
|--------|------------|------|--------|

Una fila por semana 1–8. Fechas reales.

### 3. Checklist de egreso honesto (90–110 min)

Crea/actualiza `projects/m26-capstone/egreso-checklist.md` copiando ítems de [egreso](../../../egreso.md).

Columnas: ítem | estado (hecho/parcial/no) | evidencia (path/URL) | gap.

Marca en rojo lo que aún es “no” — sin autoengaño.

### 4. Bitácora semana 1 (20–30 min)

`bitacora/semana-01.md`: horas plan vs real; 1 dependencia bloqueante.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l02 plan-8-semanas-y-egreso-checklist-honest"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | egreso.md rúbrica | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/plan-8-semanas.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L03 — Modelo tenant_id y resolución de tenant](L03-modelo-tenant-id-y-resolucion-de-tenant.md)
