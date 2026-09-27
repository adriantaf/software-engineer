---
id: L06
materia: M08
orden: 6
titulo: Merge sort y estabilidad
horas: 5.0
semana: 2
lectura: "CLRS: divide y vencerás — merge sort"
evidencia: sorts/merge.ts + nota estabilidad
---

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
