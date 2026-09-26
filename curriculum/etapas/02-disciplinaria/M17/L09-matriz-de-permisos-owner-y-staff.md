---
id: L09
materia: M17
orden: 9
titulo: Matriz de permisos owner y staff
horas: 5
semana: 3
lectura: "m13 casos de uso admin"
evidencia: "projects/m17-agenda-ops/docs/permisos.md"
---

# L09 — Matriz de permisos owner y staff

**~5 h · Semana 3**

## Objetivo

Documentar tabla acción×rol (cancelar cita, ver reportes, gestionar staff).

## Por qué importa

Roles sin matriz escrita se implementan inconsistente.

## Conceptos

- RBAC.
- owner.
- staff.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

permisos.md enlazado a endpoints. Cada ruta sensible tiene rol en comentario OpenAPI o tabla.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l09 matriz-de-permisos-owner-y-staff"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m12 | stories roles | OWASP access control |

## Hecho cuando

1. permisos.md.
2. Cobertura endpoints.
3. Commit.

## Errores comunes

- Staff = owner.
- Matriz vacía.

## Siguiente

[L10 — Middleware de autorización en API](L10-middleware-de-autorizacion-en-api.md)
