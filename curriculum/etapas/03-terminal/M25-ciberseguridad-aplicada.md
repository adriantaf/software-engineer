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

## Análogos
UABC: Seguridad / gestión. Tec: Ciberseguridad (cierre aplicado).

## Objetivos

1. Inventariar activos y superficie del SaaS desplegado.
2. Security review con **pruebas de aislamiento entre tenants**.
3. Hardening de producción (HTTPS, backups, least privilege, secrets Stripe).
4. Tabletop de incidente + runbook.
5. Intro privacidad/datos (contexto MX) por tenant.

## Cómo estudiar esta materia

- Trabaja sobre Agenda Ops, no demos ajenos.
- Prioriza cross-tenant y authz sobre hallazgos cosméticos.
- Solo tus ambientes.

## Día 1 (2–3 h)

1. Inventario: URLs, webhooks Stripe, DB, secrets CI.
2. Crea (si no existen) **dos tenants de prueba**.
3. Intenta, como usuario del tenant A, leer un recurso del B. Documenta resultado.
4. `projects/m25-ciber/inventario.md` + nota de aislamiento.

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

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Inventario, superficie, clasificación de datos por tenant |
| 2 | Review auth/roles + **cross-tenant** |
| 3 | Hardening deploy + secretos billing |
| 4 | Logging, abuso, alertas |
| 5 | Privacidad / retención |
| 6 | Tabletop + reporte final |

## Lecturas

Canon: OWASP Testing Guide (secciones) + [hilo](../../hilos/seguridad.md) + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Secciones Testing Guide / foco | Práctica |
|--------|-------------------------------|----------|
| 1 | Information gathering / inventario de superficie | Clasificación datos por tenant |
| 2 | Identity / authorization testing — **cross-tenant** | Review auth/roles |
| 3 | Configuration / deploy hardening | Secretos billing |
| 4 | Error handling / logging / abuse | Alertas mínimas |
| 5 | Privacy / data protection (retención) | Política corta en repo |
| 6 | Reporting + tabletop | `projects/m25-ciber/security-review.md` |

**Regla:** al menos 2 issues críticos/altos de aislamiento cerrados con tests.

## Prácticas
P1–P3 del frontmatter. Al menos **2** issues críticos/altos de aislamiento cerrados con tests.

## Proyecto útil
`projects/m25-ciber/security-review.md` + PRs. Alimenta M26.

## Errores comunes
Ignorar multi-tenant; 50 hallazgos CSS y cero cross-tenant; no verificar webhooks.

## Criterios de dominio
- [ ] Demo: A no lee datos de B (manual + test).
- [ ] Tabletop 30 min sin tutorial.
- [ ] TLS + secrets fuera de repo + restore probado.
