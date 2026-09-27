---
id: L15
materia: M11
orden: 15
titulo: "docker compose: API y base de datos"
horas: 5.0
semana: 4
lectura: Compose file reference
evidencia: docker-compose.yml documentado
---

# L15 — docker compose: API y base de datos

**~5.0 h · Semana 4**

El stack local del piloto: API + Postgres como en Agenda Ops.

## Objetivo

Dejar `docker-compose.yml` usable y documentado.

## Pasos

### 1. Compose (90 min)

`projects/m11-so/docker-compose.yml` (ajusta nombres):

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: agenda
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: agenda
    volumes:
      - pgdata:/var/lib/postgresql/data
    # no ports: públicos; la API habla por la red compose
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U agenda"]
      interval: 5s
      timeout: 5s
      retries: 5
  api:
    build: .
    environment:
      PORT: 3099
      DATABASE_URL: postgres://agenda:${POSTGRES_PASSWORD}@db:5432/agenda
    ports:
      - "127.0.0.1:3099:3099"
    depends_on:
      db:
        condition: service_healthy
volumes:
  pgdata:
```

### 2. Env example (30 min)

`.env.example` con `POSTGRES_PASSWORD=change-me`. `.env` en `.gitignore`.

### 3. Up (40 min)

```bash
cd projects/m11-so
cp -n .env.example .env
docker compose up -d --build
curl -s http://127.0.0.1:3099/
docker compose ps
```

### 4. Commit (15 min)

```bash
git add projects/m11-so/docker-compose.yml projects/m11-so/.env.example
git commit -m "feat(m11): l15 compose api db"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Servicios api+db; red interna; volúmenes; no exponer 5432 públicamente | [Compose specification](https://docs.docker.com/compose/compose-file/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `docker-compose.yml` con API + Postgres, volumen, red, env desde `.env.example`.
2. Nota: puerto DB solo interno o localhost; API en localhost.
3. Commit `feat(m11): l15 compose api db`.

## Errores comunes

- Publicar `5432:5432` a 0.0.0.0 sin necesidad.
- Passwords en el YAML commiteadas.
- Olvidar healthcheck / depends_on con criterio.

## Siguiente

[L16 — Playbook local y cierre M11](L16-playbook-local-y-cierre-m11.md)
