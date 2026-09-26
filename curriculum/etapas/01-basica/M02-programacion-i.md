---
id: M02
titulo: Programación I (TypeScript)
etapa: basica
orden: 2
semanas: 6
horas: 120
practicas:
  - id: p1
    titulo: 20 katas de fundamentos (variables, control, funciones)
  - id: p2
    titulo: Módulos + manejo de errores en un script real
  - id: p3
    titulo: Primera suite de tests con Vitest (10+ casos)
proyecto:
  id: proj
  titulo: CLI de hábitos y tareas con export CSV
---

# M02 — Programación I (TypeScript)

## Por qué existe

Necesitas **un** lenguaje a profundidad. TypeScript escala a web, APIs e IA tooling. Dejas de “conocer JS” y pasas a **programar**.

**En resumen:** aprendes TypeScript de verdad con katas, un script real y tests. El cierre es una CLI de hábitos que puedes enseñar.

## Objetivos de aprendizaje

1. Dominar tipos básicos, funciones, arrays, objetos, asincronía.
2. Leer errores del compilador y corregirlos sin pánico.
3. Escribir tests unitarios pequeños.
4. Entregar un CLI usable por ti mismo.

## Cómo estudiar esta materia (lecciones)

M02 sigue el formato de lecciones cortas y completas (como M01):

1. Abre las lecciones **en orden** (L01 → L24), cuatro por semana.
2. Cada lección trae objetivo, pasos con código, lectura y criterio **Hecho cuando**.
3. Marca la lección en la UI solo si cumple ese criterio.
4. Las **prácticas / proyecto** de abajo exigen evidencia en `projects/` (ver [m02-programacion](../../../projects/m02-programacion/README.md)).
5. Método general: [Cómo estudiar](../../como-estudiar.md).

**Hábitos de esta materia:**

- Código todos los días (aunque sean 45 min de katas).
- Activa `"strict": true` desde el primer `tsconfig`.
- Cuando un error de tipos aparezca: **léelo completo** antes de googlear.
- El CLI (`projects/m02-habits/`) se construye de a poco desde la **semana 3**, no al final.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura + tipado | 6–8 | EJ / Handbook según tabla Lecturas |
| Katas / labs | 6–8 | Exercism/Codewars en TS strict |
| Proyecto CLI | 4–6 | `projects/m02-habits/` + Vitest |
| Retro | 1 | 3 dudas tipadas resueltas |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Lecciones

### Semana 1 — Tipos, control y funciones (~10 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Entorno TS strict y primer programa](M02/L01-entorno-ts-strict-y-primer-programa.md) | 2.5 |
| L02 | [Valores, primitivos y variables](M02/L02-valores-primitivos-y-variables.md) | 2.5 |
| L03 | [Control de flujo](M02/L03-control-de-flujo.md) | 3 |
| L04 | [Funciones tipadas](M02/L04-funciones-tipadas.md) | 2.5 |

### Semana 2 — Arrays, objetos y narrowing (~11 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Arrays y métodos esenciales](M02/L05-arrays-y-metodos-esenciales.md) | 2.5 |
| L06 | [Objetos, interfaces y tipos](M02/L06-objetos-interfaces-y-tipos.md) | 3 |
| L07 | [map, filter y reduce](M02/L07-map-filter-y-reduce.md) | 3 |
| L08 | [Union types y narrowing](M02/L08-union-types-y-narrowing.md) | 2.5 |

### Semana 3 — Módulos, fs y CLI (~11 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [Módulos ES en Node](M02/L09-modulos-es-en-node.md) | 2.5 |
| L10 | [Leer y escribir archivos con fs](M02/L10-fs-leer-y-escribir.md) | 3 |
| L11 | [argv y diseño de CLI](M02/L11-argv-y-diseno-de-cli.md) | 2.5 |
| L12 | [Script JSON y reporte (P2)](M02/L12-script-json-y-reporte-p2.md) | 3 |

### Semana 4 — Asincronía (~11 h)

| ID | Lección | ~h |
|----|---------|----|
| L13 | [Promises y el modelo mental async](M02/L13-promises-y-modelo-mental.md) | 2.5 |
| L14 | [async/await en la práctica](M02/L14-async-await-en-la-practica.md) | 3 |
| L15 | [fetch y APIs JSON](M02/L15-fetch-y-apis-json.md) | 2.5 |
| L16 | [Integrar async en el proyecto](M02/L16-integrar-async-en-el-proyecto.md) | 3 |

### Semana 5 — Errores, estilo y tests (~11 h)

| ID | Lección | ~h |
|----|---------|----|
| L17 | [Errores, throw y mensajes](M02/L17-errores-throw-y-mensajes.md) | 2.5 |
| L18 | [Validación y código legible](M02/L18-validacion-y-codigo-legible.md) | 3 |
| L19 | [Vitest — primeros tests](M02/L19-vitest-primeros-tests.md) | 2.5 |
| L20 | [Suite de tests (P3)](M02/L20-suite-de-tests-p3.md) | 3 |

### Semana 6 — Proyecto CLI y cierre (~11 h)

| ID | Lección | ~h |
|----|---------|----|
| L21 | [CLI — dominio y persistencia](M02/L21-cli-dominio-y-persistencia.md) | 3 |
| L22 | [Comandos stats y pulido UX](M02/L22-comandos-stats-y-pulido-ux.md) | 3 |
| L23 | [Export CSV y entrega final CLI](M02/L23-export-csv-y-entrega-final-cli.md) | 2.5 |
| L24 | [Cierre M02 y evidencias](M02/L24-cierre-m02-y-evidencias.md) | 2.5 |

Empieza por **[L01](M02/L01-entorno-ts-strict-y-primer-programa.md)** hoy.

## Ejemplo — función tipada + test

```ts
export function sumar(a: number, b: number): number {
  return a + b;
}

// sumar.test.ts
import { expect, test } from "vitest";
import { sumar } from "./sumar";

test("suma positivos", () => {
  expect(sumar(2, 3)).toBe(5);
});
```

## Lecturas (mapa rápido)

Canon: *Eloquent JavaScript* (trad. ES) + [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/) + inicio de *Código limpio* (ed. ES). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos / secciones | Alternativa gratis |
|--------|-----------|----------------------|--------------------|
| 1 | L01–L04 | EJ **caps. 1–3** + TS Handbook *Basic Types* / *Everyday Types* | https://eloquentjavascript.net/ + Handbook EN |
| 2 | L05–L08 | EJ **caps. 4–5** + TS *Narrowing* | Misma URL |
| 3 | L09–L12 | EJ **cap. 10** + Node docs `fs` + TS *Modules* | MDN JS (ES) módulos + Node docs |
| 4 | L13–L16 | EJ **cap. 11** + `fetch` (MDN ES) | Misma URL |
| 5 | L17–L20 | EJ **cap. 8** + Vitest *Getting Started* + *Código limpio* **caps. 2–3** | Docs Vitest; CC en biblioteca |
| 6 | L21–L24 | Repaso guiado + proyecto CLI; opcional EJ **cap. 7** (robot) | — |

**Regla:** cada capítulo de EJ lleva **ejercicios hechos**, no solo lectura.

## Prácticas

1. **P1:** 20 katas (Codewars/Exercism filtro fácil-medio) en TS. Repo `projects/m02-katas/`. Avance por lecciones L02–L04 y cierre en L16.
2. **P2:** Script que lea un JSON y genere un reporte; maneja archivos faltantes con errores claros (L12).
3. **P3:** Vitest con ≥10 tests pasando (`npm test`) (L19–L20).

## Proyecto útil — CLI de hábitos

Requisitos mínimos:

- Comandos: `add`, `list`, `done`, `stats`, `export --csv`.
- Persistencia en archivo JSON local (`projects/m02-habits/data/`).
- Tipos estrictos (`strict: true`).
- README con ejemplos de uso.
- Tests de la lógica de dominio.

Construcción guiada: L11 (esqueleto) → L14 (async) → L18 (`done`) → L21–L23 (dominio, stats, export).

## Errores comunes

- Desactivar `strict` “para que compile”.
- Copiar soluciones de katas sin reescribirlas.
- Meter toda la lógica en un solo `index.ts` de 400 líneas.
- Tests que solo comprueban `true === true`.
- Marcar lecciones sin cumplir “Hecho cuando”.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Katas:** Repo `projects/m02-katas/` con ≥20 soluciones TS + README.
- **P2 — Script:** Script que lee JSON y reporta; maneja archivo faltante con error claro.
- **P3 — Tests:** `npm test` verde con ≥10 tests Vitest.
- **Proyecto — CLI:** Comandos add/list/done/stats/export; JSON local; README con ejemplos.

## Criterios de dominio

- [ ] Escribes un programa de ~200 líneas sin tutorial paso a paso.
- [ ] Explicas sync vs async.
- [ ] Tus tests fallan cuando rompes la lógica a propósito.
- [ ] La CLI la usarías tú durante al menos una semana real.
