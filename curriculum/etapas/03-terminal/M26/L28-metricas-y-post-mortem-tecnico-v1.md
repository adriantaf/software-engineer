---
id: L28
materia: M26
orden: 28
titulo: Métricas y post-mortem técnico v1
horas: 5.0
semana: 7
lectura: métricas semana 7
evidencia: projects/m26-capstone/post-mortem-v1.md
---

# L28 — Métricas y post-mortem técnico v1

**~5 h · Semana 7**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/post-mortem-v1.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Post-mortem técnico v1 con métricas y deuda consciente.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Deuda
- v1.1

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _métricas semana 7_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Recoge métricas v1 (30–40 min)

En `projects/m26-capstone/post-mortem-v1.md`: uptime/deploy count, tests, hallazgos seguridad, trials — lo que tengas.

### 3. Post-mortem técnico (90–110 min)

Secciones: **Qué salió bien**, **Qué dolió**, **Deuda consciente**, **v1.1 (5 ítems con fecha)**.

Sin blame theater; con owners.

### 4. Cierre de alcance (25–35 min)

Lista features que quedaron out y por qué. Bitácora semana-07.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l28 m-tricas-y-post-mortem-t-cnico-v1"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | métricas semana 7 | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/post-mortem-v1.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L29 — Video demo público multi-tenant](L29-video-demo-publico-multi-tenant.md)
