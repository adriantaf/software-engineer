# M12 — Ingeniería de requerimientos

Carpeta de **evidencia** del SRS de **Agenda Ops** (piloto single-tenant). Si no está en git, no cuenta.

## En resumen

Congelas qué construir: entrevistas, stories y un SRS con seguridad — no pantallas bonitas primero.

## Arranque rápido

```bash
mkdir -p projects/m12-srs/entrevistas
cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
# sigue L01 → guion, notas, problemas, stories, srs-v1.md
```

## Estructura

```
projects/m12-srs/
├── README.md
├── plantilla.md          # IEEE 830 adaptada
├── srs-borrador.md       # trabajo en curso
├── srs-v1.md             # P3 / proyecto — freeze
├── stories.md            # P2 — ≥8 stories
├── problemas.md
├── glosario.md
├── nota-handoff-m13.md
└── entrevistas/          # P1 — guion + notas
    ├── guion-v1.md
    └── notas-YYYY-MM-DD.md
```

## Lecciones → artefactos

| Semana | Lecciones | Qué debe existir aquí |
|--------|-----------|------------------------|
| 1 | L01–L04 | guion, notas, problemas, glosario, contexto SRS |
| 2 | L05–L08 | `stories.md` ≥8 + RNF seguridad |
| 3 | L09–L12 | MoSCoW, RF, `srs-v1.md` freeze, handoff M13 |

## Checklist (Evidencia de hecho)

- **P1 — Entrevista:** `entrevistas/guion-v1.md` + `notas-*.md`.
- **P2 — Stories:** `stories.md` (≥8 con criterios).
- **P3 — SRS:** `srs-v1.md` con ≥3 RNF seguridad/privacidad.
- **Proyecto — SRS Agenda Ops:** carpeta lista para M13/M17.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M12-requerimientos.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M12/`
- Plan: `/materia/M12/`
- Bibliografía: `curriculum/bibliografia.md#m12-requerimientos`
- Producto: `curriculum/producto-saas.md`
- Plantilla: `projects/m12-srs/plantilla.md`
