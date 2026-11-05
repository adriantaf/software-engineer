---
id: L07
materia: M08
orden: 7
titulo: Quicksort y peor caso
horas: 5
semana: 2
lectura: 'CLRS: quicksort — partición y peor caso'
evidencia: sorts/quick.ts + caso O(n²)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Quicksort brilla en promedio y falla con pivotes ingenuos en datos
      ordenados.


      **Objetivo de esta lección:** Implementar quicksort, documentar el peor
      caso O(n²) y una mitigación concreta.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Partición
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): quicksort y peor caso"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Peor caso escrito
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): quicksort y peor caso"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Quicksort y peor caso», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Quicksort y peor caso
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

      `git commit -am "feat(m08): quicksort y peor caso"`
    comandoEsperado:
      - 'git commit -am "feat(m08): quicksort y peor caso"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): quicksort y peor caso"'
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
          Implementar quicksort, documentar el peor caso O(n²) y una mitigación
          concreta.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Mitigación
    xp: 10
    cuerpo: Implementa pivote aleatorio **o** median-of-three. Nota en el markdown.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`sorts/quick.ts` con partición documentada.'
      - >-
        `sorts/quick-peor-caso.md` explica entrada adversaria (ya ordenado +
        pivote fijo) y mitigación (pivote random/median-of-three).
      - 'Tests + commit `feat(m08): quicksort y peor caso`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Quicksort y peor caso

**~5.0 h · Semana 2**

Quicksort brilla en promedio y falla con pivotes ingenuos en datos ordenados.

## Objetivo

Implementar quicksort, documentar el peor caso O(n²) y una mitigación concreta.

## Pasos

### 1. Partición (70 min)

`sorts/quick.ts`: Lomuto o Hoare — elige una y comenta invariante.

### 2. Peor caso escrito (50 min)

`sorts/quick-peor-caso.md`: secuencia que degenera con pivote `a[hi]`; contador de comparaciones opcional en modo debug.

### 3. Mitigación (50 min)

Implementa pivote aleatorio **o** median-of-three. Nota en el markdown.

### 4. Tests (40 min)

Ordenado, invertido, duplicados, random vs nativo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): quicksort y peor caso"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Quicksort promedio vs peor caso n²; pivotes | [VisuAlgo · Sorting](https://visualgo.net/en/sorting) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `sorts/quick.ts` con partición documentada.
2. `sorts/quick-peor-caso.md` explica entrada adversaria (ya ordenado + pivote fijo) y mitigación (pivote random/median-of-three).
3. Tests + commit `feat(m08): quicksort y peor caso`.

## Errores comunes

- Afirmar “quicksort es O(n log n)” sin matizar peor caso.
- Partición incorrecta (loops infinitos).
- Sin test de array con muchos duplicados.

## Siguiente

[L08 — Tabla P2 sorts en README](L08-tabla-p2-sorts-en-readme.md)
