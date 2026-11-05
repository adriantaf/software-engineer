---
id: L03
materia: M17
orden: 3
titulo: 'Login, sesión y GET /me protegido'
horas: 5
semana: 1
lectura: MDN cookies + ADR sesión M13
evidencia: POST /auth/login + GET /me
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - sesión

      - 401

      - HttpOnly


      **Objetivo de esta lección:** Login con cookie HttpOnly o JWT en cookie;
      `GET /me` devuelve 401 sin credencial.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Decide sesión vs JWT-cookie
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m17-vitrina/docs
      cat > projects/m17-vitrina/docs/auth.md << 'EOF'
      # Auth Vitrina
      - Mecanismo: cookie HttpOnly (preferido) / JWT-en-cookie
      - Secure / SameSite: ...
      - Riesgos XSS/CSRF y mitigación
      EOF
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Implementa login + GET /me
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -c /tmp/ao.ck -X POST http://localhost:3000/auth/login \
        -H 'content-type: application/json' \
        -d '{"email":"owner@demo.local","password":"Secreto123!"}'
      curl -sS -b /tmp/ao.ck http://localhost:3000/me
      curl -sS -o /tmp/me.out -w "%{http_code}" http://localhost:3000/me
      # sin cookie → 401
      ```

      Login verifica hash; setea cookie. `GET /me` → id, email, rol (sin hash).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Login, sesión y GET /me protegido», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Login, sesión y GET /me
          protegido
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `mkdir -p projects/m17-vitrina/docs`
    comandoEsperado:
      - mkdir -p projects/m17-vitrina/docs
      - 'curl -sS -c /tmp/ao.ck -X POST http://localhost:3000/auth/login \'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m17-vitrina/docs'
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
          Login con cookie HttpOnly o JWT en cookie; `GET /me` devuelve 401 sin
          credencial.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests 401/200 + commit
    xp: 10
    cuerpo: |-
      ```bash
      npm test -- auth
      git add projects/m17-vitrina/docs/auth.md projects/m17-vitrina
      git commit -m "feat(m17): L03 login sesion y me"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m17-vitrina/docs/auth.md` documenta cookie HttpOnly o
        JWT-cookie.
      - '`POST /auth/login` + `GET /me` 200 con sesión; sin cookie → 401.'
      - 'Tests cubren login→me y 401 (artefacto: `POST /auth/login`).'
      - 'Commit `docs(m17): L03 login-sesion-y-get-me-protegido`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L03 — Login, sesión y GET /me protegido

**~5.0 h · Semana 1**

El panel Vitrina necesita identidad servidor-confiable.

## Objetivo

Login con cookie HttpOnly o JWT en cookie; `GET /me` devuelve 401 sin credencial.

## Conceptos clave

- sesión
- 401
- HttpOnly

## Pasos (hazlos en orden)

### 1. Decide sesión vs JWT-cookie (20–30 min)

```bash
mkdir -p projects/m17-vitrina/docs
cat > projects/m17-vitrina/docs/auth.md << 'EOF'
# Auth Vitrina
- Mecanismo: cookie HttpOnly (preferido) / JWT-en-cookie
- Secure / SameSite: ...
- Riesgos XSS/CSRF y mitigación
EOF
```

### 2. Implementa login + GET /me (80–100 min)

Login verifica hash; setea cookie. `GET /me` → id, email, rol (sin hash).

```bash
curl -sS -c /tmp/ao.ck -X POST http://localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"Secreto123!"}'
curl -sS -b /tmp/ao.ck http://localhost:3000/me
curl -sS -o /tmp/me.out -w "%{http_code}" http://localhost:3000/me
# sin cookie → 401
```

### 3. Tests 401/200 + commit (40–50 min)

```bash
npm test -- auth
git add projects/m17-vitrina/docs/auth.md projects/m17-vitrina
git commit -m "feat(m17): L03 login sesion y me"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | MDN cookies + ADR sesión M13 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/auth.md` documenta cookie HttpOnly o JWT-cookie.
2. `POST /auth/login` + `GET /me` 200 con sesión; sin cookie → 401.
3. Tests cubren login→me y 401 (artefacto: `POST /auth/login`).
4. Commit `docs(m17): L03 login-sesion-y-get-me-protegido`.

## Errores comunes

- JWT en localStorage sin justificar XSS.
- `GET /me` sin auth devuelve 200.
- Devolver row completo con hash.

## Siguiente

[L04 — Cierre semana 1 — suite auth P1](L04-cierre-semana-1-suite-auth-p1.md)
