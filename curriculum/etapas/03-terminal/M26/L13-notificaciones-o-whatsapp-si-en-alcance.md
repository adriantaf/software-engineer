---
id: L13
materia: M26
orden: 13
titulo: Notificaciones o WhatsApp si en alcance
horas: 5.0
semana: 4
lectura: M24 go/no-go o gap doc
evidencia: projects/m26-capstone/integraciones.md
---

# L13 — Notificaciones o WhatsApp si en alcance

**~5 h · Semana 4**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/integraciones.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Decisión e integración de notificaciones/WhatsApp **solo si** está en alcance; si no, defer escrito.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Feature flag
- Fallback email

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _M24 go/no-go o gap doc_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Decisión go/no-go (25–35 min)

En `projects/m26-capstone/integraciones.md`: WhatsApp/notificaciones **in** o **out** de v1, citando alcance L01 y M24 si existe.

### 3. Si in: integra staging; si out: defer escrito (100–120 min)

**In:** webhook/provider en staging, feature flag, evidencia de envío test.

**Out:** sección **Defer** con fecha v1.1, riesgo, alternativa (email).

No dejes “tal vez”.

### 4. Fallback (25–35 min)

Cómo se entera el cliente si falla el canal. Bitácora semana-04.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l13 notificaciones-o-whatsapp-si-en-alcance"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | M24 go/no-go o gap doc | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/integraciones.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L14 — App móvil M20 conectada o plan cierre](L14-app-movil-m20-conectada-o-plan-cierre.md)
