---
id: L05
materia: M19
orden: 5
titulo: "ADR hosting: PaaS vs VPS"
horas: 5.0
semana: 2
lectura: Docs Fly/Railway/Render o VPS
evidencia: projects/m19-ops/adr-hosting.md
---

# L05 — ADR hosting: PaaS vs VPS

**~5.0 h · Semana 2**

Evitas re-decidir cada semana.

## Objetivo

Documentar decisión de hosting para Agenda Ops con criterios costo, TLS, Postgres gestionado, DX.

## Conceptos clave

- PaaS
- VPS+Docker
- egress y region

## Pasos (hazlos en orden)

### 1. ADR PaaS vs VPS (70–90 min)

```bash
cat > projects/m19-ops/adr-hosting.md << 'EOF'
# ADR hosting
## Contexto
Agenda Ops necesita HTTPS + Postgres managed o self-host.
## Opciones
A) PaaS  B) VPS
## Decisión
…
## Consecuencias
costo, SSH, backups, tiempo-a-staging
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/adr-hosting.md
git commit -m "docs(m19): L05 adr hosting paas vs vps"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Docs Fly/Railway/Render o VPS | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m19-ops/adr-hosting.md` con decisión PaaS vs VPS y consecuencias.
2. Commit `docs(m19): L05 adr-hosting-paas-vs-vps`.

## Errores comunes

- ADR sin costos/tiempo ni Agenda Ops.
- Elegir VPS sin plan de backups.

## Siguiente

[L06 — Deploy staging con HTTPS](L06-deploy-staging-con-https.md)
