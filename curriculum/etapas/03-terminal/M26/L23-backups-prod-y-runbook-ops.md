---
id: L23
materia: M26
orden: 23
titulo: Backups prod y runbook ops
horas: 5.0
semana: 6
lectura: M19 runbook
evidencia: projects/m26-capstone/memoria/ops.md
---

# L23 — Backups prod y runbook ops

**~5 h · Semana 6**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/ops.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Backups prod + restore documentado en runbook ops.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- RTO/RPO honesto
- Restore

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _M19 runbook_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Estado de backups (25–35 min)

En `projects/m26-capstone/memoria/ops.md`: última fecha de backup, retención, enlace a restore-test M25.

### 3. Runbook ops corto (100–120 min)

Secciones: deploy, rollback, restore, rotar secreto, escalación. Comandos reales de **tu** stack:

```bash
# plantilla — sustituye por tus comandos reales
# deploy: …
# rollback: …
# restore dry-run: …
```

Incluye RTO/RPO honestos.

### 4. Fecha de próxima prueba restore (20–30 min)

Agenda en el doc. Bitácora semana-06.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l23 backups-prod-y-runbook-ops"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | M19 runbook | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/ops.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L24 — Hardening final pre-demo pública](L24-hardening-final-pre-demo-publica.md)
