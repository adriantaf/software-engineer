---
id: L06
materia: M07
orden: 6
titulo: Cola (Queue) y cola circular
horas: 5.0
semana: 2
lectura: "Joyanes / texto univ. ED (ed. ES): Pilas y colas (y variantes) — ED: colas FIFO; cola circular para evitar desplazamientos"
evidencia: "Queue<T> + tests; opcional CircularQueue"
---

# L06 — Cola (Queue) y cola circular

**~5.0 h · Semana 2**

FIFO es el buffer de BFS y de trabajos; la cola circular evita O(n) por shift ingenuo.

## Objetivo

Implementar cola eficiente (circular o lista con tail) con dequeue O(1) amortizado.

## Pasos

### 1. Cola base (90 min)

`enqueue`, `dequeue`, `front`. Evita `array.shift()` en hot path sin documentar O(n).

### 2. Circular (opcional 60 min)

Arreglo fijo + índices head/tail; test de wrap-around.

### 3. Tests (75 min)

FIFO, cola vacía, llenar circular y reusar espacio.

### 4. Lectura (45 min)

Capítulo colas.

### 5. Commit (30 min)

`feat(m07): queue y cola circular`.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Semana 2: Pilas y colas (y variantes) — ED: colas FIFO; cola circular para evitar desplazamientos | [MDN Map/Set (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

1. Cola con dequeue O(1) documentado.
2. Tests FIFO y bordes.
3. Commit.

## Errores comunes

- Usar shift en array grande sin medir.
- Confundir tail de lista con cola circular.
## Siguiente

[L07 — Deque y casos de uso](L07-deque-y-casos-de-uso.md)
