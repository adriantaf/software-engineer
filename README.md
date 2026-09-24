# Academia de Egreso Competente

Plan de estudios personal de **Adrian Tafoya** para volverse ingeniero de software competente (y base para una empresa de talla mundial). Alineado a **UABC** (*Ingeniero en Software y Tecnologías Emergentes*) y **Tec de Monterrey** (*ITC*), con más práctica y proyectos útiles que una carrera típica.

> "Si puedes imaginarlo, puedes programarlo." — Alejandro Sánchez Taboada

## Diagnóstico (punto de partida)

Nivel real: **pre-junior** (amplitud sin profundidad). No junior todavía. Detalle en [`curriculum/nivel.md`](curriculum/nivel.md).

## Qué hay en este repo

| Ruta | Contenido |
|------|-----------|
| `curriculum/` | Plan universitario: 3 etapas, 25 materias, libros ES, prácticas, proyectos |
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

1. En el repo: **Settings → Pages → Build and deployment → Source: GitHub Actions**
2. El workflow `.github/workflows/deploy-pages.yml` publica en cada push a `main` (y a la rama del PR mientras esté activa).

Empieza por **M01**.

## Ritmo

- Meta: **≥ 20 h/semana**
- Inglés en paralelo (Beginner 2 → B1 lectura técnica)
- Desde febrero: UABC en línea; esta academia adelanta y profundiza

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
