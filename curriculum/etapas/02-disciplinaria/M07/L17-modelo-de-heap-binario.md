---
id: L17
materia: M07
orden: 17
titulo: Modelo de heap binario
horas: 5
semana: 5
lectura: 'Heap binario como array: índices padre/hijos'
evidencia: array-backed heap model + heapifyUp/Down
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Codificar el modelo (índices + heapify up/down) antes de la
      API insert/extractMin.


      El heap vive en un array: padre en `(i-1)>>1`, hijos `2i+1` y `2i+2`.
  - id: s2
    tipo: ejemplo
    titulo: 1. VisuAlgo + notas
    xp: 10
    cuerpo: |-
      ```ts
      export const parent = (i: number) => (i - 1) >> 1
      export const left = (i: number) => 2 * i + 1
      export const right = (i: number) => 2 * i + 2
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Modelo de heap binario" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: array-backed heap model + heapifyUp/Down
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
    pregunta: ¿Es buena práctica en esta lección? “Confundir índices 0-based y 1-based."
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
          Codificar el modelo (índices + heapify up/down) antes de la API
          insert/extractMin.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Helpers
    xp: 10
    cuerpo: |-
      `src/heap-model.ts`:

      ```ts
      export const parent = (i: number) => (i - 1) >> 1
      export const left = (i: number) => 2 * i + 1
      export const right = (i: number) => 2 * i + 2
      ```

      Tests de índices 0..10.
  - id: s7
    tipo: explicacion
    titulo: 3. heapifyUp / heapifyDown
    xp: 10
    cuerpo: >-
      Funciones que mutan `number[]` asumiendo min-heap. Casos de prueba: subir
      una hoja menor que el padre; bajar una raíz mayor que un hijo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Módulo con helpers `parent`/`left`/`right` y `heapifyUp`/`heapifyDown`
        sobre array.
      - Tests unitarios de índices y de un heapify sobre array casi-heap.
      - 'Commit `feat(m07): modelo heap binario`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L17 — Modelo de heap binario

**~5.0 h · Semana 5**

El heap vive en un array: padre en `(i-1)>>1`, hijos `2i+1` y `2i+2`.

## Objetivo

Codificar el modelo (índices + heapify up/down) antes de la API insert/extractMin.

## Pasos

### 1. VisuAlgo + notas (40 min)

Observa un min-heap. En `docs/heap.md` escribe la propiedad de heap y la forma completa de niveles.

### 2. Helpers (50 min)

`src/heap-model.ts`:

```ts
export const parent = (i: number) => (i - 1) >> 1
export const left = (i: number) => 2 * i + 1
export const right = (i: number) => 2 * i + 2
```

Tests de índices 0..10.

### 3. heapifyUp / heapifyDown (90 min)

Funciones que mutan `number[]` asumiendo min-heap. Casos de prueba: subir una hoja menor que el padre; bajar una raíz mayor que un hijo.

### 4. Diagrama array↔árbol (30 min)

En `docs/heap.md`, tabla índice→valor para un heap de ejemplo.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): modelo heap binario"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Heap shape + heap property; índices 2i+1 / 2i+2 | [VisuAlgo · Heap](https://visualgo.net/en/heap) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Módulo con helpers `parent`/`left`/`right` y `heapifyUp`/`heapifyDown` sobre array.
2. Tests unitarios de índices y de un heapify sobre array casi-heap.
3. Commit `feat(m07): modelo heap binario`.

## Errores comunes

- Confundir índices 0-based y 1-based.
- Heapify que no restaura la propiedad.
- Tratar el heap como BST ordenado inorder.

## Siguiente

[L18 — Heap mínimo: insert y extractMin](L18-heap-minimo-insert-y-extractmin.md)
