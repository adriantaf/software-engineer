---
id: L03
materia: M23
orden: 3
titulo: Export de ejemplo y borrador pipeline
horas: 5
semana: 1
lectura: "Reproducibilidad jobs métricas"
evidencia: "projects/m23-ia/metricas/export-ejemplo.csv + pipeline.md"
---

# L03 — Export de ejemplo y borrador pipeline

**~5 h · Semana 1**

## Objetivo

Generar CSV de ejemplo (ficticio o anonimizado) y documentar pipeline extracción → agregación → export.

## Por qué importa

P1 entrega artefactos que M26 puede operar; hoy es diseño ejecutable.

## Conceptos

- Pipeline.
- CSV.
- Job schedule (idea).
- Idempotencia.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Exporta muestra a `projects/m23-ia/metricas/export-ejemplo.csv` (≥5 filas, columnas tenant_id + métricas).

Borrador `projects/m23-ia/metricas/pipeline.md`: pasos, herramienta, frecuencia, owner, enlace script.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l03 export-de-ejemplo-y-borrador-pipeline"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M19 | cron/job | ../../../producto-saas.md |

## Hecho cuando

1. CSV ejemplo.
2. pipeline.md borrador.
3. Script ejecutable o instrucción clara.

## Errores comunes

- CSV con nombres.
- Pipeline ‘manual cuando quiera’.

## Siguiente

[L04 — Cierre semana 1 métricas — P1 avance](L04-cierre-semana-1-metricas-p1-avance.md)
