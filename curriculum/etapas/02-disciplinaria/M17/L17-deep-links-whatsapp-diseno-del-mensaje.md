---
id: L17
materia: M17
orden: 17
titulo: Deep links WhatsApp — diseño del mensaje
horas: 5.0
semana: 5
lectura: Docs proveedor WhatsApp
evidencia: projects/m17-agenda-ops/docs/integracion-whatsapp.md
---

# L17 — Deep links WhatsApp — diseño del mensaje

**~5.0 h · Semana 5**

Canal que el design partner ya usa: wa.me con plantilla mínima de PII.

## Objetivo

`docs/integracion-whatsapp.md` con plantilla, placeholders y ejemplo URL-encoded.

## Pasos (hazlos en orden)

### 1. Diseña mensaje (50–60 min)

Ej.: “Hola {nombre}, te recordamos tu cita el {fecha} a las {hora}”. Sin notas clínicas sensibles.

### 2. Construye deep link (40 min)

Documenta `https://wa.me/52XXXXXXXXXX?text=...` y límites (no es API oficial).

### 3. Opt-in (30 min)

Cómo el negocio obtiene consentimiento; qué no harás (spam).

### 4. Commit

`docs(m17): l17 diseno deep link whatsapp`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Docs proveedor WhatsApp | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Doc plantilla (artefacto: `projects/m17-agenda-ops/docs/integracion-whatsapp.md`).
2. Sin secrets (artefacto: `projects/m17-agenda-ops/docs/integracion-whatsapp.md`).
3. Commit (artefacto: `projects/m17-agenda-ops/docs/integracion-whatsapp.md`).

## Errores comunes

- API keys en front.
- Teléfono en logs.

## Siguiente

[L18 — Botón enviar recordatorio desde ficha cita](L18-boton-enviar-recordatorio-desde-ficha-cita.md)
