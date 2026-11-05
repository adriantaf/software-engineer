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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar trade-offs heap vs BST para prioridades y dejar
      una decisión escrita de diseño.


      No todo “ordenado” necesita un árbol. Hoy eliges con tabla, no con
      intuición.
  - id: s2
    tipo: ejemplo
    titulo: 1. Tabla de operaciones
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m07): heap vs bst prioridades"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Heap vs BST para prioridades" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: COMPLEJIDAD heap vs BST
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

      `git commit -am "docs(m07): heap vs bst prioridades"`
    comandoEsperado:
      - 'git commit -am "docs(m07): heap vs bst prioridades"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "docs(m07): heap vs bst prioridades"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Documentar trade-offs heap vs BST para prioridades y dejar una
          decisión escrita de diseño.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Experimento mental / microbench
    xp: 10
    cuerpo: >-
      Inserta N=10_000 prioridades y extrae N/2. Compara tu heap vs extraer min
      de un BST (si tienes min). Anota tiempos en la doc.
  - id: s7
    tipo: explicacion
    titulo: 3. Decisión
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
