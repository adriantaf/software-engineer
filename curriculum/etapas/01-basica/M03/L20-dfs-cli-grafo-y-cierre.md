---
id: L20
materia: M03
orden: 20
titulo: DFS, CLI de grafo y cierre
horas: 3
semana: 5
lectura: "Rosen Cap. 10.3 — DFS; repaso cap. 10 según huecos"
evidencia: "src/dfs.ts + src/cli.ts + demos.md (10 demos) + README proyecto + checklist P1–P3 y proyecto"
---

# L20 — DFS, CLI de grafo y cierre

**~3 h · Semana 5**

Cierras M03: DFS, CLI que lee JSON e imprime recorridos y grados, y revisión honesta de todas las evidencias.

## Objetivo

Implementar DFS (iterativo o recursivo); entregar CLI del proyecto; completar a 10 demostraciones en `demos.md`; autoevaluar P1–P3 y criterios de dominio.

## Pasos

### 1. DFS (60–70 min)

`src/dfs.ts`:

```ts
import type { Grafo } from "./graph";

export function dfs<T>(g: Grafo<T>, origen: T): T[] {
  const visitados = new Set<T>();
  const orden: T[] = [];
  function visitar(v: T) {
    if (visitados.has(v)) return;
    visitados.add(v);
    orden.push(v);
    for (const w of g.adyacencia.get(v) ?? []) visitar(w);
  }
  visitar(origen);
  return orden;
}
```

Tests: mismo grafo que BFS; orden distinto salvo casos triviales. Documenta ciclo: versión con `visitados` evita bucles infinitos.

Compara BFS vs DFS en `grafos.md` con el mismo origen.

### 2. CLI del proyecto (70–80 min)

`src/cli.ts` (ejecutable con `npx tsx src/cli.ts grafos/ejemplo.json`):

- Carga JSON.
- Imprime lista de vértices y grados.
- Imprime orden BFS y DFS desde un vértice (argumento o primer vértice).
- Mensaje de ayuda si falta archivo.

Actualiza `projects/m03-discretas/README.md` con sección **Teoría**: 1 párrafo BFS, 1 DFS, 1 representación.

### 3. P1 — Diez demostraciones (30 min)

Cuenta entradas en `demos.md`. Si faltan, completa hasta **10** (pueden ser cortas pero completas). Numeración continua.

### 4. Checklist final (40 min)

| Ítem | Evidencia |
|------|-----------|
| **P1** | `demos.md` con 10 pruebas |
| **P2** | `sets.ts`, `relations.ts` (matriz), `graph.ts` + tests |
| **P3** | `complejidad.md` con 5 funciones |
| **Proyecto** | CLI funcional + `grafos/*.json` |

Ejecuta:

```bash
cd projects/m03-discretas && npm test
npx tsx src/cli.ts grafos/ejemplo.json
```

Pega salida relevante en README o `apuntes/cierre.md`.

### 5. Criterios de dominio (20 min)

En `apuntes/cierre.md`, responde sí/no + frase:

- [ ] Inducción de un sumatorio sin copiar.
- [ ] Lista vs matriz de adyacencia en un caso concreto.
- [ ] Permutación vs combinación en problema nuevo.
- [ ] Big-O no confundido con velocidad empírica.

### 6. Commits y UI (15 min)

Commit final coherente. Marca lecciones L01–L20 solo si cada una cumple su “Hecho cuando”. Marca prácticas/proyecto en la ficha con evidencia real.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 10.3 (DFS) + repaso según huecos |
| Ficha | [M03 — Matemáticas discretas](../M03-matematicas-discretas.md) |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `dfs` y `bfs` probados; CLI imprime grados y ambos recorridos.
2. `demos.md` tiene ≥10 demostraciones; P2 y P3 verificables.
3. `cierre.md` o README documenta retro y criterios de dominio.

## Errores comunes

- Marcar M03 completa sin CLI ni tests verdes.
- DFS sin manejar ciclos en grafo no dirigido.
- README del proyecto sin teoría (solo comandos).

## Siguiente

Vuelve a la [ficha M03](../M03-matematicas-discretas.md), cierra checkboxes con evidencia, y continúa con **M04 — Probabilidad y estadística** (o la materia que siga en tu plan).
