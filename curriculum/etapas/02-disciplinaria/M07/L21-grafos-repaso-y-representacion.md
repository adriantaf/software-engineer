---
id: L21
materia: M07
orden: 21
titulo: "Grafos: repaso y representación"
horas: 5.0
semana: 6
lectura: "Repaso M03 + ED grafos"
evidencia: "Adjacency list en TS reutilizable"
---

# L21 — Grafos: repaso y representación

**~5.0 h · Semana 6**

Semana 6 de M07: rigor en implementación, tests y documentación de costos.

## Objetivo

Avanzar evidencia `Adjacency list en TS reutilizable` con código TS, tests Vitest y notas en COMPLEJIDAD/README.

## Pasos

### 1. Lectura dirigida (60 min)

Lee la sección indicada en tu texto ED sobre **Grafos**. Anota definiciones formales (pre/post condiciones).

### 2. Implementación (120 min)

Crea o extiende módulos bajo `src/` con tipos explícitos. Sin `any`. Exporta API mínima documentada en comentario JSDoc breve.

### 3. Tests (90 min)

Mínimo **5** tests: feliz, vacío, borde, caso que fuerza estructura interna (p. ej. colisión, rotación simple, heapify), regresión.

### 4. Documentación (30 min)

Actualiza `COMPLEJIDAD.md` o README con Big-O de operaciones nuevas. Si comparas con nativo, di **cuándo** gana cada uno.

### 5. Commit (30 min)

Mensaje `feat(m07)` o `docs(m07)` descriptivo en español.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Ver ficha | Capítulo de la semana |

## Hecho cuando

1. Código + tests verdes para el foco de la lección.
2. Costos documentados.
3. Commit en git.

## Errores comunes

- Copiar implementación sin entender invariantes.
- Tests solo “felices”.
- Omitir commit.
## Siguiente

[L22 — Benchmark P3: nativo vs propio](L22-benchmark-p3-nativo-vs-propio.md)
