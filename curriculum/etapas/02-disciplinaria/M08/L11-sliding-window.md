---
id: L11
materia: M08
orden: 11
titulo: Sliding window
horas: 5.0
semana: 3
lectura: Ventana deslizante fija y variable
evidencia: 2 problemas ventana
---

# L11 — Sliding window

**~5.0 h · Semana 3**

La ventana mantiene un invariante local y se desliza en O(n) total.

## Objetivo

Resolver dos problemas de ventana y documentar el invariante de cada uno.

## Pasos

### 1. Lectura / bosquejo (30 min)

Fija (max sum subarray size k) vs variable (longest substring without repeat).

### 2. Problema ventana fija (60 min)

Implementa + tests (k > n, k=1, k=n).

### 3. Problema ventana variable (80 min)

Map/set de frecuencia; mueve `right`, encoge `left`. Complejidad O(n).

### 4. Índice (20 min)

Patrón `sliding-window`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): sliding window"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Window fija vs variable; invariante de la ventana | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Dos problemas sliding window (fija y/o variable) con análisis.
2. Tests incluyen ventana más grande que el array.
3. Commit `feat(m08): sliding window`.

## Errores comunes

- Recalcular la ventana desde cero cada paso (O(nk) disfrazado).
- Olvidar encoger la ventana en la variante variable.
- Sin invariante escrito.

## Siguiente

[L12 — Índice de patrones (5+ entradas)](L12-indice-de-patrones-5-entradas.md)
