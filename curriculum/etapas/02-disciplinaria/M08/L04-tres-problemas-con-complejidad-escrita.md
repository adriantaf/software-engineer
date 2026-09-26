---
id: L04
materia: M08
orden: 4
titulo: Tres problemas con complejidad escrita
horas: 5.0
semana: 1
lectura: "Plantilla de entrega: enunciado, complejidad, código, tests"
evidencia: problems/ con 3 entradas + complejidad
---

# L04 — Tres problemas con complejidad escrita

**~5.0 h · Semana 1**

Cierras la semana 1 con la plantilla P1 que usarás el resto del curso.

## Objetivo

Dejar tres problemas completos en `problems/` e iniciar `indice-patrones.md`.

## Pasos

### 1. Plantilla (20 min)

Cada problema:

```
problems/NN-nombre/
  enunciado.md    # problema + complejidad objetivo
  solution.ts
  solution.test.ts
```

### 2. Completar / añadir hasta 3 (120 min)

Si L01 ya trajo 2, añade un tercero (p. ej. “mover ceros”, “intersección de arrays”). 30–45 min de intento serio antes de editorial propia.

### 3. Índice (40 min)

`indice-patrones.md` tabla: id | patrón | archivo | complejidad | notas.

### 4. Suite (30 min)

```bash
cd projects/m08-algoritmos && npm test
```

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "feat(m08): tres problemas con complejidad"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Disciplina de evidencia por problema (P1) | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Tres carpetas bajo `problems/` (pueden incluir las de L01) cada una con enunciado, complejidad, solución y ≥3 tests.
2. Filas iniciales en `indice-patrones.md` (≥3).
3. Commit `feat(m08): tres problemas con complejidad`.

## Errores comunes

- Código sin enunciado ni Big-O.
- Un solo test feliz.
- Índice vacío al cerrar la semana.

## Siguiente

[L05 — Insertion sort implementado](L05-insertion-sort-implementado.md)
