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
Sin análisis, “optimizas” a ciegas. Aprendes patrones transferibles (no maratón tóxica).

**En resumen:** clasificas problemas por patrón, mides complejidad y construyes algo útil (autocomplete) para tu producto.


## Objetivos
Big-O, divide y vencerás, greedy intro, DP intro, grafos cortos.

## Cómo estudiar esta materia
4–5 problemas/semana. Después de resolver: escribe complejidad en voz alta.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Teoría CLRS | 6–8 | Caps. Lecturas |
| Problemas | 6–8 | 2–3 problemas con editorial |
| Proyecto | 4–6 | Autocomplete / búsqueda |
| Retro | 1 | Un medio que aún no sale |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)
1. Reescribe binary search en TS con tests de bordes.
2. Justifica O(log n) en Markdown.
3. Resuelve 2 problemas de arrays fáciles sin mirar la solución primero.

## Ejemplo
```ts
export function binarySearch(a: number[], t: number): number {
  let lo = 0, hi = a.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (a[mid] === t) return mid;
    if (a[mid]! < t) lo = mid + 1; else hi = mid - 1;
  }
  return -1;
}
```

## Temario
Semanas: complejidad → sorting → searching/two pointers → trees/graphs intro → DP intro → proyecto autocomplete.

## Lecturas

Canon: *Introducción a los algoritmos* — Cormen et al. (CLRS, ed. ES). Alternativa: VisuAlgo + enunciados M08. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos (CLRS, por tema) | Alternativa |
|--------|---------------------------|-------------|
| 1 | **Caps. de crecimiento / notación asintótica** (Θ, O, Ω) | Notas M08 + justificar Big-O de 5 funciones tuyas |
| 2 | **Ordenamiento** (heapsort/mergesort/quicksort — los que cubra tu ed.) | VisuAlgo Sorting + implementar 2 |
| 3 | **Búsqueda**, hashing aplicado, two pointers / sliding window (notas M08) | Problemas filtrados (fácil→medio) |
| 4 | **Árboles y grafos** intro (BFS/DFS, caminos) | VisuAlgo Graph |
| 5 | **Programación dinámica** intro (1–2 problemas clásicos) | Editorial propia en Markdown |
| 6 | Proyecto autocomplete: estructura + complejidad documentada | — |

**Regla:** cada problema: enunciado, complejidad, código, 3 casos de prueba.

## Proyecto útil
Motor de autocomplete para catálogo/clientes del CRM.

## Errores comunes
Copiar soluciones; confundir promedio con peor caso; DP sin caso base.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — 15 problemas:** Carpeta con enunciado, complejidad, código, 3 tests c/u.
- **P2 — Sorts:** ≥2 ordenamientos + análisis Big-O.
- **P3 — DP intro:** 3 problemas DP con caso base explicado.
- **Proyecto — Autocomplete:** Demo con dataset de prueba + README de complejidad.

## Criterios de dominio
- [ ] Resuelves un medio de arrays/hashes explicando complejidad.
- [ ] Autocomplete funciona con dataset de prueba.
