---
id: L24
materia: M25
orden: 24
titulo: Security review final y cierre M25
horas: 5
semana: 6
lectura: "OWASP Reporting + ficha M25"
evidencia: "projects/m25-ciber/security-review.md"
---

# L24 — Security review final y cierre M25

**~5 h · Semana 6**

## Objetivo

Completar `security-review.md`; checklist dominio; handoff M26.

## Por qué importa

M26 exige review M25 vigente; tabletop demuestra que no solo leíste OWASP.

## Conceptos

- Contención
- Rotación credenciales
- Post-mortem blameless

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Cada tabletop: línea de tiempo, decisiones, acciones con dueño y fecha.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m25): l24 security-review-final-y-cierre-m25"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | Proyecto security-review | egreso.md |
| Catálogo | Entrada M25 | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

1. Narrativa ≥30 min equivalente escrita.
2. security-review.md enlaza PRs y tests.

## Errores comunes

- Tabletop copiado de blog.
- Review sin pruebas cross-tenant.
