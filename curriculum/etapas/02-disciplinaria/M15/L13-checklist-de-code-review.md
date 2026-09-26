---
id: L13
materia: M15
orden: 13
titulo: Checklist de code review
horas: 5
semana: 4
lectura: "Checklist propio + seguridad"
evidencia: "projects/m15-calidad/checklist-review.md"
---

# L13 — Checklist de code review

**~5 h · Semana 4**

## Objetivo

Redactar checklist PR: estilo, tests, migraciones, secrets, auth, IDOR.

## Por qué importa

P3 exige aplicarlo en un PR real o simulado.

## Conceptos

- review.
- checklist.
- seguridad.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥15 ítems verificables. Incluye “¿hay test de regresión?” y “¿validación server?”.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l13 checklist-de-code-review"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Hilo | seguridad.md | Código limpio |

## Hecho cuando

1. checklist-review.md.
2. Ítems seguridad.
3. Commit.

## Errores comunes

- Checklist vago.
- Sin ítems auth.

## Siguiente

[L14 — Review simulado en PR o notas](L14-review-simulado-en-pr-o-notas.md)
