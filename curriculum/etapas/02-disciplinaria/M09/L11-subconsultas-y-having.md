---
id: L11
materia: M09
orden: 11
titulo: Subconsultas y HAVING
horas: 5.0
semana: 3
lectura: "Elmasri: subconsultas; HAVING"
evidencia: sql/subq-clientes-frecuentes.sql
---

# L11 — Subconsultas y HAVING

**~5.0 h · Semana 3**

“Clientes con más de 2 citas completadas” pide filtrar **grupos**, no filas.

## Objetivo

Crear `sql/subq-clientes-frecuentes.sql` con `HAVING` y al menos una subconsulta.

## Pasos

### 1. Lectura (40 min)

Subconsultas escalares, `IN`/`EXISTS`, y `HAVING`.

### 2. HAVING (60 min)

```sql
SELECT cl.nombre, count(*) AS completadas
FROM citas c
JOIN clientes cl ON cl.id = c.cliente_id
WHERE c.estado = 'completada'
GROUP BY cl.id, cl.nombre
HAVING count(*) >= 2
ORDER BY completadas DESC;
```

### 3. Subconsulta (60 min)

Lista servicios que **nunca** se han agendado (`NOT EXISTS` o `LEFT JOIN … IS NULL`). Prefiere `EXISTS` y explica por qué en un comentario.

### 4. Compara mentalmente con JOIN (30 min)

Reescribe una de las dos con puro JOIN. ¿Más legible? Anota preferencia.

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: subconsultas; HAVING | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Una query con `HAVING` y otra con subconsulta (`IN` / `EXISTS` / escalar).
2. Ambas ejecutadas con comentario de salida.
3. Commit.

## Errores comunes

- Usar `WHERE count(*) > 1` en lugar de `HAVING`.
- Subconsulta correlacionada innecesariamente lenta sin mirar el plan (eso es L14; hoy solo correctness).
- Clientes frecuentes incluyendo solo canceladas.

## Siguiente

[L12 — Cinco consultas P2 comentadas](L12-cinco-consultas-p2-comentadas.md)
