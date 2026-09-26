---
id: L13
materia: M11
orden: 13
titulo: Imágenes, contenedores y volúmenes
horas: 5.0
semana: 4
lectura: Docker docs get started + Silberschatz síntesis
evidencia: labs/docker-intro.md
---

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

Por qué el volumen sobrevive a `docker rm` y por qué eso importa en Agenda Ops.

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
