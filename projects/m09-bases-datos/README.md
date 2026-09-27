# M09 — Bases de datos

Carpeta de **evidencia** + scaffold SQL de Agenda Ops. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Diseñas el esquema del producto: ER, SQL real, índices y migraciones sin SQL injection.

## Arranque rápido (Docker)

```bash
cd projects/m09-bases-datos
cp .env.example .env   # edita passwords locales
docker compose up -d
# espera healthy, luego:
set -a && source .env && set +a
psql "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" \
  -c 'SELECT version();'
psql "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" \
  -f migrations/001_init.sql
```

Sin Docker: instala PostgreSQL 16+, crea DB/usuario con los mismos nombres del `.env` y aplica las migraciones igual.

## Estructura

```
projects/m09-bases-datos/
├── README.md
├── docker-compose.yml
├── .env.example
├── er-agenda.md          # P1 — modelo + 3FN
├── glosario.md
├── explain-notas.md      # P2 — planes
├── roles.md              # P3 — least privilege
├── reportes.md           # Proyecto — ≥2 reportes
├── migrations/           # esquema versionado
├── seeds/                # datos demo
├── sql/                  # consultas L09–L17
└── samples/              # salidas opcionales (sin secretos)
```

## Lecciones → artefactos

| Semana | Lecciones | Qué debe existir aquí |
|--------|-----------|------------------------|
| 1 | L01–L04 | Compose/.env, `er-agenda.md` borrador, `glosario.md` |
| 2 | L05–L08 | ER hasta 3FN + nota de desnormalización |
| 3 | L09–L12 | `sql/` con joins, agg, subqueries (≥5 archivos al cierre P2) |
| 4 | L13–L16 | Índices + `explain-notas.md` |
| 5 | L17–L20 | `transaccion-cita.sql`, migraciones 002/003, `roles.md`, seeds, `reportes.md` |

## Checklist (Evidencia de hecho)

- **P1 — ER:** `er-agenda.md` hasta 3FN enlazado desde este README.
- **P2 — SQL:** `sql/` + `explain-notas.md`.
- **P3 — Migraciones:** `migrations/` + `roles.md` con least privilege demostrable.
- **Proyecto — Esquema:** `seeds/` + `reportes.md` con ≥2 reportes útiles.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M09-bases-de-datos.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M09/`
- Plan: `/materia/M09/`
- Producto: `curriculum/producto-saas.md`
