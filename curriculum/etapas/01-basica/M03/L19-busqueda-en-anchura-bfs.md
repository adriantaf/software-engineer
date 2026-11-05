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
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      BFS explora por capas; en grafos no ponderados da distancia en número de
      aristas.


      **Objetivo de esta lección:** Implementar BFS desde un vértice origen;
      devolver orden de visita y distancias; probar en `ejemplo.json` y en un
      grafo donde BFS ≠ DFS.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Algoritmo en papel
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: >-
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


      `src/bfs.ts`: Tests: - Orden y distancias en grafo línea `A-B-C-D`. -
      Origen inexistente → error claro. - Grafo desconexo: nodos no alcanzables
      ausentes en `distancia` o con ∞ (documenta convención).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Búsqueda en anchura (BFS)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`bfs` pasa tests en al menos dos grafos.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Búsqueda en anchura
          (BFS)
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
      ¿Es recomendable en esta lección? “Usar pila en lugar de cola (eso es
      DFS)."
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
        texto: >-
          Implementar BFS desde un vértice origen; devolver orden de visita y
          distancias; probar en `ejemplo.json` y en un grafo donde BFS ≠ DFS.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Traza manual
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
