---
id: L03
materia: M17
orden: 3
titulo: Login, sesión y GET /me protegido
horas: 5.0
semana: 1
lectura: MDN cookies + ADR sesión M13
evidencia: POST /auth/login + GET /me
---

# L03 — Login, sesión y GET /me protegido

**~5.0 h · Semana 1**

El panel necesita identidad servidor-confiable: cookie HttpOnly (preferida) o JWT en cookie documentada.

## Objetivo

`POST /auth/login` + `GET /me` con 401 sin credencial; documentar elección en `docs/auth.md`.

## Pasos (hazlos en orden)

### 1. Decide sesión vs JWT-cookie (20–30 min)

Escribe en `docs/auth.md`: opción, por qué, riesgos XSS/CSRF. Evita localStorage sin justificar.

### 2. Implementa login + me (80–100 min)

Login verifica hash; setea cookie Secure/HttpOnly/SameSite (en local puedes relajar Secure documentándolo). `GET /me` lee sesión y devuelve id, email, rol — no el hash.

### 3. Tests 401/200 (40–50 min)

Login → me 200; request sin cookie → 401; password malo → 401 (sin filtrar “email existe” si puedes).

### 4. Commit

`feat(m17): l03 login sesion y me`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | MDN cookies + ADR sesión M13 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Login+me (artefacto: `POST /auth/login`).
2. 401 test (artefacto: `POST /auth/login`).
3. auth.md (artefacto: `POST /auth/login`).
4. Commit `docs(m17): L03 login-sesion-y-get-me-protegido`.

## Errores comunes

- JWT localStorage sin doc.
- Me devuelve todo el row.

## Siguiente

[L04 — Cierre semana 1 — suite auth P1](L04-cierre-semana-1-suite-auth-p1.md)
