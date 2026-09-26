---
id: L16
materia: M09
orden: 16
titulo: Documentar planes de ejecución
horas: 5.0
semana: 4
lectura: Repaso EXPLAIN + tu explain-notas.md
evidencia: explain-notas.md completo — cierra P2
---

# L16 — Documentar planes de ejecución

**~5.0 h · Semana 4**

La evidencia de P2 es legible por otro humano (tú en tres meses).

## Objetivo

Cerrar `explain-notas.md` y la checklist P2 en el README.

## Pasos

### 1. Pulido del documento (90 min)

Relee `explain-notas.md`. Añade:

- Link relativo al `.sql`
- Pregunta de negocio en una línea
- Conclusión binaria: ¿mantenemos el índice? sí/no + cuándo revisarlo

### 2. Índice de sql/ (40 min)

Tabla corta en README: archivo → pregunta.

### 3. Autorevisión P2 (40 min)

Checklist ficha M09: joins/agregaciones + EXPLAIN comentado. Lista gaps si los hay (y ciérralos).

### 4. Commit (20 min)

```bash
git commit -am "docs(m09): cierra P2 explain y sql"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Repaso EXPLAIN + tu explain-notas.md | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `explain-notas.md` tiene pregunta, SQL, antes, cambio, después, conclusión.
2. README marca P2 (sql/ + explain) como listo.
3. Commit de cierre P2.

## Errores comunes

- Notas solo con screenshots ilegibles.
- No enlazar el archivo SQL del reporte.
- Cerrar P2 sin ≥5 queries de L12.

## Siguiente

[L17 — Transacciones ACID](L17-transacciones-acid.md)
