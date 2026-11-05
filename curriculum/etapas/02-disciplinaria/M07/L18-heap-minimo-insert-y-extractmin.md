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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entregar `MinHeap` completo con insert/extractMin/peek y
      tests de orden.


      Con el modelo listo, montas la estructura usable.
  - id: s2
    tipo: ejemplo
    titulo: 1. Clase MinHeap
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): minheap insert extractMin"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Heap mínimo: insert y extractMin" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: MinHeap operativo + tests
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

      `git commit -am "feat(m07): minheap insert extractMin"`
    comandoEsperado:
      - 'git commit -am "feat(m07): minheap insert extractMin"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m07): minheap insert extractMin"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Entregar `MinHeap` completo con insert/extractMin/peek y tests de
          orden.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tests
    xp: 10
    cuerpo: >-
      Insertar `{5,3,8,1}` → extract 1,3,5,8; peek no muta; extract vacío; 100
      random vs `[...].sort((a,b)=>a-b)`.
  - id: s7
    tipo: explicacion
    titulo: 3. Complejidad
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
