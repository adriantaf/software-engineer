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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Docker no “aisla magia”: usa cgroups. Hoy lo conectas con OOM de
      contenedor.


      **Objetivo de esta lección:** Explicar límites de memoria en contenedores
      con un experimento o procedimiento escrito.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      ```bash

      docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0
      || true

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Experimento
    xp: 10
    cuerpo: >-
      ```bash

      docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0
      || true

      ```


      Si tienes Docker: Documenta el fallo. Si no hay Docker: deja el comando y
      describe el resultado esperado + plan de verificación en L13.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «cgroups y memoria en contenedores», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de cgroups y memoria en
          contenedores
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang 0
      || true`
    comandoEsperado:
      - >-
        docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M --vm-hang
        0 || true
      - git add projects/m11-so/labs/cgroups-nota.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: docker run --rm -m 64m progrium/stress --vm 1 --vm-bytes 128M
      --vm-hang 0 || true
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
          Explicar límites de memoria en contenedores con un experimento o
          procedimiento escrito.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Diseño piloto
    xp: 10
    cuerpo: Propón límites tentativos API vs Postgres en un VPS 2 GB.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
