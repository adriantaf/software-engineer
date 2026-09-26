"""Per-lesson evidencia paths and lab overlays for thin generator specs (M25/M26)."""
from __future__ import annotations

# Exact evidencia paths (generator used placeholders for M25 week 1).
M25_EVIDENCIA = {
    1: "projects/m25-ciber/inventario.md",
    2: "projects/m25-ciber/clasificacion-datos.md",
    3: "projects/m25-ciber/tenants-prueba.md",
    4: "projects/m25-ciber/aislamiento/prueba-manual-01.md",
    5: "projects/m25-ciber/review/authn.md",
    6: "projects/m25-ciber/review/authz-matrix.md",
    7: "projects/m25-ciber/aislamiento/tests.md",
    8: "projects/m25-ciber/hallazgos/hallazgo-01.md",
    9: "projects/m25-ciber/hardening/headers.md",
    10: "projects/m25-ciber/hardening/stripe-secrets.md",
    11: "projects/m25-ciber/hardening/least-privilege.md",
    12: "projects/m25-ciber/hardening/restore-test.md",
    13: "projects/m25-ciber/logging/politica-logs.md",
    14: "projects/m25-ciber/abuso/rate-limit.md",
    15: "projects/m25-ciber/alertas/minimas.md",
    16: "projects/m25-ciber/logging/errores.md",
    17: "projects/m25-ciber/privacidad/retencion.md",
    18: "projects/m25-ciber/privacidad/exports.md",
    19: "projects/m25-ciber/privacidad/aviso-borrador.md",
    20: "projects/m25-ciber/hallazgos/hallazgo-02.md",
    21: "projects/m25-ciber/tabletop/env-leak.md",
    22: "projects/m25-ciber/tabletop/cross-tenant-incident.md",
    23: "projects/m25-ciber/runbook-incidentes.md",
    24: "projects/m25-ciber/security-review.md",
}

# Lab steps: list of (title, time, body) inserted AFTER reading step, BEFORE commit.
# If present, replaces auto-split of pasos_extra.
M25_LABS: dict[int, list[tuple[str, str, str]]] = {
    1: [
        (
            "Crea carpetas de evidencia",
            "15–20 min",
            """```bash
mkdir -p projects/m25-ciber/{aislamiento,review,hardening,logging,abuso,alertas,privacidad,tabletop,hallazgos,bitacora}
```

Lee `projects/m25-ciber/README.md` y anota URLs de staging/prod que ya tengas (M19).""",
        ),
        (
            "Inventario sin secretos",
            "90–120 min",
            """Crea `projects/m25-ciber/inventario.md` con tabla:

| Activo | Tipo | Ambiente | Dueño | Notas |
|--------|------|----------|-------|-------|

Incluye ≥8 filas: API Agenda Ops, panel, Postgres, dominio, CI, webhook Stripe, storage/backups, repo. **Sin** passwords ni API keys.""",
        ),
        (
            "Marca superficie de ataque",
            "40–50 min",
            """Añade sección **Superficie** con 5 endpoints o entradas de datos (login, citas CRUD, webhooks, exports). Bitácora `bitacora/semana-01.md` con 5 líneas.""",
        ),
    ],
    4: [
        (
            "Prepara IDs de prueba",
            "20–30 min",
            """Usa tenants A/B de L03. Anota en `aislamiento/prueba-manual-01.md`: `tenant_a_id`, `tenant_b_id`, `cita_b_id`, usuario A.""",
        ),
        (
            "Prueba manual IDOR",
            "90–110 min",
            """Autenticado como A, pide recurso de B (GET cita / cliente). Documenta:

```bash
# ejemplo — adapta a tu API; redacta tokens
curl -s -o /tmp/a.json -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A" \\
  "$API/citas/$CITA_B_ID"
```

Pega status + fragmento de body **redactado**. Espera 403/404; si 200 con datos de B → hallazgo crítico.""",
        ),
        (
            "Clasifica resultado",
            "30–40 min",
            """Sección **Resultado**: PASS / FAIL. Si FAIL, abre issue y enlázalo. No “arregles en silencio” sin evidencia.""",
        ),
    ],
    7: [
        (
            "Elige harness",
            "25–35 min",
            """Vitest/Jest/supertest en el repo producto. Anota comando `npm test -- aislamiento` (o similar) en `aislamiento/tests.md`.""",
        ),
        (
            "Escribe el test cross-tenant",
            "100–130 min",
            """Test mínimo: login A + GET recurso B → assert status ∈ {403,404} **o** body sin datos de B.

Si aún no hay seed de dos tenants, crea helper de seed en test (no uses prod).""",
        ),
        (
            "Corre y documenta",
            "30–40 min",
            """Pega salida del test (verde o rojo). Si rojo porque el bug existe: deja el test fallando **o** `it.failing` documentado + issue. Objetivo: el fallo sea visible.""",
        ),
    ],
    21: [
        (
            "Escenario tabletop .env",
            "30–40 min",
            """En `tabletop/env-leak.md` define: quién filtró (gist/chat), qué secrets estaban, alcance (staging vs prod).""",
        ),
        (
            "Narrativa ≥30 min de decisión",
            "90–110 min",
            """Escribe timeline minuto a minuto (T+0 … T+60): detectar, rotar claves Stripe/DB, revocar sesiones, comunicar. Sin copiar tutorial genérico — usa **tus** nombres de servicio.""",
        ),
        (
            "Acciones verificables",
            "30–40 min",
            """Checklist de 8 acciones con dueño=tú y evidencia esperada (issue, rotación documentada).""",
        ),
    ],
    24: [
        (
            "Reúne evidencias P1–P3",
            "40–50 min",
            """Índice en `security-review.md`: inventario, aislamiento (manual+CI), ≥2 hallazgos cerrados, hardenings, tabletops, runbook.""",
        ),
        (
            "Rúbrica y riesgo residual",
            "80–100 min",
            """Tabla de controles: control | evidencia | residual. Declara qué **no** está listo para M26 demo pública.""",
        ),
        (
            "Handoff M26",
            "30–40 min",
            """Sección handoff: issues abiertos, tests obligatorios en CI, secretos a rotar antes de video público.""",
        ),
    ],
}

M26_EVIDENCIA = {
    1: "projects/m26-capstone/alcance.md",
    2: "projects/m26-capstone/plan-8-semanas.md",
    3: "projects/m26-capstone/memoria/tenancy-modelo.md",
    4: "projects/m26-capstone/riesgos.md",
    5: "projects/m26-capstone/onboarding.md",
    6: "projects/m26-capstone/demo-tenants.md",
    7: "projects/m26-capstone/memoria/panel-admin.md",
    8: "projects/m26-capstone/demos/semana-02.md",
    9: "projects/m26-capstone/memoria/citas-crud.md",
    10: "projects/m26-capstone/memoria/clientes-servicios.md",
    11: "projects/m26-capstone/memoria/roles.md",
    12: "projects/m26-capstone/tests-regresion.md",
    13: "projects/m26-capstone/integraciones.md",
    14: "projects/m26-capstone/mobile-gap.md",
    15: "projects/m26-capstone/metricas.md",
    16: "projects/m26-capstone/demos/semana-04.md",
    17: "projects/m26-capstone/memoria/stripe-productos.md",
    18: "projects/m26-capstone/memoria/landing-precios.md",
    19: "projects/m26-capstone/memoria/billing-flujo.md",
    20: "projects/m26-capstone/memoria/webhooks-stripe.md",
    21: "projects/m26-capstone/seguridad-m25.md",
    22: "projects/m26-capstone/ci-cross-tenant.md",
    23: "projects/m26-capstone/memoria/ops.md",
    24: "projects/m26-capstone/hardening-final.md",
    25: "projects/m26-capstone/memoria/arquitectura.md",
    26: "projects/m26-capstone/memoria/tenancy-billing-seguridad.md",
    27: "projects/m26-capstone/comercial.md",
    28: "projects/m26-capstone/post-mortem-v1.md",
    29: "projects/m26-capstone/demo.md",
    30: "projects/m26-capstone/egreso-checklist.md",
    31: "projects/m26-capstone/README.md",
    32: "projects/m26-capstone/cierre.md",
}

M26_OBJETIVOS = {
    1: "Congelar por escrito el alcance SaaS v1 de Agenda Ops (in/out) alineado a producto-saas y rúbrica de egreso.",
    2: "Publicar plan de 8 semanas con hitos semanales y checklist de egreso honesto (gaps visibles).",
    3: "Documentar modelo `tenant_id`, resolución de tenant (subdominio/header/sesión) y límites de confianza.",
    4: "Listar riesgos del integrador (billing, aislamiento, ops) con mitigaciones y dueños.",
    5: "Dejar onboarding self-service de tenant nuevo usable en staging (flujo + evidencia).",
    6: "Seeds/datos demo para ≥2 tenants distintos, listos para demos internas.",
    7: "Panel admin por tenant con rutas/capturas y nota de authz.",
    8: "Demo interna semana 2: dos tenants, guion y resultado en `demos/semana-02.md`.",
    9: "CRUD de citas multi-tenant con tests de aislamiento en el camino crítico.",
    10: "Clientes y servicios scoped por tenant con evidencia en repo + memoria.",
    11: "Roles staff/owner mínimos documentados y aplicados.",
    12: "Suite de regresión de flujos críticos en CI (o pipeline documentado).",
    13: "Decisión e integración de notificaciones/WhatsApp **solo si** está en alcance; si no, defer escrito.",
    14: "App móvil M20 conectada a API v1 **o** plan de cierre explícito del gap.",
    15: "Métricas comerciales M22 visibles en producto o dashboard interno.",
    16: "Demo interna semana 4: flujos completos multi-tenant grabados/escritos.",
    17: "Productos Free/Pro en Stripe **test mode** documentados.",
    18: "Landing pública de precios en staging/prod con precios MXN coherentes con M22.",
    19: "Checkout test end-to-end (crear sesión → pagar test card → estado Pro).",
    20: "Webhooks Stripe verificados en deploy (firma + idempotencia básica).",
    21: "Re-ejecutar security review M25 y cerrar gaps bloqueantes.",
    22: "CI con tests cross-tenant obligatorios (falla el build si A lee B).",
    23: "Backups prod + restore documentado en runbook ops.",
    24: "Hardening final pre-demo pública (headers, secretos, errores).",
    25: "Memoria: arquitectura y diagramas (C4/ligero) del SaaS real.",
    26: "Memoria: tenancy + billing + seguridad con evidencias enlazadas.",
    27: "Registro comercial M22 (demos/trials) enlazado al capstone.",
    28: "Post-mortem técnico v1 con métricas y deuda consciente.",
    29: "Video demo público multi-tenant (sin tutorial de fondo).",
    30: "Checklist de egreso con cada ítem enlazado a evidencia en git/URL.",
    31: "README capstone como índice maestro de toda la evidencia.",
    32: "Cierre integrador + handoff v1.1 (qué sigue, qué no).",
}

M26_LABS: dict[int, list[tuple[str, str, str]]] = {
    1: [
        (
            "Crea estructura capstone",
            "20–30 min",
            """```bash
mkdir -p projects/m26-capstone/{memoria,demos,bitacora}
```

Copia mentalmente [producto-saas](../../../producto-saas.md) y [egreso](../../../egreso.md) al lado.""",
        ),
        (
            "Congela alcance.md",
            "100–130 min",
            """`alcance.md` con secciones: **In scope v1**, **Out of scope**, **Dependencias** (M17/M19/M22/M25), **Criterios de egreso que toca**.

≥8 bullets in, ≥5 out. Nada de “tal vez WhatsApp” sin decidir.""",
        ),
        (
            "Bitácora semana 1",
            "20–30 min",
            """`bitacora/semana-01.md`: horas plan vs real; 1 riesgo que ya ves.""",
        ),
    ],
    17: [
        (
            "Stripe test mode",
            "30–40 min",
            """Confirma claves `sk_test` / `pk_test` solo en secretos de entorno. Documenta en `memoria/stripe-productos.md` el dashboard URL (sin keys).""",
        ),
        (
            "Crea productos Free/Pro",
            "90–110 min",
            """Crea Price objects alineados a `projects/m22-bektor/pricing.md`. Tabla: product_id, price_id, MXN, intervalo, qué desbloquea en Agenda Ops.""",
        ),
        (
            "Enlaza al tenant",
            "40–50 min",
            """Describe cómo el `tenant_id` queda asociado al Customer/Subscription Stripe (campo metadata). Sin implementar webhook aún (L20).""",
        ),
    ],
    19: [
        (
            "Checkout Session",
            "40–50 min",
            """Implementa o verifica endpoint que crea Checkout Session en test mode para un tenant Free → Pro.""",
        ),
        (
            "Pago con tarjeta test",
            "60–80 min",
            """Completa pago con `4242…`. Documenta en `billing-flujo.md` pasos + IDs (session, subscription) **sin** secretos.""",
        ),
        (
            "Estado en app",
            "40–50 min",
            """Verifica que el tenant pasa a Pro en tu modelo (flag/plan). Si solo Stripe lo sabe y la app no, anota gap explícito.""",
        ),
    ],
    29: [
        (
            "Guion del video",
            "40–50 min",
            """`demo.md`: guion ≤8 min — login A, cita, login B, prueba de aislamiento, pricing/checkout test, cierre.""",
        ),
        (
            "Graba",
            "90–120 min",
            """Graba pantalla (Loom/OBS). Sin tutorial de terceros de fondo. URLs de staging/prod reales.""",
        ),
        (
            "Publica enlace",
            "20–30 min",
            """Enlace unlisted/público en `demo.md` + duración + fecha. Si el video es privado, no cuenta para egreso.""",
        ),
    ],
}


def evidencia_for(materia: str, orden: int, fallback: str) -> str:
    if materia == "M25" and orden in M25_EVIDENCIA:
        return M25_EVIDENCIA[orden]
    if materia == "M26" and orden in M26_EVIDENCIA:
        return M26_EVIDENCIA[orden]
    # Clean vague generator evidencia
    if "según lección" in fallback or fallback.endswith(" "):
        return fallback.split()[0] if fallback.split() else fallback
    return fallback


def lab_overlay(materia: str, orden: int) -> list[tuple[str, str, str]] | None:
    if materia == "M25":
        return M25_LABS.get(orden)
    if materia == "M26":
        return M26_LABS.get(orden)
    return None


def objetivo_for(materia: str, orden: int, fallback: str) -> str:
    if materia == "M26" and orden in M26_OBJETIVOS:
        return M26_OBJETIVOS[orden]
    return fallback
