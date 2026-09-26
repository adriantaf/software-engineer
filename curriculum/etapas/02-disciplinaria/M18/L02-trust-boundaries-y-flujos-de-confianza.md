---
id: L02
materia: M18
orden: 2
titulo: Trust boundaries y flujos de confianza
horas: 5.0
semana: 1
lectura: STRIDE por boundary + M13 `trust-boundaries`
evidencia: projects/m18-appsec/trust-boundaries-appsec.md
---

# L02 — Trust boundaries y flujos de confianza

**~5.0 h · Semana 1**

Dibuja dónde termina la confianza: browser, CDN, API, DB, WhatsApp.

## Objetivo

Diagrama de boundaries + 3 flujos (login, crear cita, deep-link WA) en el threat model.

## Pasos (hazlos en orden)

### 1. Boundaries (60–70 min)

ASCII/Mermaid: zonas Trusted/Untrusted. Cookies cruzan cuál frontera.

### 2. Flujos (60–70 min)

Para cada flujo: datos en tránsito, autenticación requerida, qué falla si se omite authz.

### 3. Commit

`docs(m18): l02 trust boundaries`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | STRIDE por boundary + M13 `trust-boundaries` | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥4 boundaries documentados (artefacto: `projects/m18-appsec/trust-boundaries-appsec.md`).
2. Pregunta de abuso por límite (artefacto: `projects/m18-appsec/trust-boundaries-appsec.md`).
3. Enlace a diseño M13 si aplica (artefacto: `projects/m18-appsec/trust-boundaries-appsec.md`).
4. Commit `docs(m18): L02 trust-boundaries-y-flujos-de-confianza`.

## Errores comunes

- Un solo boundary “internet”.
- Ignorar Postgres como activo interno.

## Siguiente

[L03 — STRIDE aplicado al CRM de citas](L03-stride-aplicado-al-crm-de-citas.md)
