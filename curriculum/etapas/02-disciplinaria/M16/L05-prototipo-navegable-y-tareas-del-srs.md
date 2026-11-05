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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin prototipo, las sesiones inventan la UI. Hoy lo dejas clicable.


      **Objetivo de esta lección:** `projects/m16-ihc/prototipo/` usable en test
      de 15–30 min.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Pantallas mínimas
    xp: 10
    cuerpo: >-
      HTML estático o Figma prototype: Login, Agenda del día, Nueva pedido,
      Confirmación/error.
  - id: s3
    tipo: ejemplo
    titulo: tareas-srs.md
    xp: 10
    cuerpo: >-
      | Tarea test | Historia SRS | |------------|--------------| | Agendar
      pedido cliente nuevo | H-pedido-01 | | Cancelar pedido de hoy |
      H-pedido-02 |
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Prototipo navegable y tareas del SRS», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Prototipo navegable y
          tareas del SRS
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
      ¿Es recomendable en esta lección? “Prototipo de marketing no usable en
      test."
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
        texto: '`projects/m16-ihc/prototipo/` usable en test de 15–30 min.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
