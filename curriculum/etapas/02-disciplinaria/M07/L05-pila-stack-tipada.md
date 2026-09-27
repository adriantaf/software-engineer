---
id: L05
materia: M07
orden: 5
titulo: Pila (Stack) tipada
horas: 5.0
semana: 2
lectura: "Pilas LIFO: push, pop, peek e invariantes"
evidencia: Stack<T> con push/pop/peek + 4 tests (inicio P1)
---

# L05 — Pila (Stack) tipada

**~5.0 h · Semana 2**

LIFO es la base de undo, parsers y DFS. Hoy la implementas tipada y la usas en un ejercicio corto.

## Objetivo

Entregar `Stack<T>` con API mínima, tests LIFO y un caso de uso (paréntesis balanceados o undo).

## Pasos

### 1. Lectura (30 min)

Sección de pilas en tu texto ED. Anota precondiciones de `pop`/`peek`.

### 2. Implementación (60 min)

`src/stack.ts` — puedes basarte en array **privado** o en tu lista; no reexportes mutadores internos.

```ts
export class Stack<T> {
  push(x: T): void
  pop(): T          // o T | undefined — documenta
  peek(): T
  get size(): number
  isEmpty(): boolean
}
```

### 3. Tests LIFO (45 min)

Push A,B,C → pop C,B,A; peek no modifica size; pop vacío; size tras N operaciones.

### 4. Ejercicio (70 min)

`src/exercises/balanced.ts`: `isBalanced(s: string): boolean` usando `Stack<string>`. Tests: `()`, `([]){}`, `([)]`, vacío, `(((`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): stack tipado"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Pila LIFO; aplicaciones (paréntesis, undo) | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/stack.ts` tipado con `push`/`pop`/`peek`/`isEmpty`; ≥4 tests verdes.
2. Un ejercicio (paréntesis o undo de 3 comandos) en `src/exercises/balanced.ts` o test dedicado.
3. Commit `feat(m07): stack tipado`.

## Errores comunes

- Exponer el array interno mutable.
- `pop` en vacío sin definir comportamiento (throw vs undefined).
- Implementar “pila” sin tests de LIFO.

## Siguiente

[L06 — Cola (Queue) y cola circular](L06-cola-queue-y-cola-circular.md)
