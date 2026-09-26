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

Al terminar debes poder:

1. Implementar lista, pila, cola, hash y árbol con tests.
2. Explicar costo temporal y espacial en notación asintótica.
3. Elegir estructura según caso de uso real y comparar con tipos nativos de JS/TS.

## Cómo estudiar esta materia (lecciones)

M07 sigue el formato de lecciones cortas y completas (como M01/M06): marcas una a una cuando cumples “Hecho cuando”.

1. Abre las lecciones **en orden** (L01 → L24).
2. Cada lección trae objetivo, pasos, lectura y criterio “Hecho cuando”.
3. Marca la lección en la UI solo si cumple ese criterio.
4. Las **prácticas / proyecto** exigen evidencia en `projects/m07-estructuras/`.
5. Regla de oro: leer el capítulo → implementar → medir. Sin implementación no cuenta.
6. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura + diseño | 6–8 | Capítulos ED de la semana (L01–L04, …) |
| Implementar + tests | 6–8 | Estructura + ≥5 tests |
| Benchmark / README | 4–6 | Vs nativas o guía de uso |
| Retro | 1 | Cuándo hash gana a árbol |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la fila de lectura de esa lección.

## Lecciones

### Semana 1 — Arrays y listas (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Entorno del proyecto y arrays dinámicos](M07/L01-entorno-del-proyecto-y-arrays-dinamicos.md) | 5 |
| L02 | [Lista enlazada simple](M07/L02-lista-enlazada-simple.md) | 5 |
| L03 | [Lista doble y operaciones indexadas](M07/L03-lista-doble-y-operaciones-indexadas.md) | 5 |
| L04 | [Secuencias: repaso de costos y cierre semana 1](M07/L04-secuencias-repaso-de-costos-y-cierre-semana-1.md) | 5 |

### Semana 2 — Pilas y colas (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Pila (Stack) tipada](M07/L05-pila-stack-tipada.md) | 5 |
| L06 | [Cola (Queue) y cola circular](M07/L06-cola-queue-y-cola-circular.md) | 5 |
| L07 | [Deque y casos de uso](M07/L07-deque-y-casos-de-uso.md) | 5 |
| L08 | [Pilas, colas y cierre P1 parcial](M07/L08-pilas-colas-y-cierre-p1-parcial.md) | 5 |

### Semana 3 — Tablas hash (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [Función hash y mapa conceptual](M07/L09-funcion-hash-y-mapa-conceptual.md) | 5 |
| L10 | [Tabla hash con encadenamiento](M07/L10-tabla-hash-con-encadenamiento.md) | 5 |
| L11 | [Factor de carga y rehash](M07/L11-factor-de-carga-y-rehash.md) | 5 |
| L12 | [Hash vs Map nativo (P1 cierre)](M07/L12-hash-vs-map-nativo-p1-cierre.md) | 5 |

### Semana 4 — Árboles BST (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L13 | [BST: inserción y búsqueda](M07/L13-bst-insercion-y-busqueda.md) | 5 |
| L14 | [Recorridos inorder, preorder, postorder](M07/L14-recorridos-inorder-preorder-postorder.md) | 5 |
| L15 | [BST: mínimo, máximo y sucesor](M07/L15-bst-minimo-maximo-y-sucesor.md) | 5 |
| L16 | [Visualización y P2 parcial](M07/L16-visualizacion-y-p2-parcial.md) | 5 |

### Semana 5 — Heaps (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L17 | [Modelo de heap binario](M07/L17-modelo-de-heap-binario.md) | 5 |
| L18 | [Heap mínimo: insert y extractMin](M07/L18-heap-minimo-insert-y-extractmin.md) | 5 |
| L19 | [Cola de prioridad](M07/L19-cola-de-prioridad.md) | 5 |
| L20 | [Heap vs BST para prioridades](M07/L20-heap-vs-bst-para-prioridades.md) | 5 |

### Semana 6 — Grafos, benchmarks y cierre (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L21 | [Grafos: repaso y representación](M07/L21-grafos-repaso-y-representacion.md) | 5 |
| L22 | [Benchmark P3: nativo vs propio](M07/L22-benchmark-p3-nativo-vs-propio.md) | 5 |
| L23 | [README cuándo usar cada estructura](M07/L23-readme-cuando-usar-cada-estructura.md) | 5 |
| L24 | [Cierre M07 y evidencias](M07/L24-cierre-m07-y-evidencias.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: texto universitario de ED estilo Joyanes (ed. ES) **o** apuntes equivalentes + implementación propia. Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos / foco |
|--------|-----------|------------------|
| 1 | L01–L04 | Arrays y **listas enlazadas** (costos, operaciones) |
| 2 | L05–L08 | **Pilas y colas** (y variantes) |
| 3 | L09–L12 | **Tablas hash** (función, colisiones, load factor) |
| 4 | L13–L16 | **Árboles** / BST + recorridos |
| 5 | L17–L20 | **Heaps** intro + prioridad |
| 6 | L21–L24 | **Grafos** (repaso M03) + benchmarks + README |

**Regla:** leer el capítulo → implementar → medir. MDN `Map`/`Set` como contraste, no sustituto de tu hash en P1.

## Ejemplo

```ts
export class Stack<T> {
  private items: T[] = [];
  push(x: T) { this.items.push(x); }
  pop(): T | undefined { return this.items.pop(); }
  get size() { return this.items.length; }
}
```

## Prácticas

1. **P1:** Lista, pila, cola, hash con tests — L01–L12.
2. **P2:** BST + recorridos — L13–L16.
3. **P3:** Benchmarks vs `Array`/`Map` — L22.

## Proyecto útil

Librería en `projects/m07-estructuras/` con README “cuándo usar cada una”, suite verde y API exportada (L23–L24).

## Errores comunes

- Usar solo arrays para todo; olvidar colisiones en hash; no medir.
- Marcar lecciones sin cumplir “Hecho cuando”.
- Prometer O(1) donde hay amortizado o peor caso distinto sin explicarlo.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Básicas:** Lista, pila, cola, hash con tests en `projects/m07-estructuras/`.
- **P2 — BST:** Árbol + recorridos + tests.
- **P3 — Bench:** Tabla tiempos vs `Array`/`Map`.
- **Proyecto — Lib ED:** README “cuándo usar cada una” + suite verde.

## Criterios de dominio

- [ ] Explicas cuándo un hash gana a un árbol.
- [ ] Tus estructuras pasan tests y un benchmark documentado.
