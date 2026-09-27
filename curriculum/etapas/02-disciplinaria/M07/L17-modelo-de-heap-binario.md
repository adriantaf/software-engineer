---
id: L17
materia: M07
orden: 17
titulo: Modelo de heap binario
horas: 5.0
semana: 5
lectura: "Heap binario como array: índices padre/hijos"
evidencia: array-backed heap model + heapifyUp/Down
---

# L17 — Modelo de heap binario

**~5.0 h · Semana 5**

El heap vive en un array: padre en `(i-1)>>1`, hijos `2i+1` y `2i+2`.

## Objetivo

Codificar el modelo (índices + heapify up/down) antes de la API insert/extractMin.

## Pasos

### 1. VisuAlgo + notas (40 min)

Observa un min-heap. En `docs/heap.md` escribe la propiedad de heap y la forma completa de niveles.

### 2. Helpers (50 min)

`src/heap-model.ts`:

```ts
export const parent = (i: number) => (i - 1) >> 1
export const left = (i: number) => 2 * i + 1
export const right = (i: number) => 2 * i + 2
```

Tests de índices 0..10.

### 3. heapifyUp / heapifyDown (90 min)

Funciones que mutan `number[]` asumiendo min-heap. Casos de prueba: subir una hoja menor que el padre; bajar una raíz mayor que un hijo.

### 4. Diagrama array↔árbol (30 min)

En `docs/heap.md`, tabla índice→valor para un heap de ejemplo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): modelo heap binario"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Heap shape + heap property; índices 2i+1 / 2i+2 | [VisuAlgo · Heap](https://visualgo.net/en/heap) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Módulo con helpers `parent`/`left`/`right` y `heapifyUp`/`heapifyDown` sobre array.
2. Tests unitarios de índices y de un heapify sobre array casi-heap.
3. Commit `feat(m07): modelo heap binario`.

## Errores comunes

- Confundir índices 0-based y 1-based.
- Heapify que no restaura la propiedad.
- Tratar el heap como BST ordenado inorder.

## Siguiente

[L18 — Heap mínimo: insert y extractMin](L18-heap-minimo-insert-y-extractmin.md)
