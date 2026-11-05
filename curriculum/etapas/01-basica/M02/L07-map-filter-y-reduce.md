---
id: L07
materia: M02
orden: 7
titulo: 'map, filter y reduce'
horas: 3
semana: 2
lectura: EJ cap. 5 (funciones de orden superior)
evidencia: src/colecciones/reportes.ts con 3 funciones HOF + katas HOF
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar reportes sobre `Habito[]` con
      `map`/`filter`/`reduce` y leer EJ cap. 5 con ejercicios hechos.


      `stats` y `export` de tu CLI serán pipelines de datos. Este patrón es el
      idioma natural.
  - id: s2
    tipo: ejemplo
    titulo: 1. Reportes de hábitos
    xp: 10
    cuerpo: >-
      ```ts

      import type { Habito } from "../modelo/habito.js";


      export function nombresOrdenados(habitos: Habito[]): string[] {
        return [...habitos]
          .sort((a, b) => a.nombre.localeCompare(b.nombre))
          .map((h) => h.nombre);
      }


      export function habitosConEtiqueta(habitos: Habito[], etiqueta: string):
      Habito[] {
        return habitos.filter((h) => h.etiquetas?.includes(etiqueta));
      }


      export function totalMarcados(habitos: Habito[]): number {
        return habitos.reduce((acc, h) => acc + h.completados.length, 0);
      }

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "map, filter y reduce" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: src/colecciones/reportes.ts con 3 funciones HOF + katas HOF
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “`reduce` sin tipo de acumulador y TS
      infiere mal."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar reportes sobre `Habito[]` con `map`/`filter`/`reduce` y
          leer EJ cap. 5 con ejercicios hechos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Pipeline legible
    xp: 10
    cuerpo: >-
      `src/colecciones/pipeline.ts` — función `resumenSemanal(habitos)` que
      compone filtros y reduce a un objeto `{ activos: number; marcados: number
      }`.
  - id: s7
    tipo: explicacion
    titulo: 3. EJ cap. 5
    xp: 10
    cuerpo: >-
      Lee el capítulo y resuelve **≥2 ejercicios** (flatten, groupBy simple,
      etc.) en TS.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`reportes.ts` exporta las tres funciones y se usan desde un demo.'
      - Ejercicios cap. 5 commiteados.
      - >-
        Puedes dibujar en papel el flujo datos → map → filter → reduce para
        `stats`.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
