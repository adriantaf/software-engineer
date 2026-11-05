---
id: L05
materia: M07
orden: 5
titulo: Pila (Stack) tipada
horas: 5
semana: 2
lectura: 'Pilas LIFO: push, pop, peek e invariantes'
evidencia: Stack<T> con push/pop/peek + 4 tests (inicio P1)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entregar `Stack<T>` con API mínima, tests LIFO y un caso de
      uso (paréntesis balanceados o undo).


      LIFO es la base de undo, parsers y DFS. Hoy la implementas tipada y la
      usas en un ejercicio corto.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```ts
      export class Stack<T> {
        push(x: T): void
        pop(): T          // o T | undefined — documenta
        peek(): T
        get size(): number
        isEmpty(): boolean
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Pila (Stack) tipada" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: Stack<T> con push/pop/peek + 4 tests (inicio P1)
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “Exponer el array interno mutable."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Entregar `Stack<T>` con API mínima, tests LIFO y un caso de uso
          (paréntesis balanceados o undo).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: >-
      `src/stack.ts` — puedes basarte en array **privado** o en tu lista; no
      reexportes mutadores internos.


      ```ts

      export class Stack<T> {
        push(x: T): void
        pop(): T          // o T | undefined — documenta
        peek(): T
        get size(): number
        isEmpty(): boolean
      }

      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Tests LIFO
    xp: 10
    cuerpo: >-
      Push A,B,C → pop C,B,A; peek no modifica size; pop vacío; size tras N
      operaciones.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `src/stack.ts` tipado con `push`/`pop`/`peek`/`isEmpty`; ≥4 tests
        verdes.
      - >-
        Un ejercicio (paréntesis o undo de 3 comandos) en
        `src/exercises/balanced.ts` o test dedicado.
      - 'Commit `feat(m07): stack tipado`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
