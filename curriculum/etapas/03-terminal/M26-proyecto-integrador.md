---
id: M26
titulo: Proyecto integrador / titulación interna
etapa: terminal
orden: 26
semanas: 8
horas: 160
practicas:
  - id: p1
    titulo: Alcance SaaS congelado + plan de 8 semanas
  - id: p2
    titulo: Memoria técnica del SaaS v1
  - id: p3
    titulo: Demo pública / video del producto multi-tenant
proyecto:
  id: proj
  titulo: Agenda Ops SaaS en producción + egreso
---

# M26 — Proyecto integrador (SaaS)

## Por qué existe

Cierre de la academia. El egreso es un **SaaS vertical en producción**, no un CRUD suelto. Ver [producto-saas.md](../../producto-saas.md) y [egreso.md](../../egreso.md).

## Análogos
UABC: Desarrollo de aplicaciones innovadoras. Tec: cierre de ingeniería de software.

## Objetivos
Cumplir la rúbrica de egreso **en modo SaaS**: multi-tenant, billing test (Stripe), aislamiento, ops, evidencia comercial.

## Cómo estudiar esta materia
- Congela alcance semana 1 (MVP SaaS de la spec, no features infinitas).
- Cada semana: demo con **≥2 tenants**.
- Seguridad y billing no se dejan para el final.

## Día 1 (2–3 h)
1. `projects/m26-capstone/alcance.md` alineado a [producto-saas.md](../../producto-saas.md).
2. Checklist de egreso marcado.
3. Plan 8 sprints + fecha de demo pública.
4. Stripe test: cuenta + productos Free/Pro creados (aunque el wire sea parcial).

## Temario (8 semanas)

| Semana | Foco |
|--------|------|
| 1 | Alcance SaaS, tenancy, riesgos |
| 2–4 | Multi-tenant + onboarding + features críticas |
| 5 | Stripe test + landing de precios |
| 6 | Hardening + tests cross-tenant + CI |
| 7 | Memoria técnica + métricas + M22 |
| 8 | Demo, video, cierre egreso |

## Lecturas

Canon: memoria técnica propia + [producto-saas](../../producto-saas.md) + rúbrica [egreso](../../egreso.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura / relectura | Uso |
|--------|---------------------|-----|
| 1 | [producto-saas.md](../../producto-saas.md) completo + egreso | `alcance.md` congelado |
| 2 | Tu SRS (M12) + diseño (M13) — solo gaps multi-tenant | Onboarding tenant |
| 3 | Docs Stripe **test mode** (Checkout / Customer) intro | Preparar productos Free/Pro |
| 4 | Repaso ADRs de tenancy | Features críticas |
| 5 | Docs Stripe Checkout + webhooks (test) | Landing precios |
| 6 | Informe M25 + OWASP access control (repaso) | Tests cross-tenant + CI |
| 7 | Plantilla memoria técnica (estructura M26) + métricas M22 | Memoria v1 |
| 8 | Checklist egreso | Demo + video |

**Regla:** cada semana demo con ≥2 tenants; billing y seguridad no se aplazan.

## Entregables
1. **SaaS en producción** (Agenda Ops) con ≥2 tenants demo.
2. Landing de precios + checkout Stripe **test mode**.
3. Memoria técnica (arquitectura, tenancy, billing, seguridad).
4. App móvil/desktop conectada (o justificación fuerte; por defecto sí).
5. Security review M25 vigente (cross-tenant).
6. Registro comercial M22 (trials/demos).
7. Video demo sin tutorial de fondo.

## Errores comunes
Scope creep; un solo tenant “de mentira”; Stripe solo en localhost; demo con secretos en claro.

## Criterios de dominio final
CRUD con auth + deploy + tests en un fin de semana **y** explicas aislamiento multi-tenant + el IDOR cross-tenant.
