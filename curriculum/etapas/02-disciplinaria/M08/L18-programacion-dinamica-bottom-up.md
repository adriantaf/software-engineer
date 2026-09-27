---
id: L18
materia: M08
orden: 18
titulo: Programación dinámica bottom-up
horas: 5.0
semana: 5
lectura: DP bottom-up / tabulación
evidencia: dp/bottom-up-ejemplo.ts
---

# L18 — Programación dinámica bottom-up

**~5.0 h · Semana 5**

Tabular elimina la pila de recursión y deja el orden de dependencias explícito.

## Objetivo

Reescribir el problema de L17 (o uno nuevo) en bottom-up con tabla `dp[]`.

## Pasos

### 1. Diseña el orden (30 min)

En papel: de qué celda depende `dp[i]`.

### 2. Implementación (70 min)

`dp/bottom-up-ejemplo.ts`. Inicializa bases; loop hasta n.

### 3. Equivalencia (40 min)

Test: para n en 0..20, memo === bottom-up.

### 4. Nota espacial (40 min)

¿Puedes usar 2 variables en fib? Documéntalo; no es obligatorio optimizar.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): dp bottom-up"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Tabla dp[]; orden de llenado; equivalencia con memo | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `dp/bottom-up-ejemplo.ts` con tabulación del mismo problema que L17 (o coin change simple).
2. Comparas espacial (optimización de variables opcionales) en nota corta.
3. Commit `feat(m08): dp bottom-up`.

## Errores comunes

- Llenar la tabla en orden incorrecto.
- Off-by-one en índices.
- Copiar memo y llamarlo bottom-up sin array dp.

## Siguiente

[L19 — Tres problemas DP (P3)](L19-tres-problemas-dp-p3.md)
