---
id: L10
materia: M09
orden: 10
titulo: Agregaciones y GROUP BY
horas: 5.0
semana: 3
lectura: "Elmasri: agregación GROUP BY; PG aggregate functions"
evidencia: sql/agg-citas-por-servicio.sql
---

# L10 — Agregaciones y GROUP BY

**~5.0 h · Semana 3**

El dueño pregunta: “¿qué servicio se agenda más?”. Eso es `GROUP BY`.

## Objetivo

Entregar `sql/agg-citas-por-servicio.sql` con al menos dos agregaciones ejecutadas.

## Pasos

### 1. Lectura (40 min)

Funciones de agregación y `GROUP BY` / `WHERE` vs filtros de grupo.

### 2. Escribe y corre (90 min)

```sql
-- sql/agg-citas-por-servicio.sql
SELECT s.nombre,
       count(*) AS total_citas,
       count(*) FILTER (WHERE c.estado = 'completada') AS completadas,
       coalesce(sum(s.precio_centavos) FILTER (WHERE c.estado = 'completada'), 0) AS ingresos_centavos
FROM citas c
JOIN servicios s ON s.id = c.servicio_id
GROUP BY s.id, s.nombre
ORDER BY total_citas DESC;
```

(Ajusta si usas snapshot de precio en la cita.)

### 3. Segunda query (45 min)

Citas por día (`date_trunc('day', inicia_en)`) de los últimos 14 días.

### 4. Frase de negocio (20 min)

En comentario del SQL: “El servicio más agendado esta semana es X con N citas”.

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: agregación GROUP BY; PG aggregate functions | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe y corre un SQL con `GROUP BY` + `COUNT`/`SUM`.
2. Interpretas el resultado en una frase de negocio.
3. Commit.

## Errores comunes

- Seleccionar columnas no agregadas fuera del `GROUP BY`.
- Sumar `precio` en float.
- Reportar conteos sin filtrar `cancelada` cuando la pregunta es “atendidas”.

## Siguiente

[L11 — Subconsultas y HAVING](L11-subconsultas-y-having.md)
