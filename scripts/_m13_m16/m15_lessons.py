"""M15 — V&V y calidad: 16 lessons at M01/M09 quality."""
from __future__ import annotations

FILENAMES = {
    1: "L01-entorno-m15-y-piramide-de-tests.md",
    2: "L02-tests-unitarios-puros-de-reglas-de-cita.md",
    3: "L03-que-no-testear-y-carpetas-de-coverage.md",
    4: "L04-cierre-semana-1-suite-dominio-y-bitacora.md",
    5: "L05-fake-repositorio-y-reloj-para-tests-rapidos.md",
    6: "L06-tests-de-integracion-con-persistencia.md",
    7: "L07-tests-http-de-api-auth-y-validacion.md",
    8: "L08-idor-y-roles-casos-403.md",
    9: "L09-workflow-github-actions-esqueleto.md",
    10: "L10-lint-y-formato-en-pipeline.md",
    11: "L11-npm-audit-y-politica-de-dependencias.md",
    12: "L12-badge-readme-y-artefacto-de-test.md",
    13: "L13-checklist-de-code-review.md",
    14: "L14-review-simulado-en-pr-o-notas.md",
    15: "L15-politica-bug-test-el-mismo-dia.md",
    16: "L16-cierre-m15-pipeline-coverage-dominio-dominio.md",
}

LESSONS: list[dict] = []

LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Entorno M15 y pirámide de tests",
        horas=5.0,
        semana=1,
        lectura="Pirámide de tests; Vitest setup Agenda Ops",
        evidencia="projects/m15-calidad/ + piramide.md + Vitest verde",
        _lectura_corta="Pirámide: muchos unit, menos integración, pocos E2E",
        _enlace_titulo="Vitest — Getting Started",
        _enlace="https://vitest.dev/guide/",
        _hecho="""1. `projects/m15-calidad/` con Vitest y un test smoke verde.
2. `piramide.md` dibuja capas y qué irá en cada una para citas/auth.
3. Commit `docs(m15): entorno y piramide de tests`.""",
        _errores="""- Pirámide invertida (todo E2E).
- Proyecto sin script `test`.
- Copiar pirámide genérica sin mapear a Agenda Ops.""",
        siguiente="[L02 — Tests unitarios puros de reglas de cita](L02-tests-unitarios-puros-de-reglas-de-cita.md)",
        body=r"""
# L01 — Entorno M15 y pirámide de tests

**~5.0 h · Semana 1**

Sin suite local, CI es teatro. Hoy levantas Vitest y decides la pirámide del piloto.

## Objetivo

`projects/m15-calidad/` ejecutable + `piramide.md` concreto.

## Por qué empieza así

M14 te dejó reglas/services; M15 los blindan. M17 heredará este pipeline.

## Pasos (hazlos en orden)

### 1. Scaffold (50–70 min)

```bash
cd projects/m15-calidad
npm init -y
npm install -D typescript vitest @types/node
# scripts.test = "vitest run"
```

Estructura:

```text
src/domain/
src/application/
tests/
piramide.md
```

Puedes reutilizar lógica de `projects/m14-patrones` (copia o path documentado).

### 2. Smoke test (30 min)

`tests/smoke.test.ts` assert `1+1` o import de un módulo dominio.

### 3. piramide.md (60–70 min)

| Capa | Ejemplos Agenda Ops | Cantidad relativa |
|------|---------------------|-------------------|
| Unit | solape, precio, DTO validate | mayoría |
| Integración | repo + Postgres test | media |
| HTTP/API | 401/403 crear cita | menos |
| E2E UI | 1–2 flujos | mínimo |

### 4. Commit

`docs(m15): entorno y piramide de tests`
""",
    )
)

LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Tests unitarios puros de reglas de cita",
        horas=5.0,
        semana=1,
        lectura="Código limpio cap. pruebas; reglas de solape/estado",
        evidencia="tests/domain/ reglas de cita ≥5 tests",
        _lectura_corta="Unit tests puros: sin I/O; reglas de cita",
        _hecho="""1. Funciones de dominio (solape, transición de estado, o validar rango) con ≥5 tests.
2. Al menos un test que **falla** si rompes la regla a propósito (red→green documentado en nota breve).
3. Commit `test(m15): reglas de cita unitarias`.""",
        _errores="""- Tests que levantan servidor HTTP para una resta de fechas.
- Asserts débiles (`toBeTruthy` en objetos).
- Reglas duplicadas en test y producción divergentes.""",
        siguiente="[L03 — Qué no testear y carpetas de coverage](L03-que-no-testear-y-carpetas-de-coverage.md)",
        body=r"""
# L02 — Tests unitarios puros de reglas de cita

**~5.0 h · Semana 1**

La base de la pirámide: reglas que el dueño del negocio nota si fallan (doble booking).

## Objetivo

Suite unitaria de dominio de citas sin DB ni HTTP.

## Pasos (hazlos en orden)

### 1. Extrae regla (40–50 min)

Ejemplo:

```ts
export function rangesOverlap(aStart: Date, aEnd: Date, bStart: Date, bEnd: Date): boolean {
  return aStart < bEnd && bStart < aEnd;
}
```

### 2. Tabla de casos (60–70 min)

Adyacentes, contenidos, idénticos, invertidos (`end < start` → throw/invalid).

### 3. Red→green (30 min)

Rompe la función, mira fallar, restaura — anota en `docs/red-green-cita.md`.

### 4. Commit

`test(m15): reglas de cita unitarias`
""",
    )
)

LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Qué no testear y carpetas de coverage",
        horas=5.0,
        semana=1,
        lectura="Coverage útil; exclusiones conscientes",
        evidencia="vitest coverage en domain/ + docs/no-testear.md",
        _lectura_corta="No perseguir 100% en boilerplate; coverage en domain/",
        _enlace_titulo="Vitest — Coverage",
        _enlace="https://vitest.dev/guide/coverage.html",
        _hecho="""1. Coverage configurado enfocando `src/domain/**` (o carpeta equivalente).
2. `docs/no-testear.md` lista ≥3 cosas que no testearás (ORM glue, framework).
3. Commit `test(m15): coverage dominio y politica no-testear`.""",
        _errores="""- 100% en DTOs vacíos y 0% en solape.
- Excluir `domain/` “porque es difícil”.
- Subir reportes HTML enormes al repo sin necesidad.""",
        siguiente="[L04 — Cierre semana 1 — suite dominio y bitácora](L04-cierre-semana-1-suite-dominio-y-bitacora.md)",
        body=r"""
# L03 — Qué no testear y carpetas de coverage

**~5.0 h · Semana 1**

Coverage es brújula, no religión. Hoy apuntas el medidor al dominio.

## Objetivo

Config de coverage + política escrita.

## Pasos (hazlos en orden)

### 1. Instala provider (30 min)

`npm i -D @vitest/coverage-v8` y script `test:cov`.

### 2. include domain (40 min)

### 3. no-testear.md (50 min)

Ejemplos: wrappers del framework, generados, `main.ts` de boot.

### 4. Commit

`test(m15): coverage dominio y politica no-testear`
""",
    )
)

LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Cierre semana 1 — suite dominio y bitácora",
        horas=5.0,
        semana=1,
        lectura="Cierre suite dominio; bitácora",
        evidencia="bitacora-semana-1.md + piramide actualizada",
        _lectura_corta="Cierre semana 1: unitarios de dominio estables",
        _hecho="""1. `npm test` verde; bitácora lista reglas cubiertas.
2. piramide.md actualizada con conteo real de tests unitarios.
3. Commit `docs(m15): cierre semana 1 suite dominio`.""",
        _errores="""- Suite flaky ignorada.
- Bitácora sin números.
- Marcar avance sin coverage script.""",
        siguiente="[L05 — Fake repositorio y reloj para tests rápidos](L05-fake-repositorio-y-reloj-para-tests-rapidos.md)",
        body=r"""
# L04 — Cierre semana 1 — suite dominio y bitácora

**~5.0 h · Semana 1**

Consolida la base unitaria antes de fakes e HTTP.

## Objetivo

Bitácora + pirámide con números reales.

## Pasos (hazlos en orden)

### 1. Corre suite + cov (30 min)

### 2. Bitácora (50 min)

### 3. Deuda (30 min) — qué falta en integración

### 4. Commit

`docs(m15): cierre semana 1 suite dominio`
""",
    )
)

LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Fake repositorio y reloj para tests rápidos",
        horas=5.0,
        semana=2,
        lectura="Fakes vs mocks; reloj inyectable",
        evidencia="InMemory repo + Clock fake + tests de servicio",
        _lectura_corta="Fakes: repo en memoria y reloj determinista",
        _hecho="""1. `FakeClock` o `() => Date` inyectable; test de “cita en el pasado” estable.
2. Repo in-memory usado por tests de application service.
3. Commit `test(m15): fake repo y reloj`.""",
        _errores="""- Mock de cada método del repo sin estado (frágil).
- `Date.now` global sin restore.
- Fake más complejo que producción.""",
        siguiente="[L06 — Tests de integración con persistencia](L06-tests-de-integracion-con-persistencia.md)",
        body=r"""
# L05 — Fake repositorio y reloj para tests rápidos

**~5.0 h · Semana 2**

Los tests de application layer deben ser rápidos y deterministas.

## Objetivo

Fakes de repo y reloj cableados al service de citas.

## Pasos (hazlos en orden)

### 1. Puerto Clock (30 min)

### 2. InMemoryCitaRepository (50–60 min) — reutiliza M14 si existe

### 3. Tests de servicio (60–70 min)

### 4. Commit

`test(m15): fake repo y reloj`
""",
    )
)

LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Tests de integración con persistencia",
        horas=5.0,
        semana=2,
        lectura="Tests de integración DB; isolation",
        evidencia="tests/integration/ con Postgres o SQLite documentado",
        _lectura_corta="Integración: repository real contra DB de prueba",
        _hecho="""1. Al menos 1 test de integración que escribe/lee cita en DB de prueba (Docker PG, Testcontainers, o SQLite — documenta cuál).
2. Setup/teardown o transacciones que no dejen basura.
3. Commit `test(m15): integracion persistencia`.""",
        _errores="""- Usar la DB de desarrollo con datos del design partner.
- Tests de integración mezclados sin tag/carpeta.
- Sin documentar cómo levantar la DB en README.""",
        siguiente="[L07 — Tests HTTP de API — auth y validación](L07-tests-http-de-api-auth-y-validacion.md)",
        body=r"""
# L06 — Tests de integración con persistencia

**~5.0 h · Semana 2**

El fake miente a veces. Un test real de persistencia ancla el Repository Postgres (o el que elegiste en M13).

## Objetivo

Carpeta `tests/integration/` con evidencia P1 (segunda capa).

## Pasos (hazlos en orden)

### 1. Elige estrategia (40 min)

Documenta en README: Docker compose service `db_test`, o SQLite solo para spike.

### 2. Test save/find (80–100 min)

### 3. Script npm `test:integration` (30 min)

### 4. Commit

`test(m15): integracion persistencia`
""",
    )
)

LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Tests HTTP de API — auth y validación",
        horas=5.0,
        semana=2,
        lectura="Supertest/fetch contra app; 401 y 400",
        evidencia="tests/http/ login/citas 401 y 400",
        _lectura_corta="HTTP tests: sin auth → 401; body inválido → 400",
        _hecho="""1. App mínima (Express/Fastify/Hono o spike) con ruta protegida de citas.
2. Tests automatizados: sin cookie/token → 401; body inválido → 400.
3. Commit `test(m15): http auth y validacion`.""",
        _errores="""- Probar solo el happy path.
- Servidor global compartido sin aislamiento.
- Hardcodear secrets de prod.""",
        siguiente="[L08 — IDOR y roles — casos 403](L08-idor-y-roles-casos-403.md)",
        body=r"""
# L07 — Tests HTTP de API — auth y validación

**~5.0 h · Semana 2**

La pirámide necesita la capa que habla HTTP: el contrato que el front verá.

## Objetivo

Tests 401/400 contra API de prueba del piloto.

## Pasos (hazlos en orden)

### 1. Mini app (60–80 min)

Si M17 no existe, spike en `projects/m15-calidad/src/http/`.

### 2. Casos (60–70 min)

Tabla de la ficha M15: feliz opcional hoy; 401 y 400 obligatorios.

### 3. Commit

`test(m15): http auth y validacion`
""",
    )
)

LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="IDOR y roles — casos 403",
        horas=5.0,
        semana=2,
        lectura="IDOR; autorización por dueño/rol",
        evidencia="tests HTTP 403 IDOR + rol insuficiente",
        _lectura_corta="403: IDOR de cita ajena y rol staff vs owner",
        _hecho="""1. Test: usuario A no lee/modifica cita de B → 403 (o 404 documentado).
2. Test: rol insuficiente → 403.
3. Commit `test(m15): idor y roles 403`.""",
        _errores="""- Devolver 200 con body vacío (silencio peligroso sin política).
- Mensajes que revelan existencia de recurso ajeno sin decisión consciente.
- Solo test de UI ocultando botón.""",
        siguiente="[L09 — Workflow GitHub Actions — esqueleto](L09-workflow-github-actions-esqueleto.md)",
        body=r"""
# L08 — IDOR y roles — casos 403

**~5.0 h · Semana 2**

Hilo seguridad: el piloto single-tenant aún puede tener IDOR entre usuarios/roles.

## Objetivo

Automatizar 403 (P1 capa API completa).

## Pasos (hazlos en orden)

### 1. Fixtures de dos usuarios (40 min)

### 2. Tests IDOR + rol (80–100 min)

### 3. Actualiza piramide.md (20 min)

### 4. Commit

`test(m15): idor y roles 403`
""",
    )
)

LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Workflow GitHub Actions — esqueleto",
        horas=5.0,
        semana=3,
        lectura="GitHub Actions basics; ci.yml",
        evidencia=".github/workflows/m15-ci.yml (o documentado) verde",
        _lectura_corta="Workflow CI: checkout, node, npm test",
        _enlace_titulo="GitHub Actions — Quickstart",
        _enlace="https://docs.github.com/es/actions/writing-workflows/quickstart",
        _hecho="""1. Workflow YAML que corre en push/PR e instala deps + `npm test` en `projects/m15-calidad` (o monorepo doc).
2. README M15 enlaza al workflow / badge path.
3. Commit `ci(m15): workflow esqueleto github actions`.""",
        _errores="""- Workflow solo en docs sin YAML.
- `npm test` en raíz sin `working-directory`.
- Secrets pegados en el YAML.""",
        siguiente="[L10 — Lint y formato en pipeline](L10-lint-y-formato-en-pipeline.md)",
        body=r"""
# L09 — Workflow GitHub Actions — esqueleto

**~5.0 h · Semana 3**

P2: CI real. Hoy el esqueleto que falla si los tests fallan.

## Objetivo

`.github/workflows/` con job de test para M15.

## Pasos (hazlos en orden)

### 1. Escribe YAML (60–70 min)

```yaml
name: m15-ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: projects/m15-calidad
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: npm
          cache-dependency-path: projects/m15-calidad/package-lock.json
      - run: npm ci
      - run: npm test
```

Ajusta si aún no hay lockfile (`npm install`).

### 2. Documenta ruta (30 min)

### 3. Commit + push cuando puedas verificar

`ci(m15): workflow esqueleto github actions`
""",
    )
)

LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Lint y formato en pipeline",
        horas=5.0,
        semana=3,
        lectura="ESLint/Prettier o oxlint; fail on lint",
        evidencia="script lint en CI",
        _lectura_corta="Lint en CI: mismo estándar local y remoto",
        _hecho="""1. Script `npm run lint` local verde.
2. Paso de lint en el workflow (falla el job si lint falla).
3. Commit `ci(m15): lint en pipeline`.""",
        _errores="""- Lint solo warning ignorado.
- Reglas tan estrictas que nadie corre local.
- Formatear en CI sin config en repo.""",
        siguiente="[L11 — npm audit y política de dependencias](L11-npm-audit-y-politica-de-dependencias.md)",
        body=r"""
# L10 — Lint y formato en pipeline

**~5.0 h · Semana 3**

CI sin lint deja pasar basura que los tests no ven.

## Objetivo

Lint (y opcional format check) en local + Actions.

## Pasos (hazlos en orden)

### 1. Config ESLint o equivalente (60–70 min)

### 2. Añade step al workflow (30 min)

### 3. Commit

`ci(m15): lint en pipeline`
""",
    )
)

LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="npm audit y política de dependencias",
        horas=5.0,
        semana=3,
        lectura="npm audit; política high/critical",
        evidencia="audit en CI + docs/politica-deps.md",
        _lectura_corta="Audit en CI; excepciones con ticket/motivo",
        _hecho="""1. `npm audit --audit-level=high` (o equivalente) en workflow o script CI.
2. `docs/politica-deps.md` describe qué hacer con vulns y excepciones.
3. Commit `ci(m15): npm audit y politica deps`.""",
        _errores="""- `--audit-level=critical` sin mirar high.
- Silenciar audit con flag oculto permanente.
- No pinear versiones y vivir en builds flaky.""",
        siguiente="[L12 — Badge README y artefacto de test](L12-badge-readme-y-artefacto-de-test.md)",
        body=r"""
# L11 — npm audit y política de dependencias

**~5.0 h · Semana 3**

El piloto también tiene supply chain. Hoy el audit deja de ser opcional.

## Objetivo

Audit en pipeline + política escrita (P2 completo con lint+test+audit).

## Pasos (hazlos en orden)

### 1. Corre audit local (30 min)

### 2. Añade a CI (40 min)

### 3. política-deps.md (50 min)

### 4. Commit

`ci(m15): npm audit y politica deps`
""",
    )
)

LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Badge README y artefacto de test",
        horas=5.0,
        semana=3,
        lectura="Badges Actions; artifacts opcionales",
        evidencia="README con badge/enlace CI + nota de artefacto",
        _lectura_corta="Visibilidad del pipeline en README M15",
        _hecho="""1. README M15 muestra badge o enlace claro al workflow.
2. Documentas (o configuras) artefacto de reporte de test/coverage opcional.
3. Commit `docs(m15): badge ci y artefacto`.""",
        _errores="""- Badge a repo ajeno.
- Prometer coverage upload sin secretos/config.
- README sin cómo correr tests local.""",
        siguiente="[L13 — Checklist de code review](L13-checklist-de-code-review.md)",
        body=r"""
# L12 — Badge README y artefacto de test

**~5.0 h · Semana 3**

Si el pipeline no se ve, no existe para el equipo-de-uno futuro.

## Objetivo

README con señal de CI + instrucciones locales.

## Pasos (hazlos en orden)

### 1. Badge o enlace (30 min)

### 2. Sección “Cómo correr tests” (40 min)

### 3. Commit

`docs(m15): badge ci y artefacto`
""",
    )
)

LESSONS.append(
    dict(
        id="L13",
        orden=13,
        titulo="Checklist de code review",
        horas=5.0,
        semana=4,
        lectura="Checklist review: calidad + seguridad",
        evidencia="checklist-review.md (P3)",
        _lectura_corta="Checklist PR: tests, auth, secrets, migraciones",
        _hecho="""1. `checklist-review.md` con ítems de estilo, tests, seguridad (auth/IDOR/validación), secrets.
2. Ítems accionables (sí/no), no vagos.
3. Commit `docs(m15): checklist de code review`.""",
        _errores="""- Lista de 80 ítems inusable.
- Cero ítems de seguridad.
- Copiar checklist enterprise sin adaptar al piloto.""",
        siguiente="[L14 — Review simulado en PR o notas](L14-review-simulado-en-pr-o-notas.md)",
        body=r"""
# L13 — Checklist de code review

**~5.0 h · Semana 4**

P3 empieza aquí: lo que mirarás en cada PR del piloto.

## Objetivo

`projects/m15-calidad/checklist-review.md` usable.

## Pasos (hazlos en orden)

### 1. Borrador por secciones (70–90 min)

Estilo · Tests · Authz · Validación · Migraciones · Secrets · Observabilidad mínima.

### 2. Alinea a M13 boundaries (30 min)

### 3. Commit

`docs(m15): checklist de code review`
""",
    )
)

LESSONS.append(
    dict(
        id="L14",
        orden=14,
        titulo="Review simulado en PR o notas",
        horas=5.0,
        semana=4,
        lectura="Aplicar checklist a un cambio real",
        evidencia="review-ejemplo.md o comentarios en PR",
        _lectura_corta="Evidencia de uso del checklist en un cambio",
        _hecho="""1. `review-ejemplo.md` (o captura/enlace PR) aplicando el checklist a un diff tuyo.
2. Al menos 1 hallazgo real o “N/A justificado” por sección de seguridad.
3. Commit `docs(m15): review simulado P3`.""",
        _errores="""- Checklist todo ✓ sin mirar el diff.
- Review de código ajeno inventado.
- Sin enlace al commit/diff revisado.""",
        siguiente="[L15 — Política bug → test el mismo día](L15-politica-bug-test-el-mismo-dia.md)",
        body=r"""
# L14 — Review simulado en PR o notas

**~5.0 h · Semana 4**

La checklist sin uso no cuenta para P3.

## Objetivo

Evidencia de review aplicado.

## Pasos (hazlos en orden)

### 1. Elige un diff (20 min) — idealmente de M14/M15

### 2. Llena review-ejemplo.md (80–100 min)

### 3. Commit

`docs(m15): review simulado P3`
""",
    )
)

LESSONS.append(
    dict(
        id="L15",
        orden=15,
        titulo="Política bug → test el mismo día",
        horas=5.0,
        semana=4,
        lectura="Regresión inmediata; ejemplo real",
        evidencia="docs/bug-test-mismo-dia.md + test de regresión",
        _lectura_corta="Todo bug encontrado genera test el mismo día",
        _hecho="""1. Política escrita en el repo.
2. Al menos un bug (real o inyectado) con test de regresión añadido el mismo día (documentado).
3. Commit `test(m15): regresion bug mismo dia`.""",
        _errores="""- Política sin ejemplo.
- Fix sin test.
- Test que no falla ante el bug.""",
        siguiente="[L16 — Cierre M15 — pipeline, coverage dominio, dominio](L16-cierre-m15-pipeline-coverage-dominio-dominio.md)",
        body=r"""
# L15 — Política bug → test el mismo día

**~5.0 h · Semana 4**

Regla del plan: el bug no se cierra solo con el fix.

## Objetivo

Política + una regresión demostrable.

## Pasos (hazlos en orden)

### 1. Escribe la política (40 min)

### 2. Inyecta o usa un bug (60–80 min)

Red (test falla) → fix → green.

### 3. Commit

`test(m15): regresion bug mismo dia`
""",
    )
)

LESSONS.append(
    dict(
        id="L16",
        orden=16,
        titulo="Cierre M15 — pipeline, coverage dominio, dominio",
        horas=5.0,
        semana=4,
        lectura="Criterios de dominio ficha M15; pipeline verde",
        evidencia="README final P1–P3 + autoevaluación",
        _lectura_corta="Cierre: CI lint+test+audit, coverage dominio, 401/403",
        _hecho="""1. README documenta P1 pirámide, P2 CI, P3 checklist con rutas.
2. Autoevaluación: 401/403 automatizados; coverage enfocado a dominio.
3. Commit `docs(m15): cierre pipeline y criterios de dominio`.""",
        _errores="""- CI roto en main.
- Coverage solo boilerplate.
- Sin enlace a workflow.""",
        siguiente="Materia siguiente: [M16 — IHC](../M16-ihc.md) · L01 en `../M16/`.",
        body=r"""
# L16 — Cierre M15 — pipeline, coverage dominio, dominio

**~5.0 h · Semana 4**

Proyecto: pipeline verde + coverage de negocio + hábitos de review/regresión.

## Objetivo

Cierre evidenciable y handoff a M17/M18.

## Pasos (hazlos en orden)

### 1. Verifica CI localmente (40 min)

lint + test + audit.

### 2. README de cierre (60 min)

### 3. Autoevaluación criterios ficha (40 min)

### 4. Commit

`docs(m15): cierre pipeline y criterios de dominio`
""",
    )
)
