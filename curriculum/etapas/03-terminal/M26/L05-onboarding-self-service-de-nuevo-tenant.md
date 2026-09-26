---
id: L05
materia: M26
orden: 5
titulo: Onboarding self-service de nuevo tenant
horas: 5.0
semana: 2
lectura: Flujo registro negocio
evidencia: projects/m26-capstone/onboarding.md
---

# L05 — Onboarding self-service de nuevo tenant

**~5 h · Semana 2**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/onboarding.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Dejar onboarding self-service de tenant nuevo usable en staging (flujo + evidencia).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Signup
- Seed datos
- Aislamiento día 1

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Flujo registro negocio_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Mapea el flujo signup (25–35 min)

En `projects/m26-capstone/onboarding.md`: pasos UI/API desde “crear negocio” hasta primer login staff.

### 3. Ejecuta onboarding de un tenant nuevo (100–120 min)

En staging: crea tenant C (o re-crea A limpio) **sin** SQL manual si el producto ya lo permite.

Documenta: URLs, IDs, tiempo, qué aún es manual (gap explícito).

```bash
# ejemplo — adapta endpoint real
curl -s -X POST "$API/tenants" -H "Content-Type: application/json" \
  -d '{"name":"Barbería Demo C","owner_email":"owner-c@example.test"}'
```

### 4. Criterio self-service (25–35 min)

PASS si un tercero podría completar sin tu SSH. Si no: lista tareas para cerrar gap. Bitácora semana-02.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l05 onboarding-self-service-de-nuevo-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Flujo registro negocio | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/onboarding.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L06 — Seeds y datos demo por tenant](L06-seeds-y-datos-demo-por-tenant.md)
