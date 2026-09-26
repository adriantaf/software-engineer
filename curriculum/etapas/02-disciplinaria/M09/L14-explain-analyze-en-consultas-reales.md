---
id: L14
materia: M09
orden: 14
titulo: EXPLAIN ANALYZE en consultas reales
horas: 5.0
semana: 4
lectura: "PG: EXPLAIN / Using EXPLAIN"
evidencia: explain-notas.md con plan ANTES pegado
---

# L14 — EXPLAIN ANALYZE en consultas reales

**~5.0 h · Semana 4**

El plan de ejecución es la radiografía. Hoy lees una de **tu** query.

## Objetivo

Llenar la sección “Plan (antes…)” de `explain-notas.md`.

## Pasos

### 1. Lectura (45 min)

[Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — enfócate en nodos Seq Scan, Index Scan, cost, rows, actual time.

### 2. Elige query (20 min)

Copia tu reporte diario o agg a `sql/explain-reporte-diario.sql`.

### 3. Corre EXPLAIN (60 min)

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT …;
```

Pega salida completa en `explain-notas.md`.

### 4. Traducción al español (60 min)

Escribe 5–8 líneas: qué nodo domina, estimaciones vs reality (`rows` vs `actual rows`), buffers.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): explain analyze reporte diario"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | PG: EXPLAIN / Using EXPLAIN | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Corres `EXPLAIN (ANALYZE, BUFFERS)` sobre una query de reporte.
2. Pegas el plan en `explain-notas.md` (sección antes).
3. Explicas en llano Seq Scan vs Index Scan.

## Errores comunes

- Solo `EXPLAIN` sin `ANALYZE` y hablar de tiempos reales.
- Pegar el plan sin interpretar una sola línea.
- Medir con tabla vacía.

## Siguiente

[L15 — Optimizar query lenta de reporte](L15-optimizar-query-lenta-de-reporte.md)
