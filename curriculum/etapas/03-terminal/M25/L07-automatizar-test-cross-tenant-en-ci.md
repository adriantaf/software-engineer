---
id: L07
materia: M25
orden: 7
titulo: Automatizar test cross-tenant en CI
horas: 5.0
semana: 2
lectura: OWASP — Identity / Authorization testing
evidencia: projects/m25-ciber/aislamiento/tests.md
---

# L07 — Automatizar test cross-tenant en CI

**~5 h · Semana 2**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/aislamiento/tests.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Al menos un test que falle si A lee cita de B.

## Por qué empieza así

Cosmética CSS no salva un leak entre barberías.

Conceptos que debes poder explicar al cerrar:

- Authn vs authz
- tenant_id en sesión
- Tests de regresión

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP — Identity / Authorization testing_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Elige harness (25–35 min)

Vitest/Jest/supertest en el repo producto. Anota comando `npm test -- aislamiento` (o similar) en `aislamiento/tests.md`.

### 3. Escribe el test cross-tenant (100–130 min)

Test mínimo: login A + GET recurso B → assert status ∈ {403,404} **o** body sin datos de B.

Si aún no hay seed de dos tenants, crea helper de seed en test (no uses prod).

### 4. Corre y documenta (30–40 min)

Pega salida del test (verde o rojo). Si rojo porque el bug existe: deja el test fallando **o** `it.failing` documentado + issue. Objetivo: el fallo sea visible.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l07 automatizar-test-cross-tenant-en-ci"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP — Identity / Authorization testing | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/aislamiento/tests.md`.
2. Evidencia en ruta indicada.
3. Si es test: corre en CI o documenta por qué no aún.
4. Commit `docs(m25): l07 …` en el historial.

## Errores comunes

- 50 hallazgos menores y cero cross-tenant.
- tenant_id solo en frontend.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L08 — Cerrar ≥1 hallazgo crítico de aislamiento](L08-cerrar-1-hallazgo-critico-de-aislamiento.md)
