---
id: L09
materia: M14
orden: 9
titulo: Observer para eventos de dominio
horas: 5.0
semana: 3
lectura: Observer; cita creada → listeners
evidencia: src/events/ observer + tests + ADR
---

# L09 — Observer para eventos de dominio

**~5.0 h · Semana 3**

Crear cita no debería conocer todos los side-effects. Observer (o event emitter tipado) desacopla.

## Objetivo

Evento `CitaCreada` + listeners + tests + ADR.

## Pasos (hazlos en orden)

### 1. Tipos de evento (30 min)

### 2. Emitter + subscribe (60–70 min)

### 3. Integra en facade o service mínimo (40 min)

### 4. Tests + ADR + commit

`feat(m14): observer eventos de dominio`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Observer/eventos de dominio: desacoplar efectos al crear cita | [Refactoring.Guru — Observer (ES)](https://refactoring.guru/es/design-patterns/observer) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Emisor de `CitaCreada` con ≥2 listeners (p. ej. audit log + notify stub).
2. Tests: al crear, ambos listeners reciben el evento.
3. Commit `feat(m14): observer eventos de dominio`.

## Errores comunes

- Observer síncrono que rompe el flujo si un listener lanza — documenta política.
- Event bus global Singleton sin necesidad.
- Listeners que mutan la cita a espaldas del aggregate.

## Siguiente

[L10 — Command para acciones admin reversibles](L10-command-para-acciones-admin-reversibles.md)
