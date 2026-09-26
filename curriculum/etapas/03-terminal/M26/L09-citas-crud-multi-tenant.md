---
id: L09
materia: M26
orden: 9
titulo: Citas CRUD multi-tenant
horas: 5.0
semana: 3
lectura: Paridad M17 sin hardcode piloto
evidencia: projects/m26-capstone/memoria/citas-crud.md
---

# L09 — Citas CRUD multi-tenant

**~5 h · Semana 3**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/citas-crud.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

CRUD de citas multi-tenant con tests de aislamiento en el camino crítico.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Regresión
- tenant_id en queries

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Paridad M17 sin hardcode piloto_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Matriz CRUD citas (25–35 min)

En `projects/m26-capstone/memoria/citas-crud.md` tabla create/read/update/cancel × status esperado por tenant.

### 3. Implementa/verifica flujos + aislamiento (100–130 min)

Ejecuta create/edit/cancel en A y B. Ningún hardcode de un solo design partner.

```bash
# create en A
curl -s -X POST "$API/citas" -H "Authorization: Bearer $TOKEN_A" \
  -H "Content-Type: application/json" \
  -d '{"servicio_id":"…","cliente_id":"…","starts_at":"2026-10-01T16:00:00Z"}'

# A intenta leer cita de B → 403/404
curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A" "$API/citas/$CITA_B"
```

Pega status codes en la memoria.

### 4. Test mínimo (30–40 min)

Añade o enlaza test de regresión. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l09 citas-crud-multi-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Paridad M17 sin hardcode piloto | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/citas-crud.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L10 — Clientes y servicios por tenant](L10-clientes-y-servicios-por-tenant.md)
