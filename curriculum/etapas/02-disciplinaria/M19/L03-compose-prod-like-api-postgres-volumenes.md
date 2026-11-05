---
id: L03
materia: M19
orden: 3
titulo: 'Compose prod-like: API + Postgres + volúmenes'
horas: 5
semana: 1
lectura: Compose file reference
evidencia: compose.yml + projects/m19-ops/docker.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - depends_on healthy

      - volumen db-data

      - puerto 5432 no publicado


      **Objetivo de esta lección:** Orquestar API y PostgreSQL con volúmenes
      persistentes, red interna y healthchecks.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: compose prod-like
    xp: 10
    cuerpo: |-
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Up + health
    xp: 10
    cuerpo: |-
      ```bash
      docker compose up -d --build
      curl -sS http://localhost:3000/health
      docker compose ps
      ```

      Pega comandos en `projects/m19-ops/docker.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Compose prod-like: API + Postgres + volúmenes», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Compose prod-like: API
          + Postgres + vol…
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Publicar puerto 5432 al host en
      prod-like."
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
          Orquestar API y PostgreSQL con volúmenes persistentes, red interna y
          healthchecks.
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
      git add compose.yml projects/m19-ops/docker.md
      git commit -m "feat(m19): L03 compose prod-like"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`compose.yml` (o `compose.prod.yml`) API+Postgres con volumen.'
      - '`docker compose up` + `/health` 200 documentados en docker.md.'
      - 'Commit `docs(m19): L03 compose-prod-like-api-postgres-volumenes`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
