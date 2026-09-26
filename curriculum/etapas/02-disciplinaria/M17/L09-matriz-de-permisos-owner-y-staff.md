---
id: L09
materia: M17
orden: 9
titulo: Matriz de permisos owner y staff
horas: 5.0
semana: 3
lectura: m13 casos de uso admin
evidencia: projects/m17-agenda-ops/docs/permisos.md
---

# L09 — Matriz de permisos owner y staff

**~5.0 h · Semana 3**

Roles sin matriz escrita se implementan a ojo.

## Objetivo

`docs/permisos.md`: acción × rol (cancelar, reportes, gestionar staff, CRUD).

## Pasos (hazlos en orden)

### 1. Inventario de rutas (40 min)

Lista endpoints sensibles actuales.

### 2. Matriz (70–90 min)

Tabla Markdown: Owner / Staff / Anónimo → Allow/Deny. Enlaza a stories M12.

### 3. Gaps (30 min)

Marca lo aún no enforced en API (L10 lo cierra).

### 4. Commit

`docs(m17): l09 matriz permisos owner staff`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m13 casos de uso admin | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. permisos.md (artefacto: `projects/m17-agenda-ops/docs/permisos.md`).
2. Cobertura endpoints (artefacto: `projects/m17-agenda-ops/docs/permisos.md`).
3. Commit (artefacto: `projects/m17-agenda-ops/docs/permisos.md`).

## Errores comunes

- Staff = owner.
- Matriz vacía.

## Siguiente

[L10 — Middleware de autorización en API](L10-middleware-de-autorizacion-en-api.md)
