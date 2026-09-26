---
id: L06
materia: M09
orden: 6
titulo: Segunda forma normal
horas: 5.0
semana: 2
lectura: "*Fundamentos de BD* — Elmasri & Navathe (ed. ES): SQL consultas (SELECT/JOIN) — Elmasri 2FN"
evidencia: "tablas split + justificación"
---

# L06 — Segunda forma normal

**~5.0 h · Semana 2**

Modelas y operas el esquema del producto con PostgreSQL real, parametrización y permisos mínimos.

## Objetivo

Entregar `tablas split + justificación` con SQL ejecutado (no solo leído).

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
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Semana 2: SQL consultas (SELECT/JOIN) — Elmasri 2FN | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
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

[L07 — Tercera forma normal (P1)](L07-tercera-forma-normal-p1.md)
