---
id: L16
materia: M11
orden: 16
titulo: Playbook local y cierre M11
horas: 5
semana: 4
lectura: Ficha M11 completa
evidencia: playbook.md + cierre P1–P3
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Otro desarrollador debe levantar el stack solo con tu playbook.


      **Objetivo de esta lección:** Publicar `playbook.md` y cerrar evidencias
      P1–P3.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Redacta playbook
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so
      git commit -m "docs(m11): cierre playbook"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Dry-run
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so
      git commit -m "docs(m11): cierre playbook"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Playbook local y cierre M11», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Playbook local y cierre
          M11
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

      `git add projects/m11-so`
    comandoEsperado:
      - git add projects/m11-so
      - 'git commit -m "docs(m11): cierre playbook"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m11-so'
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
        texto: Publicar `playbook.md` y cerrar evidencias P1–P3.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M11
    xp: 25
    enunciado: >-
      Cierra **Sistemas operativos** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: Procesos, señales y permisos en Linux'
      - 'P2: Scripts de administración (backup, rotación logs)'
      - 'P3: Dockerizar un servicio Node + volumen (sin root innecesario)'
      - 'Proyecto: Playbook de operación local del stack'
      - playbook.md + cierre P1–P3
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          `playbook.md` con prerequisitos, up/down, backup, restore,
          troubleshooting.
      - id: r3
        criterio: 'README enlaza P1 labs, P2 scripts, P3 Docker, playbook.'
      - id: r4
        criterio: 'Commit `docs(m11): cierre playbook`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `playbook.md` con prerequisitos, up/down, backup, restore,
        troubleshooting.
      - 'README enlaza P1 labs, P2 scripts, P3 Docker, playbook.'
      - 'Commit `docs(m11): cierre playbook`.'
    siguiente: Materia M11 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Playbook local y cierre M11

**~5.0 h · Semana 4**

Otro desarrollador debe levantar el stack solo con tu playbook.

## Objetivo

Publicar `playbook.md` y cerrar evidencias P1–P3.

## Pasos

### 1. Redacta playbook (90–110 min)

`projects/m11-so/playbook.md`:

- Prerequisitos (Docker, puertos)
- `cp .env.example .env` + editar
- `docker compose up -d --build`
- Healthcheck curl
- Backup (`scripts/backup.sh`)
- Restore de prueba (enlace)
- `docker compose down`
- Diagrama Mermaid host → api/db → volume

### 2. Dry-run (50 min)

Sigue el playbook desde cero (borra contenedores) y anota fricciones; corrígelas.

### 3. Checklist dominio (30 min)

Responde en `dominio-oral.md`: SIGTERM, backup+restore, non-root, playbook ajeno.

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): cierre playbook"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Playbook reproducible: up/down/backup/restore | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `playbook.md` con prerequisitos, up/down, backup, restore, troubleshooting.
2. README enlaza P1 labs, P2 scripts, P3 Docker, playbook.
3. Commit `docs(m11): cierre playbook`.

## Errores comunes

- Playbook que solo funciona en tu cabeza.
- Secretos en el playbook.
- Marcar dominio sin restore documentado.

## Siguiente

Cierra la [ficha M11](../M11-sistemas-operativos.md). Recomendado: [M27](../M27-sistemas-bajo-nivel.md) o sigue a [M12](../M12-requerimientos.md).
