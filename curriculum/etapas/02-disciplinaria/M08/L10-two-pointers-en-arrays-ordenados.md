---
id: L10
materia: M08
orden: 10
titulo: Two pointers en arrays ordenados
horas: 5
semana: 3
lectura: Two pointers / left-right en secuencias ordenadas
evidencia: 2 problemas two pointers
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Con orden, left/right reemplazan búsquedas anidadas.


      **Objetivo de esta lección:** Entregar dos soluciones two-pointers bien
      testeadas e indexadas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Patrón en papel
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): two pointers arrays ordenados"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Problema A — pair sum
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): two pointers arrays ordenados"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Two pointers en arrays ordenados», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Two pointers en arrays
          ordenados
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

      `git commit -am "feat(m08): two pointers arrays ordenados"`
    comandoEsperado:
      - 'git commit -am "feat(m08): two pointers arrays ordenados"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): two pointers arrays ordenados"'
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
        texto: Entregar dos soluciones two-pointers bien testeadas e indexadas.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Problema B
    xp: 10
    cuerpo: >-
      Ej. contenedor de agua, squaring sorted array, merge dos ordenados
      in-place conceptual. Misma plantilla.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Dos problemas two-pointers con arrays ordenados (o justificación de por
        qué ordenas antes).
      - Complejidad O(n) tras ordenar si aplica — dilo explícito.
      - 'Commit `feat(m08): two pointers arrays ordenados`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Two pointers en arrays ordenados

**~5.0 h · Semana 3**

Con orden, left/right reemplazan búsquedas anidadas.

## Objetivo

Entregar dos soluciones two-pointers bien testeadas e indexadas.

## Pasos

### 1. Patrón en papel (25 min)

Dibuja pair-sum = target en array ordenado. Anota cuándo mueves left vs right.

### 2. Problema A — pair sum (60 min)

`problems/…-pair-sum/`. Tests: hay par, no hay, duplicados, negativos.

### 3. Problema B (70 min)

Ej. contenedor de agua, squaring sorted array, merge dos ordenados in-place conceptual. Misma plantilla.

### 4. Índice + nota (30 min)

Compara con hash two-sum: trade-off ordenar+O(n) vs hash O(n) promedio.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): two pointers arrays ordenados"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Punteros extremos; pair sum en array ordenado | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Dos problemas two-pointers con arrays ordenados (o justificación de por qué ordenas antes).
2. Complejidad O(n) tras ordenar si aplica — dilo explícito.
3. Commit `feat(m08): two pointers arrays ordenados`.

## Errores comunes

- Two pointers en no ordenado sin ordenar ni justificar.
- Índices que se cruzan mal (loop infinito).
- No cubrir caso sin solución.

## Siguiente

[L11 — Sliding window](L11-sliding-window.md)
