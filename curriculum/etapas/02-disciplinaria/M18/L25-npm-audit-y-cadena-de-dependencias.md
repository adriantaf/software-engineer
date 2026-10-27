---
id: L25
materia: M18
orden: 25
titulo: npm audit y cadena de dependencias
horas: 5.0
semana: 7
lectura: OWASP A06 Vulnerable Components
evidencia: projects/m18-appsec/docs/npm-audit.md
---

# L25 — npm audit y cadena de dependencias

**~5.0 h · Semana 7**

A06: la cadena de deps es superficie. Hoy mides y remedias al menos un high/critical.

## Objetivo

Salida de audit en `projects/m18-appsec/docs/npm-audit.md` (+ mirror `projects/m18-appsec/deps-audit.md` si quieres); ≥1 remediación o justificación.

## Pasos

### 1. Corre audit (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
npm audit --omit=dev 2>/dev/null || npm audit
npm audit --json > /tmp/m18-audit.json || true
mkdir -p projects/m18-appsec/docs
cp /tmp/m18-audit.json projects/m18-appsec/docs/npm-audit.json 2>/dev/null || true
```
### 2. Documenta + remedia (70–90 min)

```bash
cat > projects/m18-appsec/docs/npm-audit.md <<'EOF'
# npm audit — Vitrina
Fecha:
High/Critical:
Acción (update / ignore justificado):
Commit:
EOF
# Remedia al menos 1
npm audit fix --omit=dev || true
npm ls --depth=0 | head
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/npm-audit.md
git commit -m "docs(m18): l25 npm audit"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A06 Vulnerable Components | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Audit guardado (artefacto: `projects/m18-appsec/docs/npm-audit.md`).
2. ≥1 acción tomada (artefacto: `projects/m18-appsec/docs/npm-audit.md`).
3. Commit `docs(m18): L25 npm-audit-y-cadena-de-dependencias`.

## Errores comunes

- `npm audit fix --force` sin leer.
- Ignorar todo.

## Siguiente

[L26 — Secretos, .env y rotación](L26-secretos-env-y-rotacion.md)
