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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar `Queue<T>` correcta en costos y una
      `CircularQueue` de capacidad fija con política de overflow explícita.


      FIFO alimenta BFS y buffers de trabajo. La cola circular evita
      desplazamientos en un buffer fijo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Queue lineal
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): queue y cola circular"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cola (Queue) y cola circular" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: Queue<T> + tests; opcional CircularQueue
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git commit -am "feat(m07): queue y cola circular"`
    comandoEsperado:
      - 'git commit -am "feat(m07): queue y cola circular"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m07): queue y cola circular"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar `Queue<T>` correcta en costos y una `CircularQueue` de
          capacidad fija con política de overflow explícita.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tests FIFO
    xp: 10
    cuerpo: >-
      Orden de salida; vacía; un elemento; secuencia enqueue/dequeue
      intercalada.
  - id: s7
    tipo: explicacion
    titulo: 3. CircularQueue
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
