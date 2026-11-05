---
id: L20
materia: M08
orden: 20
titulo: Patrones DP y transiciones
horas: 5
semana: 5
lectura: Catálogo personal de patrones DP
evidencia: dp/README patrones
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la semana DP dejando un mapa mental reutilizable.


      **Objetivo de esta lección:** Documentar patrones DP ligados a tus tres
      problemas y preparar el salto al proyecto autocomplete.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tabla de patrones
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m08): patrones DP y transiciones"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Relee transiciones
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m08): patrones DP y transiciones"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Patrones DP y transiciones», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Patrones DP y
          transiciones
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git commit -am "docs(m08): patrones DP y transiciones"`
    comandoEsperado:
      - 'git commit -am "docs(m08): patrones DP y transiciones"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "docs(m08): patrones DP y transiciones"'
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Documentar patrones DP ligados a tus tres problemas y preparar el
          salto al proyecto autocomplete.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Flashcards
    xp: 10
    cuerpo: 5 preguntas autoevaluación al final del README (“¿qué es overlapping…?”).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`dp/README.md` con tabla de patrones → problemas tuyos.'
      - Cada problema P3 referenciado; bitácora semana 5 opcional.
      - 'Commit `docs(m08): patrones DP y transiciones`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Patrones DP y transiciones

**~5.0 h · Semana 5**

Cierras la semana DP dejando un mapa mental reutilizable.

## Objetivo

Documentar patrones DP ligados a tus tres problemas y preparar el salto al proyecto autocomplete.

## Pasos

### 1. Tabla de patrones (60 min)

En `dp/README.md`: patrón | estado típico | transición | tu archivo.

### 2. Relee transiciones (50 min)

Corrige cualquier enunciado ambiguo de L19.

### 3. Flashcards (40 min)

5 preguntas autoevaluación al final del README (“¿qué es overlapping…?”).

### 4. Enlace raíz (30 min)

README del proyecto: sección P3 completa.

### 5. Commit (15 min)

```bash
git commit -am "docs(m08): patrones DP y transiciones"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | 1D, knapsack 0/1 intro, paths en grid | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `dp/README.md` con tabla de patrones → problemas tuyos.
2. Cada problema P3 referenciado; bitácora semana 5 opcional.
3. Commit `docs(m08): patrones DP y transiciones`.

## Errores comunes

- Catálogo genérico sin tus rutas.
- Transiciones incorrectas copiadas.
- No enlazar desde README raíz.

## Siguiente

[L21 — Autocomplete: elección de estructura](L21-autocomplete-eleccion-de-estructura.md)
