---
id: L10
materia: M22
orden: 10
titulo: Demos 5–6 — escuchar precio en voz alta
horas: 5.0
semana: 3
lectura: Lean — experimentos de mercado
evidencia: projects/m22-bektor/demos/demo-05.md + demo-06.md
---

# L10 — Demos 5–6 — escuchar precio en voz alta

**~5 h · Semana 3**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos/demo-05.md + demo-06.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Dos demos donde **dices el precio** o rango Pro sin tartamudear y registras reacción.

## Por qué empieza así

M26 integrará Stripe; hoy practicas defensa del valor en MXN.

Conceptos que debes poder explicar al cerrar:

- Anclaje precio.
- Free/Pro.
- Objeción precio.
- Trial como reduce riesgo.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — experimentos de mercado_.

Traduce a Agenda Ops: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor/demos`.

Documenta demos 5–6. En cada ficha campo **Reacción precio** (verbatim si puedes).

### 3. Laboratorio principal (90–120 min)

Ajusta `projects/m22-bektor/pricing.md` con límites técnicos reales del producto (no prometer IA ilimitada si M23 costea tokens).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l10 demos-5-6-escuchar-precio-en-voz-alta"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — experimentos de mercado | [producto-saas (Agenda Ops)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos/demo-05.md + demo-06.md`.
2. 2 demos con precio dicho.
3. pricing.md actualizado.
4. Reacción documentada.
5. Commit `docs(m22): l10 …` en el historial.

## Errores comunes

- Evitar nombrar precio.
- Prometer features inexistentes.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L11 — Refinar ICP tras objeciones recurrentes](L11-refinar-icp-tras-objeciones-recurrentes.md)
