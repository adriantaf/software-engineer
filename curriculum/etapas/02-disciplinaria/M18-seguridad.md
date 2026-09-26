---
id: M18
titulo: Seguridad del software (AppSec)
etapa: disciplinaria
orden: 18
semanas: 8
horas: 160
practicas:
  - id: p1
    titulo: Threat model STRIDE del CRM (documento)
  - id: p2
    titulo: Reproducir y corregir ≥5 hallazgos OWASP en tu app
  - id: p3
    titulo: Checklist Secure SDLC en CI (audit, secrets, headers)
proyecto:
  id: proj
  titulo: Informe AppSec + PR de hardening con tests de regresión
---

# M18 — Seguridad del software (AppSec)

## Por qué existe

Es la **capa B** de la pista de ciberseguridad. Un ingeniero que “sabe hacer CRUDs” pero deja SQLi/XSS/IDOR **no es competente**. Aquí aprendes a **modelar amenazas, romper (solo tu sistema) y reparar**.

**En resumen:** amenazas → PoC en **tu** app → fix → test. Las siglas azules están en el glosario.


## Objetivos de aprendizaje

1. Hacer threat modeling ligero (STRIDE) de tu producto.
2. Explicar y mitigar el OWASP Top 10 en código real.
3. Diseñar auth (hashing, sesiones/JWT, CSRF) sin inventar crypto.
4. Meter seguridad en el pipeline (secrets, `npm audit`, headers).
5. Escribir tests que fallen si reaparece una vulnerabilidad básica.

## Cómo estudiar esta materia (lecciones)

M18 es la **capa B** de AppSec con lecciones L01–L32 (formato M01): amenaza → PoC en **tu** Agenda Ops → fix → test.

1. Orden **L01 → L32**; marca solo con “Hecho cuando” cumplido.
2. **Solo** atacas localhost/staging que controlas.
3. Evidencia en `projects/m18-appsec/` y commits de hardening en el repo del producto.
4. OWASP Top 10 y Cheat Sheets en español; mapa cada lectura a un endpoint real.
5. [Cómo estudiar](../../como-estudiar.md) y [hilo seguridad](../../hilos/seguridad.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lecciones OWASP | 10–12 | 4× ~5 h (lectura + lab en tu API) |
| Hallazgos P2 | 4–6 | Tabla PoC → fix → test |
| CI / informe (P3) | 4–6 | Pipeline, headers, informe |
| Retro | 1 | Riesgo residual escrito |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la lectura OWASP de esa lección.

## Lecciones

### Semana 1 — Threat modeling STRIDE y OWASP Top 10 (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Activos, actores y datos sensibles en Agenda Ops](M18/L01-activos-actores-y-datos-sensibles-en-agenda-ops.md) | 5 |
| L02 | [Trust boundaries y flujos de confianza](M18/L02-trust-boundaries-y-flujos-de-confianza.md) | 5 |
| L03 | [STRIDE aplicado al CRM de citas](M18/L03-stride-aplicado-al-crm-de-citas.md) | 5 |
| L04 | [Threat model v0 y lectura OWASP Top 10](M18/L04-threat-model-v0-y-lectura-owasp-top-10.md) | 5 |

### Semana 2 — Autenticación: hashing, sesiones y JWT (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Inventario de autenticación actual](M18/L05-inventario-de-autenticacion-actual.md) | 5 |
| L06 | [Hashing de contraseñas con bcrypt o argon2](M18/L06-hashing-de-contrasenas-con-bcrypt-o-argon2.md) | 5 |
| L07 | [Sesiones server-side vs JWT en Agenda Ops](M18/L07-sesiones-server-side-vs-jwt-en-agenda-ops.md) | 5 |
| L08 | [Threat model v1 post-autenticación (P1)](M18/L08-threat-model-v1-post-autenticacion-p1.md) | 5 |

### Semana 3 — Cookies, CSRF y ciclo de sesión (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Cookies Secure, HttpOnly y SameSite](M18/L09-cookies-secure-httponly-y-samesite.md) | 5 |
| L10 | [CSRF en formularios y mutaciones state-changing](M18/L10-csrf-en-formularios-y-mutaciones-state-changing.md) | 5 |
| L11 | [Fijación de sesión y logout completo](M18/L11-fijacion-de-sesion-y-logout-completo.md) | 5 |
| L12 | [Checklist cookies y CSRF en staging](M18/L12-checklist-cookies-y-csrf-en-staging.md) | 5 |

### Semana 4 — Inyección: SQLi y XSS en Agenda Ops (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [SQLi: reproducir en tu propia API](M18/L13-sqli-reproducir-en-tu-propia-api.md) | 5 |
| L14 | [Mitigar SQLi: queries parametrizadas y permisos DB](M18/L14-mitigar-sqli-queries-parametrizadas-y-permisos-db.md) | 5 |
| L15 | [XSS reflejado en campos de cliente o búsqueda](M18/L15-xss-reflejado-en-campos-de-cliente-o-busqueda.md) | 5 |
| L16 | [XSS almacenado y escape en plantillas/API](M18/L16-xss-almacenado-y-escape-en-plantillas-api.md) | 5 |

### Semana 5 — Control de acceso, IDOR y rate limiting (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L17 | [IDOR en citas y recursos por ID](M18/L17-idor-en-citas-y-recursos-por-id.md) | 5 |
| L18 | [Autorización por rol owner vs staff](M18/L18-autorizacion-por-rol-owner-vs-staff.md) | 5 |
| L19 | [Rate limiting en login y endpoints sensibles](M18/L19-rate-limiting-en-login-y-endpoints-sensibles.md) | 5 |
| L20 | [Tests automatizados cross-user (P2 avance)](M18/L20-tests-automatizados-cross-user-p2-avance.md) | 5 |

### Semana 6 — SSRF, uploads y JSON de confianza (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L21 | [SSRF: superficie en webhooks e integraciones](M18/L21-ssrf-superficie-en-webhooks-e-integraciones.md) | 5 |
| L22 | [Subida de archivos segura](M18/L22-subida-de-archivos-segura.md) | 5 |
| L23 | [Deserialización y JSON peligroso](M18/L23-deserializacion-y-json-peligroso.md) | 5 |
| L24 | [Consolidar hallazgos semana 6 en P2](M18/L24-consolidar-hallazgos-semana-6-en-p2.md) | 5 |

### Semana 7 — Dependencias, secretos, headers y CSP (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L25 | [npm audit y cadena de dependencias](M18/L25-npm-audit-y-cadena-de-dependencias.md) | 5 |
| L26 | [Secretos, .env y rotación](M18/L26-secretos-env-y-rotacion.md) | 5 |
| L27 | [Cabeceras de seguridad con Helmet o equivalente](M18/L27-cabeceras-de-seguridad-con-helmet-o-equivalente.md) | 5 |
| L28 | [CSP básica sin romper Agenda Ops](M18/L28-csp-basica-sin-romper-agenda-ops.md) | 5 |

### Semana 8 — Secure SDLC, informe y tests de regresión (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L29 | [Pipeline CI: lint, test, audit, anti-secretos](M18/L29-pipeline-ci-lint-test-audit-anti-secretos.md) | 5 |
| L30 | [Estructura del informe AppSec](M18/L30-estructura-del-informe-appsec.md) | 5 |
| L31 | [Tests de regresión de seguridad (≥3)](M18/L31-tests-de-regresion-de-seguridad-3.md) | 5 |
| L32 | [Cierre M18 — dominio y riesgo residual](M18/L32-cierre-m18-dominio-y-riesgo-residual.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: **OWASP Top 10** + Cheat Sheets. Ver [bibliografía](../../bibliografia.md) y [hilo seguridad](../../hilos/seguridad.md).

| Semana | Lecciones | Lectura OWASP / recurso | Enfoque Agenda Ops |
|--------|-----------|-------------------------|-------------------|
| 1 | L01–L04 | STRIDE / Threat Modeling | Activos, boundaries, mapa Top 10 |
| 2 | L05–L08 | **A07** Auth + Password Storage | Hashing, sesión/JWT, threat model v1 (P1) |
| 3 | L09–L12 | CSRF + Session Management | Cookies, CSRF, checklist staging |
| 4 | L13–L16 | **A03** Injection + XSS Prevention | SQLi/XSS en citas y clientes |
| 5 | L17–L20 | **A01** Access Control + Rate Limit | IDOR, roles, tests cross-user |
| 6 | L21–L24 | SSRF, File Upload, API hardening | Hallazgos P2 ≥5 |
| 7 | L25–L28 | **A06** + Secrets + Headers + CSP | audit, rotación, Helmet, CSP |
| 8 | L29–L32 | Secure SDLC + informe | CI P3, informe, ≥3 tests seguridad |

**Regla:** hallazgo → PoC en **tu** app → fix → test. Nada de laboratorio genérico sin trasladar al piloto.



## Ejemplo — hashing de contraseñas (idea correcta)

```ts
// Usa una lib madura (p.ej. bcrypt / argon2). NUNCA MD5/SHA solo.
import bcrypt from "bcrypt";

export async function hashPassword(plain: string): Promise<string> {
  return bcrypt.hash(plain, 12);
}

export async function verifyPassword(plain: string, hash: string): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
```

## Ejemplo — IDOR (qué buscar)

Si `GET /api/citas/123` devuelve la cita **sin comprobar** que pertenece al usuario autenticado, tienes IDOR. Fix: autorización por `userId`/rol en el servidor, no solo ocultar botones en el front.



## Prácticas

1. **P1:** Threat model v1 revisado (después de semana 2).
2. **P2:** Tabla hallazgo → PoC (en tu app) → commit de fix → test.
3. **P3:** CI con al menos: lint, test, `npm audit` (o equivalente), grep anti-secretos básico.

## Proyecto útil

Entrega en `projects/m18-appsec/`:

1. Informe AppSec (amenazas, hallazgos, mitigaciones, residual risk).
2. PR/commits de hardening en el repo del producto.
3. ≥3 tests automatizados de seguridad (ej. usuario A no lee recurso de B; input XSS escapado).

## Errores comunes

- “Security by obscurity” (ocultar rutas admin sin auth).
- Guardar JWT en `localStorage` sin entender XSS.
- Inventar cifrado casero.
- Atacar sitios ajenos (ilegal e inútil para tu egreso).

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — STRIDE:** Documento de threat model v1.
- **P2 — ≥5 hallazgos:** Tabla PoC → commit fix → test.
- **P3 — CI:** Lint+test+audit (+ grep secretos).
- **Proyecto — Informe:** `projects/m18-appsec/` + PRs hardening.

## Criterios de dominio

- [ ] Explicas SQLi y XSS con ejemplo y mitigación.
- [ ] Tu app no lee recursos cross-user (demo + test).
- [ ] No hay secretos en el historial de git del producto.
- [ ] Tienes checklist pre-deploy de seguridad y la usas.
