---
id: L16
materia: M14
orden: 16
titulo: Cierre M14 — cinco patrones e integración M17
horas: 5
semana: 4
lectura: ≥5 patrones justificados; plan handoff M17
evidencia: README índice ≥5 + handoff-m17.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Proyecto de la materia: ≥5 patrones justificados en Vitrina + camino a
      M17.


      **Objetivo de esta lección:** Índice final + handoff; criterios de dominio
      autoevaluados.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Cuenta 5
    xp: 10
    cuerpo: >-
      Strategy, Factory, Adapter, Decorator, Facade, Observer, Command,
      Repository… elige ≥5 reales.
  - id: s3
    tipo: ejemplo
    titulo: Handoff
    xp: 10
    cuerpo: >-
      Qué se queda en `m14-patrones` vs qué nace en M17; enlaces a M13
      endpoints.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M14 — cinco patrones e integración M17», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M14 — cinco
          patrones e integraci…
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Contar Decorator+logging como 5
      patrones repetidos sin sustancia."
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
        texto: Índice final + handoff; criterios de dominio autoevaluados.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M14
    xp: 25
    enunciado: >-
      Cierra **Patrones de software** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: Implementar Strategy, Observer, Factory'
      - 'P2: Repository + Service en el backend'
      - 'P3: Refactor de un módulo legacy tuyo'
      - 'Proyecto: Aplicar ≥5 patrones en Vitrina con justificación'
      - README índice ≥5 + handoff-m17.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: README lista ≥5 patrones con enlace a código y ADR.
      - id: r3
        criterio: '`handoff-m17.md` dice qué módulos copiar/portar al repo web.'
      - id: r4
        criterio: 'Commit `docs(m14): cierre cinco patrones e integracion M17`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - README lista ≥5 patrones con enlace a código y ADR.
      - '`handoff-m17.md` dice qué módulos copiar/portar al repo web.'
      - 'Commit `docs(m14): cierre cinco patrones e integracion M17`.'
    siguiente: Materia M14 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Cierre M14 — cinco patrones e integración M17

**~5.0 h · Semana 4**

Proyecto de la materia: ≥5 patrones justificados en Vitrina + camino a M17.

## Objetivo

Índice final + handoff; criterios de dominio autoevaluados.

## Pasos (hazlos en orden)

### 1. Cuenta 5 (40 min)

Strategy, Factory, Adapter, Decorator, Facade, Observer, Command, Repository… elige ≥5 reales.

### 2. Handoff (50–60 min)

Qué se queda en `m14-patrones` vs qué nace en M17; enlaces a M13 endpoints.

### 3. Autoevaluación (30 min)

Patrón rechazado; tests de API pública; repo sin SQL en dominio.

### 4. Commit

`docs(m14): cierre cinco patrones e integracion M17`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Proyecto: ≥5 patrones con ADR; integración hacia M17 | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. README lista ≥5 patrones con enlace a código y ADR.
2. `handoff-m17.md` dice qué módulos copiar/portar al repo web.
3. Commit `docs(m14): cierre cinco patrones e integracion M17`.

## Errores comunes

- Contar Decorator+logging como 5 patrones repetidos sin sustancia.
- Sin patrón rechazado documentado.
- Handoff vacío.

## Siguiente

Materia siguiente: [M15 — V&V y calidad](../M15-vv-calidad.md) · L01 en `../M15/`.
