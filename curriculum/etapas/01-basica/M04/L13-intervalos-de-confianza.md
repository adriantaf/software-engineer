---
id: L13
materia: M04
orden: 13
titulo: Intervalos de confianza interpretados
horas: 5
semana: 4
lectura: "Walpole cap. 8 (IC media, intro) · OpenStax Ch. 8"
evidencia: "projects/m04-stats/src/ic-media.ts + notas/ic-interpretacion.md"
---

# L13 — Intervalos de confianza interpretados

**~5 h · Semana 4**

Construyes un IC del 95% para la media de pedidos (fórmula con z o t según tu lectura) y practicas la frase correcta de interpretación.

## Objetivo

Calcular IC para μ con tus datos y explicar qué significa “95% de confianza” **sin** decir que μ está dentro con probabilidad 95%.

## Pasos

### 1. Fórmula en nota (30 min)

`notas/ic-interpretacion.md`: IC = x̄ ± z_{0.025} · (s/√n). Frase correcta vs incorrecta (dos ejemplos).

### 2. Código (60 min)

`src/ic-media.ts`: dado array de pedidos, devuelve `{ media, s, n, icBajo, icAlto }` usando z≈1.96 si n≥30.

### 3. Producto (40 min)

“Si el IC de conversión semanal es [4%, 9%], ¿lanzamos el feature?” — respuesta prudente.

### 4. Lectura (90 min)

Walpole cap. 8 (intervalo para la media).

### 5. Commit

```bash
git commit -am "feat(m04): intervalo confianza media L13"
```

## Hecho cuando

1. IC calculado sobre tu CSV.
2. Nota con interpretación correcta.
3. Commit.

## Siguiente

[L14 — Hipótesis simple con pregunta de negocio](L14-prueba-de-hipotesis-simple.md)
