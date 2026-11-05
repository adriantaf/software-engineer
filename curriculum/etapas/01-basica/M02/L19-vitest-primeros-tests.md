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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `npm test` verde con al menos 3 casos útiles (no
      `expect(true).toBe(true)`).


      P3 exige ≥10 tests. Hoy instalas el hábito: red → verde → refactor.
  - id: s2
    tipo: ejemplo
    titulo: 1. Config
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Vitest — primeros tests" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: >-
          vitest.config + ≥3 tests en habits o katas (parseArgv, validar,
          reporte)
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
      ¿Es buena práctica en esta lección? “Tests que solo comprueban tipos o
      constantes."
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
          `npm test` verde con al menos 3 casos útiles (no
          `expect(true).toBe(true)`).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tests de parseArgv
    xp: 10
    cuerpo: |-
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
  - id: s7
    tipo: explicacion
    titulo: 3. Test de dominio
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
