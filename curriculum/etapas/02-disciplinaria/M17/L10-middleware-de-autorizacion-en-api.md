---
id: L10
materia: M17
orden: 10
titulo: Middleware de autorización en API
horas: 5.0
semana: 3
lectura: Middleware pattern
evidencia: authorize(role) middleware
---

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
git add projects/m17-agenda-ops
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
