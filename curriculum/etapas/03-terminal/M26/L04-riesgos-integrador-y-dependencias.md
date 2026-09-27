---
id: L04
materia: M26
orden: 4
titulo: Riesgos integrador y dependencias
horas: 5.0
semana: 1
lectura: M21 riesgos + M25 pendientes
evidencia: projects/m26-capstone/riesgos.md
---

# L04 — Riesgos integrador y dependencias

**~5 h · Semana 1**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/riesgos.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Listar riesgos del integrador (billing, aislamiento, ops) con mitigaciones y dueños.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Stripe
- Hosting
- Scope creep

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _M21 riesgos + M25 pendientes_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Lista riesgos P0–P2 (25–35 min)

En `projects/m26-capstone/riesgos.md` tabla: riesgo | impacto | probabilidad | mitigación | dueño | enlace M25 si aplica.

### 3. Cubre dependencias críticas (90–110 min)

Filas mínimas: aislamiento cross-tenant, Stripe webhooks, hosting/DB, scope creep WhatsApp/móvil, restore backups, secretos.

Cada P0 con mitigación accionable esta semana.

### 4. Revisión con plan-8 (25–35 min)

Enlaza cada P0 a una semana del plan. Bitácora semana-01.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l04 riesgos-integrador-y-dependencias"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | M21 riesgos + M25 pendientes | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/riesgos.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L05 — Onboarding self-service de nuevo tenant](L05-onboarding-self-service-de-nuevo-tenant.md)
