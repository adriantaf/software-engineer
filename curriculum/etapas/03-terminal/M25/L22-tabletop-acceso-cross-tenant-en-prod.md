---
id: L22
materia: M25
orden: 22
titulo: Tabletop — acceso cross-tenant en prod
horas: 5.0
semana: 6
lectura: OWASP Reporting + ficha M25
evidencia: projects/m25-ciber/tabletop/cross-tenant-incident.md
---

# L22 — Tabletop — acceso cross-tenant en prod

**~5 h · Semana 6**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/tabletop/cross-tenant-incident.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Simulación: reporte cliente; contención; fix.

## Por qué empieza así

M26 exige review M25 vigente; tabletop demuestra que no solo leíste OWASP.

Conceptos que debes poder explicar al cerrar:

- Contención
- Rotación credenciales
- Post-mortem blameless

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Reporting + ficha M25_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Escenario cross-tenant en prod (30–40 min)

En `projects/m25-ciber/tabletop/cross-tenant-incident.md`: cliente B reporta ver datos de A. Define detección inicial.

### 3. Timeline de contención (90–110 min)

T+0 … T+120: verificar, deshabilitar endpoint/feature flag, notificar, rotar si aplica, comunicar.

Roles: tú = on-call. Sin copiar blog genérico — usa tus URLs/servicios.

### 4. Acciones y dueños (25–35 min)

Checklist ≥8 acciones con evidencia esperada. Bitácora semana-06.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l22 tabletop-acceso-cross-tenant-en-prod"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Reporting + ficha M25 | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/tabletop/cross-tenant-incident.md`.
2. Narrativa ≥30 min equivalente escrita.
3. security-review.md enlaza PRs y tests.
4. Commit `docs(m25): l22 …` en el historial.

## Errores comunes

- Tabletop copiado de blog.
- Review sin pruebas cross-tenant.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L23 — Runbook de respuesta incidentes](L23-runbook-de-respuesta-incidentes.md)
