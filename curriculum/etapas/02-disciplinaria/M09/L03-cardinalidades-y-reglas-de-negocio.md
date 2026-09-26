---
id: L03
materia: M09
orden: 3
titulo: Cardinalidades y reglas de negocio
horas: 5.0
semana: 1
lectura: "*Fundamentos de BD* — Elmasri & Navathe (ed. ES): Modelo ER / relacional — Elmasri relaciones"
evidencia: "ER revisado con FKs planeadas"
---

# L03 — Cardinalidades y reglas de negocio

**~5.0 h · Semana 1**

Modelas y operas el esquema del producto con PostgreSQL real, parametrización y permisos mínimos.

## Objetivo

Entregar `ER revisado con FKs planeadas` con SQL ejecutado (no solo leído).

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
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Semana 1: Modelo ER / relacional — Elmasri relaciones | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
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

[L04 — Glosario alineado al dominio](L04-glosario-alineado-al-dominio.md)
