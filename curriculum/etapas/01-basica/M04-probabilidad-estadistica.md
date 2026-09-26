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

**En resumen:** usas datos para preguntar mejor (no solo calcular). Simulas, describes un CSV y escribes un informe que un negocio entendería.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Modelar incertidumbre (probabilidad, independencia, Bayes a nivel intro).
2. Simular y contrastar distribuciones discretas y la Normal (intuición).
3. Calcular e interpretar descriptivos, correlación y muestreo con cuidado.
4. Comunicar hallazgos en un informe con limitaciones (sin overclaim).

## Cómo estudiar esta materia (lecciones)

M04 sigue el formato de lecciones cortas y completas (como M01): marcas una a una en la UI.

1. Abre las lecciones **en orden** (L01 → L16).
2. Cada lección trae objetivo, pasos, lectura de libro y criterio “Hecho cuando”.
3. Marca la lección solo si cumple ese criterio.
4. Las **prácticas / proyecto** de abajo exigen evidencia en `projects/m04-stats/`.
5. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Probabilidad | 6–8 | L01–L04, simulaciones TS |
| Distribuciones | 6–8 | L05–L08, contrastar teoría vs simulación |
| Descriptiva + muestreo | 6–8 | L09–L12, CSV real, gráficos |
| Informe + inferencia | 6–8 | L13–L16, IC/hipótesis + `informe.md` |
| Retro | 1 | Correlación ≠ causalidad (ejemplo tuyo) |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia en `projects/m04-stats/`). No saltes la lectura de esa lección.

## Lecciones

### Semana 1 — Probabilidad y producto (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Proyecto M04 y simulación de moneda](M04/L01-proyecto-m04-y-simulacion-moneda.md) | 5 |
| L02 | [Eventos, reglas y frecuentismo](M04/L02-eventos-y-probabilidad-basica.md) | 5 |
| L03 | [Independencia y probabilidad condicional](M04/L03-independencia-y-condicional.md) | 5 |
| L04 | [Bayes intro para decisiones de producto](M04/L04-bayes-intro-producto.md) | 5 |

### Semana 2 — Distribuciones (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Variables aleatorias y Bernoulli](M04/L05-variable-aleatoria-bernoulli.md) | 5 |
| L06 | [Distribución binomial: fórmula vs simulación](M04/L06-distribucion-binomial.md) | 5 |
| L07 | [Esperanza y varianza en código](M04/L07-esperanza-y-varianza.md) | 5 |
| L08 | [Normal, z-scores y preview del TCL](M04/L08-normal-intuicion-y-clt.md) | 5 |

### Semana 3 — Descriptiva, visualización y muestreo (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [Descriptivos y primer pipeline CSV](M04/L09-descriptivos-y-csv.md) | 5 |
| L10 | [Dispersión, percentiles y outliers](M04/L10-dispersion-percentiles-outliers.md) | 5 |
| L11 | [Visualización e histogramas para no técnicos](M04/L11-visualizacion-e-histogramas.md) | 5 |
| L12 | [Correlación, muestreo y sesgo](M04/L12-correlacion-muestreo-y-sesgo.md) | 5 |

### Semana 4 — Inferencia e informe (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L13 | [Intervalos de confianza interpretados](M04/L13-intervalos-de-confianza.md) | 5 |
| L14 | [Hipótesis simple con pregunta de negocio](M04/L14-prueba-de-hipotesis-simple.md) | 5 |
| L15 | [Informe para negocio (`informe.md`)](M04/L15-informe-para-negocio.md) | 5 |
| L16 | [Cierre M04: evidencias y dominio](M04/L16-cierre-m04-evidencias.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Probabilidad y estadística para ingeniería y ciencias* — Walpole, Myers et al. (ed. ES). Alternativa gratis: OpenStax *Introductory Statistics*. Catálogo: [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos (Walpole) | Alternativa (OpenStax) |
|--------|-----------|---------------------|-------------------------|
| 1 | L01–L04 | **Cap. 2** — Probabilidad | **Ch. 3** Probability Topics |
| 2 | L05–L08 | **Caps. 5–6** (selectos) — discretas + Normal intuición | **Ch. 4–6** Discrete / Continuous / Normal |
| 3 | L09–L12 | **Cap. 1** (datos) + descriptivos; muestreo selecto | **Ch. 1–2** + correlación |
| 4 | L13–L16 | **Cap. 8** (IC intro) + **Cap. 9** (hipótesis ligera) + informe | **Ch. 7–9** CLT / CI / Hypothesis (idea) |

**Regla:** cada fórmula del capítulo → una simulación o cálculo en TS en `projects/m04-stats/`.

Dataset sugerido para el proyecto: CSV pequeño (ventas, pedidos) o abierto en [datos.gob.mx](https://datos.gob.mx).

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

## Prácticas

1. **P1:** Simulación en TS que aproxime probabilidades conocidas (moneda, dados).
2. **P2:** Pipeline CSV → limpia → media/mediana/σ → tablas.
3. **P3:** Hipótesis (“¿los viernes hay más pedidos?”) y conclusión cuidadosa.

## Proyecto útil

Informe `projects/m04-stats/informe.md`: pregunta, datos, método, resultado, limitaciones. Se reutiliza en M22 (emprendimiento).

## Errores comunes

- Confundir correlación con causalidad.
- Promediar porcentajes sin ponderar.
- Tirar outliers sin justificar.
- Informe solo con números y sin recomendación accionable.
- Marcar lecciones sin cumplir “Hecho cuando”.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Simulación:** `projects/m04-stats/` con 10_000 lanzamientos y conclusión escrita.
- **P2 — CSV:** Pipeline limpia → tablas descriptivas; notebook o script.
- **P3 — Hipótesis:** Una pregunta de negocio + conclusión cuidadosa (sin overclaim).
- **Proyecto — Informe:** `informe.md`: pregunta, datos, método, resultado, limitaciones.

Detalle y checklist: [`projects/m04-stats/README.md`](../../../projects/m04-stats/README.md).

## Criterios de dominio

- [ ] Escribes explícitamente “correlación ≠ causalidad” con un ejemplo tuyo.
- [ ] Explicas un histograma a un no técnico.
- [ ] Interpretas un intervalo de confianza sin decir “hay 95% de probabilidad de que μ esté ahí”.
- [ ] Tu informe incluye limitaciones y una recomendación accionable.
