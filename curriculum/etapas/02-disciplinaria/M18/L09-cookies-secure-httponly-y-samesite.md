---
id: L09
materia: M18
orden: 9
titulo: 'Cookies Secure, HttpOnly y SameSite'
horas: 5
semana: 3
lectura: OWASP Session Management + cookie flags
evidencia: projects/m18-appsec/pocs/cookies.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Tabla real de cookies en
      `projects/m18-appsec/pocs/cookies.md`; fix Secure/HttpOnly/SameSite si
      faltan.


      Atributos correctos o sesión robable. Hoy aplicas flags en tu stack.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inspección Set-Cookie
    xp: 10
    cuerpo: |-
      ```bash
      curl -sI -X POST localhost:3000/auth/login \
        -H 'content-type: application/json' \
        -d '{"email":"owner@test.local","password":"***"}' | rg -i 'set-cookie|HTTP/
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cookies Secure, HttpOnly y SameSite" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/pocs/cookies.md
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

      `curl -sI -X POST localhost:3000/auth/login \`
    comandoEsperado:
      - 'curl -sI -X POST localhost:3000/auth/login \'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sI -X POST localhost:3000/auth/login \'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Tabla real de cookies en `projects/m18-appsec/pocs/cookies.md`; fix
          Secure/HttpOnly/SameSite si faltan.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta + harden
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/pocs/cookies.md <<'EOF'
      Cookies lab
      | Nombre | HttpOnly | Secure | SameSite | Path | Max-Age |
      |--------|----------|--------|----------|------|---------|
      | sid? | | | | | |
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Tabla de cookies real (artefacto:
        `projects/m18-appsec/pocs/cookies.md`).
      - >-
        Parche o justificación documentada (artefacto:
        `projects/m18-appsec/pocs/cookies.md`).
      - 'Commit `docs(m18): L09 cookies-secure-httponly-y-samesite`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Cookies Secure, HttpOnly y SameSite

**~5.0 h · Semana 3**

Atributos correctos o sesión robable. Hoy aplicas flags en tu stack.

## Objetivo

Tabla real de cookies en `projects/m18-appsec/pocs/cookies.md`; fix Secure/HttpOnly/SameSite si faltan.

## Pasos

### 1. Inspección Set-Cookie (30–40 min)

```bash
curl -sI -X POST localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' | rg -i 'set-cookie|HTTP/
```
### 2. Documenta + harden (70–90 min)

```bash
cat > projects/m18-appsec/pocs/cookies.md <<'EOF'
# Cookies lab
| Nombre | HttpOnly | Secure | SameSite | Path | Max-Age |
|--------|----------|--------|----------|------|---------|
| sid? | | | | | |

## Antes / después
- Antes: …
- Después: …
## ¿JS puede leer la cookie de sesión?
document.cookie → …
EOF
```

Ejemplo Express / cookie-session:

```ts
res.cookie("sid", sessionId, {
  httpOnly: true,
  secure: process.env.NODE_ENV === "production",
  sameSite: "lax", // o "strict" si no hay cross-site legítimo
  path: "/",
});
```
### 3. Prueba HttpOnly (20 min)

En DevTools Console (sesión logueada): `document.cookie` no debe mostrar la cookie de sesión. Captura redactada en `pocs/cookies.md`.
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/pocs/cookies.md
git commit -m "fix(m18): l09 cookie flags"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP Session Management + cookie flags | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla de cookies real (artefacto: `projects/m18-appsec/pocs/cookies.md`).
2. Parche o justificación documentada (artefacto: `projects/m18-appsec/pocs/cookies.md`).
3. Commit `docs(m18): L09 cookies-secure-httponly-y-samesite`.

## Errores comunes

- SameSite=None sin Secure.
- Cookie de sesión accesible desde JS.

## Siguiente

[L10 — CSRF en formularios y mutaciones state-changing](L10-csrf-en-formularios-y-mutaciones-state-changing.md)
