---
id: L29
materia: M18
orden: 29
titulo: "Pipeline CI: lint, test, audit, anti-secretos"
horas: 5
semana: 8
lectura: "Secure SDLC + CI guides"
evidencia: "projects/m18-appsec/ci-appsec.yml snippet o enlace workflow"
---

# L29 — Pipeline CI: lint, test, audit, anti-secretos

**~5 h · Semana 8**

## Objetivo

Añadir job CI con lint, tests, `npm audit` (fail on high), grep básico anti-secretos.

## Por qué importa

P3 de la ficha: seguridad en el pipeline, no solo en la cabeza.

## Conceptos

- Fail build on audit.
- Trufflehog/gitleaks lite.
- Branch protection (idea).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea o extiende workflow GitHub Actions / CI del repo. Documenta en `projects/m18-appsec/ci-appsec.md` qué corre en cada PR.

Ejecuta pipeline en branch de prueba y pega enlace/run id.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l29 pipeline-ci-lint-test-audit-anti-secreto"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | DevSecOps guideline | Ficha P3 |

## Hecho cuando

1. CI documentado.
2. Audit en pipeline.
3. Run verde o excepciones justificadas.

## Errores comunes

- CI que nunca falla.
- Secretos en workflow logs.

## Siguiente

[L30 — Estructura del informe AppSec](L30-estructura-del-informe-appsec.md)
