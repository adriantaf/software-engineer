---
id: L05
materia: M15
orden: 5
titulo: Fake repositorio y reloj para tests rápidos
horas: 5.0
semana: 2
lectura: Fakes vs mocks; reloj inyectable
evidencia: InMemory repo + Clock fake + tests de servicio
---

# L05 — Fake repositorio y reloj para tests rápidos

**~5.0 h · Semana 2**

Los tests de application layer deben ser rápidos y deterministas.

## Objetivo

Fakes de repo y reloj cableados al service de pedidos.

## Pasos (hazlos en orden)

### 1. Puerto Clock (30 min)

### 2. InMemoryCitaRepository (50–60 min) — reutiliza M14 si existe

### 3. Tests de servicio (60–70 min)

### 4. Commit

`test(m15): fake repo y reloj`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Fakes: repo en memoria y reloj determinista | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `FakeClock` o `() => Date` inyectable; test de “pedido en el pasado” estable.
2. Repo in-memory usado por tests de application service.
3. Commit `test(m15): fake repo y reloj`.

## Errores comunes

- Mock de cada método del repo sin estado (frágil).
- `Date.now` global sin restore.
- Fake más complejo que producción.

## Siguiente

[L06 — Tests de integración con persistencia](L06-tests-de-integracion-con-persistencia.md)
