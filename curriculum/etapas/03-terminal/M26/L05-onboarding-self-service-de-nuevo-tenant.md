---
id: L05
materia: M26
orden: 5
titulo: Onboarding self-service de nuevo tenant
horas: 5
semana: 2
lectura: "Flujo registro negocio"
evidencia: "repo producto + nota onboarding"
---

# L05 — Onboarding self-service de nuevo tenant

**~5 h · Semana 2**

## Objetivo

Entregar evidencia de: Onboarding self-service de nuevo tenant para el capstone Agenda Ops en producción.

## Por qué importa

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

## Conceptos

- Signup
- Seed datos
- Aislamiento día 1

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m26-capstone/memoria projects/m26-capstone/demos projects/m26-capstone/bitacora
```

Implementa o documenta gap: nuevo negocio sin tu intervención manual. Dos tenants con nombres reales ficticios.

Registra horas y bloqueos en `projects/m26-capstone/bitacora/semana-02.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m26): l05 onboarding-self-service-de-nuevo-tenant"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | [producto-saas.md](../../producto-saas.md) | [egreso.md](../../egreso.md) |
| Ficha | M26-proyecto-integrador.md | M25 security-review |
| Catálogo | Entrada M26 | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

1. Artefacto indicado existe: repo.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L06 — Seeds y datos demo por tenant](L06-seeds-y-datos-demo-por-tenant.md)
