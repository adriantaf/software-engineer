---
id: L21
materia: M07
orden: 21
titulo: "Grafos: repaso y representación"
horas: 5.0
semana: 6
lectura: "Grafos: lista de adyacencia vs matriz"
evidencia: Adjacency list en TS reutilizable
---

# L21 — Grafos: repaso y representación

**~5.0 h · Semana 6**

Repasas M03 con una API TypeScript reutilizable (base para M08 BFS/DFS).

## Objetivo

Implementar grafo por lista de adyacencia con tests claros.

## Pasos

### 1. Lectura corta (30 min)

Lista vs matriz: memoria y costo de `neighbors`. Elige lista para el curso.

### 2. API (80 min)

`src/graph.ts`:

```ts
export class Graph {
  addVertex(v: string): void
  addEdge(a: string, b: string, undirected = true): void
  neighbors(v: string): string[]
  vertices(): string[]
}
```

### 3. Tests (50 min)

Triángulo A-B-C; dirigido vs no dirigido; vértice aislado.

### 4. Ejemplo dominio (40 min)

En `docs/grafo-agenda.md`: clientes/servicios como “quién recomienda a quién” (3 nodos). Solo documentación.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): grafo lista de adyacencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Lista de adyacencia; dirigido vs no dirigido | [VisuAlgo · Graph](https://visualgo.net/en/graphds) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/graph.ts` con `addVertex`, `addEdge`, `neighbors`.
2. Tests: grafo pequeño no dirigido; edge bidireccional; vecino ausente.
3. Commit `feat(m07): grafo lista de adyacencia`.

## Errores comunes

- Matriz densa para grafo sparse sin justificar.
- Olvidar simetría en no dirigido.
- API sin tipos (arrays `any`).

## Siguiente

[L22 — Benchmark P3: nativo vs propio](L22-benchmark-p3-nativo-vs-propio.md)
