---
id: L01
materia: M25
orden: 1
titulo: Inventario de activos SaaS prod y staging
horas: 5.0
semana: 1
lectura: OWASP Testing Guide — information gathering
evidencia: projects/m25-ciber/inventario.md
---

# L01 — Inventario de activos SaaS prod y staging

**~5 h · Semana 1**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/inventario.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Listar URLs, repos, DB, colas, webhooks Stripe, CI y clasificar sin secretos.

## Por qué empieza así

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

Conceptos que debes poder explicar al cerrar:

- Superficie de ataque
- Staging ≠ prod
- Activo sin dueño = riesgo

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Testing Guide — information gathering_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Crea carpetas de evidencia (15–20 min)

```bash
mkdir -p projects/m25-ciber/{aislamiento,review,hardening,logging,abuso,alertas,privacidad,tabletop,hallazgos,bitacora}
```

Lee `projects/m25-ciber/README.md` y anota URLs de staging/prod que ya tengas (M19).

### 3. Inventario sin secretos (90–120 min)

Crea `projects/m25-ciber/inventario.md` con tabla:

| Activo | Tipo | Ambiente | Dueño | Notas |
|--------|------|----------|-------|-------|

Incluye ≥8 filas: API Agenda Ops, panel, Postgres, dominio, CI, webhook Stripe, storage/backups, repo. **Sin** passwords ni API keys.

### 4. Marca superficie de ataque (40–50 min)

Añade sección **Superficie** con 5 endpoints o entradas de datos (login, citas CRUD, webhooks, exports). Bitácora `bitacora/semana-01.md` con 5 líneas.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m25): l01 inventario-de-activos-saas-prod-y-stagin"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Testing Guide — information gathering | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/inventario.md`.
2. Sin secretos en markdown.
3. Conexión Agenda Ops escrita en bitácora.
4. Commit `docs(m25): l01 …` en el historial.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L02 — Clasificación de datos por tenant](L02-clasificacion-de-datos-por-tenant.md)
