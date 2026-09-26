---
id: L28
materia: M18
orden: 28
titulo: CSP básica sin romper Agenda Ops
horas: 5.0
semana: 7
lectura: Content Security Policy Cheat Sheet
evidencia: projects/m18-appsec/csp.md + commit opcional
---

# L28 — CSP básica sin romper Agenda Ops

**~5.0 h · Semana 7**

CSP report-only o enforce gradual.

## Objetivo

CSP que no rompa panel; documenta excepciones.

## Pasos (hazlos en orden)

### 1. Política borrador (50 min)

default-src 'self'; script-src cuidadoso.

### 2. Prueba UI (70–90 min)

Login, agenda, WA link. Ajusta.

### 3. Commit

`feat(m18): l28 csp basica`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Content Security Policy Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Política escrita (artefacto: `projects/m18-appsec/csp.md`).
2. Prueba report-only o estricta (artefacto: `projects/m18-appsec/csp.md`).
3. Sin romper build (artefacto: `projects/m18-appsec/csp.md`).
4. Commit `docs(m18): L28 csp-basica-sin-romper-agenda-ops`.

## Errores comunes

- `unsafe-inline` everywhere.
- CSP en meta sin HTTPS.

## Siguiente

[L29 — Pipeline CI: lint, test, audit, anti-secretos](L29-pipeline-ci-lint-test-audit-anti-secretos.md)
