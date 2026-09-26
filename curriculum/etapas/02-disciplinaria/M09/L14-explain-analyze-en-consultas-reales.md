---
id: L14
materia: M09
orden: 14
titulo: EXPLAIN ANALYZE en consultas reales
horas: 5.0
semana: 4
lectura: "PG EXPLAIN"
evidencia: "explain-notas.md primera entrada"
---

# L14 — EXPLAIN ANALYZE en consultas reales

**~5.0 h · Semana 4**

Modelas y operas el esquema del producto con PostgreSQL real, parametrización y permisos mínimos.

## Objetivo

Entregar `explain-notas.md primera entrada` con SQL ejecutado (no solo leído).

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

[L15 — Optimizar query lenta de reporte](L15-optimizar-query-lenta-de-reporte.md)
