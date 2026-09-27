---
id: L02
materia: M15
orden: 2
titulo: Tests unitarios puros de reglas de pedido
horas: 5.0
semana: 1
lectura: Código limpio cap. pruebas; reglas de solape/estado
evidencia: tests/domain/ reglas de pedido ≥5 tests
---

# L02 — Tests unitarios puros de reglas de pedido

**~5.0 h · Semana 1**

La base de la pirámide: reglas que el dueño del negocio nota si fallan (doble booking).

## Objetivo

Suite unitaria de dominio de pedidos sin DB ni HTTP.

## Pasos (hazlos en orden)

### 1. Extrae regla (40–50 min)

Ejemplo:

```ts
export function rangesOverlap(aStart: Date, aEnd: Date, bStart: Date, bEnd: Date): boolean {
  return aStart < bEnd && bStart < aEnd;
}
```

### 2. Tabla de casos (60–70 min)

Adyacentes, contenidos, idénticos, invertidos (`end < start` → throw/invalid).

### 3. Red→green (30 min)

Rompe la función, mira fallar, restaura — anota en `docs/red-green-pedido.md`.

### 4. Commit

`test(m15): reglas de pedido unitarias`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Unit tests puros: sin I/O; reglas de pedido | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Funciones de dominio (solape, transición de estado, o validar rango) con ≥5 tests.
2. Al menos un test que **falla** si rompes la regla a propósito (red→green documentado en nota breve).
3. Commit `test(m15): reglas de pedido unitarias`.

## Errores comunes

- Tests que levantan servidor HTTP para una resta de fechas.
- Asserts débiles (`toBeTruthy` en objetos).
- Reglas duplicadas en test y producción divergentes.

## Siguiente

[L03 — Qué no testear y carpetas de coverage](L03-que-no-testear-y-carpetas-de-coverage.md)
