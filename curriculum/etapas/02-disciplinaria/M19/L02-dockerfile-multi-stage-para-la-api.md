---
id: L02
materia: M19
orden: 2
titulo: Dockerfile multi-stage para la API
horas: 5
semana: 1
lectura: Dockerfile best practices (oficial)
evidencia: Dockerfile en repo + projects/m19-ops/docker.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Escribir Dockerfile multi-stage: build TS/bundle y runtime
      slim sin devDependencies ni fuentes.


      - multi-stage

      - USER node

      - HEALTHCHECK
  - id: s2
    tipo: ejemplo
    titulo: 1. Dockerfile multi-stage
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Dockerfile multi-stage para la API" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: Dockerfile en repo + projects/m19-ops/docker.md
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “`COPY .env` en la imagen."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Escribir Dockerfile multi-stage: build TS/bundle y runtime slim sin
          devDependencies ni fuentes.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. .dockerignore + build
    xp: 10
    cuerpo: >-
      ```bash

      printf '%s\n' .env node_modules .git '*.md' tests keystores >>
      .dockerignore

      docker build -t vitrina-api:dev .

      ```


      Documenta en `projects/m19-ops/docker.md`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add Dockerfile .dockerignore projects/m19-ops/docker.md
      git commit -m "feat(m19): L02 dockerfile multi-stage"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Dockerfile multi-stage + `.dockerignore` en el repo de la API.
      - '`projects/m19-ops/docker.md` documenta `docker build` exitoso.'
      - 'Commit `docs(m19): L02 dockerfile-multi-stage-para-la-api`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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

En el repo de la API (`projects/m17-vitrina/` o ruta documentada):

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
docker build -t vitrina-api:dev .
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
