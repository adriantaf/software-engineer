---
id: L19
materia: M02
orden: 19
titulo: Vitest — primeros tests
horas: 2.5
semana: 5
lectura: Vitest Getting Started
evidencia: 'vitest.config + ≥3 tests en habits o katas (parseArgv, validar, reporte)'
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3 exige ≥10 tests. Hoy instalas el hábito: red → verde → refactor.


      **Objetivo de esta lección:** `npm test` verde con al menos 3 casos útiles
      (no `expect(true).toBe(true)`).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Config
    xp: 10
    cuerpo: |-
      ```ts
      import { defineConfig } from "vitest/config";

      export default defineConfig({
        test: {
          include: ["src/**/*.test.ts"],
        },
      });
      ```

      `vitest.config.ts`: `package.json`: `"test": "vitest run"`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Tests de parseArgv
    xp: 10
    cuerpo: |-
      ```ts
      import { describe, expect, test } from "vitest";
      import { parseArgv } from "./comandos.js";

      describe("parseArgv", () => {
        test("add con nombre", () => {
          expect(parseArgv(["node", "cli", "add", "Correr"])).toEqual({
            tipo: "add",
            nombre: "Correr",
          });
        });

        test("list", () => {
          expect(parseArgv(["node", "cli", "list"])).toEqual({ tipo: "list" });
        });

        test("sin comando → help", () => {
          expect(parseArgv(["node", "cli"])).toEqual({ tipo: "help" });
        });
      });
      ```

      `src/comandos.test.ts`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Vitest — primeros tests», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`npm test` pasa con ≥3 tests significativos.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Vitest — primeros tests
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Tests que solo comprueban tipos o
      constantes."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          `npm test` verde con al menos 3 casos útiles (no
          `expect(true).toBe(true)`).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Test de dominio
    xp: 10
    cuerpo: Tests para `validarNombreHabito` o `formatearReporte` (P2).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`npm test` pasa con ≥3 tests significativos.'
      - Rompiste a propósito una aserción y viste el test fallar.
      - 'Commit `test(m02): vitest parseArgv`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L19 — Vitest — primeros tests

**~2.5 h · Semana 5**

Configuras Vitest en `m02-habits` (o katas) y escribes tests que **fallan** cuando rompes la lógica.

## Objetivo

`npm test` verde con al menos 3 casos útiles (no `expect(true).toBe(true)`).

## Por qué importa

P3 exige ≥10 tests. Hoy instalas el hábito: red → verde → refactor.

## Pasos

### 1. Config (25 min)

`vitest.config.ts`:

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["src/**/*.test.ts"],
  },
});
```

`package.json`: `"test": "vitest run"`.

### 2. Tests de parseArgv (45 min)

`src/comandos.test.ts`:

```ts
import { describe, expect, test } from "vitest";
import { parseArgv } from "./comandos.js";

describe("parseArgv", () => {
  test("add con nombre", () => {
    expect(parseArgv(["node", "cli", "add", "Correr"])).toEqual({
      tipo: "add",
      nombre: "Correr",
    });
  });

  test("list", () => {
    expect(parseArgv(["node", "cli", "list"])).toEqual({ tipo: "list" });
  });

  test("sin comando → help", () => {
    expect(parseArgv(["node", "cli"])).toEqual({ tipo: "help" });
  });
});
```

### 3. Test de dominio (40 min)

Tests para `validarNombreHabito` o `formatearReporte` (P2).

### 4. Vitest docs (30 min)

[Getting Started](https://vitest.dev/guide/) — `describe`, `test`, `expect`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Vitest | [Getting Started](https://vitest.dev/guide/) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `npm test` pasa con ≥3 tests significativos.
2. Rompiste a propósito una aserción y viste el test fallar.
3. Commit `test(m02): vitest parseArgv`.

## Errores comunes

- Tests que solo comprueban tipos o constantes.
- No aislar funciones puras (todo mockeado innecesariamente).
- Olvidar extensión `.js` en imports en tests.

## Siguiente

[L20 — Suite de tests (P3)](L20-suite-de-tests-p3.md)
