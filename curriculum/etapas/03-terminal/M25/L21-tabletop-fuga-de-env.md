---
id: L21
materia: M25
orden: 21
titulo: Tabletop — fuga de .env
horas: 5
semana: 6
lectura: "OWASP Reporting + ficha M25"
evidencia: "projects/m25-ciber/tabletop/env-leak.md"
---

# L21 — Tabletop — fuga de .env

**~5 h · Semana 6**

## Objetivo

Simulación 30 min: secretos filtrados; pasos; comunicación.

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
git commit -m "docs(m25): l21 tabletop-fuga-de-env"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | Proyecto security-review | egreso.md |

## Hecho cuando

1. Narrativa ≥30 min equivalente escrita.
2. security-review.md enlaza PRs y tests.

## Errores comunes

- Tabletop copiado de blog.
- Review sin pruebas cross-tenant.

## Siguiente

[L22 — Tabletop — acceso cross-tenant en prod](L22-tabletop-acceso-cross-tenant-en-prod.md)
