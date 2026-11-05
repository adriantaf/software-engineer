---
id: L05
materia: M08
orden: 5
titulo: Insertion sort implementado
horas: 5
semana: 2
lectura: 'CLRS: insertion sort — invariante del prefijo ordenado'
evidencia: sorts/insertion.ts + tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Insertion es el sort didáctico: invariante “a[0..i) ordenado” y base de la
      semana P2.


      **Objetivo de esta lección:** Implementar insertion sort, analizarlo y
      dejar tests que cubran mejor y peor caso.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: VisuAlgo
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/sorts
      git commit -m "feat(m08): insertion sort"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/sorts
      git commit -m "feat(m08): insertion sort"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Insertion sort implementado», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Insertion sort
          implementado
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

      `git add projects/m08-algoritmos/sorts`
    comandoEsperado:
      - git add projects/m08-algoritmos/sorts
      - 'git commit -m "feat(m08): insertion sort"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m08-algoritmos/sorts'
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
          Implementar insertion sort, analizarlo y dejar tests que cubran mejor
          y peor caso.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Análisis
    xp: 10
    cuerpo: >-
      `sorts/insertion-analisis.md`: peor Θ(n²), mejor Θ(n), espacial,
      estabilidad = sí.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `sorts/insertion.ts` ordena números (o genérico comparable) in-place o
        documentando copia.
      - 'Tests: vacío, uno, invertido, ya ordenado, duplicados.'
      - >-
        `sorts/insertion-analisis.md` con peor/mejor caso; commit `feat(m08):
        insertion sort`.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L05 — Insertion sort implementado

**~5.0 h · Semana 2**

Insertion es el sort didáctico: invariante “a[0..i) ordenado” y base de la semana P2.

## Objetivo

Implementar insertion sort, analizarlo y dejar tests que cubran mejor y peor caso.

## Pasos

### 1. VisuAlgo (20 min)

Modo insertion; anota cuántas escrituras ves en un array invertido vs casi ordenado.

### 2. Implementación (70 min)

`sorts/insertion.ts` — `export function insertionSort(a: number[]): number[]` (mutando o devolviendo copia; dilo en JSDoc).

### 3. Análisis (40 min)

`sorts/insertion-analisis.md`: peor Θ(n²), mejor Θ(n), espacial, estabilidad = sí.

### 4. Tests (50 min)

Incluye array de 100 elementos random vs `[...a].sort((x,y)=>x-y)`.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/sorts
git commit -m "feat(m08): insertion sort"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Insertion sort: Θ(n²) peor / Θ(n) casi ordenado | [VisuAlgo · Sorting](https://visualgo.net/en/sorting) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `sorts/insertion.ts` ordena números (o genérico comparable) in-place o documentando copia.
2. Tests: vacío, uno, invertido, ya ordenado, duplicados.
3. `sorts/insertion-analisis.md` con peor/mejor caso; commit `feat(m08): insertion sort`.

## Errores comunes

- Llamar a `Array.sort` y presentarlo como insertion.
- No probar el caso ya ordenado (mejor caso).
- Olvidar estabilidad (aunque insertion es estable — menciónalo).

## Siguiente

[L06 — Merge sort y estabilidad](L06-merge-sort-y-estabilidad.md)
