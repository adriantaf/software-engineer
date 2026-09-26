---
id: L09
materia: M19
orden: 9
titulo: Promover configuración a producción
horas: 5.0
semana: 3
lectura: 12-factor config
evidencia: projects/m19-ops/ambientes.md actualizado
---

# L09 — Promover configuración a producción

**~5.0 h · Semana 3**

Prod es para design partner, no laboratorio.

## Objetivo

Desplegar prod con misma imagen que staging y distintas env vars; documentar diferencias.

## Conceptos clave

- promoción imagen
- separación datos

## Pasos (hazlos en orden)

### 1. Checklist promoción a prod (60–80 min)

```bash
cat >> projects/m19-ops/ambientes.md << 'EOF'
## Promoción staging → prod
1. Migraciones aplicadas
2. Secrets distintos a staging
3. Smoke health+login
4. Rollback plan listo
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/ambientes.md
git commit -m "docs(m19): L09 promover config a produccion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | 12-factor config | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/ambientes.md` incluye checklist de promoción a prod.
2. Commit `docs(m19): L09 promover-configuracion-a-produccion`.

## Errores comunes

- Promover con mismos secrets que staging.
- Sin plan de rollback.

## Siguiente

[L10 — Logs, rollback y versión desplegada](L10-logs-rollback-y-version-desplegada.md)
