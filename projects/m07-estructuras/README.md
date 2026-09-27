# M07 — Estructuras de datos

Carpeta de **evidencia** + librería TypeScript. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Implementas estructuras a mano para elegir bien (no solo usar `Array`). Mides y documentas trade-offs.

## Arranque rápido

```bash
cd projects/m07-estructuras
npm install
npm test
npm run build   # opcional
npm run bench   # P3 — cuando exista bench/run.ts
```

Si aún no hay `package.json`, L01 te guía a crearlo (TypeScript strict + Vitest).

## Estructura esperada

```
projects/m07-estructuras/
├── README.md                 # esta guía + “cuándo usar cada una” (L23)
├── package.json
├── tsconfig.json
├── COMPLEJIDAD.md            # tablas Big-O (desde L01)
├── bitacora/                 # semana-01.md … cierre-m07.md
├── docs/                     # hash-notes, bst, heap, etc.
├── src/
│   ├── index.ts              # API pública
│   ├── dynamic-array.ts
│   ├── singly-linked-list.ts
│   ├── doubly-linked-list.ts
│   ├── stack.ts
│   ├── queue.ts
│   ├── circular-queue.ts
│   ├── deque.ts
│   ├── hash/
│   ├── hash-map.ts
│   ├── bst.ts
│   ├── heap-model.ts
│   ├── min-heap.ts
│   ├── priority-queue.ts
│   ├── graph.ts
│   └── exercises/
├── tests/                    # o *.test.ts junto a src (Vitest)
└── bench/
    ├── run.ts
    └── RESULTADOS.md         # P3
```

## Lecciones → artefactos

| Semana | Lecciones | Qué debe existir aquí |
|--------|-----------|------------------------|
| 1 | L01–L04 | Toolchain, DynamicArray, listas, `COMPLEJIDAD.md`, `bitacora/semana-01.md` |
| 2 | L05–L08 | Stack, Queue, CircularQueue, Deque + sección LIFO/FIFO en README |
| 3 | L09–L12 | Hash + HashMap (rehash) + cierre P1 vs `Map` |
| 4 | L13–L16 | BST + recorridos + format + README P2 |
| 5 | L17–L20 | Heap, MinHeap, PriorityQueue, heap vs BST |
| 6 | L21–L24 | Graph, `bench/RESULTADOS.md`, guía de selección, cierre |

## Checklist (Evidencia de hecho)

- **P1 — Básicas:** Lista, pila, cola, hash con tests.
- **P2 — BST:** Árbol + recorridos + tests.
- **P3 — Bench:** Tabla tiempos vs `Array`/`Map` en `bench/RESULTADOS.md`.
- **Proyecto — Lib ED:** README “cuándo usar cada una” + suite verde + `src/index.ts`.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M07-estructuras-de-datos.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M07/`
- Plan: `/materia/M07/`
