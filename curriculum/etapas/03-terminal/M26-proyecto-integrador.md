---
id: M26
titulo: Proyecto integrador / titulación interna
etapa: terminal
orden: 26
semanas: 8
horas: 160
practicas:
  - id: p1
    titulo: Alcance SaaS congelado + plan de 8 semanas
  - id: p2
    titulo: Memoria técnica del SaaS v1
  - id: p3
    titulo: Demo pública / video del producto multi-tenant
proyecto:
  id: proj
  titulo: Agenda Ops SaaS en producción + egreso
---

# M26 — Proyecto integrador (SaaS)

## Por qué existe

Cierre del plan de ingeniería de software. El egreso interno es un **SaaS vertical en producción** — [Agenda Ops](../../producto-saas.md) multi-tenant — no un CRUD suelto ni un portafolio de tutoriales. Integra M17 (piloto), M19 (ops), M22 (comercial), M25 (security review) y la rúbrica de [egreso.md](../../egreso.md).

**En resumen:** cierras el plan con Agenda Ops en producción: ≥2 tenants, Stripe test, evidencia de egreso.


## Objetivos de aprendizaje

Al terminar debes poder:

1. Congelar alcance SaaS v1 y ejecutar un plan de 8 semanas medible.
2. Operar **multi-tenant** con aislamiento demostrable (manual + tests).
3. Integrar billing en **Stripe test mode** (Checkout + webhooks verificados).
4. Mantener security review M25 vigente (cross-tenant, secretos, headers).
5. Entregar memoria técnica (arquitectura, tenancy, billing, seguridad).
6. Demostrar el producto en video público y cumplir la rúbrica de egreso.

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md), [producto-saas.md](../../producto-saas.md) y [egreso.md](../../egreso.md) en la semana 1.
- **Congela alcance** semana 1: MVP de la spec, no features infinitas.
- Cada semana: demo interna con **≥2 tenants** distintos.
- Billing y cross-tenant **no** se aplazan a la semana 8.
- Trabaja en `projects/m26-capstone/`; enlaza repos de app si viven aparte.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Build SaaS | 8–10 | Tenancy + features |
| Billing/sec | 4–6 | Stripe test + tests cross-tenant |
| Memoria/demo | 4–6 | Video + rúbrica egreso |
| Retro | 1 | Gaps honestos |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Abre o crea `projects/m26-capstone/` y alinea `projects/m26-capstone/alcance.md` con [producto-saas.md](../../producto-saas.md).
2. Marca el checklist de [egreso.md](../../egreso.md) en `projects/m26-capstone/egreso-checklist.md` (estado actual honesto).
3. Plan de **8 sprints** en `projects/m26-capstone/plan-8-semanas.md` con fecha de demo pública.
4. Stripe test: cuenta + productos/planes Free/Pro creados (wire parcial OK si está documentado).
5. Crea dos tenants de prueba nombrados (no “tenant1” genérico sin datos).
6. Commit, por ejemplo: `docs(m26): alcance congelado + plan 8 semanas`.

## Ejemplo — criterio de aislamiento (idea)

```text
Como usuario del tenant A con token válido:
  GET /api/citas/{id-de-cita-del-tenant-B} → debe ser 403 o 404, nunca 200 con datos ajenos.
Automatiza al menos un caso en CI.
```

Regla: el egreso exige explicar **IDOR cross-tenant** y cómo lo evitas.

## Temario semanal

### Semana 1 — Alcance, tenancy y riesgos (~20 h)

- `alcance.md` congelado: in/out scope SaaS v1.
- Modelo `tenant_id` en datos y middleware de resolución de tenant.
- Riesgos y dependencias (Stripe, hosting, M25 pendiente).
- Práctica P1 entregable: plan 8 semanas + alcance firmado por ti.

### Semana 2 — Multi-tenant y onboarding (~20 h)

- Registro de nuevo negocio (tenant) sin intervención manual tuya.
- Seeds o wizard mínimo; datos aislados por tenant.
- Demo: tenant A y B con nombres y datos distintos.

### Semana 3 — Features críticas del vertical (~20 h)

- Citas, clientes, servicios, admin — paridad razonable con piloto M17.
- Nada de hardcode del negocio piloto único.
- Tests de regresión en flujos críticos.

### Semana 4 — Features críticas (cont.) + integraciones (~20 h)

- WhatsApp / notificaciones si están en alcance congelado.
- App móvil M20 conectada o gap documentado con plan de cierre.
- Métricas mínimas (M22) registradas.

### Semana 5 — Stripe test y landing de precios (~20 h)

- Landing pública con planes Free/Pro.
- Checkout test mode; webhooks con verificación de firma.
- Usuario de prueba completa flujo de suscripción test.

### Semana 6 — Hardening, CI y M25 (~20 h)

- Security review M25 vigente; tests cross-tenant en pipeline.
- Backups, secretos, headers prod.
- Cierre de issues críticos de aislamiento.

### Semana 7 — Memoria técnica y métricas (~20 h)

- Práctica P2: memoria v1 en `projects/m26-capstone/memoria/` (tenancy, billing, seguridad, ops).
- Registro comercial / trials (M22) referenciado.
- Diagramas de arquitectura actualizados.

### Semana 8 — Demo, video y egreso (~20 h)

- Práctica P3: video público multi-tenant (sin tutorial de fondo).
- Demo en vivo opcional; checklist egreso completo.
- Post-mortem honesto: qué queda para v1.1.

## Lecturas

Canon: memoria técnica propia + [producto-saas](../../producto-saas.md) + rúbrica [egreso](../../egreso.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura / relectura | Uso |
|--------|---------------------|-----|
| 1 | [producto-saas.md](../../producto-saas.md) completo + egreso | `alcance.md` congelado |
| 2 | SRS (M12) + diseño (M13) — gaps multi-tenant | Onboarding tenant |
| 3 | Docs Stripe **test mode** (Checkout / Customer) | Productos Free/Pro |
| 4 | ADRs de tenancy del repo | Features críticas |
| 5 | Stripe Checkout + webhooks (test) | Landing precios |
| 6 | Informe M25 + OWASP access control | Tests cross-tenant + CI |
| 7 | Plantilla memoria + métricas M22 | Memoria v1 |
| 8 | Checklist egreso | Demo + video |

**Regla:** cada semana demo con ≥2 tenants; billing y seguridad no se aplazan.

## Prácticas

1. **P1 — Alcance:** `projects/m26-capstone/alcance.md` congelado + `plan-8-semanas.md`.
2. **P2 — Memoria:** `projects/m26-capstone/memoria/` con arquitectura, tenancy, billing, seguridad.
3. **P3 — Demo:** Enlace a video público en `projects/m26-capstone/demo.md` (multi-tenant visible).

## Proyecto útil

**Agenda Ops SaaS en producción + egreso** — evidencia central en `projects/m26-capstone/README.md`:

- URL de producción (o staging público acordado) con ≥2 tenants demo.
- Enlaces a repos de aplicación, infra y memoria.
- Estado de Stripe test, review M25 y app móvil (conectada o justificación escrita fuerte).
- Checklist [egreso.md](../../egreso.md) con capturas o hashes de commit de cierre.

## Entregables

1. **SaaS en producción** (Agenda Ops) con ≥2 tenants demo.
2. Landing de precios + checkout Stripe **test mode**.
3. Memoria técnica (arquitectura, tenancy, billing, seguridad).
4. App móvil/desktop conectada (o justificación fuerte documentada; por defecto se espera conexión).
5. Security review M25 vigente (cross-tenant).
6. Registro comercial M22 (trials/demos).
7. Video demo sin tutorial de fondo.

## Errores comunes

- Scope creep después de congelar alcance.
- Un solo tenant “de mentira” o datos compartidos entre negocios.
- Stripe solo en localhost sin webhook en entorno desplegado.
- Demo con secretos en claro o `.env` filtrado.
- Memoria genérica que no describe **tu** tenancy real.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Alcance:** `projects/m26-capstone/alcance.md` + `plan-8-semanas.md`.
- **P2 — Memoria:** `projects/m26-capstone/memoria/` completa.
- **P3 — Demo:** `projects/m26-capstone/demo.md` con URL de video público.
- **Proyecto — Egreso:** Prod + Stripe test + review M25 + evidencia M22 en README.

## Criterios de dominio

Cierre **final** del plan: demuestras dominio integrado, no solo materias sueltas.

- [ ] CRUD con auth + deploy + tests en un fin de semana **y** explicas aislamiento multi-tenant.
- [ ] Explicas IDOR cross-tenant y cómo lo previenes (demo + test).
- [ ] Checkout Stripe test completado al menos una vez de punta a punta.
- [ ] Video y memoria permiten a un tercero entender el SaaS sin tu voz en vivo.
- [ ] Checklist de egreso marcado con evidencia enlazada en `projects/m26-capstone/`.
