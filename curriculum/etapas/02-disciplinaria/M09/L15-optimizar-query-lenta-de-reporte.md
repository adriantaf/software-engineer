---
id: L15
materia: M09
orden: 15
titulo: Optimizar query lenta de reporte
horas: 5.0
semana: 4
lectura: Elmasri selectividad / PG Index-Only Scans intro
evidencia: Plan DESPUÉS + cambio (índice o reescritura)
---

# L15 — Optimizar query lenta de reporte

**~5.0 h · Semana 4**

Una pasada de EXPLAIN no basta: cambias algo y vuelves a medir.

## Objetivo

Completar “Plan (después)” y la conclusión en `explain-notas.md`.

## Pasos

### 1. Hipótesis (30 min)

Ejemplos: falta índice en `(tenant_id, inicia_en)`; `WHERE date(inicia_en) = …` impide uso de índice; SELECT * innecesario.

### 2. Cambia una sola cosa (60–90 min)

Índice **o** reescritura (mejor `inicia_en >= @start AND inicia_en < @end` que casteos).

### 3. Remide (45 min)

Mismo `EXPLAIN (ANALYZE, BUFFERS)`. Pega en la sección después.

### 4. Criterio de éxito (30 min)

Si con seeds pequeños no hay diferencia, dilo honestamente y explica qué pasaríacon 100k citas (orden de magnitud).

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri selectividad / PG Index-Only Scans intro | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Aplicas un cambio (índice, filtro, reescritura).
2. Vuelves a correr EXPLAIN ANALYZE.
3. Documentas comparación antes/después.

## Errores comunes

- Declarar victoria sin segunda medición.
- Índice que no se usa (tipo de dato / función sobre columna).
- Optimizar una query que nadie corre.

## Siguiente

[L16 — Documentar planes de ejecución](L16-documentar-planes-de-ejecucion.md)
