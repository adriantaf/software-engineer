---
id: L13
materia: M08
orden: 13
titulo: BFS repaso y cola
horas: 5
semana: 4
lectura: BFS sobre grafos / grids con cola
evidencia: 1 problema BFS + grafo test
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      BFS explora por capas; la cola es obligatoria.


      **Objetivo de esta lección:** Implementar BFS reutilizable y resolver un
      problema con evidencia P1.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Grafo de prueba
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): bfs con cola"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`bfs(start)`'
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): bfs con cola"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «BFS repaso y cola», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de BFS repaso y cola
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

      `git commit -am "feat(m08): bfs con cola"`
    comandoEsperado:
      - 'git commit -am "feat(m08): bfs con cola"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): bfs con cola"'
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
        texto: Implementar BFS reutilizable y resolver un problema con evidencia P1.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Problema
    xp: 10
    cuerpo: >-
      Ej. número de islas (grid), shortest path en grid sin pesos, o “grados de
      separación”. Carpeta en `problems/`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Utilidad de grafo o grid + `bfs` que retorna orden de visita o
        distancias.
      - Un problema en `problems/` resuelto con BFS + ≥3 tests.
      - 'Commit `feat(m08): bfs con cola`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — BFS repaso y cola

**~5.0 h · Semana 4**

BFS explora por capas; la cola es obligatoria.

## Objetivo

Implementar BFS reutilizable y resolver un problema con evidencia P1.

## Pasos

### 1. Grafo de prueba (40 min)

`src/graph.ts` (lista de adyacencia) o reusa el de M07 copiando lo mínimo. Tests de vecinos.

### 2. `bfs(start)` (70 min)

Cola + set visitados; opcional mapa `dist`. Complejidad O(V+E) en análisis corto `docs/bfs.md`.

### 3. Problema (70 min)

Ej. número de islas (grid), shortest path en grid sin pesos, o “grados de separación”. Carpeta en `problems/`.

### 4. Índice (20 min)

Patrón `bfs`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): bfs con cola"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | BFS: cola, visitados, capas O(V+E) | [VisuAlgo · BFS](https://visualgo.net/en/dfsbfs) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Utilidad de grafo o grid + `bfs` que retorna orden de visita o distancias.
2. Un problema en `problems/` resuelto con BFS + ≥3 tests.
3. Commit `feat(m08): bfs con cola`.

## Errores comunes

- BFS con stack (eso es DFS).
- No marcar visitados → loops.
- Complejidad sin hablar de V y E.

## Siguiente

[L14 — DFS y componentes](L14-dfs-y-componentes.md)
