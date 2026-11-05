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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar un BST de números (o `T` comparable) con
      `insert` y `contains`, más tests que demuestren el orden.


      P2 empieza con el invariante: izquierda < nodo < derecha.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura + VisuAlgo
    xp: 10
    cuerpo: >-
      ```ts

      class BstNode { left: BstNode | null; right: BstNode | null;
      constructor(public key: number) {} }

      export class BST { insert(key: number): void; contains(key: number):
      boolean }

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "BST: inserción y búsqueda" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: BST insert/contains + tests ordenados
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
      ¿Es buena práctica en esta lección? “Insertar sin respetar orden (rompe
      invariante)."
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
          Implementar un BST de números (o `T` comparable) con `insert` y
          `contains`, más tests que demuestren el orden.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Nodos e insert
    xp: 10
    cuerpo: >-
      `src/bst.ts`:


      ```ts

      class BstNode { left: BstNode | null; right: BstNode | null;
      constructor(public key: number) {} }

      export class BST { insert(key: number): void; contains(key: number):
      boolean }

      ```


      Define política de duplicados en un comentario de una línea.
  - id: s7
    tipo: explicacion
    titulo: 3. Tests
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
