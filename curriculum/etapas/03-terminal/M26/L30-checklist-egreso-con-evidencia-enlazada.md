---
id: L30
materia: M26
orden: 30
titulo: Checklist egreso con evidencia enlazada
horas: 5.0
semana: 8
lectura: egreso.md
evidencia: projects/m26-capstone/egreso-checklist.md
---

# L30 — Checklist egreso con evidencia enlazada

**~5 h · Semana 8**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/egreso-checklist.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Checklist de egreso con cada ítem enlazado a evidencia en git/URL.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Hashes commit
- URLs

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _egreso.md_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Congela checklist final (30–40 min)

En `projects/m26-capstone/egreso-checklist.md`: cada ítem de [egreso](../../../egreso.md) con estado final.

### 3. Enlaza evidencias (100–120 min)

Cada “hecho” lleva path git, URL, o commit hash. Nada de “está en mi laptop”.

```bash
git log --oneline -20 -- projects/m26-capstone projects/m25-ciber
```

Pega hashes relevantes junto a ítems difíciles.

### 4. Ítems parciales (25–35 min)

Los parciales explican gap + plan. Bitácora semana-08.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l30 checklist-egreso-con-evidencia-enlazada"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | egreso.md | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/egreso-checklist.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L31 — README capstone índice maestro](L31-readme-capstone-indice-maestro.md)
