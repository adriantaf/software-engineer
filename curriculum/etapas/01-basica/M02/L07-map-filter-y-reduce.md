---
id: L07
materia: M02
orden: 7
titulo: map, filter y reduce
horas: 3
semana: 2
lectura: "EJ cap. 5 (funciones de orden superior)"
evidencia: "src/colecciones/reportes.ts con 3 funciones HOF + katas HOF"
---

# L07 — map, filter y reduce

**~3 h · Semana 2**

Funciones de orden superior con tipos genéricos ligeros: encadenar transformaciones sin bucles imperativos innecesarios.

## Objetivo

Implementar reportes sobre `Habito[]` con `map`/`filter`/`reduce` y leer EJ cap. 5 con ejercicios hechos.

## Por qué importa

`stats` y `export` de tu CLI serán pipelines de datos. Este patrón es el idioma natural.

## Pasos

### 1. Reportes de hábitos (55 min)

`src/colecciones/reportes.ts`:

```ts
import type { Habito } from "../modelo/habito.js";

export function nombresOrdenados(habitos: Habito[]): string[] {
  return [...habitos]
    .sort((a, b) => a.nombre.localeCompare(b.nombre))
    .map((h) => h.nombre);
}

export function habitosConEtiqueta(habitos: Habito[], etiqueta: string): Habito[] {
  return habitos.filter((h) => h.etiquetas?.includes(etiqueta));
}

export function totalMarcados(habitos: Habito[]): number {
  return habitos.reduce((acc, h) => acc + h.completados.length, 0);
}
```

### 2. Pipeline legible (35 min)

`src/colecciones/pipeline.ts` — función `resumenSemanal(habitos)` que compone filtros y reduce a un objeto `{ activos: number; marcados: number }`.

### 3. EJ cap. 5 (50 min)

Lee el capítulo y resuelve **≥2 ejercicios** (flatten, groupBy simple, etc.) en TS.

### 4. Katas HOF (30 min)

Dos katas estilo “aplicar función a cada elemento” o reduce custom.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 5 |
| TS Handbook | [More on Functions — generics intro](https://www.typescriptlang.org/docs/handbook/2/generics.html) (solo primeras secciones) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `reportes.ts` exporta las tres funciones y se usan desde un demo.
2. Ejercicios cap. 5 commiteados.
3. Puedes dibujar en papel el flujo datos → map → filter → reduce para `stats`.

## Errores comunes

- `reduce` sin tipo de acumulador y TS infiere mal.
- Mutar elementos dentro de `map`.
- Encadenar 8 pasos sin extraer función con nombre.

## Siguiente

[L08 — Union types y narrowing](L08-union-types-y-narrowing.md)
