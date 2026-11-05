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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3: imagen de servicio Node endurecida lo razonable para local/piloto.


      **Objetivo de esta lección:** Escribir un `Dockerfile` que no corra como
      root.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: App mínima
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Dockerfile
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Dockerfile Node sin root (P3)», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Dockerfile Node sin
          root (P3)
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
    pregunta: ¿Es recomendable en esta lección? “Correr como root sin justificación."
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
        texto: Escribir un `Dockerfile` que no corra como root.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Verificación user
    xp: 10
    cuerpo: 'Debe ser `app`, no `root`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`Dockerfile` multi-stage o slim con `USER` no-root.'
      - App mínima en `app/` que responde HTTP; build documentado.
      - 'Commit `feat(m11): l14 dockerfile non-root`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
