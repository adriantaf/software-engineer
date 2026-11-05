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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Command reversible de cancelación + tests.


      Owner cancela por error. Command te da vocabulario para execute/undo en el
      panel admin.
  - id: s2
    tipo: ejemplo
    titulo: 2. CancelCitaCommand
    xp: 10
    cuerpo: Guarda estado previo para undo.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Command para acciones admin reversibles" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: src/admin/ command cancelar/restaurar + tests
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
      ¿Es buena práctica en esta lección? “Command sin undo cuando el enunciado
      lo pide."
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
        texto: Command reversible de cancelación + tests.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. Tests + ADR + commit
    xp: 10
    cuerpo: '`feat(m14): command admin reversible`'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Command con `execute`/`undo` para cancelar pedido (o cambiar estado).
      - 'Test: execute → estado cancelada; undo → restaurada.'
      - 'Commit `feat(m14): command admin reversible`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
