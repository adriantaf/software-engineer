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

# M15 — V&V y calidad

## Por qué existe
Sin tests, cada cambio es miedo. Incluye tests de **auth/autorización** ([hilo seguridad](../../hilos/seguridad.md)).

**En cristiano:** la calidad deja de ser opcional: pirámide de tests, CI y reviews que incluyen seguridad.

## Día 1 (2–3 h)
Elige una función de dominio (crear cita). Escribe 5 tests: feliz, duplicado, sin auth, IDOR, validación.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Tests | 6–8 | Unit/integration en CRM |
| CI | 6–8 | Actions lint+test+audit |
| Review | 4–6 | Checklist aplicada |
| Retro | 1 | Bug → test de regresión |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Temario
Pirámide → mocks/fakes → CI → coverage útil → review checklist.

## Lecturas

Canon: *Código limpio* + *El programador pragmático* + docs Vitest / Testing Library. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos / docs | Alternativa |
|--------|------------------|-------------|
| 1 | CC **cap. 9** (pruebas) + pirámide de tests (artículo/notas M15) | Docs Vitest |
| 2 | Mocks/fakes: docs Vitest mocking + Pragmático (rompe acoplamientos / testing) | Testing Library docs si hay UI |
| 3 | CI: docs de GitHub Actions *Quickstart* + checklist review | Workflow mínimo en el repo |
| 4 | Coverage útil + `npm audit` + tests de seguridad mínimos | — |

**Regla:** un bug encontrado → test de regresión el mismo día.

## Proyecto útil
CI verde + changelog + semver.

## Errores comunes
Tests que solo prueban mocks; CI que puedes saltarte; 0 tests de seguridad.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Pirámide:** Tests en ≥2 capas del CRM.
- **P2 — CI:** Workflow verde en GitHub Actions.
- **P3 — Checklist:** PR review con ítems de seguridad marcados.
- **Proyecto — Pipeline:** Coverage útil en dominio + audit en CI.

## Criterios de dominio
- [ ] Un bug en prod tiene test de regresión al día siguiente.
- [ ] CI corre `audit` o equivalente.
