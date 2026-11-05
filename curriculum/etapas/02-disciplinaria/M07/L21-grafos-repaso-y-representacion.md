---
id: L21
materia: M07
orden: 21
titulo: 'Grafos: repaso y representación'
horas: 5
semana: 6
lectura: 'Grafos: lista de adyacencia vs matriz'
evidencia: Adjacency list en TS reutilizable
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Implementar grafo por lista de adyacencia con tests claros.

      Repasas M03 con una API TypeScript reutilizable (base para M08 BFS/DFS).
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura corta
    xp: 10
    cuerpo: |-
      ```ts
      export class Graph {
        addVertex(v: string): void
        addEdge(a: string, b: string, undirected = true): void
        neighbors(v: string): string[]
        vertices(): string[]
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Grafos: repaso y representación" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: Adjacency list en TS reutilizable
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Matriz densa para grafo sparse sin
      justificar."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Implementar grafo por lista de adyacencia con tests claros.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. API
    xp: 10
    cuerpo: |-
      `src/graph.ts`:

      ```ts
      export class Graph {
        addVertex(v: string): void
        addEdge(a: string, b: string, undirected = true): void
        neighbors(v: string): string[]
        vertices(): string[]
      }
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Tests
    xp: 10
    cuerpo: Triángulo A-B-C; dirigido vs no dirigido; vértice aislado.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`src/graph.ts` con `addVertex`, `addEdge`, `neighbors`.'
      - 'Tests: grafo pequeño no dirigido; edge bidireccional; vecino ausente.'
      - 'Commit `feat(m07): grafo lista de adyacencia`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L21 — Grafos: repaso y representación

**~5.0 h · Semana 6**

Repasas M03 con una API TypeScript reutilizable (base para M08 BFS/DFS).

## Objetivo

Implementar grafo por lista de adyacencia con tests claros.

## Pasos

### 1. Lectura corta (30 min)

Lista vs matriz: memoria y costo de `neighbors`. Elige lista para el curso.

### 2. API (80 min)

`src/graph.ts`:

```ts
export class Graph {
  addVertex(v: string): void
  addEdge(a: string, b: string, undirected = true): void
  neighbors(v: string): string[]
  vertices(): string[]
}
```

### 3. Tests (50 min)

Triángulo A-B-C; dirigido vs no dirigido; vértice aislado.

### 4. Ejemplo dominio (40 min)

En `docs/grafo-agenda.md`: clientes/servicios como “quién recomienda a quién” (3 nodos). Solo documentación.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): grafo lista de adyacencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Lista de adyacencia; dirigido vs no dirigido | [VisuAlgo · Graph](https://visualgo.net/en/graphds) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/graph.ts` con `addVertex`, `addEdge`, `neighbors`.
2. Tests: grafo pequeño no dirigido; edge bidireccional; vecino ausente.
3. Commit `feat(m07): grafo lista de adyacencia`.

## Errores comunes

- Matriz densa para grafo sparse sin justificar.
- Olvidar simetría en no dirigido.
- API sin tipos (arrays `any`).

## Siguiente

[L22 — Benchmark P3: nativo vs propio](L22-benchmark-p3-nativo-vs-propio.md)
