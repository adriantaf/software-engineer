---
id: L19
materia: M03
orden: 19
titulo: Búsqueda en anchura (BFS)
horas: 3
semana: 5
lectura: 'Rosen Cap. 10.3 — BFS, distancias en grafos no ponderados'
evidencia: src/bfs.ts + tests con ejemplo.json + traza en apuntes
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar BFS desde un vértice origen; devolver orden de
      visita y distancias; probar en `ejemplo.json` y en un grafo donde BFS ≠
      DFS.


      BFS explora por capas; en grafos no ponderados da distancia en número de
      aristas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Algoritmo en papel
    xp: 10
    cuerpo: |-
      ```ts
      import type { Grafo } from "./graph";

      export type ResultadoBfs<T> = {
        orden: T[];
        distancia: Map<T, number>;
      };

      export function bfs<T>(g: Grafo<T>, origen: T): ResultadoBfs<T> {
        // cola FIFO, visitados, distancia[origen]=0
        throw new Error("implementar");
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Búsqueda en anchura (BFS)" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: src/bfs.ts + tests con ejemplo.json + traza en apuntes
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
      ¿Es buena práctica en esta lección? “Usar pila en lugar de cola (eso es
      DFS)."
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
        texto: >-
          Implementar BFS desde un vértice origen; devolver orden de visita y
          distancias; probar en `ejemplo.json` y en un grafo donde BFS ≠ DFS.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: >-
      `src/bfs.ts`:


      ```ts

      import type { Grafo } from "./graph";


      export type ResultadoBfs<T> = {
        orden: T[];
        distancia: Map<T, number>;
      };


      export function bfs<T>(g: Grafo<T>, origen: T): ResultadoBfs<T> {
        // cola FIFO, visitados, distancia[origen]=0
        throw new Error("implementar");
      }

      ```


      Tests:


      - Orden y distancias en grafo línea `A-B-C-D`.

      - Origen inexistente → error claro.

      - Grafo desconexo: nodos no alcanzables ausentes en `distancia` o con ∞
      (documenta convención).
  - id: s7
    tipo: explicacion
    titulo: 3. Traza manual
    xp: 10
    cuerpo: >-
      En `ejemplo.json`, ejecuta BFS desde `A` a mano (tabla paso a paso) y
      compara con salida del test.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`bfs` pasa tests en al menos dos grafos.'
      - Traza manual coincide con código para un origen.
      - Explicas cuándo BFS encuentra camino más corto en aristas.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L19 — Búsqueda en anchura (BFS)

**~3 h · Semana 5**

BFS explora por capas; en grafos no ponderados da distancia en número de aristas.

## Objetivo

Implementar BFS desde un vértice origen; devolver orden de visita y distancias; probar en `ejemplo.json` y en un grafo donde BFS ≠ DFS.

## Pasos

### 1. Algoritmo en papel (40 min)

En `grafos.md`, pseudocódigo BFS con cola `Q` y conjunto `visitados`. Indica invariante: al sacar `v` de `Q`, distancia mínima desde origen está fijada (grafo no ponderado).

### 2. Implementación (80–90 min)

`src/bfs.ts`:

```ts
import type { Grafo } from "./graph";

export type ResultadoBfs<T> = {
  orden: T[];
  distancia: Map<T, number>;
};

export function bfs<T>(g: Grafo<T>, origen: T): ResultadoBfs<T> {
  // cola FIFO, visitados, distancia[origen]=0
  throw new Error("implementar");
}
```

Tests:

- Orden y distancias en grafo línea `A-B-C-D`.
- Origen inexistente → error claro.
- Grafo desconexo: nodos no alcanzables ausentes en `distancia` o con ∞ (documenta convención).

### 3. Traza manual (30 min)

En `ejemplo.json`, ejecuta BFS desde `A` a mano (tabla paso a paso) y compara con salida del test.

### 4. Teoría (20 min)

Párrafo en README del proyecto: por qué BFS usa cola y complejidad `O(V+E)` con lista de adyacencia.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 10.3 (BFS) |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `bfs` pasa tests en al menos dos grafos.
2. Traza manual coincide con código para un origen.
3. Explicas cuándo BFS encuentra camino más corto en aristas.

## Errores comunes

- Usar pila en lugar de cola (eso es DFS).
- Marcar visitado al encolar vs al desencolar (elige una convención y sé consistente).
- No manejar vértices aislados.

## Siguiente

[L20 — DFS, CLI de grafo y cierre](L20-dfs-cli-grafo-y-cierre.md)
