---
id: L16
materia: M08
orden: 16
titulo: Problemas de grafos semana 4
horas: 5.0
semana: 4
lectura: "Cierre semana grafos: +2 problemas en índice"
evidencia: problems/ +2 grafos
---

# L16 — Problemas de grafos semana 4

**~5.0 h · Semana 4**

Consolidás la semana 4 con dos prácticas más y el índice al día.

## Objetivo

Sumar dos problemas de grafos bien empaquetados y actualizar el índice.

## Pasos

### 1. Selección (20 min)

Ideas: clone graph, course schedule (ciclo), flood fill, word ladder corto.

### 2. Problema 1 (80 min)

Plantilla completa + 3 tests.

### 3. Problema 2 (80 min)

Igual. Si detectas ciclo, documenta complejidad.

### 4. Índice + bitácora (30 min)

`bitacora/semana-04.md` opcional: qué patrón aún te cuesta.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): problemas grafos semana 4"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Práctica BFS/DFS adicional; índice ≥ entradas de grafos | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. **+2** problemas de grafos (además de L13–L15 si ya contaban, completa hasta tener evidencia clara de dos más o consolida carpetas).
2. `indice-patrones.md` con filas bfs/dfs/camino.
3. Commit `feat(m08): problemas grafos semana 4`.

## Errores comunes

- Reentregar el mismo archivo tres veces con otro nombre.
- Índice desactualizado.
- Tests flaky por orden de vecinos no determinista sin sort.

## Siguiente

[L17 — Memoización top-down](L17-memoizacion-top-down.md)
