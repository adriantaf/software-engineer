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

Servicios definen duración y precio base para pedidos.

## Objetivo

CRUD completo clientes y servicios con autorización owner/staff según matriz preliminar.

## Conceptos clave

- CRUD
- servicio
- cliente

## Pasos (hazlos en orden)

### 1. CRUD clientes (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/clientes \
  -H 'content-type: application/json' \
  -d '{"nombre":"Ana Demo","telefono":"+525500000000"}'
curl -sS -b /tmp/ao.ck http://localhost:3000/clientes
```

### 2. CRUD servicios (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/servicios \
  -H 'content-type: application/json' \
  -d '{"nombre":"Corte","duracionMin":30,"precioCentavos":25000}'
curl -sS -b /tmp/ao.ck http://localhost:3000/servicios
```

PATCH/DELETE según matriz (staff no borra si owner-only).

### 3. Tests + commit (40 min)

```bash
npm test -- clientes servicios
git add projects/m17-vitrina
git commit -m "feat(m17): L07 crud clientes y servicios"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | SRS RF clientes/servicios | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. CRUD `/clientes` y `/servicios` autenticados.
2. Tests mínimos create/list (+ delete owner-only si aplica).
3. Commit `docs(m17): L07 crud-clientes-y-servicios`.

## Errores comunes

- DELETE servicio sin chequear rol.
- Teléfonos reales de clientes en seeds de test.

## Siguiente

[L08 — Seeds demo y datos design partner](L08-seeds-demo-y-datos-design-partner.md)
