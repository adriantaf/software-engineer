---
id: L19
materia: M17
orden: 19
titulo: Confirmación de cita y estados
horas: 5.0
semana: 5
lectura: Flujo estado cita
evidencia: campo estado + UI
---

# L19 — Confirmación de cita y estados

**~5.0 h · Semana 5**

Staff y owner deben ver el mismo estado.

## Objetivo

Estados confirmada/pendiente/cancelada visibles y coherentes API↔UI.

## Conceptos clave

- estado
- sincronización
- cancelación

## Pasos (hazlos en orden)

### 1. Estados de cita (60–80 min)

```sql
-- enum o check: pendiente | confirmada | cancelada | atendida
ALTER TABLE citas ADD COLUMN estado TEXT NOT NULL DEFAULT 'pendiente';
```

API PATCH `/citas/:id/estado` con authz.

### 2. UI + tests (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/citas/<id>/estado \
  -H 'content-type: application/json' \
  -d '{"estado":"confirmada"}'
npm test -- citas
```

### 3. Commit (15 min)

```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L19 confirmacion estados cita"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Flujo estado cita | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Campo/enum `estado` en citas + PATCH autenticado; tests verdes.
2. Commit `docs(m17): L19 confirmacion-de-cita-y-estados`.

## Errores comunes

- Estados libres sin check/enum.
- Transiciones sin authz.

## Siguiente

[L20 — Cierre P3 integración WhatsApp](L20-cierre-p3-integracion-whatsapp.md)
