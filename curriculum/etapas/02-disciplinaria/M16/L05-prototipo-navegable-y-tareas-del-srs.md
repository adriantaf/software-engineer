---
id: L05
materia: M16
orden: 5
titulo: Prototipo navegable y tareas del SRS
horas: 5
semana: 2
lectura: Prototipo clicable; tareas Must del SRS
evidencia: prototipo/ navegable + mapa de tareas
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `projects/m16-ihc/prototipo/` usable en test de 15–30 min.

      Sin prototipo, las sesiones inventan la UI. Hoy lo dejas clicable.
  - id: s2
    tipo: ejemplo
    titulo: 1. Pantallas mínimas
    xp: 10
    cuerpo: >-
      HTML estático o Figma prototype: Login, Agenda del día, Nueva pedido,
      Confirmación/error.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Prototipo navegable y tareas del SRS" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: prototipo/ navegable + mapa de tareas
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
      ¿Es buena práctica en esta lección? “Prototipo de marketing no usable en
      test."
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
        texto: '`projects/m16-ihc/prototipo/` usable en test de 15–30 min.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. tareas-srs.md
    xp: 10
    cuerpo: |-
      | Tarea test | Historia SRS |
      |------------|--------------|
      | Agendar pedido cliente nuevo | H-pedido-01 |
      | Cancelar pedido de hoy | H-pedido-02 |
  - id: s7
    tipo: explicacion
    titulo: 3. Commit
    xp: 10
    cuerpo: '`feat(m16): prototipo navegable y tareas SRS`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Prototipo navegable (HTML/Figma) cubriendo login → agenda → crear pedido
        (mínimo).
      - '`prototipo/tareas-srs.md` mapea tareas de test a historias Must.'
      - 'Commit `feat(m16): prototipo navegable y tareas SRS`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Prototipo navegable y tareas del SRS

**~5.0 h · Semana 2**

Sin prototipo, las sesiones inventan la UI. Hoy lo dejas clicable.

## Objetivo

`projects/m16-ihc/prototipo/` usable en test de 15–30 min.

## Pasos (hazlos en orden)

### 1. Pantallas mínimas (90–120 min)

HTML estático o Figma prototype: Login, Agenda del día, Nueva pedido, Confirmación/error.

### 2. tareas-srs.md (40 min)

| Tarea test | Historia SRS |
|------------|--------------|
| Agendar pedido cliente nuevo | H-pedido-01 |
| Cancelar pedido de hoy | H-pedido-02 |

### 3. Commit

`feat(m16): prototipo navegable y tareas SRS`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Prototipo para test de pasillo alineado al SRS | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. Prototipo navegable (HTML/Figma) cubriendo login → agenda → crear pedido (mínimo).
2. `prototipo/tareas-srs.md` mapea tareas de test a historias Must.
3. Commit `feat(m16): prototipo navegable y tareas SRS`.

## Errores comunes

- Prototipo de marketing no usable en test.
- Tareas que no existen en el SRS.
- Dependencias rotas (links muertos entre pantallas).

## Siguiente

[L06 — Guion de test de usabilidad 15–30 min](L06-guion-de-test-de-usabilidad-15-30-min.md)
