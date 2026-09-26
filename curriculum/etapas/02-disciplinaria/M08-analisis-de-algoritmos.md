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

## Cómo estudiar esta materia (lecciones)

M08 sigue el formato de lecciones cortas y completas (como M01/M06): marcas una a una cuando cumples “Hecho cuando”.

1. Abre las lecciones **en orden** (L01 → L24).
2. Cada lección trae objetivo, pasos, lectura y criterio “Hecho cuando”.
3. Marca la lección en la UI solo si cumple ese criterio.
4. **4–5 problemas por semana** con editorial solo después de 30–45 min atascado.
5. Clasifica cada problema en `projects/m08-algoritmos/indice-patrones.md`.
6. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Teoría CLRS | 6–8 | Caps. según tabla Lecturas (L01–L04, …) |
| Problemas | 6–8 | 2–3 problemas con bitácora |
| Proyecto | 4–6 | Autocomplete / búsqueda |
| Retro | 1 | Un patrón que aún no sale sin pistas |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la fila de lectura de esa lección.

## Lecciones

### Semana 1 — Complejidad y análisis (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Entorno y binary search con invariante](M08/L01-entorno-y-binary-search-con-invariante.md) | 5 |
| L02 | [Notación asintótica Θ, O y Ω](M08/L02-notacion-asintotica-o-y.md) | 5 |
| L03 | [Análisis de bucles y recursión simple](M08/L03-analisis-de-bucles-y-recursion-simple.md) | 5 |
| L04 | [Tres problemas con complejidad escrita](M08/L04-tres-problemas-con-complejidad-escrita.md) | 5 |

### Semana 2 — Ordenamiento (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Insertion sort implementado](M08/L05-insertion-sort-implementado.md) | 5 |
| L06 | [Merge sort y estabilidad](M08/L06-merge-sort-y-estabilidad.md) | 5 |
| L07 | [Quicksort y peor caso](M08/L07-quicksort-y-peor-caso.md) | 5 |
| L08 | [Tabla P2 sorts en README](M08/L08-tabla-p2-sorts-en-readme.md) | 5 |

### Semana 3 — Búsqueda, hashing y two pointers (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [Hash maps en problemas de conteo](M08/L09-hash-maps-en-problemas-de-conteo.md) | 5 |
| L10 | [Two pointers en arrays ordenados](M08/L10-two-pointers-en-arrays-ordenados.md) | 5 |
| L11 | [Sliding window](M08/L11-sliding-window.md) | 5 |
| L12 | [Índice de patrones (5+ entradas)](M08/L12-indice-de-patrones-5-entradas.md) | 5 |

### Semana 4 — Árboles y grafos intro (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L13 | [BFS repaso y cola](M08/L13-bfs-repaso-y-cola.md) | 5 |
| L14 | [DFS y componentes](M08/L14-dfs-y-componentes.md) | 5 |
| L15 | [Caminos en grafos no ponderados](M08/L15-caminos-en-grafos-no-ponderados.md) | 5 |
| L16 | [Problemas de grafos semana 4](M08/L16-problemas-de-grafos-semana-4.md) | 5 |

### Semana 5 — Programación dinámica intro (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L17 | [Memoización top-down](M08/L17-memoizacion-top-down.md) | 5 |
| L18 | [Programación dinámica bottom-up](M08/L18-programacion-dinamica-bottom-up.md) | 5 |
| L19 | [Tres problemas DP (P3)](M08/L19-tres-problemas-dp-p3.md) | 5 |
| L20 | [Patrones DP y transiciones](M08/L20-patrones-dp-y-transiciones.md) | 5 |

### Semana 6 — Proyecto autocomplete (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L21 | [Autocomplete: elección de estructura](M08/L21-autocomplete-eleccion-de-estructura.md) | 5 |
| L22 | [Implementación trie o índice](M08/L22-implementacion-trie-o-indice.md) | 5 |
| L23 | [Dataset Agenda Ops y demo CLI](M08/L23-dataset-agenda-ops-y-demo-cli.md) | 5 |
| L24 | [Cierre M08 y evidencias](M08/L24-cierre-m08-y-evidencias.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Introducción a los algoritmos* — Cormen et al. (CLRS, ed. ES). Alternativa: VisuAlgo + enunciados propios. Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos (CLRS, por tema) |
|--------|-----------|---------------------------|
| 1 | L01–L04 | **Crecimiento / notación asintótica** (Θ, O, Ω) |
| 2 | L05–L08 | **Ordenamiento** (insertion, merge, quick — según tu ed.) |
| 3 | L09–L12 | **Búsqueda**, hashing, two pointers / sliding window |
| 4 | L13–L16 | **Árboles y grafos** intro (BFS/DFS, caminos) |
| 5 | L17–L20 | **Programación dinámica** intro |
| 6 | L21–L24 | Proyecto autocomplete: estructura + complejidad documentada |

**Regla:** cada problema entregado lleva enunciado, complejidad, código, **3 casos de prueba** (incl. borde).

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

## Prácticas

1. **P1 — 15 problemas:** `projects/m08-algoritmos/problems/` + `indice-patrones.md` — L04–L16 y cierre L24.
2. **P2 — Sorts:** ≥2 ordenamientos en `sorts/` — L05–L08.
3. **P3 — DP intro:** 3 problemas en `dp/` — L19–L20.

## Proyecto útil

**Autocomplete / búsqueda para tu producto:** en `projects/m08-algoritmos/autocomplete/`:

- Dataset de prueba (CSV/JSON) de clientes o servicios tipo Agenda Ops.
- API o CLI que responda a prefijos con latencia razonable en tu máquina.
- README: estructura elegida, complejidad de insert y de query, límites del dataset demo.

## Errores comunes

- Copiar soluciones de plataformas sin poder rederivarlas.
- Confundir **promedio** con **peor caso** al justificar quicksort.
- DP sin caso base o con estados mal definidos.
- Autocomplete que escanea O(n) toda la lista sin documentar que es aceptable solo en demo pequeño.
- Marcar lecciones sin cumplir “Hecho cuando”.

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
