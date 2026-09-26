---
id: L08
materia: M04
orden: 8
titulo: Normal, z-scores y preview del TCL
horas: 5
semana: 2
lectura: "Walpole cap. 6 (Normal, intro) · OpenStax Ch. 6–7"
evidencia: "projects/m04-stats/src/normal-clt.ts + notas/normal-latencia.md"
---

# L08 — Normal, z-scores y preview del TCL

**~5 h · Semana 2**

Intuición de la Normal (sin integral obligatoria): z-score, histograma de medias muestrales y por qué muchas métricas “se parecen” a campana.

## Objetivo

Simular medias de muestras de Bernoulli o uniforme y observar forma aproximadamente normal; interpretar un z-score en latencia de API.

## Pasos

### 1. Z-score (30 min)

`notas/normal-latencia.md`:

\[
z = \frac{x - \mu}{\sigma}
\]

Ejemplo: latencia media histórica 120 ms, σ = 30, hoy 195 ms → z = ?

### 2. TCL preview (70 min)

`src/normal-clt.ts`: bucle que toma 5_000 muestras de tamaño n=30 de `bernoulli(0.3)`, guarda la **media** de cada muestra, imprime histograma de medias (bins en consola o array).

### 3. Lectura (90 min)

Walpole cap. 6 (Normal, tabla Z opcional). OpenStax CLT (Ch. 7 idea).

### 4. Cierre semana 2 (20 min)

Lista en nota qué distribuciones ya simulaste (Bernoulli, Binomial, medias).

### 5. Commit

```bash
git commit -am "feat(m04): CLT preview y z-score L08"
```

## Hecho cuando

1. Script CLT ejecutado con histograma o resumen de medias.
2. Nota con z-score de latencia interpretado (¿raro o no?).
3. Commit.

## Siguiente

[L09 — Descriptivos y primer pipeline CSV](L09-descriptivos-y-csv.md)
