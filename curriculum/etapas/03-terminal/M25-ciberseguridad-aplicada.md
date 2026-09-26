---
id: M25
titulo: Ciberseguridad aplicada
etapa: terminal
orden: 25
semanas: 6
horas: 120
practicas:
  - id: p1
    titulo: Inventario de activos y superficie (prod/staging SaaS)
  - id: p2
    titulo: Security review con pruebas cross-tenant obligatorias
  - id: p3
    titulo: Tabletop de incidente (.env / fuga) documentado
proyecto:
  id: proj
  titulo: Security review SaaS (aislamiento multi-tenant) + hardening
---

# M25 — Ciberseguridad aplicada

## Por qué existe

**Capa C** de la pista de seguridad, aplicada a tu **SaaS multi-tenant**. El fallo #1 a cazar: **IDOR cross-tenant** (el tenant A lee datos del B). Ver [producto-saas](../../producto-saas.md).

**En resumen:** ciber aplicada al SaaS multi-tenant: el bug #1 a cazar es IDOR cross-tenant.


## Objetivos de aprendizaje

1. Inventariar activos y superficie del SaaS desplegado.
2. Security review con **pruebas de aislamiento entre tenants**.
3. Hardening de producción (HTTPS, backups, least privilege, secrets Stripe).
4. Tabletop de incidente + runbook.
5. Intro privacidad/datos (contexto MX) por tenant.

## Cómo estudiar esta materia (lecciones)

M25 es **ciberseguridad aplicada** al SaaS Agenda Ops: L01–L24, evidencia en `projects/m25-ciber/` y fixes en el repo del producto.

1. Orden **L01 → L24**; prioriza **IDOR cross-tenant** sobre hallazgos cosméticos.
2. Solo atacas **tus** ambientes prod/staging acordados.
3. Cierra ≥2 issues críticos/altos de aislamiento con tests antes del cierre.
4. Tabletop documentado (≥30 min narrativa) sin copiar tutorial.
5. [hilo seguridad](../../hilos/seguridad.md) + [producto-saas](../../producto-saas.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lecciones + labs | 10–12 | 4× ~5 h en inventario/review/hardening |
| Fixes cross-tenant | 4–6 | PRs con tests |
| Tabletop / informe | 4–6 | `security-review.md` |
| Retro | 1 | Riesgo residual |

Si un día solo tienes 2 h: **prueba manual A vs B** o un fix con test.

## Lecciones

### Semana 1 — Inventario y clasificación multi-tenant (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Inventario de activos SaaS prod y staging](M25/L01-inventario-de-activos-saas-prod-y-staging.md) | 5 |
| L02 | [Clasificación de datos por tenant](M25/L02-clasificacion-de-datos-por-tenant.md) | 5 |
| L03 | [Dos tenants de prueba y mapa de identidades](M25/L03-dos-tenants-de-prueba-y-mapa-de-identidades.md) | 5 |
| L04 | [Primera prueba manual cross-tenant](M25/L04-primera-prueba-manual-cross-tenant.md) | 5 |

### Semana 2 — Authn/authz y tests cross-tenant (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Review authn — sesión y tokens](M25/L05-review-authn-sesion-y-tokens.md) | 5 |
| L06 | [Review authz — roles staff vs admin](M25/L06-review-authz-roles-staff-vs-admin.md) | 5 |
| L07 | [Automatizar test cross-tenant en CI](M25/L07-automatizar-test-cross-tenant-en-ci.md) | 5 |
| L08 | [Cerrar ≥1 hallazgo crítico de aislamiento](M25/L08-cerrar-1-hallazgo-critico-de-aislamiento.md) | 5 |

### Semana 3 — Hardening deploy y Stripe (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [HTTPS, headers y configuración prod](M25/L09-https-headers-y-configuracion-prod.md) | 5 |
| L10 | [Secretos Stripe y rotación](M25/L10-secretos-stripe-y-rotacion.md) | 5 |
| L11 | [Least privilege DB y deploy](M25/L11-least-privilege-db-y-deploy.md) | 5 |
| L12 | [Backup y restore probado](M25/L12-backup-y-restore-probado.md) | 5 |

### Semana 4 — Logging, abuso y alertas (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Logging sin secretos ni PII innecesaria](M25/L13-logging-sin-secretos-ni-pii-innecesaria.md) | 5 |
| L14 | [Rate limit login y abuso básico](M25/L14-rate-limit-login-y-abuso-basico.md) | 5 |
| L15 | [Alertas mínimas operativas](M25/L15-alertas-minimas-operativas.md) | 5 |
| L16 | [Errores HTTP y fugas de stack](M25/L16-errores-http-y-fugas-de-stack.md) | 5 |

### Semana 5 — Privacidad y cierre de hallazgos (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L17 | [Retención y borrado por tenant](M25/L17-retencion-y-borrado-por-tenant.md) | 5 |
| L18 | [Minimización en exports y soporte](M25/L18-minimizacion-en-exports-y-soporte.md) | 5 |
| L19 | [Consentimiento y avisos (contexto MX)](M25/L19-consentimiento-y-avisos-contexto-mx.md) | 5 |
| L20 | [Segundo hallazgo aislamiento cerrado](M25/L20-segundo-hallazgo-aislamiento-cerrado.md) | 5 |

### Semana 6 — Tabletop y security review final (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L21 | [Tabletop — fuga de .env](M25/L21-tabletop-fuga-de-env.md) | 5 |
| L22 | [Tabletop — acceso cross-tenant en prod](M25/L22-tabletop-acceso-cross-tenant-en-prod.md) | 5 |
| L23 | [Runbook de respuesta incidentes](M25/L23-runbook-de-respuesta-incidentes.md) | 5 |
| L24 | [Security review final y cierre M25](M25/L24-security-review-final-y-cierre-m25.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: **OWASP Testing Guide** (secciones por semana) + [hilo seguridad](../../hilos/seguridad.md). Ver [bibliografía](../../bibliografia.md#m25-ciberseguridad-aplicada).

| Semana | Lecciones | OWASP / foco | Entrega |
|--------|-----------|--------------|---------|
| 1 | L01–L04 | Information gathering | `inventario.md`, tenants prueba |
| 2 | L05–L08 | Identity / authorization | Tests cross-tenant |
| 3 | L09–L12 | Configuration + Stripe | Hardening + restore |
| 4 | L13–L16 | Logging / abuse | Política logs + rate limit |
| 5 | L17–L20 | Privacy / retención | 2º hallazgo cerrado |
| 6 | L21–L24 | Reporting + tabletop | `security-review.md` |

**Regla:** al menos 2 issues críticos/altos de aislamiento cerrados con tests.



## Ejemplo — checklist SaaS

```text
[ ] Auth en endpoints sensibles
[ ] Autorización por tenant_id + rol (anti IDOR cross-tenant)
[ ] Tests automatizados cross-tenant
[ ] Rate limit en login
[ ] Headers de seguridad en prod
[ ] Backups restaurables
[ ] Logs sin secretos/PII innecesaria
[ ] Webhooks Stripe verificados (firma)
```



## Prácticas
P1–P3 del frontmatter. Al menos **2** issues críticos/altos de aislamiento cerrados con tests.

## Proyecto útil
`projects/m25-ciber/security-review.md` + PRs. Alimenta M26.

## Errores comunes
Ignorar multi-tenant; 50 hallazgos CSS y cero cross-tenant; no verificar webhooks.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Inventario:** Activos + clasificación por tenant.
- **P2 — Review:** ≥2 issues aislamiento cerrados con tests.
- **P3 — Tabletop:** 30 min documentados (.env/fuga).
- **Proyecto — Security review:** `projects/m25-ciber/security-review.md`.

## Criterios de dominio
- [ ] Demo: A no lee datos de B (manual + test).
- [ ] Tabletop 30 min sin tutorial.
- [ ] TLS + secrets fuera de repo + restore probado.
