---
id: L13
materia: M08
orden: 13
titulo: BFS repaso y cola
horas: 5.0
semana: 4
lectura: BFS sobre grafos / grids con cola
evidencia: 1 problema BFS + grafo test
---

# L13 — BFS repaso y cola

**~5.0 h · Semana 4**

BFS explora por capas; la cola es obligatoria.

## Objetivo

Implementar BFS reutilizable y resolver un problema con evidencia P1.

## Pasos

### 1. Grafo de prueba (40 min)

`src/graph.ts` (lista de adyacencia) o reusa el de M07 copiando lo mínimo. Tests de vecinos.

### 2. `bfs(start)` (70 min)

Cola + set visitados; opcional mapa `dist`. Complejidad O(V+E) en análisis corto `docs/bfs.md`.

### 3. Problema (70 min)

Ej. número de islas (grid), shortest path en grid sin pesos, o “grados de separación”. Carpeta en `problems/`.

### 4. Índice (20 min)

Patrón `bfs`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): bfs con cola"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | BFS: cola, visitados, capas O(V+E) | [VisuAlgo · BFS](https://visualgo.net/en/dfsbfs) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Utilidad de grafo o grid + `bfs` que retorna orden de visita o distancias.
2. Un problema en `problems/` resuelto con BFS + ≥3 tests.
3. Commit `feat(m08): bfs con cola`.

## Errores comunes

- BFS con stack (eso es DFS).
- No marcar visitados → loops.
- Complejidad sin hablar de V y E.

## Siguiente

[L14 — DFS y componentes](L14-dfs-y-componentes.md)
