---
id: L19
materia: M03
orden: 19
titulo: Búsqueda en anchura (BFS)
horas: 3
semana: 5
lectura: "Rosen Cap. 10.3 — BFS, distancias en grafos no ponderados"
evidencia: "src/bfs.ts + tests con ejemplo.json + traza en apuntes"
---

# L19 — Búsqueda en anchura (BFS)

**~3 h · Semana 5**

BFS explora por capas; en grafos no ponderados da distancia en número de aristas.

## Objetivo

Implementar BFS desde un vértice origen; devolver orden de visita y distancias; probar en `ejemplo.json` y en un grafo donde BFS ≠ DFS.

## Pasos

### 1. Algoritmo en papel (40 min)

En `grafos.md`, pseudocódigo BFS con cola `Q` y conjunto `visitados`. Indica invariante: al sacar `v` de `Q`, distancia mínima desde origen está fijada (grafo no ponderado).

### 2. Implementación (80–90 min)

`src/bfs.ts`:

```ts
import type { Grafo } from "./graph";

export type ResultadoBfs<T> = {
  orden: T[];
  distancia: Map<T, number>;
};

export function bfs<T>(g: Grafo<T>, origen: T): ResultadoBfs<T> {
  // cola FIFO, visitados, distancia[origen]=0
  throw new Error("implementar");
}
```

Tests:

- Orden y distancias en grafo línea `A-B-C-D`.
- Origen inexistente → error claro.
- Grafo desconexo: nodos no alcanzables ausentes en `distancia` o con ∞ (documenta convención).

### 3. Traza manual (30 min)

En `ejemplo.json`, ejecuta BFS desde `A` a mano (tabla paso a paso) y compara con salida del test.

### 4. Teoría (20 min)

Párrafo en README del proyecto: por qué BFS usa cola y complejidad `O(V+E)` con lista de adyacencia.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 10.3 (BFS) |

## Hecho cuando

1. `bfs` pasa tests en al menos dos grafos.
2. Traza manual coincide con código para un origen.
3. Explicas cuándo BFS encuentra camino más corto en aristas.

## Errores comunes

- Usar pila en lugar de cola (eso es DFS).
- Marcar visitado al encolar vs al desencolar (elige una convención y sé consistente).
- No manejar vértices aislados.

## Siguiente

[L20 — DFS, CLI de grafo y cierre](L20-dfs-cli-grafo-y-cierre.md)
