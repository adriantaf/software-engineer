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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar patrones DP ligados a tus tres problemas y
      preparar el salto al proyecto autocomplete.


      Cierras la semana DP dejando un mapa mental reutilizable.
  - id: s2
    tipo: ejemplo
    titulo: 1. Tabla de patrones
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m08): patrones DP y transiciones"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Patrones DP y transiciones" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: dp/README patrones
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git commit -am "docs(m08): patrones DP y transiciones"`
    comandoEsperado:
      - 'git commit -am "docs(m08): patrones DP y transiciones"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "docs(m08): patrones DP y transiciones"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Documentar patrones DP ligados a tus tres problemas y preparar el
          salto al proyecto autocomplete.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Relee transiciones
    xp: 10
    cuerpo: Corrige cualquier enunciado ambiguo de L19.
  - id: s7
    tipo: explicacion
    titulo: 3. Flashcards
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
