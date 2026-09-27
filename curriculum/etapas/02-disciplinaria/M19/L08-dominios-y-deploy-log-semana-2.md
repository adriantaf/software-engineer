---
id: L08
materia: M19
orden: 8
titulo: Dominios y deploy-log semana 2
horas: 5.0
semana: 2
lectura: DNS del proveedor
evidencia: projects/m19-ops/dominios.md
---

# L08 — Dominios y deploy-log semana 2

**~5.0 h · Semana 2**

Trials M22 necesitan URL estable.

## Objetivo

Registrar subdominios staging (y prod planificado); enlazar con deploy-log.

## Conceptos clave

- CNAME
- cert automático

## Pasos (hazlos en orden)

### 1. Dominios (50–60 min)

```bash
cat > projects/m19-ops/dominios.md << 'EOF'
# Dominios
| Uso | FQDN | DNS | TLS |
|-----|------|-----|-----|
| API staging | api-staging.… | CNAME → PaaS | managed |
EOF
```

### 2. Actualiza deploy-log semana 2 (30 min)

```bash
echo "| $(date -I) | staging | … | https://… | DNS OK |" >> projects/m19-ops/deploy-log.md
git add projects/m19-ops/dominios.md projects/m19-ops/deploy-log.md
git commit -m "docs(m19): L08 dominios deploy-log semana2"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | DNS del proveedor | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/dominios.md` + fila nueva en `deploy-log.md`.
2. Commit `docs(m19): L08 dominios-y-deploy-log-semana-2`.

## Errores comunes

- Dominio sin TLS.
- DNS apuntando a IP efímera sin nota.

## Siguiente

[L09 — Promover configuración a producción](L09-promover-configuracion-a-produccion.md)
