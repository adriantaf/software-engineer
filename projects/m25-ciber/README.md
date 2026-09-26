# M25 — Ciberseguridad aplicada

Security review del SaaS multi-tenant Agenda Ops. Bug #1: **IDOR cross-tenant**.

## En resumen

Ciber aplicada al SaaS: inventario, aislamiento, hardening, tabletop y review final.

## Estructura esperada

```text
projects/m25-ciber/
  README.md
  inventario.md
  clasificacion-datos.md
  tenants-prueba.md
  security-review.md
  runbook-incidentes.md
  bitacora/
  aislamiento/
    prueba-manual-01.md
    tests.md
  review/
    authn.md
    authz-matrix.md
  hardening/
    headers.md
    stripe-secrets.md
    least-privilege.md
    restore-test.md
  logging/
    politica-logs.md
    errores.md
  abuso/
    rate-limit.md
  alertas/
    minimas.md
  privacidad/
    retencion.md
    exports.md
    aviso-borrador.md
  hallazgos/
    hallazgo-01.md
    hallazgo-02.md
  tabletop/
    env-leak.md
    cross-tenant-incident.md
```

## Checklist

- **P1 — Inventario:** activos + clasificación por tenant.
- **P2 — Review:** ≥2 issues de aislamiento cerrados con tests.
- **P3 — Tabletop:** ≥30 min documentados (.env / cross-tenant).
- **Proyecto — Security review:** `security-review.md`.

## Reglas

1. Solo atacas **tus** ambientes staging/prod acordados.
2. Prioriza IDOR cross-tenant sobre hallazgos cosméticos.
3. Sin secretos ni passwords en markdown.

## Enlaces

- Ficha: `curriculum/etapas/03-terminal/M25-ciberseguridad-aplicada.md`
- Bibliografía: `curriculum/bibliografia.md#m25-ciberseguridad-aplicada`
- Hilo: `curriculum/hilos/seguridad.md`
