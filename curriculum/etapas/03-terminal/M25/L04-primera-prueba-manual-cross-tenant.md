---
id: L04
materia: M25
orden: 4
titulo: Primera prueba manual cross-tenant
horas: 5
semana: 1
lectura: "OWASP Testing Guide — information gathering"
evidencia: "projects/m25-ciber/ inventario o aislamiento según lección"
---

# L04 — Primera prueba manual cross-tenant

**~5 h · Semana 1**

## Objetivo

Intentar leer recurso del tenant B autenticado como A; documentar resultado.

## Por qué importa

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

## Conceptos

- IDOR
- 403 vs 404
- Evidencia reproducible

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m25-ciber/aislamiento/nota-l01.md`: endpoint, IDs usados, status code, captura o curl redactado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m25): l04 primera-prueba-manual-cross-tenant"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Testing Guide inventario | [producto-saas](../../producto-saas.md) |
| Ficha | M25 checklist SaaS | M18 access control |
| Catálogo | Entrada M25 | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

1. Archivo de evidencia de L04 en git.
2. Sin secretos en markdown.
3. Conexión Agenda Ops escrita en bitácora.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.

## Siguiente

[L05 — Review authn — sesión y tokens](L05-review-authn-sesion-y-tokens.md)
