---
id: L20
materia: M07
orden: 20
titulo: Heap vs BST para prioridades
horas: 5
semana: 5
lectura: Trade-offs heap vs BST para colas de prioridad
evidencia: COMPLEJIDAD heap vs BST
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      No todo “ordenado” necesita un árbol. Hoy eliges con tabla, no con
      intuición.


      **Objetivo de esta lección:** Documentar trade-offs heap vs BST para
      prioridades y dejar una decisión escrita de diseño.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tabla de operaciones
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m07): heap vs bst prioridades"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Experimento mental / microbench
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m07): heap vs bst prioridades"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Heap vs BST para prioridades», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Heap vs BST para
          prioridades
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

      `git commit -am "docs(m07): heap vs bst prioridades"`
    comandoEsperado:
      - 'git commit -am "docs(m07): heap vs bst prioridades"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "docs(m07): heap vs bst prioridades"'
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
          Documentar trade-offs heap vs BST para prioridades y dejar una
          decisión escrita de diseño.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Decisión
    xp: 10
    cuerpo: >-
      `docs/heap-vs-bst.md`: párrafo “En Agenda Ops para cola VIP usaría ___
      porque ___”.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Sección en `COMPLEJIDAD.md` o `docs/heap-vs-bst.md` con tabla de ops.
      - Bitácora semana 5 con una decisión (“para scheduler usaría…”).
      - 'Commit `docs(m07): heap vs bst prioridades`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Heap vs BST para prioridades

**~5.0 h · Semana 5**

No todo “ordenado” necesita un árbol. Hoy eliges con tabla, no con intuición.

## Objetivo

Documentar trade-offs heap vs BST para prioridades y dejar una decisión escrita de diseño.

## Pasos

### 1. Tabla de operaciones (60 min)

Filas: insert, find-min, extract-min, delete arbitrario, sorted iterate. Columnas: MinHeap, BST, `Map`+sort (referencia).

### 2. Experimento mental / microbench (70 min)

Inserta N=10_000 prioridades y extrae N/2. Compara tu heap vs extraer min de un BST (si tienes min). Anota tiempos en la doc.

### 3. Decisión (40 min)

`docs/heap-vs-bst.md`: párrafo “En Agenda Ops para cola VIP usaría ___ porque ___”.

### 4. Bitácora (30 min)

`bitacora/semana-05.md`.

### 5. Commit (15 min)

```bash
git commit -am "docs(m07): heap vs bst prioridades"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Heap: mejor extract-min; BST: ordered scan / delete arbitrario | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Sección en `COMPLEJIDAD.md` o `docs/heap-vs-bst.md` con tabla de ops.
2. Bitácora semana 5 con una decisión (“para scheduler usaría…”).
3. Commit `docs(m07): heap vs bst prioridades`.

## Errores comunes

- Decir que BST siempre es O(log n) sin hablar del peor caso degenerado.
- Afirmar que heap permite search arbitrario O(log n).
- Tabla sin ops concretas (insert/extract/search).

## Siguiente

[L21 — Grafos: repaso y representación](L21-grafos-repaso-y-representacion.md)
