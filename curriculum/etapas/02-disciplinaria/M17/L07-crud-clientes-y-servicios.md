---
id: L07
materia: M17
orden: 7
titulo: CRUD clientes y servicios
horas: 5.0
semana: 2
lectura: SRS RF clientes/servicios
evidencia: /clientes /servicios
---

# L07 — CRUD clientes y servicios

**~5.0 h · Semana 2**

Servicios definen duración/precio; clientes son PII — trázalos al SRS.

## Objetivo

CRUD `/clientes` y `/servicios` con auth y 404 coherente.

## Pasos (hazlos en orden)

### 1. Endpoints (100–120 min)

Create/read/update/(soft)delete. Validar teléfono/nombre. No mezclar clientes entre negocios.

### 2. Tests (40–50 min)

Feliz + 404 + 401. Update servicio cambia duración usada en citas nuevas (documenta comportamiento).

### 3. Commit

`feat(m17): l07 crud clientes servicios`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | SRS RF clientes/servicios | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. CRUD ambos recursos (artefacto: `/clientes /servicios`).
2. Tests (artefacto: `/clientes /servicios`).
3. Commit (artefacto: `/clientes /servicios`).

## Errores comunes

- Mezclar cliente entre negocios.
- Sin validación.

## Siguiente

[L08 — Seeds demo y datos design partner](L08-seeds-demo-y-datos-design-partner.md)
