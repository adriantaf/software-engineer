# Academia de Egreso Competente

Plan de estudios personal de **Adrian Tafoya** para volverse ingeniero de software competente (y base para una empresa de talla mundial), con más práctica y proyectos útiles que una carrera típica.

> "Si puedes imaginarlo, puedes programarlo." — Alejandro Sánchez Taboada

## Diagnóstico (punto de partida)

Nivel real: **pre-junior** (amplitud sin profundidad). No junior todavía. Detalle en [`curriculum/nivel.md`](curriculum/nivel.md).

## Qué hay en este repo

| Ruta | Contenido |
|------|-----------|
| `curriculum/` | Plan: 26 materias, pista ciberseguridad, SaaS Agenda Ops, labs, egreso |
| `academia/` | App web simple (Astro + Tailwind + DaisyUI) para seguir el plan y marcar progreso |
| `progress.json` | Avance commiteable (sincroniza desde la UI) |
| `projects/` | Evidencia y bitácoras |

## Arranque rápido

```bash
cd academia
npm install
npm run dev
```

Abre `http://localhost:4321/software-engineer/` (base de GitHub Pages).

### GitHub Pages

URL: **https://adriantaf.github.io/software-engineer/**

1. Espera a que el workflow *Deploy GitHub Pages* cree/actualice la rama `gh-pages`
2. En el repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch**
3. Branch: **`gh-pages`** / folder: **`/` (root)** → Save
4. Abre la URL de arriba (puede tardar 1–2 minutos la primera vez)

Empieza por **M01**.

## Ritmo

- Meta: **≥ 20 h/semana**
- Inglés en paralelo (Beginner 2 → B1 lectura técnica)
- Si cursas carrera presencial o en línea, esta academia adelanta y profundiza en paralelo

## Reglas

1. No saltes proyectos.
2. Commit semanal de progreso.
3. TypeScript a profundidad primero.
4. Libros en español hasta B1 lectura.
5. Si no está en git, no cuenta.

## Mentoría

Reporta a Cursor: materia + evidencia + duda concreta. Corrección de profesor, no elogios vacíos.

## Egreso

Ver [`curriculum/egreso.md`](curriculum/egreso.md). Meta de dominio: **junior sólido** con producto en producción.
