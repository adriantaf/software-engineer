---
id: L01
materia: M08
orden: 1
titulo: Entorno y binary search con invariante
horas: 5
semana: 1
lectura: 'Búsqueda binaria e invariante del intervalo [lo, hi]'
evidencia: binary-search.ts + analisis + 2 problemas arrays
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M08 exige carpetas de evidencia y el hábito: invariante → código →
      complejidad → tests.


      **Objetivo de esta lección:** Levantar `projects/m08-algoritmos/`,
      implementar binary search con invariante documentado y dejar dos problemas
      de arrays.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Scaffold
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p
      projects/m08-algoritmos/{src,problems,sorts,dp,autocomplete,docs,tests}

      cd projects/m08-algoritmos

      cat README.md

      ```


      Si no hay toolchain: Script `"test": "vitest run"`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Binary search
    xp: 10
    cuerpo: >-
      ```ts

      /** Invariante: si t está en a, está en a[lo..hi] inclusive. */

      export function binarySearch(a: number[], t: number): number

      ```


      `src/binary-search.ts`: Define convención con duplicados (p. ej. cualquier
      índice, o el primero).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Entorno y binary search con invariante», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Entorno y binary search
          con invariante
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `mkdir -p
      projects/m08-algoritmos/{src,problems,sorts,dp,autocomplete,docs,tests}`
    comandoEsperado:
      - >-
        mkdir -p
        projects/m08-algoritmos/{src,problems,sorts,dp,autocomplete,docs,tests}
      - cd projects/m08-algoritmos
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: mkdir -p
      projects/m08-algoritmos/{src,problems,sorts,dp,autocomplete,docs,tests}
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
          Levantar `projects/m08-algoritmos/`, implementar binary search con
          invariante documentado y dejar dos problemas de arrays.
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
      `docs/binary-search-analisis.md`: invariante, por qué O(log n), qué pasa
      si el array no está ordenado.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m08-algoritmos/` con carpetas `problems/`, `sorts/`, `dp/`,
        `autocomplete/` y Vitest configurado.
      - >-
        `src/binary-search.ts` + `docs/binary-search-analisis.md` con
        invariante; ≥4 tests.
      - >-
        Dos problemas en `problems/` (enunciado + complejidad + 3 tests c/u);
        commit `feat(m08): binary search y 2 problemas arrays`.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Entorno y binary search con invariante

**~5.0 h · Semana 1**

M08 exige carpetas de evidencia y el hábito: invariante → código → complejidad → tests.

## Objetivo

Levantar `projects/m08-algoritmos/`, implementar binary search con invariante documentado y dejar dos problemas de arrays.

## Pasos (hazlos en orden)

### 1. Scaffold (25 min)

```bash
mkdir -p projects/m08-algoritmos/{src,problems,sorts,dp,autocomplete,docs,tests}
cd projects/m08-algoritmos
cat README.md
```

Si no hay toolchain:

```bash
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init --strict --rootDir src --outDir dist --module nodenext --moduleResolution nodenext --target ES2022
```

Script `"test": "vitest run"`.

### 2. Binary search (75 min)

`src/binary-search.ts`:

```ts
/** Invariante: si t está en a, está en a[lo..hi] inclusive. */
export function binarySearch(a: number[], t: number): number
```

Define convención con duplicados (p. ej. cualquier índice, o el primero).

### 3. Análisis (35 min)

`docs/binary-search-analisis.md`: invariante, por qué O(log n), qué pasa si el array no está ordenado.

### 4. Tests + 2 problemas (90 min)

Tests: vacío, uno, ausente, presente, duplicados.

Luego `problems/01-two-sum/` y `problems/02-max-subarray/` (o nombres claros): cada uno con `enunciado.md`, `solution.ts`, `solution.test.ts` (3 casos), línea de complejidad en el enunciado. 30–45 min atascado antes de mirar pistas.

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): binary search y 2 problemas arrays"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Búsqueda binaria: invariante y O(log n) | [VisuAlgo · Binary Search](https://visualgo.net/en/binsearch) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m08-algoritmos/` con carpetas `problems/`, `sorts/`, `dp/`, `autocomplete/` y Vitest configurado.
2. `src/binary-search.ts` + `docs/binary-search-analisis.md` con invariante; ≥4 tests.
3. Dos problemas en `problems/` (enunciado + complejidad + 3 tests c/u); commit `feat(m08): binary search y 2 problemas arrays`.

## Errores comunes

- Binary search sin invariante escrito.
- Off-by-one en `hi = mid` vs `hi = mid-1`.
- Problemas sin complejidad ni casos borde.

## Siguiente

[L02 — Notación asintótica Θ, O y Ω](L02-notacion-asintotica-o-y.md)
