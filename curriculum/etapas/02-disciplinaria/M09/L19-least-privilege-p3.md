---
id: L19
materia: M09
orden: 19
titulo: Least privilege (P3)
horas: 5.0
semana: 5
lectura: "PG: roles / GRANT; Elmasri seguridad intro"
evidencia: roles.md + 003_roles_app.sql — cierra P3
---

# L19 — Least privilege (P3)

**~5.0 h · Semana 5**

El hilo de seguridad empieza aquí: la app no es dueña del clúster.

## Objetivo

Aplicar `migrations/003_roles_app.sql` (ajustando password local) y completar `roles.md`.

## Pasos

### 1. Lectura (40 min)

[PG privileges](https://www.postgresql.org/docs/current/ddl-priv.html) — GRANT/REVOKE básicos.

### 2. Ajusta y aplica 003 (45 min)

Edita la password del `CREATE ROLE` con tu `APP_DB_PASSWORD` **local**. Aplica el SQL.

### 3. Prueba positiva (40 min)

```bash
psql "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/agenda_ops" \
  -c 'SELECT count(*) FROM citas;'
```

### 4. Prueba negativa (40 min)

```sql
DROP TABLE citas;          -- debe fallar
CREATE TABLE hack(x int);  -- debe fallar
```

Pega el error en `roles.md`.

### 5. Commit (20 min) — sin secretos

```bash
git add projects/m09-bases-datos/roles.md projects/m09-bases-datos/migrations/003_roles_app.sql
git commit -m "feat(m09): rol agenda_app least privilege"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | PG: roles / GRANT; Elmasri seguridad intro | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe rol `agenda_app` (o equivalente) sin superuser.
2. Demuestras SELECT/INSERT OK y DDL denegado (error pegado en `roles.md`).
3. README marca P3 listo.

## Errores comunes

- App y migraciones con el mismo superuser.
- GRANT ALL TABLES TO PUBLIC.
- Password del rol app en el README.

## Siguiente

[L20 — Reportes, seeds y cierre M09](L20-reportes-seeds-y-cierre-m09.md)
