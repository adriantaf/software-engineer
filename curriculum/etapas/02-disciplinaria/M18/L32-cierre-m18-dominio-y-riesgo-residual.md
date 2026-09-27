---
id: L32
materia: M18
orden: 32
titulo: Cierre M18 — dominio y riesgo residual
horas: 5.0
semana: 8
lectura: Repaso completo M18
evidencia: projects/m18-appsec/informe-appsec.md final + README
---

# L32 — Cierre M18 — dominio y riesgo residual

**~5.0 h · Semana 8**

Riesgo residual explícito > “somos seguros”. Cierra P1–P3 y handoff a M19/M25.

## Objetivo

`projects/m18-appsec/informe-appsec.md` final + README con residual top-3 y criterios de dominio.

## Pasos

### 1. Auditoría de evidencias (40–50 min)

```bash
ls -la projects/m18-appsec projects/m18-appsec/docs projects/m18-appsec/findings projects/m18-appsec/ci projects/m18-appsec/pocs
test -f projects/m18-appsec/threat-model-v1.md && echo P1=ok
wc -l projects/m18-appsec/findings-table.md
test -f projects/m18-appsec/ci/ci-appsec.yml && echo P3=ok
test -f projects/m18-appsec/docs/auth-inventario.md && echo auth=ok
```
### 2. Residual + handoff (50–60 min)

```bash
printf "\n## Riesgo residual (cierre)\n| Riesgo | Dueño | Fecha revisión |\n|--------|-------|----------------|\n| … | | |\n\n## Handoff\n- M19: secrets en PaaS, HTTPS, backups\n- M25: retest en trial\n" >> projects/m18-appsec/informe-appsec.md
```
### 3. README final (20–30 min)

Actualiza `projects/m18-appsec/README.md`: P1/P2/P3 ✅, enlace informe, residual.

```bash
git add projects/m18-appsec/README.md projects/m18-appsec/informe-appsec.md
git commit -m "docs(m18): l32 cierre dominio residual"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Repaso completo M18 | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Informe final (artefacto: `projects/m18-appsec/informe-appsec.md final`).
2. P1–P3 verificables (artefacto: `projects/m18-appsec/informe-appsec.md final`).
3. Commit `docs(m18): L32 cierre-m18-dominio-y-riesgo-residual`.

## Errores comunes

- Marcar dominio sin tests.
- Deploy público sin headers.

## Siguiente

Materia siguiente / refuerzo: [M19 — Nube/DevOps](../M19-nube-devops.md) y [hilo seguridad](../../../hilos/seguridad.md).
