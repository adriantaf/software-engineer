---
id: L16
materia: M15
orden: 16
titulo: 'Cierre M15 — pipeline, coverage dominio, dominio'
horas: 5
semana: 4
lectura: Criterios de dominio ficha M15; pipeline verde
evidencia: README final P1–P3 + autoevaluación
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Proyecto: pipeline verde + coverage de negocio + hábitos de
      review/regresión.


      **Objetivo de esta lección:** Cierre evidenciable y handoff a M17/M18.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Verifica CI localmente
    xp: 10
    cuerpo: lint + test + audit.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m15): cierre pipeline y criterios de dominio`'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M15 — pipeline, coverage dominio, dominio», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M15 — pipeline,
          coverage dominio…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
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
        texto: Cierre evidenciable y handoff a M17/M18.
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
    pregunta: ¿Debes hacer esto? “Coverage solo boilerplate."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M15
    xp: 25
    enunciado: >-
      Cierra **Verificación, validación y calidad** con evidencia real en el
      repo. Marca la rúbrica solo si puedes demostrar cada criterio (si no está
      en git, no cuenta).
    entregables:
      - 'P1: Pirámide de tests en Vitrina'
      - 'P2: CI en GitHub Actions (lint + test + audit)'
      - 'P3: Checklist de code review (incluye seguridad)'
      - 'Proyecto: Pipeline CI verde + coverage en lógica de negocio'
      - README final P1–P3 + autoevaluación
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: 'README documenta P1 pirámide, P2 CI, P3 checklist con rutas.'
      - id: r3
        criterio: 'Autoevaluación: 401/403 automatizados; coverage enfocado a dominio.'
      - id: r4
        criterio: 'Commit `docs(m15): cierre pipeline y criterios de dominio`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'README documenta P1 pirámide, P2 CI, P3 checklist con rutas.'
      - 'Autoevaluación: 401/403 automatizados; coverage enfocado a dominio.'
      - 'Commit `docs(m15): cierre pipeline y criterios de dominio`.'
    siguiente: Materia M15 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Cierre M15 — pipeline, coverage dominio, dominio

**~5.0 h · Semana 4**

Proyecto: pipeline verde + coverage de negocio + hábitos de review/regresión.

## Objetivo

Cierre evidenciable y handoff a M17/M18.

## Pasos (hazlos en orden)

### 1. Verifica CI localmente (40 min)

lint + test + audit.

### 2. README de cierre (60 min)

### 3. Autoevaluación criterios ficha (40 min)

### 4. Commit

`docs(m15): cierre pipeline y criterios de dominio`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Cierre: CI lint+test+audit, coverage dominio, 401/403 | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. README documenta P1 pirámide, P2 CI, P3 checklist con rutas.
2. Autoevaluación: 401/403 automatizados; coverage enfocado a dominio.
3. Commit `docs(m15): cierre pipeline y criterios de dominio`.

## Errores comunes

- CI roto en main.
- Coverage solo boilerplate.
- Sin enlace a workflow.

## Siguiente

Materia siguiente: [M16 — IHC](../M16-ihc.md) · L01 en `../M16/`.
