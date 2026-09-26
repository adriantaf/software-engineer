---
id: L02
materia: M17
orden: 2
titulo: Registro con hash de contraseña
horas: 5.0
semana: 1
lectura: OWASP Password Storage + bcrypt/argon2
evidencia: POST /auth/register
---

# L02 — Registro con hash de contraseña

**~5.0 h · Semana 1**

Agenda Ops no admite usuarios en texto plano. Hoy nace `POST /auth/register`.

## Objetivo

Registro con validación (email/password), hash bcrypt/argon2 y usuario ligado al negocio piloto.

## Pasos (hazlos en orden)

### 1. Lectura OWASP Password Storage (25–35 min)

Cheat Sheet: cost factor, no MD5/SHA solo, never log passwords.

### 2. Esquema usuarios (30–40 min)

Tabla `usuarios` (o migración): email único, `password_hash`, `rol`, `negocio_id`/`tenant_id` nullable documentado. Sin password en claro.

### 3. Endpoint register (70–90 min)

`POST /auth/register` con Zod/valibot: email válido, password ≥8 (o política documentada). Respuesta 201 sin devolver el hash. 400 en inválido.

### 4. Tests (40–50 min)

```bash
npm test -- auth   # o vitest filter
```

Casos: 201 feliz; 400 email malo; hash ≠ plaintext en DB.

### 5. Commit

`feat(m17): l02 register con hash`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | OWASP Password Storage + bcrypt/argon2 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Register funciona (artefacto: `POST /auth/register`).
2. Hash no reversible (artefacto: `POST /auth/register`).
3. Test 400 (artefacto: `POST /auth/register`).
4. Commit `docs(m17): L02 registro-con-hash-de-contrasena`.

## Errores comunes

- MD5.
- Password en logs.

## Siguiente

[L03 — Login, sesión y GET /me protegido](L03-login-sesion-y-get-me-protegido.md)
