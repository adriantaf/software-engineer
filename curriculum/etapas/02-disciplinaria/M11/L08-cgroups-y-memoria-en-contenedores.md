---
id: L08
materia: M11
orden: 8
titulo: cgroups y memoria en contenedores
horas: 5
semana: 2
lectura: Docker docs memory + Silberschatz resumen
evidencia: labs/cgroups-nota.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Explicar límites de memoria en contenedores con un
      experimento o procedimiento escrito.


      Docker no “aisla magia”: usa cgroups. Hoy lo conectas con OOM de
      contenedor.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      ```bash

      docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0
      || true

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "cgroups y memoria en contenedores" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: labs/cgroups-nota.md
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0
      || true`
    comandoEsperado:
      - >-
        docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang
        0 || true
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M
      --vm-hang 0 || true
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Explicar límites de memoria en contenedores con un experimento o
          procedimiento escrito.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Experimento
    xp: 10
    cuerpo: >-
      Si tienes Docker:


      ```bash

      docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0
      || true

      ```


      Documenta el fallo. Si no hay Docker: deja el comando y describe el
      resultado esperado + plan de verificación en L13.
  - id: s7
    tipo: explicacion
    titulo: 3. Diseño piloto
    xp: 10
    cuerpo: Propón límites tentativos API vs Postgres en un VPS 2 GB.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/cgroups-nota.md` explica límite `-m`/`mem_limit` y qué ve el
        proceso.
      - >-
        Experimento documentado con `docker run --memory` (o nota si Docker no
        está disponible + comandos listos).
      - 'Commit `docs(m11): l08 cgroups memoria`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — cgroups y memoria en contenedores

**~5.0 h · Semana 2**

Docker no “aisla magia”: usa cgroups. Hoy lo conectas con OOM de contenedor.

## Objetivo

Explicar límites de memoria en contenedores con un experimento o procedimiento escrito.

## Pasos

### 1. Lectura (40 min)

Docker memory constraints + idea de cgroup v1/v2 (alto nivel). Notas en `labs/cgroups-nota.md`.

### 2. Experimento (60–75 min)

Si tienes Docker:

```bash
docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0 || true
```

Documenta el fallo. Si no hay Docker: deja el comando y describe el resultado esperado + plan de verificación en L13.

### 3. Diseño piloto (30 min)

Propón límites tentativos API vs Postgres en un VPS 2 GB.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/cgroups-nota.md
git commit -m "docs(m11): l08 cgroups memoria"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | cgroups memoria/CPU; docker run -m; por qué el límite no es “RAM del host” | [Docker · Memory constraints](https://docs.docker.com/config/containers/resource_constraints/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/cgroups-nota.md` explica límite `-m`/`mem_limit` y qué ve el proceso.
2. Experimento documentado con `docker run --memory` (o nota si Docker no está disponible + comandos listos).
3. Commit `docs(m11): l08 cgroups memoria`.

## Errores comunes

- Contenedor sin límite en un VPS pequeño compartiendo con Postgres.
- Confundir límite soft/hard.
- Pensar que cgroup “arregla leaks”.

## Siguiente

[L09 — Sistema de archivos: inodos y espacio](L09-sistema-de-archivos-inodos-y-espacio.md)
