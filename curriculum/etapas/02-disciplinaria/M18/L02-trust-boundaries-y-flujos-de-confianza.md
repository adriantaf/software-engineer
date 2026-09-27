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

M10 y M13 nombraron boundaries; hoy los operacionalizas para AppSec.

## Objetivo

Documentar ≥4 límites y 3 flujos (login, crear pedido, deep-link WA) en `projects/m18-appsec/trust-boundaries-appsec.md`.

## Pasos

### 1. Ancla M13 (20–30 min)

```bash
ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin M13; parte de cero)"
touch projects/m18-appsec/trust-boundaries-appsec.md
```
### 2. Tabla de límites (70–90 min)

Por cada límite: origen, destino, protocolo, autenticación, datos. Mínimo 4.

```markdown
| Origen | Destino | Protocolo | Auth | Datos |
|--------|---------|-----------|------|-------|
| Browser | API | HTTPS | cookie/JWT | PII pedidos |
| API | Postgres | TCP | user app | SQL |
| API | SMTP futuro | TLS | API key | recordatorios |
| Operador | Hosting | SSH/HTTPS | MFA | logs, .env |
```
### 3. Flujos + abuso (40–50 min)

Para login, crear pedido y deep-link WA: datos en tránsito, auth requerida, fallo si se omite authz. Una pregunta de abuso por límite.

```bash
printf "\n## Flujos\n- login:\n- crear pedido:\n- deep-link WA:\n\n## Abuso por límite\n" >> projects/m18-appsec/trust-boundaries-appsec.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/trust-boundaries-appsec.md
git commit -m "docs(m18): l02 trust boundaries"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | STRIDE por boundary + M13 `trust-boundaries` | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥4 boundaries documentados (artefacto: `projects/m18-appsec/trust-boundaries-appsec.md`).
2. Pregunta de abuso por límite (artefacto: `projects/m18-appsec/trust-boundaries-appsec.md`).
3. Commit `docs(m18): L02 trust-boundaries-y-flujos-de-confianza`.

## Errores comunes

- Un solo boundary “internet”.
- Ignorar Postgres como activo interno.

## Siguiente

[L03 — STRIDE aplicado al SaaS de menú/pedidos](L03-stride-aplicado-al-crm-de-pedidos.md)
