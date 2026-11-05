---
id: L11
materia: M14
orden: 11
titulo: 'Cierre P1 — Strategy, Observer y Factory'
horas: 5
semana: 3
lectura: 'Evidencia P1: 3 patrones con tests y ADRs'
evidencia: README P1 checklist + suite verde
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 de la ficha: tres patrones con justificación. Hoy cierras evidencia.


      **Objetivo de esta lección:** Checklist P1 verificable en git.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m14): cierre P1 strategy observer factory`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre P1 — Strategy, Observer y Factory», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre P1 — Strategy,
          Observer y Factory
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Marcar P1 con un solo patrón."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: Checklist P1 verificable en git.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “ADRs vacíos."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Strategy, Observer y Factory tienen código + tests + ADR cada uno.'
      - README marca P1 con rutas.
      - 'Commit `docs(m14): cierre P1 strategy observer factory`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Cierre P1 — Strategy, Observer y Factory

**~5.0 h · Semana 3**

P1 de la ficha: tres patrones con justificación. Hoy cierras evidencia.

## Objetivo

Checklist P1 verificable en git.

## Pasos (hazlos en orden)

### 1. `npm test` (20 min)

### 2. Tabla P1 en README (50 min)

### 3. Relee ADRs (40 min) — una frase de “por qué no if/switch”

### 4. Commit

`docs(m14): cierre P1 strategy observer factory`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Cierre práctica P1: Strategy + Observer + Factory | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Strategy, Observer y Factory tienen código + tests + ADR cada uno.
2. README marca P1 con rutas.
3. Commit `docs(m14): cierre P1 strategy observer factory`.

## Errores comunes

- Marcar P1 con un solo patrón.
- ADRs vacíos.
- Tests fallando en CI local.

## Siguiente

[L12 — Repaso comportamiento y anti-patrón propio](L12-repaso-comportamiento-y-anti-patron-propio.md)
