---
id: L15
materia: M14
orden: 15
titulo: Refactor P3 — módulo legacy antes y después
horas: 5
semana: 4
lectura: Refactor con comportamiento preservado
evidencia: refactor-notas.md + diff/commits (P3)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3: tomas código tuyo (spike feo, god function de precios, etc.) y lo
      refactorizas.


      **Objetivo de esta lección:** `refactor-notas.md` + evidencia en git.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige módulo
    xp: 10
    cuerpo: >-
      Si no hay legacy, crea `src/legacy/agendar-todo-en-uno.ts` a propósito y
      luego rompe el monolito.
  - id: s3
    tipo: ejemplo
    titulo: Notas + commit
    xp: 10
    cuerpo: '`refactor(m14): modulo legacy P3`'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Refactor P3 — módulo legacy antes y después», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Refactor P3 — módulo
          legacy antes y des…
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
      ¿Es recomendable en esta lección? “Reescribir de cero y llamarlo
      refactor."
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
        texto: '`refactor-notas.md` + evidencia en git.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Cambiar comportamiento observable sin test."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`refactor-notas.md` con módulo antes/después y qué patrón aplicaste.'
      - Evidencia git (commits o diff pegado) y tests verdes post-refactor.
      - >-
        Commit `refactor(m14): modulo legacy P3` (o docs si el diff está en
        notas).
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Refactor P3 — módulo legacy antes y después

**~5.0 h · Semana 4**

P3: tomas código tuyo (spike feo, god function de precios, etc.) y lo refactorizas.

## Objetivo

`refactor-notas.md` + evidencia en git.

## Pasos (hazlos en orden)

### 1. Elige módulo (20 min)

Si no hay legacy, crea `src/legacy/agendar-todo-en-uno.ts` a propósito y luego rompe el monolito.

### 2. Caracteriza con test (40 min)

### 3. Refactor hacia patrones ya vistos (80–100 min)

### 4. Notas + commit

`refactor(m14): modulo legacy P3`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Refactor de módulo legacy propio con antes/después | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `refactor-notas.md` con módulo antes/después y qué patrón aplicaste.
2. Evidencia git (commits o diff pegado) y tests verdes post-refactor.
3. Commit `refactor(m14): modulo legacy P3` (o docs si el diff está en notas).

## Errores comunes

- Reescribir de cero y llamarlo refactor.
- Cambiar comportamiento observable sin test.
- Notas sin rutas de archivo.

## Siguiente

[L16 — Cierre M14 — cinco patrones e integración M17](L16-cierre-m14-cinco-patrones-e-integracion-m17.md)
