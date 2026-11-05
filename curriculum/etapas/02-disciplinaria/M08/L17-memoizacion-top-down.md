---
id: L17
materia: M08
orden: 17
titulo: Memoización top-down
horas: 5
semana: 5
lectura: CLRS DP intro — top-down con memo
evidencia: dp/memo-ejemplo.ts
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      DP empieza viendo subproblemas solapados: fibonacci es el laboratorio.


      **Objetivo de esta lección:** Implementar una solución top-down con memo y
      demostrar el ahorro de llamadas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/dp
      git commit -m "feat(m08): memoizacion top-down"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Fib (u otro) naive vs memo
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/dp
      git commit -m "feat(m08): memoizacion top-down"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Memoización top-down», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Memoización top-down
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

      `git add projects/m08-algoritmos/dp`
    comandoEsperado:
      - git add projects/m08-algoritmos/dp
      - 'git commit -m "feat(m08): memoizacion top-down"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m08-algoritmos/dp'
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
          Implementar una solución top-down con memo y demostrar el ahorro de
          llamadas.
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
    cuerpo: fib(0..10) conocidos; n=40 memo termina en ms.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `dp/memo-ejemplo.ts` (fib o paths) con y sin memo, o contador de
        llamadas.
      - >-
        Tests de valores conocidos; nota de complejidad en `dp/README.md`
        borrador.
      - 'Commit `feat(m08): memoizacion top-down`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L17 — Memoización top-down

**~5.0 h · Semana 5**

DP empieza viendo subproblemas solapados: fibonacci es el laboratorio.

## Objetivo

Implementar una solución top-down con memo y demostrar el ahorro de llamadas.

## Pasos

### 1. Lectura (40 min)

CLRS intro DP: overlapping subproblems + optimal substructure. Anota en `dp/README.md`.

### 2. Fib (u otro) naive vs memo (70 min)

`dp/memo-ejemplo.ts`: versión ingenua (solo para n pequeño) y `fibMemo` con `Map`/`array`. Contador de llamadas.

### 3. Tests (40 min)

fib(0..10) conocidos; n=40 memo termina en ms.

### 4. Definición de estado (40 min)

Escribe: estado = `__`, transición = `__`, base = `__`.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/dp
git commit -m "feat(m08): memoizacion top-down"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Recursión + mapa memo; overlapping subproblems | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `dp/memo-ejemplo.ts` (fib o paths) con y sin memo, o contador de llamadas.
2. Tests de valores conocidos; nota de complejidad en `dp/README.md` borrador.
3. Commit `feat(m08): memoizacion top-down`.

## Errores comunes

- Memoizar sin clave correcta (olvidar argumentos).
- Creer que memo cambia la respuesta (solo el tiempo).
- Sin caso base.

## Siguiente

[L18 — Programación dinámica bottom-up](L18-programacion-dinamica-bottom-up.md)
