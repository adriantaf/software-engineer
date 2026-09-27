---
id: L20
materia: M07
orden: 20
titulo: Heap vs BST para prioridades
horas: 5.0
semana: 5
lectura: Trade-offs heap vs BST para colas de prioridad
evidencia: COMPLEJIDAD heap vs BST
---

# L20 — Heap vs BST para prioridades

**~5.0 h · Semana 5**

No todo “ordenado” necesita un árbol. Hoy eliges con tabla, no con intuición.

## Objetivo

Documentar trade-offs heap vs BST para prioridades y dejar una decisión escrita de diseño.

## Pasos

### 1. Tabla de operaciones (60 min)

Filas: insert, find-min, extract-min, delete arbitrario, sorted iterate. Columnas: MinHeap, BST, `Map`+sort (referencia).

### 2. Experimento mental / microbench (70 min)

Inserta N=10_000 prioridades y extrae N/2. Compara tu heap vs extraer min de un BST (si tienes min). Anota tiempos en la doc.

### 3. Decisión (40 min)

`docs/heap-vs-bst.md`: párrafo “En Agenda Ops para cola VIP usaría ___ porque ___”.

### 4. Bitácora (30 min)

`bitacora/semana-05.md`.

### 5. Commit (15 min)

```bash
git commit -am "docs(m07): heap vs bst prioridades"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Heap: mejor extract-min; BST: ordered scan / delete arbitrario | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Sección en `COMPLEJIDAD.md` o `docs/heap-vs-bst.md` con tabla de ops.
2. Bitácora semana 5 con una decisión (“para scheduler usaría…”).
3. Commit `docs(m07): heap vs bst prioridades`.

## Errores comunes

- Decir que BST siempre es O(log n) sin hablar del peor caso degenerado.
- Afirmar que heap permite search arbitrario O(log n).
- Tabla sin ops concretas (insert/extract/search).

## Siguiente

[L21 — Grafos: repaso y representación](L21-grafos-repaso-y-representacion.md)
