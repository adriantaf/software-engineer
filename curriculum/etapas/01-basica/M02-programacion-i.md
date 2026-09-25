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

**En cristiano:** aprendes TypeScript de verdad con katas, un script real y tests. El cierre es una CLI de hábitos que puedes enseñar.

## Análogos

- UABC: Metodología de la Programación, Programación Estructurada
- Tec: Pensamiento computacional y programación

## Objetivos

1. Dominar tipos básicos, funciones, arrays, objetos, asincronía.
2. Leer errores del compilador y corregirlos sin pánico.
3. Escribir tests unitarios pequeños.
4. Entregar un CLI usable por ti mismo.

## Cómo estudiar esta materia

- Código todos los días (aunque sean 45 min de katas).
- Activa `"strict": true` desde el primer `tsconfig`.
- Cuando un error de tipos aparezca: **léelo completo** antes de googlear.
- El CLI del proyecto se construye de a poco desde la semana 3, no al final.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura + tipado | 6–8 | EJ / Handbook según tabla Lecturas |
| Katas / labs | 6–8 | Exercism/Codewars en TS strict |
| Proyecto CLI | 4–6 | `projects/m02-habits/` + Vitest |
| Retro | 1 | 3 dudas tipadas resueltas |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)

1. Crea el proyecto:
   ```bash
   mkdir -p projects/m02-katas && cd projects/m02-katas
   npm init -y
   npm install -D typescript tsx vitest @types/node
   npx tsc --init
   ```
2. En `tsconfig.json` deja `strict` en `true`.
3. Escribe `src/hola.ts`:
   ```ts
   function saludar(nombre: string): string {
     return `Hola, ${nombre}`;
   }
   console.log(saludar("Adrian"));
   ```
4. Ejecuta: `npx tsx src/hola.ts`
5. Rompe el tipo a propósito (`saludar(42)`) y lee el error del compilador.
6. Empieza el capítulo 1 de *Eloquent JavaScript* (ES) y resuelve 2 ejercicios en TS.

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

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Tipos, variables, control de flujo, funciones |
| 2 | Arrays, objetos, `map`/`filter`/`reduce`, tipado |
| 3 | Módulos, `fs`, CLI args (`process.argv`) |
| 4 | Async/await, Promises, fetch básico |
| 5 | Errores, validación, Vitest |
| 6 | Proyecto CLI + pulido |

## Lecturas

Canon: *Eloquent JavaScript* (trad. ES) + [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/) + inicio de *Código limpio* (ed. ES). Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos / secciones | Alternativa gratis |
|--------|----------------------|--------------------|
| 1 | EJ **caps. 1–3** (valores/tipos; estructura; funciones) + TS Handbook *Basic Types* / *Everyday Types* | https://eloquentjavascript.net/ + Handbook EN |
| 2 | EJ **caps. 4–5** (objetos/arrays; funciones de orden superior) + TS *Narrowing* | Misma URL |
| 3 | EJ **cap. 10** (módulos) + Node docs `fs` + TS *Modules* | MDN JS (ES) módulos + Node docs |
| 4 | EJ **cap. 11** (asíncrono) + `fetch` (MDN ES) | Misma URL |
| 5 | EJ **cap. 8** (bugs y errores) + Vitest *Getting Started* + *Código limpio* **caps. 2–3** (nombres; funciones) | Docs Vitest; CC en biblioteca |
| 6 | Repaso guiado + proyecto CLI (sin capítulo nuevo obligatorio); opcional EJ **cap. 7** (proyecto robot) como inspiración | — |

**Regla:** cada capítulo de EJ lleva **ejercicios hechos**, no solo lectura.

## Prácticas

1. **P1:** 20 katas (Codewars/Exercism filtro fácil-medio) en TS. Repo `projects/m02-katas/`.
2. **P2:** Script que lea un JSON y genere un reporte; maneja archivos faltantes con errores claros.
3. **P3:** Vitest con ≥10 tests pasando (`npm test`).

## Proyecto útil — CLI de hábitos

Requisitos mínimos:

- Comandos: `add`, `list`, `done`, `stats`, `export --csv`.
- Persistencia en archivo JSON local.
- Tipos estrictos (`strict: true`).
- README con ejemplos de uso.
- Tests de la lógica de dominio.

## Errores comunes

- Desactivar `strict` “para que compile”.
- Copiar soluciones de katas sin reescribirlas.
- Meter toda la lógica en un solo `index.ts` de 400 líneas.
- Tests que solo comprueban `true === true`.

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
