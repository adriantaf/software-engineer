---
id: L13
materia: M26
orden: 13
titulo: Pedido WhatsApp y pago al recoger (perfil)
horas: 5.0
semana: 4
lectura: producto-saas — pedido WA + flag pago online
evidencia: projects/m26-capstone/integraciones.md
---

# L13 — Pedido WhatsApp y pago al recoger (perfil)

**~5 h · Semana 4**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/integraciones.md`**.

## Objetivo

Perfil público del tenant: menú + botón **Pedir por WhatsApp** (`wa.me`) con mensaje prefijado; default **pago al recoger**. Documenta el flag futuro/activo de checkout online.

## Pasos (hazlos en orden)

### 1. Spec en integraciones.md (40 min)

Tabla por tenant: teléfono WA, plantilla de mensaje, pago default, ¿checkout online activado?

### 2. Implementa / verifica deep-link (90–120 min)

- Genera `https://wa.me/<tel>?text=` con ítems + total.
- Sin WhatsApp Business API en v1.
- Si el tenant tiene `pago_online=true`, documenta enlace a Stripe Checkout (L17–L19); si no, solo al recoger.

### 3. Commit (15 min)

```bash
git add projects/m26-capstone/integraciones.md
git commit -m "docs(m26): l13 pedido whatsapp perfil"
```

## Hecho cuando

1. Al menos 1 tenant demo con pedido WA reproducible.
2. `integraciones.md` describe pago al recoger vs online.
3. Commit en git.

## Errores comunes

- Exigir API oficial de WhatsApp para egreso.
- Mezclar el teléfono del comensal con el del negocio en `wa.me`.

## Siguiente

[L14 — App móvil M20 conectada o plan cierre](L14-app-movil-m20-conectada-o-plan-cierre.md)
