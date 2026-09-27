# M08 — Análisis de algoritmos

Carpeta de **evidencia** de patrones, sorts, DP y autocomplete Agenda Ops. Si no está en git, no cuenta.

## En resumen

Clasificas problemas por patrón, mides complejidad y construyes autocomplete útil para tu producto.

## Arranque rápido

```bash
cd projects/m08-algoritmos
npm install
npm test
# Demo autocomplete (cuando exista L23):
npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json --prefix ti --k 5
```

Si aún no hay toolchain, L01 te guía (TypeScript strict + Vitest).

## Estructura esperada

```
projects/m08-algoritmos/
├── README.md
├── package.json
├── tsconfig.json
├── indice-patrones.md          # P1 — ≥15 filas al cierre
├── bitacora/                   # cierre-m08.md, semanas opcionales
├── docs/
│   ├── notacion.md
│   ├── analisis-bucles.md
│   └── binary-search-analisis.md
├── src/
│   ├── binary-search.ts
│   └── graph.ts                # BFS/DFS helpers
├── problems/                   # NN-nombre/{enunciado.md,solution.ts,solution.test.ts}
├── sorts/
│   ├── README.md               # P2 tabla comparativa
│   ├── insertion.ts
│   ├── merge.ts
│   ├── quick.ts
│   └── *-analisis.md
├── dp/
│   ├── README.md               # P3 patrones
│   ├── memo-ejemplo.ts
│   ├── bottom-up-ejemplo.ts
│   └── <problema>/             # ×3 con caso base
├── autocomplete/
│   ├── DISENO.md
│   ├── README.md
│   ├── cli.ts
│   ├── data/                   # CSV/JSON Agenda Ops
│   └── src/
└── tests/
```

## Plantilla de problema (P1)

Cada entrada en `problems/`:

1. `enunciado.md` — problema + **complejidad** objetivo  
2. `solution.ts` — TypeScript strict  
3. `solution.test.ts` — ≥3 casos (borde incluido)

## Lecciones → artefactos

| Semana | Lecciones | Qué debe existir aquí |
|--------|-----------|------------------------|
| 1 | L01–L04 | Toolchain, binary search, `docs/notacion.md`, ≥3 problems, índice inicial |
| 2 | L05–L08 | `sorts/` insertion/merge/quick + `sorts/README.md` |
| 3 | L09–L12 | Hash, two pointers, sliding window; índice ≥5 |
| 4 | L13–L16 | BFS/DFS/caminos + problemas grafos |
| 5 | L17–L20 | Memo, bottom-up, 3 DP (P3), catálogo patrones |
| 6 | L21–L24 | Autocomplete DISENO + código + dataset/CLI; índice ≥15; cierre |

## Checklist (Evidencia de hecho)

- **P1 — 15 problemas:** `problems/` + `indice-patrones.md` (≥15).
- **P2 — Sorts:** ≥2 (ideal 3) en `sorts/` + tabla Big-O.
- **P3 — DP intro:** 3 problemas en `dp/` con caso base.
- **Proyecto — Autocomplete:** `autocomplete/` con DISENO, tests, dataset y CLI.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M08-analisis-de-algoritmos.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M08/`
- Producto: `curriculum/producto-saas.md`
- Plan: `/materia/M08/`
