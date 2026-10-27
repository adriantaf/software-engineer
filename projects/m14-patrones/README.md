# M14 — Patrones de software

Carpeta de **evidencia** de esta materia. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Aplicas pocos patrones con justificación (no nombres de adorno) en el dominio del piloto **Vitrina** (pedidos, precios, notificaciones).

## Arranque rápido (L01)

```bash
cd projects/m14-patrones
npm install
npm test
```

Si aún no hay `package.json`, créalo siguiendo la lección L01 (TypeScript strict + Vitest).

## Estructura esperada

```text
src/
  pricing/          ← Strategy (L01)
  notify/           ← Factory (L02)
  calendar/         ← Adapter (L05)
  pedidos/            ← Decorator, Facade, Repository, Service
  events/           ← Observer (L09)
  admin/            ← Command (L10)
  index.ts          ← API pública (L08)
adr/                ← un ADR corto por patrón
docs/
tests/              ← o colocalizados *.test.ts
refactor-notas.md   ← P3
```

## Checklist (Evidencia de hecho)

- **P1 — 3 patrones:** Strategy, Observer y Factory con tests + ADRs.
- **P2 — Repo/Service:** interfaces de dominio separadas de persistencia.
- **P3 — Refactor:** `refactor-notas.md` + diff/commits.
- **Proyecto — ≥5 patrones:** este README índice + ADRs.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M14-patrones.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M14/`
- Bibliografía: `curriculum/bibliografia.md#m14-patrones`
