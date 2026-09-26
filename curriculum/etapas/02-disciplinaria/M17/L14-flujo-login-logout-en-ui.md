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

Primera impresión del piloto: labels claros, error de credencial, logout limpio.

## Objetivo

Form login accesible + logout que limpia sesión en cliente y servidor.

## Pasos (hazlos en orden)

### 1. Form (70–90 min)

Labels, autocomplete, mensaje 401 en español. No meter token en querystring.

### 2. Logout (30–40 min)

Botón visible; limpia cookie/estado; redirect login.

### 3. Checklist manual (20 min)

`docs/ui-login-checklist.md` con 5 pasos.

### 4. Commit

`feat(m17): l14 login logout ui`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Forms accesibles | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Login/logout (artefacto: `páginas login`).
2. Errores visibles (artefacto: `páginas login`).
3. Sin password en state (artefacto: `páginas login`).
4. Commit `docs(m17): L14 flujo-login-logout-en-ui`.

## Errores comunes

- Alert genérico.
- Token en querystring.

## Siguiente

[L15 — Listas con loading, error y vacío](L15-listas-con-loading-error-y-vacio.md)
