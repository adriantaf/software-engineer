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

Canal que el design partner ya usa.

## Objetivo

Definir plantilla mensaje recordatorio/confirmación con placeholders y enlace wa.me.

## Conceptos clave

- deep link
- plantilla
- PII mínima

## Pasos (hazlos en orden)

### 1. Diseña mensaje wa.me (50–60 min)

```bash
# plantilla (sin PII real en git):
# https://wa.me/52XXXXXXXXXX?text=Hola%20...%20cita%20...
```

Documenta en `projects/m17-agenda-ops/docs/integracion-whatsapp.md` campos: nombre, fecha, deep link ficha.

### 2. Helper URL encoder (40–50 min)

```ts
export function whatsappReminderUrl(phoneE164: string, text: string) {
  const n = phoneE164.replace(/\\D/g, "");
  return `https://wa.me/${n}?text=${encodeURIComponent(text)}`;
}
```

```bash
npm test -- whatsapp
```

### 3. Commit (15 min)

```bash
git add projects/m17-agenda-ops
git commit -m "docs(m17): L17 deep links whatsapp mensaje"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Docs proveedor WhatsApp | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-agenda-ops/docs/integracion-whatsapp.md` define plantilla wa.me + helper testeado.
2. Commit `docs(m17): L17 deep-links-whatsapp-diseno-del-mensaje`.

## Errores comunes

- Pegar teléfonos reales en el repo.
- Texto wa.me sin `encodeURIComponent`.

## Siguiente

[L18 — Botón enviar recordatorio desde ficha cita](L18-boton-enviar-recordatorio-desde-ficha-cita.md)
