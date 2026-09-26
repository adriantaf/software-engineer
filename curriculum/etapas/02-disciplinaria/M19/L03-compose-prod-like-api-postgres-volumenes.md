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

Compose que imita prod: red interna, volumen datos, env file.

## Objetivo

`compose.yml` (o `compose.prod.yml`) API+Postgres; `docker compose up` documentado.

## Pasos (hazlos en orden)

### 1. Compose (80–100 min)

Depends_on healthy; puerto solo lo necesario; secrets via env_file no bakeado.

### 2. Prueba (50–60 min)

Up → health → login smoke local.

### 3. Commit

`feat(m19): l03 compose prod-like`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Compose file reference | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Compose levanta stack (artefacto: `compose.yml`).
2. Healthcheck OK (artefacto: `compose.yml`).
3. Postgres con volumen (artefacto: `compose.yml`).
4. Commit `docs(m19): L03 compose-prod-like-api-postgres-volumenes`.

## Errores comunes

- 5432:5432 público.
- password en compose commiteado.

## Siguiente

[L04 — Stack local documentado y P1 Docker](L04-stack-local-documentado-y-p1-docker.md)
