---
id: L11
materia: M16
orden: 11
titulo: Informe de usabilidad para stakeholders
horas: 5
semana: 3
lectura: Informe ejecutivo; riesgos UX→seguridad
evidencia: informe-usabilidad.md (proyecto)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `informe-usabilidad.md` completo.

      El proyecto de M16 es el informe que el design partner entiende.
  - id: s2
    tipo: ejemplo
    titulo: 2. Cuerpo
    xp: 10
    cuerpo: >-
      Método, participantes (anónimos), tareas, hallazgos, iteración, backlog
      residual.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Informe de usabilidad para stakeholders" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: informe-usabilidad.md (proyecto)
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
    pregunta: ¿Es buena práctica en esta lección? “Informe solo técnico para ti."
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
        texto: '`informe-usabilidad.md` completo.'
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
    cuerpo: '`docs(m16): informe de usabilidad`'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `informe-usabilidad.md` con resumen ejecutivo (1 pág), método, top
        hallazgos, cambios hechos/planificados.
      - Sección de riesgos UX que pueden virar a bugs de seguridad.
      - 'Commit `docs(m16): informe de usabilidad`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — Informe de usabilidad para stakeholders

**~5.0 h · Semana 3**

El proyecto de M16 es el informe que el design partner entiende.

## Objetivo

`informe-usabilidad.md` completo.

## Pasos (hazlos en orden)

### 1. Resumen ejecutivo (40 min)

### 2. Cuerpo (80–100 min)

Método, participantes (anónimos), tareas, hallazgos, iteración, backlog residual.

### 3. Riesgos seguridad UX (30 min)

### 4. Commit

`docs(m16): informe de usabilidad`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Informe para design partner: método, hallazgos, cambios | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. `informe-usabilidad.md` con resumen ejecutivo (1 pág), método, top hallazgos, cambios hechos/planificados.
2. Sección de riesgos UX que pueden virar a bugs de seguridad.
3. Commit `docs(m16): informe de usabilidad`.

## Errores comunes

- Informe solo técnico para ti.
- Sin prioridades.
- Ocultar hallazgos incómodos.

## Siguiente

[L12 — Cierre M16 — handoff M17 y criterios dominio](L12-cierre-m16-handoff-m17-y-criterios-dominio.md)
