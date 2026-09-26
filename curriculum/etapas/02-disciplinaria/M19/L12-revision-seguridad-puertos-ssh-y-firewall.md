---
id: L12
materia: M19
orden: 12
titulo: "Revisión seguridad: puertos, SSH y firewall"
horas: 5.0
semana: 3
lectura: M18 + M11 seguridad host
evidencia: projects/m19-ops/security-host.md
---

# L12 — Revisión seguridad: puertos, SSH y firewall

**~5.0 h · Semana 3**

Deploy sin postura de host revierte M18.

## Objetivo

Checklist puertos expuestos, SSH (clave, no password), firewall si VPS.

## Conceptos clave

- firewall
- SSH
- least privilege

## Pasos (hazlos en orden)

### 1. Revisión host (70–90 min)

```bash
# Si VPS (ejemplos — adapta; no abras 0.0.0.0:5432 al mundo):
# sudo ufw status
# ss -tulpn | head
cat > projects/m19-ops/security-host.md << 'EOF'
# Host security
| Control | Estado | Notas |
|---------|--------|-------|
| SSH keys only | | |
| Firewall | | DB no pública |
| Updates | | |
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/security-host.md
git commit -m "docs(m19): L12 seguridad puertos ssh firewall"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | M18 + M11 seguridad host | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m19-ops/security-host.md` (SSH, firewall, DB no pública).
2. Commit `docs(m19): L12 revision-seguridad-puertos-ssh-y-firewall`.

## Errores comunes

- Postgres expuesto a 0.0.0.0.
- SSH con password root.

## Siguiente

[L13 — Backup automático PostgreSQL](L13-backup-automatico-postgresql.md)
