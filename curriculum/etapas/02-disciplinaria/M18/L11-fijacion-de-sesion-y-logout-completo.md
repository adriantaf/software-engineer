---
id: L11
materia: M18
orden: 11
titulo: Fijación de sesión y logout completo
horas: 5.0
semana: 3
lectura: Session fixation + logout best practices
evidencia: projects/m18-appsec/session-lifecycle.md
---

# L11 — Fijación de sesión y logout completo

**~5.0 h · Semana 3**

Login debe rotar session id; logout debe invalidar servidor.

## Objetivo

Demo: session id cambia post-login; logout invalida; test o checklist.

## Pasos (hazlos en orden)

### 1. Prueba fijación (50–60 min)

Intenta fijar cookie pre-login (en tu local). Documenta.

### 2. Logout servidor (50–60 min)

Almacén de sesiones: borrar id. JWT: blacklist/TTL corto documentado.

### 3. Commit

`fix(m18): l11 session fixation logout`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Session fixation + logout best practices | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Doc ciclo de vida (artefacto: `projects/m18-appsec/session-lifecycle.md`).
2. Pruebas login/logout documentadas (artefacto: `projects/m18-appsec/session-lifecycle.md`).
3. Commit si hubo fix (artefacto: `projects/m18-appsec/session-lifecycle.md`).

## Errores comunes

- Logout solo borra cookie cliente.
- Session id pre-login reutilizado.

## Siguiente

[L12 — Checklist cookies y CSRF en staging](L12-checklist-cookies-y-csrf-en-staging.md)
