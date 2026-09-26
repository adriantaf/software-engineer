---
id: L19
materia: M09
orden: 19
titulo: Least privilege (P3)
horas: 5.0
semana: 5
lectura: "hilos/seguridad.md"
evidencia: "roles.md + rol app"
---

# L19 — Least privilege (P3)

**~5.0 h · Semana 5**

Modelas y operas el esquema del producto con PostgreSQL real, parametrización y permisos mínimos.

## Objetivo

Entregar `roles.md + rol app` con SQL ejecutado (no solo leído).

## Pasos

### 1. Lectura (45 min)

Capítulo Elmasri indicado. Subraya definiciones (entidad, relación, dependencia funcional, ACID).

### 2. Trabajo en repo (150 min)

Ejecuta contra tu BD local. **Nunca** pegues contraseñas en git; usa `.env` ignorado y `README` con variables.

### 3. Query parametrizada (30 min)

Si aplica capa TS, muestra `$1` placeholders; si solo SQL, usa variables psql `\set`.

### 4. Evidencia en git (45 min)

Archivos `.sql` o migraciones + salida ejemplo en comentario o `samples/`.

### 5. Commit (30 min)

`feat(m09): ...` descriptivo.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Elmasri & Navathe | Sección de la semana |
| PostgreSQL docs | Tema equivalente (Query, EXPLAIN, Roles) |

## Hecho cuando

1. Artefacto pedido existe y fue ejecutado.
2. Sin secretos en git.
3. Commit.

## Errores comunes

- SQL concatenado estilo injection demo.
- Usuario superuser para la app.
- Migraciones solo en local sin historial.
## Siguiente

[L20 — Reportes, seeds y cierre M09](L20-reportes-seeds-y-cierre-m09.md)
