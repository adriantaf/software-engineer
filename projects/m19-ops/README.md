# M19 — Cómputo en la nube y DevOps

Carpeta de **evidencia** ops del piloto Vitrina. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

El piloto sobrevive fuera de tu laptop: Docker, secretos, HTTPS, backup con restore probado.

## Arranque rápido (local prod-like)

```bash
cd projects/m17-vitrina   # o ruta del Dockerfile
docker build -t vitrina-api:dev .
docker compose -f compose.yml up -d
curl -sS http://localhost:3000/health
```

Documenta los comandos reales en `docker.md`.

## Estructura esperada

```
projects/m19-ops/
├── README.md
├── ambientes.md          # staging vs prod (sin secretos)
├── docker.md             # P1
├── deploy-log.md         # P2
├── backup.md
├── restore-test.md       # P3
├── runbook.md            # Proyecto
├── adr-hosting.md
├── docs/
│   ├── monitoreo.md
│   └── host-security.md
├── scripts/              # dump/restore helpers
└── logs/                 # capturas redactadas opcionales
```

## Lecciones → artefactos

| Semana | Foco | Artefacto |
|--------|------|-----------|
| 1 | Docker multi-stage + Compose | `docker.md` (P1) |
| 2 | Staging HTTPS + smoke | `deploy-log.md` |
| 3 | Prod, logs, rollback, host | runbook borrador |
| 4 | Backup + restore + runbook | `restore-test.md` (P3), `runbook.md` |

## Checklist (Evidencia de hecho)

- **P1 — Imágenes:** Dockerfile multi-stage + Compose documentados.
- **P2 — Deploy:** URL HTTPS en `deploy-log.md`; secretos fuera de la imagen.
- **P3 — Restore:** `restore-test.md` con fecha y resultado real.
- **Proyecto — Runbook:** `runbook.md` completo.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M19-nube-devops.md`
- App: `projects/m17-vitrina/`
- Plan: `/materia/M19/`
