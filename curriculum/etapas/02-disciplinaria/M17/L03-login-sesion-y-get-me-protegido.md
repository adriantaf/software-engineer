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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Login con cookie HttpOnly o JWT en cookie; `GET /me`
      devuelve 401 sin credencial.


      - sesión

      - 401

      - HttpOnly
  - id: s2
    tipo: ejemplo
    titulo: 1. Decide sesión vs JWT-cookie
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Login, sesión y GET /me protegido" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: POST /auth/login + GET /me
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `mkdir -p projects/m17-vitrina/docs`
    comandoEsperado:
      - mkdir -p projects/m17-vitrina/docs
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m17-vitrina/docs'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Login con cookie HttpOnly o JWT en cookie; `GET /me` devuelve 401 sin
          credencial.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementa login + GET /me
    xp: 10
    cuerpo: |-
      Login verifica hash; setea cookie. `GET /me` → id, email, rol (sin hash).

      ```bash
      curl -sS -c /tmp/ao.ck -X POST http://localhost:3000/auth/login \
        -H 'content-type: application/json' \
        -d '{"email":"owner@demo.local","password":"Secreto123!"}'
      curl -sS -b /tmp/ao.ck http://localhost:3000/me
      curl -sS -o /tmp/me.out -w "%{http_code}" http://localhost:3000/me
      sin cookie → 401
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Tests 401/200 + commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
