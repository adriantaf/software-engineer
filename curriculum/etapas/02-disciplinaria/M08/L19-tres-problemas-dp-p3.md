---
id: L19
materia: M08
orden: 19
titulo: Tres problemas DP (P3)
horas: 5.0
semana: 5
lectura: "P3: tres problemas DP con caso base explícito"
evidencia: dp/ tres carpetas con caso base
---

# L19 — Tres problemas DP (P3)

**~5.0 h · Semana 5**

P3 exige tres problemas con caso base y transición explícitos — no solo fib.

## Objetivo

Entregar tres DP distintos empaquetados como evidencia P3.

## Pasos

### 1. Elige trio (20 min)

Ejemplos: climbing stairs, min coin change, unique paths, house robber, LCS intro corta. Evita tres fibs.

### 2. Problema 1 (70 min)

Carpeta con `enunciado.md` (estado/base/transición), `solution.ts`, tests.

### 3. Problemas 2 y 3 (110 min)

Misma plantilla. Uno puede ser top-down y otro bottom-up.

### 4. README P3 (20 min)

Lista las tres rutas en `dp/README.md`.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/dp
git commit -m "feat(m08): tres problemas DP P3"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Plantilla: estado, base, transición, complejidad | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Tres carpetas bajo `dp/` (o `dp/p1`, `dp/p2`, `dp/p3`) cada una con enunciado, caso base, transición, código y tests.
2. P3 checklist enlazada desde README.
3. Commit `feat(m08): tres problemas DP P3`.

## Errores comunes

- Tres variantes del mismo fib.
- Sin caso base escrito.
- Complejidad espacial omitida.

## Siguiente

[L20 — Patrones DP y transiciones](L20-patrones-dp-y-transiciones.md)
