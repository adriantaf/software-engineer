---
id: L09
materia: M16
orden: 9
titulo: Priorizar top 5 hallazgos
horas: 5
semana: 3
lectura: Impacto × frecuencia; backlog UX
evidencia: iteracion/backlog-top5.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Backlog priorizado para la iteración.

      No puedes arreglar 40 cosas. Hoy eliges cinco con criterio.
  - id: s2
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: '`docs(m16): backlog top 5 hallazgos`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Priorizar top 5 hallazgos" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: iteracion/backlog-top5.md
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
    pregunta: ¿Es buena práctica en esta lección? “Priorizar solo lo fácil de arreglar."
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
        texto: Backlog priorizado para la iteración.
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
      - '`backlog-top5.md` con score impacto×frecuencia y dueño (M16 fix vs M17).'
      - Al menos 1 hallazgo de severidad alta en el top.
      - 'Commit `docs(m16): backlog top 5 hallazgos`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Priorizar top 5 hallazgos

**~5.0 h · Semana 3**

No puedes arreglar 40 cosas. Hoy eliges cinco con criterio.

## Objetivo

Backlog priorizado para la iteración.

## Pasos (hazlos en orden)

### 1. Scoring (50–60 min)

### 2. Define “hecho” por ítem (40 min)

### 3. Commit

`docs(m16): backlog top 5 hallazgos`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Priorizar top 5 para iterar en M16/M17 | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. `backlog-top5.md` con score impacto×frecuencia y dueño (M16 fix vs M17).
2. Al menos 1 hallazgo de severidad alta en el top.
3. Commit `docs(m16): backlog top 5 hallazgos`.

## Errores comunes

- Priorizar solo lo fácil de arreglar.
- Top 5 sin relación a P1/P2.
- Mezclar bugs de backend sin etiquetar.

## Siguiente

[L10 — Iteración UI — antes y después](L10-iteracion-ui-antes-y-despues.md)
