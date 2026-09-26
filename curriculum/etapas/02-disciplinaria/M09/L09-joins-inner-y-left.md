---
id: L09
materia: M09
orden: 9
titulo: Joins inner y left
horas: 5.0
semana: 3
lectura: "*Fundamentos de BD* — Elmasri & Navathe (ed. ES): Índices y EXPLAIN — Elmasri SQL"
evidencia: "sql/joins-*.sql ejecutados"
---

# L09 — Joins inner y left

**~5.0 h · Semana 3**

Modelas y operas el esquema del producto con PostgreSQL real, parametrización y permisos mínimos.

## Objetivo

Entregar `sql/joins-*.sql ejecutados` con SQL ejecutado (no solo leído).

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

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Semana 3: Índices y EXPLAIN — Elmasri SQL | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

1. Artefacto pedido existe y fue ejecutado.
2. Sin secretos en git.
3. Commit.

## Errores comunes

- SQL concatenado estilo injection demo.
- Usuario superuser para la app.
- Migraciones solo en local sin historial.
## Siguiente

[L10 — Agregaciones y GROUP BY](L10-agregaciones-y-group-by.md)
