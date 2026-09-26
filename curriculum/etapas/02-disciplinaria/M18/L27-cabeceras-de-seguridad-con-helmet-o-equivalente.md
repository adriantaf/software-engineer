---
id: L27
materia: M18
orden: 27
titulo: Cabeceras de seguridad con Helmet o equivalente
horas: 5.0
semana: 7
lectura: Security Headers Cheat Sheet
evidencia: commit headers + captura curl
---

# L27 — Cabeceras de seguridad con Helmet o equivalente

**~5.0 h · Semana 7**

Confirma headers en staging; completa gaps M17.

## Objetivo

Headers activos verificados; doc en appsec.

## Pasos (hazlos en orden)

### 1. curl -I (40 min)

### 2. Ajustes (60–80 min)

X-Content-Type-Options, Frame, Referrer-Policy, etc.

### 3. Commit

`fix(m18): l27 security headers`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Security Headers Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Headers visibles en staging (artefacto: `commit headers`).
2. Login sigue funcionando (artefacto: `commit headers`).
3. Commit (artefacto: `commit headers`).

## Errores comunes

- HSTS en localhost sin TLS.
- CSP rota todo sin reporte.

## Siguiente

[L28 — CSP básica sin romper Agenda Ops](L28-csp-basica-sin-romper-agenda-ops.md)
