---
id: L12
materia: M15
orden: 12
titulo: Badge README y artefacto de test
horas: 5
semana: 3
lectura: "README pipeline"
evidencia: "projects/m15-calidad/README.md CI"
---

# L12 — Badge README y artefacto de test

**~5 h · Semana 3**

## Objetivo

Enlazar workflow en README; opcional subir resumen de tests como artefacto.

## Por qué importa

El design partner no ve tu CI; tu yo futuro sí necesita el enlace.

## Conceptos

- badge.
- documentación.
- onboarding.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

README: cómo correr tests local vs CI. Captura o enlace Actions.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l12 badge-readme-y-artefacto-de-test"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| GitHub | badges | — |

## Hecho cuando

1. README actualizado.
2. Enlace CI.
3. Cierre semana 3 P2.

## Errores comunes

- CI secreta.
- Sin instrucciones local.

## Siguiente

[L13 — Checklist de code review](L13-checklist-de-code-review.md)
