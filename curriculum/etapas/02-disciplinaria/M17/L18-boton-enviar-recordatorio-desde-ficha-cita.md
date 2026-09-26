---
id: L18
materia: M17
orden: 18
titulo: Botón enviar recordatorio desde ficha cita
horas: 5.0
semana: 5
lectura: UI + API log
evidencia: acción recordatorio
---

# L18 — Botón enviar recordatorio desde ficha cita

**~5.0 h · Semana 5**

Cierra el loop operativo: desde la ficha, abrir WhatsApp o registrar intento.

## Objetivo

Acción en UI + log sanitizado (sin teléfono completo si puedes) + pasos de prueba manual.

## Pasos (hazlos en orden)

### 1. API/UI acción (80–100 min)

Botón “Recordar por WhatsApp” genera link o abre ventana. Confirmación anti-spam.

### 2. Auditoría ligera (30 min)

Tabla/log: citaId, userId, timestamp — no dump de mensaje con PII.

### 3. Prueba manual (20 min)

Pasos en `docs/integracion-whatsapp.md`.

### 4. Commit

`feat(m17): l18 boton recordatorio whatsapp`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | UI + API log | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Acción en UI (artefacto: `acción recordatorio`).
2. Log sanitizado (artefacto: `acción recordatorio`).
3. Test manual pasos (artefacto: `acción recordatorio`).
4. Commit `docs(m17): L18 boton-enviar-recordatorio-desde-ficha-cita`.

## Errores comunes

- Spam sin confirmación.
- Log con teléfono.

## Siguiente

[L19 — Confirmación de cita y estados](L19-confirmacion-de-cita-y-estados.md)
