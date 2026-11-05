---
id: L06
materia: M08
orden: 6
titulo: Merge sort y estabilidad
horas: 5
semana: 2
lectura: 'CLRS: divide y vencerás — merge sort'
evidencia: sorts/merge.ts + nota estabilidad
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Merge garantiza Θ(n log n) y puede ser estable si el merge elige bien ante
      empates.


      **Objetivo de esta lección:** Implementar merge sort y demostrar
      estabilidad con un test o ejemplo documentado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): merge sort y estabilidad"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`merge` + `mergeSort`'
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): merge sort y estabilidad"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Merge sort y estabilidad», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Merge sort y
          estabilidad
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

      `git commit -am "feat(m08): merge sort y estabilidad"`
    comandoEsperado:
      - 'git commit -am "feat(m08): merge sort y estabilidad"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): merge sort y estabilidad"'
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
          Implementar merge sort y demostrar estabilidad con un test o ejemplo
          documentado.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Estabilidad
    xp: 10
    cuerpo: >-
      `sorts/estabilidad.md` + test con objetos `{k, id}`: mismos `k` preservan
      orden de `id`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`sorts/merge.ts` con `merge` + `mergeSort`.'
      - >-
        Nota de estabilidad con ejemplo de pares `(key, payload)` en
        `sorts/estabilidad.md`.
      - 'Tests verdes; commit `feat(m08): merge sort y estabilidad`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Merge sort y estabilidad

**~5.0 h · Semana 2**

Merge garantiza Θ(n log n) y puede ser estable si el merge elige bien ante empates.

## Objetivo

Implementar merge sort y demostrar estabilidad con un test o ejemplo documentado.

## Pasos

### 1. Lectura (40 min)

CLRS merge sort + VisuAlgo. Escribe la recurrencia T(n)=2T(n/2)+Θ(n).

### 2. `merge` + `mergeSort` (90 min)

`sorts/merge.ts`. Al comparar iguales, toma primero del buffer izquierdo (estabilidad).

### 3. Estabilidad (50 min)

`sorts/estabilidad.md` + test con objetos `{k, id}`: mismos `k` preservan orden de `id`.

### 4. Tests adicionales (30 min)

Random vs sort nativo; vacío; un elemento.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): merge sort y estabilidad"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Merge sort Θ(n log n); estabilidad al fusionar | [VisuAlgo · Sorting](https://visualgo.net/en/sorting) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `sorts/merge.ts` con `merge` + `mergeSort`.
2. Nota de estabilidad con ejemplo de pares `(key, payload)` en `sorts/estabilidad.md`.
3. Tests verdes; commit `feat(m08): merge sort y estabilidad`.

## Errores comunes

- Merge que pisa el orden relativo de iguales (rompe estabilidad).
- Olvidar costo espacial Θ(n).
- Recursión sin caso base en length ≤ 1.

## Siguiente

[L07 — Quicksort y peor caso](L07-quicksort-y-peor-caso.md)
