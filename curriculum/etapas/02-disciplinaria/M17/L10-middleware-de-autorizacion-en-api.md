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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - middleware

      - 403

      - contexto usuario


      **Objetivo de esta lección:** Middleware que verifica rol y negocio en
      cada handler sensible.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Middleware authorize
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Aplica a rutas sensibles
    xp: 10
    cuerpo: |-
      ```bash
      # staff cookie → 403 en acción owner
      curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" \
        -X DELETE http://localhost:3000/servicios/<id>
      # 403
      ```

      Ej.: `DELETE /servicios/:id` y `/admin/*` → `authorize("owner")`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Middleware de autorización en API», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Middleware de
          autorización en API
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
    pregunta: ¿Es recomendable en esta lección? “Check de rol solo en el front."
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
        texto: Middleware que verifica rol y negocio en cada handler sensible.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests IDOR/403 + commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
