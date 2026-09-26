---
id: L10
materia: M15
orden: 10
titulo: Lint y formato en pipeline
horas: 5
semana: 3
lectura: "ESLint + Prettier del stack"
evidencia: "ci.yml lint step"
---

# L10 — Lint y formato en pipeline

**~5 h · Semana 3**

## Objetivo

Añadir paso `npm run lint` (o equivalente) que falle CI si hay errores.

## Por qué importa

Estilo consistente reduce ruido en review.

## Conceptos

- lint.
- format.
- fail fast.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Configura lint en spike o enlaza monorepo. Paso en CI documentado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l10 lint-y-formato-en-pipeline"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M15-vv-calidad.md | — |

## Hecho cuando

1. Lint en CI.
2. Fix o suppress justificado.
3. Commit.

## Errores comunes

- lint --fix en CI sin check.
- Desactivar reglas críticas.

## Siguiente

[L11 — npm audit y política de dependencias](L11-npm-audit-y-politica-de-dependencias.md)
