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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Cierre evidenciable y handoff a M17/M18.


      Proyecto: pipeline verde + coverage de negocio + hábitos de
      review/regresión.
  - id: s2
    tipo: ejemplo
    titulo: 1. Verifica CI localmente
    xp: 10
    cuerpo: lint + test + audit.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M15 — pipeline, coverage dominio, dominio" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: README final P1–P3 + autoevaluación
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
    pregunta: ¿Es buena práctica en esta lección? “CI roto en main."
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
        texto: Cierre evidenciable y handoff a M17/M18.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 4. Commit
    xp: 10
    cuerpo: '`docs(m15): cierre pipeline y criterios de dominio`'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'README documenta P1 pirámide, P2 CI, P3 checklist con rutas.'
      - 'Autoevaluación: 401/403 automatizados; coverage enfocado a dominio.'
      - 'Commit `docs(m15): cierre pipeline y criterios de dominio`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
