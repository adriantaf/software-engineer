---
id: L07
materia: M14
orden: 7
titulo: Facade para el flujo agendar pedido
horas: 5
semana: 2
lectura: Facade; orquestar validación + persistencia + notify
evidencia: src/pedidos/agendar-facade.ts + tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El caso de uso “agendar” toca varias piezas. Facade ofrece una puerta al
      application layer.


      **Objetivo de esta lección:** Facade `agendarCita` + tests de feliz/error.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Subsistemas stubs
    xp: 10
    cuerpo: 'Validador de solape, repo in-memory, notifier no-op.'
  - id: s3
    tipo: ejemplo
    titulo: Facade
    xp: 10
    cuerpo: Orquesta; traduce errores a resultados tipados.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Facade para el flujo agendar pedido», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Facade para el flujo
          agendar pedido
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
    pregunta: ¿Es recomendable en esta lección? “Facade dios de 20 dependencias."
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
        texto: Facade `agendarCita` + tests de feliz/error.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests + ADR + commit
    xp: 10
    cuerpo: '`feat(m14): facade agendar pedido`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `agendarCita(...)` facade coordina validación + save + notify (stubs
        ok).
      - >-
        Test de flujo feliz y un fallo (p. ej. slot ocupado) sin que el caller
        toque 3 servicios.
      - 'Commit `feat(m14): facade agendar pedido`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Facade para el flujo agendar pedido

**~5.0 h · Semana 2**

El caso de uso “agendar” toca varias piezas. Facade ofrece una puerta al application layer.

## Objetivo

Facade `agendarCita` + tests de feliz/error.

## Pasos (hazlos en orden)

### 1. Subsistemas stubs (40 min)

Validador de solape, repo in-memory, notifier no-op.

### 2. Facade (60–70 min)

Orquesta; traduce errores a resultados tipados.

### 3. Tests + ADR + commit

`feat(m14): facade agendar pedido`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Facade: API simple sobre subsistema de agendar | [Refactoring.Guru — Facade (ES)](https://refactoring.guru/es/design-patterns/facade) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `agendarCita(...)` facade coordina validación + save + notify (stubs ok).
2. Test de flujo feliz y un fallo (p. ej. slot ocupado) sin que el caller toque 3 servicios.
3. Commit `feat(m14): facade agendar pedido`.

## Errores comunes

- Facade dios de 20 dependencias.
- Duplicar reglas fuera y dentro del facade.
- Sin test del camino de error.

## Siguiente

[L08 — Tests de regresión en API pública del módulo](L08-tests-de-regresion-en-api-publica-del-modulo.md)
