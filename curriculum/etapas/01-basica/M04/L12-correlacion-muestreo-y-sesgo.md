---
id: L12
materia: M04
orden: 12
titulo: Correlación, muestreo y sesgo
horas: 5
semana: 3
lectura: "Walpole correlación intro · OpenStax Ch. 2 (correlation)"
evidencia: "projects/m04-stats/src/correlacion.ts + notas/correlacion-no-causalidad.md"
---

# L12 — Correlación, muestreo y sesgo

**~5 h · Semana 3**

Calculas correlación de Pearson entre dos columnas numéricas, escribes **correlación ≠ causalidad** con tu ejemplo y discutes sesgo de muestreo.

## Objetivo

Cerrar P2 (pipeline + tablas + reflexión) y preparar inferencia de la semana 4.

## Pasos

### 1. Correlación (50 min)

`src/correlacion.ts` — función `correlacionPearson(xs, ys)` (covarianza / producto de σ). Aplícala a `pedidos` vs `ingresos_mxn`.

### 2. Nota obligatoria (45 min)

`notas/correlacion-no-causalidad.md`:

```markdown
# Correlación ≠ causalidad

## Mi ejemplo (software o producto)
-

## Tres razones alternativas (confusores)
1.
2.
3.

## Muestreo
¿Mi CSV representa a todos los días/canales? ¿Qué sesgo veo?
```

### 3. Checklist P2 (30 min)

Verifica en `projects/m04-stats/README.md`: limpieza, descriptivos, tablas commiteadas.

### 4. Lectura (90 min)

Correlación y limitaciones. Muestreo aleatorio simple (idea).

### 5. Commit

```bash
git commit -am "feat(m04): correlacion muestreo cierre P2 L12"
```

## Hecho cuando

1. Correlación calculada y reportada con cautela.
2. Nota con ejemplo propio de no causalidad.
3. P2 lista para marcar en UI (pipeline completo).
4. Commit.

## Siguiente

[L13 — Intervalos de confianza interpretados](L13-intervalos-de-confianza.md)
