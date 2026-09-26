---
id: L14
materia: M11
orden: 14
titulo: Dockerfile Node sin root (P3)
horas: 5.0
semana: 4
lectura: Dockerfile reference USER
evidencia: projects/m11-so/Dockerfile
---

# L14 — Dockerfile Node sin root (P3)

**~5.0 h · Semana 4**

P3: imagen de servicio Node endurecida lo razonable para local/piloto.

## Objetivo

Escribir un `Dockerfile` que no corra como root.

## Pasos

### 1. App mínima (40 min)

Reutiliza o adapta `app/graceful-server.js` como `CMD`. Añade `app/package.json` si hace falta (`"type":"module"`).

### 2. Dockerfile (75 min)

```dockerfile
FROM node:20-bookworm-slim
WORKDIR /app
RUN groupadd -r app && useradd -r -g app app
COPY --chown=app:app app/package*.json ./
RUN npm ci --omit=dev || npm install --omit=dev
COPY --chown=app:app app/ ./
USER app
EXPOSE 3099
CMD ["node", "graceful-server.js"]
```

Ajusta rutas a tu layout. Documenta build:

```bash
docker build -t m11-api:dev -f projects/m11-so/Dockerfile projects/m11-so
docker run --rm -p 127.0.0.1:3099:3099 m11-api:dev
```

### 3. Verificación user (30 min)

```bash
docker run --rm m11-api:dev id
```

Debe ser `app`, no `root`.

### 4. Commit (15 min)

```bash
git add projects/m11-so/Dockerfile projects/m11-so/app
git commit -m "feat(m11): l14 dockerfile non-root"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | USER no-root; npm ci; no secretos en capas | [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `Dockerfile` multi-stage o slim con `USER` no-root.
2. App mínima en `app/` que responde HTTP; build documentado.
3. Commit `feat(m11): l14 dockerfile non-root`.

## Errores comunes

- Correr como root sin justificación.
- `COPY .` con `.env` dentro.
- `npm install` en runtime en vez de build.

## Siguiente

[L15 — docker compose: API y base de datos](L15-docker-compose-api-y-base-de-datos.md)
