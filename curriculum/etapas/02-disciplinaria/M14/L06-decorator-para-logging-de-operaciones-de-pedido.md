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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Decorator de logging sobre operaciones de pedido.


      Quieres auditoría de “quién creó pedido” sin contaminar el dominio con
      Winston.
  - id: s2
    tipo: ejemplo
    titulo: 1. Interfaz CitaOps
    xp: 10
    cuerpo: '`create`, `cancel` mínimos (pueden ser in-memory).'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Decorator para logging de operaciones de pedido" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: src/pedidos/ decorator logger + tests
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
      ¿Es buena práctica en esta lección? “Meter `console.log` dentro de la
      regla de solape."
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
        texto: Decorator de logging sobre operaciones de pedido.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. LoggingCitaOps
    xp: 10
    cuerpo: Delega + empuja a un `LogSink` inyectable.
  - id: s7
    tipo: explicacion
    titulo: 3. Tests (40 min) + ADR + commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
