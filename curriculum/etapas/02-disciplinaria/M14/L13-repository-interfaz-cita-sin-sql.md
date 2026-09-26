---
id: L13
materia: M14
orden: 13
titulo: Repository — interfaz Cita sin SQL
horas: 5.0
semana: 4
lectura: Repository; puerto de persistencia
evidencia: src/citas/cita-repository.ts + InMemory + ADR (P2 inicio)
---

# L13 — Repository — interfaz Cita sin SQL

**~5.0 h · Semana 4**

P2: capas backend alineadas a M13. Empiezas por el puerto de persistencia.

## Objetivo

`CitaRepository` + impl in-memory + ADR.

## Pasos (hazlos en orden)

### 1. Tipos de dominio Cita (30 min) — alineados a M13

### 2. Interfaz + InMemory (70–90 min)

### 3. Tests + ADR + commit

`feat(m14): repository cita sin sql`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Repository: interfaz de dominio sin SQL; impl in-memory | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `CitaRepository` con `findById`/`save` (y filtro por dueño/negocio si aplica).
2. `InMemoryCitaRepository` + tests; **cero** SQL en el dominio.
3. Commit `feat(m14): repository cita sin sql`.

## Errores comunes

- Interfaz que expone `query(sql: string)`.
- Repo que es solo un alias del ORM entity.
- Sin tests del in-memory.

## Siguiente

[L14 — Service — capa aplicación de citas](L14-service-capa-aplicacion-de-citas.md)
