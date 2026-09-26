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

Si VPS: SSH keys, ufw/security group. Si PaaS: documenta superficie.

## Objetivo

Checklist host harden; sin SSH password abierto al mundo.

## Pasos (hazlos en orden)

### 1. Inventario puertos (40 min)

### 2. Hardening/doc (70–90 min)

`docs/host-security.md`.

### 3. Commit

`docs(m19): l12 host security`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | M18 + M11 seguridad host | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Checklist completo (artefacto: `projects/m19-ops/security-host.md`).
2. SSH seguro o N/A PaaS (artefacto: `projects/m19-ops/security-host.md`).
3. Sin Postgres público (artefacto: `projects/m19-ops/security-host.md`).
4. Commit `docs(m19): L12 revision-seguridad-puertos-ssh-y-firewall`.

## Errores comunes

- SSH password root.
- 22 abierto al mundo sin necesidad.

## Siguiente

[L13 — Backup automático PostgreSQL](L13-backup-automatico-postgresql.md)
