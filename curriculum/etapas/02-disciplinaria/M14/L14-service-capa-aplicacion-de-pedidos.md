---
id: L14
materia: M14
orden: 14
titulo: Service — capa aplicación de pedidos
horas: 5.0
semana: 4
lectura: Application service; orquestación y authz
evidencia: src/pedidos/pedido-service.ts + tests (P2)
---

# L14 — Service — capa aplicación de pedidos

**~5.0 h · Semana 4**

El service es lo que M13 llamó application layer: orquesta dominio + puertos.

## Objetivo

`CitaService` testeable sin HTTP.

## Pasos (hazlos en orden)

### 1. API del service (40 min)

`crear`, `cancelar`, `listarDelDia`.

### 2. Implementación (70–90 min)

Inyecta repo (+ clock + notifier opcionales).

### 3. Tests P2 + README + commit

`feat(m14): service capa aplicacion pedidos`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Service de aplicación: reglas + repo; sin HTTP ni SQL | [Refactoring.Guru — Patrones (ES)](https://refactoring.guru/es/design-patterns) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `CitaService` usa `CitaRepository` y valida solape/rol (stub de auth ok).
2. Tests de servicio con repo in-memory (P2 evidenciado).
3. Commit `feat(m14): service capa aplicacion pedidos`.

## Errores comunes

- Service que importa Express.
- Authz solo “si rol en string del DTO” sin explicación.
- Duplicar facade y service sin roles claros — documenta relación.

## Siguiente

[L15 — Refactor P3 — módulo legacy antes y después](L15-refactor-p3-modulo-legacy-antes-y-despues.md)
