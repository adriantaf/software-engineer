---
id: M15
titulo: Verificación, validación y calidad
etapa: disciplinaria
orden: 15
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Pirámide de tests en el CRM
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

## Cómo estudiar esta materia

- Cada bug encontrado → test de regresión el mismo día (regla del plan).
- Trabaja sobre código real o spike en `projects/m15-calidad/` que refleje endpoints del SRS M12.
- Lee docs oficiales de Vitest / Testing Library el día que los uses.
- La CI debe ser **obligatoria** para merge; no “corro tests a mano cuando me acuerdo”.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Tests | 6–8 | Unit + integration en dominio/API |
| CI | 6–8 | Workflow Actions lint+test+audit |
| Review | 4–6 | Checklist aplicada en un PR real o simulado |
| Retro | 1 | Bug → test de regresión documentado |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Crea evidencia:
   ```bash
   mkdir -p projects/m15-calidad/tests projects/m15-calidad/.github/workflows
   ```
2. Elige una función de dominio (p. ej. `crearCita`, validar solapamiento, calcular duración).
3. Escribe 5 tests en `projects/m15-calidad/tests/`:
   - Camino feliz
   - Regla de negocio violada (duplicado, horario inválido)
   - Sin autenticación (401) si es capa HTTP
   - IDOR o acceso cross-rol (403)
   - Input inválido (400)
4. Documenta la pirámide objetivo en `projects/m15-calidad/piramide.md` (qué va en cada capa).
5. Commit: `test(m15): cinco casos iniciales dominio/auth`.

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

## Lecturas

Canon: *Código limpio* (cap. pruebas) + *El programador pragmático* (testing y acoplamiento) + docs Vitest / Testing Library. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos / docs | Alternativa |
|--------|------------------|-------------|
| 1 | *Código limpio* **cap. 9** (pruebas) + tu `piramide.md` | [Vitest](https://vitest.dev) getting started |
| 2 | Mocks/fakes: docs Vitest mocking + notas pragmáticas | Testing Library si hay UI |
| 3 | GitHub Actions *Quickstart* + checklist review propia | Workflow en el repo |
| 4 | Coverage útil + `npm audit` + tests de seguridad mínimos | OWASP Testing Guide (selecto) |

**Regla:** un bug encontrado → test de regresión el mismo día.

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
