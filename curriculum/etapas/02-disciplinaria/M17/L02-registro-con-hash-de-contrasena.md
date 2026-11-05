---
id: L02
materia: M17
orden: 2
titulo: Registro con hash de contraseña
horas: 5
semana: 1
lectura: OWASP Password Storage + bcrypt/argon2
evidencia: POST /auth/register
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar registro: validar email/password, hash fuerte,
      persistir usuario ligado al negocio piloto.


      - hash

      - registro

      - validación
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura OWASP Password Storage
    xp: 10
    cuerpo: |-
      ```sql
      -- migrations/00x_usuarios.sql (adapta a tu ORM)
      CREATE TABLE usuarios (
        id UUID PRIMARY KEY,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        rol TEXT NOT NULL CHECK (rol IN ('owner','staff')),
        negocio_id UUID NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT now()
      );
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Registro con hash de contraseña" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: POST /auth/register
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “MD5/SHA sin salt como ‘hash’."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar registro: validar email/password, hash fuerte, persistir
          usuario ligado al negocio piloto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Migración usuarios
    xp: 10
    cuerpo: |-
      ```sql
      -- migrations/00x_usuarios.sql (adapta a tu ORM)
      CREATE TABLE usuarios (
        id UUID PRIMARY KEY,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        rol TEXT NOT NULL CHECK (rol IN ('owner','staff')),
        negocio_id UUID NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT now()
      );
      ```

      ```bash
      aplica con tu runner, ej.:
      npm run migrate
      o: psql "$DATABASE_URL" -f migrations/00x_usuarios.sql
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. POST /auth/register
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -X POST http://localhost:3000/auth/register \
        -H 'content-type: application/json' \
        -d '{"email":"owner@demo.local","password":"Secreto123!"}'
      # 201 + id/email/rol — nunca password_hash
      curl -sS -X POST http://localhost:3000/auth/register \
        -H 'content-type: application/json' \
        -d '{"email":"malo","password":"x"}'
      # 400
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`POST /auth/register` crea usuario con `password_hash` (bcrypt/argon2).'
      - >-
        Test 201 feliz y 400 email inválido en suite auth (artefacto: `POST
        /auth/register`).
      - 'Respuesta 201 no incluye el hash (artefacto: `POST /auth/register`).'
      - 'Commit `docs(m17): L02 registro-con-hash-de-contrasena`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L02 — Registro con hash de contraseña

**~5.0 h · Semana 1**

Auth real desde el MVP — no usuarios en texto plano.

## Objetivo

Implementar registro: validar email/password, hash fuerte, persistir usuario ligado al negocio piloto.

## Conceptos clave

- hash
- registro
- validación

## Pasos (hazlos en orden)

### 1. Lectura OWASP Password Storage (25–35 min)

Abre la Cheat Sheet (enlace en la tabla). Anota en `docs/auth.md`: algoritmo (bcrypt/argon2), cost factor, y “nunca MD5/SHA solo”.

### 2. Migración usuarios (30–40 min)

```sql
-- migrations/00x_usuarios.sql (adapta a tu ORM)
CREATE TABLE usuarios (
  id UUID PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  rol TEXT NOT NULL CHECK (rol IN ('owner','staff')),
  negocio_id UUID NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

```bash
# aplica con tu runner, ej.:
npm run migrate
# o: psql "$DATABASE_URL" -f migrations/00x_usuarios.sql
```

### 3. POST /auth/register (70–90 min)

Valida body (Zod/valibot): email, password ≥8. Hash con bcrypt/argon2. Respuesta **201** sin el hash.

```bash
curl -sS -X POST http://localhost:3000/auth/register \
  -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"Secreto123!"}'
# 201 + id/email/rol — nunca password_hash
curl -sS -X POST http://localhost:3000/auth/register \
  -H 'content-type: application/json' \
  -d '{"email":"malo","password":"x"}'
# 400
```

### 4. Tests + commit (40–50 min)

```bash
npm test -- auth
git add projects/m17-vitrina
git commit -m "feat(m17): L02 register con hash"
```

Casos mínimos: 201 feliz; 400 email inválido; hash ≠ plaintext en DB.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | OWASP Password Storage + bcrypt/argon2 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `POST /auth/register` crea usuario con `password_hash` (bcrypt/argon2).
2. Test 201 feliz y 400 email inválido en suite auth (artefacto: `POST /auth/register`).
3. Respuesta 201 **no** incluye el hash (artefacto: `POST /auth/register`).
4. Commit `docs(m17): L02 registro-con-hash-de-contrasena`.

## Errores comunes

- MD5/SHA sin salt como ‘hash’.
- Loguear password o hash en claro.
- Devolver `password_hash` en JSON.

## Siguiente

[L03 — Login, sesión y GET /me protegido](L03-login-sesion-y-get-me-protegido.md)
