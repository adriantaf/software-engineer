---
id: L21
materia: M26
orden: 21
titulo: Re-ejecutar review M25 y cerrar gaps
horas: 5.0
semana: 6
lectura: security-review.md
evidencia: projects/m26-capstone/seguridad-m25.md
---

# L21 — Re-ejecutar review M25 y cerrar gaps

**~5 h · Semana 6**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/seguridad-m25.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Re-ejecutar security review M25 y cerrar gaps bloqueantes.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Cross-tenant CI
- Headers

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _security-review.md_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Relee security-review M25 (30–40 min)

En `projects/m26-capstone/seguridad-m25.md` índice de hallazgos abiertos vs cerrados desde `projects/m25-ciber/security-review.md`.

### 3. Cierra gaps bloqueantes (100–120 min)

Lista P0/P1. Cada uno: issue, fix o waiver firmado con riesgo residual.

Re-corre test cross-tenant:

```bash
pnpm test -- aislamiento   # adapta
```

### 4. Handoff a demo pública (25–35 min)

Qué debe estar verde antes del video. Bitácora semana-06.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l21 re-ejecutar-review-m25-y-cerrar-gaps"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | security-review.md | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/seguridad-m25.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L22 — CI con tests cross-tenant obligatorios](L22-ci-con-tests-cross-tenant-obligatorios.md)
