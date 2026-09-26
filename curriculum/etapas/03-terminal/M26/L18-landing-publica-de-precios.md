---
id: L18
materia: M26
orden: 18
titulo: Landing pública de precios
horas: 5.0
semana: 5
lectura: Marketing repo o /pricing
evidencia: projects/m26-capstone/memoria/landing-precios.md
---

# L18 — Landing pública de precios

**~5 h · Semana 5**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/landing-precios.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Landing pública de precios en staging/prod con precios MXN coherentes con M22.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- CTA trial
- Planes claros

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Marketing repo o /pricing_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Define copy de precios (25–35 min)

En `projects/m26-capstone/memoria/landing-precios.md`: planes Free/Pro, precios MXN alineados a M22, CTA trial.

### 3. Publica página en staging/prod (100–120 min)

Ruta `/pricing` o landing marketing. Verifica en navegador:

```bash
curl -sI "https://TU-DOMINIO/pricing" | head -n 15
```

Enlaza URL desde README capstone.

### 4. Coherencia con Stripe (25–35 min)

Tabla: texto landing ↔ price_id (sin secretos). Bitácora semana-05.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l18 landing-p-blica-de-precios"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Marketing repo o /pricing | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/landing-precios.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L19 — Checkout test end-to-end](L19-checkout-test-end-to-end.md)
