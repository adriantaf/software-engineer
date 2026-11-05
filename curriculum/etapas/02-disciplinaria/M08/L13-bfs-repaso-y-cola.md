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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar BFS reutilizable y resolver un problema con
      evidencia P1.


      BFS explora por capas; la cola es obligatoria.
  - id: s2
    tipo: ejemplo
    titulo: 1. Grafo de prueba
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): bfs con cola"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "BFS repaso y cola" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: 1 problema BFS + grafo test
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

      `git commit -am "feat(m08): bfs con cola"`
    comandoEsperado:
      - 'git commit -am "feat(m08): bfs con cola"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): bfs con cola"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Implementar BFS reutilizable y resolver un problema con evidencia P1.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `bfs(start)`
    xp: 10
    cuerpo: >-
      Cola + set visitados; opcional mapa `dist`. Complejidad O(V+E) en análisis
      corto `docs/bfs.md`.
  - id: s7
    tipo: explicacion
    titulo: 3. Problema
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
