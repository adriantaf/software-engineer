---
id: L16
materia: M26
orden: 16
titulo: Demo interna semana 4 — flujos completos
horas: 5.0
semana: 4
lectura: demo script
evidencia: projects/m26-capstone/demos/semana-04.md
---

# L16 — Demo interna semana 4 — flujos completos

**~5 h · Semana 4**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/demos/semana-04.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Demo interna semana 4: flujos completos multi-tenant grabados/escritos.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Vertical completo

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _demo script_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Guion demo semana 4 (25–35 min)

En `projects/m26-capstone/demos/semana-04.md`: vertical completo — onboarding o login, pedido, contraste tenants, mención billing si listo.

### 3. Ejecuta flujos completos (100–120 min)

Graba o documenta con timestamps. Dos tenants. Anexa bugs encontrados como issues.

### 4. Comparación vs semana 2 (20–30 min)

Qué mejoró. Bitácora semana-04.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l16 demo-interna-semana-4-flujos-completos"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | demo script | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/demos/semana-04.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L17 — Stripe test — productos Free/Pro](L17-stripe-test-productos-free-pro.md)
