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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Atributos correctos o sesión robable. Hoy aplicas flags en tu stack.


      **Objetivo de esta lección:** Tabla real de cookies en
      `projects/m18-appsec/pocs/cookies.md`; fix Secure/HttpOnly/SameSite si
      faltan.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inspección Set-Cookie
    xp: 10
    cuerpo: |-
      ```bash
      curl -sI -X POST localhost:3000/auth/login \
        -H 'content-type: application/json' \
        -d '{"email":"owner@test.local","password":"***"}' | rg -i 'set-cookie|HTTP/
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta + harden
    xp: 10
    cuerpo: |-
      ```bash
      curl -sI -X POST localhost:3000/auth/login \
        -H 'content-type: application/json' \
        -d '{"email":"owner@test.local","password":"***"}' | rg -i 'set-cookie|HTTP/
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cookies Secure, HttpOnly y SameSite», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cookies Secure,
          HttpOnly y SameSite
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

      `curl -sI -X POST localhost:3000/auth/login \`
    comandoEsperado:
      - 'curl -sI -X POST localhost:3000/auth/login \'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sI -X POST localhost:3000/auth/login \'
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
          Tabla real de cookies en `projects/m18-appsec/pocs/cookies.md`; fix
          Secure/HttpOnly/SameSite si faltan.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Cookie de sesión accesible desde JS."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
