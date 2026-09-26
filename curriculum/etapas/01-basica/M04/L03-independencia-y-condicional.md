---
id: L03
materia: M04
orden: 3
titulo: Independencia y probabilidad condicional
horas: 5
semana: 1
lectura: "Walpole cap. 2 (condicional, independencia) · OpenStax Ch. 3"
evidencia: "projects/m04-stats/src/condicional.ts + notas/independencia-producto.md"
---

# L03 — Independencia y probabilidad condicional

**~5 h · Semana 1**

Calculas P(A|B), distingues independencia de “no correlación visual” y evitas el error base-rate en decisiones de producto.

## Objetivo

Simular o calcular un ejemplo de P(A|B) y documentar un caso donde asumir independencia rompe un funnel o un modelo de riesgo.

## Idea clave

**Condicional:** restringes el espacio a lo que ya pasó (B).  
**Independencia:** P(A|B) = P(A) — saber B no cambia A.

En funnels: “¿compró dado que abrió el carrito?” es condicional, no marginal.

## Pasos

### 1. Tabla de contingencia pequeña (45 min)

Inventa o usa datos de ejemplo (30 sesiones):

| | Compra (C) | No compra |
|---|------------|-----------|
| Vio promo (V) | 8 | 12 |
| No vio promo | 2 | 8 |

Calcula a mano:

- P(C)
- P(C|V)
- P(C|¬V)

¿V “ayuda”? Compara condicionales, no solo totales.

### 2. Código de verificación (50 min)

`src/condicional.ts` — funciones:

```ts
export function pCondicional(
  cuentaAB: number,
  cuentaB: number,
): number {
  if (cuentaB === 0) return NaN;
  return cuentaAB / cuentaB;
}
```

Opcional: simula dos monedas independientes y estima P(segunda cara | primera cara) ≈ 0.5.

### 3. Nota de producto (40 min)

`notas/independencia-producto.md`:

```markdown
# Independencia vs condicional

## Ejemplo funnel (tabla arriba)
- P(C|V) =
- Conclusión cauta:

## Caso donde asumir independencia falla
(ej. dispositivo móvil y tipo de usuario)

## Base rate (1 párrafo)
Por qué “el 90% de churners no abrió el email” no implica que el email salve al 90%.
```

### 4. Lectura (60 min)

Walpole: probabilidad condicional, regla del producto, independencia.

### 5. Commit

```bash
git commit -am "docs(m04): condicional e independencia L03"
```

## Lectura de esta lección

| Fuente | Foco |
|--------|------|
| Walpole | Cap. 2 — conditional probability |
| OpenStax | Ch. 3 — conditional / independent events |

## Hecho cuando

1. Tabla y tres probabilidades calculadas (en nota o script).
2. `condicional.ts` con `pCondicional` usado en el ejemplo.
3. Nota con funnel y párrafo base-rate.
4. Commit.

## Errores comunes

- Confundir P(A|B) con P(B|A) (lo arreglas formalmente en L04 con Bayes).
- Decir “independiente” porque dos gráficos “se ven” separados con poca data.

## Siguiente

[L04 — Bayes intro para decisiones de producto](L04-bayes-intro-producto.md)
