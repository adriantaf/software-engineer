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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El heap vive en un array: padre en `(i-1)>>1`, hijos `2i+1` y `2i+2`.


      **Objetivo de esta lección:** Codificar el modelo (índices + heapify
      up/down) antes de la API insert/extractMin.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: VisuAlgo + notas
    xp: 10
    cuerpo: |-
      ```ts
      export const parent = (i: number) => (i - 1) >> 1
      export const left = (i: number) => 2 * i + 1
      export const right = (i: number) => 2 * i + 2
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Helpers
    xp: 10
    cuerpo: |-
      ```ts
      export const parent = (i: number) => (i - 1) >> 1
      export const left = (i: number) => 2 * i + 1
      export const right = (i: number) => 2 * i + 2
      ```

      `src/heap-model.ts`: Tests de índices 0..10.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Modelo de heap binario», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Modelo de heap binario
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
    pregunta: ¿Es recomendable en esta lección? “Confundir índices 0-based y 1-based."
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
          Codificar el modelo (índices + heapify up/down) antes de la API
          insert/extractMin.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: heapifyUp / heapifyDown
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
