---
id: L10
materia: M04
orden: 10
titulo: Dispersión, percentiles y outliers
horas: 5
semana: 3
lectura: "Walpole descriptivos (dispersión) · OpenStax Ch. 2"
evidencia: "projects/m04-stats/src/percentiles.ts + salida/dispersion.md"
---

# L10 — Dispersión, percentiles y outliers

**~5 h · Semana 3**

Añades desviación estándar, IQR y regla de outliers; decides qué hacer con un día “Black Friday” en tus datos.

## Objetivo

Extender el pipeline con σ, p25/p75 y documentar una decisión sobre outliers (mantener, etiquetar o excluir con justificación).

## Pasos

### 1. Funciones (60 min)

`src/percentiles.ts`: percentil empírico (ordenar + interpolación simple). Usa `varianzaMuestral` de L07 para σ.

### 2. Informe corto (50 min)

`salida/dispersion.md`: rango, σ, IQR, lista de fechas outlier (si hay).

### 3. Decisión de negocio (30 min)

Párrafo: “Si informo media de pedidos al dueño, ¿incluyo el outlier?” — consecuencias de cada opción.

### 4. Lectura (90 min)

Desviación, coeficiente de variación (si aparece en Walpole).

### 5. Commit

```bash
git commit -am "feat(m04): dispersion percentiles L10"
```

## Hecho cuando

1. `dispersion.md` con σ e IQR.
2. Decisión sobre outliers justificada.
3. Commit.

## Siguiente

[L11 — Visualización e histogramas para no técnicos](L11-visualizacion-e-histogramas.md)
