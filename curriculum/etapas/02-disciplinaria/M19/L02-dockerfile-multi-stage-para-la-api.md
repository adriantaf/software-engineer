---
id: L02
materia: M19
orden: 2
titulo: Dockerfile multi-stage para la API
horas: 5.0
semana: 1
lectura: Dockerfile best practices (oficial)
evidencia: Dockerfile en repo + projects/m19-ops/docker.md
---

# L02 — Dockerfile multi-stage para la API

**~5.0 h · Semana 1**

Imagen final sin devDependencies ni `.env`.

## Objetivo

Dockerfile multi-stage + `.dockerignore`; build local exitoso.

## Pasos (hazlos en orden)

### 1. Escribe Dockerfile (90–110 min)

Stages build/runtime. USER no-root. HEALTHCHECK a `/health`.

### 2. dockerignore (20 min)

`.env`, `node_modules`, tests pesados, keystores.

### 3. Build (40 min)

```bash
docker build -t agenda-ops-api:dev .
```

### 4. Commit

`feat(m19): l02 dockerfile multi-stage`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Dockerfile best practices (oficial) | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Dockerfile multi-stage (artefacto: `Dockerfile en repo`).
2. docker.md con comandos (artefacto: `Dockerfile en repo`).
3. .dockerignore (artefacto: `Dockerfile en repo`).
4. Commit `docs(m19): L02 dockerfile-multi-stage-para-la-api`.

## Errores comunes

- COPY .env.
- root en runtime.

## Siguiente

[L03 — Compose prod-like: API + Postgres + volúmenes](L03-compose-prod-like-api-postgres-volumenes.md)
