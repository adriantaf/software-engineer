---
id: L14
materia: M10
orden: 14
titulo: Sesiones, tokens y estado en APIs
horas: 5.0
semana: 4
lectura: MDN Web Storage vs cookies + OAuth2 vista alta
evidencia: labs/sesiones.md
---

# L14 — Sesiones, tokens y estado en APIs

**~5.0 h · Semana 4**

El panel (origen A) hablará con la API (origen B). Hoy eliges cómo viaja la identidad.

## Objetivo

Dejar una decisión documentada sesión vs token para el piloto single-tenant.

## Pasos

### 1. Modelos (50 min)

En `labs/sesiones.md`: (1) session id opaco en cookie HttpOnly; (2) access token Bearer; (3) híbrido access corto + refresh.

### 2. Amenazas (40 min)

XSS → robo de token en JS vs cookie HttpOnly; CSRF → SameSite + anti-CSRF; replay → TTL corto.

### 3. Decisión piloto (50 min)

Elige **un** modelo para M17 y escribe “por qué”. Anota qué cambia cuando llegue multi-tenant (M19+).

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/sesiones.md
git commit -m "docs(m10): l14 sesiones tokens"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Sesión server-side vs JWT/opaque token; dónde vive el estado | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/sesiones.md` compara sesión+cookie vs Bearer token para Vitrina (pros/contras).
2. Diagrama: browser → API → store de sesión/Redis/PG.
3. Commit `docs(m10): l14 sesiones tokens`.

## Errores comunes

- JWT eterno en localStorage sin rotación ni revoke.
- Mezclar “stateless” con “sin authz”.
- Olvidar logout / invalidación.

## Siguiente

[L15 — CORS, preflight y errores típicos](L15-cors-preflight-y-errores-tipicos.md)
