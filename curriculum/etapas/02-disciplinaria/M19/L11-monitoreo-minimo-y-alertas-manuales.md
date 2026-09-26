---
id: L11
materia: M19
orden: 11
titulo: Monitoreo mínimo y alertas manuales
horas: 5.0
semana: 3
lectura: Uptime básico
evidencia: projects/m19-ops/monitoring.md
---

# L11 — Monitoreo mínimo y alertas manuales

**~5.0 h · Semana 3**

Uptime mínimo: ping health + alerta humana.

## Objetivo

`docs/monitoreo.md`: qué miras, cada cuánto, a quién avisas.

## Pasos (hazlos en orden)

### 1. Define señales (40 min)

### 2. Configura check (70–90 min)

Cron externo, Better Uptime free, o script. Evidencia.

### 3. Commit

`docs(m19): l11 monitoreo minimo`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Uptime básico | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Monitoreo definido (artefacto: `projects/m19-ops/monitoring.md`).
2. Contacto (artefacto: `projects/m19-ops/monitoring.md`).
3. health prod (artefacto: `projects/m19-ops/monitoring.md`).
4. Commit `docs(m19): L11 monitoreo-minimo-y-alertas-manuales`.

## Errores comunes

- Asumir siempre up.
- Alertas sin acción.

## Siguiente

[L12 — Revisión seguridad: puertos, SSH y firewall](L12-revision-seguridad-puertos-ssh-y-firewall.md)
