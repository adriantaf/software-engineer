---
id: L15
materia: M14
orden: 15
titulo: Refactor P3 — módulo legacy antes y después
horas: 5.0
semana: 4
lectura: Refactor con comportamiento preservado
evidencia: refactor-notas.md + diff/commits (P3)
---

# L15 — Refactor P3 — módulo legacy antes y después

**~5.0 h · Semana 4**

P3: tomas código tuyo (spike feo, god function de precios, etc.) y lo refactorizas.

## Objetivo

`refactor-notas.md` + evidencia en git.

## Pasos (hazlos en orden)

### 1. Elige módulo (20 min)

Si no hay legacy, crea `src/legacy/agendar-todo-en-uno.ts` a propósito y luego rompe el monolito.

### 2. Caracteriza con test (40 min)

### 3. Refactor hacia patrones ya vistos (80–100 min)

### 4. Notas + commit

`refactor(m14): modulo legacy P3`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Refactor de módulo legacy propio con antes/después | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `refactor-notas.md` con módulo antes/después y qué patrón aplicaste.
2. Evidencia git (commits o diff pegado) y tests verdes post-refactor.
3. Commit `refactor(m14): modulo legacy P3` (o docs si el diff está en notas).

## Errores comunes

- Reescribir de cero y llamarlo refactor.
- Cambiar comportamiento observable sin test.
- Notas sin rutas de archivo.

## Siguiente

[L16 — Cierre M14 — cinco patrones e integración M17](L16-cierre-m14-cinco-patrones-e-integracion-m17.md)
