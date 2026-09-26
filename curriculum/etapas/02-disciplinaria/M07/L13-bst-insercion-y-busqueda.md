---
id: L13
materia: M07
orden: 13
titulo: BST: inserción y búsqueda
horas: 5.0
semana: 4
lectura: "ED: árboles binarios de búsqueda"
evidencia: "BST insert/contains + tests ordenados"
---

# L13 — BST: inserción y búsqueda

**~5.0 h · Semana 4**

Semana 4 de M07: rigor en implementación, tests y documentación de costos.

## Objetivo

Avanzar evidencia `BST insert/contains + tests ordenados` con código TS, tests Vitest y notas en COMPLEJIDAD/README.

## Pasos

### 1. Lectura dirigida (60 min)

Lee la sección indicada en tu texto ED sobre **BST**. Anota definiciones formales (pre/post condiciones).

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

[L14 — Recorridos inorder, preorder, postorder](L14-recorridos-inorder-preorder-postorder.md)
