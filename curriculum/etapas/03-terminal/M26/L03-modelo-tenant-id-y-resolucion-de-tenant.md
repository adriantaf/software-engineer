---
id: L03
materia: M26
orden: 3
titulo: Modelo tenant_id y resolución de tenant
horas: 5.0
semana: 1
lectura: ADRs tenancy del repo
evidencia: projects/m26-capstone/memoria/tenancy-modelo.md
---

# L03 — Modelo tenant_id y resolución de tenant

**~5 h · Semana 1**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/tenancy-modelo.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Documentar modelo `tenant_id`, resolución de tenant (subdominio/header/sesión) y límites de confianza.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Row-level
- Subdomain vs header
- Middleware

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _ADRs tenancy del repo_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Prepara carpetas (15–25 min)

```bash
mkdir -p projects/m26-capstone/memoria
```

Confirma que escribirás `projects/m26-capstone/memoria/tenancy-modelo.md`.

### 3. Laboratorio principal (100–130 min)

```bash
mkdir -p projects/m26-capstone/memoria projects/m26-capstone/demos projects/m26-capstone/bitacora
```

Documenta cómo se resuelve tenant en API y UI. Diagrama request → tenant context.

Registra horas y bloqueos en `projects/m26-capstone/bitacora/semana-01.md`.

### 4. Criterio de calidad (30–45 min)

Relee `projects/m26-capstone/memoria/tenancy-modelo.md`: ¿un mentor externo entendería el resultado sin preguntarte?

Añade enlace a issue/PR/URL de staging si aplica. Bitácora de la semana: 5 líneas de horas y bloqueos.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m26): l03 modelo-tenant-id-y-resoluci-n-de-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | ADRs tenancy del repo | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/tenancy-modelo.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L04 — Riesgos integrador y dependencias](L04-riesgos-integrador-y-dependencias.md)
