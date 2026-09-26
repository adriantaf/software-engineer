---
id: L10
materia: M19
orden: 10
titulo: Logs, rollback y versión desplegada
horas: 5.0
semana: 3
lectura: Runbook ops
evidencia: projects/m19-ops/runbook.md sección rollback
---

# L10 — Logs, rollback y versión desplegada

**~5.0 h · Semana 3**

Sabes qué versión corre y cómo volver atrás.

## Objetivo

Sección runbook: versión, dónde están logs, procedimiento rollback ensayado en seco.

## Pasos (hazlos en orden)

### 1. Versionado (40 min)

Tag/git sha visible en `/health` o header.

### 2. Rollback dry-run (70–90 min)

Documenta pasos sin necesariamente tumbar prod si riesgoso — al menos staging.

### 3. Commit

`docs(m19): l10 logs rollback version`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Runbook ops | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Rollback documentado (artefacto: `projects/m19-ops/runbook.md sección rollback`).
2. Versión en runbook (artefacto: `projects/m19-ops/runbook.md sección rollback`).
3. Prueba o simulacro (artefacto: `projects/m19-ops/runbook.md sección rollback`).
4. Commit `docs(m19): L10 logs-rollback-y-version-desplegada`.

## Errores comunes

- Rollback ‘redeploy main’ sin tag.
- Sin logs.

## Siguiente

[L11 — Monitoreo mínimo y alertas manuales](L11-monitoreo-minimo-y-alertas-manuales.md)
