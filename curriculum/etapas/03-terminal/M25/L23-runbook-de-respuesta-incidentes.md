---
id: L23
materia: M25
orden: 23
titulo: Runbook de respuesta incidentes
horas: 5.0
semana: 6
lectura: OWASP Reporting + ficha M25
evidencia: projects/m25-ciber/runbook-incidentes.md
---

# L23 — Runbook de respuesta incidentes

**~5 h · Semana 6**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/runbook-incidentes.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Unificar playbooks en runbook corto enlazado desde ops.

## Por qué empieza así

M26 exige review M25 vigente; tabletop demuestra que no solo leíste OWASP.

Conceptos que debes poder explicar al cerrar:

- Contención
- Rotación credenciales
- Post-mortem blameless

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Reporting + ficha M25_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Índice de playbooks (25–35 min)

En `projects/m25-ciber/runbook-incidentes.md` enlaza tabletops L21–L22 + hardening relevante.

### 3. Runbook operable (100–120 min)

Secciones fijas: **Severidad**, **Contactos**, **Contención 15 min**, **Evidencia a preservar**, **Comunicación**, **Post-mortem**.

Cada sección con pasos numerados ejecutables a las 3 a.m.

### 4. Enlace desde ops (20–30 min)

Añade link desde `projects/m25-ciber/README.md` o runbook M19. Bitácora semana-06.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l23 runbook-de-respuesta-incidentes"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Reporting + ficha M25 | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/runbook-incidentes.md`.
2. Narrativa ≥30 min equivalente escrita.
3. security-review.md enlaza PRs y tests.
4. Commit `docs(m25): l23 …` en el historial.

## Errores comunes

- Tabletop copiado de blog.
- Review sin pruebas cross-tenant.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L24 — Security review final y cierre M25](L24-security-review-final-y-cierre-m25.md)
