---
id: L06
materia: M16
orden: 6
titulo: Guion de test de usabilidad 15–30 min
horas: 5
semana: 2
lectura: 'Krug: test de pasillo; consentimiento básico'
evidencia: guion-usabilidad.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `guion-usabilidad.md` listo para leer en voz alta.

      El guion evita sesiones anécdota. Hoy lo escribes antes de citar gente.
  - id: s2
    tipo: ejemplo
    titulo: 1. Estructura
    xp: 10
    cuerpo: |-
      Contexto → consentimiento → tareas (del L05) → debrief.

      Usa el extracto de la ficha M16 como base y adáptalo a tu sub-vertical.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Guion de test de usabilidad 15–30 min" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: guion-usabilidad.md
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
      ¿Es buena práctica en esta lección? “Guion que defiende el diseño (“es
      fácil ¿verdad?”)."
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
        texto: '`guion-usabilidad.md` listo para leer en voz alta.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Criterios de éxito por tarea
    xp: 10
    cuerpo: 'Observable: “creó la pedido sin ayuda del facilitador”.'
  - id: s7
    tipo: explicacion
    titulo: 4. Commit
    xp: 10
    cuerpo: '`docs(m16): guion de usabilidad`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`guion-usabilidad.md` con intro, tareas, preguntas de cierre y tiempo.'
      - Incluye consentimiento básico y anonimización de notas.
      - 'Commit `docs(m16): guion de usabilidad`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Guion de test de usabilidad 15–30 min

**~5.0 h · Semana 2**

El guion evita sesiones anécdota. Hoy lo escribes antes de citar gente.

## Objetivo

`guion-usabilidad.md` listo para leer en voz alta.

## Pasos (hazlos en orden)

### 1. Estructura (60–70 min)

Contexto → consentimiento → tareas (del L05) → debrief.

Usa el extracto de la ficha M16 como base y adáptalo a tu sub-vertical.

### 2. Criterios de éxito por tarea (40 min)

Observable: “creó la pedido sin ayuda del facilitador”.

### 3. Piloto contigo mismo (30 min) — cronometra

### 4. Commit

`docs(m16): guion de usabilidad`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Guion 15–30 min + consentimiento y think-aloud | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. `guion-usabilidad.md` con intro, tareas, preguntas de cierre y tiempo.
2. Incluye consentimiento básico y anonimización de notas.
3. Commit `docs(m16): guion de usabilidad`.

## Errores comunes

- Guion que defiende el diseño (“es fácil ¿verdad?”).
- Sesiones de 2 horas.
- Sin espacio para think-aloud.

## Siguiente

[L07 — Sesiones 1–3 — notas de participantes](L07-sesiones-1-3-notas-de-participantes.md)
