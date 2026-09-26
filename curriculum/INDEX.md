# Plan de Ingeniería de Software

Plan de estudios personal de ingeniería de software, con prácticas evaluables, proyectos útiles y rúbrica de egreso.

## Objetivo

Egresar **competente**: poder diseñar, construir, probar, desplegar y mantener software real, y que el conocimiento no sea el freno principal para crear lo que imagines (con tiempo y recursos).

> "Si puedes imaginarlo, puedes programarlo." — Alejandro Sánchez Taboada

## Diagnóstico inicial (Adrian, 2026)

- **Nivel real:** pre-junior / amplitud sin profundidad.
- Conoces superficies (HTML/CSS/JS, React, Astro, Express básico, Flutter, MySQL/SQLite, Electron).
- Falta ciclo completo de ingeniería, datos sólidos, testing, redes/SO, algoritmos y producto.
- Bektor sin clientes = problema de oferta/ventas, no de maquetado.
- **No te presentes como junior** hasta tener evidencia de producción + tests + deploy.

## Ritmo

- Meta: **≥ 20 horas / semana**.
- Inglés en paralelo (curso actual → B1 lectura técnica en 12–24 meses).
- Si cursas universidad en paralelo: este plan **adelanta y profundiza**; no compite.

## Estructura (3 etapas, 27 materias)

1. [Etapa Básica](etapas/01-basica/README.md) — M01–M06 (~4–5 meses)
2. [Etapa Disciplinaria](etapas/02-disciplinaria/README.md) — M07–M20 + **M27** (~12–14 meses)
3. [Etapa Terminal](etapas/03-terminal/README.md) — M21–M26 (~7–9 meses)

**Pista de ciberseguridad:** [M10](etapas/02-disciplinaria/M10-redes.md) → [M18 AppSec](etapas/02-disciplinaria/M18-seguridad.md) → [M25](etapas/03-terminal/M25-ciberseguridad-aplicada.md) · [Hilo seguridad](hilos/seguridad.md)

**Producto / capstone:** SaaS vertical [**Agenda Ops**](producto-saas.md) (M12→M26) · [Hilo producto](hilos/producto.md)

Ver también:

- [Cómo estudiar](como-estudiar.md) ← léelo antes de M01
- [Instalar en iPhone (PWA)](instalar-iphone.md) — icono + offline
- [Glosario](glosario.md) — siglas con definición en español
- [Bibliografía](bibliografia.md) — libros + alternativa gratis
- [Producto SaaS](producto-saas.md)
- [Hilo producto](hilos/producto.md) — artefactos M12→M26
- [Filosofía](filosofia.md) — mejor que la escuela tradicional
- [Labs (índice)](labs/README.md)
- [Niveles y criterios](nivel.md)
- [Rúbrica de egreso](egreso.md)

## Reglas de oro

1. **No saltes proyectos.** La práctica y el proyecto cierran la materia.
2. **Evidencia en git.** Commit semanal de progreso (`progress.json` + repos de proyectos).
3. **Un lenguaje a profundidad primero:** TypeScript (escala a web, backend e IA tooling).
4. **Libros en español** mientras el inglés no esté en B1 lectura técnica.
5. **Tutoriales no cuentan como dominio.** Debes poder explicar y construir sin mirar el video.
6. Reporta a tu mentor (Cursor) con: materia + qué hiciste + enlace/código + dudas concretas.

## Cómo usar este plan

```bash
cd academia
npm install
npm run dev
```

Abre el dashboard, sigue la materia actual y marca prácticas/proyectos. El avance se guarda en el navegador y puedes sincronizarlo a `progress.json` en la raíz del repo.
