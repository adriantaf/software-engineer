---
id: L05
materia: M07
orden: 5
titulo: Pila (Stack) tipada
horas: 5.0
semana: 2
lectura: "ED: pilas LIFO, aplicaciones (paréntesis, undo)"
evidencia: "Stack<T> con push/pop/peek + 4 tests (inicio P1)"
---

# L05 — Pila (Stack) tipada

**~5.0 h · Semana 2**

La pila es la interfaz LIFO: implementación sobre array o lista, pero API propia.

## Objetivo

Implementar pila genérica con tests y documentar O(1) en operaciones core.

## Pasos

### 1. API (60 min)

`push`, `pop`, `peek`, `size`, `isEmpty`. Decide: `pop` en vacío lanza error tipado.

### 2. Tests (75 min)

LIFO orden, pop vacío, peek no muta, muchos pushes.

### 3. Aplicación mini (60 min)

`balanceParentesis(s: string): boolean` usando tu pila.

### 4. Lectura (45 min)

Capítulo pilas.

### 5. Commit (30 min)

`feat(m07): stack tipado`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Ver ficha | Capítulo de la semana |

## Hecho cuando

1. Stack con 4+ tests.
2. Ejercicio paréntesis funcionando.
3. Big-O en COMPLEJIDAD.

## Errores comunes

- Exponer array interno mutable.
- `peek` que hace pop por error.
## Siguiente

[L06 — Cola (Queue) y cola circular](L06-cola-queue-y-cola-circular.md)
