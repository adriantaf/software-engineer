---
id: L06
materia: M17
orden: 6
titulo: API citas — crear y listar con reglas
horas: 5.0
semana: 2
lectura: REST + validación horarios
evidencia: POST/GET /citas
---

# L06 — API citas — crear y listar con reglas

**~5.0 h · Semana 2**

Core del piloto: `POST/GET /citas` con auth y reglas de horario.

## Objetivo

Crear/listar citas; 201/400/409; listado filtrable por fecha; 401 sin auth.

## Pasos (hazlos en orden)

### 1. Contratos OpenAPI o tabla (20 min)

Documenta body: clienteId, servicioId, inicio, notas. Errores esperados.

### 2. Implementa endpoints (90–110 min)

Validación + regla solapamiento → 409. Listar exige sesión y filtra por negocio.

### 3. Tests (40–50 min)

201 feliz; 400 fin≤inicio; 409 solape; 401 sin cookie.

### 4. Commit

`feat(m17): l06 api citas crear listar`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | REST + validación horarios | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. POST/GET citas (artefacto: `POST/GET /citas`).
2. Reglas testeadas (artefacto: `POST/GET /citas`).
3. 401 sin auth (artefacto: `POST/GET /citas`).
4. Commit `docs(m17): L06 api-citas-crear-y-listar-con-reglas`.

## Errores comunes

- Listar sin auth.
- Timezone ignorada.

## Siguiente

[L07 — CRUD clientes y servicios](L07-crud-clientes-y-servicios.md)
