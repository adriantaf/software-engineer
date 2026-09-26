---
id: L15
materia: M08
orden: 15
titulo: Caminos en grafos no ponderados
horas: 5.0
semana: 4
lectura: Camino más corto en aristas unitarias = BFS
evidencia: camino mínimo en aristas no peso
---

# L15 — Caminos en grafos no ponderados

**~5.0 h · Semana 4**

Con peso uniforme, BFS da el camino con menos aristas.

## Objetivo

Calcular distancia (y camino) mínimo start→goal con BFS y parents.

## Pasos

### 1. Extiende BFS (60 min)

Guarda `parent` o `prev`. Al llegar a goal, reconstruye lista invirtiendo.

### 2. API clara (40 min)

`shortestPath(graph, start, goal): { dist: number, path: string[] } | null`

### 3. Tests (50 min)

Camino simple; sin camino; start=goal dist 0; grafo con ciclo no se cuelga.

### 4. Problema / doc (40 min)

Enunciado tipo “mínimas citas de referencias entre clientes” (grafo demo) en `problems/` o `docs/`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): camino minimo no ponderado BFS"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | BFS distancias; reconstruir camino con parent[] | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Función que devuelve distancia y/o camino start→goal en grafo no ponderado.
2. Tests: alcanzable, inalcanzable, start=goal.
3. Commit `feat(m08): camino minimo no ponderado BFS`.

## Errores comunes

- Usar Dijkstra “porque sí” en grafos unitarios sin justificar.
- No reconstruir camino cuando se pide.
- Distancia mal inicializada (0 vs Infinity).

## Siguiente

[L16 — Problemas de grafos semana 4](L16-problemas-de-grafos-semana-4.md)
