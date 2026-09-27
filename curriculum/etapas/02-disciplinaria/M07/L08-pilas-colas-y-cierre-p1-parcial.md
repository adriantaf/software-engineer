---
id: L08
materia: M07
orden: 8
titulo: Pilas, colas y cierre P1 parcial
horas: 5.0
semana: 2
lectura: Repaso LIFO/FIFO y checklist P1 parcial
evidencia: README sección LIFO/FIFO + bitácora semana 2
---

# L08 — Pilas, colas y cierre P1 parcial

**~5.0 h · Semana 2**

P1 pide lista, pila, cola y hash. Hoy cierras la mitad LIFO/FIFO con documentación clara.

## Objetivo

Dejar documentado el uso de stack/queue/deque, bitácora de semana 2 y suite verde antes de hash.

## Pasos

### 1. Checklist de archivos (30 min)

```bash
ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts
npm test
```

Arregla fallos antes de documentar.

### 2. Sección README (75 min)

Añade tabla: estructura | orden | ops tipicas | ejemplo producto (Agenda Ops: undo de cita, cola de espera, etc.).

### 3. Export barrel (45 min)

`src/index.ts` reexporta Stack, Queue, Deque, listas, DynamicArray. Verifica `npm run build` si tienes `tsc`.

### 4. Bitácora (40 min)

`bitacora/semana-02.md`: un bug que cazaste (p. ej. circular lleno/vacío) y cómo lo viste en un test.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre semana 2 pilas y colas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Cuándo pila vs cola vs deque | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. README tiene sección “LIFO / FIFO / Deque” con cuándo usar cada una (tabla o bullets).
2. `bitacora/semana-02.md` + `npm test` verde para stack/queue/deque.
3. Commit `docs(m07): cierre semana 2 pilas y colas`.

## Errores comunes

- README genérico sin mencionar tus archivos `src/*.ts`.
- Dejar ejercicios de paréntesis rotos.
- Marcar P1 “parcial” sin lista/pila/cola presentes.

## Siguiente

[L09 — Función hash y mapa conceptual](L09-funcion-hash-y-mapa-conceptual.md)
