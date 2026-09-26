---
id: L04
materia: M04
orden: 4
titulo: Bayes intro para decisiones de producto
horas: 5
semana: 1
lectura: "Walpole cap. 2 (Bayes) · OpenStax Ch. 3 (Bayes section)"
evidencia: "projects/m04-stats/src/bayes-spam.ts + notas/bayes-producto.md"
---

# L04 — Bayes intro para decisiones de producto

**~5 h · Semana 1**

Aplicas el teorema de Bayes en un mini escenario (spam, fraude o diagnóstico de bug) y cierras la semana 1 con evidencia P1 casi lista.

## Objetivo

Calcular un posterior P(causa|evidencia) con números concretos y explicar por qué el prior importa en alertas de monitoring.

## Teorema (recordatorio)

\[
P(H|E) = \frac{P(E|H)\,P(H)}{P(E)}
\]

En código suele ser más claro con una tabla o con conteos.

## Pasos

### 1. Ejemplo numérico clásico (40 min)

Prior P(spam) = 0.4. Si es spam, P(palabra “gratis”|spam) = 0.8; si no, 0.1. Calcula P(spam|“gratis”) con Bayes. Haz el mismo cálculo en una hoja antes de codear.

### 2. `src/bayes-spam.ts` (60 min)

```ts
export function bayes(
  pH: number,
  pEH: number,
  pENotH: number,
): number {
  const pE = pEH * pH + pENotH * (1 - pH);
  if (pE === 0) return NaN;
  return (pEH * pH) / pE;
}
```

Exporta el ejemplo numérico como test o `console.assert` aproximado.

### 3. Traducción a producto (45 min)

`notas/bayes-producto.md`:

```markdown
# Bayes en alertas

## Escenario
Alerta de error 500: prior de incidente real, tasa de falsos positivos del umbral.

## Posterior después de 3 alertas seguidas
-

## Decisión
¿Silenciar, escalar o investigar? (1 párrafo, sin ML)
```

### 4. Cierre P1 (30 min)

Revisa checklist P1 en `projects/m04-stats/README.md`:

- Moneda 10k ✓ (L01)
- Otro experimento (dado o Bayes) ✓
- Conclusión escrita ✓

Si falta algo, complétalo antes de marcar P1 en la UI.

### 5. Lectura (50 min)

Walpole: teorema de Bayes y ejercicios cortos (2–3).

### 6. Commit

```bash
git commit -am "feat(m04): Bayes intro y cierre semana 1"
```

## Lectura de esta lección

| Fuente | Foco |
|--------|------|
| Walpole | Cap. 2 — Bayes |
| OpenStax | Ch. 3 — Bayes’ theorem |

## Hecho cuando

1. `bayes-spam.ts` implementa `bayes` y un ejemplo numérico verificado.
2. Nota con escenario de alertas y decisión.
3. Evidencia P1 revisada (moneda + segundo experimento + texto).
4. Commit.

## Errores comunes

- Ignorar el prior cuando la evidencia es rara pero dramática.
- Marcar P1 sin 10_000 lanzamientos documentados.

## Siguiente

[L05 — Variables aleatorias y Bernoulli](L05-variable-aleatoria-bernoulli.md)
