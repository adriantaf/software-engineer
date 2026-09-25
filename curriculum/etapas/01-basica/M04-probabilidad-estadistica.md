---
id: M04
titulo: Probabilidad y estadística aplicada
etapa: basica
orden: 4
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Simular experimentos (moneda, dados) y contrastar con teoría
  - id: p2
    titulo: Estadísticos descriptivos sobre un CSV real
  - id: p3
    titulo: Intervalo de confianza / hipótesis simple interpretada
proyecto:
  id: proj
  titulo: Informe de datos de un negocio o dataset público
---

# M04 — Probabilidad y estadística aplicada

## Por qué existe

Métricas de producto, calidad de software y (más adelante) ML necesitan intuición estadística. Aquí aprendes a **preguntar con datos**, no solo a calcular.

**En cristiano:** usas datos para preguntar mejor (no solo calcular). Simulas, describes un CSV y escribes un informe que un negocio entendería.

## Análogos

- UABC: Probabilidad y Estadística
- Tec: Estadística y manejo de datos

## Objetivos

1. Probabilidad básica y variables aleatorias discretas.
2. Media, mediana, varianza, correlaciones simples.
3. Visualizar e interpretar (no solo calcular).
4. Comunicar hallazgos en un informe claro.

## Cómo estudiar esta materia

- Cada fórmula → una simulación en TypeScript que la “compruebe”.
- Usa datasets reales (pequeños): ventas, clima, CSV abiertos.
- El informe final se escribe como si se lo entregaras a un dueño de negocio.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Probabilidad | 6–8 | Caps. Lecturas + simulación TS |
| Descriptiva | 6–8 | CSV real → media/mediana/σ |
| Informe | 4–6 | `informe.md` con limitaciones |
| Retro | 1 | Correlación ≠ causalidad (ejemplo tuyo) |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)

1. Crea `projects/m04-stats/`.
2. Simula 10_000 lanzamientos de moneda y estima P(cara):
   ```ts
   function lanzar(): "cara" | "cruz" {
     return Math.random() < 0.5 ? "cara" : "cruz";
   }
   ```
3. Compara tu estimación con 0.5. ¿Qué pasa con 100 vs 10_000 lanzamientos?
4. Anota en Markdown: “la ley de los grandes números en mis palabras”.
5. Baja un CSV pequeño (o inventa 30 filas de “pedidos diarios”).

## Ejemplo — media y mediana

```ts
export function media(xs: number[]): number {
  return xs.reduce((a, b) => a + b, 0) / xs.length;
}

export function mediana(xs: number[]): number {
  const s = [...xs].sort((a, b) => a - b);
  const m = Math.floor(s.length / 2);
  return s.length % 2 ? s[m]! : (s[m - 1]! + s[m]!) / 2;
}
```

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Probabilidad, independencia, Bayes intro |
| 2 | Distribuciones (Bernoulli, Binomial, Normal intuición) |
| 3 | Estadística descriptiva + muestreo |
| 4 | Proyecto informe |

## Lecturas

Canon: *Probabilidad y estadística para ingeniería y ciencias* — Walpole, Myers et al. (ed. ES). Alternativa gratis: OpenStax *Introductory Statistics*. Catálogo: [bibliografía](../../bibliografia.md).

| Semana | Capítulos (Walpole) | Alternativa gratis (OpenStax) |
|--------|---------------------|-------------------------------|
| 1 | **Cap. 2** — Probabilidad (eventos, independencia, Bayes intro) | **Ch. 3** Probability Topics |
| 2 | **Caps. 5–6** (selectos) — discretas (Bernoulli/Binomial) + continua/Normal intuición | **Ch. 4–6** Discrete RV / Continuous / Normal |
| 3 | **Cap. 1** (datos) + **Cap. 8** (distribuciones muestrales / IC intro, selecto) + descriptivos | **Ch. 1–2** + **Ch. 7–8** (CLT / Confidence Intervals) |
| 4 | Proyecto informe: aplica caps. de S1–S3; opcional **Cap. 9** (hipótesis de una muestra, lectura ligera) | **Ch. 9** Hypothesis Testing (solo la idea) + CSV de [datos.gob.mx](https://datos.gob.mx) |

**Regla:** cada fórmula del capítulo → una simulación o cálculo en TS en `projects/m04-stats/`.

## Prácticas

1. **P1:** Simulación en TS que aproxime probabilidades conocidas.
2. **P2:** Pipeline CSV → limpia → media/mediana/σ → tablas.
3. **P3:** Hipótesis (“¿los viernes hay más pedidos?”) y conclusión cuidadosa.

## Proyecto útil

Informe `informe.md`: pregunta, datos, método, resultado, limitaciones. Se reutiliza en M22 (emprendimiento).

## Errores comunes

- Confundir correlación con causalidad.
- Promediar porcentajes sin ponderar.
- Tirar outliers sin justificar.
- Informe solo con números y sin recomendación accionable.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Simulación:** `projects/m04-stats/` con 10_000 lanzamientos y conclusión escrita.
- **P2 — CSV:** Pipeline limpia → tablas descriptivas; notebook o script.
- **P3 — Hipótesis:** Una pregunta de negocio + conclusión cuidadosa (sin overclaim).
- **Proyecto — Informe:** `informe.md`: pregunta, datos, método, resultado, limitaciones.

## Criterios de dominio

- [ ] Escribes explícitamente “correlación ≠ causalidad” con un ejemplo tuyo.
- [ ] Explicas un histograma a un no técnico.
