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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - hash

      - registro

      - validación


      **Objetivo de esta lección:** Implementar registro: validar
      email/password, hash fuerte, persistir usuario ligado al negocio piloto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura OWASP Password Storage
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Migración usuarios
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Registro con hash de contraseña», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Registro con hash de
          contraseña
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “MD5/SHA sin salt como ‘hash’."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Implementar registro: validar email/password, hash fuerte, persistir
          usuario ligado al negocio piloto.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: POST /auth/register
    xp: 10
    cuerpo: >-
      Valida body (Zod/valibot): email, password ≥8. Hash con bcrypt/argon2.
      Respuesta **201** sin el hash.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
