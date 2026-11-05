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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Evento `CitaCreada` + listeners + tests + ADR.


      Crear pedido no debería conocer todos los side-effects. Observer (o event
      emitter tipado) desacopla.
  - id: s2
    tipo: ejemplo
    titulo: 4. Tests + ADR + commit
    xp: 10
    cuerpo: '`feat(m14): observer eventos de dominio`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Observer para eventos de dominio" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/events/ observer + tests + ADR
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
      ¿Es buena práctica en esta lección? “Observer síncrono que rompe el flujo
      si un listener lanza — documenta política."
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
        texto: Evento `CitaCreada` + listeners + tests + ADR.
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
      - >-
        Emisor de `CitaCreada` con ≥2 listeners (p. ej. audit log + notify
        stub).
      - 'Tests: al crear, ambos listeners reciben el evento.'
      - 'Commit `feat(m14): observer eventos de dominio`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
