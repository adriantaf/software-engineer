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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar `DoublyLinkedList<T>` con borrado por valor y
      acceso indexado lineal (`at(i)`), documentando que el índice **no** es
      O(1).


      Con `prev` y `next` el borrado deja de ser un recorrido ciego desde `head`
      si ya tienes el nodo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura + sketch
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): lista doble e indexada"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Lista doble y operaciones indexadas" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: DoublyLinkedList + deleteByValue; tests de borde
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

      `git commit -am "feat(m07): lista doble e indexada"`
    comandoEsperado:
      - 'git commit -am "feat(m07): lista doble e indexada"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m07): lista doble e indexada"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar `DoublyLinkedList<T>` con borrado por valor y acceso
          indexado lineal (`at(i)`), documentando que el índice **no** es O(1).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: >-
      `src/doubly-linked-list.ts`: nodos con `prev`/`next`; `append`;
      `deleteByValue(v)` (o `delete(node)`); `at(i)` que recorre desde head (o
      desde el extremo más cercano si quieres bonus).
  - id: s7
    tipo: explicacion
    titulo: 3. Tests de borde
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
