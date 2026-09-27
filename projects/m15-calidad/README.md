# M15 — Verificación, validación y calidad

Carpeta de **evidencia** de esta materia. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

La calidad deja de ser opcional: pirámide de tests, CI y reviews que incluyen seguridad en el piloto **Vitrina**.

## Arranque rápido (L01)

```bash
cd projects/m15-calidad
npm install
npm test
```

## Estructura esperada

```text
src/domain/           ← reglas puras (L02)
src/application/      ← services + fakes (L05)
src/http/             ← spike API para tests 401/403 (L07–L08)
tests/
  domain/
  integration/        ← L06
  http/               ← L07–L08
piramide.md           ← L01
checklist-review.md   ← L13 / P3
docs/
```

## Cómo correr

| Script | Qué hace |
|--------|----------|
| `npm test` | Vitest unitario |
| `npm run test:cov` | Coverage enfocado a `src/domain` |
| `npm run lint` | ESLint (L10) |

CI: documenta el workflow en README cuando completes L09–L12 (ruta típica `.github/workflows/m15-ci.yml`).

## Checklist (Evidencia de hecho)

- **P1 — Pirámide:** `piramide.md` + tests en ≥2 capas.
- **P2 — CI:** workflow verde (enlace aquí).
- **P3 — Checklist:** `checklist-review.md` + evidencia de uso.
- **Proyecto — Pipeline:** coverage de dominio + audit en CI.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M15-vv-calidad.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M15/`
- Bibliografía: `curriculum/bibliografia.md#m15-v-v-y-calidad`
