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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar insertion sort, analizarlo y dejar tests que
      cubran mejor y peor caso.


      Insertion es el sort didáctico: invariante “a[0..i) ordenado” y base de la
      semana P2.
  - id: s2
    tipo: ejemplo
    titulo: 1. VisuAlgo
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/sorts
      git commit -m "feat(m08): insertion sort"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Insertion sort implementado" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: sorts/insertion.ts + tests
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

      `git add projects/m08-algoritmos/sorts`
    comandoEsperado:
      - git add projects/m08-algoritmos/sorts
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m08-algoritmos/sorts'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar insertion sort, analizarlo y dejar tests que cubran mejor
          y peor caso.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: >-
      `sorts/insertion.ts` — `export function insertionSort(a: number[]):
      number[]` (mutando o devolviendo copia; dilo en JSDoc).
  - id: s7
    tipo: explicacion
    titulo: 3. Análisis
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
