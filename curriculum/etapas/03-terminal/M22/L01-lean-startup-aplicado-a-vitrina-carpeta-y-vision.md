---
id: L01
materia: M22
orden: 1
titulo: Lean Startup aplicado a Vitrina — carpeta y visión
horas: 5.0
semana: 1
lectura: El método Lean Startup — visión, start, build-measure-learn
evidencia: projects/m22-bektor/demos + bitacora-m22.md
---

# L01 — Lean Startup aplicado a Vitrina — carpeta y visión

**~5 h · Semana 1**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos + bitacora-m22.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Crear estructura comercial, leer visión/start/BML y escribir hipótesis de negocio SaaS (no agencia).

## Por qué empieza así

M22 vende **suscripción** al producto que construiste; Bektor como agencia no es el modelo del plan.

Conceptos que debes poder explicar al cerrar:

- Visión vs estrategia.
- Build-measure-learn.
- SaaS vertical.
- Anti-patrón agencia.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _El método Lean Startup — visión, start, build-measure-learn_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

```bash
mkdir -p projects/m22-bektor/demos
```

### 3. Laboratorio principal (90–120 min)

Lista 3 supuestos que **matarían** el negocio si fueran falsos.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l01 lean-startup-aplicado-a-vitrina-carpe"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | El método Lean Startup — visión, start, build-measure-learn | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos + bitacora-m22.md`.
2. demos/ existe.
3. bitacora con BML.
4. 3 supuestos críticos.
5. Commit `docs(m22): l01 …` en el historial.

## Errores comunes

- Volver a vender ‘páginas web’.
- Leer sin escribir acción.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L02 — ICP único — sub-vertical fijado por escrito](L02-icp-unico-sub-vertical-fijado-por-escrito.md)
