# Producto de la academia: SaaS vertical “Agenda Ops”

Nombre de trabajo (puedes cambiar el branding). Este es el **hilo de producto** de M12 → M26 y el destino de Bektor.

## Visión

Software de **citas + clientes + panel** vendido por **suscripción** a negocios de servicio locales (default ICP: salones, clínicas o talleres en Ensenada / Baja California).

No eres agencia de “páginas web”. Eres el operador de un **SaaS vertical**.

## Por qué este producto (tendencias + tu contexto)

- Vertical SaaS > herramientas horizontales genéricas para un fundador solo.
- Scheduling/ops + pagos + (luego) AI sobre el workflow es un patrón 2026 viable.
- Encaja con lo que ya construyes en M12–M17 y con demos locales reales.
- Enseña ingeniería seria: multi-tenant, billing, aislamiento, ops, AppSec.

## ICP (cliente ideal)

- Dueño de negocio de **servicios con citas** (1–3 sucursales o un solo local).
- Hoy usa WhatsApp + libretas / Excel.
- Paga **MXN/mes** si le ahorra no-shows y desorden (no si solo “se ve bonito”).

Elige **un** sub-vertical y no cambies cada semana (ej. solo barberías, o solo consultorios).

## Evolución técnica (camino obligatorio)

| Fase | Materias | Qué entregas |
|------|----------|--------------|
| Piloto single-tenant | M12–M17 | Un negocio design partner; auth, citas, admin, HTTPS |
| Camino a SaaS | M17 cierre → M19–M21 | `tenants`, `tenant_id`, onboarding, staging/prod |
| Comercialización | M22 | Planes Free/Pro, precio MXN, trials = demos |
| AI por tenant | M23 | FAQ/RAG scoped; sin mezclar datos entre tenants |
| Seguridad SaaS | M18 + M25 | OWASP + **aislamiento cross-tenant** + tabletop |
| Egreso | M26 | SaaS live: ≥2 tenants, Stripe test, landing, runbook |

## MVP SaaS (definición de “listo para egreso”)

Funcional:

- [ ] Alta de tenant (negocio) + usuario owner
- [ ] Servicios, citas, clientes **aislados por tenant**
- [ ] Roles (owner / staff) dentro del tenant
- [ ] Landing con precios + checkout **Stripe test mode**
- [ ] Panel admin del tenant usable sin ti
- [ ] WhatsApp deep-link o equivalente de contacto
- [ ] (M23) Asistente FAQ **solo** con docs de ese tenant

Técnico:

- [ ] `tenant_id` en todas las filas de negocio
- [ ] Tests: usuario del tenant A **no** lee datos del B (IDOR cross-tenant)
- [ ] Secrets fuera del repo; HTTPS en prod; backup + restore probado
- [ ] CI verde (lint, test, audit básico)

## Billing (fijado)

**Stripe** en modo test. Planes sugeridos (ajusta números con evidencia de M22):

- Free: 1 calendario, límites bajos (para trial)
- Pro: citas ilimitadas razonables + recordatorios / export

No uses PayPal como billing primario del aprendizaje.

## Métricas (aunque sean “test”)

Documenta en `projects/m26-capstone/metricas.md`:

- Tenants creados (demo)
- Trials iniciados (M22)
- MRR teórico en test (si hubiera pagos reales)
- Activación: % tenants con ≥1 cita creada en 7 días

## Qué no es el producto

- Agencia “te hago tu página”
- Field-service pesado (flotas/dispatch) en el primer egreso
- Marketplace
- Chatbot genérico sin workflow de citas

## Lecturas relacionadas

- [Hilo producto](hilos/producto.md) — mapa de artefactos M12→M26
- [M17](etapas/02-disciplinaria/M17-aplicaciones-web.md) · [M22](etapas/03-terminal/M22-emprendimiento.md) · [M26](etapas/03-terminal/M26-proyecto-integrador.md)
- [Egreso](egreso.md) · [Hilo seguridad](hilos/seguridad.md)
