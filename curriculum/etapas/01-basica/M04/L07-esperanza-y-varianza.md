---
id: L07
materia: M04
orden: 7
titulo: Esperanza y varianza en código
horas: 5
semana: 2
lectura: "Walpole cap. 5 (E[X], Var) · OpenStax Ch. 4–5"
evidencia: "projects/m04-stats/src/stats-basic.ts + notas/esperanza-varianza.md"
---

# L07 — Esperanza y varianza en código

**~5 h · Semana 2**

Calculas E[X] y Var(X) por definición en casos discretos y verificas con simulación; conectas varianza con “ruido” en métricas.

## Objetivo

Implementar `media`, `varianzaMuestral` y comprobar E[X]=np, Var(X)=np(1−p) para Binomial vía Monte Carlo.

## Pasos

### 1. Estadísticos (50 min)

`src/stats-basic.ts` (reutiliza funciones de la ficha M04):

```ts
export function media(xs: number[]): number {
  return xs.reduce((a, b) => a + b, 0) / xs.length;
}

export function varianzaMuestral(xs: number[]): number {
  const m = media(xs);
  return xs.reduce((s, x) => s + (x - m) ** 2, 0) / (xs.length - 1);
}
```

### 2. Verificación Binomial (50 min)

Simula 20_000 valores `binomial(50, 0.2)`; compara media y varianza muestral con 10 y 50×0.2×0.8.

### 3. Nota (40 min)

`notas/esperanza-varianza.md`: por qué dos features con la misma media pueden tener diferente riesgo (varianza en ingresos diarios).

### 4. Lectura (90 min)

Walpole: esperanza y varianza de variables discretas.

### 5. Commit

```bash
git commit -am "feat(m04): media varianza y binomial L07"
```

## Hecho cuando

1. `stats-basic.ts` con media y varianza muestral.
2. Comparación teórica vs simulada documentada.
3. Commit.

## Siguiente

[L08 — Normal, z-scores y preview del TCL](L08-normal-intuicion-y-clt.md)
