---
id: L16
materia: M19
orden: 16
titulo: Cierre M19 — checklist pre-demo M22
horas: 5.0
semana: 4
lectura: Repaso M19
evidencia: projects/m19-ops/cierre-m19.md
---

# L16 — Cierre M19 — checklist pre-demo M22

**~5.0 h · Semana 4**

Handoff a M20 (API staging HTTPS) y M22.

## Objetivo

Verificar P1–P3, criterios dominio, prod estable para trials.

## Conceptos clave

- checklist
- dominio

## Pasos (hazlos en orden)

### 1. Checklist pre-demo M22 (50–60 min)

```bash
cat > projects/m19-ops/cierre-m19.md << 'EOF'
# Cierre M19
- [ ] docker.md P1
- [ ] deploy-log HTTPS P2
- [ ] restore-test.md P3
- [ ] runbook.md
Handoff: URL staging para M20/M22
EOF
ls projects/m19-ops
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops
git commit -m "docs(m19): L16 cierre checklist pre-demo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Repaso M19 | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/cierre-m19.md` checklist P1–P3 + handoff URL staging.
2. Commit `docs(m19): L16 cierre-m19-checklist-pre-demo-m22`.

## Errores comunes

- Cerrar sin restore-test.
- No dejar URL staging para M20/M22.

## Siguiente

Materia siguiente: [M20 — Aplicaciones móviles](../M20-aplicaciones-moviles.md) (consume tu staging).
