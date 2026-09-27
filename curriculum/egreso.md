# Rúbrica de egreso (titulación interna)

No es título oficial. Meta de dominio: **SaaS vertical Vitrina** en producción. Ver [producto-saas.md](producto-saas.md).

## Checklist

- [ ] **SaaS web en producción:** multi-tenant (`tenant_id`), auth, roles, tests, CI, deploy HTTPS, backups **con restore probado**.
- [ ] **≥2 tenants demo** con datos aislados (prueba A no lee B).
- [ ] **Menú + pedidos** por tenant (WhatsApp / pago al recoger; checkout online opcional).
- [ ] **Billing Stripe test mode** + landing de precios de la plataforma (Free/Pro del negocio).
- [ ] **Temas:** ≥2 built-in + 1 tema de terceros en catálogo e instalable.
- [ ] **Onboarding** de un negocio nuevo sin intervención manual tuya (o con runbook ≤15 min).
- [ ] **SRS + diseño** (diagramas + trust boundaries + modelo de tenancy).
- [ ] **App móvil o desktop** conectada al mismo backend (p. ej. staff: cola de pedidos).
- [ ] **AppSec (M18):** threat model + ≥5 hallazgos OWASP corregidos con tests.
- [ ] **Ciberseguridad aplicada (M25):** security review con **cross-tenant** + tabletop + hardening.
- [ ] **Portfolio ED/algoritmos** (implementación + complejidad).
- [ ] **10 demos/trials** documentadas (M22) + al menos 1 piloto pagado o carta de intención / trial activo serio.
- [ ] **Video o demo en vivo** (arquitectura, tenancy, amenaza cross-tenant) **sin tutorial**.
- [ ] **Inglés:** progreso hacia B1 lectura técnica.

## Entregables del proyecto integrador (M26)

1. Repositorio público del SaaS.
2. Memoria técnica: ICP, arquitectura, multi-tenant, Stripe (suscripción + checkout comensal opcional), temas, seguridad, métricas.
3. URL prod + landing de plataforma + instructivo deploy/runbook.
4. Tests (≥70% lógica de negocio) + tests anti-IDOR **cross-tenant** + XSS básico.
5. Registro comercial en `projects/m22-bektor/` / `projects/m26-capstone/`.

## Criterio de “aprobado”

Puedes levantar (o extender) el núcleo del SaaS con auth + tenancy + menú/pedidos + deploy + tests en un fin de semana sin tutorial paso a paso, **y** demuestras aislamiento entre tenants.
