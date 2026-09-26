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

P3 sin backup es teatro.

## Objetivo

Automatizar pg_dump o backup gestionado; retención y ubicación segura.

## Conceptos clave

- pg_dump
- cron
- cifrado opcional

## Pasos (hazlos en orden)

### 1. Script backup Postgres (80–100 min)

```bash
cat > projects/m19-ops/scripts/pg_dump_daily.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail
: "${DATABASE_URL:?}"
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
OUT="backups/agenda-${STAMP}.sql.gz"
mkdir -p backups
pg_dump "$DATABASE_URL" | gzip > "$OUT"
echo "wrote $OUT"
EOF
chmod +x projects/m19-ops/scripts/pg_dump_daily.sh
```

### 2. Documenta backup.md (40 min)

```bash
cat > projects/m19-ops/backup.md << 'EOF'
# Backup
- Comando: `scripts/pg_dump_daily.sh`
- Destino: object storage / volumen cifrado
- Retención: 7–30 días
- Cron: …
EOF
# añade backups/ a .gitignore
git add projects/m19-ops/scripts/pg_dump_daily.sh projects/m19-ops/backup.md
git commit -m "feat(m19): L13 backup automatico postgresql"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | pg_dump + proveedor backups | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/scripts/pg_dump_daily.sh` + `projects/m19-ops/backup.md`.
2. Commit `docs(m19): L13 backup-automatico-postgresql`.

## Errores comunes

- Dumps con PII en el repo git.
- Backup sin retención ni destino.

## Siguiente

[L14 — Prueba de restore en entorno aislado](L14-prueba-de-restore-en-entorno-aislado.md)
