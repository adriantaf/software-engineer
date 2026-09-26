---
id: L06
materia: M04
orden: 6
titulo: "Distribución binomial: fórmula vs simulación"
horas: 5
semana: 2
lectura: "Walpole cap. 5 (Binomial) · OpenStax Ch. 4"
evidencia: "projects/m04-stats/src/binomial.ts + notas/binomial-ab-test.md"
---

# L06 — Distribución binomial: fórmula vs simulación

**~5 h · Semana 2**

Cuentas éxitos en n ensayos independientes: simulas Binomial(n,p) y contrastas con la PMF teórica en un caso pequeño.

## Objetivo

Implementar “n Bernoullis” y calcular P(X = k) con coeficiente binomial para n ≤ 20; interpretar n como tamaño de muestra de usuarios.

## Pasos

### 1. Simulación (60 min)

`src/binomial.ts`:

```ts
import { bernoulli } from "./bernoulli";

export function binomial(n: number, p: number): number {
  let s = 0;
  for (let i = 0; i < n; i++) s += bernoulli(p);
  return s;
}

export function factorial(n: number): number {
  let f = 1;
  for (let i = 2; i <= n; i++) f *= i;
  return f;
}

export function pmfBinomial(n: number, p: number, k: number): number {
  const comb = factorial(n) / (factorial(k) * factorial(n - k));
  return comb * Math.pow(p, k) * Math.pow(1 - p, n - k);
}
```

Histograma manual: 10_000 valores de `binomial(20, 0.3)` agrupados por k.

### 2. A/B sin heroísmo (45 min)

`notas/binomial-ab-test.md`: “100 usuarios, 12 conversiones en A vs 15 en B” — ¿qué puedes decir **sin** aún hacer test formal? (Solo tamaño de efecto y cautela.)

### 3. Lectura (90 min)

Walpole: Binomial. OpenStax: binomial distribution.

### 4. Commit

```bash
git commit -am "feat(m04): binomial sim y PMF L06"
```

## Hecho cuando

1. Simulación + al menos un k con PMF teórica comparada.
2. Nota A/B cautelosa.
3. Commit.

## Siguiente

[L07 — Esperanza y varianza en código](L07-esperanza-y-varianza.md)
