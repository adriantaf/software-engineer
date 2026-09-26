---
id: M03
titulo: Matemáticas discretas
etapa: basica
orden: 3
semanas: 5
horas: 100
practicas:
  - id: p1
    titulo: Cuaderno de demostraciones (10 pruebas cortas)
  - id: p2
    titulo: Implementar conjuntos, relaciones y grafos simples en TS
  - id: p3
    titulo: Contar complejidad de 5 algoritmos propios
proyecto:
  id: proj
  titulo: Bitácora matemática + visualizador de grafos CLI
---

# M03 — Matemáticas discretas

## Por qué existe

Es el lenguaje de estructuras de datos, bases de datos y algoritmos. Aquí la haces **aplicada a código**, no solo de pizarrón.

**En resumen:** lógica, conjuntos y grafos no son adorno: los usas al razonar algoritmos y modelos. Demuestras a mano y codeas lo esencial.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Razonar con lógica proposicional y predicados; escribir demostraciones cortas correctas.
2. Operar con conjuntos, relaciones y funciones (propiedades y contraejemplos).
3. Aplicar inducción matemática y técnicas básicas de conteo.
4. Modelar problemas con grafos; implementar representaciones y BFS/DFS en TypeScript.
5. Conectar cada idea con evidencia en `projects/m03-discretas/`.

## Cómo estudiar esta materia (lecciones)

M03 sigue el mismo formato que M01: lecciones cortas, completas, en orden.

1. Abre las lecciones **en orden** (L01 → L20).
2. Cada lección trae objetivo, pasos, lectura de Rosen y criterio “Hecho cuando”.
3. Marca la lección en la UI solo si cumple ese criterio.
4. **Regla de rigor:** cada semana ≥3 ejercicios resueltos **a mano** (en `demos.md` o anexos) **antes** de confiar solo en el código.
5. Alterna teoría en papel y TypeScript (`strict`) según los pasos de cada lección.
6. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Teoría Rosen | 6–8 | Capítulos de la semana + demostraciones en `demos.md` |
| Implementación | 6–8 | Módulos TS en `projects/m03-discretas/src/` |
| Proyecto CLI | 4–6 | Grafo JSON, BFS/DFS, grados (L18–L20) |
| Retro | 1 | Una prueba o algoritmo que aún no te sale |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la fila de lectura de esa lección.

## Lecciones

### Semana 1 — Lógica y demostraciones (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Lógica proposicional y tablas de verdad](M03/L01-logica-proposicional-y-tablas-de-verdad.md) | 2.5 |
| L02 | [Implicación, equivalencias y leyes](M03/L02-implicacion-equivalencias-y-leyes.md) | 2.5 |
| L03 | [Predicados y cuantificadores](M03/L03-predicados-y-cuantificadores.md) | 3 |
| L04 | [Métodos de demostración (intro)](M03/L04-metodos-de-demostracion.md) | 3 |

### Semana 2 — Conjuntos y funciones (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Conjuntos: notación y membresía](M03/L05-conjuntos-notacion-y-membresia.md) | 2.5 |
| L06 | [Operaciones conjuntistas en TypeScript](M03/L06-operaciones-conjuntistas-en-typescript.md) | 3 |
| L07 | [Leyes de conjuntos y pruebas](M03/L07-leyes-de-conjuntos-y-pruebas.md) | 2.5 |
| L08 | [Funciones: imagen, inyectividad y biyección](M03/L08-funciones-imagen-e-inyectividad.md) | 3 |

### Semana 3 — Relaciones e inducción (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [Relaciones y propiedades](M03/L09-relaciones-y-propiedades.md) | 2.5 |
| L10 | [Equivalencias y particiones](M03/L10-equivalencias-y-particiones.md) | 2.5 |
| L11 | [Órdenes parciales y totales](M03/L11-ordenes-parciales-y-totales.md) | 2.5 |
| L12 | [Inducción matemática](M03/L12-induccion-matematica.md) | 3 |

### Semana 4 — Conteo y complejidad (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L13 | [Conteo: regla del producto y la suma](M03/L13-conteo-reglas-producto-y-suma.md) | 2.5 |
| L14 | [Permutaciones y combinaciones](M03/L14-permutaciones-y-combinaciones.md) | 3 |
| L15 | [Principio de inclusión-exclusión](M03/L15-inclusion-exclusion.md) | 2.5 |
| L16 | [Binomial, Pascal y Big-O de funciones propias](M03/L16-binomial-y-complejidad.md) | 3 |

### Semana 5 — Grafos y cierre (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L17 | [Grafos: modelo y terminología](M03/L17-grafos-modelo-y-terminologia.md) | 2.5 |
| L18 | [Representación de grafos en TS](M03/L18-representacion-de-grafos-en-ts.md) | 3 |
| L19 | [Búsqueda en anchura (BFS)](M03/L19-busqueda-en-anchura-bfs.md) | 3 |
| L20 | [DFS, CLI de grafo y cierre](M03/L20-dfs-cli-grafo-y-cierre.md) | 3 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Matemáticas discretas y sus aplicaciones* — Kenneth H. Rosen (ed. ES). Si tu edición numera ±1, sigue el **título**. Catálogo: [bibliografía](../../bibliografia.md#m03-matematicas-discretas).

| Semana | Lecciones | Capítulos / foco Rosen |
|--------|-----------|-------------------------|
| 1 | L01–L04 | **Cap. 1** — Lógica proposicional, predicados, métodos de prueba |
| 2 | L05–L08 | **Cap. 2** — Conjuntos, funciones, secuencias (selecto) |
| 3 | L09–L12 | **Cap. 9** (relaciones) + **Cap. 5** (inducción/recursión, selecto) |
| 4 | L13–L16 | **Cap. 6** — Conteo / combinatoria |
| 5 | L17–L20 | **Cap. 10** — Grafos, caminos, BFS/DFS |

**Regla:** no avances de capítulo más rápido que las lecciones de esa semana. Los ejercicios del libro se filtran: prioriza los que piden **demostrar** o **contar con justificación**.

## Prácticas

1. **P1:** 10 demostraciones cortas (Markdown o escaneo) en `projects/m03-discretas/demos.md`.
2. **P2:** Operaciones de conjuntos, matriz de relación y lista de adyacencia con tests (Vitest).
3. **P3:** Big-O justificado para 5 funciones tuyas en `projects/m03-discretas/complejidad.md`.

## Proyecto útil

CLI que lea un grafo (JSON), imprima BFS/DFS, grados de nodos y un resumen del recorrido. Documenta en el README la teoría detrás de cada algoritmo.

## Errores comunes

- Solo leer sin demostrar nada a mano.
- Confundir → (implicación) con ↔ (bicondicional).
- Marcar lecciones sin cumplir “Hecho cuando”.
- Decir “es O(n)” sin argumentar el peor caso.
- Implementar BFS/DFS sin probar en un grafo de 4–6 nodos dibujado a mano.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Demos:** 10 demostraciones numeradas en `projects/m03-discretas/demos.md` (enunciado + prueba).
- **P2 — Código:** `src/sets.ts`, `src/relations.ts`, `src/graph.ts` (o nombres equivalentes) con tests que pasen.
- **P3 — Big-O:** `projects/m03-discretas/complejidad.md` con 5 funciones y análisis de peor caso.
- **Proyecto — Grafo CLI:** `src/cli.ts` (o `bin/`) lee JSON, imprime BFS/DFS y grados; README actualizado.

## Criterios de dominio

- [ ] Pruebas por inducción un sumatorio o propiedad simple sin copiar la solución.
- [ ] Explicas por qué un grafo conviene como lista o como matriz en un caso concreto.
- [ ] Distingues permutación de combinación en un problema nuevo.
- [ ] No confundes O(n) con “rápido en mi laptop”.
