---
id: L13
materia: M07
orden: 13
titulo: "BST: inserción y búsqueda"
horas: 5.0
semana: 4
lectura: "Árboles binarios de búsqueda: invariante e insert/contains"
evidencia: BST insert/contains + tests ordenados
---

# L13 — BST: inserción y búsqueda

**~5.0 h · Semana 4**

P2 empieza con el invariante: izquierda < nodo < derecha.

## Objetivo

Implementar un BST de números (o `T` comparable) con `insert` y `contains`, más tests que demuestren el orden.

## Pasos

### 1. Lectura + VisuAlgo (40 min)

Inserta la secuencia 8,3,10,1,6 en VisuAlgo BST. Copia el dibujo a `docs/bst-semana4.md`.

### 2. Nodos e insert (90 min)

`src/bst.ts`:

```ts
class BstNode { left: BstNode | null; right: BstNode | null; constructor(public key: number) {} }
export class BST { insert(key: number): void; contains(key: number): boolean }
```

Define política de duplicados en un comentario de una línea.

### 3. Tests (60 min)

Vacío contains false; insert uno; secuencia 8,3,10,1,6 contains todos; ausente; duplicado según política.

### 4. Complejidad (20 min)

`COMPLEJIDAD.md`: O(h) con h altura; peor caso cadena O(n).

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst insert y contains"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | BST: hijo izq < nodo < der; insert y search | [VisuAlgo · BST](https://visualgo.net/en/bst) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/bst.ts` con `insert` y `contains` respetando invariante BST.
2. ≥5 tests (vacío, cadena ordenada, duplicado definido, contains true/false).
3. Commit `feat(m07): bst insert y contains`.

## Errores comunes

- Insertar sin respetar orden (rompe invariante).
- Duplicados silenciosos sin política (ignorar / contar / throw).
- Confundir BST con heap.

## Siguiente

[L14 — Recorridos inorder, preorder, postorder](L14-recorridos-inorder-preorder-postorder.md)
