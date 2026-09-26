---
id: L19
materia: M26
orden: 19
titulo: Checkout test end-to-end
horas: 5.0
semana: 5
lectura: Stripe Checkout
evidencia: projects/m26-capstone/memoria/billing-flujo.md
---

# L19 — Checkout test end-to-end

**~5 h · Semana 5**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/billing-flujo.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Checkout test end-to-end (crear sesión → pagar test card → estado Pro).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Webhook
- Customer portal opcional

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Stripe Checkout_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Checkout Session (40–50 min)

Implementa o verifica endpoint que crea Checkout Session en test mode para un tenant Free → Pro.

### 3. Pago con tarjeta test (60–80 min)

Completa pago con `4242…`. Documenta en `billing-flujo.md` pasos + IDs (session, subscription) **sin** secretos.

### 4. Estado en app (40–50 min)

Verifica que el tenant pasa a Pro en tu modelo (flag/plan). Si solo Stripe lo sabe y la app no, anota gap explícito.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m26): l19 checkout-test-end-to-end"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Stripe Checkout | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/billing-flujo.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L20 — Webhooks Stripe verificados en deploy](L20-webhooks-stripe-verificados-en-deploy.md)
