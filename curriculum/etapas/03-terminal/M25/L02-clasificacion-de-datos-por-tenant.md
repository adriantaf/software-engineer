---
id: L02
materia: M25
orden: 2
titulo: Clasificación de datos por tenant
horas: 5.0
semana: 1
lectura: OWASP Testing Guide — information gathering
evidencia: projects/m25-ciber/clasificacion-datos.md
---

# L02 — Clasificación de datos por tenant

**~5 h · Semana 1**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/clasificacion-datos.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Etiquetar datos (PII citas, credenciales, billing metadata) y flujo entre componentes.

## Por qué empieza así

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

Conceptos que debes poder explicar al cerrar:

- PII mínima
- tenant_id como control
- Logs y PII

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Testing Guide — information gathering_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Prepara carpetas (15–25 min)

```bash
mkdir -p projects/m25-ciber
```

Confirma que escribirás `projects/m25-ciber/clasificacion-datos.md`.

### 3. Laboratorio principal (100–130 min)

`projects/m25-ciber/clasificacion-datos.md`: por tipo de dato, ¿en qué tabla/campo?, ¿quién accede?, retención esperada.

### 4. Criterio de calidad (30–45 min)

Relee `projects/m25-ciber/clasificacion-datos.md`: ¿un mentor externo entendería el resultado sin preguntarte?

Añade enlace a issue/PR/URL de staging si aplica. Bitácora de la semana: 5 líneas de horas y bloqueos.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m25): l02 clasificaci-n-de-datos-por-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Testing Guide — information gathering | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/clasificacion-datos.md`.
2. Sin secretos en markdown.
3. Conexión Agenda Ops escrita en bitácora.
4. Commit `docs(m25): l02 …` en el historial.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L03 — Dos tenants de prueba y mapa de identidades](L03-dos-tenants-de-prueba-y-mapa-de-identidades.md)
