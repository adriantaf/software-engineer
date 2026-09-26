---
id: L08
materia: M14
orden: 8
titulo: Tests de regresión en API pública del módulo
horas: 5.0
semana: 2
lectura: Tests de contrato/API pública; no internals
evidencia: tests de regresión sobre exports públicos + nota
---

# L08 — Tests de regresión en API pública del módulo

**~5.0 h · Semana 2**

Los patrones van a mover archivos. Los tests deben anclar el *comportamiento* exportado.

## Objetivo

Capa de regresión sobre la API pública de `projects/m14-patrones`.

## Pasos (hazlos en orden)

### 1. Define superficie pública (30 min)

`src/index.ts` reexporta lo estable.

### 2. Tests de contrato (80–100 min)

Casos: precio promo, notifier channel, agendar ok/conflicto.

### 3. Nota + commit

`test(m14): regresion api publica modulos`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Proteger el comportamiento público tras refactors de patrones | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Suite que ejercita exports públicos (pricing, factory, facade) en verde.
2. `docs/regresion-api-publica.md` lista qué es “contrato” vs detalle interno.
3. Commit `test(m14): regresion api publica modulos`.

## Errores comunes

- Tests acoplados a nombres privados.
- Borrar tests “porque cambió el patrón”.
- Cobertura solo de archivos vacíos.

## Siguiente

[L09 — Observer para eventos de dominio](L09-observer-para-eventos-de-dominio.md)
