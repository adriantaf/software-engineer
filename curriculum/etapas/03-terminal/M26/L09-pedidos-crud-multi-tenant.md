---
id: L09
materia: M26
orden: 9
titulo: Pedidos CRUD multi-tenant
horas: 5.0
semana: 3
lectura: Paridad M17 sin hardcode piloto
evidencia: projects/m26-capstone/memoria/pedidos-crud.md
---

# L09 — Pedidos CRUD multi-tenant

**~5 h · Semana 3**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/pedidos-crud.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

CRUD de pedidos multi-tenant con tests de aislamiento en el camino crítico (menú → pedido → estados).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Regresión
- `tenant_id` en queries
- Snapshot de precio por línea

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _Paridad M17 sin hardcode piloto_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Matriz CRUD pedidos (25–35 min)

En `projects/m26-capstone/memoria/pedidos-crud.md` tabla create/read/update estado × status esperado por tenant.

### 3. Implementa/verifica flujos + aislamiento (100–130 min)

Ejecuta create + cambio de estado en A y B. Ningún hardcode de un solo design partner.

```bash
# create en A
curl -s -X POST "$API/orders" -H "Authorization: Bearer $TOKEN_A" \
  -H "Content-Type: application/json" \
  -d '{"canal":"whatsapp","pago":"al_recoger","items":[{"menuItemId":"…","cantidad":2}]}'

# A intenta leer pedido de B → 403/404
curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A" "$API/orders/$ORDER_B"
```

Pega status codes en la memoria.

### 4. Test mínimo (30–40 min)

Añade o enlaza test de regresión cross-tenant. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l09 pedidos-crud-multi-tenant"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | Paridad M17 sin hardcode piloto | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Create/list/estado de pedidos funciona en ≥2 tenants.
2. A no lee pedidos de B (evidencia HTTP + test).
3. Memoria `pedidos-crud.md` en git.

## Errores comunes

- Reusar IDs de menú del tenant A en el tenant B.
- Confiar en el precio enviado por el cliente.

## Siguiente

[L10 — Menú por tenant](L10-menu-por-tenant.md)
