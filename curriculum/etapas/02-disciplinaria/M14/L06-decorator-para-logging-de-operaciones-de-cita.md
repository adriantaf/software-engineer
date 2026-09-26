---
id: L06
materia: M14
orden: 6
titulo: Decorator para logging de operaciones de cita
horas: 5.0
semana: 2
lectura: Decorator; logging sin ensuciar el core
evidencia: src/citas/ decorator logger + tests
---

# L06 — Decorator para logging de operaciones de cita

**~5.0 h · Semana 2**

Quieres auditoría de “quién creó cita” sin contaminar el dominio con Winston.

## Objetivo

Decorator de logging sobre operaciones de cita.

## Pasos (hazlos en orden)

### 1. Interfaz CitaOps (30 min)

`create`, `cancel` mínimos (pueden ser in-memory).

### 2. LoggingCitaOps (60–70 min)

Delega + empuja a un `LogSink` inyectable.

### 3. Tests (40 min) + ADR + commit

`feat(m14): decorator logging citas`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Decorator: añade logging cruzando la misma interfaz | [Refactoring.Guru — Decorator (ES)](https://refactoring.guru/es/design-patterns/decorator) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Decorador envuelve un `CitaOps` (o similar) y registra llamada sin cambiar el resultado.
2. Test demuestra que el inner se invoca y que el log recibe evento.
3. Commit `feat(m14): decorator logging citas`.

## Errores comunes

- Meter `console.log` dentro de la regla de solape.
- Decorator que cambia reglas de negocio “de paso”.
- Sin interfaz común inner/outer.

## Siguiente

[L07 — Facade para el flujo agendar cita](L07-facade-para-el-flujo-agendar-cita.md)
