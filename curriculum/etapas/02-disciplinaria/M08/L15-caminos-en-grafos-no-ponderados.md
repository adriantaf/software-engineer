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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Calcular distancia (y camino) mínimo start→goal con BFS y
      parents.


      Con peso uniforme, BFS da el camino con menos aristas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Extiende BFS
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): camino minimo no ponderado BFS"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Caminos en grafos no ponderados" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: camino mínimo en aristas no peso
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

      `git commit -am "feat(m08): camino minimo no ponderado BFS"`
    comandoEsperado:
      - 'git commit -am "feat(m08): camino minimo no ponderado BFS"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): camino minimo no ponderado BFS"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Calcular distancia (y camino) mínimo start→goal con BFS y parents.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. API clara
    xp: 10
    cuerpo: >-
      `shortestPath(graph, start, goal): { dist: number, path: string[] } |
      null`
  - id: s7
    tipo: explicacion
    titulo: 3. Tests
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
