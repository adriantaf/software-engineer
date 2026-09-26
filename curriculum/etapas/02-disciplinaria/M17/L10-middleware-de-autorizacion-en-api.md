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

403 debe ser imposible de saltar desde el front.

## Objetivo

Middleware `authorize(roles)` (o políticas) en handlers sensibles + tests 403/IDOR.

## Pasos (hazlos en orden)

### 1. Implementa middleware (80–100 min)

Inyecta usuario de sesión; rechaza rol insuficiente; opcional: scope por `negocio_id`.

### 2. Aplica a rutas (40 min)

Admin staff, borrar servicio, etc. según matriz.

### 3. Tests (40–50 min)

Staff en acción owner → 403. Usuario A no lee cita de B si aplica.

### 4. Commit

`feat(m17): l10 middleware autorizacion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Middleware pattern | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Middleware activo (artefacto: `authorize(role) middleware`).
2. 403 tests (artefacto: `authorize(role) middleware`).
3. Sin lógica duplicada (artefacto: `authorize(role) middleware`).
4. Commit `docs(m17): L10 middleware-de-autorizacion-en-api`.

## Errores comunes

- Check solo en UI.
- Hardcode user id.

## Siguiente

[L11 — Panel admin mínimo — gestión staff](L11-panel-admin-minimo-gestion-staff.md)
