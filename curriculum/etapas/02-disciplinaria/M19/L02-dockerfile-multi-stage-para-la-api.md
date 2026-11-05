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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - multi-stage

      - USER node

      - HEALTHCHECK


      **Objetivo de esta lección:** Escribir Dockerfile multi-stage: build
      TS/bundle y runtime slim sin devDependencies ni fuentes.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Dockerfile multi-stage
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

      En el repo de la API (`projects/m17-vitrina/` o ruta documentada):
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: .dockerignore + build
    xp: 10
    cuerpo: >-
      ```bash

      printf '%s\n' .env node_modules .git '*.md' tests keystores >>
      .dockerignore

      docker build -t vitrina-api:dev .

      ```


      Documenta en `projects/m19-ops/docker.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Dockerfile multi-stage para la API», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Dockerfile multi-stage
          para la API
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “`COPY .env` en la imagen."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Escribir Dockerfile multi-stage: build TS/bundle y runtime slim sin
          devDependencies ni fuentes.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
