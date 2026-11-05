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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar `SinglyLinkedList<T>` con
      `prepend`/`append`/`find` y contrastar costos con `DynamicArray` en
      `COMPLEJIDAD.md`.


      Pasas de índices contiguos a nodos enlazados: trade-off memoria vs
      inserción en cabeza.
  - id: s2
    tipo: ejemplo
    titulo: 1. Dibuja antes de codificar
    xp: 10
    cuerpo: |-
      ```ts
      class Node<T> {
        constructor(public value: T, public next: Node<T> | null = null) {}
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Lista enlazada simple" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: 'SinglyLinkedList con insert head/tail, find, 5 tests'
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
      ¿Es buena práctica en esta lección? “Perder la referencia a `head` al
      hacer `prepend`."
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
          Implementar `SinglyLinkedList<T>` con `prepend`/`append`/`find` y
          contrastar costos con `DynamicArray` en `COMPLEJIDAD.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Nodo y API
    xp: 10
    cuerpo: >-
      `src/singly-linked-list.ts`:


      ```ts

      class Node<T> {
        constructor(public value: T, public next: Node<T> | null = null) {}
      }

      ```


      Métodos: `prepend`, `append` (guarda `tail` si puedes), `find`, `get
      size`, `toArray()`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Cinco tests
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m07-estructuras && npm test
      ```
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
