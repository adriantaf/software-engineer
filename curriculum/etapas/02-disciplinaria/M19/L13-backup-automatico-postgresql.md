---
id: L13
materia: M19
orden: 13
titulo: Backup automático PostgreSQL
horas: 5.0
semana: 4
lectura: pg_dump + proveedor backups
evidencia: projects/m19-ops/backup.md
---

# L13 — Backup automático PostgreSQL

**~5.0 h · Semana 4**

Backup que no corre no existe.

## Objetivo

`backup.md` + script/cron `pg_dump` (o snapshot proveedor) con retención.

## Pasos (hazlos en orden)

### 1. Script dump (80–100 min)

```bash
pg_dump "$DATABASE_URL" -Fc -f backup.dump
```

Almacena fuera del contenedor efímero.

### 2. Automatiza (40 min)

Cron/GitHub scheduled/PaaS job. Documenta.

### 3. Commit

`feat(m19): l13 backup postgres`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | pg_dump + proveedor backups | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Procedimiento escrito (artefacto: `projects/m19-ops/backup.md`).
2. Job programado o gestionado (artefacto: `projects/m19-ops/backup.md`).
3. Tamaño estimado (artefacto: `projects/m19-ops/backup.md`).
4. Commit `docs(m19): L13 backup-automatico-postgresql`.

## Errores comunes

- Backup manual olvidado.
- Dump en repo git.

## Siguiente

[L14 — Prueba de restore en entorno aislado](L14-prueba-de-restore-en-entorno-aislado.md)
