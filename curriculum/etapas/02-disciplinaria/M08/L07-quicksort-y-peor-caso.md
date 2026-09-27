---
id: L07
materia: M08
orden: 7
titulo: Quicksort y peor caso
horas: 5.0
semana: 2
lectura: "CLRS: quicksort — partición y peor caso"
evidencia: sorts/quick.ts + caso O(n²)
---

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
