---
id: L17
materia: M26
orden: 17
titulo: Stripe test — productos Free/Pro
horas: 5.0
semana: 5
lectura: Stripe docs test mode
evidencia: projects/m26-capstone/memoria/stripe-productos.md
---

# L17 — Stripe test — productos Free/Pro

**~5 h · Semana 5**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/stripe-productos.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Productos Free/Pro en Stripe **test mode** documentados.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Price ids
- Test cards

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Stripe docs test mode_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Stripe test mode (30–40 min)

Confirma claves `sk_test` / `pk_test` solo en secretos de entorno. Documenta en `memoria/stripe-productos.md` el dashboard URL (sin keys).

### 3. Crea productos Free/Pro (90–110 min)

Crea Price objects alineados a `projects/m22-bektor/pricing.md`. Tabla: product_id, price_id, MXN, intervalo, qué desbloquea en Agenda Ops.

### 4. Enlaza al tenant (40–50 min)

Describe cómo el `tenant_id` queda asociado al Customer/Subscription Stripe (campo metadata). Sin implementar webhook aún (L20).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l17 stripe-test-productos-free-pro"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Stripe docs test mode | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/stripe-productos.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L18 — Landing pública de precios](L18-landing-publica-de-precios.md)
