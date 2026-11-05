---
id: L12
materia: M12
orden: 12
titulo: Revisión M13 y cierre M12
horas: 5
semana: 3
lectura: Ficha M12 + handoff diseño
evidencia: nota-handoff-m13.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Dejas el testigo listo para diseño (Larman/UML en M13).


      **Objetivo de esta lección:** Handoff explícito + cierre de evidencias.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Relectura SRS
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs
      git commit -m "docs(m12): cierre handoff m13"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Handoff
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs
      git commit -m "docs(m12): cierre handoff m13"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Revisión M13 y cierre M12», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Revisión M13 y cierre
          M12
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

      `git add projects/m12-srs`
    comandoEsperado:
      - git add projects/m12-srs
      - 'git commit -m "docs(m12): cierre handoff m13"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m12-srs'
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
        texto: Handoff explícito + cierre de evidencias.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M12
    xp: 25
    enunciado: >-
      Cierra **Ingeniería de requerimientos** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: Entrevista a un negocio real (o simulado serio)'
      - 'P2: User stories + criterios de aceptación'
      - 'P3: SRS v1 con requisitos de seguridad'
      - 'Proyecto: SRS de Vitrina (piloto single-tenant)'
      - nota-handoff-m13.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          `nota-handoff-m13.md` lista entidades candidatas, 5 preguntas abiertas
          y riesgos.
      - id: r3
        criterio: README m12 con checklist P1–P3 y proyecto cerrados.
      - id: r4
        criterio: 'Commit `docs(m12): cierre handoff m13`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `nota-handoff-m13.md` lista entidades candidatas, 5 preguntas abiertas y
        riesgos.
      - README m12 con checklist P1–P3 y proyecto cerrados.
      - 'Commit `docs(m12): cierre handoff m13`.'
    siguiente: Materia M12 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Revisión M13 y cierre M12

**~5.0 h · Semana 3**

Dejas el testigo listo para diseño (Larman/UML en M13).

## Objetivo

Handoff explícito + cierre de evidencias.

## Pasos

### 1. Relectura SRS (40 min)

Lee `srs-v1.md` como si fueras M13: marca ambigüedades.

### 2. Handoff (75 min)

`nota-handoff-m13.md`:

- Entidades candidatas (Cliente, Servicio, Pedido, Usuario…)
- Casos de uso Must
- Reglas de conflicto de horario
- Preguntas abiertas
- Riesgos (alcance, datos, auth)

### 3. Dominio (30 min)

Auto-check de la ficha: ¿puedes decir “no” con alternativa escrita? ¿3 RNF? ¿Must con criterios?

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): cierre handoff m13"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Handoff a análisis/diseño: entidades, casos de uso, riesgos | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `nota-handoff-m13.md` lista entidades candidatas, 5 preguntas abiertas y riesgos.
2. README m12 con checklist P1–P3 y proyecto cerrados.
3. Commit `docs(m12): cierre handoff m13`.

## Errores comunes

- Handoff vacío “lee el SRS”.
- Reabrir alcance Must sin versión.
- No enlazar stories/SRS desde README.

## Siguiente

Cierra la [ficha M12](../M12-requerimientos.md). Siguiente: [M13 — Análisis y diseño](../M13-analisis-y-diseno.md).
