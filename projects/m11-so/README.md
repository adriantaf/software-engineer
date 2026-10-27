# M11 — Sistemas operativos

Carpeta de **evidencia** + scripts/Docker del stack local Vitrina. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Administras procesos, permisos y un contenedor sin abusar de root ni meter secretos en la imagen.

## Arranque rápido

```bash
mkdir -p projects/m11-so/{labs,scripts,app,samples,backups,logs}
cd projects/m11-so
# tras L14–L15:
cp -n .env.example .env   # edita POSTGRES_PASSWORD
docker compose up -d --build
curl -s http://127.0.0.1:3099/
```

## Estructura

```
projects/m11-so/
├── README.md
├── playbook.md           # proyecto — operación local
├── restore-prueba.md     # P2 — evidencia de restore
├── Dockerfile            # P3
├── docker-compose.yml    # P3
├── .env.example
├── labs/                 # P1 — procesos, memoria, FS, docker
├── scripts/              # P2 — backup.sh, rotate-logs.sh
├── app/                  # servidor Node de labs / imagen
├── backups/              # salida local (no secretos de prod)
└── logs/
```

## Lecciones → artefactos

| Semana | Lecciones | Qué debe existir aquí |
|--------|-----------|------------------------|
| 1 | L01–L04 | labs procesos + `app/graceful-server.js` |
| 2 | L05–L08 | labs memoria / OOM / cgroups |
| 3 | L09–L12 | permisos + `scripts/backup.sh` + restore |
| 4 | L13–L16 | Dockerfile, compose, `playbook.md` |

## Checklist (Evidencia de hecho)

- **P1 — Labs:** `labs/` con procesos/señales/permisos.
- **P2 — Scripts:** `scripts/backup.sh` + rotación + `restore-prueba.md`.
- **P3 — Docker:** `Dockerfile` no-root + `docker-compose.yml`.
- **Proyecto — Playbook:** `playbook.md` enlazado desde este README.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M11-sistemas-operativos.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M11/`
- Plan: `/materia/M11/`
- Bibliografía: `curriculum/bibliografia.md#m11-sistemas-operativos`
- Producto: `curriculum/producto-saas.md`
