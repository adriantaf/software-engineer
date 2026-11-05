---
id: L20
materia: M03
orden: 20
titulo: 'DFS, CLI de grafo y cierre'
horas: 3
semana: 5
lectura: Rosen Cap. 10.3 — DFS; repaso cap. 10 según huecos
evidencia: >-
  src/dfs.ts + src/cli.ts + demos.md (10 demos) + README proyecto + checklist
  P1–P3 y proyecto
formato: pasos
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras M03: DFS, CLI que lee JSON e imprime recorridos y grados, y
      revisión honesta de todas las evidencias.


      **Objetivo de esta lección:** Implementar DFS (iterativo o recursivo);
      entregar CLI del proyecto; completar a 10 demostraciones en `demos.md`;
      autoevaluar P1–P3 y criterios de dominio.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: DFS
    xp: 10
    cuerpo: >-
      ```ts

      import type { Grafo } from "./graph";


      export function dfs<T>(g: Grafo<T>, origen: T): T[] {
        const visitados = new Set<T>();
        const orden: T[] = [];
        function visitar(v: T) {
          if (visitados.has(v)) return;
          visitados.add(v);
          orden.push(v);
          for (const w of g.adyacencia.get(v) ?? []) visitar(w);
        }
        visitar(origen);
        return orden;
      }

      ```


      `src/dfs.ts`: Tests: mismo grafo que BFS; orden distinto salvo casos
      triviales. Documenta ciclo: versión con `visitados` evita bucles
      infinitos. Compara BFS vs DFS en `grafos.md` con el mismo origen.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: CLI del proyecto
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m03-discretas && npm test
      npx tsx src/cli.ts grafos/ejemplo.json
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «DFS, CLI de grafo y cierre», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`dfs` y `bfs` probados; CLI imprime grados y ambos recorridos.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de DFS, CLI de grafo y
          cierre
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
      ¿Es recomendable en esta lección? “Marcar M03 completa sin CLI ni tests
      verdes."
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
          Implementar DFS (iterativo o recursivo); entregar CLI del proyecto;
          completar a 10 demostraciones en `demos.md`; autoevaluar P1–P3 y
          criterios de dominio.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M03
    xp: 25
    enunciado: >-
      Cierra **Matemáticas discretas** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: Cuaderno de demostraciones (10 pruebas cortas)'
      - 'P2: Implementar conjuntos, relaciones y grafos simples en TS'
      - 'P3: Contar complejidad de 5 algoritmos propios'
      - 'Proyecto: Bitácora matemática + visualizador de grafos CLI'
      - >-
        src/dfs.ts + src/cli.ts + demos.md (10 demos) + README proyecto +
        checklist P1–P3 y proyecto
    rubrica:
      - id: r1
        criterio: '`dfs` y `bfs` probados; CLI imprime grados y ambos recorridos.'
      - id: r2
        criterio: '`demos.md` tiene ≥10 demostraciones; P2 y P3 verificables.'
      - id: r3
        criterio: '`cierre.md` o README documenta retro y criterios de dominio.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`dfs` y `bfs` probados; CLI imprime grados y ambos recorridos.'
      - '`demos.md` tiene ≥10 demostraciones; P2 y P3 verificables.'
      - '`cierre.md` o README documenta retro y criterios de dominio.'
    siguiente: Materia M03 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — DFS, CLI de grafo y cierre

**~3 h · Semana 5**

Cierras M03: DFS, CLI que lee JSON e imprime recorridos y grados, y revisión honesta de todas las evidencias.

## Objetivo

Implementar DFS (iterativo o recursivo); entregar CLI del proyecto; completar a 10 demostraciones en `demos.md`; autoevaluar P1–P3 y criterios de dominio.

## Pasos

### 1. DFS (60–70 min)

`src/dfs.ts`:

```ts
import type { Grafo } from "./graph";

export function dfs<T>(g: Grafo<T>, origen: T): T[] {
  const visitados = new Set<T>();
  const orden: T[] = [];
  function visitar(v: T) {
    if (visitados.has(v)) return;
    visitados.add(v);
    orden.push(v);
    for (const w of g.adyacencia.get(v) ?? []) visitar(w);
  }
  visitar(origen);
  return orden;
}
```

Tests: mismo grafo que BFS; orden distinto salvo casos triviales. Documenta ciclo: versión con `visitados` evita bucles infinitos.

Compara BFS vs DFS en `grafos.md` con el mismo origen.

### 2. CLI del proyecto (70–80 min)

`src/cli.ts` (ejecutable con `npx tsx src/cli.ts grafos/ejemplo.json`):

- Carga JSON.
- Imprime lista de vértices y grados.
- Imprime orden BFS y DFS desde un vértice (argumento o primer vértice).
- Mensaje de ayuda si falta archivo.

Actualiza `projects/m03-discretas/README.md` con sección **Teoría**: 1 párrafo BFS, 1 DFS, 1 representación.

### 3. P1 — Diez demostraciones (30 min)

Cuenta entradas en `demos.md`. Si faltan, completa hasta **10** (pueden ser cortas pero completas). Numeración continua.

### 4. Checklist final (40 min)

| Ítem | Evidencia |
|------|-----------|
| **P1** | `demos.md` con 10 pruebas |
| **P2** | `sets.ts`, `relations.ts` (matriz), `graph.ts` + tests |
| **P3** | `complejidad.md` con 5 funciones |
| **Proyecto** | CLI funcional + `grafos/*.json` |

Ejecuta:

```bash
cd projects/m03-discretas && npm test
npx tsx src/cli.ts grafos/ejemplo.json
```

Pega salida relevante en README o `apuntes/cierre.md`.

### 5. Criterios de dominio (20 min)

En `apuntes/cierre.md`, responde sí/no + frase:

- [ ] Inducción de un sumatorio sin copiar.
- [ ] Lista vs matriz de adyacencia en un caso concreto.
- [ ] Permutación vs combinación en problema nuevo.
- [ ] Big-O no confundido con velocidad empírica.

### 6. Commits y UI (15 min)

Commit final coherente. Marca lecciones L01–L20 solo si cada una cumple su “Hecho cuando”. Marca prácticas/proyecto en la ficha con evidencia real.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 10.3 (DFS) + repaso según huecos |
| Ficha | [M03 — Matemáticas discretas](../M03-matematicas-discretas.md) |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `dfs` y `bfs` probados; CLI imprime grados y ambos recorridos.
2. `demos.md` tiene ≥10 demostraciones; P2 y P3 verificables.
3. `cierre.md` o README documenta retro y criterios de dominio.

## Errores comunes

- Marcar M03 completa sin CLI ni tests verdes.
- DFS sin manejar ciclos en grafo no dirigido.
- README del proyecto sin teoría (solo comandos).

## Siguiente

Vuelve a la [ficha M03](../M03-matematicas-discretas.md), cierra checkboxes con evidencia, y continúa con **M04 — Probabilidad y estadística** (o la materia que siga en tu plan).
