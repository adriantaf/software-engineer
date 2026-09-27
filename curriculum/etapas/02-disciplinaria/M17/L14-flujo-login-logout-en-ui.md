---
id: L14
materia: M17
orden: 14
titulo: Flujo login/logout en UI
horas: 5.0
semana: 4
lectura: Forms accesibles
evidencia: páginas login
---

# L14 — Flujo login/logout en UI

**~5.0 h · Semana 4**

Primera impresión del piloto.

## Objetivo

Form login con labels, errores de credencial, logout que limpia sesión.

## Conceptos clave

- login UI
- error auth
- logout

## Pasos (hazlos en orden)

### 1. Página login (60–80 min)

Form email/password → `POST /auth/login` (credentials include). Maneja error 401 visible.

### 2. Logout limpia sesión (40–50 min)

```bash
# DevTools → Application → Cookies: tras logout la cookie de sesión desaparece
```

Botón logout → `POST /auth/logout` + redirect `/login`.

### 3. Commit (15 min)

```bash
git add projects/m17-agenda-ops/apps
git commit -m "feat(m17): L14 login logout UI"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Forms accesibles | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. UI login/logout funcional; cookie de sesión desaparece tras logout.
2. Commit `docs(m17): L14 flujo-login-logout-en-ui`.

## Errores comunes

- Logout solo limpia estado React y deja cookie.
- Form sin mensaje de 401.

## Siguiente

[L15 — Listas con loading, error y vacío](L15-listas-con-loading-error-y-vacio.md)
