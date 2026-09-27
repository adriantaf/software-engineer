---
id: L12
materia: M09
orden: 12
titulo: Cinco consultas P2 comentadas
horas: 5.0
semana: 3
lectura: Repaso Elmasri SQL + tutorial PG
evidencia: sql/ con ≥5 archivos .sql comentados — avanza P2
---

# L12 — Cinco consultas P2 comentadas

**~5.0 h · Semana 3**

Cierras el paquete de consultas de la práctica **P2** (falta EXPLAIN en semana 4).

## Objetivo

Dejar ≥5 SQL comentados, ejecutables, orientados a Agenda Ops.

## Pasos

### 1. Inventario (20 min)

```bash
ls projects/m09-bases-datos/sql/*.sql
```

### 2. Completa el set (150 min)

Mínimo sugerido:

1. `joins-citas-cliente.sql` (L09)
2. `agg-citas-por-servicio.sql` (L10)
3. `subq-clientes-frecuentes.sql` (L11)
4. `reporte-no-shows.sql` — tasa o listado de no-show
5. `reporte-agenda-del-dia.sql` — citas de un día (`\set dia '''2026-09-26'''` o literal)

Cada archivo: encabezado con pregunta de negocio + comentario de salida.

### 3. Smoke test (40 min)

Corre los cinco seguidos; arregla los que fallen.

### 4. Commit (20 min)

```bash
git add projects/m09-bases-datos/sql
git commit -m "feat(m09): cinco consultas P2 comentadas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Repaso Elmasri SQL + tutorial PG | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Hay ≥5 archivos `.sql` en `sql/` (joins, agg, subq, +2 reportes o variantes).
2. Cada uno tiene comentario de propósito + salida ejemplo.
3. Commit de paquete P2 queries.

## Errores comunes

- Cinco archivos vacíos o idénticos.
- Queries que no corren.
- Sin relación con preguntas de negocio del salón.

## Siguiente

[L13 — Índices B-tree intro](L13-indices-b-tree-intro.md)
