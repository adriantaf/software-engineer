---
id: L09
materia: M18
orden: 9
titulo: Cookies Secure, HttpOnly y SameSite
horas: 5.0
semana: 3
lectura: OWASP Session Management + cookie flags
evidencia: projects/m18-appsec/cookies-lab.md
---

# L09 — Cookies Secure, HttpOnly y SameSite

**~5.0 h · Semana 3**

Atributos correctos o sesión robable.

## Objetivo

Checklist de cookie de sesión en staging/local documentado; fix flags faltantes.

## Pasos (hazlos en orden)

### 1. Inspección (40 min)

DevTools / `Set-Cookie` en login.

### 2. Hardening (70–90 min)

Secure (prod), HttpOnly, SameSite=Lax o Strict justificado.

### 3. Evidencia (20 min)

Captura headers redactados en `pocs/cookies.md`.

### 4. Commit

`fix(m18): l09 cookie flags`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP Session Management + cookie flags | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla de cookies real (artefacto: `projects/m18-appsec/cookies-lab.md`).
2. Parche o justificación documentada (artefacto: `projects/m18-appsec/cookies-lab.md`).
3. Prueba HttpOnly.
4. Commit `docs(m18): L09 cookies-secure-httponly-y-samesite`.

## Errores comunes

- SameSite=None sin Secure.
- Cookie de sesión accesible desde JS.

## Siguiente

[L10 — CSRF en formularios y mutaciones state-changing](L10-csrf-en-formularios-y-mutaciones-state-changing.md)
