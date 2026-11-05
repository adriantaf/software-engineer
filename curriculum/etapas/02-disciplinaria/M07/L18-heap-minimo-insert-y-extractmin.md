---
id: L18
materia: M07
orden: 18
titulo: 'Heap mínimo: insert y extractMin'
horas: 5
semana: 5
lectura: Operaciones insert y extract-min en heap
evidencia: MinHeap operativo + tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Con el modelo listo, montas la estructura usable.


      **Objetivo de esta lección:** Entregar `MinHeap` completo con
      insert/extractMin/peek y tests de orden.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Clase MinHeap
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): minheap insert extractMin"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Tests
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): minheap insert extractMin"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Heap mínimo: insert y extractMin», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Heap mínimo: insert y
          extractMin
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

      `git commit -am "feat(m07): minheap insert extractMin"`
    comandoEsperado:
      - 'git commit -am "feat(m07): minheap insert extractMin"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m07): minheap insert extractMin"'
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
          Entregar `MinHeap` completo con insert/extractMin/peek y tests de
          orden.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Complejidad
    xp: 10
    cuerpo: Filas en `COMPLEJIDAD.md` para heap.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`src/min-heap.ts` con `insert`, `extractMin`, `peek`, `size`.'
      - >-
        ≥5 tests: orden de extracción, vacío, un elemento, secuencia aleatoria
        vs sort.
      - 'Commit `feat(m07): minheap insert extractMin`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L18 — Heap mínimo: insert y extractMin

**~5.0 h · Semana 5**

Con el modelo listo, montas la estructura usable.

## Objetivo

Entregar `MinHeap` completo con insert/extractMin/peek y tests de orden.

## Pasos

### 1. Clase MinHeap (90 min)

`src/min-heap.ts` usa `heap-model.ts`. `insert`: push + heapifyUp. `extractMin`: swap root/último, pop, heapifyDown.

### 2. Tests (70 min)

Insertar `{5,3,8,1}` → extract 1,3,5,8; peek no muta; extract vacío; 100 random vs `[...].sort((a,b)=>a-b)`.

### 3. Complejidad (30 min)

Filas en `COMPLEJIDAD.md` para heap.

### 4. Export (20 min)

Reexporta desde `src/index.ts`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): minheap insert extractMin"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | insert O(log n); extractMin O(log n); peek O(1) | [VisuAlgo · Heap](https://visualgo.net/en/heap) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/min-heap.ts` con `insert`, `extractMin`, `peek`, `size`.
2. ≥5 tests: orden de extracción, vacío, un elemento, secuencia aleatoria vs sort.
3. Commit `feat(m07): minheap insert extractMin`.

## Errores comunes

- extractMin sin heapifyDown.
- Insert solo con `push` al array sin subir.
- Tests que no verifican orden de salida.

## Siguiente

[L19 — Cola de prioridad](L19-cola-de-prioridad.md)
