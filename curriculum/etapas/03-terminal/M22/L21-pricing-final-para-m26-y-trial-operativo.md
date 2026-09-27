---
id: L21
materia: M22
orden: 21
titulo: Pricing final para M26 y trial operativo
horas: 5.0
semana: 6
lectura: Stripe docs (preview) + pricing.md
evidencia: projects/m22-bektor/pricing.md final
---

# L21 — Pricing final para M26 y trial operativo

**~5 h · Semana 6**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/pricing.md final`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Congelar pricing Free/Pro MXN para integración Stripe test en M26; checklist trial operativo.

## Por qué empieza así

Semana 6 cierra comercial de la materia con números estables.

Conceptos que debes poder explicar al cerrar:

- Price freeze.
- Trial 14d.
- Límites.
- Handoff M26.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Stripe docs (preview) + pricing.md_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Marca `projects/m22-bektor/pricing.md` sección **Final M22** con fecha congelación.

### 3. Laboratorio principal (90–120 min)

Lista checklist trial: alta tenant, credenciales, soporte WhatsApp, activación medida.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l21 pricing-final-para-m26-y-trial-operativo"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Stripe docs (preview) + pricing.md | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/pricing.md final`.
2. Pricing congelado fechado.
3. Checklist trial.
4. P3 listo para UI.
5. Commit `docs(m22): l21 …` en el historial.

## Errores comunes

- Cambiar precio post-cierre sin nota.
- Trial sin proceso.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L22 — Síntesis comercial para backlog M21](L22-sintesis-comercial-para-backlog-m21.md)
