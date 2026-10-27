---
id: L19
materia: M17
orden: 19
titulo: Confirmación de pedido y estados
horas: 5.0
semana: 5
lectura: Flujo estado pedido
evidencia: campo estado + UI
---

# L19 — Confirmación de pedido y estados

**~5.0 h · Semana 5**

Staff y owner deben ver el mismo estado.

## Objetivo

Estados confirmada/pendiente/cancelada visibles y coherentes API↔UI.

## Conceptos clave

- estado
- sincronización
- cancelación

## Pasos (hazlos en orden)

### 1. Estados de pedido (60–80 min)

```sql
-- enum o check: pendiente | confirmada | cancelada | atendida
ALTER TABLE pedidos ADD COLUMN estado TEXT NOT NULL DEFAULT 'pendiente';
```

API PATCH `/pedidos/:id/estado` con authz.

### 2. UI + tests (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/pedidos/<id>/estado \
  -H 'content-type: application/json' \
  -d '{"estado":"confirmada"}'
npm test -- pedidos
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L19 confirmacion estados pedido"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Flujo estado pedido | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Campo/enum `estado` en pedidos + PATCH autenticado; tests verdes.
2. Commit `docs(m17): L19 confirmacion-de-pedido-y-estados`.

## Errores comunes

- Estados libres sin check/enum.
- Transiciones sin authz.

## Siguiente

[L20 — Cierre P3 integración WhatsApp](L20-cierre-p3-integracion-whatsapp.md)
