---
id: L05
materia: M08
orden: 5
titulo: Insertion sort implementado
horas: 5.0
semana: 2
lectura: "CLRS: insertion sort — invariante del prefijo ordenado"
evidencia: sorts/insertion.ts + tests
---

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
