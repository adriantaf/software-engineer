---
id: L17
materia: M08
orden: 17
titulo: Memoización top-down
horas: 5.0
semana: 5
lectura: CLRS DP intro — top-down con memo
evidencia: dp/memo-ejemplo.ts
---

# L17 — Memoización top-down

**~5.0 h · Semana 5**

DP empieza viendo subproblemas solapados: fibonacci es el laboratorio.

## Objetivo

Implementar una solución top-down con memo y demostrar el ahorro de llamadas.

## Pasos

### 1. Lectura (40 min)

CLRS intro DP: overlapping subproblems + optimal substructure. Anota en `dp/README.md`.

### 2. Fib (u otro) naive vs memo (70 min)

`dp/memo-ejemplo.ts`: versión ingenua (solo para n pequeño) y `fibMemo` con `Map`/`array`. Contador de llamadas.

### 3. Tests (40 min)

fib(0..10) conocidos; n=40 memo termina en ms.

### 4. Definición de estado (40 min)

Escribe: estado = `__`, transición = `__`, base = `__`.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/dp
git commit -m "feat(m08): memoizacion top-down"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Recursión + mapa memo; overlapping subproblems | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `dp/memo-ejemplo.ts` (fib o paths) con y sin memo, o contador de llamadas.
2. Tests de valores conocidos; nota de complejidad en `dp/README.md` borrador.
3. Commit `feat(m08): memoizacion top-down`.

## Errores comunes

- Memoizar sin clave correcta (olvidar argumentos).
- Creer que memo cambia la respuesta (solo el tiempo).
- Sin caso base.

## Siguiente

[L18 — Programación dinámica bottom-up](L18-programacion-dinamica-bottom-up.md)
