---
id: L24
materia: M25
orden: 24
titulo: Security review final y cierre M25
horas: 5.0
semana: 6
lectura: OWASP Reporting + ficha M25
evidencia: projects/m25-ciber/security-review.md
---

# L24 — Security review final y cierre M25

**~5 h · Semana 6**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/security-review.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Completar `security-review.md`; checklist dominio; handoff M26.

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

### 2. Reúne evidencias P1–P3 (40–50 min)

Índice en `security-review.md`: inventario, aislamiento (manual+CI), ≥2 hallazgos cerrados, hardenings, tabletops, runbook.

### 3. Rúbrica y riesgo residual (80–100 min)

Tabla de controles: control | evidencia | residual. Declara qué **no** está listo para M26 demo pública.

### 4. Handoff M26 (30–40 min)

Sección handoff: issues abiertos, tests obligatorios en CI, secretos a rotar antes de video público.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l24 security-review-final-y-cierre-m25"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Reporting + ficha M25 | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/security-review.md`.
2. Narrativa ≥30 min equivalente escrita.
3. security-review.md enlaza PRs y tests.
4. Commit `docs(m25): l24 …` en el historial.

## Errores comunes

- Tabletop copiado de blog.
- Review sin pruebas cross-tenant.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
