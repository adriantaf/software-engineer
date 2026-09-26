---
id: L10
materia: M25
orden: 10
titulo: Secretos Stripe y rotación
horas: 5.0
semana: 3
lectura: OWASP Configuration + Stripe webhooks docs
evidencia: projects/m25-ciber/hardening/stripe-secrets.md
---

# L10 — Secretos Stripe y rotación

**~5 h · Semana 3**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/hardening/stripe-secrets.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Inventario claves test/live; ninguna en repo; webhook secret.

## Por qué empieza así

Billing roto o secrets filtrados tumba el SaaS antes del primer cliente.

Conceptos que debes poder explicar al cerrar:

- Stripe signature
- Secrets manager / env
- Restore ≠ backup

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Configuration + Stripe webhooks docs_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Inventario de secretos Stripe (25–35 min)

En `projects/m25-ciber/hardening/stripe-secrets.md` tabla:

| Secreto | Ambiente | Dónde vive | Rotación |
|---------|----------|------------|----------|

Incluye `sk_test`/`sk_live`, `pk_*`, webhook signing secret. **Nunca** pegues valores.

### 3. Busca fugas en repo e historial (90–110 min)

Busca patrones sin imprimir valores:

```bash
rg -n "sk_live|sk_test|whsec_" --glob '!.git' . || true
rg -n "STRIPE_" .env.example apps/ || true
```

Documenta hallazgos (path + tipo). Si hay key en git: plan de rotación + `.gitignore`/secret scanning.

### 4. Plan de rotación (30–40 min)

Checklist de 6 pasos para rotar webhook secret en staging. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l10 secretos-stripe-y-rotaci-n"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Configuration + Stripe webhooks docs | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/hardening/stripe-secrets.md`.
2. Checklist ítem demostrado.
3. Sin valores de API keys.
4. Commit `docs(m25): l10 …` en el historial.

## Errores comunes

- Solo checklist teórico.
- Restore nunca probado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L11 — Least privilege DB y deploy](L11-least-privilege-db-y-deploy.md)
