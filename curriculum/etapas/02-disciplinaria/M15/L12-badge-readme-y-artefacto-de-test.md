---
id: L12
materia: M15
orden: 12
titulo: Badge README y artefacto de test
horas: 5
semana: 3
lectura: Badges Actions; artifacts opcionales
evidencia: README con badge/enlace CI + nota de artefacto
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Si el pipeline no se ve, no existe para el equipo-de-uno futuro.


      **Objetivo de esta lección:** README con señal de CI + instrucciones
      locales.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m15): badge ci y artefacto`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Badge README y artefacto de test», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Badge README y
          artefacto de test
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
    pregunta: ¿Es recomendable en esta lección? “Badge a repo ajeno."
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
        texto: README con señal de CI + instrucciones locales.
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
    pregunta: ¿Debes hacer esto? “Prometer coverage upload sin secretos/config."
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
      - README M15 muestra badge o enlace claro al workflow.
      - >-
        Documentas (o configuras) artefacto de reporte de test/coverage
        opcional.
      - 'Commit `docs(m15): badge ci y artefacto`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Badge README y artefacto de test

**~5.0 h · Semana 3**

Si el pipeline no se ve, no existe para el equipo-de-uno futuro.

## Objetivo

README con señal de CI + instrucciones locales.

## Pasos (hazlos en orden)

### 1. Badge o enlace (30 min)

### 2. Sección “Cómo correr tests” (40 min)

### 3. Commit

`docs(m15): badge ci y artefacto`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Visibilidad del pipeline en README M15 | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. README M15 muestra badge o enlace claro al workflow.
2. Documentas (o configuras) artefacto de reporte de test/coverage opcional.
3. Commit `docs(m15): badge ci y artefacto`.

## Errores comunes

- Badge a repo ajeno.
- Prometer coverage upload sin secretos/config.
- README sin cómo correr tests local.

## Siguiente

[L13 — Checklist de code review](L13-checklist-de-code-review.md)
