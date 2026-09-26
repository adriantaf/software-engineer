---
id: L29
materia: M17
orden: 29
titulo: ADR tenant_id y modelo multi-negocio
horas: 5.0
semana: 8
lectura: producto-saas multi-tenant
evidencia: projects/m17-agenda-ops/docs/adr-tenant-id.md
---

# L29 — ADR tenant_id y modelo multi-negocio

**~5.0 h · Semana 8**

M26 depende de esta decisión; el piloto es single-tenant con cableado listo.

## Objetivo

`docs/adr-tenant-id.md`: dónde vive `tenant_id`/`negocio_id`, tablas, queries siempre filtradas.

## Pasos (hazlos en orden)

### 1. Contexto (30 min)

Relee producto-saas fases multi-tenant.

### 2. ADR (80–100 min)

Opciones; decisión; consecuencias; lista de tablas; qué **no** harás en M17 (SaaS completo).

### 3. Spot-check queries (30 min)

Al menos un listado de citas documenta filtro por negocio.

### 4. Commit

`docs(m17): l29 adr tenant id`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | producto-saas multi-tenant | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. adr-tenant-id.md (artefacto: `projects/m17-agenda-ops/docs/adr-tenant-id.md`).
2. Tablas listadas (artefacto: `projects/m17-agenda-ops/docs/adr-tenant-id.md`).
3. Commit (artefacto: `projects/m17-agenda-ops/docs/adr-tenant-id.md`).

## Errores comunes

- Multi-tenant completo día 1.
- Sin filtro en queries.

## Siguiente

[L30 — Checklist camino a SaaS](L30-checklist-camino-a-saas.md)
