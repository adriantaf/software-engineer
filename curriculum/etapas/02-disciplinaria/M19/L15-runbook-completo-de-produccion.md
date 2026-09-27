---
id: L15
materia: M19
orden: 15
titulo: Runbook completo de producción
horas: 5.0
semana: 4
lectura: SRE runbook lite
evidencia: projects/m19-ops/runbook.md completo
---

# L15 — Runbook completo de producción

**~5.0 h · Semana 4**

Proyecto único M19.

## Objetivo

Unificar deploy, rollback, backup, restore, URLs, secretos (referencias), health.

## Conceptos clave

- runbook
- handoff

## Pasos (hazlos en orden)

### 1. Runbook completo (70–90 min)

Completa `projects/m19-ops/runbook.md`: deploy, rollback, logs, backup, restore, contactos, URLs (sin secretos).

```bash
wc -l projects/m19-ops/runbook.md
rg -n "Rollback|Backup|Health|Secrets" projects/m19-ops/runbook.md
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/runbook.md
git commit -m "docs(m19): L15 runbook produccion completo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | SRE runbook lite | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/runbook.md` completo (deploy, rollback, backup, restore, URLs).
2. Commit `docs(m19): L15 runbook-completo-de-produccion`.

## Errores comunes

- Runbook genérico de internet.
- Faltan URLs o dueños.

## Siguiente

[L16 — Cierre M19 — checklist pre-demo M22](L16-cierre-m19-checklist-pre-demo-m22.md)
