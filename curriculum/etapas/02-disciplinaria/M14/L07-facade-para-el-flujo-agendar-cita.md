---
id: L07
materia: M14
orden: 7
titulo: Facade para el flujo agendar cita
horas: 5.0
semana: 2
lectura: Facade; orquestar validación + persistencia + notify
evidencia: src/citas/agendar-facade.ts + tests
---

# L07 — Facade para el flujo agendar cita

**~5.0 h · Semana 2**

El caso de uso “agendar” toca varias piezas. Facade ofrece una puerta al application layer.

## Objetivo

Facade `agendarCita` + tests de feliz/error.

## Pasos (hazlos en orden)

### 1. Subsistemas stubs (40 min)

Validador de solape, repo in-memory, notifier no-op.

### 2. Facade (60–70 min)

Orquesta; traduce errores a resultados tipados.

### 3. Tests + ADR + commit

`feat(m14): facade agendar cita`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Facade: API simple sobre subsistema de agendar | [Refactoring.Guru — Facade (ES)](https://refactoring.guru/es/design-patterns/facade) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `agendarCita(...)` facade coordina validación + save + notify (stubs ok).
2. Test de flujo feliz y un fallo (p. ej. slot ocupado) sin que el caller toque 3 servicios.
3. Commit `feat(m14): facade agendar cita`.

## Errores comunes

- Facade dios de 20 dependencias.
- Duplicar reglas fuera y dentro del facade.
- Sin test del camino de error.

## Siguiente

[L08 — Tests de regresión en API pública del módulo](L08-tests-de-regresion-en-api-publica-del-modulo.md)
