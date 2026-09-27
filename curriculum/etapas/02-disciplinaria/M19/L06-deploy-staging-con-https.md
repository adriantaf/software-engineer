---
id: L06
materia: M19
orden: 6
titulo: Deploy staging con HTTPS
horas: 5.0
semana: 2
lectura: "Proveedor: deploy + TLS"
evidencia: projects/m19-ops/deploy-log.md
---

# L06 — Deploy staging con HTTPS

**~5.0 h · Semana 2**

Primera URL pública del piloto.

## Objetivo

Desplegar staging con HTTPS forzado y variables en panel del host.

## Conceptos clave

- HTTP→HTTPS
- env vars
- build remoto

## Pasos (hazlos en orden)

### 1. Deploy staging HTTPS (90–120 min)

Sigue el ADR. Inyecta secrets en el panel.

```bash
curl -sSI https://TU-STAGING.example/health | head -15
```

### 2. deploy-log.md (30–40 min)

```bash
cat > projects/m19-ops/deploy-log.md << 'EOF'
# Deploy log
| Fecha | Env | Versión/commit | URL | Resultado |
|-------|-----|----------------|-----|-----------|
| YYYY-MM-DD | staging | abc123 | https://… | OK health |
EOF
git add projects/m19-ops/deploy-log.md
git commit -m "docs(m19): L06 deploy staging https"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Proveedor: deploy + TLS | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/deploy-log.md` con URL HTTPS staging y commit/versión.

## Errores comunes

- Deploy ‘OK’ sin URL en deploy-log.
- Secrets en el Dockerfile.

## Siguiente

[L07 — Smoke test: login, cita y health externo](L07-smoke-test-login-cita-y-health-externo.md)
