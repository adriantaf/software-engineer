---
id: L21
materia: M17
orden: 21
titulo: Variables de entorno y secrets
horas: 5.0
semana: 6
lectura: 12-factor config
evidencia: projects/m17-agenda-ops/.env.example
---

# L21 — Variables de entorno y secrets

**~5.0 h · Semana 6**

Deploy seguro empieza por no commitear secrets.

## Objetivo

Separar config: DATABASE_URL, SESSION_SECRET, etc. `.env.example` sin valores reales.

## Conceptos clave

- env
- secrets
- example

## Pasos (hazlos en orden)

### 1. Inventaria vars (40–50 min)

```bash
cat projects/m17-agenda-ops/.env.example
rg -n "process\\.env|env\\." projects/m17-agenda-ops/src | head -40
```

Cada var en `.env.example` con comentario; **sin** valores secretos.

### 2. Separa secrets de config (40 min)

```bash
# ejemplo .env.example
cat >> projects/m17-agenda-ops/.env.example << 'EOF'
# DATABASE_URL=postgresql://app:changeme@localhost:5432/agenda_ops
# SESSION_SECRET=change-me-min-32-chars
# CORS_ORIGIN=http://localhost:5173
EOF
```

Confirma `.env` en `.gitignore`.

### 3. Commit (15 min)

```bash
git add projects/m17-agenda-ops/.env.example
git status | grep -i '\\.env$' && echo 'FAIL: .env tracked' || true
git commit -m "docs(m17): L21 env example secrets"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | 12-factor config | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-agenda-ops/.env.example` lista vars con comentarios; `.env` no tracked.
2. Commit `docs(m17): L21 variables-de-entorno-y-secrets`.

## Errores comunes

- Commitear `.env`.
- Secrets horneados en código.

## Siguiente

[L22 — Deploy staging en PaaS](L22-deploy-staging-en-paas.md)
