---
id: L01
materia: M14
orden: 1
titulo: Entorno M14 y Strategy de precios
horas: 5.0
semana: 1
lectura: GoF/Refactoring.Guru Strategy; precios Vitrina
evidencia: projects/m14-patrones/ con Vitest + Strategy precios + tests
---

# L01 — Entorno M14 y Strategy de precios

**~5.0 h · Semana 1**

Patrones sin repo ejecutable son vocabulario vacío. Hoy levantas Vitest y cobras tarifas del piloto con Strategy.

## Objetivo

Dejar `projects/m14-patrones/` usable y un Strategy de precios con tests.

## Por qué empieza así

Vitrina tendrá promo, tarifa base y (luego) pedido abandonado. Strategy evita `switch` esparcidos en el service de pedidos.

## Pasos (hazlos en orden)

### 1. Revisa scaffold (20 min)

```bash
ls projects/m14-patrones
cat projects/m14-patrones/README.md
```

Si aún no hay `package.json`, créalo en el siguiente paso (el scaffold del repo ya puede traer stubs).

### 2. Init TypeScript + Vitest (50–70 min)

```bash
cd projects/m14-patrones
npm init -y
npm install -D typescript vitest @types/node
npx tsc --init --strict --rootDir src --outDir dist
```

`package.json`:

```json
{
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest"
  }
}
```

### 3. Implementa Strategy (70–90 min)

`src/pricing/strategy.ts`:

```ts
export type CalculoPrecio = { calcular(base: number): number };

export const tarifaBase: CalculoPrecio = { calcular: (b) => b };
export const tarifaPromoDiez: CalculoPrecio = {
  calcular: (b) => Math.round(b * 0.9 * 100) / 100,
};

export function totalServicio(base: number, s: CalculoPrecio): number {
  return s.calcular(base);
}
```

Tests en `src/pricing/strategy.test.ts` (≥3 casos).

### 4. ADR corto (30–40 min)

`adr/strategy-precios.md`: contexto (promos del salón/clínica), decisión, por qué no `if` en el controller.

### 5. Commit (15 min)

```bash
git add projects/m14-patrones
git commit -m "feat(m14): strategy de precios con tests"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Strategy: familia de algoritmos intercambiables (tarifas) | [Refactoring.Guru — Strategy (ES)](https://refactoring.guru/es/design-patterns/strategy) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m14-patrones/` tiene `package.json` con script `test` (Vitest) y TypeScript strict.
2. Strategy de precios (p. ej. base / promo −10 %) con ≥3 tests verdes.
3. `adr/strategy-precios.md` justifica el patrón; commit `feat(m14): strategy de precios con tests`.

## Errores comunes

- Un `if` gigante llamado “Strategy” sin interfaz/tipo común.
- Tests que solo verifican mocks.
- Subir `node_modules/`.

## Siguiente

[L02 — Factory Method para notificadores de canal](L02-factory-method-para-notificadores-de-canal.md)
