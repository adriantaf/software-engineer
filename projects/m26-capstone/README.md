# M26 — Proyecto integrador (capstone)

Evidencia de egreso: Agenda Ops SaaS multi-tenant en producción.

## En resumen

Cierras el plan con ≥2 tenants, Stripe test, security review M25 y demo pública.

## Estructura esperada

```text
projects/m26-capstone/
  README.md                 ← índice maestro (L31)
  alcance.md                ← L01 (P1)
  plan-8-semanas.md         ← L02
  egreso-checklist.md       ← L02 / L30
  riesgos.md
  onboarding.md
  demo-tenants.md
  integraciones.md
  mobile-gap.md
  metricas.md
  comercial.md
  post-mortem-v1.md
  demo.md                   ← L29 (P3 video)
  seguridad-m25.md
  ci-cross-tenant.md
  hardening-final.md
  tests-regresion.md
  cierre.md                 ← L32
  bitacora/
    semana-01.md … semana-08.md
  demos/
    semana-02.md
    semana-04.md
  memoria/                  ← P2
    tenancy-modelo.md
    panel-admin.md
    citas-crud.md
    clientes-servicios.md
    roles.md
    stripe-productos.md
    landing-precios.md
    billing-flujo.md
    webhooks-stripe.md
    ops.md
    arquitectura.md
    tenancy-billing-seguridad.md
```

## Checklist

- **P1 — Alcance:** `alcance.md` congelado + plan 8 semanas.
- **P2 — Memoria:** arquitectura, tenancy, billing, seguridad.
- **P3 — Demo:** video público multi-tenant (`demo.md`).
- **Proyecto — Egreso:** prod + Stripe test + review M25 + demos M22.

## Reglas

1. Congela alcance en semana 1 y respétalo.
2. Billing y cross-tenant **no** se aplazan a la semana 8.
3. Cada semana: demo interna con ≥2 tenants.

## Enlaces

- Ficha: `curriculum/etapas/03-terminal/M26-proyecto-integrador.md`
- Egreso: `curriculum/egreso.md`
- Bibliografía: `curriculum/bibliografia.md#m26-proyecto-integrador`
