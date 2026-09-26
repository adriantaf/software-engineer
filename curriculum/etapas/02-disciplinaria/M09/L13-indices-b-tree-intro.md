---
id: L13
materia: M09
orden: 13
titulo: Índices B-tree intro
horas: 5.0
semana: 4
lectura: "Elmasri: índices; PG docs Indexes / CREATE INDEX"
evidencia: Índice nuevo documentado + \d citas
---

# L13 — Índices B-tree intro

**~5.0 h · Semana 4**

Un índice no es un logro: es una apuesta sobre lecturas vs escrituras.

## Objetivo

Entender B-tree en la práctica y dejar un índice justificado por una query tuya.

## Pasos

### 1. Lectura (50 min)

Elmasri (índices) + [PG CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html) (solo B-tree por ahora).

### 2. Inventario actual (30 min)

```sql
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'citas';
```

Compara con lo que ya creó `001_init.sql`.

### 3. Elige una query lenta potencial (60 min)

Ej. filtrar por `estado` + rango de `inicia_en`. Diseña:

```sql
CREATE INDEX IF NOT EXISTS idx_citas_estado_inicia
  ON citas (estado, inicia_en);
```

Ponlo en `migrations/002_auditoria_y_indices.sql` (o archivo nuevo) si aún no está.

### 4. Aplica y verifica (40 min)

```bash
psql "..." -f migrations/002_auditoria_y_indices.sql
psql "..." -c '\d citas'
```

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: índices; PG docs Indexes / CREATE INDEX | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Creas (o justificas) al menos un índice adicional alineado a un reporte.
2. Documentas en `explain-notas.md` o migración por qué existe.
3. Commit.

## Errores comunes

- Indexar todas las columnas.
- Índice único accidental que rompe inserts legítimos.
- No saber qué es B-tree vs “magia del motor”.

## Siguiente

[L14 — EXPLAIN ANALYZE en consultas reales](L14-explain-analyze-en-consultas-reales.md)
