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

Roles sin matriz escrita se implementan inconsistente.

## Objetivo

Documentar tabla acción×rol (cancelar cita, ver reportes, gestionar staff).

## Conceptos clave

- RBAC
- owner
- staff

## Pasos (hazlos en orden)

### 1. Redacta matriz owner/staff (60–80 min)

```bash
mkdir -p projects/m17-agenda-ops/docs
```

Crea `projects/m17-agenda-ops/docs/permisos.md`:

```md
| Acción | owner | staff |
|--------|-------|-------|
| CRUD citas propias negocio | sí | sí |
| Borrar servicio | sí | no |
| Invitar staff | sí | no |
| Ver panel /admin | sí | no |
```

### 2. Cruza con rutas API (40 min)

```bash
rg -n "router\\.(get|post|patch|delete)|app\\.(get|post)" projects/m17-agenda-ops/src | head -40
```

Marca en la matriz qué ruta aplica cada fila.

### 3. Commit (15 min)

```bash
git add projects/m17-agenda-ops/docs/permisos.md
git commit -m "docs(m17): L09 matriz permisos owner staff"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m13 casos de uso admin | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-agenda-ops/docs/permisos.md` con matriz owner/staff y rutas.
2. Commit `docs(m17): L09 matriz-de-permisos-owner-y-staff`.

## Errores comunes

- Matriz genérica sin rutas del piloto.
- Permisos solo ‘en la cabeza’.

## Siguiente

[L10 — Middleware de autorización en API](L10-middleware-de-autorizacion-en-api.md)
