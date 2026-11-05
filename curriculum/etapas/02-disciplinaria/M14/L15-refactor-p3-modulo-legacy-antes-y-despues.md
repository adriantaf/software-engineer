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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `refactor-notas.md` + evidencia en git.


      P3: tomas código tuyo (spike feo, god function de precios, etc.) y lo
      refactorizas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige módulo
    xp: 10
    cuerpo: >-
      Si no hay legacy, crea `src/legacy/agendar-todo-en-uno.ts` a propósito y
      luego rompe el monolito.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Refactor P3 — módulo legacy antes y después" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: refactor-notas.md + diff/commits (P3)
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Reescribir de cero y llamarlo
      refactor."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: '`refactor-notas.md` + evidencia en git.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 4. Notas + commit
    xp: 10
    cuerpo: '`refactor(m14): modulo legacy P3`'
  - id: s7
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
