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

## Cómo estudiar esta materia (lecciones)

M26 es el **capstone**: Agenda Ops SaaS en **producción** con L01–L32 (máxima profundidad del plan), evidencia en `projects/m26-capstone/` y repos de aplicación.

1. Orden **L01 → L32**; congela alcance en semana 1 y respétalo.
2. Cada semana: demo interna con **≥2 tenants** distintos.
3. Billing (Stripe test) y cross-tenant **no** se aplazan a la semana 8.
4. Memoria y video deben explicar **tu** tenancy real a un tercero.
5. [egreso.md](../../egreso.md) + [producto-saas](../../producto-saas.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Build SaaS (lecciones) | 10–12 | 4× ~5 h features/ops/billing |
| Seguridad / billing | 4–6 | M25 + Stripe webhooks |
| Memoria / demo | 4–6 | Video + rúbrica egreso |
| Retro | 1 | Gaps honestos |

Si un día solo tienes 2 h: **un entregable del sprint** (test, página, doc memoria).

## Lecciones

### Semana 1 — Alcance congelado y modelo tenancy (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Alcance SaaS v1 congelado](M26/L01-alcance-saas-v1-congelado.md) | 5 |
| L02 | [Plan 8 semanas y egreso-checklist honesto](M26/L02-plan-8-semanas-y-egreso-checklist-honesto.md) | 5 |
| L03 | [Modelo tenant_id y resolución de tenant](M26/L03-modelo-tenant-id-y-resolucion-de-tenant.md) | 5 |
| L04 | [Riesgos integrador y dependencias](M26/L04-riesgos-integrador-y-dependencias.md) | 5 |

### Semana 2 — Onboarding y dos tenants demo (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Onboarding self-service de nuevo tenant](M26/L05-onboarding-self-service-de-nuevo-tenant.md) | 5 |
| L06 | [Seeds y datos demo por tenant](M26/L06-seeds-y-datos-demo-por-tenant.md) | 5 |
| L07 | [Panel admin por tenant](M26/L07-panel-admin-por-tenant.md) | 5 |
| L08 | [Demo interna semana 2 — dos tenants](M26/L08-demo-interna-semana-2-dos-tenants.md) | 5 |

### Semana 3 — Features críticas — citas y catálogo (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Citas CRUD multi-tenant](M26/L09-citas-crud-multi-tenant.md) | 5 |
| L10 | [Clientes y servicios por tenant](M26/L10-clientes-y-servicios-por-tenant.md) | 5 |
| L11 | [Staff y permisos mínimos](M26/L11-staff-y-permisos-minimos.md) | 5 |
| L12 | [Tests regresión flujos críticos](M26/L12-tests-regresion-flujos-criticos.md) | 5 |

### Semana 4 — Integraciones, móvil y métricas (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Notificaciones o WhatsApp si en alcance](M26/L13-notificaciones-o-whatsapp-si-en-alcance.md) | 5 |
| L14 | [App móvil M20 conectada o plan cierre](M26/L14-app-movil-m20-conectada-o-plan-cierre.md) | 5 |
| L15 | [Métricas M22 en producto](M26/L15-metricas-m22-en-producto.md) | 5 |
| L16 | [Demo interna semana 4 — flujos completos](M26/L16-demo-interna-semana-4-flujos-completos.md) | 5 |

### Semana 5 — Stripe test y landing de precios (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L17 | [Stripe test — productos Free/Pro](M26/L17-stripe-test-productos-free-pro.md) | 5 |
| L18 | [Landing pública de precios](M26/L18-landing-publica-de-precios.md) | 5 |
| L19 | [Checkout test end-to-end](M26/L19-checkout-test-end-to-end.md) | 5 |
| L20 | [Webhooks Stripe verificados en deploy](M26/L20-webhooks-stripe-verificados-en-deploy.md) | 5 |

### Semana 6 — M25 vigente, CI y ops (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L21 | [Re-ejecutar review M25 y cerrar gaps](M26/L21-re-ejecutar-review-m25-y-cerrar-gaps.md) | 5 |
| L22 | [CI con tests cross-tenant obligatorios](M26/L22-ci-con-tests-cross-tenant-obligatorios.md) | 5 |
| L23 | [Backups prod y runbook ops](M26/L23-backups-prod-y-runbook-ops.md) | 5 |
| L24 | [Hardening final pre-demo pública](M26/L24-hardening-final-pre-demo-publica.md) | 5 |

### Semana 7 — Memoria técnica y comercial (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L25 | [Memoria — arquitectura y diagramas](M26/L25-memoria-arquitectura-y-diagramas.md) | 5 |
| L26 | [Memoria — tenancy, billing, seguridad](M26/L26-memoria-tenancy-billing-seguridad.md) | 5 |
| L27 | [Registro comercial M22 y trials](M26/L27-registro-comercial-m22-y-trials.md) | 5 |
| L28 | [Métricas y post-mortem técnico v1](M26/L28-metricas-y-post-mortem-tecnico-v1.md) | 5 |

### Semana 8 — Demo pública y egreso (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L29 | [Video demo público multi-tenant](M26/L29-video-demo-publico-multi-tenant.md) | 5 |
| L30 | [Checklist egreso con evidencia enlazada](M26/L30-checklist-egreso-con-evidencia-enlazada.md) | 5 |
| L31 | [README capstone índice maestro](M26/L31-readme-capstone-indice-maestro.md) | 5 |
| L32 | [Cierre integrador y handoff v1.1](M26/L32-cierre-integrador-y-handoff-v1-1.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: memoria propia + [producto-saas](../../producto-saas.md) + [egreso](../../egreso.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura / relectura | Uso |
|--------|-----------|---------------------|-----|
| 1 | L01–L04 | producto-saas + egreso | `alcance.md`, tenancy |
| 2 | L05–L08 | SRS M12 / diseño M13 | Onboarding tenants |
| 3 | L09–L12 | ADRs API M17 | CRUD multi-tenant |
| 4 | L13–L16 | M24 go/no-go, M20 README | Integraciones |
| 5 | L17–L20 | Stripe Checkout + webhooks | Landing + test mode |
| 6 | L21–L24 | Informe M25 | CI cross-tenant |
| 7 | L25–L28 | Métricas M22 | Memoria v1 |
| 8 | L29–L32 | Checklist egreso | Video + README capstone |

**Regla:** cada semana demo ≥2 tenants; producción o staging público acordado.



## Ejemplo — criterio de aislamiento (idea)

```text
Como usuario del tenant A con token válido:
  GET /api/citas/{id-de-cita-del-tenant-B} → debe ser 403 o 404, nunca 200 con datos ajenos.
Automatiza al menos un caso en CI.
```

Regla: el egreso exige explicar **IDOR cross-tenant** y cómo lo evitas.



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
