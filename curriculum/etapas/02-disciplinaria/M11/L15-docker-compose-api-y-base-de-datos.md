---
id: L15
materia: M11
orden: 15
titulo: 'docker compose: API y base de datos'
horas: 5
semana: 4
lectura: Compose file reference
evidencia: docker-compose.yml documentado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Dejar `docker-compose.yml` usable y documentado.

      El stack local del piloto: API + Postgres como en Vitrina.
  - id: s2
    tipo: ejemplo
    titulo: 1. Compose
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "docker compose: API y base de datos" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: docker-compose.yml documentado
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Publicar `5432:5432` a 0.0.0.0 sin
      necesidad."
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
        texto: Dejar `docker-compose.yml` usable y documentado.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Env example
    xp: 10
    cuerpo: '`.env.example` con `POSTGRES_PASSWORD=change-me`. `.env` en `.gitignore`.'
  - id: s7
    tipo: ejemplo
    titulo: 3. Up
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m11-so
      cp -n .env.example .env
      docker compose up -d --build
      curl -s http://127.0.0.1:3099/
      docker compose ps
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `docker-compose.yml` con API + Postgres, volumen, red, env desde
        `.env.example`.
      - 'Nota: puerto DB solo interno o localhost; API en localhost.'
      - 'Commit `feat(m11): l15 compose api db`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L15 — docker compose: API y base de datos

**~5.0 h · Semana 4**

El stack local del piloto: API + Postgres como en Vitrina.

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
