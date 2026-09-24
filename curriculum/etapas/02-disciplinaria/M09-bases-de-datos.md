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

## Análogos
UABC: Bases de datos. Tec: Desarrollo web y BD.

## Objetivos
Modelo relacional, SQL sólido, índices, transacciones, migraciones, usuarios con permisos mínimos.

## Cómo estudiar esta materia
Diseña en papel antes de crear tablas. Cada query peligrosa → versión parametrizada.

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

## Libros (ES)
*Fundamentos de bases de datos* (Elmasri/Silberschatz, ed. ES).

## Proyecto útil
Esquema CRM + 5 reportes SQL + migraciones versionadas.

## Errores comunes
SQLi por concatenación; un solo usuario postgres para todo; sin migraciones.

## Criterios de dominio
- [ ] Diseñas un esquema nuevo en 30 min y justificas FKs.
- [ ] Demuestras una query parametrizada y un rol least-privilege.
