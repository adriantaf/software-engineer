---
id: L16
materia: M08
orden: 16
titulo: Problemas de grafos semana 4
horas: 5
semana: 4
lectura: 'Cierre semana grafos: +2 problemas en índice'
evidencia: problems/ +2 grafos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Consolidás la semana 4 con dos prácticas más y el índice al día.


      **Objetivo de esta lección:** Sumar dos problemas de grafos bien
      empaquetados y actualizar el índice.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Selección
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos
      git commit -m "feat(m08): problemas grafos semana 4"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Problema 1
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos
      git commit -m "feat(m08): problemas grafos semana 4"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Problemas de grafos semana 4», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Problemas de grafos
          semana 4
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

      `git add projects/m08-algoritmos`
    comandoEsperado:
      - git add projects/m08-algoritmos
      - 'git commit -m "feat(m08): problemas grafos semana 4"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m08-algoritmos'
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
          Sumar dos problemas de grafos bien empaquetados y actualizar el
          índice.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Problema 2
    xp: 10
    cuerpo: 'Igual. Si detectas ciclo, documenta complejidad.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        +2 problemas de grafos (además de L13–L15 si ya contaban, completa hasta
        tener evidencia clara de dos más o consolida carpetas).
      - '`indice-patrones.md` con filas bfs/dfs/camino.'
      - 'Commit `feat(m08): problemas grafos semana 4`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Problemas de grafos semana 4

**~5.0 h · Semana 4**

Consolidás la semana 4 con dos prácticas más y el índice al día.

## Objetivo

Sumar dos problemas de grafos bien empaquetados y actualizar el índice.

## Pasos

### 1. Selección (20 min)

Ideas: clone graph, course schedule (ciclo), flood fill, word ladder corto.

### 2. Problema 1 (80 min)

Plantilla completa + 3 tests.

### 3. Problema 2 (80 min)

Igual. Si detectas ciclo, documenta complejidad.

### 4. Índice + bitácora (30 min)

`bitacora/semana-04.md` opcional: qué patrón aún te cuesta.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): problemas grafos semana 4"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Práctica BFS/DFS adicional; índice ≥ entradas de grafos | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. **+2** problemas de grafos (además de L13–L15 si ya contaban, completa hasta tener evidencia clara de dos más o consolida carpetas).
2. `indice-patrones.md` con filas bfs/dfs/camino.
3. Commit `feat(m08): problemas grafos semana 4`.

## Errores comunes

- Reentregar el mismo archivo tres veces con otro nombre.
- Índice desactualizado.
- Tests flaky por orden de vecinos no determinista sin sort.

## Siguiente

[L17 — Memoización top-down](L17-memoizacion-top-down.md)
