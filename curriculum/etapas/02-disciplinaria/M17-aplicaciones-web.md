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
  titulo: Agenda/CRM en producción (MVP)
---

# M17 — Aplicaciones web full-stack

## Por qué existe
Aquí nace el producto útil. **Auth y roles desde el MVP**, no “lo ponemos después” ([hilo seguridad](../../hilos/seguridad.md)). Prepárate para M18.

## Análogos
UABC: Aplicaciones web. Tec: Desarrollo web y BD.

## Objetivos
HTTP, API, auth, validación, front serio, deploy público HTTPS.

## Cómo estudiar esta materia
Vertical slices: cada semana una historia de usuario completa (API+UI+test).

## Día 1 (2–3 h)
1. Scaffold API + DB según M09/M13.
2. Endpoint `POST /auth/register` + `POST /auth/login` con hash.
3. Ruta protegida `GET /me` que falle sin sesión/token.
4. Test: sin auth → 401.

## Stack sugerido
TypeScript + Node (Express/Fastify/Hono) + PostgreSQL + React o Astro islands.

## Temario
Semanas: auth → CRUD citas → admin roles → front → WhatsApp links → deploy → pulido → handoff a M18.

## Recursos (ES)
MDN ES, OWASP intro, docs del framework.

## Proyecto útil
**Agenda + CRM** para negocio Ensenada: servicios, citas, clientes, admin, WhatsApp, deploy público.

## Errores comunes
Auth solo en el front; JWT mal guardado; deploy HTTP; MVP eterno.

## Criterios de dominio
- [ ] Usuario nuevo se onbandea sin ti (README + UX).
- [ ] Roles se respetan en API (demo).
