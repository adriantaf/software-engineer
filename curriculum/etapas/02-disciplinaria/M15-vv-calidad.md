---
id: M15
titulo: Verificación, validación y calidad
etapa: disciplinaria
orden: 15
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Pirámide de tests en Agenda Ops
  - id: p2
    titulo: CI en GitHub Actions (lint + test + audit)
  - id: p3
    titulo: Checklist de code review (incluye seguridad)
proyecto:
  id: proj
  titulo: Pipeline CI verde + coverage en lógica de negocio
---

# M15 — Verificación, validación y calidad

## Por qué existe

Sin pruebas automatizadas, cada cambio en Agenda Ops es apuesta. La calidad no es un departamento: es pirámide de tests, integración continua y revisiones que incluyen **auth, IDOR y validación de entrada** ([hilo seguridad](../../hilos/seguridad.md)). Esta materia prepara el pipeline que M17 mantendrá verde y que M18 endurecerá con tests de regresión AppSec.

**En resumen:** la calidad deja de ser opcional: pirámide de tests, CI y reviews que incluyen seguridad.


## Objetivos de aprendizaje

Al terminar debes poder:

1. Diseñar una pirámide de tests (unitarios, integración, pocos E2E) para el dominio de citas/clientes.
2. Escribir tests de dominio y API que fallen ante reglas de negocio rotas.
3. Incluir casos de seguridad mínimos: sin auth, IDOR, input inválido.
4. Configurar CI en GitHub Actions: lint, test, audit de dependencias.
5. Usar mocks/fakes con criterio (no probar solo el mock).
6. Aplicar checklist de code review con ítems de seguridad y calidad.
7. Medir coverage útil en lógica de negocio, no en archivos boilerplate.

## Cómo estudiar esta materia (lecciones)

M15 deja la calidad del piloto **Agenda Ops** automatizada: L01–L16.

1. Cada bug encontrado → test de regresión el mismo día (regla del plan).
2. Trabaja sobre spike en `projects/m15-calidad/` o el repo M17 cuando exista.
3. CI debe ser obligatoria para merge; no “corro tests a mano cuando me acuerdo”.
4. Marca lecciones al cumplir “Hecho cuando”.
5. [Cómo estudiar](../../como-estudiar.md) y [hilo seguridad](../../hilos/seguridad.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Tests | 6–8 | Lecciones unit/API de la semana |
| CI | 6–8 | Workflow Actions lint+test+audit |
| Review | 4–6 | Checklist en PR real o simulado |
| Retro | 1 | Bug → test documentado |

Si un día solo tienes 2 h: **una lección práctica**. No saltes la lectura de esa lección.

## Lecciones

### Semana 1 — Pirámide y tests de dominio (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Entorno M15 y pirámide de tests](M15/L01-entorno-m15-y-piramide-de-tests.md) | 5 |
| L02 | [Tests unitarios puros de reglas de cita](M15/L02-tests-unitarios-puros-de-reglas-de-cita.md) | 5 |
| L03 | [Qué no testear y carpetas de coverage](M15/L03-que-no-testear-y-carpetas-de-coverage.md) | 5 |
| L04 | [Cierre semana 1 — suite dominio y bitácora](M15/L04-cierre-semana-1-suite-dominio-y-bitacora.md) | 5 |

### Semana 2 — Integración, fakes y API (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Fake repositorio y reloj para tests rápidos](M15/L05-fake-repositorio-y-reloj-para-tests-rapidos.md) | 5 |
| L06 | [Tests de integración con persistencia](M15/L06-tests-de-integracion-con-persistencia.md) | 5 |
| L07 | [Tests HTTP de API — auth y validación](M15/L07-tests-http-de-api-auth-y-validacion.md) | 5 |
| L08 | [IDOR y roles — casos 403](M15/L08-idor-y-roles-casos-403.md) | 5 |

### Semana 3 — CI en GitHub Actions (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Workflow GitHub Actions — esqueleto](M15/L09-workflow-github-actions-esqueleto.md) | 5 |
| L10 | [Lint y formato en pipeline](M15/L10-lint-y-formato-en-pipeline.md) | 5 |
| L11 | [npm audit y política de dependencias](M15/L11-npm-audit-y-politica-de-dependencias.md) | 5 |
| L12 | [Badge README y artefacto de test](M15/L12-badge-readme-y-artefacto-de-test.md) | 5 |

### Semana 4 — Review, regresión y cierre (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Checklist de code review](M15/L13-checklist-de-code-review.md) | 5 |
| L14 | [Review simulado en PR o notas](M15/L14-review-simulado-en-pr-o-notas.md) | 5 |
| L15 | [Política bug → test el mismo día](M15/L15-politica-bug-test-el-mismo-dia.md) | 5 |
| L16 | [Cierre M15 — pipeline, coverage dominio, dominio](M15/L16-cierre-m15-pipeline-coverage-dominio-dominio.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Código limpio* (cap. pruebas) + *El programador pragmático* (testing) + docs Vitest. Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos / docs | Alternativa |
|--------|-----------|------------------|-------------|
| 1 | L01–L04 | *Código limpio* **cap. 9** + `piramide.md` | [Vitest](https://vitest.dev) |
| 2 | L05–L08 | Mocks/fakes + tests HTTP 401/403 | OWASP Auth (selecto) |
| 3 | L09–L12 | GitHub Actions + lint + `npm audit` | Workflow en repo |
| 4 | L13–L16 | Checklist review + regresiones + cierre | OWASP Testing Guide (selecto) |

**Regla:** un bug encontrado → test de regresión el mismo día.



## Ejemplo — tabla de casos mínimos (crear cita)

| Caso | Entrada | Esperado |
|------|---------|----------|
| Feliz | slot libre, usuario owner | 201 + cita |
| Duplicado | mismo slot | 409 o error dominio |
| Sin auth | sin cookie/token | 401 |
| IDOR | cita de otro negocio/usuario | 403 |
| Inválido | fin antes de inicio | 400 |

## Ejemplo — workflow CI mínimo (esquema)

```yaml
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm audit --audit-level=high
```

Ajusta rutas si el código vive en monorepo; documenta en `projects/m15-calidad/README.md`.

## Temario semanal

### Semana 1 — Pirámide y tests de dominio (~20 h)

- Unit tests puros: reglas de citas, precios, validaciones.
- Qué no testear (framework, detalles de ORM sin valor).
- Coverage en carpetas `domain/` o equivalente.
- Entregable: suite inicial + `piramide.md`.

### Semana 2 — Integración, mocks y API (~20 h)

- Tests de integración con DB de prueba o Testcontainers (si aplica).
- Fakes de reloj o repositorio en memoria para tests rápidos.
- Tests HTTP supertest/fetch contra app levantada en test.
- Ampliar casos de seguridad del Día 1.

### Semana 3 — CI y calidad en el pipeline (~20 h)

- GitHub Actions: lint, test, `npm audit` o equivalente.
- Fallar build en audit high/critical (o documentar excepciones con ticket).
- Badge o enlace al workflow en README del proyecto.
- Entregable: workflow en `.github/workflows/` (repo raíz o documentado desde M15).

### Semana 4 — Review, regresión y cierre (~20 h)

- Checklist de PR: estilo, tests, seguridad, migraciones, secrets.
- Simular review en PR propio o `projects/m15-calidad/review-ejemplo.md`.
- Política: bug encontrado → test el mismo día.
- Changelog o notas de versión si aplicas semver en el piloto.


## Prácticas

1. **P1 — Pirámide:** Tests en ≥2 capas (unit + integration o API) documentados en `projects/m15-calidad/`.
2. **P2 — CI:** Workflow verde en GitHub Actions (ruta documentada en README M15).
3. **P3 — Checklist:** `projects/m15-calidad/checklist-review.md` aplicado a un PR (captura o comentarios).

## Proyecto útil

**Pipeline CI verde + coverage en negocio:**

- Workflow estable en main.
- Reporte de coverage (Vitest v8 o c8) enfocado en módulos de dominio.
- `projects/m15-calidad/README.md` explica cómo correr tests local y en CI.

## Errores comunes

- Tests que solo assertan mocks (cero confianza).
- CI opcional o saltable con `--no-verify` habitual.
- Cero tests de auth/IDOR “porque es piloto”.
- Perseguir 100 % coverage en DTOs y cero en reglas de citas.
- No pinchar versiones en CI y builds flaky sin investigar.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Pirámide:** `projects/m15-calidad/piramide.md` + tests en `projects/m15-calidad/tests/` (o repo producto enlazado).
- **P2 — CI:** `.github/workflows/*.yml` verde (enlace en `projects/m15-calidad/README.md`).
- **P3 — Checklist:** `projects/m15-calidad/checklist-review.md` + evidencia de uso en PR.
- **Proyecto — Pipeline:** coverage de dominio documentado + `npm audit` (o equivalente) en CI.

## Criterios de dominio

- [ ] Un bug en prod (o piloto) tendría test de regresión al día siguiente.
- [ ] CI corre lint, test y audit sin pasos manuales olvidados.
- [ ] Demuestras caso 401 y 403 con test automatizado.
- [ ] Sabes explicar qué parte de la pirámide no merece E2E todavía.
