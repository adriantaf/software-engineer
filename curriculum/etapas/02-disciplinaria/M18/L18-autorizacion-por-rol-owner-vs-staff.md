---
id: L18
materia: M18
orden: 18
titulo: Autorización por rol owner vs staff
horas: 5.0
semana: 5
lectura: Access Control Cheat Sheet
evidencia: projects/m18-appsec/rbac-matrix.md
---

# L18 — Autorización por rol owner vs staff

**~5.0 h · Semana 5**

Matriz M17 debe cumplirse en servidor.

## Objetivo

Tests 403 staff→admin; hallazgos si UI ocultaba y API no.

## Pasos (hazlos en orden)

### 1. Matriz vs código (40 min)

Diff permisos.md vs middleware.

### 2. Tests roles (80–100 min)

Cobertura de acciones Deny.

### 3. Commit

`test(m18): l18 authz roles owner staff`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Access Control Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Matriz completa (artefacto: `projects/m18-appsec/rbac-matrix.md`).
2. ≥1 prueba manual rol (artefacto: `projects/m18-appsec/rbac-matrix.md`).
3. Gaps listados (artefacto: `projects/m18-appsec/rbac-matrix.md`).
4. Commit `docs(m18): L18 autorizacion-por-rol-owner-vs-staff`.

## Errores comunes

- Un solo rol ‘admin’.
- 404 para esconder sin authz.

## Siguiente

[L19 — Rate limiting en login y endpoints sensibles](L19-rate-limiting-en-login-y-endpoints-sensibles.md)
