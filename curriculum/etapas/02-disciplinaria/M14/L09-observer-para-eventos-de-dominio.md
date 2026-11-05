---
id: L09
materia: M14
orden: 9
titulo: Observer para eventos de dominio
horas: 5
semana: 3
lectura: Observer; pedido creada → listeners
evidencia: src/events/ observer + tests + ADR
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Crear pedido no debería conocer todos los side-effects. Observer (o event
      emitter tipado) desacopla.


      **Objetivo de esta lección:** Evento `CitaCreada` + listeners + tests +
      ADR.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tests + ADR + commit
    xp: 10
    cuerpo: '`feat(m14): observer eventos de dominio`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Observer para eventos de dominio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Observer para eventos
          de dominio
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Observer síncrono que rompe el flujo si
      un listener lanza — documenta política."
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
        texto: Evento `CitaCreada` + listeners + tests + ADR.
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
    pregunta: ¿Debes hacer esto? “Event bus global Singleton sin necesidad."
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
      - >-
        Emisor de `CitaCreada` con ≥2 listeners (p. ej. audit log + notify
        stub).
      - 'Tests: al crear, ambos listeners reciben el evento.'
      - 'Commit `feat(m14): observer eventos de dominio`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Observer para eventos de dominio

**~5.0 h · Semana 3**

Crear pedido no debería conocer todos los side-effects. Observer (o event emitter tipado) desacopla.

## Objetivo

Evento `CitaCreada` + listeners + tests + ADR.

## Pasos (hazlos en orden)

### 1. Tipos de evento (30 min)

### 2. Emitter + subscribe (60–70 min)

### 3. Integra en facade o service mínimo (40 min)

### 4. Tests + ADR + commit

`feat(m14): observer eventos de dominio`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Observer/eventos de dominio: desacoplar efectos al crear pedido | [Refactoring.Guru — Observer (ES)](https://refactoring.guru/es/design-patterns/observer) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Emisor de `CitaCreada` con ≥2 listeners (p. ej. audit log + notify stub).
2. Tests: al crear, ambos listeners reciben el evento.
3. Commit `feat(m14): observer eventos de dominio`.

## Errores comunes

- Observer síncrono que rompe el flujo si un listener lanza — documenta política.
- Event bus global Singleton sin necesidad.
- Listeners que mutan la pedido a espaldas del aggregate.

## Siguiente

[L10 — Command para acciones admin reversibles](L10-command-para-acciones-admin-reversibles.md)
