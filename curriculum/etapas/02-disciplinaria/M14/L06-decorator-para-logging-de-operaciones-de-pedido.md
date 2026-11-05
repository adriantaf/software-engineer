---
id: L06
materia: M14
orden: 6
titulo: Decorator para logging de operaciones de pedido
horas: 5
semana: 2
lectura: Decorator; logging sin ensuciar el core
evidencia: src/pedidos/ decorator logger + tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Quieres auditoría de “quién creó pedido” sin contaminar el dominio con
      Winston.


      **Objetivo de esta lección:** Decorator de logging sobre operaciones de
      pedido.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Interfaz CitaOps
    xp: 10
    cuerpo: '`create`, `cancel` mínimos (pueden ser in-memory).'
  - id: s3
    tipo: ejemplo
    titulo: LoggingCitaOps
    xp: 10
    cuerpo: Delega + empuja a un `LogSink` inyectable.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Decorator para logging de operaciones de pedido», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Decorator para logging
          de operaciones d…
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
      ¿Es recomendable en esta lección? “Meter `console.log` dentro de la regla
      de solape."
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
        texto: Decorator de logging sobre operaciones de pedido.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests (40 min) + ADR + commit
    xp: 10
    cuerpo: '`feat(m14): decorator logging pedidos`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Decorador envuelve un `CitaOps` (o similar) y registra llamada sin
        cambiar el resultado.
      - Test demuestra que el inner se invoca y que el log recibe evento.
      - 'Commit `feat(m14): decorator logging pedidos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Decorator para logging de operaciones de pedido

**~5.0 h · Semana 2**

Quieres auditoría de “quién creó pedido” sin contaminar el dominio con Winston.

## Objetivo

Decorator de logging sobre operaciones de pedido.

## Pasos (hazlos en orden)

### 1. Interfaz CitaOps (30 min)

`create`, `cancel` mínimos (pueden ser in-memory).

### 2. LoggingCitaOps (60–70 min)

Delega + empuja a un `LogSink` inyectable.

### 3. Tests (40 min) + ADR + commit

`feat(m14): decorator logging pedidos`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Decorator: añade logging cruzando la misma interfaz | [Refactoring.Guru — Decorator (ES)](https://refactoring.guru/es/design-patterns/decorator) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Decorador envuelve un `CitaOps` (o similar) y registra llamada sin cambiar el resultado.
2. Test demuestra que el inner se invoca y que el log recibe evento.
3. Commit `feat(m14): decorator logging pedidos`.

## Errores comunes

- Meter `console.log` dentro de la regla de solape.
- Decorator que cambia reglas de negocio “de paso”.
- Sin interfaz común inner/outer.

## Siguiente

[L07 — Facade para el flujo agendar pedido](L07-facade-para-el-flujo-agendar-pedido.md)
