---
id: L13
materia: M17
orden: 13
titulo: Scaffold front y rutas protegidas
horas: 5.0
semana: 4
lectura: React Router / framework docs
evidencia: front app + router
---

# L13 — Scaffold front y rutas protegidas

**~5.0 h · Semana 4**

Agenda Ops se usa desde el navegador a diario.

## Objetivo

Front (`apps/web` o `client/`) con login, layout y redirect si no hay sesión.

## Pasos (hazlos en orden)

### 1. Scaffold UI (60–80 min)

Router + página login + shell panel. `VITE_API_URL` / equivalente en `.env.example`.

### 2. Protected routes (50–60 min)

Sin sesión → `/login`. Con sesión → agenda.

### 3. CORS documentado (20 min)

Origen front permitido en API; nada de `*` en prod.

### 4. Commit

`feat(m17): l13 scaffold front rutas protegidas`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | React Router / framework docs | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Front arranca (artefacto: `front app`).
2. Redirect sin sesión (artefacto: `front app`).
3. Commit (artefacto: `front app`).

## Errores comunes

- CORS `*` sin doc.
- API_URL hardcode prod.

## Siguiente

[L14 — Flujo login/logout en UI](L14-flujo-login-logout-en-ui.md)
