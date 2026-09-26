---
id: L14
materia: M08
orden: 14
titulo: DFS y componentes
horas: 5.0
semana: 4
lectura: DFS y componentes conexas
evidencia: problema componentes conexas
---

# L14 — DFS y componentes

**~5.0 h · Semana 4**

DFS recorre profundo; sirve para marcar componentes y ciclos introductorios.

## Objetivo

Contar componentes conexas (o resolver problema equivalente) con DFS y tests.

## Pasos

### 1. DFS base (50 min)

`dfs(v, visited)` recursivo. Versión iterativa opcional.

### 2. Componentes (70 min)

Algoritmo: para cada vértice no visitado, DFS y ++count. Tests con 1 componente, 3 componentes, grafo vacío.

### 3. Problema empaquetado (60 min)

`problems/…-componentes/` con enunciado de red social / salas conectadas.

### 4. Índice (20 min)

Patrón `dfs`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): dfs componentes conexas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | DFS recursivo/iterativo; contar componentes | [VisuAlgo · DFS](https://visualgo.net/en/dfsbfs) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `connectedComponents(graph)` (o problema equivalente) con tests.
2. Documentas recursivo vs stack explícito en 5–8 líneas.
3. Commit `feat(m08): dfs componentes conexas`.

## Errores comunes

- Contar nodos en vez de componentes.
- No resetear visitados entre componentes.
- Stack overflow en grafos grandes sin mencionar límite de recursión.

## Siguiente

[L15 — Caminos en grafos no ponderados](L15-caminos-en-grafos-no-ponderados.md)
