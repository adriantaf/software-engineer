---
id: L10
materia: M18
orden: 10
titulo: CSRF en formularios y mutaciones state-changing
horas: 5.0
semana: 3
lectura: CSRF Prevention Cheat Sheet
evidencia: fix + projects/m18-appsec/csrf-notes.md
---

# L10 — CSRF en formularios y mutaciones state-changing

**~5.0 h · Semana 3**

Si usas cookies de sesión, CSRF importa.

## Objetivo

PoC CSRF (en tu app) o justificación SameSite+método; mitigación (token o SameSite estricto).

## Pasos (hazlos en orden)

### 1. Analiza superficie (40 min)

POST/PATCH/DELETE que cambian estado con cookie.

### 2. PoC controlada (60–80 min)

HTML local que intenta mutar. Documenta resultado.

### 3. Mitiga (40 min)

Token CSRF o política SameSite+JSON-only documentada.

### 4. Commit

`fix(m18): l10 csrf mitigacion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | CSRF Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Lista rutas mutables (artefacto: `fix`).
2. ≥1 ruta protegida (artefacto: `fix`).
3. curl sin token falla (artefacto: `fix`).
4. Commit `docs(m18): L10 csrf-en-formularios-y-mutaciones-state-changing`.

## Errores comunes

- Confiar solo en CORS.
- GET que borra datos.

## Siguiente

[L11 — Fijación de sesión y logout completo](L11-fijacion-de-sesion-y-logout-completo.md)
