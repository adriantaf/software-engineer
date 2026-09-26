---
id: L01
materia: M08
orden: 1
titulo: Entorno y binary search con invariante
horas: 5.0
semana: 1
lectura: "CLRS: inserción ordenada / búsqueda binaria"
evidencia: "binary-search.ts + analisis + 2 problemas arrays"
---

# L01 — Entorno y binary search con invariante

**~5.0 h · Semana 1**

M08 conecta teoría CLRS con problemas clasificados y el autocomplete del producto.

## Objetivo

Producir evidencia en `projects/m08-algoritmos/` alineada con: binary-search.ts + analisis + 2 problemas arrays.

## Pasos

### 1. Carpetas (15 min)

```bash
mkdir -p projects/m08-algoritmos/{problems,sorts,dp,autocomplete}
```

### 2. Binary search (90 min)

Reescribe con invariante `[lo,hi]`. Tests: vacío, uno, ausente, duplicados (define convención).

### 3. Análisis (45 min)

`binary-search-analisis.md` — O(log n) peor caso.

### 4. Dos problemas arrays (90 min)

p. ej. two sum, max subarray — sin mirar solución 30 min; luego editorial propia.

### 5. Commit (30 min)

`feat(m08): binary search + 2 problemas`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| CLRS (Cormen et al.) | Sección de la semana en ficha M08 |
| Alternativa | VisuAlgo + notas propias |

## Hecho cuando

1. Evidencia en repo según objetivo.
2. Complejidad escrita.
3. Commit.

## Errores comunes

- Copiar solución sin invariante.
- Confundir O promedio con peor caso.
## Siguiente

[L02 — Notación asintótica Θ, O y Ω](L02-notacion-asintotica-o-y.md)
