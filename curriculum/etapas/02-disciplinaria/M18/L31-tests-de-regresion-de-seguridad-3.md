---
id: L31
materia: M18
orden: 31
titulo: Tests de regresión de seguridad (≥3)
horas: 5.0
semana: 8
lectura: Security unit tests patterns
evidencia: ≥3 tests en repo producto
---

# L31 — Tests de regresión de seguridad (≥3)

**~5.0 h · Semana 8**

≥3 tests que fallen si reabres agujeros (IDOR, XSS escape, authz rol u equivalentes).

## Objetivo

Suite documentada en `projects/m18-appsec/docs/security-tests.md`; CI los corre.

## Pasos

### 1. Selecciona 3 (20–30 min)

```bash
cat > projects/m18-appsec/docs/security-tests.md <<'EOF'
# Security regression tests
| # | Archivo | Protege |
|---|---------|---------|
| 1 | tests/security/authz-cross-user.test.ts | IDOR pedidos |
| 2 | tests/security/xss-escape.test.ts | stored XSS notas |
| 3 | tests/security/rbac-settings.test.ts | staff≠owner |
EOF
```
### 2. Implementa / verde (100–120 min)

Nombres claros `security.*.test.ts` (o carpeta `tests/security/`).

```bash
npm test -- --testPathPattern=security
# Confirma que el workflow L29 incluye este pattern
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "test(m18): l31 regresion seguridad"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Security unit tests patterns | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥3 tests listados (artefacto: `≥3 tests en repo producto`).
2. CI los ejecuta (artefacto: `≥3 tests en repo producto`).
3. Commit `docs(m18): L31 tests-de-regresion-de-seguridad-3`.

## Errores comunes

- Tests skipped.
- Solo manual.

## Siguiente

[L32 — Cierre M18 — dominio y riesgo residual](L32-cierre-m18-dominio-y-riesgo-residual.md)
