---
id: L14
materia: M11
orden: 14
titulo: Dockerfile Node sin root (P3)
horas: 5
semana: 4
lectura: Dockerfile reference USER
evidencia: projects/m11-so/Dockerfile
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Escribir un `Dockerfile` que no corra como root.

      P3: imagen de servicio Node endurecida lo razonable para local/piloto.
  - id: s2
    tipo: ejemplo
    titulo: 1. App mínima
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Dockerfile Node sin root (P3)" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m11-so/Dockerfile
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
    pregunta: ¿Es buena práctica en esta lección? “Correr como root sin justificación."
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
        texto: Escribir un `Dockerfile` que no corra como root.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Dockerfile
    xp: 10
    cuerpo: |-
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
  - id: s7
    tipo: ejemplo
    titulo: 3. Verificación user
    xp: 10
    cuerpo: |-
      ```bash
      docker run --rm m11-api:dev id
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`Dockerfile` multi-stage o slim con `USER` no-root.'
      - App mínima en `app/` que responde HTTP; build documentado.
      - 'Commit `feat(m11): l14 dockerfile non-root`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
