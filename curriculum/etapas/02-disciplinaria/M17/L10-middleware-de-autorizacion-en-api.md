---
id: L10
materia: M17
orden: 10
titulo: Middleware de autorización en API
horas: 5
semana: 3
lectura: Middleware pattern
evidencia: authorize(role) middleware
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Middleware que verifica rol y negocio en cada handler
      sensible.


      - middleware

      - 403

      - contexto usuario
  - id: s2
    tipo: ejemplo
    titulo: 1. Middleware authorize
    xp: 10
    cuerpo: |-
      ```ts
      // src/middleware/authorize.ts
      export function authorize(...roles: Array<"owner"|"staff">) {
        return (req, res, next) => {
          const u = req.user; // inyectado por auth
          if (!u || !roles.includes(u.rol)) return res.status(403).json({ error: "forbidden" });
          next();
        };
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Middleware de autorización en API" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: authorize(role) middleware
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
    pregunta: ¿Es buena práctica en esta lección? “Check de rol solo en el front."
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
        texto: Middleware que verifica rol y negocio en cada handler sensible.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Aplica a rutas sensibles
    xp: 10
    cuerpo: |-
      Ej.: `DELETE /servicios/:id` y `/admin/*` → `authorize("owner")`.

      ```bash
      staff cookie → 403 en acción owner
      curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" \
        -X DELETE http://localhost:3000/servicios/<id>
      403
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Tests IDOR/403 + commit
    xp: 10
    cuerpo: |-
      ```bash
      npm test -- authz
      git add projects/m17-vitrina
      git commit -m "feat(m17): L10 middleware autorizacion"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Middleware `authorize(roles)` aplicado a rutas sensibles.
      - Tests 403 (staff en acción owner) e IDOR básico si aplica.
      - 'Commit `docs(m17): L10 middleware-de-autorizacion-en-api`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — Middleware de autorización en API

**~5.0 h · Semana 3**

403 debe ser imposible de evitar desde el front.

## Objetivo

Middleware que verifica rol y negocio en cada handler sensible.

## Conceptos clave

- middleware
- 403
- contexto usuario

## Pasos (hazlos en orden)

### 1. Middleware authorize (80–100 min)

```ts
// src/middleware/authorize.ts
export function authorize(...roles: Array<"owner"|"staff">) {
  return (req, res, next) => {
    const u = req.user; // inyectado por auth
    if (!u || !roles.includes(u.rol)) return res.status(403).json({ error: "forbidden" });
    next();
  };
}
```

### 2. Aplica a rutas sensibles (40 min)

Ej.: `DELETE /servicios/:id` y `/admin/*` → `authorize("owner")`.

```bash
# staff cookie → 403 en acción owner
curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" \
  -X DELETE http://localhost:3000/servicios/<id>
# 403
```

### 3. Tests IDOR/403 + commit (40–50 min)

```bash
npm test -- authz
git add projects/m17-vitrina
git commit -m "feat(m17): L10 middleware autorizacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Middleware pattern | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Middleware `authorize(roles)` aplicado a rutas sensibles.
2. Tests 403 (staff en acción owner) e IDOR básico si aplica.
3. Commit `docs(m17): L10 middleware-de-autorizacion-en-api`.

## Errores comunes

- Check de rol solo en el front.
- Hardcodear `userId` en el middleware.

## Siguiente

[L11 — Panel admin mínimo — gestión staff](L11-panel-admin-minimo-gestion-staff.md)
