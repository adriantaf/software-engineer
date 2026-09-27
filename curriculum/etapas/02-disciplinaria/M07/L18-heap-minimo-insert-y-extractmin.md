---
id: L18
materia: M07
orden: 18
titulo: "Heap mínimo: insert y extractMin"
horas: 5.0
semana: 5
lectura: Operaciones insert y extract-min en heap
evidencia: MinHeap operativo + tests
---

# L18 — Heap mínimo: insert y extractMin

**~5.0 h · Semana 5**

Con el modelo listo, montas la estructura usable.

## Objetivo

Entregar `MinHeap` completo con insert/extractMin/peek y tests de orden.

## Pasos

### 1. Clase MinHeap (90 min)

`src/min-heap.ts` usa `heap-model.ts`. `insert`: push + heapifyUp. `extractMin`: swap root/último, pop, heapifyDown.

### 2. Tests (70 min)

Insertar `{5,3,8,1}` → extract 1,3,5,8; peek no muta; extract vacío; 100 random vs `[...].sort((a,b)=>a-b)`.

### 3. Complejidad (30 min)

Filas en `COMPLEJIDAD.md` para heap.

### 4. Export (20 min)

Reexporta desde `src/index.ts`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): minheap insert extractMin"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | insert O(log n); extractMin O(log n); peek O(1) | [VisuAlgo · Heap](https://visualgo.net/en/heap) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/min-heap.ts` con `insert`, `extractMin`, `peek`, `size`.
2. ≥5 tests: orden de extracción, vacío, un elemento, secuencia aleatoria vs sort.
3. Commit `feat(m07): minheap insert extractMin`.

## Errores comunes

- extractMin sin heapifyDown.
- Insert solo con `push` al array sin subir.
- Tests que no verifican orden de salida.

## Siguiente

[L19 — Cola de prioridad](L19-cola-de-prioridad.md)
