---
id: L03
materia: M07
orden: 3
titulo: Lista doble y operaciones indexadas
horas: 5.0
semana: 1
lectura: "Listas dobles: prev/next, borrado e indexación lineal"
evidencia: DoublyLinkedList + deleteByValue; tests de borde
---

# L03 — Lista doble y operaciones indexadas

**~5.0 h · Semana 1**

Con `prev` y `next` el borrado deja de ser un recorrido ciego desde `head` si ya tienes el nodo.

## Objetivo

Implementar `DoublyLinkedList<T>` con borrado por valor y acceso indexado lineal (`at(i)`), documentando que el índice **no** es O(1).

## Pasos

### 1. Lectura + sketch (40 min)

Capítulo de listas dobles. Dibuja borrado de nodo intermedio (4 punteros).

### 2. Implementación (90 min)

`src/doubly-linked-list.ts`: nodos con `prev`/`next`; `append`; `deleteByValue(v)` (o `delete(node)`); `at(i)` que recorre desde head (o desde el extremo más cercano si quieres bonus).

### 3. Tests de borde (60 min)

Borrar de lista vacía; borrar único nodo (head=tail=null); borrar cabeza; borrar cola; `at(-1)` / fuera de rango.

### 4. Documenta indexación (30 min)

En `COMPLEJIDAD.md`: `at(i)` es O(n). Una frase: “si necesitas índice frecuente, usa array”.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): lista doble e indexada"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Listas doblemente enlazadas; borrado O(1) con nodo conocido | [VisuAlgo · Linked List](https://visualgo.net/en/list) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/doubly-linked-list.ts` con `append`, `deleteByValue` (o por nodo) y `at(i)` documentado O(n).
2. ≥5 tests: vacío, un nodo, borrar cabeza/cola/medio, índice inválido.
3. Commit `feat(m07): lista doble e indexada`.

## Errores comunes

- Olvidar actualizar `prev` al borrar.
- Prometer acceso O(1) por índice en lista enlazada.
- Dejar `tail` huérfano tras borrar el último.

## Siguiente

[L04 — Secuencias: repaso de costos y cierre semana 1](L04-secuencias-repaso-de-costos-y-cierre-semana-1.md)
