---
id: L09
materia: M04
orden: 9
titulo: Descriptivos y primer pipeline CSV
horas: 5
semana: 3
lectura: "Walpole cap. 1 + descriptivos · OpenStax Ch. 1–2"
evidencia: "projects/m04-stats/data/pedidos.csv + src/csv-descriptivos.ts + salida/tabla-descriptivos.md"
---

# L09 — Descriptivos y primer pipeline CSV

**~5 h · Semana 3**

Bajas o inventas un CSV de pedidos diarios, limpias columnas básicas y calculas media, mediana y conteos — inicio formal de **P2**.

## Objetivo

Pipeline reproducible: CSV → parse → `media`/`mediana` → tabla Markdown commiteada.

## Pasos

### 1. Dataset (45 min)

Crea `data/pedidos.csv` con ≥30 filas, columnas sugeridas:

`fecha, pedidos, ingresos_mxn, canal`

O descarga un CSV pequeño de [datos.gob.mx](https://datos.gob.mx) y documenta la fuente en `data/README.md`.

### 2. Parser (60 min)

`src/csv-descriptivos.ts` lee el archivo ( `fs.readFileSync` + split o librería ligera), convierte `pedidos` a número, ignora filas inválidas con log.

### 3. Tabla de salida (40 min)

`salida/tabla-descriptivos.md`:

```markdown
# Descriptivos — pedidos

| Métrica | pedidos | ingresos_mxn |
|---------|---------|--------------|
| n | | |
| media | | |
| mediana | | |
```

### 4. Lectura (90 min)

Walpole cap. 1 (datos) + medidas de tendencia central.

### 5. Commit

```bash
git add projects/m04-stats/data projects/m04-stats/salida projects/m04-stats/src/csv-descriptivos.ts
git commit -m "feat(m04): pipeline CSV descriptivos L09"
```

## Hecho cuando

1. CSV en `data/` con fuente documentada.
2. Script genera tabla con n, media, mediana.
3. Commit.

## Siguiente

[L10 — Dispersión, percentiles y outliers](L10-dispersion-percentiles-outliers.md)
