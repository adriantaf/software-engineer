---
id: M09
titulo: Bases de datos
etapa: disciplinaria
orden: 9
semanas: 5
horas: 100
practicas:
  - id: p1
    titulo: Modelo ER + normalización hasta 3FN
  - id: p2
    titulo: "SQL: joins, agregaciones, índices"
  - id: p3
    titulo: Migraciones, transacciones y least privilege
proyecto:
  id: proj
  titulo: Esquema del CRM/POS con seeds y reportes
---

# M09 — Bases de datos

## Por qué existe

Los datos son el corazón del producto. Un esquema mal modelado te persigue en cada feature; un solo usuario `postgres` para la app y concatenar SQL son incidentes de seguridad evitables. Esta materia diseña el **esquema de Agenda Ops / CRM** con SQL real, índices, transacciones y migraciones versionadas.

Seguridad desde el día 1: **queries parametrizadas + least privilege** ([hilo](../../hilos/seguridad.md)).

**En resumen:** diseñas el esquema del producto: ER, SQL real, índices y migraciones sin SQL injection.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Modelar entidades del dominio (cliente, servicio, cita, usuario) en ER y normalizar hasta 3FN con justificación.
2. Escribir SQL de joins, agregaciones y subconsultas contra PostgreSQL.
3. Leer un plan de ejecución con `EXPLAIN` y decidir cuándo añadir un índice.
4. Aplicar transacciones ACID en operaciones multi-paso (p. ej. crear cita + auditoría).
5. Versionar el esquema con migraciones reproducibles y seeds de demo.
6. Crear un rol de aplicación con permisos mínimos (sin superuser).

## Cómo estudiar esta materia (piloto de lecciones)

M09 sigue el formato de lecciones cortas y completas (como M01/M06): marcas una a una cuando cumples “Hecho cuando”.

1. Abre las lecciones **en orden** (L01 → L20).
2. Cada lección trae objetivo, pasos, lectura y criterio “Hecho cuando”.
3. Marca la lección en la UI solo si cumple ese criterio.
4. **Diseña en papel o diagrama** antes de `CREATE TABLE`; cada FK debe tener una razón de negocio.
5. Ejecuta todo contra una BD local (Docker o nativa); no solo leas Elmasri.
6. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Modelo ER | 6–8 | Diagrama + normalización (L01–L08) |
| SQL + EXPLAIN | 6–8 | Queries del dominio (L09–L16) |
| Migraciones | 4–6 | Seeds + least privilege (L17–L20) |
| Retro | 1 | Una query lenta explicada |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la fila de lectura de esa lección.

## Lecciones

### Semana 1 — Modelo ER y diseño conceptual (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [PostgreSQL local y carpeta de evidencia](M09/L01-postgresql-local-y-carpeta-de-evidencia.md) | 5 |
| L02 | [Entidades Cliente, Servicio, Cita](M09/L02-entidades-cliente-servicio-cita.md) | 5 |
| L03 | [Cardinalidades y reglas de negocio](M09/L03-cardinalidades-y-reglas-de-negocio.md) | 5 |
| L04 | [Glosario alineado al dominio](M09/L04-glosario-alineado-al-dominio.md) | 5 |

### Semana 2 — Normalización (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Primera forma normal y anomalías](M09/L05-primera-forma-normal-y-anomalias.md) | 5 |
| L06 | [Segunda forma normal](M09/L06-segunda-forma-normal.md) | 5 |
| L07 | [Tercera forma normal (P1)](M09/L07-tercera-forma-normal-p1.md) | 5 |
| L08 | [Trade-offs de desnormalización](M09/L08-trade-offs-de-desnormalizacion.md) | 5 |

### Semana 3 — SQL avanzado (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [Joins inner y left](M09/L09-joins-inner-y-left.md) | 5 |
| L10 | [Agregaciones y GROUP BY](M09/L10-agregaciones-y-group-by.md) | 5 |
| L11 | [Subconsultas y HAVING](M09/L11-subconsultas-y-having.md) | 5 |
| L12 | [Cinco consultas P2 comentadas](M09/L12-cinco-consultas-p2-comentadas.md) | 5 |

### Semana 4 — Índices y rendimiento (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L13 | [Índices B-tree intro](M09/L13-indices-b-tree-intro.md) | 5 |
| L14 | [EXPLAIN ANALYZE en consultas reales](M09/L14-explain-analyze-en-consultas-reales.md) | 5 |
| L15 | [Optimizar query lenta de reporte](M09/L15-optimizar-query-lenta-de-reporte.md) | 5 |
| L16 | [Documentar planes de ejecución](M09/L16-documentar-planes-de-ejecucion.md) | 5 |

### Semana 5 — Transacciones, migraciones y proyecto (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L17 | [Transacciones ACID](M09/L17-transacciones-acid.md) | 5 |
| L18 | [Migraciones versionadas](M09/L18-migraciones-versionadas.md) | 5 |
| L19 | [Least privilege (P3)](M09/L19-least-privilege-p3.md) | 5 |
| L20 | [Reportes, seeds y cierre M09](M09/L20-reportes-seeds-y-cierre-m09.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Fundamentos de sistemas de bases de datos* — Elmasri & Navathe (ed. ES). Alternativa: tutorial PostgreSQL oficial. Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos / secciones |
|--------|-----------|----------------------|
| 1 | L01–L04 | **Modelo ER** + diseño conceptual |
| 2 | L05–L08 | **Normalización** (1FN–3FN, BCNF intro) |
| 3 | L09–L12 | **SQL** avanzado (joins, agregaciones, subconsultas) |
| 4 | L13–L16 | **Índices**, plan de ejecución / `EXPLAIN` |
| 5 | L17–L20 | **Transacciones** (ACID) + migraciones + proyecto |

**Regla:** cada concepto SQL → consulta ejecutada contra tu BD de práctica, no solo lectura.

## Ejemplo — query parametrizada (idea)

```ts
// Bien: parámetros. Mal: `WHERE id = ${id}` concatenado.
await db.query(
  "SELECT * FROM citas WHERE id = $1 AND negocio_id = $2",
  [citaId, negocioId]
);
```

Regla: el identificador de negocio/tenant en el `WHERE` es autorización, no solo filtro de UI.

## Prácticas

1. **P1 — ER:** `er-agenda.md` hasta 3FN — L01–L08.
2. **P2 — SQL:** `sql/` + `explain-notas.md` — L09–L16.
3. **P3 — Migraciones:** `migrations/` + `roles.md` — L17–L19.

## Proyecto útil

**Esquema CRM / Agenda Ops con seeds y reportes:** todo bajo `projects/m09-bases-datos/`:

- Migraciones que levanten el esquema desde cero en CI o en la máquina de un compañero.
- Seeds realistas (clientes, servicios, citas en distintos estados).
- Dos reportes SQL documentados en `reportes.md` (pregunta de negocio + query + ejemplo de salida).
- README con comando `docker compose up` o equivalente si usas contenedor.

Piensa en M17: columnas que faciliten `tenant_id` más adelante (sin implementar multi-tenant aún).

## Errores comunes

- SQL injection por concatenación en el código de aplicación.
- Un solo usuario `postgres` para migraciones **y** runtime de la app.
- Migraciones manuales en producción sin historial en git.
- Índices en todas las columnas “por si acaso” sin medir.
- Olvidar FKs y arreglar integridad solo en la capa de aplicación.
- Marcar lecciones sin cumplir “Hecho cuando”.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — ER:** `projects/m09-bases-datos/er-agenda.md` (hasta 3FN) enlazado en README.
- **P2 — SQL:** `projects/m09-bases-datos/sql/` + `explain-notas.md`.
- **P3 — Migraciones:** `projects/m09-bases-datos/migrations/` + `roles.md` con least privilege demostrable.
- **Proyecto — Esquema:** Seeds + `reportes.md` con ≥2 reportes útiles.

## Criterios de dominio

- [ ] Diseñas un esquema nuevo en ~30 min y justificas cada FK.
- [ ] Demuestras una query parametrizada y un rol de BD sin superuser.
- [ ] Explicas un plan `EXPLAIN` de una query tuya en lenguaje llano.
- [ ] Otro dev puede recrear la BD siguiendo solo tu README.
