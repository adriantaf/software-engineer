---
id: L05
materia: M04
orden: 5
titulo: Variables aleatorias y Bernoulli
horas: 5
semana: 2
lectura: "Walpole cap. 5 (Bernoulli) · OpenStax Ch. 4 (Discrete RV)"
evidencia: "projects/m04-stats/src/bernoulli.ts + notas/bernoulli-conversion.md"
---

# L05 — Variables aleatorias y Bernoulli

**~5 h · Semana 2**

Modelas éxito/fracaso (clic, crash, compra) como Bernoulli(p) y comparas simulación con media teórica p.

## Objetivo

Definir variable aleatoria discreta, implementar muestreo Bernoulli y relacionar p con una tasa de conversión.

## Pasos

### 1. Definiciones en nota (30 min)

`notas/bernoulli-conversion.md`: PMF de Bernoulli, soporte {0,1}, parámetro p.

### 2. `src/bernoulli.ts` (60 min)

```ts
export function bernoulli(p: number): 0 | 1 {
  return Math.random() < p ? 1 : 0;
}

export function simularBernoulli(n: number, p: number) {
  const xs: number[] = [];
  for (let i = 0; i < n; i++) xs.push(bernoulli(p));
  const media = xs.reduce((a, b) => a + b, 0) / n;
  return { xs, media };
}
```

Compara media simulada con p para p = 0.07 (conversión típica) y n = 50_000.

### 3. Producto (40 min)

Escribe: si mañana lanzas un botón, ¿qué supuesto Bernoulli estás haciendo? ¿Qué violaría el modelo (mismo usuario muchas veces)?

### 4. Lectura (90 min)

Walpole cap. 5 (inicio, Bernoulli). OpenStax Ch. 4 discrete random variables.

### 5. Commit

```bash
git commit -am "feat(m04): Bernoulli y conversión L05"
```

## Hecho cuando

1. `bernoulli.ts` con simulación y comparación p vs media muestral.
2. Nota con definición y párrafo de producto.
3. Commit.

## Siguiente

[L06 — Distribución binomial: fórmula vs simulación](L06-distribucion-binomial.md)
