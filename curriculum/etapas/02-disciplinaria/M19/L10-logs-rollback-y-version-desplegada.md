---
id: L10
materia: M19
orden: 10
titulo: Logs, rollback y versión desplegada
horas: 5
semana: 3
lectura: "Runbook ops"
evidencia: "projects/m19-ops/runbook.md sección rollback"
---

# L10 — Logs, rollback y versión desplegada

**~5 h · Semana 3**

## Objetivo

Documentar dónde ver logs, cómo identificar versión y rollback a imagen/tag anterior.

## Por qué importa

A las 11 p.m. solo cuenta el runbook.

## Conceptos

- rollback
- tag git
- logs PaaS

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

runbook.md: Rollback en ≤10 pasos numerados. Prueba rollback en staging si es seguro.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l10 logs-rollback-y-version-desplegada"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Proveedor | logs | — |
| Catálogo | Entrada M19 | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

1. Rollback documentado.
2. Versión en runbook.
3. Prueba o simulacro.

## Errores comunes

- Rollback ‘redeploy main’ sin tag
- Sin logs

## Siguiente

[L11 — Monitoreo mínimo y alertas manuales](L11-monitoreo-minimo-y-alertas-manuales.md)
