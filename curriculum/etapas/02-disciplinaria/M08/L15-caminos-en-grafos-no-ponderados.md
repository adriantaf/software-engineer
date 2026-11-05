---
id: L15
materia: M08
orden: 15
titulo: Caminos en grafos no ponderados
horas: 5
semana: 4
lectura: Camino más corto en aristas unitarias = BFS
evidencia: camino mínimo en aristas no peso
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Con peso uniforme, BFS da el camino con menos aristas.


      **Objetivo de esta lección:** Calcular distancia (y camino) mínimo
      start→goal con BFS y parents.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Extiende BFS
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): camino minimo no ponderado BFS"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: API clara
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): camino minimo no ponderado BFS"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Caminos en grafos no ponderados», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Caminos en grafos no
          ponderados
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

      `git commit -am "feat(m08): camino minimo no ponderado BFS"`
    comandoEsperado:
      - 'git commit -am "feat(m08): camino minimo no ponderado BFS"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): camino minimo no ponderado BFS"'
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
        texto: Calcular distancia (y camino) mínimo start→goal con BFS y parents.
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
    cuerpo: >-
      Camino simple; sin camino; start=goal dist 0; grafo con ciclo no se
      cuelga.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Función que devuelve distancia y/o camino start→goal en grafo no
        ponderado.
      - 'Tests: alcanzable, inalcanzable, start=goal.'
      - 'Commit `feat(m08): camino minimo no ponderado BFS`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Caminos en grafos no ponderados

**~5.0 h · Semana 4**

Con peso uniforme, BFS da el camino con menos aristas.

## Objetivo

Calcular distancia (y camino) mínimo start→goal con BFS y parents.

## Pasos

### 1. Extiende BFS (60 min)

Guarda `parent` o `prev`. Al llegar a goal, reconstruye lista invirtiendo.

### 2. API clara (40 min)

`shortestPath(graph, start, goal): { dist: number, path: string[] } | null`

### 3. Tests (50 min)

Camino simple; sin camino; start=goal dist 0; grafo con ciclo no se cuelga.

### 4. Problema / doc (40 min)

Enunciado tipo “mínimas citas de referencias entre clientes” (grafo demo) en `problems/` o `docs/`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): camino minimo no ponderado BFS"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | BFS distancias; reconstruir camino con parent[] | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Función que devuelve distancia y/o camino start→goal en grafo no ponderado.
2. Tests: alcanzable, inalcanzable, start=goal.
3. Commit `feat(m08): camino minimo no ponderado BFS`.

## Errores comunes

- Usar Dijkstra “porque sí” en grafos unitarios sin justificar.
- No reconstruir camino cuando se pide.
- Distancia mal inicializada (0 vs Infinity).

## Siguiente

[L16 — Problemas de grafos semana 4](L16-problemas-de-grafos-semana-4.md)
