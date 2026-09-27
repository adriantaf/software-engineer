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

Imagen pequeña y sin toolchain reduce superficie.

## Objetivo

Escribir Dockerfile multi-stage: build TS/bundle y runtime slim sin devDependencies ni fuentes.

## Conceptos clave

- multi-stage
- USER node
- HEALTHCHECK

## Pasos (hazlos en orden)

### 1. Dockerfile multi-stage (90–110 min)

En el repo de la API (`projects/m17-agenda-ops/` o ruta documentada):

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:22-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup -S app && adduser -S app -G app
COPY --from=build /app /app
USER app
EXPOSE 3000
HEALTHCHECK CMD wget -qO- http://127.0.0.1:3000/health || exit 1
CMD ["node", "dist/index.js"]
```

### 2. .dockerignore + build (40–50 min)

```bash
printf '%s\n' .env node_modules .git '*.md' tests keystores >> .dockerignore
docker build -t agenda-ops-api:dev .
```

Documenta en `projects/m19-ops/docker.md`.

### 3. Commit (15 min)

```bash
git add Dockerfile .dockerignore projects/m19-ops/docker.md
git commit -m "feat(m19): L02 dockerfile multi-stage"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Dockerfile best practices (oficial) | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Dockerfile multi-stage + `.dockerignore` en el repo de la API.
2. `projects/m19-ops/docker.md` documenta `docker build` exitoso.
3. Commit `docs(m19): L02 dockerfile-multi-stage-para-la-api`.

## Errores comunes

- `COPY .env` en la imagen.
- Correr runtime como root.

## Siguiente

[L03 — Compose prod-like: API + Postgres + volúmenes](L03-compose-prod-like-api-postgres-volumenes.md)
