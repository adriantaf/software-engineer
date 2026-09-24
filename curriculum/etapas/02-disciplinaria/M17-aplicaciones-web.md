---
id: M17
titulo: Aplicaciones web full-stack
etapa: disciplinaria
orden: 17
semanas: 8
horas: 160
practicas:
  - id: p1
    titulo: API REST con auth real + validación
  - id: p2
    titulo: Front con rutas protegidas y estados de carga/error
  - id: p3
    titulo: Integración WhatsApp deep-links + panel admin con roles
proyecto:
  id: proj
  titulo: MVP Agenda Ops (piloto) listo para multi-tenant
---

# M17 — Aplicaciones web full-stack

## Por qué existe
Aquí nace el **piloto** del SaaS [Agenda Ops](../../producto-saas.md). **Auth y roles desde el MVP**. Prepárate para M18 y para multi-tenant después.

## Análogos
UABC: Aplicaciones web. Tec: Desarrollo web y BD.

## Objetivos
HTTP, API, auth, validación, front serio, deploy público HTTPS. Modelo de datos que **pueda** llevar `tenant_id`.

## Cómo estudiar esta materia
Vertical slices: cada semana una historia de usuario completa (API+UI+test). Un solo negocio piloto = design partner.

## Día 1 (2–3 h)
1. Scaffold API + DB según M09/M13.
2. Endpoint `POST /auth/register` + `POST /auth/login` con hash.
3. Ruta protegida `GET /me` que falle sin sesión/token.
4. Test: sin auth → 401.
5. Lee [producto-saas.md](../../producto-saas.md) y anota 3 decisiones de modelo que faciliten multi-tenant luego.

## Stack sugerido
TypeScript + Node (Express/Fastify/Hono) + PostgreSQL + React o Astro islands.

## Temario
Semanas: auth → CRUD citas → admin roles → front → WhatsApp links → deploy → pulido → **checklist camino a SaaS**.

## Checklist camino a multi-tenant (cierre M17)
- [ ] Tablas de negocio sin hardcodear “el único negocio” en el código
- [ ] Documentado dónde irá `tenant_id` (ADR corto)
- [ ] Roles claros (owner/staff) dentro del negocio piloto
- [ ] HTTPS en deploy

## Recursos (ES)
MDN ES, OWASP intro, docs del framework, [producto-saas.md](../../producto-saas.md).

## Proyecto útil
**Agenda Ops — piloto:** servicios, citas, clientes, admin, WhatsApp, deploy público para **un** negocio de Ensenada. No es el SaaS multi-tenant completo aún; es la base.

## Errores comunes
Auth solo en el front; JWT mal guardado; deploy HTTP; MVP eterno; mezclar UI de “agencia” con producto SaaS.

## Criterios de dominio
- [ ] Usuario nuevo se onbandea sin ti (README + UX).
- [ ] Roles se respetan en API (demo).
- [ ] ADR de multi-tenant existe.
