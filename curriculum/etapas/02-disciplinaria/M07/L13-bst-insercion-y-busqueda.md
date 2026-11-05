---
id: L13
materia: M07
orden: 13
titulo: 'BST: inserción y búsqueda'
horas: 5
semana: 4
lectura: 'Árboles binarios de búsqueda: invariante e insert/contains'
evidencia: BST insert/contains + tests ordenados
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2 empieza con el invariante: izquierda < nodo < derecha.


      **Objetivo de esta lección:** Implementar un BST de números (o `T`
      comparable) con `insert` y `contains`, más tests que demuestren el orden.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura + VisuAlgo
    xp: 10
    cuerpo: >-
      ```ts

      class BstNode { left: BstNode | null; right: BstNode | null;
      constructor(public key: number) {} }

      export class BST { insert(key: number): void; contains(key: number):
      boolean }

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Nodos e insert
    xp: 10
    cuerpo: >-
      ```ts

      class BstNode { left: BstNode | null; right: BstNode | null;
      constructor(public key: number) {} }

      export class BST { insert(key: number): void; contains(key: number):
      boolean }

      ```


      `src/bst.ts`: Define política de duplicados en un comentario de una línea.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «BST: inserción y búsqueda», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de BST: inserción y
          búsqueda
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
      ¿Es recomendable en esta lección? “Insertar sin respetar orden (rompe
      invariante)."
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
          Implementar un BST de números (o `T` comparable) con `insert` y
          `contains`, más tests que demuestren el orden.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests
    xp: 10
    cuerpo: >-
      Vacío contains false; insert uno; secuencia 8,3,10,1,6 contains todos;
      ausente; duplicado según política.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`src/bst.ts` con `insert` y `contains` respetando invariante BST.'
      - >-
        ≥5 tests (vacío, cadena ordenada, duplicado definido, contains
        true/false).
      - 'Commit `feat(m07): bst insert y contains`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — BST: inserción y búsqueda

**~5.0 h · Semana 4**

P2 empieza con el invariante: izquierda < nodo < derecha.

## Objetivo

Implementar un BST de números (o `T` comparable) con `insert` y `contains`, más tests que demuestren el orden.

## Pasos

### 1. Lectura + VisuAlgo (40 min)

Inserta la secuencia 8,3,10,1,6 en VisuAlgo BST. Copia el dibujo a `docs/bst-semana4.md`.

### 2. Nodos e insert (90 min)

`src/bst.ts`:

```ts
class BstNode { left: BstNode | null; right: BstNode | null; constructor(public key: number) {} }
export class BST { insert(key: number): void; contains(key: number): boolean }
```

Define política de duplicados en un comentario de una línea.

### 3. Tests (60 min)

Vacío contains false; insert uno; secuencia 8,3,10,1,6 contains todos; ausente; duplicado según política.

### 4. Complejidad (20 min)

`COMPLEJIDAD.md`: O(h) con h altura; peor caso cadena O(n).

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): bst insert y contains"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | BST: hijo izq < nodo < der; insert y search | [VisuAlgo · BST](https://visualgo.net/en/bst) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/bst.ts` con `insert` y `contains` respetando invariante BST.
2. ≥5 tests (vacío, cadena ordenada, duplicado definido, contains true/false).
3. Commit `feat(m07): bst insert y contains`.

## Errores comunes

- Insertar sin respetar orden (rompe invariante).
- Duplicados silenciosos sin política (ignorar / contar / throw).
- Confundir BST con heap.

## Siguiente

[L14 — Recorridos inorder, preorder, postorder](L14-recorridos-inorder-preorder-postorder.md)
