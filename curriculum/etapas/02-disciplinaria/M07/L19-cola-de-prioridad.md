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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Envolver el MinHeap en `PriorityQueue<T>` con tres casos de
      uso testeados.


      La PQ es la fachada del heap para el dominio (turnos, jobs, eventos).
  - id: s2
    tipo: ejemplo
    titulo: 1. API
    xp: 10
    cuerpo: |-
      ```ts
      enqueue(item: T, priority: number): void
      dequeue(): T
      peek(): T
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Cola de prioridad" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: PriorityQueue API + 3 casos
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “PQ que es solo un array sorted en
      cada insert sin decir O(n)."
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
          Envolver el MinHeap en `PriorityQueue<T>` con tres casos de uso
          testeados.
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
      Guarda `{ item, priority }` en el heap; compara por priority (tie-break
      opcional por orden de llegada).
  - id: s7
    tipo: explicacion
    titulo: 3. Tres casos
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
