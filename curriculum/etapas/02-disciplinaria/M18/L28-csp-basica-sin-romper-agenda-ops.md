---
id: L28
materia: M18
orden: 28
titulo: CSP básica sin romper Agenda Ops
horas: 5.0
semana: 7
lectura: Content Security Policy Cheat Sheet
evidencia: projects/m18-appsec/docs/csp.md + commit opcional
---

# L28 — CSP básica sin romper Agenda Ops

**~5.0 h · Semana 7**

CSP report-only primero: observas violaciones sin romper el panel.

## Objetivo

Política en `projects/m18-appsec/docs/csp.md`; report-only en staging; anota violaciones.

## Pasos

### 1. Inventaria fuentes (30–40 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'cdn\.|googleapis|script src|link href' -g '*.html' -g '*.tsx' -g '*.jsx' | head -30
cat > projects/m18-appsec/docs/csp.md <<'EOF'
# CSP — Agenda Ops
## Fuentes externas
- …

## Política propuesta (report-only)
default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none';

## Violaciones observadas
- …
EOF
```
### 2. Report-Only (60–80 min)

```ts
app.use((_req, res, next) => {
  res.setHeader(
    "Content-Security-Policy-Report-Only",
    "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'",
  );
  next();
});
```

```bash
curl -sI localhost:3000/ | rg -i content-security-policy
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/csp.md
git commit -m "docs(m18): l28 csp report-only"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Content Security Policy Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Política escrita (artefacto: `projects/m18-appsec/docs/csp.md`).
2. Prueba report-only o estricta (artefacto: `projects/m18-appsec/docs/csp.md`).
3. Commit `docs(m18): L28 csp-basica-sin-romper-agenda-ops`.

## Errores comunes

- `unsafe-inline` everywhere.
- CSP en meta sin HTTPS.

## Siguiente

[L29 — Pipeline CI: lint, test, audit, anti-secretos](L29-pipeline-ci-lint-test-audit-anti-secretos.md)
