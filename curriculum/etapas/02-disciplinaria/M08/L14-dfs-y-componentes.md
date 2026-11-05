---
id: L14
materia: M08
orden: 14
titulo: DFS y componentes
horas: 5
semana: 4
lectura: DFS y componentes conexas
evidencia: problema componentes conexas
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Contar componentes conexas (o resolver problema equivalente)
      con DFS y tests.


      DFS recorre profundo; sirve para marcar componentes y ciclos
      introductorios.
  - id: s2
    tipo: ejemplo
    titulo: 1. DFS base
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): dfs componentes conexas"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "DFS y componentes" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: problema componentes conexas
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

      `git commit -am "feat(m08): dfs componentes conexas"`
    comandoEsperado:
      - 'git commit -am "feat(m08): dfs componentes conexas"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): dfs componentes conexas"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Contar componentes conexas (o resolver problema equivalente) con DFS y
          tests.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Componentes
    xp: 10
    cuerpo: >-
      Algoritmo: para cada vértice no visitado, DFS y ++count. Tests con 1
      componente, 3 componentes, grafo vacío.
  - id: s7
    tipo: explicacion
    titulo: 3. Problema empaquetado
    xp: 10
    cuerpo: '`problems/…-componentes/` con enunciado de red social / salas conectadas.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`connectedComponents(graph)` (o problema equivalente) con tests.'
      - Documentas recursivo vs stack explícito en 5–8 líneas.
      - 'Commit `feat(m08): dfs componentes conexas`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L14 — DFS y componentes

**~5.0 h · Semana 4**

DFS recorre profundo; sirve para marcar componentes y ciclos introductorios.

## Objetivo

Contar componentes conexas (o resolver problema equivalente) con DFS y tests.

## Pasos

### 1. DFS base (50 min)

`dfs(v, visited)` recursivo. Versión iterativa opcional.

### 2. Componentes (70 min)

Algoritmo: para cada vértice no visitado, DFS y ++count. Tests con 1 componente, 3 componentes, grafo vacío.

### 3. Problema empaquetado (60 min)

`problems/…-componentes/` con enunciado de red social / salas conectadas.

### 4. Índice (20 min)

Patrón `dfs`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): dfs componentes conexas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | DFS recursivo/iterativo; contar componentes | [VisuAlgo · DFS](https://visualgo.net/en/dfsbfs) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `connectedComponents(graph)` (o problema equivalente) con tests.
2. Documentas recursivo vs stack explícito en 5–8 líneas.
3. Commit `feat(m08): dfs componentes conexas`.

## Errores comunes

- Contar nodos en vez de componentes.
- No resetear visitados entre componentes.
- Stack overflow en grafos grandes sin mencionar límite de recursión.

## Siguiente

[L15 — Caminos en grafos no ponderados](L15-caminos-en-grafos-no-ponderados.md)
