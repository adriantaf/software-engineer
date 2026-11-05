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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un atacante no necesita XSS si tu sesión acepta POST cross-site.


      **Objetivo de esta lección:** Lista rutas mutables + protección en
      `projects/m18-appsec/pocs/csrf-notes.md`; ≥1 ruta crítica con
      token/SameSite; curl sin token → 403.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario mutaciones
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n "\.(post|put|patch|delete)\(" -g '*.ts' -g '!node_modules' | head
      -40

      cat > projects/m18-appsec/pocs/csrf-notes.md <<'EOF'

      # CSRF notes

      | Ruta | Método | Protección | Estado |

      |------|--------|------------|--------|

      | /api/pedidos | POST | | |

      | /api/pedidos/:id | PUT/DELETE | | |

      | /auth/logout | POST | | |

      EOF

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Protege la ruta crítica
    xp: 10
    cuerpo: >-
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


      Token sincronizado, double-submit o SameSite estricto + método seguro.
      Ejemplo chequeo:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «CSRF en formularios y mutaciones state-changing», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de CSRF en formularios y
          mutaciones state-…
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

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
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
          Lista rutas mutables + protección en
          `projects/m18-appsec/pocs/csrf-notes.md`; ≥1 ruta crítica con
          token/SameSite; curl sin token → 403.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: curl sin token
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
