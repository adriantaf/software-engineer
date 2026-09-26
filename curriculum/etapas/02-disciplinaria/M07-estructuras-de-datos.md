---
id: M07
titulo: Estructuras de datos
etapa: disciplinaria
orden: 7
semanas: 6
horas: 120
practicas:
  - id: p1
    titulo: Implementar lista, pila, cola y hash map
  - id: p2
    titulo: Árboles BST + recorridos
  - id: p3
    titulo: Benchmarks de tus estructuras vs nativas
proyecto:
  id: proj
  titulo: Librería de ED con tests y documentación
---

# M07 — Estructuras de datos

## Por qué existe
Elegir mal una estructura te cuesta latencia y dinero. Aquí las **implementas** para entender trade-offs, no solo las usas.

**En resumen:** implementas estructuras a mano para elegir bien (no solo usar `Array`). Mides y documentas trade-offs.


## Objetivos de aprendizaje
1. Implementar lista, pila, cola, hash, árbol.
2. Explicar costo temporal/espacial.
3. Elegir estructura según caso de uso real.

## Cómo estudiar esta materia
- Primero implementa a mano; luego compara con `Array`/`Map` nativos.
- Cada estructura: 5 tests mínimos + un benchmark ingenuo.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura + diseño | 6–8 | Capítulos ED de la semana |
| Implementar + tests | 6–8 | Estructura + 5 tests |
| Benchmark | 4–6 | Vs nativas documentado |
| Retro | 1 | Cuándo hash gana a árbol |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy
1. Crea `projects/m07-estructuras/`.
2. Implementa una pila tipada en TS con `push`/`pop`/`peek`.
3. Escribe 4 tests Vitest.
4. Anota Big-O de cada operación en el README.

## Ejemplo
```ts
export class Stack<T> {
  private items: T[] = [];
  push(x: T) { this.items.push(x); }
  pop(): T | undefined { return this.items.pop(); }
  get size() { return this.items.length; }
}
```

## Temario semanal
Arrays, listas, pilas, colas, hash tables, árboles, heaps intro, grafos (repaso M03).

## Lecturas

Canon: texto universitario de ED estilo Joyanes (ed. ES) **o** apuntes equivalentes + implementación propia. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos / foco de lectura | Alternativa |
|--------|----------------------------|-------------|
| 1 | Arrays y **listas enlazadas** (costos, operaciones) | Implementa + 5 tests; compara con `Array` |
| 2 | **Pilas y colas** (y variantes) | Misma librería `projects/m07-estructuras/` |
| 3 | **Tablas hash** (función, colisiones, load factor) | Docs MDN `Map`/`Set` como contraste |
| 4 | **Árboles** / BST + recorridos | Visualización propia o VisuAlgo |
| 5 | **Heaps** intro + prioridad | Implementación mínima + tests |
| 6 | **Grafos** (repaso M03) + benchmarks + README “cuándo usar cada una” | — |

**Regla:** leer el capítulo → implementar → medir. Sin implementación no cuenta.

## Prácticas
P1–P3 del frontmatter. Evidencia en `projects/m07-estructuras/`.

## Proyecto útil
Librería publicada localmente con README “cuándo usar cada una”.

## Errores comunes
Usar solo arrays para todo; olvidar colisiones en hash; no medir.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Básicas:** Lista, pila, cola, hash con tests en `projects/m07-estructuras/`.
- **P2 — BST:** Árbol + recorridos + tests.
- **P3 — Bench:** Tabla tiempos vs `Array`/`Map`.
- **Proyecto — Lib ED:** README “cuándo usar cada una” + suite verde.

## Criterios de dominio
- [ ] Explicas cuándo un hash gana a un árbol.
- [ ] Tus estructuras pasan tests y un benchmark documentado.
