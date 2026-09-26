---
id: L06
materia: M07
orden: 6
titulo: Cola (Queue) y cola circular
horas: 5.0
semana: 2
lectura: Colas FIFO; cola circular con buffer fijo
evidencia: Queue<T> + tests; opcional CircularQueue
---

# L06 — Cola (Queue) y cola circular

**~5.0 h · Semana 2**

FIFO alimenta BFS y buffers de trabajo. La cola circular evita desplazamientos en un buffer fijo.

## Objetivo

Implementar `Queue<T>` correcta en costos y una `CircularQueue` de capacidad fija con política de overflow explícita.

## Pasos

### 1. Queue lineal (70 min)

`src/queue.ts`: `enqueue`, `dequeue`, `front`/`peek`, `size`. Preferible lista con head/tail o índices sobre buffer — **no** `shift` silencioso O(n) sin nota.

### 2. Tests FIFO (40 min)

Orden de salida; vacía; un elemento; secuencia enqueue/dequeue intercalada.

### 3. CircularQueue (80 min)

`src/circular-queue.ts`: capacidad N; índices `head`/`tail` módulo N; distingue lleno vs vacío (`size` o slot sentinela). Overflow: throw o return false — elige y documéntalo en JSDoc.

### 4. Tests circulares (40 min)

Llenar hasta capacidad; overflow; vaciar tras wrap-around (enqueue que da la vuelta al buffer).

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): queue y cola circular"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Cola FIFO; buffer circular head/tail | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/queue.ts` con `enqueue`/`dequeue`/`front` y ≥4 tests FIFO.
2. `src/circular-queue.ts` (o sección en el mismo archivo) con capacidad fija y overflow definido.
3. Commit `feat(m07): queue y cola circular`.

## Errores comunes

- Usar `Array.shift` sin documentar O(n) (si lo usas, dilo y prefiere head index o lista).
- Circular: confundir “lleno” y “vacío” sin sentinel o size.
- Tests solo enqueue sin dequeue.

## Siguiente

[L07 — Deque y casos de uso](L07-deque-y-casos-de-uso.md)
