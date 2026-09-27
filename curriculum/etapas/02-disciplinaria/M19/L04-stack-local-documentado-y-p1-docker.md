---
id: L04
materia: M19
orden: 4
titulo: Stack local documentado y P1 Docker
horas: 5.0
semana: 1
lectura: Repaso semana 1
evidencia: projects/m19-ops/docker.md completo
---

# L04 — Stack local documentado y P1 Docker

**~5.0 h · Semana 1**

Cierra semana 1 con P1 listo para marcar.

## Objetivo

Consolidar instrucciones un comando, troubleshooting y evidencia de login/pedido en contenedores.

## Conceptos clave

- reproducibilidad
- logs compose

## Pasos (hazlos en orden)

### 1. Cierra docker.md P1 (60–80 min)

```bash
cat >> projects/m19-ops/docker.md << 'EOF'
## Comandos
- build: `docker build -t vitrina-api:dev .`
- up: `docker compose up -d`
- down: `docker compose down`
- logs: `docker compose logs -f api`
EOF
```

### 2. Verifica end-to-end local (40 min)

```bash
docker compose down && docker compose up -d --build
curl -sS http://localhost:3000/health
# login smoke local (cookie) — anota OK en docker.md
git add projects/m19-ops/docker.md
git commit -m "docs(m19): L04 docker.md P1 completo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Repaso semana 1 | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/docker.md` completo (build/up/down/logs) — P1.
2. Commit `docs(m19): L04 stack-local-documentado-y-p1-docker`.

## Errores comunes

- docker.md sin comandos copy-pasteables.
- Marcar P1 sin `compose up` real.

## Siguiente

[L05 — ADR hosting: PaaS vs VPS](L05-adr-hosting-paas-vs-vps.md)
