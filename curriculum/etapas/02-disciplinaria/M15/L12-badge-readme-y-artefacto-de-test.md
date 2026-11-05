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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** README con señal de CI + instrucciones locales.

      Si el pipeline no se ve, no existe para el equipo-de-uno futuro.
  - id: s2
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: '`docs(m15): badge ci y artefacto`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Badge README y artefacto de test" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: README con badge/enlace CI + nota de artefacto
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
    pregunta: ¿Es buena práctica en esta lección? “Badge a repo ajeno."
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
        texto: README con señal de CI + instrucciones locales.
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
      - README M15 muestra badge o enlace claro al workflow.
      - >-
        Documentas (o configuras) artefacto de reporte de test/coverage
        opcional.
      - 'Commit `docs(m15): badge ci y artefacto`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
