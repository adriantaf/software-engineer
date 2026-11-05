---
id: L03
materia: M07
orden: 3
titulo: Lista doble y operaciones indexadas
horas: 5
semana: 1
lectura: 'Listas dobles: prev/next, borrado e indexación lineal'
evidencia: DoublyLinkedList + deleteByValue; tests de borde
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Con `prev` y `next` el borrado deja de ser un recorrido ciego desde `head`
      si ya tienes el nodo.


      **Objetivo de esta lección:** Implementar `DoublyLinkedList<T>` con
      borrado por valor y acceso indexado lineal (`at(i)`), documentando que el
      índice **no** es O(1).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura + sketch
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): lista doble e indexada"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): lista doble e indexada"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Lista doble y operaciones indexadas», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Lista doble y
          operaciones indexadas
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

      `git commit -am "feat(m07): lista doble e indexada"`
    comandoEsperado:
      - 'git commit -am "feat(m07): lista doble e indexada"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m07): lista doble e indexada"'
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
          Implementar `DoublyLinkedList<T>` con borrado por valor y acceso
          indexado lineal (`at(i)`), documentando que el índice no es O(1).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests de borde
    xp: 10
    cuerpo: >-
      Borrar de lista vacía; borrar único nodo (head=tail=null); borrar cabeza;
      borrar cola; `at(-1)` / fuera de rango.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `src/doubly-linked-list.ts` con `append`, `deleteByValue` (o por nodo) y
        `at(i)` documentado O(n).
      - '≥5 tests: vacío, un nodo, borrar cabeza/cola/medio, índice inválido.'
      - 'Commit `feat(m07): lista doble e indexada`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L03 — Lista doble y operaciones indexadas

**~5.0 h · Semana 1**

Con `prev` y `next` el borrado deja de ser un recorrido ciego desde `head` si ya tienes el nodo.

## Objetivo

Implementar `DoublyLinkedList<T>` con borrado por valor y acceso indexado lineal (`at(i)`), documentando que el índice **no** es O(1).

## Pasos

### 1. Lectura + sketch (40 min)

Capítulo de listas dobles. Dibuja borrado de nodo intermedio (4 punteros).

### 2. Implementación (90 min)

`src/doubly-linked-list.ts`: nodos con `prev`/`next`; `append`; `deleteByValue(v)` (o `delete(node)`); `at(i)` que recorre desde head (o desde el extremo más cercano si quieres bonus).

### 3. Tests de borde (60 min)

Borrar de lista vacía; borrar único nodo (head=tail=null); borrar cabeza; borrar cola; `at(-1)` / fuera de rango.

### 4. Documenta indexación (30 min)

En `COMPLEJIDAD.md`: `at(i)` es O(n). Una frase: “si necesitas índice frecuente, usa array”.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): lista doble e indexada"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Listas doblemente enlazadas; borrado O(1) con nodo conocido | [VisuAlgo · Linked List](https://visualgo.net/en/list) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/doubly-linked-list.ts` con `append`, `deleteByValue` (o por nodo) y `at(i)` documentado O(n).
2. ≥5 tests: vacío, un nodo, borrar cabeza/cola/medio, índice inválido.
3. Commit `feat(m07): lista doble e indexada`.

## Errores comunes

- Olvidar actualizar `prev` al borrar.
- Prometer acceso O(1) por índice en lista enlazada.
- Dejar `tail` huérfano tras borrar el último.

## Siguiente

[L04 — Secuencias: repaso de costos y cierre semana 1](L04-secuencias-repaso-de-costos-y-cierre-semana-1.md)
