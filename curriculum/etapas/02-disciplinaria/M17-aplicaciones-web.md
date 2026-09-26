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

Aquí nace el **piloto web** de [Agenda Ops](../../producto-saas.md): citas, clientes, servicios y admin para **un** negocio de servicios (design partner), no un CRUD genérico. Auth, roles y validación van desde el MVP — no “después en M18”. El modelo de datos debe **poder** llevar `tenant_id` en M26 sin reescribir todo.

Esta materia integra M09 (esquema), M12–M13 (requerimientos/diseño), M15 (tests) y prepara M19 (deploy) y M18 (AppSec).

**En resumen:** nace el piloto web de Agenda Ops: auth real, CRUD de citas, roles y base para multi-tenant.


## Objetivos de aprendizaje

Al terminar debes poder:

1. Diseñar y exponer una API REST con validación de entrada y códigos HTTP coherentes.
2. Implementar registro/login con hash de contraseña y sesión o JWT **validada en servidor**.
3. Proteger rutas en front y API; manejar loading, error y vacío en UI.
4. CRUD de citas, clientes y servicios alineado al SRS del piloto.
5. Panel admin con roles owner/staff y autorización en cada endpoint sensible.
6. Deep-links WhatsApp para recordatorios o confirmaciones (sin sustituir la API).
7. Desplegar el piloto en HTTPS con checklist documentado hacia multi-tenant.

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md) y [producto-saas.md](../../producto-saas.md) antes de la semana 2.
- **Vertical slices:** cada semana una historia de usuario completa (API + UI + test mínimo).
- Un solo negocio piloto (design partner); no mezcles UI de “agencia” con producto SaaS.
- Cada endpoint nuevo: test de auth (401/403) antes de pulir CSS.
- Documenta decisiones de `tenant_id` en ADR corto al cierre (semana 8).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth + API | 6–8 | Sesiones/JWT bien hechos |
| Front | 6–8 | Rutas protegidas + estados |
| Integración | 4–6 | WhatsApp links / admin |
| Retro | 1 | ADR o gap hacia SaaS |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Crea o abre la carpeta de evidencia:
   ```bash
   mkdir -p projects/m17-agenda-ops/docs
   ```
2. Scaffold API + conexión DB según esquema M09 (`projects/m17-agenda-ops/` o repo enlazado en README).
3. `POST /auth/register` + `POST /auth/login` con hash (bcrypt/argon2 — no MD5).
4. Ruta protegida `GET /me` que falle con **401** sin sesión/token; test automatizado mínimo.
5. Lee [producto-saas.md](../../producto-saas.md) y anota en `projects/m17-agenda-ops/docs/decisiones-multitenant.md` **3** decisiones de modelo que faciliten `tenant_id` luego.
6. Commit, por ejemplo: `feat(m17): auth register/login + GET /me protegido`.

## Stack sugerido

TypeScript + Node (Express/Fastify/Hono) + PostgreSQL + React, Astro islands o similar. El stack exacto vive en `projects/m17-agenda-ops/stack.md`; no cambies a mitad de materia sin ADR.

## Ejemplo — test de auth mínimo

```ts
import { expect, test } from "vitest";

test("GET /me sin token devuelve 401", async () => {
  const res = await fetch(`${API_URL}/me`);
  expect(res.status).toBe(401);
});
```

Regla: la autorización se prueba en el **servidor**, no solo ocultando botones.

## Temario semanal

### Semana 1 — Auth, usuarios y fundación (~20 h)

- Modelo de usuario vinculado al negocio piloto (sin multi-tenant aún).
- Registro, login, logout; cookies HttpOnly o JWT con almacenamiento seguro documentado.
- Validación de payload (Zod/class-validator/etc.).
- Práctica P1 inicio: suite de tests auth en verde.

### Semana 2 — CRUD citas y clientes (~20 h)

- Endpoints REST citas/clientes/servicios según SRS M12.
- Reglas de negocio mínimas (no citas en el pasado sin override, etc.).
- Seeds o fixtures para demo con design partner.
- Paginación o filtros simples en listados.

### Semana 3 — Roles owner/staff (~20 h)

- Matriz de permisos: quién cancela citas, quién ve reportes.
- Middleware de autorización por rol en API.
- Panel admin básico (aunque sea feo pero claro).
- Práctica P3 inicio: demo de staff bloqueado en acción de owner.

### Semana 4 — Front serio (~20 h)

- Rutas protegidas; redirect a login.
- Estados loading / error / vacío en listas y formularios.
- Formularios accesibles (labels, errores de validación visibles).
- Práctica P2: capturas o notas en `projects/m17-agenda-ops/docs/ui-estados.md`.

### Semana 5 — WhatsApp e integración (~20 h)

- Deep links o plantillas oficiales según docs del proveedor (sin secretos en front).
- Flujo: recordatorio o confirmación desde ficha de cita.
- Log de envíos o intentos (sin PII en logs de prod).

### Semana 6 — Deploy HTTPS (~20 h)

- Deploy en PaaS o VPS con TLS (Let’s Encrypt o proveedor).
- Variables de entorno fuera del repo; health check.
- Smoke test post-deploy documentado en README.

### Semana 7 — Hardening ligero y OWASP map (~20 h)

- Repaso OWASP Top 10 **overview**: qué aplica ya a tu piloto.
- Headers de seguridad básicos donde puedas (HSTS en prod, etc.).
- Rate limit en login introductorio.

### Semana 8 — Checklist camino a SaaS (~20 h)

- ADR `tenant_id`: dónde va la columna, cómo migrar datos piloto.
- Checklist abajo marcado o con gaps honestos.
- Demo grabable del piloto para design partner.

## Checklist camino a multi-tenant (cierre M17)

- [ ] Tablas de negocio sin hardcodear “el único negocio” en el código
- [ ] Documentado dónde irá `tenant_id` (`projects/m17-agenda-ops/docs/adr-tenant-id.md` o similar)
- [ ] Roles claros (owner/staff) dentro del negocio piloto
- [ ] HTTPS en deploy
- [ ] Tests de auth/roles en CI o script local reproducible

## Lecturas

Canon: MDN Web Docs (ES) + docs del framework + OWASP Top 10 overview + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura | Alternativa |
|--------|---------|-------------|
| 1 | MDN **auth/cookies/sesiones** (ES) + docs auth del framework | OWASP Auth Cheat Sheet |
| 2 | Docs CRUD/routing + modelo citas (SRS M12) | — |
| 3 | Control de acceso / roles (docs + notas M13) | OWASP Access Control |
| 4 | MDN forms/accesibilidad básica + UI del piloto | — |
| 5 | WhatsApp / deep links (docs oficiales) | — |
| 6 | Docs deploy del PaaS + HTTPS | — |
| 7 | OWASP Top 10 **overview** (mapa hacia M18) | https://owasp.org |
| 8 | [producto-saas.md](../../producto-saas.md) multi-tenant + ADR | Checklist en esta ficha |

**Regla:** cada semana deja el piloto más demoable; la lectura sirve al commit, no al revés.

## Prácticas

1. **P1 — API auth:** Registro/login + validación; tests 401/403 en `projects/m17-agenda-ops/`; evidencia en README.
2. **P2 — Front:** Rutas protegidas; loading/error/vacío documentados en `projects/m17-agenda-ops/docs/ui-estados.md`.
3. **P3 — Admin + WhatsApp:** Roles owner/staff demostrables + deep-link o flujo WhatsApp en `projects/m17-agenda-ops/docs/integracion-whatsapp.md`.

## Proyecto útil

**Agenda Ops — piloto web** en `projects/m17-agenda-ops/`:

- README con URL de staging/prod, credenciales demo **solo** de entorno de prueba.
- CRUD citas/clientes/servicios usable por un design partner real.
- Admin con roles; integración WhatsApp mínima.
- Enlace al ADR multi-tenant y al checklist de cierre.

No es el SaaS multi-tenant completo (eso es M26); es la base sólida con auth y modelo extensible.

## Errores comunes

- Auth solo en el front (botones ocultos sin check en API).
- JWT en `localStorage` sin entender el riesgo XSS (documenta tu elección).
- Deploy HTTP “temporal” que nunca se corrige.
- MVP eterno sin deploy; mezclar branding agencia con producto Agenda Ops.
- Olvidar validación server-side y confiar en el formulario.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — API auth:** Tests auth + README en `projects/m17-agenda-ops/README.md`.
- **P2 — Front:** `projects/m17-agenda-ops/docs/ui-estados.md` (o capturas en repo).
- **P3 — Admin:** Demo roles + `integracion-whatsapp.md`.
- **Proyecto — Piloto:** Deploy HTTPS + checklist camino a SaaS marcado o gaps documentados.

## Criterios de dominio

- [ ] Usuario nuevo se onboardea sin ti (README + UX clara).
- [ ] Roles se respetan en API (demo reproducible staff vs owner).
- [ ] ADR de multi-tenant existe y es coherente con M09/M12.
- [ ] Piloto desplegado en HTTPS accesible para demo del design partner.
