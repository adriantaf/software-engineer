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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Checklist P1 verificable en git.

      P1 de la ficha: tres patrones con justificación. Hoy cierras evidencia.
  - id: s2
    tipo: ejemplo
    titulo: 4. Commit
    xp: 10
    cuerpo: '`docs(m14): cierre P1 strategy observer factory`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre P1 — Strategy, Observer y Factory" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: README P1 checklist + suite verde
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
    pregunta: ¿Es buena práctica en esta lección? “Marcar P1 con un solo patrón."
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
        texto: Checklist P1 verificable en git.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Strategy, Observer y Factory tienen código + tests + ADR cada uno.'
      - README marca P1 con rutas.
      - 'Commit `docs(m14): cierre P1 strategy observer factory`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
