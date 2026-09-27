---
id: L09
materia: M06
orden: 9
titulo: Union types y modelado de estados
horas: 5
semana: 3
lectura: "TS Handbook — Unions and Intersection Types"
evidencia: "Tipos de estado discriminated union + tests"
---

# L09 — Union types y modelado de estados

**~5 h · Semana 3**

Los union types modelan estados mutuamente excluyentes mejor que `boolean` sueltos.

## Objetivo

Modelar estados de préstamo/libro (o tu dominio) con **discriminated unions**; eliminar flags inconsistentes (`prestado` + `fechaDevolucion` sin sentido).

## Pasos

### 1. Lectura (45 min)

Handbook: union types, literal types.

### 2. Diseño (60 min)

```ts
type EstadoLibro =
  | { tipo: "disponible" }
  | { tipo: "prestado"; hasta: Date }
  | { tipo: "reservado"; por: string };
```

Adapta a tu dominio.

### 3. Migración (120 min)

Refactor entidades; actualiza métodos y tests.

### 4. Funciones totales (90 min)

`function puedePrestar(estado: EstadoLibro): boolean` con switch exhaustivo (`never` en default).

### 5. Commit (15 min)

`refactor(m06): union types para estados`

## Hecho cuando

1. Estados inválidos no representables en tipos (en la medida posible).
2. Switch exhaustivo con `assertNever`.
3. Tests actualizados.

## Errores comunes

- `string` libre donde cabe union literal.
- Mezclar null y union sin criterio.

## Siguiente

[L10 — Narrowing y type guards](L10-narrowing-y-type-guards.md)
