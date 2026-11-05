---
id: L06
materia: M07
orden: 6
titulo: Cola (Queue) y cola circular
horas: 5
semana: 2
lectura: Colas FIFO; cola circular con buffer fijo
evidencia: Queue<T> + tests; opcional CircularQueue
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      FIFO alimenta BFS y buffers de trabajo. La cola circular evita
      desplazamientos en un buffer fijo.


      **Objetivo de esta lección:** Implementar `Queue<T>` correcta en costos y
      una `CircularQueue` de capacidad fija con política de overflow explícita.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Queue lineal
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): queue y cola circular"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Tests FIFO
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): queue y cola circular"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cola (Queue) y cola circular», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cola (Queue) y cola
          circular
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git commit -am "feat(m07): queue y cola circular"`
    comandoEsperado:
      - 'git commit -am "feat(m07): queue y cola circular"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m07): queue y cola circular"'
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
          Implementar `Queue<T>` correcta en costos y una `CircularQueue` de
          capacidad fija con política de overflow explícita.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: CircularQueue
    xp: 10
    cuerpo: >-
      `src/circular-queue.ts`: capacidad N; índices `head`/`tail` módulo N;
      distingue lleno vs vacío (`size` o slot sentinela). Overflow: throw o
      return false — elige y documéntalo en JSDoc.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`src/queue.ts` con `enqueue`/`dequeue`/`front` y ≥4 tests FIFO.'
      - >-
        `src/circular-queue.ts` (o sección en el mismo archivo) con capacidad
        fija y overflow definido.
      - 'Commit `feat(m07): queue y cola circular`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Cola (Queue) y cola circular

**~5.0 h · Semana 2**

FIFO alimenta BFS y buffers de trabajo. La cola circular evita desplazamientos en un buffer fijo.

## Objetivo

Implementar `Queue<T>` correcta en costos y una `CircularQueue` de capacidad fija con política de overflow explícita.

## Pasos

### 1. Queue lineal (70 min)

`src/queue.ts`: `enqueue`, `dequeue`, `front`/`peek`, `size`. Preferible lista con head/tail o índices sobre buffer — **no** `shift` silencioso O(n) sin nota.

### 2. Tests FIFO (40 min)

Orden de salida; vacía; un elemento; secuencia enqueue/dequeue intercalada.

### 3. CircularQueue (80 min)

`src/circular-queue.ts`: capacidad N; índices `head`/`tail` módulo N; distingue lleno vs vacío (`size` o slot sentinela). Overflow: throw o return false — elige y documéntalo en JSDoc.

### 4. Tests circulares (40 min)

Llenar hasta capacidad; overflow; vaciar tras wrap-around (enqueue que da la vuelta al buffer).

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): queue y cola circular"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Cola FIFO; buffer circular head/tail | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/queue.ts` con `enqueue`/`dequeue`/`front` y ≥4 tests FIFO.
2. `src/circular-queue.ts` (o sección en el mismo archivo) con capacidad fija y overflow definido.
3. Commit `feat(m07): queue y cola circular`.

## Errores comunes

- Usar `Array.shift` sin documentar O(n) (si lo usas, dilo y prefiere head index o lista).
- Circular: confundir “lleno” y “vacío” sin sentinel o size.
- Tests solo enqueue sin dequeue.

## Siguiente

[L07 — Deque y casos de uso](L07-deque-y-casos-de-uso.md)
