---
id: L01
materia: M19
orden: 1
titulo: Inventario de secretos y ambientes staging/prod
horas: 5.0
semana: 1
lectura: Docker docs — env vars + 12-factor
evidencia: projects/m19-ops/secrets-inventory.md + ambientes.md
---

# L01 — Inventario de secretos y ambientes staging/prod

**~5.0 h · Semana 1**

M19 empieza donde M18 dejó: nada de secretos en git antes de empaquetar.

## Objetivo

Crear inventario de secretos sin valores y definir URLs/objetivo de staging y prod para Vitrina.

## Conceptos clave

- DATABASE_URL
- SESSION_SECRET
- Stripe test futuro

## Pasos (hazlos en orden)

### 1. Carpetas de evidencia (15 min)

```bash
mkdir -p projects/m19-ops/{scripts,logs,docs}
ls projects/m19-ops
```

### 2. Inventario de secretos sin valores (80–100 min)

```bash
cat > projects/m19-ops/secrets-inventory.md << 'EOF'
# Inventario de secretos (SIN valores)
| Variable | Staging | Prod | Quién inyecta | Rotación |
|----------|---------|------|---------------|----------|
| DATABASE_URL | sí | sí | PaaS/VPS secrets | 90d |
| SESSION_SECRET | sí | sí | secrets manager | 90d |
EOF
```

Cruza con M17:

```bash
cat projects/m17-vitrina/.env.example
```

### 3. ambientes.md staging vs prod (30–40 min)

```bash
cat > projects/m19-ops/ambientes.md << 'EOF'
# Ambientes
| Env | URL API | URL Front | Notas |
|-----|---------|-----------|-------|
| local | http://localhost:3000 | http://localhost:5173 | |
| staging | https://… | https://… | |
| prod | TBD | TBD | |
EOF
git add projects/m19-ops
git commit -m "docs(m19): L01 inventario secretos ambientes"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Docker docs — env vars + 12-factor | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Existen `projects/m19-ops/secrets-inventory.md` y `projects/m19-ops/ambientes.md`.
2. Inventario **sin** valores secretos; URLs staging/prod anotadas.
3. Commit `docs(m19): L01 inventario-de-secretos-y-ambientes-staging-prod`.

## Errores comunes

- Pegar JWT/passwords en markdown.
- Un solo ambiente llamado ‘prod’.

## Siguiente

[L02 — Dockerfile multi-stage para la API](L02-dockerfile-multi-stage-para-la-api.md)
