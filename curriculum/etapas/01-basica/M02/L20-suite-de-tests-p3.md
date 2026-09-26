---
id: L20
materia: M02
orden: 20
titulo: Suite de tests (P3)
horas: 3
semana: 5
lectura: "Vitest — matchers y casos borde"
evidencia: "npm test verde con ≥10 tests de dominio (habits + reportes)"
---

# L20 — Suite de tests (P3)

**~3 h · Semana 5**

Completas la **práctica P3**: ≥10 tests de lógica de dominio, sin tocar red ni disco real en la mayoría.

## Objetivo

Cobertura de validación, parse, reportes y funciones sobre `Habito[]` — tests rápidos y deterministas.

## Por qué importa

La evidencia P3 es binaria: `npm test` verde y conteo ≥10. La CLI confiable se sostiene aquí.

## Pasos

### 1. Inventario de funciones puras (20 min)

Lista en `TESTING.md` qué funciones merecen test (dominio, no `main`).

### 2. Ampliar suite (100 min)

Apunta a ≥10 tests totales, por ejemplo:

- `parseArgv` (3+)
- `validarNombreHabito` (3+)
- `formatearReporte` / `totalMarcados` (4+)

Usa `describe` por módulo.

### 3. Casos borde (40 min)

Nombre vacío, JSON de reporte con `items: []`, hábito sin completados en stats futuro.

### 4. CI local (20 min)

Documenta en README: `npm test` antes de cada commit de features.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Vitest | [Matchers](https://vitest.dev/api/expect.html) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `npm test` → ≥10 tests passing.
2. `TESTING.md` o README explica qué cubre cada grupo.
3. Listo para marcar **P3** en la ficha con evidencia.

## Errores comunes

- Tests que leen `habits.json` real (frágiles).
- Un solo test gigante.
- No correr tests tras refactor L18.

## Siguiente

[L21 — CLI: dominio y persistencia](L21-cli-dominio-y-persistencia.md)
