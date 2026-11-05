---
id: L16
materia: M14
orden: 16
titulo: Cierre M14 — cinco patrones e integración M17
horas: 5
semana: 4
lectura: ≥5 patrones justificados; plan handoff M17
evidencia: README índice ≥5 + handoff-m17.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Índice final + handoff; criterios de dominio autoevaluados.


      Proyecto de la materia: ≥5 patrones justificados en Vitrina + camino a
      M17.
  - id: s2
    tipo: ejemplo
    titulo: 1. Cuenta 5
    xp: 10
    cuerpo: >-
      Strategy, Factory, Adapter, Decorator, Facade, Observer, Command,
      Repository… elige ≥5 reales.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M14 — cinco patrones e integración M17" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: README índice ≥5 + handoff-m17.md
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
      ¿Es buena práctica en esta lección? “Contar Decorator+logging como 5
      patrones repetidos sin sustancia."
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
        texto: Índice final + handoff; criterios de dominio autoevaluados.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Handoff
    xp: 10
    cuerpo: >-
      Qué se queda en `m14-patrones` vs qué nace en M17; enlaces a M13
      endpoints.
  - id: s7
    tipo: explicacion
    titulo: 3. Autoevaluación
    xp: 10
    cuerpo: Patrón rechazado; tests de API pública; repo sin SQL en dominio.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - README lista ≥5 patrones con enlace a código y ADR.
      - '`handoff-m17.md` dice qué módulos copiar/portar al repo web.'
      - 'Commit `docs(m14): cierre cinco patrones e integracion M17`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Cierre M14 — cinco patrones e integración M17

**~5.0 h · Semana 4**

Proyecto de la materia: ≥5 patrones justificados en Vitrina + camino a M17.

## Objetivo

Índice final + handoff; criterios de dominio autoevaluados.

## Pasos (hazlos en orden)

### 1. Cuenta 5 (40 min)

Strategy, Factory, Adapter, Decorator, Facade, Observer, Command, Repository… elige ≥5 reales.

### 2. Handoff (50–60 min)

Qué se queda en `m14-patrones` vs qué nace en M17; enlaces a M13 endpoints.

### 3. Autoevaluación (30 min)

Patrón rechazado; tests de API pública; repo sin SQL en dominio.

### 4. Commit

`docs(m14): cierre cinco patrones e integracion M17`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Proyecto: ≥5 patrones con ADR; integración hacia M17 | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. README lista ≥5 patrones con enlace a código y ADR.
2. `handoff-m17.md` dice qué módulos copiar/portar al repo web.
3. Commit `docs(m14): cierre cinco patrones e integracion M17`.

## Errores comunes

- Contar Decorator+logging como 5 patrones repetidos sin sustancia.
- Sin patrón rechazado documentado.
- Handoff vacío.

## Siguiente

Materia siguiente: [M15 — V&V y calidad](../M15-vv-calidad.md) · L01 en `../M15/`.
