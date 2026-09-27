---
id: L19
materia: M07
orden: 19
titulo: Cola de prioridad
horas: 5.0
semana: 5
lectura: Priority queue sobre heap; API de tareas
evidencia: PriorityQueue API + 3 casos
---

# L19 — Cola de prioridad

**~5.0 h · Semana 5**

La PQ es la fachada del heap para el dominio (turnos, jobs, eventos).

## Objetivo

Envolver el MinHeap en `PriorityQueue<T>` con tres casos de uso testeados.

## Pasos

### 1. API (30 min)

```ts
enqueue(item: T, priority: number): void
dequeue(): T
peek(): T
```

Menor `priority` sale primero (documenta si inviertes).

### 2. Implementación (70 min)

Guarda `{ item, priority }` en el heap; compara por priority (tie-break opcional por orden de llegada).

### 3. Tres casos (70 min)

Tests: (1) turnos `{cliente, prioridad}`; (2) vaciar cola; (3) mismas prioridades — orden estable o documentado.

### 4. Nota de producto (30 min)

En README: cómo Agenda Ops usaría PQ para “siguiente en cola VIP”.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): priority queue"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | PQ: enqueue con prioridad, dequeue del mínimo/máximo | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/priority-queue.ts` genérica (prioridad numérica o comparator).
2. Tres casos de prueba de dominio (p. ej. turnos Agenda Ops: urgente < normal).
3. Commit `feat(m07): priority queue`.

## Errores comunes

- PQ que es solo un array sorted en cada insert sin decir O(n).
- Prioridades invertidas sin documentar (min vs max).
- Casos de prueba sin prioridades distintas.

## Siguiente

[L20 — Heap vs BST para prioridades](L20-heap-vs-bst-para-prioridades.md)
