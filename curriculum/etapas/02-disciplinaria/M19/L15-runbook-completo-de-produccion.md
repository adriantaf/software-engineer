---
id: L15
materia: M19
orden: 15
titulo: Runbook completo de producción
horas: 5
semana: 4
lectura: "SRE runbook lite"
evidencia: "projects/m19-ops/runbook.md completo"
---

# L15 — Runbook completo de producción

**~5 h · Semana 4**

## Objetivo

Unificar deploy, rollback, backup, restore, URLs, secretos (referencias), health.

## Por qué importa

Proyecto único M19.

## Conceptos

- runbook
- handoff

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

runbook.md enlazado desde README m19-ops. Índice al inicio.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l15 runbook-completo-de-produccion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | proyecto M19 | — |

## Hecho cuando

1. Runbook navegable.
2. Enlaces internos.
3. URLs prod/staging.

## Errores comunes

- Runbook disperso
- Sin restore

## Siguiente

[L16 — Cierre M19 — checklist pre-demo M22](L16-cierre-m19-checklist-pre-demo-m22.md)
