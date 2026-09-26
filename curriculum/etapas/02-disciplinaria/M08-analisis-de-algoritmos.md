---
id: M08
titulo: Análisis de algoritmos
etapa: disciplinaria
orden: 8
semanas: 6
horas: 120
practicas:
  - id: p1
    titulo: 15 problemas clasificados por patrón
  - id: p2
    titulo: Ordenamientos implementados + análisis
  - id: p3
    titulo: Búsqueda y DP intro (3 problemas)
proyecto:
  id: proj
  titulo: Autocomplete / búsqueda para tu producto
---

# M08 — Análisis de algoritmos

## Por qué existe

Sin análisis, “optimizas” a ciegas: cambias código sin saber si el cuello de botella es O(n²) o la red. Esta materia te da **patrones transferibles** (two pointers, binary search, grafos cortos, DP intro) y te obliga a **justificar complejidad** en voz alta — no una maratón tóxica de plataformas.

El proyecto autocomplete enlaza con el catálogo de clientes/servicios de [Agenda Ops](../../producto-saas.md): búsqueda rápida con dataset realista.

**En resumen:** clasificas problemas por patrón, mides complejidad y construyes algo útil (autocomplete) para tu producto.


## Objetivos de aprendizaje

Al terminar debes poder:

1. Expresar y comparar costos en notación asintótica (Θ, O, Ω) en peor caso y en promedio cuando aplique.
2. Implementar y analizar al menos dos ordenamientos distintos (p. ej. merge y quick o heap).
3. Aplicar binary search, two pointers y sliding window en problemas de arrays ordenados o ventanas.
4. Recorrer grafos con BFS/DFS y resolver un camino corto introductorio.
5. Resolver 2–3 problemas de programación dinámica con caso base y transición explícitos.
6. Entregar un motor de autocomplete documentado (estructura de datos + complejidad de consulta).

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md) si aún no tienes la rutina de 20 h/semana.
- **4–5 problemas por semana** con editorial solo después de 30–45 min atascado.
- Después de cada solución: escribe complejidad temporal y espacial en Markdown (`projects/m08-algoritmos/`).
- Clasifica cada problema por **patrón** (hash, two pointers, graph, DP…) en un índice `projects/m08-algoritmos/indice-patrones.md`.
- No copies soluciones completas: entiende el invariante y reescribe sin mirar.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Teoría CLRS | 6–8 | Caps. según tabla Lecturas |
| Problemas | 6–8 | 2–3 problemas con bitácora |
| Proyecto | 4–6 | Autocomplete / búsqueda |
| Retro | 1 | Un patrón que aún no sale sin pistas |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Crea la carpeta de evidencia:
   ```bash
   mkdir -p projects/m08-algoritmos/problems projects/m08-algoritmos/sorts
   ```
2. Reescribe **binary search** en TypeScript con tests de bordes (array vacío, un elemento, objetivo ausente, duplicados si aplica).
3. En `projects/m08-algoritmos/binary-search-analisis.md`, justifica **O(log n)** en peor caso (3–5 frases).
4. Resuelve **2** problemas fáciles de arrays (p. ej. two sum, max subarray intro) sin mirar la solución primero; guarda en `projects/m08-algoritmos/problems/`.
5. Commit atómico, por ejemplo: `feat(m08): binary search + 2 problemas arrays`.

## Ejemplo — binary search con invariante

```ts
export function binarySearch(a: number[], t: number): number {
  let lo = 0, hi = a.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (a[mid] === t) return mid;
    if (a[mid]! < t) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;
}
```

Regla: el invariante es “si `t` está, está en `[lo, hi]`”. Cada iteración reduce el intervalo a la mitad → O(log n).

## Temario semanal

### Semana 1 — Complejidad y análisis (~20 h)

- Notación Θ, O, Ω; funciones comunes (log n, n log n, n²).
- Análisis de bucles anidados y recursión simple (árbol de llamadas).
- Binary search y variantes (lower bound intro).
- Bitácora: 3 problemas con complejidad escrita en voz alta.

### Semana 2 — Ordenamiento (~20 h)

- Comparación de algoritmos: insertion, merge, quick, heap (según tu edición CLRS).
- Estabilidad, peor caso vs promedio de quicksort.
- Práctica P2: implementa ≥2 sorts en `projects/m08-algoritmos/sorts/` + tabla Big-O en README.
- VisuAlgo Sorting como apoyo visual (no sustituto de implementar).

### Semana 3 — Búsqueda, hashing y two pointers (~20 h)

- Hash maps para conteos y lookup O(1) amortizado.
- Two pointers y sliding window en arrays/strings.
- Problemas clasificados en `indice-patrones.md` (mín. 5 entradas esta semana).

### Semana 4 — Árboles y grafos intro (~20 h)

- BFS/DFS; representación lista de adyacencia.
- Caminos en grafos no ponderados; intro a Dijkstra si el tiempo alcanza.
- Conecta con M07: cuándo un heap o un hash cambia la solución.

### Semana 5 — Programación dinámica intro (~20 h)

- Memoización top-down vs bottom-up.
- 3 problemas clásicos (p. ej. escalones, mochila 0/1 simplificada, LCS intro) con **caso base** explícito.
- Práctica P3: cada problema en carpeta propia con explicación del estado DP.

### Semana 6 — Proyecto autocomplete (~20 h)

- Trie, prefix map o índice invertido según tu dataset (documenta la elección).
- Integración con dominio Agenda Ops: nombres de clientes o servicios (dataset de prueba en repo).
- Demo CLI o endpoint mínimo + README de complejidad de búsqueda por prefijo.

## Lecturas

Canon: *Introducción a los algoritmos* — Cormen et al. (CLRS, ed. ES). Alternativa: VisuAlgo + enunciados propios. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos (CLRS, por tema) | Alternativa |
|--------|---------------------------|-------------|
| 1 | **Crecimiento / notación asintótica** (Θ, O, Ω) | Notas M08 + justificar Big-O de 5 funciones tuyas |
| 2 | **Ordenamiento** (heapsort/mergesort/quicksort — los que cubra tu ed.) | VisuAlgo Sorting + implementar 2 |
| 3 | **Búsqueda**, hashing, two pointers / sliding window (notas M08) | Problemas filtrados (fácil→medio) |
| 4 | **Árboles y grafos** intro (BFS/DFS, caminos) | VisuAlgo Graph |
| 5 | **Programación dinámica** intro (1–2 problemas clásicos en libro) | Editorial propia en Markdown |
| 6 | Proyecto autocomplete: estructura + complejidad documentada | — |

**Regla:** cada problema entregado lleva enunciado, complejidad, código, **3 casos de prueba** (incl. borde).

## Prácticas

1. **P1 — 15 problemas:** Carpeta `projects/m08-algoritmos/problems/` con subcarpetas o archivos por problema; clasificación por patrón en `indice-patrones.md`.
2. **P2 — Sorts:** ≥2 ordenamientos en `projects/m08-algoritmos/sorts/` + análisis Big-O comparado en `projects/m08-algoritmos/sorts/README.md`.
3. **P3 — DP intro:** 3 problemas en `projects/m08-algoritmos/dp/` con caso base y transición explicados en Markdown.

## Proyecto útil

**Autocomplete / búsqueda para tu producto:** en `projects/m08-algoritmos/autocomplete/` (o ruta documentada en `projects/m08-algoritmos/README.md`):

- Dataset de prueba (CSV/JSON) de clientes o servicios tipo Agenda Ops.
- API o CLI que responda a prefijos con latencia razonable en tu máquina.
- README: estructura elegida, complejidad de insert y de query, límites del dataset demo.

## Errores comunes

- Copiar soluciones de plataformas sin poder rederivarlas.
- Confundir **promedio** con **peor caso** al justificar quicksort.
- DP sin caso base o con estados mal definidos.
- Autocomplete que escanea O(n) toda la lista sin documentar que es aceptable solo en demo pequeño.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — 15 problemas:** `projects/m08-algoritmos/problems/` con enunciado, complejidad, código, 3 tests c/u; `indice-patrones.md` actualizado.
- **P2 — Sorts:** `projects/m08-algoritmos/sorts/` con ≥2 implementaciones + `README.md` de análisis Big-O.
- **P3 — DP intro:** `projects/m08-algoritmos/dp/` con 3 problemas y caso base explicado.
- **Proyecto — Autocomplete:** Demo en `projects/m08-algoritmos/autocomplete/` + README de complejidad enlazado desde `projects/m08-algoritmos/README.md`.

## Criterios de dominio

- [ ] Resuelves un problema **medio** de arrays/hashes explicando complejidad sin mirar notas.
- [ ] Comparas dos sorts en peor y caso promedio con honestidad.
- [ ] Autocomplete funciona con dataset de prueba y documentas la estructura subyacente.
- [ ] Tu índice de patrones tiene ≥15 entradas alineadas con P1.
