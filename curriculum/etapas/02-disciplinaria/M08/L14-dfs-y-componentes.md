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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      DFS recorre profundo; sirve para marcar componentes y ciclos
      introductorios.


      **Objetivo de esta lección:** Contar componentes conexas (o resolver
      problema equivalente) con DFS y tests.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: DFS base
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): dfs componentes conexas"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Componentes
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): dfs componentes conexas"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «DFS y componentes», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de DFS y componentes
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

      `git commit -am "feat(m08): dfs componentes conexas"`
    comandoEsperado:
      - 'git commit -am "feat(m08): dfs componentes conexas"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): dfs componentes conexas"'
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
          Contar componentes conexas (o resolver problema equivalente) con DFS y
          tests.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Problema empaquetado
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
