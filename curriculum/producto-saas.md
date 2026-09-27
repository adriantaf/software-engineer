# Producto del plan: SaaS vertical “Vitrina”

Nombre de trabajo (puedes cambiar el branding). Este es el **hilo de producto** de M12 → M26 y el destino de Bektor.

## Visión

Software de **menú digital + pedidos** vendido por **suscripción** a comida rápida y barras de bebidas (café, boba, matcha, jugos, etc.). El producto principal es el **menú público**; la landing del negocio es opcional.

No eres agencia de “páginas web”. Eres el operador de un **SaaS vertical**.

## Por qué este producto (tendencias + tu contexto)

- Vertical SaaS > herramientas horizontales genéricas para un fundador solo.
- Menú + WhatsApp + pago al recoger (y checkout online opcional) es un workflow real en locales pequeños.
- Temas Free/Pro + catálogo para desarrolladores enseña marketplace acotado sin distraer del core.
- Enseña ingeniería seria: multi-tenant, billing, aislamiento, ops, AppSec.

## ICP (cliente ideal)

- Dueño de **QSR o barra de bebidas** (un local; a veces 1–2 puntos).
- Hoy usa WhatsApp + menú en PDF/Instagram/historias.
- Paga **MXN/mes** si le ordena el menú, reduce confusión de pedidos y le da un link serio (no si solo “se ve bonito”).

Elige **un** sub-vertical y no cambies cada semana (ej. solo bobas, o solo cafés/matcha).

## Evolución técnica (camino obligatorio)

| Fase | Materias | Qué entregas |
|------|----------|--------------|
| Piloto single-tenant | M12–M17 | Un local design partner; auth, menú, pedidos WA, admin, HTTPS |
| Camino a SaaS | M17 cierre → M19–M21 | `tenants`, `tenant_id`, onboarding, staging/prod |
| Comercialización | M22 | Planes Free/Pro, precio MXN, trials = demos |
| AI por tenant | M23 | FAQ/RAG del menú y políticas **scoped** por tenant |
| Seguridad SaaS | M18 + M25 | OWASP + **aislamiento cross-tenant** + tabletop |
| Egreso | M26 | SaaS live: ≥2 tenants, Stripe test, temas, runbook |

## MVP SaaS (definición de “listo para egreso”)

Funcional:

- [ ] Alta de tenant (negocio) + usuario owner
- [ ] Menú (categorías, ítems, precios, disponibilidad) **aislado por tenant**
- [ ] Pedidos con estados (recibido / listo / entregado) y cliente mínimo (nombre + WhatsApp)
- [ ] Perfil público: **menú** (core) + landing opcional
- [ ] Pedido por **WhatsApp** (`wa.me` con mensaje prefijado) y **pago al recoger** (default)
- [ ] Flag por tenant: pedido online + **Stripe Checkout** (test) si lo activa
- [ ] Roles (owner / staff) dentro del tenant
- [ ] Landing de la **plataforma** con precios Free/Pro + checkout Stripe test (suscripción del negocio)
- [ ] Temas: ≥2 built-in (1 free, 1 pro/preview) + catálogo con **1 tema de terceros** instalable
- [ ] (M23) Asistente FAQ **solo** con docs/menú de ese tenant

Técnico:

- [ ] `tenant_id` en todas las filas de negocio
- [ ] Tests: usuario del tenant A **no** lee datos del B (IDOR cross-tenant)
- [ ] Secrets fuera del repo; HTTPS en prod; backup + restore probado
- [ ] CI verde (lint, test, audit básico)

## Billing (fijado)

**Stripe** en modo test.

**Suscripción del negocio** (ajusta números con evidencia de M22):

- Free: menú con límite bajo de ítems, 1 tema free, sin landing rica, sin pago online
- Pro: más ítems, temas pro, landing opcional, flag de checkout online

**Pago del comensal (opcional):** Stripe Checkout test cuando el tenant lo active; default = pagar al recoger.

**Temas de terceros de paga (egreso):** listados en catálogo + checkout a la plataforma; reparto a creadores **documentado**. Stripe Connect / payouts reales = **v1.1** (no bloquea egreso).

No uses PayPal como billing primario del aprendizaje.

## Métricas (aunque sean “test”)

Documenta en `projects/m26-capstone/metricas.md`:

- Tenants creados (demo)
- Trials iniciados (M22)
- MRR teórico en test (si hubiera pagos reales)
- Activación: % tenants con ≥1 ítem de menú publicado y ≥1 pedido de prueba en 7 días
- Temas instalados / tema de terceros listado

## Qué no es el producto

- Agencia “te hago tu página”
- Delivery propio / flotas
- CRM genérico de citas (ese hilo quedó fuera a propósito)
- WhatsApp Business API de pago como requisito de v1 (el MVP usa deep-link `wa.me`)
- Marketplace de apps completo; solo **temas** acotados
- Chatbot genérico sin menú ni pedido

## Lecturas relacionadas

- [Hilo producto](hilos/producto.md) — mapa de artefactos M12→M26
- [M17](etapas/02-disciplinaria/M17-aplicaciones-web.md) · [M22](etapas/03-terminal/M22-emprendimiento.md) · [M26](etapas/03-terminal/M26-proyecto-integrador.md)
- [Egreso](egreso.md) · [Hilo seguridad](hilos/seguridad.md)
