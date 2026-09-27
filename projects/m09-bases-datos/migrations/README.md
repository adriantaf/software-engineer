# Migraciones

Archivos numerados, **idempotentes en intención** (cada uno avanza el esquema una vez).

Orden sugerido:

| Archivo | Qué hace |
|---------|----------|
| `001_init.sql` | Extensiones + tablas base (clientes, servicios, citas) |
| `002_auditoria_y_indices.sql` | Tabla de auditoría + índices de reporte (L13–L18) |
| `003_roles_app.sql` | Grants al rol `agenda_app` (L19; o vive en `roles.md`) |

Aplicar a mano (hasta que elijas una herramienta):

```bash
# Desde projects/m09-bases-datos/ con .env cargado
set -a && source .env && set +a
psql "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" \
  -f migrations/001_init.sql
```

Registra en git cada migración que ya aplicaste en tu máquina de evidencia.
