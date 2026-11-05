---
id: L19
materia: M07
orden: 19
titulo: Cola de prioridad
horas: 5
semana: 5
lectura: Priority queue sobre heap; API de tareas
evidencia: PriorityQueue API + 3 casos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La PQ es la fachada del heap para el dominio (turnos, jobs, eventos).


      **Objetivo de esta lección:** Envolver el MinHeap en `PriorityQueue<T>`
      con tres casos de uso testeados.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: API
    xp: 10
    cuerpo: |-
      ```ts
      enqueue(item: T, priority: number): void
      dequeue(): T
      peek(): T
      ```

      Menor `priority` sale primero (documenta si inviertes).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): priority queue"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cola de prioridad», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Cola de prioridad
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “PQ que es solo un array sorted en cada
      insert sin decir O(n)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Envolver el MinHeap en `PriorityQueue<T>` con tres casos de uso
          testeados.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tres casos
    xp: 10
    cuerpo: >-
      Tests: (1) turnos `{cliente, prioridad}`; (2) vaciar cola; (3) mismas
      prioridades — orden estable o documentado.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`src/priority-queue.ts` genérica (prioridad numérica o comparator).'
      - >-
        Tres casos de prueba de dominio (p. ej. turnos Agenda Ops: urgente <
        normal).
      - 'Commit `feat(m07): priority queue`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L19 — Cola de prioridad

**~5.0 h · Semana 5**

La PQ es la fachada del heap para el dominio (turnos, jobs, eventos).

## Objetivo

Envolver el MinHeap en `PriorityQueue<T>` con tres casos de uso testeados.

## Pasos

### 1. API (30 min)

```ts
enqueue(item: T, priority: number): void
dequeue(): T
peek(): T
```

Menor `priority` sale primero (documenta si inviertes).

### 2. Implementación (70 min)

Guarda `{ item, priority }` en el heap; compara por priority (tie-break opcional por orden de llegada).

### 3. Tres casos (70 min)

Tests: (1) turnos `{cliente, prioridad}`; (2) vaciar cola; (3) mismas prioridades — orden estable o documentado.

### 4. Nota de producto (30 min)

En README: cómo Agenda Ops usaría PQ para “siguiente en cola VIP”.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): priority queue"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | PQ: enqueue con prioridad, dequeue del mínimo/máximo | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/priority-queue.ts` genérica (prioridad numérica o comparator).
2. Tres casos de prueba de dominio (p. ej. turnos Agenda Ops: urgente < normal).
3. Commit `feat(m07): priority queue`.

## Errores comunes

- PQ que es solo un array sorted en cada insert sin decir O(n).
- Prioridades invertidas sin documentar (min vs max).
- Casos de prueba sin prioridades distintas.

## Siguiente

[L20 — Heap vs BST para prioridades](L20-heap-vs-bst-para-prioridades.md)
