---
id: L08
materia: M08
orden: 8
titulo: Tabla P2 sorts en README
horas: 5.0
semana: 2
lectura: Comparativa de ordenamientos P2
evidencia: sorts/README.md P2 parcial
---

# L08 — Tabla P2 sorts en README

**~5.0 h · Semana 2**

P2 parcial: tres sorts propios + tabla defendible.

## Objetivo

Publicar `sorts/README.md` comparativo y verificar tests de la carpeta sorts.

## Pasos

### 1. Auditoría (30 min)

```bash
ls sorts/*.ts
npm test
```

### 2. Tabla (70 min)

Columnas: algoritmo | peor | promedio | espacial | estable | cuándo usarlo. Filas: insertion, merge, quick, `Array.sort` (motor).

### 3. Microbench opcional (60 min)

`sorts/bench.ts` N=5_000 — pega números en el README (honestos).

### 4. Enlace raíz (30 min)

Desde `projects/m08-algoritmos/README.md` → sección P2.

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "docs(m08): tabla P2 sorts"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Tabla peor/promedio/espacial/estable por sort | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `sorts/README.md` con tabla insertion/merge/quick (y nativo como referencia).
2. Suite de sorts verde; enlace desde README raíz del proyecto.
3. Commit `docs(m08): tabla P2 sorts`.

## Errores comunes

- Tabla copiada de Internet sin alinear a tu código.
- Omitir estabilidad o memoria.
- Dejar quick sin nota de peor caso.

## Siguiente

[L09 — Hash maps en problemas de conteo](L09-hash-maps-en-problemas-de-conteo.md)
