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

## Análogos
UABC/Tec: Estructuras de datos.

## Objetivos
1. Implementar lista, pila, cola, hash, árbol.
2. Explicar costo temporal/espacial.
3. Elegir estructura según caso de uso real.

## Cómo estudiar esta materia
- Primero implementa a mano; luego compara con `Array`/`Map` nativos.
- Cada estructura: 5 tests mínimos + un benchmark ingenuo.

## Día 1 (2–3 h)
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

## Temario
Arrays, listas, pilas, colas, hash tables, árboles, heaps intro, grafos (repaso M03).

## Libros (ES)
Texto universitario de ED en español + implementación propia obligatoria.

## Prácticas
P1–P3 del frontmatter. Evidencia en `projects/m07-estructuras/`.

## Proyecto útil
Librería publicada localmente con README “cuándo usar cada una”.

## Errores comunes
Usar solo arrays para todo; olvidar colisiones en hash; no medir.

## Criterios de dominio
- [ ] Explicas cuándo un hash gana a un árbol.
- [ ] Tus estructuras pasan tests y un benchmark documentado.
