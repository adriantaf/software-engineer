---
id: L10
materia: M14
orden: 10
titulo: Command para acciones admin reversibles
horas: 5
semana: 3
lectura: Command; undo de acción admin
evidencia: src/admin/ command cancelar/restaurar + tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Owner cancela por error. Command te da vocabulario para execute/undo en el
      panel admin.


      **Objetivo de esta lección:** Command reversible de cancelación + tests.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: CancelCitaCommand
    xp: 10
    cuerpo: Guarda estado previo para undo.
  - id: s3
    tipo: ejemplo
    titulo: Tests + ADR + commit
    xp: 10
    cuerpo: '`feat(m14): command admin reversible`'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Command para acciones admin reversibles», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Command para acciones
          admin reversibles
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
      ¿Es recomendable en esta lección? “Command sin undo cuando el enunciado lo
      pide."
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
        texto: Command reversible de cancelación + tests.
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
    pregunta: ¿Debes hacer esto? “Guardar UI clicks como commands innecesarios."
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
      - Command con `execute`/`undo` para cancelar pedido (o cambiar estado).
      - 'Test: execute → estado cancelada; undo → restaurada.'
      - 'Commit `feat(m14): command admin reversible`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Command para acciones admin reversibles

**~5.0 h · Semana 3**

Owner cancela por error. Command te da vocabulario para execute/undo en el panel admin.

## Objetivo

Command reversible de cancelación + tests.

## Pasos (hazlos en orden)

### 1. Interfaz Command (25 min)

### 2. CancelCitaCommand (70–80 min)

Guarda estado previo para undo.

### 3. Tests + ADR + commit

`feat(m14): command admin reversible`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Command: encapsular acción admin con undo | [Refactoring.Guru — Command (ES)](https://refactoring.guru/es/design-patterns/command) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Command con `execute`/`undo` para cancelar pedido (o cambiar estado).
2. Test: execute → estado cancelada; undo → restaurada.
3. Commit `feat(m14): command admin reversible`.

## Errores comunes

- Command sin undo cuando el enunciado lo pide.
- Guardar UI clicks como commands innecesarios.
- Undo que ignora invariantes (restaurar sobre slot ya ocupado — documenta).

## Siguiente

[L11 — Cierre P1 — Strategy, Observer y Factory](L11-cierre-p1-strategy-observer-y-factory.md)
