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

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md) si aún no tienes la rutina de 20 h/semana.
- **Diseña en papel o diagrama** antes de `CREATE TABLE`; cada FK debe tener una razón de negocio.
- Cada query “peligrosa” de tutorial → reescribe la versión **parametrizada** en `projects/m09-bases-datos/`.
- Ejecuta todo contra una BD local (Docker o nativa); no solo leas Elmasri.
- Piensa en M17: columnas que faciliten `tenant_id` más adelante (sin implementar multi-tenant aún).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Modelo ER | 6–8 | Diagrama + normalización |
| SQL + EXPLAIN | 6–8 | Queries del dominio |
| Migraciones | 4–6 | Seeds + least privilege |
| Retro | 1 | Una query lenta explicada |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Crea la carpeta de evidencia:
   ```bash
   mkdir -p projects/m09-bases-datos/migrations projects/m09-bases-datos/sql
   ```
2. Instala PostgreSQL (Docker Compose o local) y anota conexión en `projects/m09-bases-datos/README.md` (sin contraseñas en git).
3. Modela en papel o `er-agenda.md`: **Cliente**, **Servicio**, **Cita** (atributos, cardinalidades).
4. Primera migración: crea las 3 tablas con FKs y timestamps.
5. Crea usuario de aplicación **sin** privilegios de superuser; conecta la app o `psql` con ese rol.
6. Inserta seeds mínimos y un `JOIN` citas–cliente guardado en `projects/m09-bases-datos/sql/citas-con-cliente.sql`.
7. Commit, por ejemplo: `feat(m09): esquema inicial cliente/servicio/cita + seeds`.

## Ejemplo — query parametrizada (idea)

```ts
// Bien: parámetros. Mal: `WHERE id = ${id}` concatenado.
await db.query(
  "SELECT * FROM citas WHERE id = $1 AND negocio_id = $2",
  [citaId, negocioId]
);
```

Regla: el identificador de negocio/tenant en el `WHERE` es autorización, no solo filtro de UI.

## Temario semanal

### Semana 1 — Modelo ER y diseño conceptual (~20 h)

- Entidades, relaciones, cardinalidades del piloto Agenda Ops.
- Glosario alineado con SRS (M12) si ya existe.
- Diagrama en `projects/m09-bases-datos/er-agenda.md` o imagen exportada + fuente.
- Práctica P1 inicio: entidades core sin tablas “dios”.

### Semana 2 — Normalización (~20 h)

- 1FN, 2FN, 3FN; descomposición con dependencias funcionales.
- Ejercicios de “arreglar” tablas anómalas del dominio citas/servicios.
- Cierre P1: diagrama hasta 3FN con notas de trade-offs (desnormalización consciente solo si documentada).

### Semana 3 — SQL avanzado (~20 h)

- Inner/left join, agregaciones, `GROUP BY`, `HAVING`, subconsultas.
- Reportes de negocio: citas por semana, ingresos por servicio (datos seed).
- Práctica P2: carpeta `sql/` con ≥5 consultas útiles comentadas.

### Semana 4 — Índices y rendimiento (~20 h)

- B-tree intro; cuándo un índice ayuda y cuándo sobra.
- `EXPLAIN (ANALYZE, BUFFERS)` en al menos 2 queries; captura en `projects/m09-bases-datos/explain-notas.md`.
- Ajuste de índice en una query lenta de reporte.

### Semana 5 — Transacciones, migraciones y proyecto (~20 h)

- ACID; `BEGIN`/`COMMIT`/`ROLLBACK` en operación compuesta.
- Herramienta de migraciones (node-pg-migrate, Drizzle, Prisma migrate — elige una y documenta).
- Práctica P3: rol `app_agenda` (nombre ejemplo) con grants mínimos; sin `SUPERUSER`.
- Proyecto: seeds completos + **2 reportes** documentados para el dueño del negocio piloto.

## Lecturas

Canon: *Fundamentos de sistemas de bases de datos* — Elmasri & Navathe (ed. ES). Alternativa: tutorial PostgreSQL oficial. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos / secciones | Alternativa |
|--------|----------------------|-------------|
| 1 | **Modelo ER** + diseño conceptual (caps. de modelado) | Diagrama ER de Agenda Ops |
| 2 | **Normalización** (1FN–3FN, BCNF intro) | Ejercicios de descomposición en repo |
| 3 | **SQL** avanzado (joins, agregaciones, subconsultas) | Tutorial PostgreSQL *Querying* |
| 4 | **Índices**, plan de ejecución / `EXPLAIN` intro | Docs PostgreSQL `EXPLAIN` |
| 5 | **Transacciones** (ACID) + migraciones + proyecto reportes | Docs transacciones PG |

**Regla:** cada concepto SQL → consulta ejecutada contra tu BD de práctica, no solo lectura.

## Prácticas

1. **P1 — ER:** `projects/m09-bases-datos/er-agenda.md` (o `.png` + fuente) con normalización hasta 3FN del CRM/Agenda Ops.
2. **P2 — SQL:** `projects/m09-bases-datos/sql/` con joins/agregaciones + `explain-notas.md` con al menos un plan comentado.
3. **P3 — Migraciones:** `projects/m09-bases-datos/migrations/` versionadas + script o doc de usuario BD least-privilege en `projects/m09-bases-datos/roles.md`.

## Proyecto útil

**Esquema CRM / Agenda Ops con seeds y reportes:** todo bajo `projects/m09-bases-datos/`:

- Migraciones que levanten el esquema desde cero en CI o en la máquina de un compañero.
- Seeds realistas (clientes, servicios, citas en distintos estados).
- Dos reportes SQL documentados en `projects/m09-bases-datos/reportes.md` (pregunta de negocio + query + ejemplo de salida).
- README con comando `docker compose up` o equivalente si usas contenedor.

## Errores comunes

- SQL injection por concatenación en el código de aplicación.
- Un solo usuario `postgres` para migraciones **y** runtime de la app.
- Migraciones manuales en producción sin historial en git.
- Índices en todas las columnas “por si acaso” sin medir.
- Olvidar FKs y arreglar integridad solo en la capa de aplicación.

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
