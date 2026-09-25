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

**En cristiano:** nacen el piloto web de Agenda Ops: auth real, CRUD de citas, roles y base para multi-tenant.

## Análogos
UABC: Aplicaciones web. Tec: Desarrollo web y BD.

## Objetivos
HTTP, API, auth, validación, front serio, deploy público HTTPS. Modelo de datos que **pueda** llevar `tenant_id`.

## Cómo estudiar esta materia
Vertical slices: cada semana una historia de usuario completa (API+UI+test). Un solo negocio piloto = design partner.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth + API | 6–8 | Sesiones/JWT bien hechos |
| Front | 6–8 | Rutas protegidas + estados |
| Integración | 4–6 | WhatsApp links / admin |
| Retro | 1 | ADR `tenant_id` |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

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

## Lecturas

Canon: MDN Web Docs (ES) + docs del framework + OWASP Top 10 overview + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura | Alternativa |
|--------|---------|-------------|
| 1 | MDN **auth/cookies/sesiones** (ES) + docs auth del framework | OWASP Auth Cheat Sheet |
| 2 | Docs CRUD/routing del framework + modelo citas (tu SRS M12) | — |
| 3 | Control de acceso / roles (docs + notas M13) | OWASP Access Control |
| 4 | Front: MDN forms/accesibilidad básica + UI del piloto | — |
| 5 | Integración WhatsApp links (docs oficiales API o deep links) | — |
| 6 | Docs deploy del PaaS elegido + HTTPS | — |
| 7 | OWASP Top 10 **overview** (mapa hacia M18) | https://owasp.org |
| 8 | [producto-saas.md](../../producto-saas.md) sección multi-tenant + ADR `tenant_id` | Checklist camino a SaaS en esta ficha |

**Regla:** cada semana deja el piloto más demoable; la lectura sirve al commit, no al revés.

## Proyecto útil
**Agenda Ops — piloto:** servicios, citas, clientes, admin, WhatsApp, deploy público para **un** negocio de Ensenada. No es el SaaS multi-tenant completo aún; es la base.

## Errores comunes
Auth solo en el front; JWT mal guardado; deploy HTTP; MVP eterno; mezclar UI de “agencia” con producto SaaS.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — API auth:** Registro/login + validación; demo roles.
- **P2 — Front:** Rutas protegidas; loading/error/vacío.
- **P3 — Admin:** Roles owner/staff + deep-links WhatsApp.
- **Proyecto — Piloto:** Deploy HTTPS + checklist camino a SaaS.

## Criterios de dominio
- [ ] Usuario nuevo se onbandea sin ti (README + UX).
- [ ] Roles se respetan en API (demo).
- [ ] ADR de multi-tenant existe.
