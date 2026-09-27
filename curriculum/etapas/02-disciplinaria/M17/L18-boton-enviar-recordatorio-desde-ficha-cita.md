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

Cierra loop operativo del negocio.

## Objetivo

En UI de cita, acción que abre WhatsApp o registra intento según diseño.

## Conceptos clave

- acción usuario
- auditoría ligera
- opt-in

## Pasos (hazlos en orden)

### 1. Botón en ficha cita (70–90 min)

Acción “Enviar recordatorio” abre `wa.me` (window.open). No requiere WhatsApp Business API.

### 2. Evidencia (30 min)

```bash
# captura redactada o nota en integracion-whatsapp.md con URL de ejemplo sin teléfono real
echo "ej: https://wa.me/525500000000?text=..." >> projects/m17-agenda-ops/docs/integracion-whatsapp.md
```

### 3. Commit (15 min)

```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L18 boton recordatorio whatsapp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | UI + API log | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Botón recordatorio en ficha cita abre wa.me; evidencia en doc WhatsApp.
2. Commit `docs(m17): L18 boton-enviar-recordatorio-desde-ficha-cita`.

## Errores comunes

- Botón que llama API Business inexistente.
- Abrir wa.me con PII extra innecesaria.

## Siguiente

[L19 — Confirmación de cita y estados](L19-confirmacion-de-cita-y-estados.md)
