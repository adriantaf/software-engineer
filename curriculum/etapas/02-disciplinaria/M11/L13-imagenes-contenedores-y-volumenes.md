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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Dejar notas reproducibles de imagen/contenedor/volumen.

      Antes del Dockerfile de la API: vocabulario sólido.
  - id: s2
    tipo: ejemplo
    titulo: 1. Vocabulario
    xp: 10
    cuerpo: >-
      ```bash

      docker version

      docker run --rm hello-world

      docker volume create m11-demo

      docker run --rm -v m11-demo:/data alpine sh -c 'echo hola >/data/x; cat
      /data/x'

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Imágenes, contenedores y volúmenes" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: labs/docker-intro.md
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `docker version`
    comandoEsperado:
      - docker version
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: docker version'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Dejar notas reproducibles de imagen/contenedor/volumen.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Lab
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
  - id: s7
    tipo: explicacion
    titulo: 3. Postgres
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
