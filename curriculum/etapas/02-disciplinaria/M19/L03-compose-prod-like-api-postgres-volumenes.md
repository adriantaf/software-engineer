---
id: L03
materia: M19
orden: 3
titulo: "Compose prod-like: API + Postgres + volúmenes"
horas: 5.0
semana: 1
lectura: Compose file reference
evidencia: compose.yml + projects/m19-ops/docker.md
---

# L03 — Compose prod-like: API + Postgres + volúmenes

**~5.0 h · Semana 1**

P1 M19 es stack local idéntico en espíritu a prod.

## Objetivo

Orquestar API y PostgreSQL con volúmenes persistentes, red interna y healthchecks.

## Conceptos clave

- depends_on healthy
- volumen db-data
- puerto 5432 no publicado

## Pasos (hazlos en orden)

### 1. compose prod-like (80–100 min)

```yaml
# compose.yml (ejemplo)
services:
  db:
    image: postgres:16-alpine
    volumes: ["pgdata:/var/lib/postgresql/data"]
    env_file: [.env]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER"]
  api:
    build: .
    depends_on:
      db: { condition: service_healthy }
    env_file: [.env]
    ports: ["3000:3000"]
volumes:
  pgdata:
```

### 2. Up + health (50–60 min)

```bash
docker compose up -d --build
curl -sS http://localhost:3000/health
docker compose ps
```

Pega comandos en `projects/m19-ops/docker.md`.

### 3. Commit (15 min)

```bash
git add compose.yml projects/m19-ops/docker.md
git commit -m "feat(m19): L03 compose prod-like"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Compose file reference | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `compose.yml` (o `compose.prod.yml`) API+Postgres con volumen.
2. `docker compose up` + `/health` 200 documentados en docker.md.
3. Commit `docs(m19): L03 compose-prod-like-api-postgres-volumenes`.

## Errores comunes

- Publicar puerto 5432 al host en prod-like.
- Secrets bakeados en la imagen.

## Siguiente

[L04 — Stack local documentado y P1 Docker](L04-stack-local-documentado-y-p1-docker.md)
