---
id: L03
materia: M25
orden: 3
titulo: Dos tenants de prueba y mapa de identidades
horas: 5.0
semana: 1
lectura: OWASP Testing Guide — information gathering
evidencia: projects/m25-ciber/tenants-prueba.md
---

# L03 — Dos tenants de prueba y mapa de identidades

**~5 h · Semana 1**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/tenants-prueba.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Crear tenant A y B con usuarios staff distintos; documentar IDs y roles.

## Por qué empieza así

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

Conceptos que debes poder explicar al cerrar:

- Tenant de prueba realista
- Separación de datos
- No tenant1 genérico

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Testing Guide — information gathering_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Prepara carpetas (15–25 min)

```bash
mkdir -p projects/m25-ciber
```

Confirma que escribirás `projects/m25-ciber/tenants-prueba.md`.

### 3. Laboratorio principal (100–130 min)

`projects/m25-ciber/tenants-prueba.md`: nombres de negocio ficticios, emails de prueba, roles. Sin contraseñas en claro.

### 4. Criterio de calidad (30–45 min)

Relee `projects/m25-ciber/tenants-prueba.md`: ¿un mentor externo entendería el resultado sin preguntarte?

Añade enlace a issue/PR/URL de staging si aplica. Bitácora de la semana: 5 líneas de horas y bloqueos.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m25): l03 dos-tenants-de-prueba-y-mapa-de-identida"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Testing Guide — information gathering | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/tenants-prueba.md`.
2. Sin secretos en markdown.
3. Conexión Agenda Ops escrita en bitácora.
4. Commit `docs(m25): l03 …` en el historial.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L04 — Primera prueba manual cross-tenant](L04-primera-prueba-manual-cross-tenant.md)
