---
id: L23
materia: M08
orden: 23
titulo: Dataset Agenda Ops y demo CLI
horas: 5.0
semana: 6
lectura: Dataset realista + CLI de demostración
evidencia: CSV/JSON demo + CLI
---

# L23 — Dataset Agenda Ops y demo CLI

**~5.0 h · Semana 6**

Sin datos y sin demo, el autocomplete no es evidencia de proyecto.

## Objetivo

Cargar un dataset tipo Agenda Ops y exponer un CLI reproducible.

## Pasos

### 1. Dataset (50 min)

`autocomplete/data/servicios.json` (o csv): nombres realistas (corte, barba, tinte…). Genera ≥100 entradas (script corto aceptable).

### 2. Loader (40 min)

Función `loadAndBuild(path)` inserta todos los términos.

### 3. CLI (70 min)

`autocomplete/cli.ts`:

```bash
npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json --prefix ti --k 5
```

### 4. Latencia (40 min)

Cronometra suggest en frío/caliente; pega ms en `autocomplete/README.md` junto a N y estructura.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/autocomplete
git commit -m "feat(m08): dataset y CLI autocomplete"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Cargar N términos; latencia de suggest en máquina local | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Dataset `autocomplete/data/` (CSV o JSON) con clientes/servicios demo (≥100 filas; ideal ≥1000).
2. CLI `npx tsx autocomplete/cli.ts --prefix cor` (o similar) imprime sugerencias.
3. README autocomplete con comando y nota de latencia; commit `feat(m08): dataset y CLI autocomplete`.

## Errores comunes

- Dataset de 5 filas presentado como demo seria.
- CLI sin documentar en README.
- Medir latencia una sola vez con N minúscula y generalizar.

## Siguiente

[L24 — Cierre M08 y evidencias](L24-cierre-m08-y-evidencias.md)
