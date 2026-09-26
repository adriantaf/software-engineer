---
id: L09
materia: M15
orden: 9
titulo: Workflow GitHub Actions — esqueleto
horas: 5
semana: 3
lectura: "Actions quickstart"
evidencia: "projects/m15-calidad/.github/workflows/ci.yml o raíz"
---

# L09 — Workflow GitHub Actions — esqueleto

**~5 h · Semana 3**

## Objetivo

Crear workflow `ci.yml`: checkout, node 20, install, test.

## Por qué importa

CI obligatoria es práctica P2 y base de M17.

## Conceptos

- CI.
- workflow.
- push PR.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Workflow mínimo verde en push. Documenta ruta en README M15.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l09 workflow-github-actions-esqueleto"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| GitHub | Actions docs | — |
| Catálogo | Entrada M15 | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

1. Workflow existe.
2. Verde en main o rama.
3. README enlace.

## Errores comunes

- CI solo local.
- Sin pin de node.

## Siguiente

[L10 — Lint y formato en pipeline](L10-lint-y-formato-en-pipeline.md)
