---
id: L10
materia: M14
orden: 10
titulo: Command para acciones admin reversibles
horas: 5.0
semana: 3
lectura: Command; undo de acción admin
evidencia: src/admin/ command cancelar/restaurar + tests
---

# L10 — Command para acciones admin reversibles

**~5.0 h · Semana 3**

Owner cancela por error. Command te da vocabulario para execute/undo en el panel admin.

## Objetivo

Command reversible de cancelación + tests.

## Pasos (hazlos en orden)

### 1. Interfaz Command (25 min)

### 2. CancelCitaCommand (70–80 min)

Guarda estado previo para undo.

### 3. Tests + ADR + commit

`feat(m14): command admin reversible`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Command: encapsular acción admin con undo | [Refactoring.Guru — Command (ES)](https://refactoring.guru/es/design-patterns/command) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Command con `execute`/`undo` para cancelar cita (o cambiar estado).
2. Test: execute → estado cancelada; undo → restaurada.
3. Commit `feat(m14): command admin reversible`.

## Errores comunes

- Command sin undo cuando el enunciado lo pide.
- Guardar UI clicks como commands innecesarios.
- Undo que ignora invariantes (restaurar sobre slot ya ocupado — documenta).

## Siguiente

[L11 — Cierre P1 — Strategy, Observer y Factory](L11-cierre-p1-strategy-observer-y-factory.md)
