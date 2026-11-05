---
id: L11
materia: M18
orden: 11
titulo: Fijación de sesión y logout completo
horas: 5
semana: 3
lectura: Session fixation + logout best practices
evidencia: projects/m18-appsec/docs/session-lifecycle.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Ciclo de vida en
      `projects/m18-appsec/docs/session-lifecycle.md`: rotate post-login +
      destroy server-side en logout.


      Robar sesión fija es clásico en apps que reutilizan el mismo session id.
  - id: s2
    tipo: ejemplo
    titulo: 1. Traza el ciclo en código
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'regenerate|session\.id|destroy|logout|revoke' -g '!node_modules' |
      head -30

      cat > projects/m18-appsec/docs/session-lifecycle.md <<'EOF'

      # Session lifecycle

      1. Pre-login id: …

      2. Post-login (¿rota?): …

      3. Logout server-side: …

      4. Request posterior con cookie vieja: esperado 401

      EOF

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Fijación de sesión y logout completo" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/docs/session-lifecycle.md
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

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Ciclo de vida en `projects/m18-appsec/docs/session-lifecycle.md`:
          rotate post-login + destroy server-side en logout.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Pruebas login/logout
    xp: 10
    cuerpo: >-
      ```bash

      Dos logins: ¿cambia el valor de Set-Cookie?

      curl -sI -X POST localhost:3000/auth/login -H 'content-type:
      application/json' \
        -d '{"email":"owner@test.local","password":"***"}' | rg -i set-cookie
      Logout + reuse (debe fallar)

      curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout

      curl -b /tmp/m18-cj -s -o /dev/null -w "%{http_code}\n"
      localhost:3000/api/pedidos

      ```


      Si JWT stateless: documenta deny-list o TTL corto en el mismo archivo.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m18-appsec/docs/session-lifecycle.md
      git commit -m "fix(m18): l11 session lifecycle"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Doc ciclo de vida (artefacto:
        `projects/m18-appsec/docs/session-lifecycle.md`).
      - >-
        Pruebas login/logout documentadas (artefacto:
        `projects/m18-appsec/docs/session-lifecycle.md`).
      - 'Commit `docs(m18): L11 fijacion-de-sesion-y-logout-completo`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — Fijación de sesión y logout completo

**~5.0 h · Semana 3**

Robar sesión fija es clásico en apps que reutilizan el mismo session id.

## Objetivo

Ciclo de vida en `projects/m18-appsec/docs/session-lifecycle.md`: rotate post-login + destroy server-side en logout.

## Pasos

### 1. Traza el ciclo en código (40–50 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'regenerate|session\.id|destroy|logout|revoke' -g '!node_modules' | head -30
cat > projects/m18-appsec/docs/session-lifecycle.md <<'EOF'
# Session lifecycle
1. Pre-login id: …
2. Post-login (¿rota?): …
3. Logout server-side: …
4. Request posterior con cookie vieja: esperado 401
EOF
```
### 2. Pruebas login/logout (50–60 min)

```bash
# Dos logins: ¿cambia el valor de Set-Cookie?
curl -sI -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' | rg -i set-cookie
# Logout + reuse (debe fallar)
curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout
curl -b /tmp/m18-cj -s -o /dev/null -w "%{http_code}\n" localhost:3000/api/pedidos
```

Si JWT stateless: documenta deny-list o TTL corto en el mismo archivo.
### 3. Commit (10–15 min)

```bash
git add projects/m18-appsec/docs/session-lifecycle.md
git commit -m "fix(m18): l11 session lifecycle"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Session fixation + logout best practices | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Doc ciclo de vida (artefacto: `projects/m18-appsec/docs/session-lifecycle.md`).
2. Pruebas login/logout documentadas (artefacto: `projects/m18-appsec/docs/session-lifecycle.md`).
3. Commit `docs(m18): L11 fijacion-de-sesion-y-logout-completo`.

## Errores comunes

- Logout solo borra cookie cliente.
- Session id pre-login reutilizado.

## Siguiente

[L12 — Checklist cookies y CSRF en staging](L12-checklist-cookies-y-csrf-en-staging.md)
