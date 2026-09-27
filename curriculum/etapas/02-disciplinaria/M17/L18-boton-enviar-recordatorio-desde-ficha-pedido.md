---
id: L18
materia: M17
orden: 18
titulo: Botón pedido WhatsApp desde el perfil / ficha
horas: 5.0
semana: 5
lectura: UI + wa.me
evidencia: acción pedido WhatsApp
---

# L18 — Botón pedido WhatsApp desde el perfil / ficha

**~5.0 h · Semana 5**

Cierra el loop del comensal: ve el menú → arma mensaje → abre WhatsApp.

## Objetivo

En el perfil público (o preview), acción que abre `wa.me` con el pedido prefijado (ítems + total + “pago al recoger”).

## Conceptos clave

- deep-link `wa.me`
- mensaje prefijado
- sin WhatsApp Business API en v1

## Pasos (hazlos en orden)

### 1. Generar texto del pedido (40 min)

Función pura: lista de líneas → string URL-encoded. Ejemplo:

`Hola, quiero pedir:%0A- 2x Matcha latte%0ATotal: $130%0APago al recoger.`

### 2. Botón en UI (70–90 min)

Acción “Pedir por WhatsApp” hace `window.open` a `https://wa.me/<telefonoNegocio>?text=...`. No requiere WhatsApp Business API.

### 3. Evidencia (30 min)

```bash
echo "ej: https://wa.me/525500000000?text=..." >> projects/m17-vitrina/docs/integracion-whatsapp.md
git add projects/m17-vitrina
git commit -m "feat(m17): L18 pedido whatsapp wa.me"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| producto-saas | Pedido WhatsApp MVP | [producto-saas](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Botón abre `wa.me` con ítems del carrito/pedido de prueba.
2. Evidencia en `integracion-whatsapp.md` (teléfono demo/redactado).
3. Commit `feat(m17): L18 pedido whatsapp wa.me`.

## Errores comunes

- Exigir API oficial de WhatsApp en el piloto.
- Mandar el teléfono del cliente en la URL (el link es al negocio).

## Siguiente

[L19 — Confirmación de pedido y estados](L19-confirmacion-de-pedido-y-estados.md)
