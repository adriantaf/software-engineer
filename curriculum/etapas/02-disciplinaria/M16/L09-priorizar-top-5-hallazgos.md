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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      No puedes arreglar 40 cosas. Hoy eliges cinco con criterio.


      **Objetivo de esta lección:** Backlog priorizado para la iteración.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m16): backlog top 5 hallazgos`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Priorizar top 5 hallazgos», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Priorizar top 5
          hallazgos
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
    pregunta: ¿Es recomendable en esta lección? “Priorizar solo lo fácil de arreglar."
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
        texto: Backlog priorizado para la iteración.
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
    pregunta: ¿Debes hacer esto? “Top 5 sin relación a P1/P2."
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
      - '`backlog-top5.md` con score impacto×frecuencia y dueño (M16 fix vs M17).'
      - Al menos 1 hallazgo de severidad alta en el top.
      - 'Commit `docs(m16): backlog top 5 hallazgos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
