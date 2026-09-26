---
id: L10
materia: M08
orden: 10
titulo: Two pointers en arrays ordenados
horas: 5.0
semana: 3
lectura: Two pointers / left-right en secuencias ordenadas
evidencia: 2 problemas two pointers
---

# L10 — Two pointers en arrays ordenados

**~5.0 h · Semana 3**

Con orden, left/right reemplazan búsquedas anidadas.

## Objetivo

Entregar dos soluciones two-pointers bien testeadas e indexadas.

## Pasos

### 1. Patrón en papel (25 min)

Dibuja pair-sum = target en array ordenado. Anota cuándo mueves left vs right.

### 2. Problema A — pair sum (60 min)

`problems/…-pair-sum/`. Tests: hay par, no hay, duplicados, negativos.

### 3. Problema B (70 min)

Ej. contenedor de agua, squaring sorted array, merge dos ordenados in-place conceptual. Misma plantilla.

### 4. Índice + nota (30 min)

Compara con hash two-sum: trade-off ordenar+O(n) vs hash O(n) promedio.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): two pointers arrays ordenados"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Punteros extremos; pair sum en array ordenado | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Dos problemas two-pointers con arrays ordenados (o justificación de por qué ordenas antes).
2. Complejidad O(n) tras ordenar si aplica — dilo explícito.
3. Commit `feat(m08): two pointers arrays ordenados`.

## Errores comunes

- Two pointers en no ordenado sin ordenar ni justificar.
- Índices que se cruzan mal (loop infinito).
- No cubrir caso sin solución.

## Siguiente

[L11 — Sliding window](L11-sliding-window.md)
