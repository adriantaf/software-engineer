---
id: L06
materia: M15
orden: 6
titulo: Tests de integración con persistencia
horas: 5.0
semana: 2
lectura: Tests de integración DB; isolation
evidencia: tests/integration/ con Postgres o SQLite documentado
---

# L06 — Tests de integración con persistencia

**~5.0 h · Semana 2**

El fake miente a veces. Un test real de persistencia ancla el Repository Postgres (o el que elegiste en M13).

## Objetivo

Carpeta `tests/integration/` con evidencia P1 (segunda capa).

## Pasos (hazlos en orden)

### 1. Elige estrategia (40 min)

Documenta en README: Docker compose service `db_test`, o SQLite solo para spike.

### 2. Test save/find (80–100 min)

### 3. Script npm `test:integration` (30 min)

### 4. Commit

`test(m15): integracion persistencia`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Integración: repository real contra DB de prueba | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Al menos 1 test de integración que escribe/lee cita en DB de prueba (Docker PG, Testcontainers, o SQLite — documenta cuál).
2. Setup/teardown o transacciones que no dejen basura.
3. Commit `test(m15): integracion persistencia`.

## Errores comunes

- Usar la DB de desarrollo con datos del design partner.
- Tests de integración mezclados sin tag/carpeta.
- Sin documentar cómo levantar la DB en README.

## Siguiente

[L07 — Tests HTTP de API — auth y validación](L07-tests-http-de-api-auth-y-validacion.md)
