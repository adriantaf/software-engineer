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

Métricas de producto, A/B testing, ML posterior y calidad de software necesitan intuición estadística.

## Análogos

- UABC: Probabilidad y Estadística / Estadística avanzada (parcial)
- Tec: Estadística y manejo de datos

## Objetivos

1. Probabilidad básica y variables aleatorias discretas.
2. Media, mediana, varianza, correlaciones simples.
3. Visualizar e interpretar (no solo calcular).
4. Comunicar hallazgos en un informe claro.

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Probabilidad, independencia, Bayes intro |
| 2 | Distribuciones (Bernoulli, Binomial, Normal intuición) |
| 3 | Estadística descriptiva + muestreo |
| 4 | Proyecto informe |

## Libros (español)

- Texto univ. de probabilidad y estadística (ES) — capítulos selectos.
- *Estadística para administradores* / equivalente introductorio ES.
- Datos: portal datos.gob.mx o datasets abiertos locales.

## Prácticas

1. **P1:** Simulación en TS que aproxime probabilidades conocidas.
2. **P2:** Pipeline: CSV → limpia → media/mediana/σ → gráficos (o tablas ASCII).
3. **P3:** Plantea una hipótesis (“¿los viernes hay más pedidos?”) y concluyes con cuidado.

## Proyecto útil

Elige un negocio hipotético o dataset real (ventas, tráfico web). Entrega `informe.md` con: pregunta, datos, método, resultado, limitaciones. Esto se reutiliza en emprendimiento (M22).

## Criterios de dominio

- [ ] No confundes correlación con causalidad (lo escribes explícitamente).
- [ ] Puedes explicar un histograma a un no técnico.
