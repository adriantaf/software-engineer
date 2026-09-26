---
id: L08
materia: M25
orden: 8
titulo: Cerrar ≥1 hallazgo crítico de aislamiento
horas: 5.0
semana: 2
lectura: OWASP — Identity / Authorization testing
evidencia: projects/m25-ciber/hallazgos/hallazgo-01.md
---

# L08 — Cerrar ≥1 hallazgo crítico de aislamiento

**~5 h · Semana 2**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/hallazgos/hallazgo-01.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Fix + PR + evidencia antes de seguir cosméticos.

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

### 2. Prepara carpetas (15–25 min)

```bash
mkdir -p projects/m25-ciber/hallazgos
```

Confirma que escribirás `projects/m25-ciber/hallazgos/hallazgo-01.md`.

### 3. Laboratorio principal (100–130 min)

Trabaja en **tu** Agenda Ops desplegado. Registra comandos `curl` o Vitest/Jest con tokens de A y B.

Actualiza `projects/m25-ciber/bitacora/semana-02.md`.

### 4. Criterio de calidad (30–45 min)

Relee `projects/m25-ciber/hallazgos/hallazgo-01.md`: ¿un mentor externo entendería el resultado sin preguntarte?

Añade enlace a issue/PR/URL de staging si aplica. Bitácora de la semana: 5 líneas de horas y bloqueos.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m25): l08 cerrar-1-hallazgo-cr-tico-de-aislamiento"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP — Identity / Authorization testing | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/hallazgos/hallazgo-01.md`.
2. Evidencia en ruta indicada.
3. Si es test: corre en CI o documenta por qué no aún.
4. Commit `docs(m25): l08 …` en el historial.

## Errores comunes

- 50 hallazgos menores y cero cross-tenant.
- tenant_id solo en frontend.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L09 — HTTPS, headers y configuración prod](L09-https-headers-y-configuracion-prod.md)
