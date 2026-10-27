---
id: L07
materia: M15
orden: 7
titulo: Tests HTTP de API — auth y validación
horas: 5.0
semana: 2
lectura: Supertest/fetch contra app; 401 y 400
evidencia: tests/http/ login/pedidos 401 y 400
---

# L07 — Tests HTTP de API — auth y validación

**~5.0 h · Semana 2**

La pirámide necesita la capa que habla HTTP: el contrato que el front verá.

## Objetivo

Tests 401/400 contra API de prueba del piloto.

## Pasos (hazlos en orden)

### 1. Mini app (60–80 min)

Si M17 no existe, spike en `projects/m15-calidad/src/http/`.

### 2. Casos (60–70 min)

Tabla de la ficha M15: feliz opcional hoy; 401 y 400 obligatorios.

### 3. Commit

`test(m15): http auth y validacion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | HTTP tests: sin auth → 401; body inválido → 400 | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. App mínima (Express/Fastify/Hono o spike) con ruta protegida de pedidos.
2. Tests automatizados: sin cookie/token → 401; body inválido → 400.
3. Commit `test(m15): http auth y validacion`.

## Errores comunes

- Probar solo el happy path.
- Servidor global compartido sin aislamiento.
- Hardcodear secrets de prod.

## Siguiente

[L08 — IDOR y roles — casos 403](L08-idor-y-roles-casos-403.md)
