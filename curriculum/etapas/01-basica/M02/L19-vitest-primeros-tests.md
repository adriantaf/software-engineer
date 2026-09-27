---
id: L19
materia: M02
orden: 19
titulo: Vitest — primeros tests
horas: 2.5
semana: 5
lectura: "Vitest Getting Started"
evidencia: "vitest.config + ≥3 tests en habits o katas (parseArgv, validar, reporte)"
---

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
