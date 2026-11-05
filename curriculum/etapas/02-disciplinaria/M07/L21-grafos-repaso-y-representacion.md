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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Repasas M03 con una API TypeScript reutilizable (base para M08 BFS/DFS).


      **Objetivo de esta lección:** Implementar grafo por lista de adyacencia
      con tests claros.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura corta
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: API
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

      `src/graph.ts`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Grafos: repaso y representación», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Grafos: repaso y
          representación
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Matriz densa para grafo sparse sin
      justificar."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: Implementar grafo por lista de adyacencia con tests claros.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
