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

Es el lenguaje de estructuras de datos, bases de datos y algoritmos. UABC y Tec la exigen; aquí la haces **aplicada a código**.

**En cristiano:** lógica, conjuntos y grafos no son adorno: los usas al razonar algoritmos y modelos. Demuestras a mano y codeas lo esencial.

## Análogos

- UABC / Tec: Matemáticas discretas

## Objetivos

1. Lógica proposicional y predicados básicos.
2. Conjuntos, relaciones, funciones.
3. Inducción y conteo.
4. Grafos introductorios.
5. Conectar ideas con código TypeScript.

## Cómo estudiar esta materia

- Alterna: 1 h de teoría en papel + 1 h implementando en TS.
- No memorices tablas de verdad: **constrúyelas**.
- Cada concepto nuevo → un archivo `.ts` con 3 ejemplos.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Teoría Rosen | 6–8 | Capítulos de la semana + 3 demos |
| Implementación | 6–8 | Ops de conjuntos / grafos en TS |
| Proyecto CLI | 4–6 | Visualizador BFS/DFS |
| Retro | 1 | Una prueba que aún no te sale |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)

1. Crea `projects/m03-discretas/README.md` con el índice de temas.
2. En papel (o Markdown), escribe la tabla de verdad de `P ∧ Q`, `P ∨ Q`, `¬P`, `P → Q`.
3. Implementa en TS:
   ```ts
   export function implica(p: boolean, q: boolean): boolean {
     return !p || q;
   }
   ```
4. Verifica los 4 casos de `P → Q` con `console.log` o un test.
5. Lee el capítulo de lógica de tu libro ES (solo ese capítulo hoy).

## Ejemplo — conjunto con operaciones

```ts
export function union<T>(a: Set<T>, b: Set<T>): Set<T> {
  return new Set([...a, ...b]);
}

export function interseccion<T>(a: Set<T>, b: Set<T>): Set<T> {
  return new Set([...a].filter((x) => b.has(x)));
}
```

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Lógica, tablas de verdad, equivalencias |
| 2 | Conjuntos, operaciones, leyes |
| 3 | Relaciones, funciones, inducción |
| 4 | Combinatoria básica |
| 5 | Grafos: representación, BFS/DFS intro |

## Lecturas

Canon: *Matemáticas discretas y sus aplicaciones* — Kenneth H. Rosen (ed. ES). Si tu edición numera ±1, sigue el **título**. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos (Rosen) | Alternativa / apoyo |
|--------|-------------------|---------------------|
| 1 | **Cap. 1** — Lógica y demostraciones (proposicional, predicados, reglas) | Apuntes en `projects/m03-discretas/` + tablas de verdad propias |
| 2 | **Cap. 2** — Conjuntos, funciones, secuencias (ops y leyes) | Mismos apuntes + implementación de ops |
| 3 | **Cap. 5** (inducción/recursión, selecto) + **Cap. 9** (relaciones, selecto: matrices, propiedades) | Demostraciones cortas a mano |
| 4 | **Cap. 6** — Conteo / combinatoria básica | Ejercicios del libro filtrados (pares) |
| 5 | **Cap. 10** — Grafos (representación, caminos, BFS/DFS intro) | Implementación + dibujo de grafos pequeños |

**Regla:** cada semana ≥3 ejercicios resueltos a mano **antes** de codear.

## Prácticas

1. **P1:** 10 demostraciones cortas (escaneadas o Markdown).
2. **P2:** Implementar ops de conjuntos, matriz de relación, lista de adyacencia.
3. **P3:** Para 5 funciones tuyas, escribir Big-O y justificar.

## Proyecto útil

CLI que lea un grafo (JSON) e imprima BFS/DFS y grado de nodos. Documenta la teoría detrás.

## Errores comunes

- Solo leer sin demostrar nada a mano.
- Confundir → (implicación) con ↔ (bicondicional).
- Decir “es O(n)” sin argumentar el peor caso.
- Implementar BFS mal y no probar con un grafo de 4 nodos dibujado.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Demos:** 10 demostraciones cortas en `projects/m03-discretas/demos.md`.
- **P2 — Código:** Ops de conjuntos + matriz de relación + adyacencia con tests.
- **P3 — Big-O:** 5 funciones tuyas con Big-O justificado en Markdown.
- **Proyecto — Grafo CLI:** Lee grafo JSON, imprime BFS/DFS y grados; README con teoría.

## Criterios de dominio

- [ ] Pruebas por inducción de un sumatorio simple.
- [ ] Explicas por qué un grafo se representa de dos formas.
- [ ] No confundes O(n) con “rápido en mi laptop”.
