---
id: L12
materia: M22
orden: 12
titulo: Pricing Free/Pro — borrador defendible
horas: 5.0
semana: 3
lectura: producto-saas + límites técnicos
evidencia: projects/m22-bektor/pricing.md
---

# L12 — Pricing Free/Pro — borrador defendible

**~5 h · Semana 3**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/pricing.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Cerrar borrador Free/Pro MXN con límites (calendarios, citas/mes, staff) alineados al código actual.

## Por qué empieza así

P3 exige coherencia técnica; pricing que rompe el producto es deuda comercial.

Conceptos que debes poder explicar al cerrar:

- Free tier.
- Pro tier.
- Límites.
- Upgrade path M26.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _producto-saas + límites técnicos_.

Traduce a Agenda Ops: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Completa `projects/m22-bektor/pricing.md`: tabla planes, límites, qué pasa al exceder, política trial 14 días.

### 3. Laboratorio principal (90–120 min)

Párrafo **Por qué estos números** (costo hosting, tiempo ahorrado, comparativa local).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l12 pricing-free-pro-borrador-defendible"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | producto-saas + límites técnicos | [producto-saas (Agenda Ops)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/pricing.md`.
2. Free/Pro completos.
3. Límites técnicos.
4. Justificación breve.
5. Commit `docs(m22): l12 …` en el historial.

## Errores comunes

- Pro ‘contactar’ sin cifra.
- Free ilimitado imposible.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L13 — Métricas accionables — tablero de trials](L13-metricas-accionables-tablero-de-trials.md)
