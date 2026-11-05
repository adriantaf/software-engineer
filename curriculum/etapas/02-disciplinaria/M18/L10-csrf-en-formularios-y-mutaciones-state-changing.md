---
id: L10
materia: M18
orden: 10
titulo: CSRF en formularios y mutaciones state-changing
horas: 5
semana: 3
lectura: CSRF Prevention Cheat Sheet
evidencia: fix + projects/m18-appsec/pocs/csrf-notes.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Lista rutas mutables + protección en
      `projects/m18-appsec/pocs/csrf-notes.md`; ≥1 ruta crítica con
      token/SameSite; curl sin token → 403.


      Un atacante no necesita XSS si tu sesión acepta POST cross-site.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario mutaciones
    xp: 10
    cuerpo: |-
      ```ts
      // middleware mínimo (ilustrativo)
      export function requireCsrf(req, res, next) {
        const token = req.headers["x-csrf-token"] || req.body?._csrf;
        if (!token || token !== req.session?.csrfToken) {
          return res.status(403).json({ error: "csrf" });
        }
        next();
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "CSRF en formularios y mutaciones state-changing" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: fix + projects/m18-appsec/pocs/csrf-notes.md
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
          Lista rutas mutables + protección en
          `projects/m18-appsec/pocs/csrf-notes.md`; ≥1 ruta crítica con
          token/SameSite; curl sin token → 403.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Protege la ruta crítica
    xp: 10
    cuerpo: >-
      Token sincronizado, double-submit o SameSite estricto + método seguro.
      Ejemplo chequeo:


      ```ts

      // middleware mínimo (ilustrativo)

      export function requireCsrf(req, res, next) {
        const token = req.headers["x-csrf-token"] || req.body?._csrf;
        if (!token || token !== req.session?.csrfToken) {
          return res.status(403).json({ error: "csrf" });
        }
        next();
      }

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. curl sin token
    xp: 10
    cuerpo: >-
      ```bash

      # Con cookie de sesión válida pero sin CSRF → 403

      curl -s -o /dev/null -w "%{http_code}\n" -X POST
      localhost:3000/api/pedidos \
        -H 'content-type: application/json' -b /tmp/m18-cj \
        -d '{"clienteId":"…","inicio":"2026-01-01T10:00:00Z"}'
      # esperado: 403

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Lista rutas mutables (artefacto: `fix`).'
      - '≥1 ruta protegida (artefacto: `fix`).'
      - 'Commit `docs(m18): L10 csrf-en-formularios-y-mutaciones-state-changing`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — CSRF en formularios y mutaciones state-changing

**~5.0 h · Semana 3**

Un atacante no necesita XSS si tu sesión acepta POST cross-site.

## Objetivo

Lista rutas mutables + protección en `projects/m18-appsec/pocs/csrf-notes.md`; ≥1 ruta crítica con token/SameSite; curl sin token → 403.

## Pasos

### 1. Inventario mutaciones (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "\.(post|put|patch|delete)\(" -g '*.ts' -g '!node_modules' | head -40
cat > projects/m18-appsec/pocs/csrf-notes.md <<'EOF'
# CSRF notes
| Ruta | Método | Protección | Estado |
|------|--------|------------|--------|
| /api/pedidos | POST | | |
| /api/pedidos/:id | PUT/DELETE | | |
| /auth/logout | POST | | |
EOF
```
### 2. Protege la ruta crítica (70–90 min)

Token sincronizado, double-submit o SameSite estricto + método seguro. Ejemplo chequeo:

```ts
// middleware mínimo (ilustrativo)
export function requireCsrf(req, res, next) {
  const token = req.headers["x-csrf-token"] || req.body?._csrf;
  if (!token || token !== req.session?.csrfToken) {
    return res.status(403).json({ error: "csrf" });
  }
  next();
}
```
### 3. curl sin token (20–30 min)

```bash
# Con cookie de sesión válida pero sin CSRF → 403
curl -s -o /dev/null -w "%{http_code}\n" -X POST localhost:3000/api/pedidos \
  -H 'content-type: application/json' -b /tmp/m18-cj \
  -d '{"clienteId":"…","inicio":"2026-01-01T10:00:00Z"}'
# esperado: 403
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/pocs/csrf-notes.md
git commit -m "fix(m18): l10 csrf mutaciones"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | CSRF Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Lista rutas mutables (artefacto: `fix`).
2. ≥1 ruta protegida (artefacto: `fix`).
3. Commit `docs(m18): L10 csrf-en-formularios-y-mutaciones-state-changing`.

## Errores comunes

- Confiar solo en CORS.
- GET que borra datos.

## Siguiente

[L11 — Fijación de sesión y logout completo](L11-fijacion-de-sesion-y-logout-completo.md)
