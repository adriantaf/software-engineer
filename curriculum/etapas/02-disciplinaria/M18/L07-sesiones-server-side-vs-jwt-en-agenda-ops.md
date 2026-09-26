---
id: L07
materia: M18
orden: 7
titulo: Sesiones server-side vs JWT en Agenda Ops
horas: 5.0
semana: 2
lectura: Session Management + JWT Cheat Sheets
evidencia: projects/m18-appsec/adr-sesion-vs-jwt.md (o enlace ADR M13)
---

# L07 — Sesiones server-side vs JWT en Agenda Ops

**~5.0 h · Semana 2**

Elige o ratifica con ADR corto de seguridad.

## Objetivo

`docs/adr-sesion-vs-jwt.md` + riesgos XSS/CSRF de la opción.

## Pasos (hazlos en orden)

### 1. Compara (50 min)

Tabla pros/contras en contexto panel+API same-site vs SPA cross-origin.

### 2. ADR (60–70 min)

Decisión, mitigaciones obligatorias (HttpOnly, TTL, revoke).

### 3. Commit

`docs(m18): l07 adr sesion jwt`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Session Management + JWT Cheat Sheets | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ADR con alternativas (artefacto: `projects/m18-appsec/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
2. Prueba logout/reuse documentada (artefacto: `projects/m18-appsec/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
3. Coherente con móvil futuro (artefacto: `projects/m18-appsec/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
4. Commit `docs(m18): L07 sesiones-server-side-vs-jwt-en-agenda-ops`.

## Errores comunes

- JWT en localStorage sin plan anti-XSS.
- Sin estrategia de revocación.

## Siguiente

[L08 — Threat model v1 post-autenticación (P1)](L08-threat-model-v1-post-autenticacion-p1.md)
