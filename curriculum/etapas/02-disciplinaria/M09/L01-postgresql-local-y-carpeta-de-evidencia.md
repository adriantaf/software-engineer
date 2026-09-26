---
id: L01
materia: M09
orden: 1
titulo: PostgreSQL local y carpeta de evidencia
horas: 5.0
semana: 1
lectura: "Elmasri: intro SGBD"
evidencia: "README conexión + docker opcional"
---

# L01 — PostgreSQL local y carpeta de evidencia

**~5.0 h · Semana 1**

Modelas y operas el esquema del producto con PostgreSQL real, parametrización y permisos mínimos.

## Objetivo

Entregar `README conexión + docker opcional` con SQL ejecutado (no solo leído).

## Pasos

### 1. Carpetas (15 min)

```bash
mkdir -p projects/m09-bases-datos/{migrations,sql}
```

### 2. PostgreSQL (60 min)

Docker Compose o nativo. Documenta host/puerto/db en README (sin password).

### 3. ER borrador (90 min)

`er-agenda.md`: Cliente, Servicio, Cita — atributos y cardinalidades.

### 4. Migración inicial (60 min)

Tres tablas + FKs + timestamps.

### 5. Rol app + seed + join (45 min)

Usuario sin superuser; `sql/citas-con-cliente.sql`; commit `feat(m09): esquema inicial`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Elmasri & Navathe | Sección de la semana |
| PostgreSQL docs | Tema equivalente (Query, EXPLAIN, Roles) |

## Hecho cuando

1. Artefacto pedido existe y fue ejecutado.
2. Sin secretos en git.
3. Commit.

## Errores comunes

- SQL concatenado estilo injection demo.
- Usuario superuser para la app.
- Migraciones solo en local sin historial.
## Siguiente

[L02 — Entidades Cliente, Servicio, Cita](L02-entidades-cliente-servicio-cita.md)
