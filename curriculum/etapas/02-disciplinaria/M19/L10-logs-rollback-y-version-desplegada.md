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

A las 11 p.m. solo cuenta el runbook.

## Objetivo

Documentar dónde ver logs, cómo identificar versión y rollback a imagen/tag anterior.

## Conceptos clave

- rollback
- tag git
- logs PaaS

## Pasos (hazlos en orden)

### 1. Rollback + versión (60–80 min)

```bash
mkdir -p projects/m19-ops
cat > projects/m19-ops/runbook.md << 'EOF'
# Runbook (borrador)
## Versión desplegada
Cómo ver commit/tag en runtime (header, /health.version, o CLI PaaS).
## Rollback
1. Redeploy imagen/tag anterior
2. Verificar /health
3. Anotar en deploy-log.md
## Logs
comando CLI o URL del provider
EOF
```

```bash
# ejemplo
# fly releases / render releases / docker compose images
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/runbook.md
git commit -m "docs(m19): L10 logs rollback version"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Runbook ops | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/runbook.md` tiene secciones versión, logs y rollback.
2. Commit `docs(m19): L10 logs-rollback-y-version-desplegada`.

## Errores comunes

- Rollback ‘reiniciar el server’ sin versión pinneada.
- Logs inaccesibles documentados.

## Siguiente

[L11 — Monitoreo mínimo y alertas manuales](L11-monitoreo-minimo-y-alertas-manuales.md)
