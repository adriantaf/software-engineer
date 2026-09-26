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

## Cómo estudiar esta materia (lecciones)

M17 construye el **MVP web Agenda Ops** con profundidad: L01–L32 (8 semanas × 4 lecciones).

1. Lee [producto-saas.md](../../producto-saas.md) y el paquete M13 antes de la semana 2.
2. **Vertical slices:** cada semana una historia completa (API + UI + test mínimo cuando aplique).
3. Cada endpoint sensible: test 401/403 antes de pulir CSS.
4. Evidencia en `projects/m17-agenda-ops/`; stack fijo en `stack.md`.
5. [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth + API | 6–8 | 4 lecciones de la semana |
| Front / integración | 6–8 | Rutas, estados, WhatsApp según semana |
| Tests + docs | 4–6 | ADR, deploy, checklist |
| Retro | 1 | Gap honesto hacia M18/M19 |

Si un día solo tienes 2 h: **una lección** con commit demostrable.

## Lecciones

### Semana 1 — Auth, usuarios y fundación (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Scaffold Agenda Ops — API, DB y stack.md](M17/L01-scaffold-agenda-ops-api-db-y-stack-md.md) | 5 |
| L02 | [Registro con hash de contraseña](M17/L02-registro-con-hash-de-contrasena.md) | 5 |
| L03 | [Login, sesión y GET /me protegido](M17/L03-login-sesion-y-get-me-protegido.md) | 5 |
| L04 | [Cierre semana 1 — suite auth P1](M17/L04-cierre-semana-1-suite-auth-p1.md) | 5 |

### Semana 2 — CRUD citas, clientes y servicios (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Modelo de dominio citas, clientes y servicios](M17/L05-modelo-de-dominio-citas-clientes-y-servicios.md) | 5 |
| L06 | [API citas — crear y listar con reglas](M17/L06-api-citas-crear-y-listar-con-reglas.md) | 5 |
| L07 | [CRUD clientes y servicios](M17/L07-crud-clientes-y-servicios.md) | 5 |
| L08 | [Seeds demo y datos design partner](M17/L08-seeds-demo-y-datos-design-partner.md) | 5 |

### Semana 3 — Roles owner/staff y admin (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Matriz de permisos owner y staff](M17/L09-matriz-de-permisos-owner-y-staff.md) | 5 |
| L10 | [Middleware de autorización en API](M17/L10-middleware-de-autorizacion-en-api.md) | 5 |
| L11 | [Panel admin mínimo — gestión staff](M17/L11-panel-admin-minimo-gestion-staff.md) | 5 |
| L12 | [Demo roles y inicio P3 WhatsApp](M17/L12-demo-roles-y-inicio-p3-whatsapp.md) | 5 |

### Semana 4 — Front serio y estados UX (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Scaffold front y rutas protegidas](M17/L13-scaffold-front-y-rutas-protegidas.md) | 5 |
| L14 | [Flujo login/logout en UI](M17/L14-flujo-login-logout-en-ui.md) | 5 |
| L15 | [Listas con loading, error y vacío](M17/L15-listas-con-loading-error-y-vacio.md) | 5 |
| L16 | [Formularios citas y clientes accesibles](M17/L16-formularios-citas-y-clientes-accesibles.md) | 5 |

### Semana 5 — WhatsApp e integración (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L17 | [Deep links WhatsApp — diseño del mensaje](M17/L17-deep-links-whatsapp-diseno-del-mensaje.md) | 5 |
| L18 | [Botón enviar recordatorio desde ficha cita](M17/L18-boton-enviar-recordatorio-desde-ficha-cita.md) | 5 |
| L19 | [Confirmación de cita y estados](M17/L19-confirmacion-de-cita-y-estados.md) | 5 |
| L20 | [Cierre P3 integración WhatsApp](M17/L20-cierre-p3-integracion-whatsapp.md) | 5 |

### Semana 6 — Deploy HTTPS y smoke tests (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L21 | [Variables de entorno y secrets](M17/L21-variables-de-entorno-y-secrets.md) | 5 |
| L22 | [Deploy staging en PaaS](M17/L22-deploy-staging-en-paas.md) | 5 |
| L23 | [HTTPS y health checks](M17/L23-https-y-health-checks.md) | 5 |
| L24 | [Smoke test post-deploy](M17/L24-smoke-test-post-deploy.md) | 5 |

### Semana 7 — Hardening ligero y CI (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L25 | [Mapa OWASP Top 10 en el piloto](M17/L25-mapa-owasp-top-10-en-el-piloto.md) | 5 |
| L26 | [Headers de seguridad y CORS prod](M17/L26-headers-de-seguridad-y-cors-prod.md) | 5 |
| L27 | [Rate limit en login](M17/L27-rate-limit-en-login.md) | 5 |
| L28 | [Tests auth en CI o script local reproducible](M17/L28-tests-auth-en-ci-o-script-local-reproducible.md) | 5 |

### Semana 8 — Checklist camino a SaaS y cierre (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L29 | [ADR tenant_id y modelo multi-negocio](M17/L29-adr-tenant-id-y-modelo-multi-negocio.md) | 5 |
| L30 | [Checklist camino a SaaS](M17/L30-checklist-camino-a-saas.md) | 5 |
| L31 | [Demo grabable para design partner](M17/L31-demo-grabable-para-design-partner.md) | 5 |
| L32 | [Cierre M17 — evidencias, dominio y handoff M19](M17/L32-cierre-m17-evidencias-dominio-y-handoff-m19.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: MDN Web Docs (ES) + docs del framework + OWASP Top 10 overview + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md#m17-aplicaciones-web).

| Semana | Lecciones | Lectura | Alternativa |
|--------|-----------|---------|-------------|
| 1 | L01–L04 | MDN auth/cookies + ADR sesión M13 | OWASP Auth Cheat Sheet |
| 2 | L05–L08 | SRS M12 + modelo citas M13/M09 | — |
| 3 | L09–L12 | Control de acceso / `permisos.md` | OWASP Access Control |
| 4 | L13–L16 | MDN forms/a11y + handoff M16 | `ui-estados.md` |
| 5 | L17–L20 | WhatsApp / deep links (docs oficiales) | `integracion-whatsapp.md` |
| 6 | L21–L24 | Deploy PaaS + HTTPS | `smoke-test.md` |
| 7 | L25–L28 | OWASP Top 10 mapa + rate limit | hilo seguridad |
| 8 | L29–L32 | Multi-tenant ADR + checklist ficha | Demo design partner |

**Regla:** cada semana deja el piloto más demoable; la lectura sirve al commit.



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
