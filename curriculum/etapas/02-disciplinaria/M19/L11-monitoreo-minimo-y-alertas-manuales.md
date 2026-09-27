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

No necesitas Datadog para el piloto; sí necesitas saber si está caído.

## Objetivo

Configurar healthcheck externo o calendario de revisión manual; definir qué hacer si cae.

## Conceptos clave

- uptime
- on-call manual

## Pasos (hazlos en orden)

### 1. Monitoreo mínimo (60–80 min)

```bash
cat > projects/m19-ops/monitoring.md << 'EOF'
# Monitoreo
- Check: GET /health cada 5 min (UptimeRobot/Cron/… )
- Alerta: email/Telegram si 2 fallos
- Manual: revisar logs tras deploy
EOF
```

```bash
curl -sS https://TU-STAGING.example/health
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/monitoring.md
git commit -m "docs(m19): L11 monitoreo alertas manuales"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Uptime básico | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m19-ops/monitoring.md` con check `/health` y canal de alerta.
2. Commit `docs(m19): L11 monitoreo-minimo-y-alertas-manuales`.

## Errores comunes

- Monitoreo = ‘miro de vez en cuando’.
- Alertas al canal equivocado sin dueño.

## Siguiente

[L12 — Revisión seguridad: puertos, SSH y firewall](L12-revision-seguridad-puertos-ssh-y-firewall.md)
