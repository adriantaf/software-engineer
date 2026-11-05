---
id: L02
materia: M07
orden: 2
titulo: Lista enlazada simple
horas: 5
semana: 1
lectura: 'Listas enlazadas singulares: head/tail, inserción y búsqueda'
evidencia: 'SinglyLinkedList con insert head/tail, find, 5 tests'
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Pasas de índices contiguos a nodos enlazados: trade-off memoria vs
      inserción en cabeza.


      **Objetivo de esta lección:** Implementar `SinglyLinkedList<T>` con
      `prepend`/`append`/`find` y contrastar costos con `DynamicArray` en
      `COMPLEJIDAD.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Dibuja antes de codificar
    xp: 10
    cuerpo: |-
      ```ts
      class Node<T> {
        constructor(public value: T, public next: Node<T> | null = null) {}
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Nodo y API
    xp: 10
    cuerpo: >-
      ```ts

      class Node<T> {
        constructor(public value: T, public next: Node<T> | null = null) {}
      }

      ```


      `src/singly-linked-list.ts`: Métodos: `prepend`, `append` (guarda `tail`
      si puedes), `find`, `get size`, `toArray()`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Lista enlazada simple», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Lista enlazada simple
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
      ¿Es recomendable en esta lección? “Perder la referencia a `head` al hacer
      `prepend`."
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
          Implementar `SinglyLinkedList<T>` con `prepend`/`append`/`find` y
          contrastar costos con `DynamicArray` en `COMPLEJIDAD.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Cinco tests
    xp: 10
    cuerpo: >-
      Vacía; prepend múltiple (orden LIFO en cabeza); append mantiene orden;
      `find` ausente; `toArray` coherente tras mezcla prepend/append.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `src/singly-linked-list.ts` con `prepend`, `append`, `find`, `toArray` y
        ≥5 tests verdes.
      - '`COMPLEJIDAD.md` compara inserción en cabeza lista vs array.'
      - 'Commit `feat(m07): lista enlazada simple`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Lista enlazada simple

**~5.0 h · Semana 1**

Pasas de índices contiguos a nodos enlazados: trade-off memoria vs inserción en cabeza.

## Objetivo

Implementar `SinglyLinkedList<T>` con `prepend`/`append`/`find` y contrastar costos con `DynamicArray` en `COMPLEJIDAD.md`.

## Pasos

### 1. Dibuja antes de codificar (20 min)

En papel o Mermaid: lista vacía → prepend A → append B → find C (ausente). Anota qué punteros cambian.

### 2. Nodo y API (70–80 min)

`src/singly-linked-list.ts`:

```ts
class Node<T> {
  constructor(public value: T, public next: Node<T> | null = null) {}
}
```

Métodos: `prepend`, `append` (guarda `tail` si puedes), `find`, `get size`, `toArray()`.

### 3. Cinco tests (60 min)

Vacía; prepend múltiple (orden LIFO en cabeza); append mantiene orden; `find` ausente; `toArray` coherente tras mezcla prepend/append.

```bash
cd projects/m07-estructuras && npm test
```

### 4. Comparación escrita (40 min)

Añade fila a `COMPLEJIDAD.md`: inserción O(1) en cabeza vs O(n) mover elementos en array; búsqueda O(n) en ambos.

### 5. Commit (15 min)

```bash
git add projects/m07-estructuras
git commit -m "feat(m07): lista enlazada simple"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Listas simples: nodos, head/tail, costos de insert/find | [VisuAlgo · Linked List](https://visualgo.net/en/list) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/singly-linked-list.ts` con `prepend`, `append`, `find`, `toArray` y ≥5 tests verdes.
2. `COMPLEJIDAD.md` compara inserción en cabeza lista vs array.
3. Commit `feat(m07): lista enlazada simple`.

## Errores comunes

- Perder la referencia a `head` al hacer `prepend`.
- `append` O(n²) sin `tail` y sin documentarlo.
- Tests que solo insertan y nunca buscan.

## Siguiente

[L03 — Lista doble y operaciones indexadas](L03-lista-doble-y-operaciones-indexadas.md)
