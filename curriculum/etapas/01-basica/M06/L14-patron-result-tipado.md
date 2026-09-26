---
id: L14
materia: M06
orden: 14
titulo: Patrón Result tipado
horas: 5
semana: 4
lectura: "Notas M06 + ejemplo Result en ficha; artículos sobre Result/Either"
evidencia: "API principal devuelve Result; helpers map/flatMap opcionales"
---

# L14 — Patrón Result tipado

**~5 h · Semana 4**

`Result<T, E>` hace explícito el fracaso sin depender solo de excepciones.

## Objetivo

Implementar `Result` genérico y migrar operaciones core (`prestar`, `agregar`) a retorno `Result`.

## Pasos

### 1. Tipo base (60 min)

```ts
export type Ok<T> = { ok: true; value: T };
export type Err<E> = { ok: false; error: E };
export type Result<T, E = string> = Ok<T> | Err<E>;
```

### 2. Helpers (60 min)

`ok()`, `err()`, `map`, `flatMap` (opcional pero recomendado).

### 3. Migración API (120 min)

Elige: excepciones solo en frontera CLI; dominio usa Result.

### 4. Tests (60 min)

Casos ok y err tipados (`E` union de códigos literales).

### 5. Documentación (30 min)

En README interno, cuándo usar Result vs throw.

## Hecho cuando

1. Operaciones principales exportan Result.
2. Callers manejan `ok` con narrowing.
3. Tests cubren ambos caminos.

## Errores comunes

- Result con `error: any`.
- Mezclar throw y Result sin regla.

## Siguiente

[L15 — Tests de borde: null, vacío, duplicados (P3)](L15-tests-de-borde-p3.md)
