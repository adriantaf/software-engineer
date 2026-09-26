---
id: L14
materia: M26
orden: 14
titulo: App móvil M20 conectada o plan cierre
horas: 5.0
semana: 4
lectura: m20-movil README
evidencia: projects/m26-capstone/mobile-gap.md
---

# L14 — App móvil M20 conectada o plan cierre

**~5 h · Semana 4**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/mobile-gap.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

App móvil M20 conectada a API v1 **o** plan de cierre explícito del gap.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Misma API
- Staging HTTPS

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _m20-movil README_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Prepara carpetas (15–25 min)

```bash
mkdir -p projects/m26-capstone
```

Confirma que escribirás `projects/m26-capstone/mobile-gap.md`.

### 3. Laboratorio principal (100–130 min)

```bash
mkdir -p projects/m26-capstone/memoria projects/m26-capstone/demos projects/m26-capstone/bitacora
```

Estado conexión móvil; APK contra staging o plan con fecha.

Registra horas y bloqueos en `projects/m26-capstone/bitacora/semana-04.md`.

### 4. Criterio de calidad (30–45 min)

Relee `projects/m26-capstone/mobile-gap.md`: ¿un mentor externo entendería el resultado sin preguntarte?

Añade enlace a issue/PR/URL de staging si aplica. Bitácora de la semana: 5 líneas de horas y bloqueos.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m26): l14 app-m-vil-m20-conectada-o-plan-cierre"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | m20-movil README | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/mobile-gap.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L15 — Métricas M22 en producto](L15-metricas-m22-en-producto.md)
