---
id: L16
materia: M03
orden: 16
titulo: Binomial, Pascal y Big-O de funciones propias
horas: 3
semana: 4
lectura: "Rosen Cap. 6.4 (coeficientes binomiales) + repaso complejidad en apuntes"
evidencia: "complejidad.md (5 funciones) + trianguloPascal fila n en counting.ts"
---

# L16 — Binomial, Pascal y Big-O de funciones propias

**~3 h · Semana 4**

Cierras conteo con el triángulo de Pascal y abres **P3**: analizar complejidad de **tus** funciones con argumento de peor caso.

## Objetivo

Relacionar `C(n,k)` con coeficientes binomiales; generar una fila de Pascal; redactar análisis Big-O de 5 funciones propias (incluye las de `sets`, `relations` o `counting`).

## Pasos

### 1. Teorema del binomio (30 min)

En `conteo.md`: `(x+y)^n = ∑_{k=0}^n C(n,k) x^k y^{n-k}` y fila de Pascal como tabla.

### 2. Código Pascal (40 min)

```ts
export function filaPascal(n: number): number[] {
  const row = [1];
  for (let k = 1; k <= n; k++) {
    row[k] = (row[k - 1] * (n - k + 1)) / k;
  }
  return row;
}
```

Test: fila 5 = `[1,5,10,10,5,1]`; `filaPascal(n)[k] === nCk(n,k)` para n ≤ 12.

### 3. complejidad.md (P3) (80–90 min)

Crea `projects/m03-discretas/complejidad.md` con **5** funciones **tuyas** (de este proyecto o escritas para la tarea). Por cada una:

- Código o firma.
- **Peor caso** en términos de `n` (tamaño de entrada).
- Clase Big-O (O, Ω si el libro lo pide) con **justificación** en 3–6 frases (no solo el nombre).
- Un ejemplo de entrada que dispara el peor caso.

Incluye al menos: un bucle simple, un bucle anidado, y algo sobre `Set`/`Map`.

### 4. Demo opcional (30 min)

**Demo 10** (si aún no llegas a 10 en P1): identidad `C(n,k)=C(n-1,k-1)+C(n-1,k)` por argumento combinatorio.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 6.4 (binomio) |
| Ficha M03 | Criterio P3 |

## Hecho cuando

1. `filaPascal` verificada contra `nCk`.
2. `complejidad.md` con 5 análisis completos (peor caso argumentado).
3. No confundes `O(2^n)` con `O(n^2)` en tus propias funciones.

## Errores comunes

- Big-O sin definir qué es `n`.
- “Es lineal” porque el gráfico se ve recto en un rango pequeño.
- Pascal con enteros flotantes sin redondeo (usa división entera cuando aplica).

## Siguiente

[L17 — Grafos: modelo y terminología](L17-grafos-modelo-y-terminologia.md)
