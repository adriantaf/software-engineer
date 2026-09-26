---
id: L02
materia: M07
orden: 2
titulo: Lista enlazada simple
horas: 5.0
semana: 1
lectura: "Listas enlazadas singulares: head/tail, inserción y búsqueda"
evidencia: SinglyLinkedList con insert head/tail, find, 5 tests
---

# L02 — Lista enlazada simple

**~5.0 h · Semana 1**

Pasas de índices contiguos a nodos enlazados: trade-off memoria vs inserción en cabeza.

## Objetivo

Implementar `SinglyLinkedList<T>` con `prepend`/`append`/`find` y contrastar costos con `DynamicArray` en `COMPLEJIDAD.md`.

## Pasos

### 1. Dibuja antes de codificar (20 min)

En papel o Mermaid: lista vacía → prepend A → append B → find C (ausente). Anota qué punteros cambian.

### 2. Nodo y API (70–80 min)

`src/singly-linked-list.ts`:

```ts
class Node<T> {
  constructor(public value: T, public next: Node<T> | null = null) {}
}
```

Métodos: `prepend`, `append` (guarda `tail` si puedes), `find`, `get size`, `toArray()`.

### 3. Cinco tests (60 min)

Vacía; prepend múltiple (orden LIFO en cabeza); append mantiene orden; `find` ausente; `toArray` coherente tras mezcla prepend/append.

```bash
cd projects/m07-estructuras && npm test
```

### 4. Comparación escrita (40 min)

Añade fila a `COMPLEJIDAD.md`: inserción O(1) en cabeza vs O(n) mover elementos en array; búsqueda O(n) en ambos.

### 5. Commit (15 min)

```bash
git add projects/m07-estructuras
git commit -m "feat(m07): lista enlazada simple"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Listas simples: nodos, head/tail, costos de insert/find | [VisuAlgo · Linked List](https://visualgo.net/en/list) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/singly-linked-list.ts` con `prepend`, `append`, `find`, `toArray` y ≥5 tests verdes.
2. `COMPLEJIDAD.md` compara inserción en cabeza lista vs array.
3. Commit `feat(m07): lista enlazada simple`.

## Errores comunes

- Perder la referencia a `head` al hacer `prepend`.
- `append` O(n²) sin `tail` y sin documentarlo.
- Tests que solo insertan y nunca buscan.

## Siguiente

[L03 — Lista doble y operaciones indexadas](L03-lista-doble-y-operaciones-indexadas.md)
