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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Facade `agendarCita` + tests de feliz/error.


      El caso de uso “agendar” toca varias piezas. Facade ofrece una puerta al
      application layer.
  - id: s2
    tipo: ejemplo
    titulo: 1. Subsistemas stubs
    xp: 10
    cuerpo: 'Validador de solape, repo in-memory, notifier no-op.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Facade para el flujo agendar pedido" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: src/pedidos/agendar-facade.ts + tests
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
    pregunta: ¿Es buena práctica en esta lección? “Facade dios de 20 dependencias."
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
        texto: Facade `agendarCita` + tests de feliz/error.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Facade
    xp: 10
    cuerpo: Orquesta; traduce errores a resultados tipados.
  - id: s7
    tipo: explicacion
    titulo: 3. Tests + ADR + commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
