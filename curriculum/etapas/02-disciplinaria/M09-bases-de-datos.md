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
Los datos son el corazón del producto. Mal modelados = dolor eterno. Seguridad: **queries parametrizadas + least privilege** ([hilo](../../hilos/seguridad.md)).

**En cristiano:** diseñas el esquema del producto: ER, SQL real, índices y migraciones sin SQL injection.

## Análogos
UABC: Bases de datos. Tec: Desarrollo web y BD.

## Objetivos
Modelo relacional, SQL sólido, índices, transacciones, migraciones, usuarios con permisos mínimos.

## Cómo estudiar esta materia
Diseña en papel antes de crear tablas. Cada query peligrosa → versión parametrizada.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Modelo ER | 6–8 | Diagrama + normalización |
| SQL + EXPLAIN | 6–8 | Queries del dominio |
| Migraciones | 4–6 | Seeds + least privilege |
| Retro | 1 | Una query lenta explicada |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)
1. Instala PostgreSQL (o Docker).
2. Modela en papel: Cliente, Servicio, Cita.
3. Crea las 3 tablas y un usuario DB **sin** privilegios de superuser para la app.
4. Inserta seeds y un `JOIN` de citas con cliente.

## Ejemplo — parametrizado (idea)
```ts
// Bien: parámetros. Mal: `WHERE id = ${id}` concatenado.
await db.query("SELECT * FROM citas WHERE id = $1 AND user_id = $2", [citaId, userId]);
```

## Temario
ER → normalización → SQL avanzado → índices/EXPLAIN intro → transacciones/migraciones → proyecto reportes.

## Lecturas

Canon: *Fundamentos de sistemas de bases de datos* — Elmasri & Navathe (ed. ES). Alternativa: tutorial PostgreSQL oficial. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos / secciones | Alternativa |
|--------|----------------------|-------------|
| 1 | **Modelo ER** + diseño conceptual (caps. de modelado) | Diagrama ER de Agenda Ops |
| 2 | **Normalización** (1FN–3FN, BCNF intro) | Ejercicios de descomposición |
| 3 | **SQL** avanzado (joins, agregaciones, subconsultas) | Tutorial PostgreSQL *Querying* |
| 4 | **Índices**, plan de ejecución / `EXPLAIN` intro | Docs PostgreSQL `EXPLAIN` |
| 5 | **Transacciones** (ACID) + migraciones + proyecto reportes | Docs transacciones PG |

**Regla:** cada concepto SQL → consulta contra tu BD de práctica, no solo lectura.

## Proyecto útil
Esquema CRM + 5 reportes SQL + migraciones versionadas.

## Errores comunes
SQLi por concatenación; un solo usuario postgres para todo; sin migraciones.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — ER:** Diagrama hasta 3FN del CRM/Agenda.
- **P2 — SQL:** Joins/agregaciones + `EXPLAIN` comentado.
- **P3 — Migraciones:** Migraciones versionadas + usuario BD con least privilege.
- **Proyecto — Esquema:** Seeds + 2 reportes útiles documentados.

## Criterios de dominio
- [ ] Diseñas un esquema nuevo en 30 min y justificas FKs.
- [ ] Demuestras una query parametrizada y un rol least-privilege.
