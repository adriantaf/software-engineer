---
id: L07
materia: M19
orden: 7
titulo: "Smoke test: login, pedido y health externo"
horas: 5.0
semana: 2
lectura: Runbook borrador
evidencia: projects/m19-ops/smoke-staging.md
---

# L07 — Smoke test: login, pedido y health externo

**~5.0 h · Semana 2**

‘Contenedor verde’ ≠ producto usable.

## Objetivo

Ejecutar checklist smoke desde fuera de tu laptop: login, crear pedido, GET /health.

## Conceptos clave

- smoke test
- datos prueba

## Pasos (hazlos en orden)

### 1. Smoke staging (60–80 min)

```bash
BASE=https://TU-STAGING.example
curl -sS "$BASE/health"
curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" \
  -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"***"}'
curl -sS -b /tmp/st.ck -X POST "$BASE/pedidos" -H 'content-type: application/json' -d '{...}'
```

**No** pegues el password en el markdown.

### 2. Documenta smoke-staging.md (30 min)

```bash
cat > projects/m19-ops/smoke-staging.md << 'EOF'
# Smoke staging
Fecha: …  Health: OK  Login: OK  Pedido: OK
EOF
git add projects/m19-ops/smoke-staging.md
git commit -m "docs(m19): L07 smoke staging login pedido"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Runbook borrador | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/smoke-staging.md` con health+login+pedido y fecha (sin passwords).
2. Commit `docs(m19): L07 smoke-test-login-pedido-y-health-externo`.

## Errores comunes

- Smoke solo health, sin login/pedido.
- Password en el markdown.

## Siguiente

[L08 — Dominios y deploy-log semana 2](L08-dominios-y-deploy-log-semana-2.md)
