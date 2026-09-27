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

Agenda Ops se usa desde navegador diario.

## Objetivo

Crear front con login, layout panel, rutas protegidas redirect a login.

## Conceptos clave

- SPA
- protected route
- layout

## Pasos (hazlos en orden)

### 1. Scaffold front (60–80 min)

```bash
mkdir -p projects/m17-agenda-ops/apps/web
# Vite/Next según stack.md — TypeScript
cd projects/m17-agenda-ops/apps/web && npm create vite@latest . -- --template react-ts
```

Documenta el comando real en `stack.md`.

### 2. Rutas protegidas (60–80 min)

```ts
// ProtectedRoute: si !session → redirect /login
```

```bash
# sin cookie, /citas en browser → login
```

### 3. Commit (15 min)

```bash
git add projects/m17-agenda-ops/apps projects/m17-agenda-ops/stack.md
git commit -m "feat(m17): L13 scaffold front rutas protegidas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | React Router / framework docs | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Front scaffold en `apps/web` (o ruta en stack.md) con rutas protegidas.
2. Commit `docs(m17): L13 scaffold-front-y-rutas-protegidas`.

## Errores comunes

- Rutas ‘protegidas’ solo ocultando links.
- Front sin TypeScript / fuera de stack.md.

## Siguiente

[L14 — Flujo login/logout en UI](L14-flujo-login-logout-en-ui.md)
