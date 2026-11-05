---
id: L18
materia: M03
orden: 18
titulo: Representación de grafos en TS
horas: 3
semana: 5
lectura: Rosen Cap. 10.2 — listas de adyacencia y matrices de adyacencia
evidencia: src/graph.ts (lista + matriz) + tests carga desde ejemplo.json
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Parsear `ejemplo.json`; construir lista y matriz de
      adyacencia; comparar espacio/tiempo en un párrafo argumentado (P2).


      Misma información, dos estructuras: lista (sparse) vs matriz (dense).
      Implementas ambas y cargas desde JSON.
  - id: s2
    tipo: ejemplo
    titulo: 1. Tipos
    xp: 10
    cuerpo: |-
      ```ts
      export type Arista<T> = [T, T];

      export type GrafoJson<T = string> = {
        dirigido: boolean;
        vertices: T[];
        aristas: Arista<T>[];
      };

      export type Grafo<T> = {
        dirigido: boolean;
        vertices: T[];
        adyacencia: Map<T, T[]>;
      };
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Representación de grafos en TS" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/graph.ts (lista + matriz) + tests carga desde ejemplo.json
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
      ¿Es buena práctica en esta lección? “Vértice en arista que no está en
      `vertices`."
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
          Parsear `ejemplo.json`; construir lista y matriz de adyacencia;
          comparar espacio/tiempo en un párrafo argumentado (P2).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Carga desde JSON
    xp: 10
    cuerpo: >-
      ```ts

      export function desdeJson<T>(raw: GrafoJson<T>): Grafo<T> {
        const ady = new Map<T, T[]>();
        for (const v of raw.vertices) ady.set(v, []);
        for (const [u, v] of raw.aristas) {
          ady.get(u)!.push(v);
          if (!raw.dirigido) ady.get(v)!.push(u);
        }
        return { dirigido: raw.dirigido, vertices: [...raw.vertices], adyacencia: ady };
      }

      ```


      Lee `grafos/ejemplo.json` en tests con `fs` o importa el JSON según tu
      setup.
  - id: s7
    tipo: ejemplo
    titulo: 3. Matriz de adyacencia
    xp: 10
    cuerpo: |-
      ```ts
      export function matrizAdyacencia<T>(g: Grafo<T>): number[][] {
        const n = g.vertices.length;
        const idx = new Map(g.vertices.map((v, i) => [v, i]));
        const m = Array.from({ length: n }, () => Array(n).fill(0));
        for (const [u, vecinos] of g.adyacencia) {
          const i = idx.get(u)!;
          for (const v of vecinos) m[i][idx.get(v)!] = 1;
        }
        return m;
      }
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`desdeJson` + `matrizAdyacencia` con tests usando `ejemplo.json`.'
      - Párrafo comparando lista vs matriz con un ejemplo numérico.
      - Grados por código coinciden con L17.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L18 — Representación de grafos en TS

**~3 h · Semana 5**

Misma información, dos estructuras: lista (sparse) vs matriz (dense). Implementas ambas y cargas desde JSON.

## Objetivo

Parsear `ejemplo.json`; construir lista y matriz de adyacencia; comparar espacio/tiempo en un párrafo argumentado (P2).

## Pasos

### 1. Tipos (20 min)

`src/graph.ts`:

```ts
export type Arista<T> = [T, T];

export type GrafoJson<T = string> = {
  dirigido: boolean;
  vertices: T[];
  aristas: Arista<T>[];
};

export type Grafo<T> = {
  dirigido: boolean;
  vertices: T[];
  adyacencia: Map<T, T[]>;
};
```

### 2. Carga desde JSON (50–60 min)

```ts
export function desdeJson<T>(raw: GrafoJson<T>): Grafo<T> {
  const ady = new Map<T, T[]>();
  for (const v of raw.vertices) ady.set(v, []);
  for (const [u, v] of raw.aristas) {
    ady.get(u)!.push(v);
    if (!raw.dirigido) ady.get(v)!.push(u);
  }
  return { dirigido: raw.dirigido, vertices: [...raw.vertices], adyacencia: ady };
}
```

Lee `grafos/ejemplo.json` en tests con `fs` o importa el JSON según tu setup.

### 3. Matriz de adyacencia (50 min)

```ts
export function matrizAdyacencia<T>(g: Grafo<T>): number[][] {
  const n = g.vertices.length;
  const idx = new Map(g.vertices.map((v, i) => [v, i]));
  const m = Array.from({ length: n }, () => Array(n).fill(0));
  for (const [u, vecinos] of g.adyacencia) {
    const i = idx.get(u)!;
    for (const v of vecinos) m[i][idx.get(v)!] = 1;
  }
  return m;
}
```

Test: simetría en grafo no dirigido.

### 4. Comparación escrita (30 min)

En `grafos.md` o README: para `|V|=n`, `|E|=m`, coste espacial lista `O(n+m)` vs matriz `O(n²)`; cuándo elegirías cada una (ej. grafo denso de 50 nodos vs red social sparse).

### 5. Grados desde código (20 min)

Función `grados(g): Map<T, number>` y compara con cálculo manual de L17.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 10.2 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `desdeJson` + `matrizAdyacencia` con tests usando `ejemplo.json`.
2. Párrafo comparando lista vs matriz con un ejemplo numérico.
3. Grados por código coinciden con L17.

## Errores comunes

- Vértice en arista que no está en `vertices`.
- Matriz asimétrica en grafo no dirigido por bug de doble arista.
- Índices inconsistentes entre funciones.

## Siguiente

[L19 — Búsqueda en anchura (BFS)](L19-busqueda-en-anchura-bfs.md)
