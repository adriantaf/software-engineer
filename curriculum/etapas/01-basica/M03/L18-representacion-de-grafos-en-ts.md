---
id: L18
materia: M03
orden: 18
titulo: Representación de grafos en TS
horas: 3
semana: 5
lectura: "Rosen Cap. 10.2 — listas de adyacencia y matrices de adyacencia"
evidencia: "src/graph.ts (lista + matriz) + tests carga desde ejemplo.json"
---

# L18 — Representación de grafos en TS

**~3 h · Semana 5**

Misma información, dos estructuras: lista (sparse) vs matriz (dense). Implementas ambas y cargas desde JSON.

## Objetivo

Parsear `ejemplo.json`; construir lista y matriz de adyacencia; comparar espacio/tiempo en un párrafo argumentado (P2).

## Pasos

### 1. Tipos (20 min)

`src/graph.ts`:

```ts
export type Arista<T> = [T, T];

export type GrafoJson<T = string> = {
  dirigido: boolean;
  vertices: T[];
  aristas: Arista<T>[];
};

export type Grafo<T> = {
  dirigido: boolean;
  vertices: T[];
  adyacencia: Map<T, T[]>;
};
```

### 2. Carga desde JSON (50–60 min)

```ts
export function desdeJson<T>(raw: GrafoJson<T>): Grafo<T> {
  const ady = new Map<T, T[]>();
  for (const v of raw.vertices) ady.set(v, []);
  for (const [u, v] of raw.aristas) {
    ady.get(u)!.push(v);
    if (!raw.dirigido) ady.get(v)!.push(u);
  }
  return { dirigido: raw.dirigido, vertices: [...raw.vertices], adyacencia: ady };
}
```

Lee `grafos/ejemplo.json` en tests con `fs` o importa el JSON según tu setup.

### 3. Matriz de adyacencia (50 min)

```ts
export function matrizAdyacencia<T>(g: Grafo<T>): number[][] {
  const n = g.vertices.length;
  const idx = new Map(g.vertices.map((v, i) => [v, i]));
  const m = Array.from({ length: n }, () => Array(n).fill(0));
  for (const [u, vecinos] of g.adyacencia) {
    const i = idx.get(u)!;
    for (const v of vecinos) m[i][idx.get(v)!] = 1;
  }
  return m;
}
```

Test: simetría en grafo no dirigido.

### 4. Comparación escrita (30 min)

En `grafos.md` o README: para `|V|=n`, `|E|=m`, coste espacial lista `O(n+m)` vs matriz `O(n²)`; cuándo elegirías cada una (ej. grafo denso de 50 nodos vs red social sparse).

### 5. Grados desde código (20 min)

Función `grados(g): Map<T, number>` y compara con cálculo manual de L17.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 10.2 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `desdeJson` + `matrizAdyacencia` con tests usando `ejemplo.json`.
2. Párrafo comparando lista vs matriz con un ejemplo numérico.
3. Grados por código coinciden con L17.

## Errores comunes

- Vértice en arista que no está en `vertices`.
- Matriz asimétrica en grafo no dirigido por bug de doble arista.
- Índices inconsistentes entre funciones.

## Siguiente

[L19 — Búsqueda en anchura (BFS)](L19-busqueda-en-anchura-bfs.md)
