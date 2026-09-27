---
id: L09
materia: M09
orden: 9
titulo: Joins inner y left
horas: 5.0
semana: 3
lectura: Elmasri SQL joins + PG tutorial Queries
evidencia: sql/joins-citas-cliente.sql ejecutado
---

# L09 — Joins inner y left

**~5.0 h · Semana 3**

Los reportes del salón son JOINs. Hoy ejecutas los dos patrones básicos contra tu BD.

## Objetivo

Completar y correr `sql/joins-citas-cliente.sql` con datos reales (aunque sean seeds mínimos).

## Pasos

### 1. Seeds mínimos (30–45 min)

Si no hay filas:

```bash
psql "..." -f seeds/001_demo.sql
psql "..." -c 'SELECT count(*) FROM citas;'
```

### 2. Lectura SQL (40 min)

Elmasri: joins. Alternativa: [PG tutorial — Queries](https://www.postgresql.org/docs/current/tutorial-select.html).

### 3. Ejecuta el scaffold (60 min)

Abre `sql/joins-citas-cliente.sql`. Corre cada query. Ajusta columnas si tu esquema diverge.

### 4. Añade un tercer join útil (45 min)

Ejemplo: citas `completada` de la última semana con teléfono del cliente (para recordatorio manual). Guárdalo en el mismo archivo o en `sql/joins-completadas-recientes.sql`.

### 5. Evidencia + commit (30 min)

Comenta al final del SQL 3–5 líneas de resultado. Commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri SQL joins + PG tutorial Queries | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Ejecutaste INNER y LEFT JOIN del archivo (o el tuyo equivalente).
2. Hay comentario con salida de ejemplo en el `.sql` o en `samples/`.
3. Commit `feat(m09): joins citas cliente`.

## Errores comunes

- Usar solo comma-join (`FROM a, b WHERE`) sin entender la diferencia.
- LEFT JOIN y filtrar la tabla derecha en `WHERE` convirtiendo el left en inner sin querer.
- No tener seeds: joins sobre tablas vacías no enseñan nada.

## Siguiente

[L10 — Agregaciones y GROUP BY](L10-agregaciones-y-group-by.md)
