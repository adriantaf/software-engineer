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

Staff y owner deben ver el mismo estado en API y UI.

## Objetivo

Estados pendiente/confirmada/cancelada/atendida coherentes; tests de transición.

## Pasos (hazlos en orden)

### 1. Modelo de estados (30 min)

Diagrama ASCII de transiciones permitidas.

### 2. API + UI (90–110 min)

PATCH estado con auth; UI refleja; cancelar respeta matriz.

### 3. Tests (30–40 min)

Transición ilegal → 400/409; sin auth → 401.

### 4. Commit

`feat(m17): l19 estados confirmacion cita`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Flujo estado cita | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Estados en API/UI (artefacto: `campo estado`).
2. Tests (artefacto: `campo estado`).
3. Commit (artefacto: `campo estado`).

## Errores comunes

- Estado solo en front.
- Cancelar sin auth.

## Siguiente

[L20 — Cierre P3 integración WhatsApp](L20-cierre-p3-integracion-whatsapp.md)
