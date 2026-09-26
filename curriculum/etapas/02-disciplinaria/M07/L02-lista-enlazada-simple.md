---
id: L02
materia: M07
orden: 2
titulo: Lista enlazada simple
horas: 5.0
semana: 1
lectura: "Joyanes / texto univ. ED (ed. ES): Arrays y listas enlazadas (costos, operaciones) — ED: listas enlazadas singulares, punteros head/tail"
evidencia: "SinglyLinkedList con insert head/tail, find, 5 tests"
---

# L02 — Lista enlazada simple

**~5.0 h · Semana 1**

Pasas de índices contiguos a nodos enlazados: trade-off memoria vs inserción en cabeza.

## Objetivo

Implementar lista simple con `append`, `prepend`, búsqueda lineal y comparar con `DynamicArray` en `COMPLEJIDAD.md`.

## Pasos

### 1. Nodo y API (60 min)

```ts
class Node<T> { constructor(public value: T, public next?: Node<T>) {} }
```

Métodos mínimos: `prepend`, `append`, `find`, `toArray()` para tests.

### 2. Tests (75 min)

Lista vacía, prepend múltiple, append mantiene orden, find ausente, toArray coherente.

### 3. Comparación escrita (45 min)

Añade fila a `COMPLEJIDAD.md`: inserción O(1) en cabeza vs O(n) en array sin espacio extra.

### 4. Lectura (60 min)

Capítulo listas enlazadas. Dibuja 3 operaciones en papel antes de codificar.

### 5. Commit (30 min)

`feat(m07): lista enlazada simple`.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Semana 1: Arrays y listas enlazadas (costos, operaciones) — ED: listas enlazadas singulares, punteros head/tail | [MDN Map/Set (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

1. Lista simple con tests verdes.
2. Comparación array vs lista documentada.
3. Commit atómico.

## Errores comunes

- Perder referencia a `head` al prepend.
- `append` O(n²) por recorrer desde head cada vez sin `tail` (aceptable si lo documentas; mejor guardar tail).
## Siguiente

[L03 — Lista doble y operaciones indexadas](L03-lista-doble-y-operaciones-indexadas.md)
