---
id: L13
materia: M11
orden: 13
titulo: 'Imágenes, contenedores y volúmenes'
horas: 5
semana: 4
lectura: Docker docs get started + Silberschatz síntesis
evidencia: labs/docker-intro.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Antes del Dockerfile de la API: vocabulario sólido.


      **Objetivo de esta lección:** Dejar notas reproducibles de
      imagen/contenedor/volumen.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Vocabulario
    xp: 10
    cuerpo: >-
      ```bash

      docker version

      docker run --rm hello-world

      docker volume create m11-demo

      docker run --rm -v m11-demo:/data alpine sh -c 'echo hola >/data/x; cat
      /data/x'

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Lab
    xp: 10
    cuerpo: >-
      ```bash

      docker version

      docker run --rm hello-world

      docker volume create m11-demo

      docker run --rm -v m11-demo:/data alpine sh -c 'echo hola >/data/x; cat
      /data/x'

      ```


      Si Docker no está: instálalo o documenta el bloqueo y comandos exactos
      para cuando lo tengas (el playbook L16 lo exigirá).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Imágenes, contenedores y volúmenes», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Imágenes, contenedores
          y volúmenes
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `docker version`
    comandoEsperado:
      - docker version
      - docker run --rm hello-world
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: docker version'
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
        texto: Dejar notas reproducibles de imagen/contenedor/volumen.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Postgres
    xp: 10
    cuerpo: >-
      Por qué el volumen sobrevive a `docker rm` y por qué eso importa en
      Vitrina.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/docker-intro.md` con vocabulario y un `docker run`/`volume`
        documentado.
      - Explicas por qué el FS del contenedor no basta para Postgres.
      - 'Commit `docs(m11): l13 docker intro`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — Imágenes, contenedores y volúmenes

**~5.0 h · Semana 4**

Antes del Dockerfile de la API: vocabulario sólido.

## Objetivo

Dejar notas reproducibles de imagen/contenedor/volumen.

## Pasos

### 1. Vocabulario (40 min)

Tabla en `labs/docker-intro.md`: image, container, layer, registry, volume, network.

### 2. Lab (60–75 min)

```bash
docker version
docker run --rm hello-world
docker volume create m11-demo
docker run --rm -v m11-demo:/data alpine sh -c 'echo hola >/data/x; cat /data/x'
```

Si Docker no está: instálalo o documenta el bloqueo y comandos exactos para cuando lo tengas (el playbook L16 lo exigirá).

### 3. Postgres (30 min)

Por qué el volumen sobrevive a `docker rm` y por qué eso importa en Vitrina.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/docker-intro.md
git commit -m "docs(m11): l13 docker intro"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Imagen vs contenedor; capas; volúmenes para datos persistentes | [Docker Get Started](https://docs.docker.com/get-started/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/docker-intro.md` con vocabulario y un `docker run`/`volume` documentado.
2. Explicas por qué el FS del contenedor no basta para Postgres.
3. Commit `docs(m11): l13 docker intro`.

## Errores comunes

- Guardar la BD solo en la capa writable del contenedor.
- Confundir bind mount con named volume.
- Correr todo `--privileged`.

## Siguiente

[L14 — Dockerfile Node sin root (P3)](L14-dockerfile-node-sin-root-p3.md)
